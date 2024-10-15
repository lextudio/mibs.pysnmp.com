# SNMP MIB module (WS-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WS-MGMT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:30 2024
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wsMgmt,) = mibBuilder.importSymbols(
    "WS-SMI",
    "wsMgmt")

(DoActionNow,) = mibBuilder.importSymbols(
    "WS-TYPE-MIB",
    "DoActionNow")


# MODULE-IDENTITY

wsMgmtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1)
)
wsMgmtMib.setRevisions(
        ("2007-01-26 15:15",
         "2006-11-03 14:30",
         "2006-10-06 14:51",
         "2006-09-07 16:09",
         "2006-09-05 16:59",
         "2006-08-19 17:10",
         "2006-06-23 17:30",
         "2006-06-06 10:35",
         "2006-01-06 10:51",
         "2005-12-29 18:44",
         "2005-12-12 13:47",
         "2005-12-05 00:06",
         "2005-11-14 16:57",
         "2005-10-21 16:30",
         "2005-10-20 14:00",
         "2005-09-27 13:27",
         "2005-09-23 16:21",
         "2005-09-22 17:54",
         "2005-09-22 16:25",
         "2005-09-22 14:50",
         "2005-09-21 10:59",
         "2005-09-20 17:25",
         "2005-09-20 11:44",
         "2005-09-19 19:01",
         "2005-09-14 22:11",
         "2005-08-25 11:41",
         "2005-08-18 11:02",
         "2005-08-16 17:20",
         "2005-08-12 14:14",
         "2005-08-12 13:56",
         "2005-07-07 16:12")
)


# Types definitions



class AbbrRowStatus(Integer32):
    """Custom type AbbrRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("createAndGo", 4),
          ("destroy", 6))
    )





class DoActionShowProgress(Integer32):
    """Custom type DoActionShowProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doActionRightNow", 1),
          ("idleState", 2))
    )





class Password(OctetString):
    """Custom type Password based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )





class StaticRowEnable(Integer32):
    """Custom type StaticRowEnable based on Integer32"""
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




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsMgmtReset_ObjectIdentity = ObjectIdentity
wsMgmtReset = _WsMgmtReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 1)
)


class _WsMgmtSystemReset_Type(Integer32):
    """Custom type wsMgmtSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("reset", 1),
          ("shutDown", 2))
    )


_WsMgmtSystemReset_Type.__name__ = "Integer32"
_WsMgmtSystemReset_Object = MibScalar
wsMgmtSystemReset = _WsMgmtSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 1, 1),
    _WsMgmtSystemReset_Type()
)
wsMgmtSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSystemReset.setStatus("current")
_WsMgmtSystemFactoryDefaultCfg_Type = DoActionNow
_WsMgmtSystemFactoryDefaultCfg_Object = MibScalar
wsMgmtSystemFactoryDefaultCfg = _WsMgmtSystemFactoryDefaultCfg_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 1, 2),
    _WsMgmtSystemFactoryDefaultCfg_Type()
)
wsMgmtSystemFactoryDefaultCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSystemFactoryDefaultCfg.setStatus("current")
_WsMgmtSnmp_ObjectIdentity = ObjectIdentity
wsMgmtSnmp = _WsMgmtSnmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 2)
)
_WsMgmtSnmpV2Switch_Type = TruthValue
_WsMgmtSnmpV2Switch_Object = MibScalar
wsMgmtSnmpV2Switch = _WsMgmtSnmpV2Switch_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 2, 1),
    _WsMgmtSnmpV2Switch_Type()
)
wsMgmtSnmpV2Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSnmpV2Switch.setStatus("current")
_WsMgmtSnmpV3Switch_Type = TruthValue
_WsMgmtSnmpV3Switch_Object = MibScalar
wsMgmtSnmpV3Switch = _WsMgmtSnmpV3Switch_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 2, 2),
    _WsMgmtSnmpV3Switch_Type()
)
wsMgmtSnmpV3Switch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSnmpV3Switch.setStatus("current")
_WsMgmtHttp_ObjectIdentity = ObjectIdentity
wsMgmtHttp = _WsMgmtHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 3)
)
_WsMgmtHttpEnable_Type = TruthValue
_WsMgmtHttpEnable_Object = MibScalar
wsMgmtHttpEnable = _WsMgmtHttpEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 3, 1),
    _WsMgmtHttpEnable_Type()
)
wsMgmtHttpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtHttpEnable.setStatus("current")
_WsMgmtHttpsEnable_Type = TruthValue
_WsMgmtHttpsEnable_Object = MibScalar
wsMgmtHttpsEnable = _WsMgmtHttpsEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 3, 2),
    _WsMgmtHttpsEnable_Type()
)
wsMgmtHttpsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtHttpsEnable.setStatus("current")
_WsMgmtHttpTrustpoint_Type = DisplayString
_WsMgmtHttpTrustpoint_Object = MibScalar
wsMgmtHttpTrustpoint = _WsMgmtHttpTrustpoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 3, 3),
    _WsMgmtHttpTrustpoint_Type()
)
wsMgmtHttpTrustpoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtHttpTrustpoint.setStatus("current")
_WsMgmtAlarms_ObjectIdentity = ObjectIdentity
wsMgmtAlarms = _WsMgmtAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4)
)
_WsMgmtAlarmTable_Object = MibTable
wsMgmtAlarmTable = _WsMgmtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wsMgmtAlarmTable.setStatus("current")
_WsMgmtAlarmEntry_Object = MibTableRow
wsMgmtAlarmEntry = _WsMgmtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1)
)
wsMgmtAlarmEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtAlarmIndex"),
)
if mibBuilder.loadTexts:
    wsMgmtAlarmEntry.setStatus("current")


class _WsMgmtAlarmIndex_Type(Unsigned32):
    """Custom type wsMgmtAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_WsMgmtAlarmIndex_Type.__name__ = "Unsigned32"
_WsMgmtAlarmIndex_Object = MibTableColumn
wsMgmtAlarmIndex = _WsMgmtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 1),
    _WsMgmtAlarmIndex_Type()
)
wsMgmtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmIndex.setStatus("current")


class _WsMgmtAlarmSeverity_Type(Integer32):
    """Custom type wsMgmtAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("informational", 3),
          ("major", 1),
          ("normal", 4),
          ("warning", 2))
    )


_WsMgmtAlarmSeverity_Type.__name__ = "Integer32"
_WsMgmtAlarmSeverity_Object = MibTableColumn
wsMgmtAlarmSeverity = _WsMgmtAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 2),
    _WsMgmtAlarmSeverity_Type()
)
wsMgmtAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmSeverity.setStatus("current")
_WsMgmtAlarmTypeID_Type = Unsigned32
_WsMgmtAlarmTypeID_Object = MibTableColumn
wsMgmtAlarmTypeID = _WsMgmtAlarmTypeID_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 3),
    _WsMgmtAlarmTypeID_Type()
)
wsMgmtAlarmTypeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmTypeID.setStatus("current")
_WsMgmtAlarmTypeName_Type = DisplayString
_WsMgmtAlarmTypeName_Object = MibTableColumn
wsMgmtAlarmTypeName = _WsMgmtAlarmTypeName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 4),
    _WsMgmtAlarmTypeName_Type()
)
wsMgmtAlarmTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmTypeName.setStatus("current")
_WsMgmtAlarmTimestamp_Type = DateAndTime
_WsMgmtAlarmTimestamp_Object = MibTableColumn
wsMgmtAlarmTimestamp = _WsMgmtAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 5),
    _WsMgmtAlarmTimestamp_Type()
)
wsMgmtAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmTimestamp.setStatus("current")
_WsMgmtAlarmMessage_Type = DisplayString
_WsMgmtAlarmMessage_Object = MibTableColumn
wsMgmtAlarmMessage = _WsMgmtAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 6),
    _WsMgmtAlarmMessage_Type()
)
wsMgmtAlarmMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmMessage.setStatus("current")
_WsMgmtModuleName_Type = DisplayString
_WsMgmtModuleName_Object = MibTableColumn
wsMgmtModuleName = _WsMgmtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 7),
    _WsMgmtModuleName_Type()
)
wsMgmtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtModuleName.setStatus("current")


class _WsMgmtAlarmStatus_Type(Integer32):
    """Custom type wsMgmtAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acknowledged", 1),
          ("unacknowledged", 2))
    )


_WsMgmtAlarmStatus_Type.__name__ = "Integer32"
_WsMgmtAlarmStatus_Object = MibTableColumn
wsMgmtAlarmStatus = _WsMgmtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 8),
    _WsMgmtAlarmStatus_Type()
)
wsMgmtAlarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtAlarmStatus.setStatus("current")


class _WsMgmtAlarmRowStatus_Type(Integer32):
    """Custom type wsMgmtAlarmRowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("clear", 6))
    )


_WsMgmtAlarmRowStatus_Type.__name__ = "Integer32"
_WsMgmtAlarmRowStatus_Object = MibTableColumn
wsMgmtAlarmRowStatus = _WsMgmtAlarmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 1, 1, 9),
    _WsMgmtAlarmRowStatus_Type()
)
wsMgmtAlarmRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtAlarmRowStatus.setStatus("current")
_WsMgmtClearAllAlarms_Type = DoActionNow
_WsMgmtClearAllAlarms_Object = MibScalar
wsMgmtClearAllAlarms = _WsMgmtClearAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 2),
    _WsMgmtClearAllAlarms_Type()
)
wsMgmtClearAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtClearAllAlarms.setStatus("current")
_WsMgmtAcknowledgeAllAlarms_Type = DoActionNow
_WsMgmtAcknowledgeAllAlarms_Object = MibScalar
wsMgmtAcknowledgeAllAlarms = _WsMgmtAcknowledgeAllAlarms_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 3),
    _WsMgmtAcknowledgeAllAlarms_Type()
)
wsMgmtAcknowledgeAllAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtAcknowledgeAllAlarms.setStatus("current")
_WsMgmtNewAlarmsCount_Type = Unsigned32
_WsMgmtNewAlarmsCount_Object = MibScalar
wsMgmtNewAlarmsCount = _WsMgmtNewAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 4),
    _WsMgmtNewAlarmsCount_Type()
)
wsMgmtNewAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtNewAlarmsCount.setStatus("current")
_WsMgmtTotalAlarmsCount_Type = Unsigned32
_WsMgmtTotalAlarmsCount_Object = MibScalar
wsMgmtTotalAlarmsCount = _WsMgmtTotalAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 5),
    _WsMgmtTotalAlarmsCount_Type()
)
wsMgmtTotalAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtTotalAlarmsCount.setStatus("current")
_WsMgmtTotalAlarmsCountSinceBoot_Type = Unsigned32
_WsMgmtTotalAlarmsCountSinceBoot_Object = MibScalar
wsMgmtTotalAlarmsCountSinceBoot = _WsMgmtTotalAlarmsCountSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 6),
    _WsMgmtTotalAlarmsCountSinceBoot_Type()
)
wsMgmtTotalAlarmsCountSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtTotalAlarmsCountSinceBoot.setStatus("current")
_WsMgmtAlarmsIndexLow_Type = Unsigned32
_WsMgmtAlarmsIndexLow_Object = MibScalar
wsMgmtAlarmsIndexLow = _WsMgmtAlarmsIndexLow_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 7),
    _WsMgmtAlarmsIndexLow_Type()
)
wsMgmtAlarmsIndexLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmsIndexLow.setStatus("current")
_WsMgmtAlarmsIndexHigh_Type = Unsigned32
_WsMgmtAlarmsIndexHigh_Object = MibScalar
wsMgmtAlarmsIndexHigh = _WsMgmtAlarmsIndexHigh_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 8),
    _WsMgmtAlarmsIndexHigh_Type()
)
wsMgmtAlarmsIndexHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtAlarmsIndexHigh.setStatus("current")
_WsMgmCriticalAlarmsCount_Type = Unsigned32
_WsMgmCriticalAlarmsCount_Object = MibScalar
wsMgmCriticalAlarmsCount = _WsMgmCriticalAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 9),
    _WsMgmCriticalAlarmsCount_Type()
)
wsMgmCriticalAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmCriticalAlarmsCount.setStatus("current")
_WsMgmMajorAlarmsCount_Type = Unsigned32
_WsMgmMajorAlarmsCount_Object = MibScalar
wsMgmMajorAlarmsCount = _WsMgmMajorAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 10),
    _WsMgmMajorAlarmsCount_Type()
)
wsMgmMajorAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmMajorAlarmsCount.setStatus("current")
_WsMgmWarningAlarmsCount_Type = Unsigned32
_WsMgmWarningAlarmsCount_Object = MibScalar
wsMgmWarningAlarmsCount = _WsMgmWarningAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 11),
    _WsMgmWarningAlarmsCount_Type()
)
wsMgmWarningAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmWarningAlarmsCount.setStatus("current")
_WsMgmInfoAlarmsCount_Type = Unsigned32
_WsMgmInfoAlarmsCount_Object = MibScalar
wsMgmInfoAlarmsCount = _WsMgmInfoAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 12),
    _WsMgmInfoAlarmsCount_Type()
)
wsMgmInfoAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmInfoAlarmsCount.setStatus("current")
_WsMgmNormalAlarmsCount_Type = Unsigned32
_WsMgmNormalAlarmsCount_Object = MibScalar
wsMgmNormalAlarmsCount = _WsMgmNormalAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 13),
    _WsMgmNormalAlarmsCount_Type()
)
wsMgmNormalAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmNormalAlarmsCount.setStatus("current")
_WsMgmUnacknowledgedCriticalAlarmsCount_Type = Unsigned32
_WsMgmUnacknowledgedCriticalAlarmsCount_Object = MibScalar
wsMgmUnacknowledgedCriticalAlarmsCount = _WsMgmUnacknowledgedCriticalAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 14),
    _WsMgmUnacknowledgedCriticalAlarmsCount_Type()
)
wsMgmUnacknowledgedCriticalAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedCriticalAlarmsCount.setStatus("current")
_WsMgmUnacknowledgedMajorAlarmsCount_Type = Unsigned32
_WsMgmUnacknowledgedMajorAlarmsCount_Object = MibScalar
wsMgmUnacknowledgedMajorAlarmsCount = _WsMgmUnacknowledgedMajorAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 15),
    _WsMgmUnacknowledgedMajorAlarmsCount_Type()
)
wsMgmUnacknowledgedMajorAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedMajorAlarmsCount.setStatus("current")
_WsMgmUnacknowledgedWarningAlarmsCount_Type = Unsigned32
_WsMgmUnacknowledgedWarningAlarmsCount_Object = MibScalar
wsMgmUnacknowledgedWarningAlarmsCount = _WsMgmUnacknowledgedWarningAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 16),
    _WsMgmUnacknowledgedWarningAlarmsCount_Type()
)
wsMgmUnacknowledgedWarningAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedWarningAlarmsCount.setStatus("current")
_WsMgmUnacknowledgedInfoAlarmsCount_Type = Unsigned32
_WsMgmUnacknowledgedInfoAlarmsCount_Object = MibScalar
wsMgmUnacknowledgedInfoAlarmsCount = _WsMgmUnacknowledgedInfoAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 17),
    _WsMgmUnacknowledgedInfoAlarmsCount_Type()
)
wsMgmUnacknowledgedInfoAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedInfoAlarmsCount.setStatus("current")
_WsMgmUnacknowledgedNormalAlarmsCount_Type = Unsigned32
_WsMgmUnacknowledgedNormalAlarmsCount_Object = MibScalar
wsMgmUnacknowledgedNormalAlarmsCount = _WsMgmUnacknowledgedNormalAlarmsCount_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 18),
    _WsMgmUnacknowledgedNormalAlarmsCount_Type()
)
wsMgmUnacknowledgedNormalAlarmsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedNormalAlarmsCount.setStatus("current")
_WsMgmUnacknowledgedCriticalAlarmsCountSinceBoot_Type = Unsigned32
_WsMgmUnacknowledgedCriticalAlarmsCountSinceBoot_Object = MibScalar
wsMgmUnacknowledgedCriticalAlarmsCountSinceBoot = _WsMgmUnacknowledgedCriticalAlarmsCountSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 19),
    _WsMgmUnacknowledgedCriticalAlarmsCountSinceBoot_Type()
)
wsMgmUnacknowledgedCriticalAlarmsCountSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedCriticalAlarmsCountSinceBoot.setStatus("current")
_WsMgmUnacknowledgedMajorAlarmsCountSinceBoot_Type = Unsigned32
_WsMgmUnacknowledgedMajorAlarmsCountSinceBoot_Object = MibScalar
wsMgmUnacknowledgedMajorAlarmsCountSinceBoot = _WsMgmUnacknowledgedMajorAlarmsCountSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 20),
    _WsMgmUnacknowledgedMajorAlarmsCountSinceBoot_Type()
)
wsMgmUnacknowledgedMajorAlarmsCountSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedMajorAlarmsCountSinceBoot.setStatus("current")
_WsMgmUnacknowledgedWarningAlarmsCountSinceBoot_Type = Unsigned32
_WsMgmUnacknowledgedWarningAlarmsCountSinceBoot_Object = MibScalar
wsMgmUnacknowledgedWarningAlarmsCountSinceBoot = _WsMgmUnacknowledgedWarningAlarmsCountSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 21),
    _WsMgmUnacknowledgedWarningAlarmsCountSinceBoot_Type()
)
wsMgmUnacknowledgedWarningAlarmsCountSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedWarningAlarmsCountSinceBoot.setStatus("current")
_WsMgmUnacknowledgedInfoAlarmsCountSinceBoot_Type = Unsigned32
_WsMgmUnacknowledgedInfoAlarmsCountSinceBoot_Object = MibScalar
wsMgmUnacknowledgedInfoAlarmsCountSinceBoot = _WsMgmUnacknowledgedInfoAlarmsCountSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 22),
    _WsMgmUnacknowledgedInfoAlarmsCountSinceBoot_Type()
)
wsMgmUnacknowledgedInfoAlarmsCountSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedInfoAlarmsCountSinceBoot.setStatus("current")
_WsMgmUnacknowledgedNormalAlarmsCountSinceBoot_Type = Unsigned32
_WsMgmUnacknowledgedNormalAlarmsCountSinceBoot_Object = MibScalar
wsMgmUnacknowledgedNormalAlarmsCountSinceBoot = _WsMgmUnacknowledgedNormalAlarmsCountSinceBoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 4, 23),
    _WsMgmUnacknowledgedNormalAlarmsCountSinceBoot_Type()
)
wsMgmUnacknowledgedNormalAlarmsCountSinceBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmUnacknowledgedNormalAlarmsCountSinceBoot.setStatus("current")
_WsMgmtCert_ObjectIdentity = ObjectIdentity
wsMgmtCert = _WsMgmtCert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5)
)
_WsMgmtCertCurrent_ObjectIdentity = ObjectIdentity
wsMgmtCertCurrent = _WsMgmtCertCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2)
)


class _WsMgmtCertCurrentCountry_Type(DisplayString):
    """Custom type wsMgmtCertCurrentCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_WsMgmtCertCurrentCountry_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentCountry_Object = MibScalar
wsMgmtCertCurrentCountry = _WsMgmtCertCurrentCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 1),
    _WsMgmtCertCurrentCountry_Type()
)
wsMgmtCertCurrentCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentCountry.setStatus("obsolete")


class _WsMgmtCertCurrentState_Type(DisplayString):
    """Custom type wsMgmtCertCurrentState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsMgmtCertCurrentState_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentState_Object = MibScalar
wsMgmtCertCurrentState = _WsMgmtCertCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 2),
    _WsMgmtCertCurrentState_Type()
)
wsMgmtCertCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentState.setStatus("obsolete")


class _WsMgmtCertCurrentCity_Type(DisplayString):
    """Custom type wsMgmtCertCurrentCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsMgmtCertCurrentCity_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentCity_Object = MibScalar
wsMgmtCertCurrentCity = _WsMgmtCertCurrentCity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 3),
    _WsMgmtCertCurrentCity_Type()
)
wsMgmtCertCurrentCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentCity.setStatus("obsolete")


class _WsMgmtCertCurrentOrg_Type(DisplayString):
    """Custom type wsMgmtCertCurrentOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCurrentOrg_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentOrg_Object = MibScalar
wsMgmtCertCurrentOrg = _WsMgmtCertCurrentOrg_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 4),
    _WsMgmtCertCurrentOrg_Type()
)
wsMgmtCertCurrentOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentOrg.setStatus("obsolete")


class _WsMgmtCertCurrentOrgUnit_Type(DisplayString):
    """Custom type wsMgmtCertCurrentOrgUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCurrentOrgUnit_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentOrgUnit_Object = MibScalar
wsMgmtCertCurrentOrgUnit = _WsMgmtCertCurrentOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 6),
    _WsMgmtCertCurrentOrgUnit_Type()
)
wsMgmtCertCurrentOrgUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentOrgUnit.setStatus("obsolete")


class _WsMgmtCertCurrentCommonName_Type(DisplayString):
    """Custom type wsMgmtCertCurrentCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCurrentCommonName_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentCommonName_Object = MibScalar
wsMgmtCertCurrentCommonName = _WsMgmtCertCurrentCommonName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 7),
    _WsMgmtCertCurrentCommonName_Type()
)
wsMgmtCertCurrentCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentCommonName.setStatus("obsolete")


class _WsMgmtCertCurrentIssuer_Type(OctetString):
    """Custom type wsMgmtCertCurrentIssuer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 600),
    )


_WsMgmtCertCurrentIssuer_Type.__name__ = "OctetString"
_WsMgmtCertCurrentIssuer_Object = MibScalar
wsMgmtCertCurrentIssuer = _WsMgmtCertCurrentIssuer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 8),
    _WsMgmtCertCurrentIssuer_Type()
)
wsMgmtCertCurrentIssuer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentIssuer.setStatus("obsolete")


class _WsMgmtCertCurrentValidStart_Type(DisplayString):
    """Custom type wsMgmtCertCurrentValidStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCurrentValidStart_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentValidStart_Object = MibScalar
wsMgmtCertCurrentValidStart = _WsMgmtCertCurrentValidStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 9),
    _WsMgmtCertCurrentValidStart_Type()
)
wsMgmtCertCurrentValidStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentValidStart.setStatus("obsolete")


class _WsMgmtCertCurrentValidEnd_Type(DisplayString):
    """Custom type wsMgmtCertCurrentValidEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCurrentValidEnd_Type.__name__ = "DisplayString"
_WsMgmtCertCurrentValidEnd_Object = MibScalar
wsMgmtCertCurrentValidEnd = _WsMgmtCertCurrentValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 10),
    _WsMgmtCertCurrentValidEnd_Type()
)
wsMgmtCertCurrentValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentValidEnd.setStatus("obsolete")
_WsMgmtCertCurrentTrustPoint_Type = DisplayString
_WsMgmtCertCurrentTrustPoint_Object = MibScalar
wsMgmtCertCurrentTrustPoint = _WsMgmtCertCurrentTrustPoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 2, 11),
    _WsMgmtCertCurrentTrustPoint_Type()
)
wsMgmtCertCurrentTrustPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCurrentTrustPoint.setStatus("obsolete")
_WsMgmtCertCreate_ObjectIdentity = ObjectIdentity
wsMgmtCertCreate = _WsMgmtCertCreate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3)
)
_WsMgmtCertFileName_Type = DisplayString
_WsMgmtCertFileName_Object = MibScalar
wsMgmtCertFileName = _WsMgmtCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 2),
    _WsMgmtCertFileName_Type()
)
wsMgmtCertFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertFileName.setStatus("obsolete")


class _WsMgmtCertAction_Type(Integer32):
    """Custom type wsMgmtCertAction based on Integer32"""
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
        *(("createReq", 5),
          ("createSelf", 4),
          ("idle", 6),
          ("install", 3),
          ("query", 1),
          ("remove", 2))
    )


_WsMgmtCertAction_Type.__name__ = "Integer32"
_WsMgmtCertAction_Object = MibScalar
wsMgmtCertAction = _WsMgmtCertAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 3),
    _WsMgmtCertAction_Type()
)
wsMgmtCertAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertAction.setStatus("obsolete")
_WsMgmtCertStatus_Type = DisplayString
_WsMgmtCertStatus_Object = MibScalar
wsMgmtCertStatus = _WsMgmtCertStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 4),
    _WsMgmtCertStatus_Type()
)
wsMgmtCertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertStatus.setStatus("obsolete")


class _WsMgmtCertCountry_Type(DisplayString):
    """Custom type wsMgmtCertCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2),
    )


_WsMgmtCertCountry_Type.__name__ = "DisplayString"
_WsMgmtCertCountry_Object = MibScalar
wsMgmtCertCountry = _WsMgmtCertCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 5),
    _WsMgmtCertCountry_Type()
)
wsMgmtCertCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertCountry.setStatus("obsolete")


class _WsMgmtCertState_Type(DisplayString):
    """Custom type wsMgmtCertState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsMgmtCertState_Type.__name__ = "DisplayString"
_WsMgmtCertState_Object = MibScalar
wsMgmtCertState = _WsMgmtCertState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 6),
    _WsMgmtCertState_Type()
)
wsMgmtCertState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertState.setStatus("obsolete")


class _WsMgmtCertCity_Type(DisplayString):
    """Custom type wsMgmtCertCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsMgmtCertCity_Type.__name__ = "DisplayString"
_WsMgmtCertCity_Object = MibScalar
wsMgmtCertCity = _WsMgmtCertCity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 7),
    _WsMgmtCertCity_Type()
)
wsMgmtCertCity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertCity.setStatus("obsolete")


class _WsMgmtCertOrg_Type(DisplayString):
    """Custom type wsMgmtCertOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertOrg_Type.__name__ = "DisplayString"
_WsMgmtCertOrg_Object = MibScalar
wsMgmtCertOrg = _WsMgmtCertOrg_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 8),
    _WsMgmtCertOrg_Type()
)
wsMgmtCertOrg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertOrg.setStatus("obsolete")


class _WsMgmtCertOrgUnit_Type(DisplayString):
    """Custom type wsMgmtCertOrgUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertOrgUnit_Type.__name__ = "DisplayString"
_WsMgmtCertOrgUnit_Object = MibScalar
wsMgmtCertOrgUnit = _WsMgmtCertOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 9),
    _WsMgmtCertOrgUnit_Type()
)
wsMgmtCertOrgUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertOrgUnit.setStatus("obsolete")


class _WsMgmtCertCommonName_Type(DisplayString):
    """Custom type wsMgmtCertCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCommonName_Type.__name__ = "DisplayString"
_WsMgmtCertCommonName_Object = MibScalar
wsMgmtCertCommonName = _WsMgmtCertCommonName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 10),
    _WsMgmtCertCommonName_Type()
)
wsMgmtCertCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertCommonName.setStatus("obsolete")


class _WsMgmtCertIssuer_Type(DisplayString):
    """Custom type wsMgmtCertIssuer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertIssuer_Type.__name__ = "DisplayString"
_WsMgmtCertIssuer_Object = MibScalar
wsMgmtCertIssuer = _WsMgmtCertIssuer_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 11),
    _WsMgmtCertIssuer_Type()
)
wsMgmtCertIssuer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertIssuer.setStatus("obsolete")


class _WsMgmtCertEmail_Type(DisplayString):
    """Custom type wsMgmtCertEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertEmail_Type.__name__ = "DisplayString"
_WsMgmtCertEmail_Object = MibScalar
wsMgmtCertEmail = _WsMgmtCertEmail_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 12),
    _WsMgmtCertEmail_Type()
)
wsMgmtCertEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertEmail.setStatus("obsolete")


class _WsMgmtCertPwd_Type(DisplayString):
    """Custom type wsMgmtCertPwd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_WsMgmtCertPwd_Type.__name__ = "DisplayString"
_WsMgmtCertPwd_Object = MibScalar
wsMgmtCertPwd = _WsMgmtCertPwd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 13),
    _WsMgmtCertPwd_Type()
)
wsMgmtCertPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertPwd.setStatus("obsolete")


class _WsMgmtCertCompany_Type(DisplayString):
    """Custom type wsMgmtCertCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertCompany_Type.__name__ = "DisplayString"
_WsMgmtCertCompany_Object = MibScalar
wsMgmtCertCompany = _WsMgmtCertCompany_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 14),
    _WsMgmtCertCompany_Type()
)
wsMgmtCertCompany.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertCompany.setStatus("obsolete")


class _WsMgmtCertValidStart_Type(DisplayString):
    """Custom type wsMgmtCertValidStart based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertValidStart_Type.__name__ = "DisplayString"
_WsMgmtCertValidStart_Object = MibScalar
wsMgmtCertValidStart = _WsMgmtCertValidStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 15),
    _WsMgmtCertValidStart_Type()
)
wsMgmtCertValidStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertValidStart.setStatus("obsolete")


class _WsMgmtCertValidEnd_Type(DisplayString):
    """Custom type wsMgmtCertValidEnd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_WsMgmtCertValidEnd_Type.__name__ = "DisplayString"
_WsMgmtCertValidEnd_Object = MibScalar
wsMgmtCertValidEnd = _WsMgmtCertValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 16),
    _WsMgmtCertValidEnd_Type()
)
wsMgmtCertValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertValidEnd.setStatus("obsolete")
_WsMgmtCertTrustPoint_Type = DisplayString
_WsMgmtCertTrustPoint_Object = MibScalar
wsMgmtCertTrustPoint = _WsMgmtCertTrustPoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 3, 17),
    _WsMgmtCertTrustPoint_Type()
)
wsMgmtCertTrustPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertTrustPoint.setStatus("obsolete")
_WsMgmtCertViewTable_Object = MibTable
wsMgmtCertViewTable = _WsMgmtCertViewTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4)
)
if mibBuilder.loadTexts:
    wsMgmtCertViewTable.setStatus("current")
_WsMgmtCertViewEntry_Object = MibTableRow
wsMgmtCertViewEntry = _WsMgmtCertViewEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1)
)
wsMgmtCertViewEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtCertViewTrustpoint"),
    (0, "WS-MGMT-MIB", "wsMgmtCertViewType"),
)
if mibBuilder.loadTexts:
    wsMgmtCertViewEntry.setStatus("current")


class _WsMgmtCertViewTrustpoint_Type(DisplayString):
    """Custom type wsMgmtCertViewTrustpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewTrustpoint_Type.__name__ = "DisplayString"
_WsMgmtCertViewTrustpoint_Object = MibTableColumn
wsMgmtCertViewTrustpoint = _WsMgmtCertViewTrustpoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 1),
    _WsMgmtCertViewTrustpoint_Type()
)
wsMgmtCertViewTrustpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewTrustpoint.setStatus("current")


class _WsMgmtCertViewType_Type(Integer32):
    """Custom type wsMgmtCertViewType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("caCert", 8),
          ("serverCert", 4))
    )


_WsMgmtCertViewType_Type.__name__ = "Integer32"
_WsMgmtCertViewType_Object = MibTableColumn
wsMgmtCertViewType = _WsMgmtCertViewType_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 2),
    _WsMgmtCertViewType_Type()
)
wsMgmtCertViewType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewType.setStatus("current")


class _WsMgmtCertViewSubjectCommonName_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewSubjectCommonName_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectCommonName_Object = MibTableColumn
wsMgmtCertViewSubjectCommonName = _WsMgmtCertViewSubjectCommonName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 3),
    _WsMgmtCertViewSubjectCommonName_Type()
)
wsMgmtCertViewSubjectCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectCommonName.setStatus("current")


class _WsMgmtCertViewSubjectOrgUnit_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectOrgUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewSubjectOrgUnit_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectOrgUnit_Object = MibTableColumn
wsMgmtCertViewSubjectOrgUnit = _WsMgmtCertViewSubjectOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 4),
    _WsMgmtCertViewSubjectOrgUnit_Type()
)
wsMgmtCertViewSubjectOrgUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectOrgUnit.setStatus("current")


class _WsMgmtCertViewSubjectOrg_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewSubjectOrg_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectOrg_Object = MibTableColumn
wsMgmtCertViewSubjectOrg = _WsMgmtCertViewSubjectOrg_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 5),
    _WsMgmtCertViewSubjectOrg_Type()
)
wsMgmtCertViewSubjectOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectOrg.setStatus("current")


class _WsMgmtCertViewSubjectCity_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WsMgmtCertViewSubjectCity_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectCity_Object = MibTableColumn
wsMgmtCertViewSubjectCity = _WsMgmtCertViewSubjectCity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 6),
    _WsMgmtCertViewSubjectCity_Type()
)
wsMgmtCertViewSubjectCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectCity.setStatus("current")


class _WsMgmtCertViewSubjectState_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WsMgmtCertViewSubjectState_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectState_Object = MibTableColumn
wsMgmtCertViewSubjectState = _WsMgmtCertViewSubjectState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 7),
    _WsMgmtCertViewSubjectState_Type()
)
wsMgmtCertViewSubjectState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectState.setStatus("current")


class _WsMgmtCertViewSubjectCountry_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WsMgmtCertViewSubjectCountry_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectCountry_Object = MibTableColumn
wsMgmtCertViewSubjectCountry = _WsMgmtCertViewSubjectCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 8),
    _WsMgmtCertViewSubjectCountry_Type()
)
wsMgmtCertViewSubjectCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectCountry.setStatus("current")


class _WsMgmtCertViewSubjectEmail_Type(DisplayString):
    """Custom type wsMgmtCertViewSubjectEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewSubjectEmail_Type.__name__ = "DisplayString"
_WsMgmtCertViewSubjectEmail_Object = MibTableColumn
wsMgmtCertViewSubjectEmail = _WsMgmtCertViewSubjectEmail_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 9),
    _WsMgmtCertViewSubjectEmail_Type()
)
wsMgmtCertViewSubjectEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewSubjectEmail.setStatus("current")


class _WsMgmtCertViewIssuerCommonName_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewIssuerCommonName_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerCommonName_Object = MibTableColumn
wsMgmtCertViewIssuerCommonName = _WsMgmtCertViewIssuerCommonName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 10),
    _WsMgmtCertViewIssuerCommonName_Type()
)
wsMgmtCertViewIssuerCommonName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerCommonName.setStatus("current")


class _WsMgmtCertViewIssuerOrgUnit_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerOrgUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewIssuerOrgUnit_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerOrgUnit_Object = MibTableColumn
wsMgmtCertViewIssuerOrgUnit = _WsMgmtCertViewIssuerOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 11),
    _WsMgmtCertViewIssuerOrgUnit_Type()
)
wsMgmtCertViewIssuerOrgUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerOrgUnit.setStatus("current")


class _WsMgmtCertViewIssuerOrg_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewIssuerOrg_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerOrg_Object = MibTableColumn
wsMgmtCertViewIssuerOrg = _WsMgmtCertViewIssuerOrg_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 12),
    _WsMgmtCertViewIssuerOrg_Type()
)
wsMgmtCertViewIssuerOrg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerOrg.setStatus("current")


class _WsMgmtCertViewIssuerCity_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WsMgmtCertViewIssuerCity_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerCity_Object = MibTableColumn
wsMgmtCertViewIssuerCity = _WsMgmtCertViewIssuerCity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 13),
    _WsMgmtCertViewIssuerCity_Type()
)
wsMgmtCertViewIssuerCity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerCity.setStatus("current")


class _WsMgmtCertViewIssuerState_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WsMgmtCertViewIssuerState_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerState_Object = MibTableColumn
wsMgmtCertViewIssuerState = _WsMgmtCertViewIssuerState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 14),
    _WsMgmtCertViewIssuerState_Type()
)
wsMgmtCertViewIssuerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerState.setStatus("current")


class _WsMgmtCertViewIssuerCountry_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WsMgmtCertViewIssuerCountry_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerCountry_Object = MibTableColumn
wsMgmtCertViewIssuerCountry = _WsMgmtCertViewIssuerCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 15),
    _WsMgmtCertViewIssuerCountry_Type()
)
wsMgmtCertViewIssuerCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerCountry.setStatus("current")


class _WsMgmtCertViewIssuerEmail_Type(DisplayString):
    """Custom type wsMgmtCertViewIssuerEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertViewIssuerEmail_Type.__name__ = "DisplayString"
_WsMgmtCertViewIssuerEmail_Object = MibTableColumn
wsMgmtCertViewIssuerEmail = _WsMgmtCertViewIssuerEmail_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 16),
    _WsMgmtCertViewIssuerEmail_Type()
)
wsMgmtCertViewIssuerEmail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewIssuerEmail.setStatus("current")
_WsMgmtCertViewValidStart_Type = DisplayString
_WsMgmtCertViewValidStart_Object = MibTableColumn
wsMgmtCertViewValidStart = _WsMgmtCertViewValidStart_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 17),
    _WsMgmtCertViewValidStart_Type()
)
wsMgmtCertViewValidStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewValidStart.setStatus("current")
_WsMgmtCertViewValidEnd_Type = DisplayString
_WsMgmtCertViewValidEnd_Object = MibTableColumn
wsMgmtCertViewValidEnd = _WsMgmtCertViewValidEnd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 4, 1, 18),
    _WsMgmtCertViewValidEnd_Type()
)
wsMgmtCertViewValidEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertViewValidEnd.setStatus("current")
_WsMgmtCertConfigTable_Object = MibTable
wsMgmtCertConfigTable = _WsMgmtCertConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5)
)
if mibBuilder.loadTexts:
    wsMgmtCertConfigTable.setStatus("current")
_WsMgmtCertConfigEntry_Object = MibTableRow
wsMgmtCertConfigEntry = _WsMgmtCertConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1)
)
wsMgmtCertConfigEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtCertConfigTrustpoint"),
)
if mibBuilder.loadTexts:
    wsMgmtCertConfigEntry.setStatus("current")


class _WsMgmtCertConfigTrustpoint_Type(DisplayString):
    """Custom type wsMgmtCertConfigTrustpoint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigTrustpoint_Type.__name__ = "DisplayString"
_WsMgmtCertConfigTrustpoint_Object = MibTableColumn
wsMgmtCertConfigTrustpoint = _WsMgmtCertConfigTrustpoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 1),
    _WsMgmtCertConfigTrustpoint_Type()
)
wsMgmtCertConfigTrustpoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigTrustpoint.setStatus("current")


class _WsMgmtCertConfigKey_Type(DisplayString):
    """Custom type wsMgmtCertConfigKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigKey_Type.__name__ = "DisplayString"
_WsMgmtCertConfigKey_Object = MibTableColumn
wsMgmtCertConfigKey = _WsMgmtCertConfigKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 2),
    _WsMgmtCertConfigKey_Type()
)
wsMgmtCertConfigKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigKey.setStatus("current")


class _WsMgmtCertConfigCommonName_Type(DisplayString):
    """Custom type wsMgmtCertConfigCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigCommonName_Type.__name__ = "DisplayString"
_WsMgmtCertConfigCommonName_Object = MibTableColumn
wsMgmtCertConfigCommonName = _WsMgmtCertConfigCommonName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 3),
    _WsMgmtCertConfigCommonName_Type()
)
wsMgmtCertConfigCommonName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigCommonName.setStatus("current")


class _WsMgmtCertConfigOrgUnit_Type(DisplayString):
    """Custom type wsMgmtCertConfigOrgUnit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigOrgUnit_Type.__name__ = "DisplayString"
_WsMgmtCertConfigOrgUnit_Object = MibTableColumn
wsMgmtCertConfigOrgUnit = _WsMgmtCertConfigOrgUnit_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 4),
    _WsMgmtCertConfigOrgUnit_Type()
)
wsMgmtCertConfigOrgUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigOrgUnit.setStatus("current")


class _WsMgmtCertConfigOrg_Type(DisplayString):
    """Custom type wsMgmtCertConfigOrg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigOrg_Type.__name__ = "DisplayString"
_WsMgmtCertConfigOrg_Object = MibTableColumn
wsMgmtCertConfigOrg = _WsMgmtCertConfigOrg_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 5),
    _WsMgmtCertConfigOrg_Type()
)
wsMgmtCertConfigOrg.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigOrg.setStatus("current")


class _WsMgmtCertConfigCompany_Type(DisplayString):
    """Custom type wsMgmtCertConfigCompany based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigCompany_Type.__name__ = "DisplayString"
_WsMgmtCertConfigCompany_Object = MibTableColumn
wsMgmtCertConfigCompany = _WsMgmtCertConfigCompany_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 6),
    _WsMgmtCertConfigCompany_Type()
)
wsMgmtCertConfigCompany.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigCompany.setStatus("current")


class _WsMgmtCertConfigCity_Type(DisplayString):
    """Custom type wsMgmtCertConfigCity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WsMgmtCertConfigCity_Type.__name__ = "DisplayString"
_WsMgmtCertConfigCity_Object = MibTableColumn
wsMgmtCertConfigCity = _WsMgmtCertConfigCity_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 7),
    _WsMgmtCertConfigCity_Type()
)
wsMgmtCertConfigCity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigCity.setStatus("current")


class _WsMgmtCertConfigState_Type(DisplayString):
    """Custom type wsMgmtCertConfigState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_WsMgmtCertConfigState_Type.__name__ = "DisplayString"
_WsMgmtCertConfigState_Object = MibTableColumn
wsMgmtCertConfigState = _WsMgmtCertConfigState_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 8),
    _WsMgmtCertConfigState_Type()
)
wsMgmtCertConfigState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigState.setStatus("current")


class _WsMgmtCertConfigCountry_Type(DisplayString):
    """Custom type wsMgmtCertConfigCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_WsMgmtCertConfigCountry_Type.__name__ = "DisplayString"
_WsMgmtCertConfigCountry_Object = MibTableColumn
wsMgmtCertConfigCountry = _WsMgmtCertConfigCountry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 9),
    _WsMgmtCertConfigCountry_Type()
)
wsMgmtCertConfigCountry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigCountry.setStatus("current")


class _WsMgmtCertConfigFqdn_Type(DisplayString):
    """Custom type wsMgmtCertConfigFqdn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(9, 64),
    )


_WsMgmtCertConfigFqdn_Type.__name__ = "DisplayString"
_WsMgmtCertConfigFqdn_Object = MibTableColumn
wsMgmtCertConfigFqdn = _WsMgmtCertConfigFqdn_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 10),
    _WsMgmtCertConfigFqdn_Type()
)
wsMgmtCertConfigFqdn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigFqdn.setStatus("current")
_WsMgmtCertConfigIP_Type = IpAddress
_WsMgmtCertConfigIP_Object = MibTableColumn
wsMgmtCertConfigIP = _WsMgmtCertConfigIP_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 11),
    _WsMgmtCertConfigIP_Type()
)
wsMgmtCertConfigIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigIP.setStatus("current")


class _WsMgmtCertConfigEmail_Type(DisplayString):
    """Custom type wsMgmtCertConfigEmail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertConfigEmail_Type.__name__ = "DisplayString"
_WsMgmtCertConfigEmail_Object = MibTableColumn
wsMgmtCertConfigEmail = _WsMgmtCertConfigEmail_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 12),
    _WsMgmtCertConfigEmail_Type()
)
wsMgmtCertConfigEmail.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigEmail.setStatus("current")


class _WsMgmtCertConfigPassword_Type(Password):
    """Custom type wsMgmtCertConfigPassword based on Password"""
    subtypeSpec = Password.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_WsMgmtCertConfigPassword_Type.__name__ = "Password"
_WsMgmtCertConfigPassword_Object = MibTableColumn
wsMgmtCertConfigPassword = _WsMgmtCertConfigPassword_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 13),
    _WsMgmtCertConfigPassword_Type()
)
wsMgmtCertConfigPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigPassword.setStatus("current")
_WsMgmtCertConfigRowStatus_Type = AbbrRowStatus
_WsMgmtCertConfigRowStatus_Object = MibTableColumn
wsMgmtCertConfigRowStatus = _WsMgmtCertConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 5, 1, 14),
    _WsMgmtCertConfigRowStatus_Type()
)
wsMgmtCertConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertConfigRowStatus.setStatus("current")
_WsMgmtCertCreateTable_Object = MibTable
wsMgmtCertCreateTable = _WsMgmtCertCreateTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 6)
)
if mibBuilder.loadTexts:
    wsMgmtCertCreateTable.setStatus("current")
_WsMgmtCertCreateEntry_Object = MibTableRow
wsMgmtCertCreateEntry = _WsMgmtCertCreateEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 6, 1)
)
wsMgmtCertCreateEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtCertConfigTrustpoint"),
)
if mibBuilder.loadTexts:
    wsMgmtCertCreateEntry.setStatus("current")


class _WsMgmtCertCreateStatus_Type(Integer32):
    """Custom type wsMgmtCertCreateStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enrolled", 2),
          ("idle", 1),
          ("notEnrolled", 3))
    )


_WsMgmtCertCreateStatus_Type.__name__ = "Integer32"
_WsMgmtCertCreateStatus_Object = MibTableColumn
wsMgmtCertCreateStatus = _WsMgmtCertCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 6, 1, 1),
    _WsMgmtCertCreateStatus_Type()
)
wsMgmtCertCreateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertCreateStatus.setStatus("current")


class _WsMgmtCertCreateAction_Type(Integer32):
    """Custom type wsMgmtCertCreateAction based on Integer32"""
    defaultValue = 5

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
        *(("delCACert", 4),
          ("delServerCert", 3),
          ("enrollReq", 2),
          ("enrollSelfSigned", 1),
          ("idle", 5))
    )


_WsMgmtCertCreateAction_Type.__name__ = "Integer32"
_WsMgmtCertCreateAction_Object = MibTableColumn
wsMgmtCertCreateAction = _WsMgmtCertCreateAction_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 6, 1, 2),
    _WsMgmtCertCreateAction_Type()
)
wsMgmtCertCreateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtCertCreateAction.setStatus("current")
_WsMgmtCertKeyTable_Object = MibTable
wsMgmtCertKeyTable = _WsMgmtCertKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 7)
)
if mibBuilder.loadTexts:
    wsMgmtCertKeyTable.setStatus("current")
_WsMgmtCertKeyEntry_Object = MibTableRow
wsMgmtCertKeyEntry = _WsMgmtCertKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 7, 1)
)
wsMgmtCertKeyEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtCertKeyLabel"),
)
if mibBuilder.loadTexts:
    wsMgmtCertKeyEntry.setStatus("current")


class _WsMgmtCertKeyLabel_Type(DisplayString):
    """Custom type wsMgmtCertKeyLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_WsMgmtCertKeyLabel_Type.__name__ = "DisplayString"
_WsMgmtCertKeyLabel_Object = MibTableColumn
wsMgmtCertKeyLabel = _WsMgmtCertKeyLabel_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 7, 1, 1),
    _WsMgmtCertKeyLabel_Type()
)
wsMgmtCertKeyLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertKeyLabel.setStatus("current")


class _WsMgmtCertKeySize_Type(Integer32):
    """Custom type wsMgmtCertKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
        ValueRangeConstraint(1024, 2048),
    )


_WsMgmtCertKeySize_Type.__name__ = "Integer32"
_WsMgmtCertKeySize_Object = MibTableColumn
wsMgmtCertKeySize = _WsMgmtCertKeySize_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 7, 1, 2),
    _WsMgmtCertKeySize_Type()
)
wsMgmtCertKeySize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertKeySize.setStatus("current")
_WsMgmtCertKeyRowStatus_Type = AbbrRowStatus
_WsMgmtCertKeyRowStatus_Object = MibTableColumn
wsMgmtCertKeyRowStatus = _WsMgmtCertKeyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 7, 1, 3),
    _WsMgmtCertKeyRowStatus_Type()
)
wsMgmtCertKeyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtCertKeyRowStatus.setStatus("current")


class _WsMgmtCertNumTrustPoint_Type(Integer32):
    """Custom type wsMgmtCertNumTrustPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_WsMgmtCertNumTrustPoint_Type.__name__ = "Integer32"
_WsMgmtCertNumTrustPoint_Object = MibScalar
wsMgmtCertNumTrustPoint = _WsMgmtCertNumTrustPoint_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 5, 8),
    _WsMgmtCertNumTrustPoint_Type()
)
wsMgmtCertNumTrustPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtCertNumTrustPoint.setStatus("current")
_WsMgmtNwDiscovery_ObjectIdentity = ObjectIdentity
wsMgmtNwDiscovery = _WsMgmtNwDiscovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7)
)
_WsMgmtNetworkDiscoveryProfilesTable_Object = MibTable
wsMgmtNetworkDiscoveryProfilesTable = _WsMgmtNetworkDiscoveryProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1)
)
if mibBuilder.loadTexts:
    wsMgmtNetworkDiscoveryProfilesTable.setStatus("current")
_WsMgmtNetworkDiscoveryProfilesEntry_Object = MibTableRow
wsMgmtNetworkDiscoveryProfilesEntry = _WsMgmtNetworkDiscoveryProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1)
)
wsMgmtNetworkDiscoveryProfilesEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtDiscoveryProfileIndex"),
)
if mibBuilder.loadTexts:
    wsMgmtNetworkDiscoveryProfilesEntry.setStatus("current")


class _WsMgmtDiscoveryProfileIndex_Type(Integer32):
    """Custom type wsMgmtDiscoveryProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 127),
    )


_WsMgmtDiscoveryProfileIndex_Type.__name__ = "Integer32"
_WsMgmtDiscoveryProfileIndex_Object = MibTableColumn
wsMgmtDiscoveryProfileIndex = _WsMgmtDiscoveryProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 1),
    _WsMgmtDiscoveryProfileIndex_Type()
)
wsMgmtDiscoveryProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryProfileIndex.setStatus("current")


class _WsMgmtDiscoveryProfileName_Type(DisplayString):
    """Custom type wsMgmtDiscoveryProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 128),
    )


_WsMgmtDiscoveryProfileName_Type.__name__ = "DisplayString"
_WsMgmtDiscoveryProfileName_Object = MibTableColumn
wsMgmtDiscoveryProfileName = _WsMgmtDiscoveryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 2),
    _WsMgmtDiscoveryProfileName_Type()
)
wsMgmtDiscoveryProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryProfileName.setStatus("current")
_WsMgmtDiscoveryStartIPAddr_Type = IpAddress
_WsMgmtDiscoveryStartIPAddr_Object = MibTableColumn
wsMgmtDiscoveryStartIPAddr = _WsMgmtDiscoveryStartIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 3),
    _WsMgmtDiscoveryStartIPAddr_Type()
)
wsMgmtDiscoveryStartIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryStartIPAddr.setStatus("current")
_WsMgmtDiscoveryEndIPAddr_Type = IpAddress
_WsMgmtDiscoveryEndIPAddr_Object = MibTableColumn
wsMgmtDiscoveryEndIPAddr = _WsMgmtDiscoveryEndIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 4),
    _WsMgmtDiscoveryEndIPAddr_Type()
)
wsMgmtDiscoveryEndIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryEndIPAddr.setStatus("current")


class _WsMgmtDiscoverySnmpVersion_Type(Integer32):
    """Custom type wsMgmtDiscoverySnmpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpV1V2c", 1),
          ("snmpV1V2candsnmpV3", 3),
          ("snmpV3", 2))
    )


_WsMgmtDiscoverySnmpVersion_Type.__name__ = "Integer32"
_WsMgmtDiscoverySnmpVersion_Object = MibTableColumn
wsMgmtDiscoverySnmpVersion = _WsMgmtDiscoverySnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 5),
    _WsMgmtDiscoverySnmpVersion_Type()
)
wsMgmtDiscoverySnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtDiscoverySnmpVersion.setStatus("current")
_WsMgmtDiscoveryLastDoneTime_Type = DateAndTime
_WsMgmtDiscoveryLastDoneTime_Object = MibTableColumn
wsMgmtDiscoveryLastDoneTime = _WsMgmtDiscoveryLastDoneTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 6),
    _WsMgmtDiscoveryLastDoneTime_Type()
)
wsMgmtDiscoveryLastDoneTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryLastDoneTime.setStatus("current")


class _WsMgmtDiscoveryLastDoneStatus_Type(Integer32):
    """Custom type wsMgmtDiscoveryLastDoneStatus based on Integer32"""
    defaultValue = 1

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
        *(("abandoned", 3),
          ("failed", 4),
          ("neverDone", 1),
          ("successful", 2))
    )


_WsMgmtDiscoveryLastDoneStatus_Type.__name__ = "Integer32"
_WsMgmtDiscoveryLastDoneStatus_Object = MibTableColumn
wsMgmtDiscoveryLastDoneStatus = _WsMgmtDiscoveryLastDoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 7),
    _WsMgmtDiscoveryLastDoneStatus_Type()
)
wsMgmtDiscoveryLastDoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryLastDoneStatus.setStatus("current")
_WsMgmtDiscoveryProfileRowStatus_Type = RowStatus
_WsMgmtDiscoveryProfileRowStatus_Object = MibTableColumn
wsMgmtDiscoveryProfileRowStatus = _WsMgmtDiscoveryProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 1, 1, 8),
    _WsMgmtDiscoveryProfileRowStatus_Type()
)
wsMgmtDiscoveryProfileRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtDiscoveryProfileRowStatus.setStatus("current")
_WsMgmtNetworkDiscoveryTable_Object = MibTable
wsMgmtNetworkDiscoveryTable = _WsMgmtNetworkDiscoveryTable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2)
)
if mibBuilder.loadTexts:
    wsMgmtNetworkDiscoveryTable.setStatus("current")
_WsMgmtNetworkDiscoveryEntry_Object = MibTableRow
wsMgmtNetworkDiscoveryEntry = _WsMgmtNetworkDiscoveryEntry_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1)
)
wsMgmtNetworkDiscoveryEntry.setIndexNames(
    (0, "WS-MGMT-MIB", "wsMgmtDiscoveredDeviceIpAddr"),
)
if mibBuilder.loadTexts:
    wsMgmtNetworkDiscoveryEntry.setStatus("current")
_WsMgmtDiscoveredDeviceIpAddr_Type = IpAddress
_WsMgmtDiscoveredDeviceIpAddr_Object = MibTableColumn
wsMgmtDiscoveredDeviceIpAddr = _WsMgmtDiscoveredDeviceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 1),
    _WsMgmtDiscoveredDeviceIpAddr_Type()
)
wsMgmtDiscoveredDeviceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceIpAddr.setStatus("current")


class _WsMgmtDiscoveredDeviceHwVersion_Type(DisplayString):
    """Custom type wsMgmtDiscoveredDeviceHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WsMgmtDiscoveredDeviceHwVersion_Type.__name__ = "DisplayString"
_WsMgmtDiscoveredDeviceHwVersion_Object = MibTableColumn
wsMgmtDiscoveredDeviceHwVersion = _WsMgmtDiscoveredDeviceHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 2),
    _WsMgmtDiscoveredDeviceHwVersion_Type()
)
wsMgmtDiscoveredDeviceHwVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceHwVersion.setStatus("current")


class _WsMgmtDiscoveredDeviceSwVersion_Type(DisplayString):
    """Custom type wsMgmtDiscoveredDeviceSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WsMgmtDiscoveredDeviceSwVersion_Type.__name__ = "DisplayString"
_WsMgmtDiscoveredDeviceSwVersion_Object = MibTableColumn
wsMgmtDiscoveredDeviceSwVersion = _WsMgmtDiscoveredDeviceSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 3),
    _WsMgmtDiscoveredDeviceSwVersion_Type()
)
wsMgmtDiscoveredDeviceSwVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceSwVersion.setStatus("current")


class _WsMgmtDiscoveredDeviceClusterId_Type(Unsigned32):
    """Custom type wsMgmtDiscoveredDeviceClusterId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WsMgmtDiscoveredDeviceClusterId_Type.__name__ = "Unsigned32"
_WsMgmtDiscoveredDeviceClusterId_Object = MibTableColumn
wsMgmtDiscoveredDeviceClusterId = _WsMgmtDiscoveredDeviceClusterId_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 4),
    _WsMgmtDiscoveredDeviceClusterId_Type()
)
wsMgmtDiscoveredDeviceClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceClusterId.setStatus("current")
_WsMgmtDiscoveredDeviceName_Type = DisplayString
_WsMgmtDiscoveredDeviceName_Object = MibTableColumn
wsMgmtDiscoveredDeviceName = _WsMgmtDiscoveredDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 5),
    _WsMgmtDiscoveredDeviceName_Type()
)
wsMgmtDiscoveredDeviceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceName.setStatus("current")
_WsMgmtDiscoveredDeviceLocation_Type = DisplayString
_WsMgmtDiscoveredDeviceLocation_Object = MibTableColumn
wsMgmtDiscoveredDeviceLocation = _WsMgmtDiscoveredDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 6),
    _WsMgmtDiscoveredDeviceLocation_Type()
)
wsMgmtDiscoveredDeviceLocation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceLocation.setStatus("current")
_WsMgmtDiscoveredDeviceDescr_Type = DisplayString
_WsMgmtDiscoveredDeviceDescr_Object = MibTableColumn
wsMgmtDiscoveredDeviceDescr = _WsMgmtDiscoveredDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 7),
    _WsMgmtDiscoveredDeviceDescr_Type()
)
wsMgmtDiscoveredDeviceDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceDescr.setStatus("current")


class _WsMgmtDiscoveredDeviceDiscoveryProfileName_Type(DisplayString):
    """Custom type wsMgmtDiscoveredDeviceDiscoveryProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WsMgmtDiscoveredDeviceDiscoveryProfileName_Type.__name__ = "DisplayString"
_WsMgmtDiscoveredDeviceDiscoveryProfileName_Object = MibTableColumn
wsMgmtDiscoveredDeviceDiscoveryProfileName = _WsMgmtDiscoveredDeviceDiscoveryProfileName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 8),
    _WsMgmtDiscoveredDeviceDiscoveryProfileName_Type()
)
wsMgmtDiscoveredDeviceDiscoveryProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceDiscoveryProfileName.setStatus("current")
_WsMgmtDiscoveredDeviceDiscoveryTime_Type = DateAndTime
_WsMgmtDiscoveredDeviceDiscoveryTime_Object = MibTableColumn
wsMgmtDiscoveredDeviceDiscoveryTime = _WsMgmtDiscoveredDeviceDiscoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 9),
    _WsMgmtDiscoveredDeviceDiscoveryTime_Type()
)
wsMgmtDiscoveredDeviceDiscoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredDeviceDiscoveryTime.setStatus("current")
_WsMgmtDiscoveredNetworkDevicesTableRow_Type = RowStatus
_WsMgmtDiscoveredNetworkDevicesTableRow_Object = MibTableColumn
wsMgmtDiscoveredNetworkDevicesTableRow = _WsMgmtDiscoveredNetworkDevicesTableRow_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 7, 2, 1, 10),
    _WsMgmtDiscoveredNetworkDevicesTableRow_Type()
)
wsMgmtDiscoveredNetworkDevicesTableRow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    wsMgmtDiscoveredNetworkDevicesTableRow.setStatus("current")
_WsMgmtKey_ObjectIdentity = ObjectIdentity
wsMgmtKey = _WsMgmtKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 8)
)
_WsMgmtGenKey_Type = Unsigned32
_WsMgmtGenKey_Object = MibScalar
wsMgmtGenKey = _WsMgmtGenKey_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 8, 1),
    _WsMgmtGenKey_Type()
)
wsMgmtGenKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsMgmtGenKey.setStatus("current")
_WsMgmtSsh_ObjectIdentity = ObjectIdentity
wsMgmtSsh = _WsMgmtSsh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 11)
)
_WsMgmtSshEnable_Type = TruthValue
_WsMgmtSshEnable_Object = MibScalar
wsMgmtSshEnable = _WsMgmtSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 11, 1),
    _WsMgmtSshEnable_Type()
)
wsMgmtSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSshEnable.setStatus("current")
_WsMgmtSshPort_Type = Integer32
_WsMgmtSshPort_Object = MibScalar
wsMgmtSshPort = _WsMgmtSshPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 11, 2),
    _WsMgmtSshPort_Type()
)
wsMgmtSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSshPort.setStatus("current")


class _WsMgmtSshKeyPairName_Type(DisplayString):
    """Custom type wsMgmtSshKeyPairName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_WsMgmtSshKeyPairName_Type.__name__ = "DisplayString"
_WsMgmtSshKeyPairName_Object = MibScalar
wsMgmtSshKeyPairName = _WsMgmtSshKeyPairName_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 11, 5),
    _WsMgmtSshKeyPairName_Type()
)
wsMgmtSshKeyPairName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtSshKeyPairName.setStatus("current")
_WsMgmtTelnet_ObjectIdentity = ObjectIdentity
wsMgmtTelnet = _WsMgmtTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 13)
)
_WsMgmtTelnetEnable_Type = TruthValue
_WsMgmtTelnetEnable_Object = MibScalar
wsMgmtTelnetEnable = _WsMgmtTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 13, 1),
    _WsMgmtTelnetEnable_Type()
)
wsMgmtTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtTelnetEnable.setStatus("current")
_WsMgmtTelnetPort_Type = Integer32
_WsMgmtTelnetPort_Object = MibScalar
wsMgmtTelnetPort = _WsMgmtTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 13, 2),
    _WsMgmtTelnetPort_Type()
)
wsMgmtTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtTelnetPort.setStatus("current")
_WsMgmtFtp_ObjectIdentity = ObjectIdentity
wsMgmtFtp = _WsMgmtFtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 14)
)
_WsMgmtFtpEnable_Type = TruthValue
_WsMgmtFtpEnable_Object = MibScalar
wsMgmtFtpEnable = _WsMgmtFtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 14, 1),
    _WsMgmtFtpEnable_Type()
)
wsMgmtFtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtFtpEnable.setStatus("current")
_WsMgmtFtpRoot_Type = DisplayString
_WsMgmtFtpRoot_Object = MibScalar
wsMgmtFtpRoot = _WsMgmtFtpRoot_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 14, 2),
    _WsMgmtFtpRoot_Type()
)
wsMgmtFtpRoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtFtpRoot.setStatus("current")
_WsMgmtFtpPwd_Type = DisplayString
_WsMgmtFtpPwd_Object = MibScalar
wsMgmtFtpPwd = _WsMgmtFtpPwd_Object(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 14, 3),
    _WsMgmtFtpPwd_Type()
)
wsMgmtFtpPwd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsMgmtFtpPwd.setStatus("current")
_WsMgmtConformance_ObjectIdentity = ObjectIdentity
wsMgmtConformance = _WsMgmtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 100)
)
_WsMgmtCompliances_ObjectIdentity = ObjectIdentity
wsMgmtCompliances = _WsMgmtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 100, 1)
)
_WsMgmtGroups_ObjectIdentity = ObjectIdentity
wsMgmtGroups = _WsMgmtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 100, 2)
)

# Managed Objects groups

wsMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 100, 2, 2)
)
wsMgmtGroup.setObjects(
      *(("WS-MGMT-MIB", "wsMgmtSystemReset"),
        ("WS-MGMT-MIB", "wsMgmtSystemFactoryDefaultCfg"),
        ("WS-MGMT-MIB", "wsMgmtSnmpV2Switch"),
        ("WS-MGMT-MIB", "wsMgmtHttpEnable"),
        ("WS-MGMT-MIB", "wsMgmtAlarmStatus"),
        ("WS-MGMT-MIB", "wsMgmtAlarmSeverity"),
        ("WS-MGMT-MIB", "wsMgmtAlarmTimestamp"),
        ("WS-MGMT-MIB", "wsMgmtAlarmRowStatus"),
        ("WS-MGMT-MIB", "wsMgmtClearAllAlarms"),
        ("WS-MGMT-MIB", "wsMgmtAcknowledgeAllAlarms"),
        ("WS-MGMT-MIB", "wsMgmtAlarmIndex"),
        ("WS-MGMT-MIB", "wsMgmtModuleName"),
        ("WS-MGMT-MIB", "wsMgmtSnmpV3Switch"),
        ("WS-MGMT-MIB", "wsMgmtHttpsEnable"),
        ("WS-MGMT-MIB", "wsMgmtNewAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmtTotalAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmtGenKey"),
        ("WS-MGMT-MIB", "wsMgmtCertCreateAction"),
        ("WS-MGMT-MIB", "wsMgmtCertKeyLabel"),
        ("WS-MGMT-MIB", "wsMgmtCertKeySize"),
        ("WS-MGMT-MIB", "wsMgmtCertNumTrustPoint"),
        ("WS-MGMT-MIB", "wsMgmtCertCreateStatus"),
        ("WS-MGMT-MIB", "wsMgmtCertKeyRowStatus"),
        ("WS-MGMT-MIB", "wsMgmtSshEnable"),
        ("WS-MGMT-MIB", "wsMgmtSshPort"),
        ("WS-MGMT-MIB", "wsMgmtSshKeyPairName"),
        ("WS-MGMT-MIB", "wsMgmtTelnetEnable"),
        ("WS-MGMT-MIB", "wsMgmtTelnetPort"),
        ("WS-MGMT-MIB", "wsMgmtAlarmMessage"),
        ("WS-MGMT-MIB", "wsMgmtAlarmTypeID"),
        ("WS-MGMT-MIB", "wsMgmtAlarmTypeName"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigTrustpoint"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigKey"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigCommonName"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigOrgUnit"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigOrg"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigState"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigCity"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigCountry"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigFqdn"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigIP"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigEmail"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigPassword"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigCompany"),
        ("WS-MGMT-MIB", "wsMgmtCertViewType"),
        ("WS-MGMT-MIB", "wsMgmtCertConfigRowStatus"),
        ("WS-MGMT-MIB", "wsMgmtCertViewTrustpoint"),
        ("WS-MGMT-MIB", "wsMgmtCertViewValidStart"),
        ("WS-MGMT-MIB", "wsMgmtAlarmsIndexLow"),
        ("WS-MGMT-MIB", "wsMgmtAlarmsIndexHigh"),
        ("WS-MGMT-MIB", "wsMgmCriticalAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmMajorAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmWarningAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmInfoAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmNormalAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmtTotalAlarmsCountSinceBoot"),
        ("WS-MGMT-MIB", "wsMgmtFtpEnable"),
        ("WS-MGMT-MIB", "wsMgmtFtpRoot"),
        ("WS-MGMT-MIB", "wsMgmtFtpPwd"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredNetworkDevicesTableRow"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceDiscoveryTime"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceDiscoveryProfileName"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceDescr"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceLocation"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceName"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceClusterId"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceSwVersion"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceHwVersion"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveredDeviceIpAddr"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryProfileRowStatus"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryLastDoneStatus"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryLastDoneTime"),
        ("WS-MGMT-MIB", "wsMgmtDiscoverySnmpVersion"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryEndIPAddr"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryStartIPAddr"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryProfileName"),
        ("WS-MGMT-MIB", "wsMgmtDiscoveryProfileIndex"),
        ("WS-MGMT-MIB", "wsMgmtHttpTrustpoint"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedCriticalAlarmsCountSinceBoot"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedMajorAlarmsCountSinceBoot"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedWarningAlarmsCountSinceBoot"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedInfoAlarmsCountSinceBoot"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedNormalAlarmsCountSinceBoot"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedMajorAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedWarningAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedInfoAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedNormalAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmUnacknowledgedCriticalAlarmsCount"),
        ("WS-MGMT-MIB", "wsMgmtCertViewValidEnd"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectCommonName"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectOrgUnit"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectOrg"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectCity"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectState"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectCountry"),
        ("WS-MGMT-MIB", "wsMgmtCertViewSubjectEmail"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerCommonName"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerOrgUnit"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerOrg"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerCity"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerState"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerCountry"),
        ("WS-MGMT-MIB", "wsMgmtCertViewIssuerEmail"))
)
if mibBuilder.loadTexts:
    wsMgmtGroup.setStatus("current")

wsMgmtObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 100, 2, 3)
)
wsMgmtObsoleteGroup.setObjects(
      *(("WS-MGMT-MIB", "wsMgmtCertCurrentCountry"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentState"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentCity"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentOrg"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentOrgUnit"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentCommonName"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentIssuer"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentValidStart"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentValidEnd"),
        ("WS-MGMT-MIB", "wsMgmtCertCurrentTrustPoint"),
        ("WS-MGMT-MIB", "wsMgmtCertFileName"),
        ("WS-MGMT-MIB", "wsMgmtCertAction"),
        ("WS-MGMT-MIB", "wsMgmtCertStatus"),
        ("WS-MGMT-MIB", "wsMgmtCertCountry"),
        ("WS-MGMT-MIB", "wsMgmtCertState"),
        ("WS-MGMT-MIB", "wsMgmtCertCity"),
        ("WS-MGMT-MIB", "wsMgmtCertOrg"),
        ("WS-MGMT-MIB", "wsMgmtCertOrgUnit"),
        ("WS-MGMT-MIB", "wsMgmtCertCommonName"),
        ("WS-MGMT-MIB", "wsMgmtCertIssuer"),
        ("WS-MGMT-MIB", "wsMgmtCertEmail"),
        ("WS-MGMT-MIB", "wsMgmtCertPwd"),
        ("WS-MGMT-MIB", "wsMgmtCertCompany"),
        ("WS-MGMT-MIB", "wsMgmtCertValidStart"),
        ("WS-MGMT-MIB", "wsMgmtCertValidEnd"),
        ("WS-MGMT-MIB", "wsMgmtCertTrustPoint"),
        ("WS-MGMT-MIB", "wsMgmtGenKey"))
)
if mibBuilder.loadTexts:
    wsMgmtObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

wsMgmtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 388, 14, 4, 1, 100, 1, 1)
)
if mibBuilder.loadTexts:
    wsMgmtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WS-MGMT-MIB",
    **{"AbbrRowStatus": AbbrRowStatus,
       "DoActionShowProgress": DoActionShowProgress,
       "Password": Password,
       "StaticRowEnable": StaticRowEnable,
       "wsMgmtMib": wsMgmtMib,
       "wsMgmtReset": wsMgmtReset,
       "wsMgmtSystemReset": wsMgmtSystemReset,
       "wsMgmtSystemFactoryDefaultCfg": wsMgmtSystemFactoryDefaultCfg,
       "wsMgmtSnmp": wsMgmtSnmp,
       "wsMgmtSnmpV2Switch": wsMgmtSnmpV2Switch,
       "wsMgmtSnmpV3Switch": wsMgmtSnmpV3Switch,
       "wsMgmtHttp": wsMgmtHttp,
       "wsMgmtHttpEnable": wsMgmtHttpEnable,
       "wsMgmtHttpsEnable": wsMgmtHttpsEnable,
       "wsMgmtHttpTrustpoint": wsMgmtHttpTrustpoint,
       "wsMgmtAlarms": wsMgmtAlarms,
       "wsMgmtAlarmTable": wsMgmtAlarmTable,
       "wsMgmtAlarmEntry": wsMgmtAlarmEntry,
       "wsMgmtAlarmIndex": wsMgmtAlarmIndex,
       "wsMgmtAlarmSeverity": wsMgmtAlarmSeverity,
       "wsMgmtAlarmTypeID": wsMgmtAlarmTypeID,
       "wsMgmtAlarmTypeName": wsMgmtAlarmTypeName,
       "wsMgmtAlarmTimestamp": wsMgmtAlarmTimestamp,
       "wsMgmtAlarmMessage": wsMgmtAlarmMessage,
       "wsMgmtModuleName": wsMgmtModuleName,
       "wsMgmtAlarmStatus": wsMgmtAlarmStatus,
       "wsMgmtAlarmRowStatus": wsMgmtAlarmRowStatus,
       "wsMgmtClearAllAlarms": wsMgmtClearAllAlarms,
       "wsMgmtAcknowledgeAllAlarms": wsMgmtAcknowledgeAllAlarms,
       "wsMgmtNewAlarmsCount": wsMgmtNewAlarmsCount,
       "wsMgmtTotalAlarmsCount": wsMgmtTotalAlarmsCount,
       "wsMgmtTotalAlarmsCountSinceBoot": wsMgmtTotalAlarmsCountSinceBoot,
       "wsMgmtAlarmsIndexLow": wsMgmtAlarmsIndexLow,
       "wsMgmtAlarmsIndexHigh": wsMgmtAlarmsIndexHigh,
       "wsMgmCriticalAlarmsCount": wsMgmCriticalAlarmsCount,
       "wsMgmMajorAlarmsCount": wsMgmMajorAlarmsCount,
       "wsMgmWarningAlarmsCount": wsMgmWarningAlarmsCount,
       "wsMgmInfoAlarmsCount": wsMgmInfoAlarmsCount,
       "wsMgmNormalAlarmsCount": wsMgmNormalAlarmsCount,
       "wsMgmUnacknowledgedCriticalAlarmsCount": wsMgmUnacknowledgedCriticalAlarmsCount,
       "wsMgmUnacknowledgedMajorAlarmsCount": wsMgmUnacknowledgedMajorAlarmsCount,
       "wsMgmUnacknowledgedWarningAlarmsCount": wsMgmUnacknowledgedWarningAlarmsCount,
       "wsMgmUnacknowledgedInfoAlarmsCount": wsMgmUnacknowledgedInfoAlarmsCount,
       "wsMgmUnacknowledgedNormalAlarmsCount": wsMgmUnacknowledgedNormalAlarmsCount,
       "wsMgmUnacknowledgedCriticalAlarmsCountSinceBoot": wsMgmUnacknowledgedCriticalAlarmsCountSinceBoot,
       "wsMgmUnacknowledgedMajorAlarmsCountSinceBoot": wsMgmUnacknowledgedMajorAlarmsCountSinceBoot,
       "wsMgmUnacknowledgedWarningAlarmsCountSinceBoot": wsMgmUnacknowledgedWarningAlarmsCountSinceBoot,
       "wsMgmUnacknowledgedInfoAlarmsCountSinceBoot": wsMgmUnacknowledgedInfoAlarmsCountSinceBoot,
       "wsMgmUnacknowledgedNormalAlarmsCountSinceBoot": wsMgmUnacknowledgedNormalAlarmsCountSinceBoot,
       "wsMgmtCert": wsMgmtCert,
       "wsMgmtCertCurrent": wsMgmtCertCurrent,
       "wsMgmtCertCurrentCountry": wsMgmtCertCurrentCountry,
       "wsMgmtCertCurrentState": wsMgmtCertCurrentState,
       "wsMgmtCertCurrentCity": wsMgmtCertCurrentCity,
       "wsMgmtCertCurrentOrg": wsMgmtCertCurrentOrg,
       "wsMgmtCertCurrentOrgUnit": wsMgmtCertCurrentOrgUnit,
       "wsMgmtCertCurrentCommonName": wsMgmtCertCurrentCommonName,
       "wsMgmtCertCurrentIssuer": wsMgmtCertCurrentIssuer,
       "wsMgmtCertCurrentValidStart": wsMgmtCertCurrentValidStart,
       "wsMgmtCertCurrentValidEnd": wsMgmtCertCurrentValidEnd,
       "wsMgmtCertCurrentTrustPoint": wsMgmtCertCurrentTrustPoint,
       "wsMgmtCertCreate": wsMgmtCertCreate,
       "wsMgmtCertFileName": wsMgmtCertFileName,
       "wsMgmtCertAction": wsMgmtCertAction,
       "wsMgmtCertStatus": wsMgmtCertStatus,
       "wsMgmtCertCountry": wsMgmtCertCountry,
       "wsMgmtCertState": wsMgmtCertState,
       "wsMgmtCertCity": wsMgmtCertCity,
       "wsMgmtCertOrg": wsMgmtCertOrg,
       "wsMgmtCertOrgUnit": wsMgmtCertOrgUnit,
       "wsMgmtCertCommonName": wsMgmtCertCommonName,
       "wsMgmtCertIssuer": wsMgmtCertIssuer,
       "wsMgmtCertEmail": wsMgmtCertEmail,
       "wsMgmtCertPwd": wsMgmtCertPwd,
       "wsMgmtCertCompany": wsMgmtCertCompany,
       "wsMgmtCertValidStart": wsMgmtCertValidStart,
       "wsMgmtCertValidEnd": wsMgmtCertValidEnd,
       "wsMgmtCertTrustPoint": wsMgmtCertTrustPoint,
       "wsMgmtCertViewTable": wsMgmtCertViewTable,
       "wsMgmtCertViewEntry": wsMgmtCertViewEntry,
       "wsMgmtCertViewTrustpoint": wsMgmtCertViewTrustpoint,
       "wsMgmtCertViewType": wsMgmtCertViewType,
       "wsMgmtCertViewSubjectCommonName": wsMgmtCertViewSubjectCommonName,
       "wsMgmtCertViewSubjectOrgUnit": wsMgmtCertViewSubjectOrgUnit,
       "wsMgmtCertViewSubjectOrg": wsMgmtCertViewSubjectOrg,
       "wsMgmtCertViewSubjectCity": wsMgmtCertViewSubjectCity,
       "wsMgmtCertViewSubjectState": wsMgmtCertViewSubjectState,
       "wsMgmtCertViewSubjectCountry": wsMgmtCertViewSubjectCountry,
       "wsMgmtCertViewSubjectEmail": wsMgmtCertViewSubjectEmail,
       "wsMgmtCertViewIssuerCommonName": wsMgmtCertViewIssuerCommonName,
       "wsMgmtCertViewIssuerOrgUnit": wsMgmtCertViewIssuerOrgUnit,
       "wsMgmtCertViewIssuerOrg": wsMgmtCertViewIssuerOrg,
       "wsMgmtCertViewIssuerCity": wsMgmtCertViewIssuerCity,
       "wsMgmtCertViewIssuerState": wsMgmtCertViewIssuerState,
       "wsMgmtCertViewIssuerCountry": wsMgmtCertViewIssuerCountry,
       "wsMgmtCertViewIssuerEmail": wsMgmtCertViewIssuerEmail,
       "wsMgmtCertViewValidStart": wsMgmtCertViewValidStart,
       "wsMgmtCertViewValidEnd": wsMgmtCertViewValidEnd,
       "wsMgmtCertConfigTable": wsMgmtCertConfigTable,
       "wsMgmtCertConfigEntry": wsMgmtCertConfigEntry,
       "wsMgmtCertConfigTrustpoint": wsMgmtCertConfigTrustpoint,
       "wsMgmtCertConfigKey": wsMgmtCertConfigKey,
       "wsMgmtCertConfigCommonName": wsMgmtCertConfigCommonName,
       "wsMgmtCertConfigOrgUnit": wsMgmtCertConfigOrgUnit,
       "wsMgmtCertConfigOrg": wsMgmtCertConfigOrg,
       "wsMgmtCertConfigCompany": wsMgmtCertConfigCompany,
       "wsMgmtCertConfigCity": wsMgmtCertConfigCity,
       "wsMgmtCertConfigState": wsMgmtCertConfigState,
       "wsMgmtCertConfigCountry": wsMgmtCertConfigCountry,
       "wsMgmtCertConfigFqdn": wsMgmtCertConfigFqdn,
       "wsMgmtCertConfigIP": wsMgmtCertConfigIP,
       "wsMgmtCertConfigEmail": wsMgmtCertConfigEmail,
       "wsMgmtCertConfigPassword": wsMgmtCertConfigPassword,
       "wsMgmtCertConfigRowStatus": wsMgmtCertConfigRowStatus,
       "wsMgmtCertCreateTable": wsMgmtCertCreateTable,
       "wsMgmtCertCreateEntry": wsMgmtCertCreateEntry,
       "wsMgmtCertCreateStatus": wsMgmtCertCreateStatus,
       "wsMgmtCertCreateAction": wsMgmtCertCreateAction,
       "wsMgmtCertKeyTable": wsMgmtCertKeyTable,
       "wsMgmtCertKeyEntry": wsMgmtCertKeyEntry,
       "wsMgmtCertKeyLabel": wsMgmtCertKeyLabel,
       "wsMgmtCertKeySize": wsMgmtCertKeySize,
       "wsMgmtCertKeyRowStatus": wsMgmtCertKeyRowStatus,
       "wsMgmtCertNumTrustPoint": wsMgmtCertNumTrustPoint,
       "wsMgmtNwDiscovery": wsMgmtNwDiscovery,
       "wsMgmtNetworkDiscoveryProfilesTable": wsMgmtNetworkDiscoveryProfilesTable,
       "wsMgmtNetworkDiscoveryProfilesEntry": wsMgmtNetworkDiscoveryProfilesEntry,
       "wsMgmtDiscoveryProfileIndex": wsMgmtDiscoveryProfileIndex,
       "wsMgmtDiscoveryProfileName": wsMgmtDiscoveryProfileName,
       "wsMgmtDiscoveryStartIPAddr": wsMgmtDiscoveryStartIPAddr,
       "wsMgmtDiscoveryEndIPAddr": wsMgmtDiscoveryEndIPAddr,
       "wsMgmtDiscoverySnmpVersion": wsMgmtDiscoverySnmpVersion,
       "wsMgmtDiscoveryLastDoneTime": wsMgmtDiscoveryLastDoneTime,
       "wsMgmtDiscoveryLastDoneStatus": wsMgmtDiscoveryLastDoneStatus,
       "wsMgmtDiscoveryProfileRowStatus": wsMgmtDiscoveryProfileRowStatus,
       "wsMgmtNetworkDiscoveryTable": wsMgmtNetworkDiscoveryTable,
       "wsMgmtNetworkDiscoveryEntry": wsMgmtNetworkDiscoveryEntry,
       "wsMgmtDiscoveredDeviceIpAddr": wsMgmtDiscoveredDeviceIpAddr,
       "wsMgmtDiscoveredDeviceHwVersion": wsMgmtDiscoveredDeviceHwVersion,
       "wsMgmtDiscoveredDeviceSwVersion": wsMgmtDiscoveredDeviceSwVersion,
       "wsMgmtDiscoveredDeviceClusterId": wsMgmtDiscoveredDeviceClusterId,
       "wsMgmtDiscoveredDeviceName": wsMgmtDiscoveredDeviceName,
       "wsMgmtDiscoveredDeviceLocation": wsMgmtDiscoveredDeviceLocation,
       "wsMgmtDiscoveredDeviceDescr": wsMgmtDiscoveredDeviceDescr,
       "wsMgmtDiscoveredDeviceDiscoveryProfileName": wsMgmtDiscoveredDeviceDiscoveryProfileName,
       "wsMgmtDiscoveredDeviceDiscoveryTime": wsMgmtDiscoveredDeviceDiscoveryTime,
       "wsMgmtDiscoveredNetworkDevicesTableRow": wsMgmtDiscoveredNetworkDevicesTableRow,
       "wsMgmtKey": wsMgmtKey,
       "wsMgmtGenKey": wsMgmtGenKey,
       "wsMgmtSsh": wsMgmtSsh,
       "wsMgmtSshEnable": wsMgmtSshEnable,
       "wsMgmtSshPort": wsMgmtSshPort,
       "wsMgmtSshKeyPairName": wsMgmtSshKeyPairName,
       "wsMgmtTelnet": wsMgmtTelnet,
       "wsMgmtTelnetEnable": wsMgmtTelnetEnable,
       "wsMgmtTelnetPort": wsMgmtTelnetPort,
       "wsMgmtFtp": wsMgmtFtp,
       "wsMgmtFtpEnable": wsMgmtFtpEnable,
       "wsMgmtFtpRoot": wsMgmtFtpRoot,
       "wsMgmtFtpPwd": wsMgmtFtpPwd,
       "wsMgmtConformance": wsMgmtConformance,
       "wsMgmtCompliances": wsMgmtCompliances,
       "wsMgmtCompliance": wsMgmtCompliance,
       "wsMgmtGroups": wsMgmtGroups,
       "wsMgmtGroup": wsMgmtGroup,
       "wsMgmtObsoleteGroup": wsMgmtObsoleteGroup}
)
