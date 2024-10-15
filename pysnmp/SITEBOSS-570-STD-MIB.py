# SNMP MIB module (SITEBOSS-570-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SITEBOSS-570-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:32 2024
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

(asentria,) = mibBuilder.importSymbols(
    "ASENTRIA-ROOT-MIB",
    "asentria")

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

s570 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8)
)
s570.setRevisions(
        ("2014-12-11 01:46",
         "2014-10-16 01:45",
         "2014-10-03 01:44",
         "2014-08-14 01:43",
         "2014-07-03 01:42",
         "2014-06-24 01:41",
         "2014-05-29 01:40",
         "2014-04-11 01:39",
         "2013-06-12 01:38",
         "2013-05-28 01:37",
         "2013-05-10 01:36",
         "2013-03-15 01:35",
         "2013-02-06 01:34",
         "2013-01-14 01:33",
         "2012-11-26 01:32",
         "2012-08-22 01:31",
         "2012-07-09 01:30",
         "2012-06-12 01:29",
         "2012-04-09 01:28",
         "2012-04-05 01:27",
         "2012-03-06 01:26",
         "2011-12-05 09:00",
         "2011-10-24 09:00",
         "2011-08-08 09:00",
         "2011-08-01 09:00",
         "2011-07-08 09:00",
         "2011-01-05 09:00",
         "2010-11-03 09:00",
         "2010-08-24 09:00",
         "2010-03-16 09:00",
         "2010-01-19 09:00",
         "2009-01-25 09:00",
         "2008-11-12 09:00",
         "2008-06-09 09:00",
         "2008-06-02 11:00",
         "2008-05-15 15:00",
         "2008-04-22 16:52",
         "2008-03-21 16:50",
         "2007-10-04 10:20",
         "2007-09-14 16:52",
         "2007-09-13 23:55",
         "2007-09-13 00:00",
         "2007-09-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1)
)
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("current")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "esIndexES"),
    (0, "SITEBOSS-570-STD-MIB", "esIndexPC"),
    (0, "SITEBOSS-570-STD-MIB", "esIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointEntry.setStatus("current")


class _EsIndexES_Type(Integer32):
    """Custom type esIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EsIndexES_Type.__name__ = "Integer32"
_EsIndexES_Object = MibTableColumn
esIndexES = _EsIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 1),
    _EsIndexES_Type()
)
esIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexES.setStatus("current")


class _EsIndexPC_Type(Integer32):
    """Custom type esIndexPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EsIndexPC_Type.__name__ = "Integer32"
_EsIndexPC_Object = MibTableColumn
esIndexPC = _EsIndexPC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 2),
    _EsIndexPC_Type()
)
esIndexPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPC.setStatus("current")


class _EsIndexPoint_Type(Integer32):
    """Custom type esIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EsIndexPoint_Type.__name__ = "Integer32"
_EsIndexPoint_Object = MibTableColumn
esIndexPoint = _EsIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("current")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("current")
_EsPointInEventState_Type = Integer32
_EsPointInEventState_Object = MibTableColumn
esPointInEventState = _EsPointInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 5),
    _EsPointInEventState_Type()
)
esPointInEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointInEventState.setStatus("current")


class _EsPointValueInt_Type(Integer32):
    """Custom type esPointValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EsPointValueInt_Type.__name__ = "Integer32"
_EsPointValueInt_Object = MibTableColumn
esPointValueInt = _EsPointValueInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 6),
    _EsPointValueInt_Type()
)
esPointValueInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointValueInt.setStatus("current")
_EsPointValueStr_Type = DisplayString
_EsPointValueStr_Object = MibTableColumn
esPointValueStr = _EsPointValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 7),
    _EsPointValueStr_Type()
)
esPointValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointValueStr.setStatus("current")
_EsPointTimeLastChange_Type = DisplayString
_EsPointTimeLastChange_Object = MibTableColumn
esPointTimeLastChange = _EsPointTimeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 8),
    _EsPointTimeLastChange_Type()
)
esPointTimeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointTimeLastChange.setStatus("current")
_EsPointTimetickLastChange_Type = TimeTicks
_EsPointTimetickLastChange_Object = MibTableColumn
esPointTimetickLastChange = _EsPointTimetickLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 1, 1, 1, 9),
    _EsPointTimetickLastChange_Type()
)
esPointTimetickLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointTimetickLastChange.setStatus("current")
_DataEventStatus_ObjectIdentity = ObjectIdentity
dataEventStatus = _DataEventStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2)
)
_DeStatusTable_Object = MibTable
deStatusTable = _DeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deStatusTable.setStatus("current")
_DeStatusEntry_Object = MibTableRow
deStatusEntry = _DeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2, 1, 1)
)
deStatusEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "deStatusIndex"),
)
if mibBuilder.loadTexts:
    deStatusEntry.setStatus("current")


class _DeStatusIndex_Type(Integer32):
    """Custom type deStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DeStatusIndex_Type.__name__ = "Integer32"
_DeStatusIndex_Object = MibTableColumn
deStatusIndex = _DeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2, 1, 1, 1),
    _DeStatusIndex_Type()
)
deStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusIndex.setStatus("current")
_DeStatusName_Type = DisplayString
_DeStatusName_Object = MibTableColumn
deStatusName = _DeStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2, 1, 1, 2),
    _DeStatusName_Type()
)
deStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusName.setStatus("current")
_DeStatusCounter_Type = Integer32
_DeStatusCounter_Object = MibTableColumn
deStatusCounter = _DeStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2, 1, 1, 3),
    _DeStatusCounter_Type()
)
deStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusCounter.setStatus("current")
_DeStatusThreshold_Type = Integer32
_DeStatusThreshold_Object = MibTableColumn
deStatusThreshold = _DeStatusThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 2, 1, 1, 4),
    _DeStatusThreshold_Type()
)
deStatusThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusThreshold.setStatus("current")
_ModemStatus_Type = DisplayString
_ModemStatus_Object = MibScalar
modemStatus = _ModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 3),
    _ModemStatus_Type()
)
modemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemStatus.setStatus("current")
_ModemCLIDLogTable_Object = MibTable
modemCLIDLogTable = _ModemCLIDLogTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 4)
)
if mibBuilder.loadTexts:
    modemCLIDLogTable.setStatus("current")
_ModemCLIDLogEntry_Object = MibTableRow
modemCLIDLogEntry = _ModemCLIDLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 4, 1)
)
modemCLIDLogEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "modemCLIDLogIndex"),
)
if mibBuilder.loadTexts:
    modemCLIDLogEntry.setStatus("current")


class _ModemCLIDLogIndex_Type(Integer32):
    """Custom type modemCLIDLogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ModemCLIDLogIndex_Type.__name__ = "Integer32"
_ModemCLIDLogIndex_Object = MibTableColumn
modemCLIDLogIndex = _ModemCLIDLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 4, 1, 1),
    _ModemCLIDLogIndex_Type()
)
modemCLIDLogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCLIDLogIndex.setStatus("current")
_ModemCLIDLogNumber_Type = DisplayString
_ModemCLIDLogNumber_Object = MibTableColumn
modemCLIDLogNumber = _ModemCLIDLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 4, 1, 2),
    _ModemCLIDLogNumber_Type()
)
modemCLIDLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCLIDLogNumber.setStatus("current")
_FuelSensorStatus_ObjectIdentity = ObjectIdentity
fuelSensorStatus = _FuelSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6)
)
_FsStatusTable_Object = MibTable
fsStatusTable = _FsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsStatusTable.setStatus("current")
_FsStatusEntry_Object = MibTableRow
fsStatusEntry = _FsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1)
)
fsStatusEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "fsStatusIndex"),
)
if mibBuilder.loadTexts:
    fsStatusEntry.setStatus("current")


class _FsStatusIndex_Type(Integer32):
    """Custom type fsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsStatusIndex_Type.__name__ = "Integer32"
_FsStatusIndex_Object = MibTableColumn
fsStatusIndex = _FsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 1),
    _FsStatusIndex_Type()
)
fsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusIndex.setStatus("current")
_FsStatusName_Type = DisplayString
_FsStatusName_Object = MibTableColumn
fsStatusName = _FsStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 2),
    _FsStatusName_Type()
)
fsStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusName.setStatus("current")
_FsStatusDeviceState_Type = DisplayString
_FsStatusDeviceState_Object = MibTableColumn
fsStatusDeviceState = _FsStatusDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 3),
    _FsStatusDeviceState_Type()
)
fsStatusDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusDeviceState.setStatus("current")
_FsStatusVolumeValueString_Type = DisplayString
_FsStatusVolumeValueString_Object = MibTableColumn
fsStatusVolumeValueString = _FsStatusVolumeValueString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 4),
    _FsStatusVolumeValueString_Type()
)
fsStatusVolumeValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusVolumeValueString.setStatus("current")
_FsStatusVolumePercentLevel_Type = DisplayString
_FsStatusVolumePercentLevel_Object = MibTableColumn
fsStatusVolumePercentLevel = _FsStatusVolumePercentLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 7),
    _FsStatusVolumePercentLevel_Type()
)
fsStatusVolumePercentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusVolumePercentLevel.setStatus("current")
_FsStatusVolumeInEventState_Type = DisplayString
_FsStatusVolumeInEventState_Object = MibTableColumn
fsStatusVolumeInEventState = _FsStatusVolumeInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 8),
    _FsStatusVolumeInEventState_Type()
)
fsStatusVolumeInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusVolumeInEventState.setStatus("current")
_FsStatusCombined_Type = DisplayString
_FsStatusCombined_Object = MibTableColumn
fsStatusCombined = _FsStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 6, 1, 1, 9),
    _FsStatusCombined_Type()
)
fsStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusCombined.setStatus("current")
_WirelessModemStatus_ObjectIdentity = ObjectIdentity
wirelessModemStatus = _WirelessModemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7)
)
_WmsStatus_Type = DisplayString
_WmsStatus_Object = MibScalar
wmsStatus = _WmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 1),
    _WmsStatus_Type()
)
wmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsStatus.setStatus("current")
_WmsSignal_Type = DisplayString
_WmsSignal_Object = MibScalar
wmsSignal = _WmsSignal_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 2),
    _WmsSignal_Type()
)
wmsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsSignal.setStatus("current")
_WmsRSSI_Type = DisplayString
_WmsRSSI_Object = MibScalar
wmsRSSI = _WmsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 3),
    _WmsRSSI_Type()
)
wmsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsRSSI.setStatus("current")
_WmsBER_Type = DisplayString
_WmsBER_Object = MibScalar
wmsBER = _WmsBER_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 4),
    _WmsBER_Type()
)
wmsBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBER.setStatus("current")
_WmsUpdated_Type = DisplayString
_WmsUpdated_Object = MibScalar
wmsUpdated = _WmsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 5),
    _WmsUpdated_Type()
)
wmsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsUpdated.setStatus("current")
_WmsRegistration_Type = DisplayString
_WmsRegistration_Object = MibScalar
wmsRegistration = _WmsRegistration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 6),
    _WmsRegistration_Type()
)
wmsRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsRegistration.setStatus("current")
_WmsLAC_Type = DisplayString
_WmsLAC_Object = MibScalar
wmsLAC = _WmsLAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 7),
    _WmsLAC_Type()
)
wmsLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsLAC.setStatus("current")
_WmsCellID_Type = DisplayString
_WmsCellID_Object = MibScalar
wmsCellID = _WmsCellID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 8),
    _WmsCellID_Type()
)
wmsCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsCellID.setStatus("current")
_WmsIMSI_Type = DisplayString
_WmsIMSI_Object = MibScalar
wmsIMSI = _WmsIMSI_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 9),
    _WmsIMSI_Type()
)
wmsIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsIMSI.setStatus("current")
_WmsPhnum_Type = DisplayString
_WmsPhnum_Object = MibScalar
wmsPhnum = _WmsPhnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 10),
    _WmsPhnum_Type()
)
wmsPhnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsPhnum.setStatus("current")
_WmsLocalIP_Type = DisplayString
_WmsLocalIP_Object = MibScalar
wmsLocalIP = _WmsLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 11),
    _WmsLocalIP_Type()
)
wmsLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsLocalIP.setStatus("current")
_WmsMgfID_Type = DisplayString
_WmsMgfID_Object = MibScalar
wmsMgfID = _WmsMgfID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 12),
    _WmsMgfID_Type()
)
wmsMgfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsMgfID.setStatus("current")
_WmsModelID_Type = DisplayString
_WmsModelID_Object = MibScalar
wmsModelID = _WmsModelID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 13),
    _WmsModelID_Type()
)
wmsModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsModelID.setStatus("current")
_WmsIMEI_Type = DisplayString
_WmsIMEI_Object = MibScalar
wmsIMEI = _WmsIMEI_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 14),
    _WmsIMEI_Type()
)
wmsIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsIMEI.setStatus("current")
_WmsRevID_Type = DisplayString
_WmsRevID_Object = MibScalar
wmsRevID = _WmsRevID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 15),
    _WmsRevID_Type()
)
wmsRevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsRevID.setStatus("current")
_WmsNetName_Type = DisplayString
_WmsNetName_Object = MibScalar
wmsNetName = _WmsNetName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 16),
    _WmsNetName_Type()
)
wmsNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsNetName.setStatus("current")
_WmsGPRSStatus_Type = DisplayString
_WmsGPRSStatus_Object = MibScalar
wmsGPRSStatus = _WmsGPRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 17),
    _WmsGPRSStatus_Type()
)
wmsGPRSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsGPRSStatus.setStatus("current")
_WmsBand_Type = DisplayString
_WmsBand_Object = MibScalar
wmsBand = _WmsBand_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 18),
    _WmsBand_Type()
)
wmsBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBand.setStatus("current")
_WmsChannel_Type = DisplayString
_WmsChannel_Object = MibScalar
wmsChannel = _WmsChannel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 19),
    _WmsChannel_Type()
)
wmsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsChannel.setStatus("current")
_WmsCountryCode_Type = DisplayString
_WmsCountryCode_Object = MibScalar
wmsCountryCode = _WmsCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 20),
    _WmsCountryCode_Type()
)
wmsCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsCountryCode.setStatus("current")
_WmsNetCode_Type = DisplayString
_WmsNetCode_Object = MibScalar
wmsNetCode = _WmsNetCode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 21),
    _WmsNetCode_Type()
)
wmsNetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsNetCode.setStatus("current")
_WmsPLMNColor_Type = DisplayString
_WmsPLMNColor_Object = MibScalar
wmsPLMNColor = _WmsPLMNColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 22),
    _WmsPLMNColor_Type()
)
wmsPLMNColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsPLMNColor.setStatus("current")
_WmsBScolor_Type = DisplayString
_WmsBScolor_Object = MibScalar
wmsBScolor = _WmsBScolor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 23),
    _WmsBScolor_Type()
)
wmsBScolor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBScolor.setStatus("current")
_WmsMpRACH_Type = DisplayString
_WmsMpRACH_Object = MibScalar
wmsMpRACH = _WmsMpRACH_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 24),
    _WmsMpRACH_Type()
)
wmsMpRACH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsMpRACH.setStatus("current")
_WmsMinRxLevel_Type = DisplayString
_WmsMinRxLevel_Object = MibScalar
wmsMinRxLevel = _WmsMinRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 25),
    _WmsMinRxLevel_Type()
)
wmsMinRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsMinRxLevel.setStatus("current")
_WmsBaseCoeff_Type = DisplayString
_WmsBaseCoeff_Object = MibScalar
wmsBaseCoeff = _WmsBaseCoeff_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 26),
    _WmsBaseCoeff_Type()
)
wmsBaseCoeff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBaseCoeff.setStatus("current")
_WmsSIMStatus_Type = DisplayString
_WmsSIMStatus_Object = MibScalar
wmsSIMStatus = _WmsSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 27),
    _WmsSIMStatus_Type()
)
wmsSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsSIMStatus.setStatus("current")
_WmsICCID_Type = DisplayString
_WmsICCID_Object = MibScalar
wmsICCID = _WmsICCID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 28),
    _WmsICCID_Type()
)
wmsICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsICCID.setStatus("current")
_WmsModemType_Type = DisplayString
_WmsModemType_Object = MibScalar
wmsModemType = _WmsModemType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 7, 29),
    _WmsModemType_Type()
)
wmsModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsModemType.setStatus("current")
_AcPowerMonitorStatus_ObjectIdentity = ObjectIdentity
acPowerMonitorStatus = _AcPowerMonitorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8)
)
_AcpmStatusTable_Object = MibTable
acpmStatusTable = _AcpmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1)
)
if mibBuilder.loadTexts:
    acpmStatusTable.setStatus("current")
_AcpmStatusEntry_Object = MibTableRow
acpmStatusEntry = _AcpmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1)
)
acpmStatusEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmsIndex"),
)
if mibBuilder.loadTexts:
    acpmStatusEntry.setStatus("current")


class _AcpmsIndex_Type(Integer32):
    """Custom type acpmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmsIndex_Type.__name__ = "Integer32"
_AcpmsIndex_Object = MibTableColumn
acpmsIndex = _AcpmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 1),
    _AcpmsIndex_Type()
)
acpmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsIndex.setStatus("current")
_AcpmsName_Type = DisplayString
_AcpmsName_Object = MibTableColumn
acpmsName = _AcpmsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 2),
    _AcpmsName_Type()
)
acpmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsName.setStatus("current")
_AcpmsAvgVoltageValueStr_Type = DisplayString
_AcpmsAvgVoltageValueStr_Object = MibTableColumn
acpmsAvgVoltageValueStr = _AcpmsAvgVoltageValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 3),
    _AcpmsAvgVoltageValueStr_Type()
)
acpmsAvgVoltageValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageValueStr.setStatus("current")
_AcpmsAvgVoltageMinStr_Type = DisplayString
_AcpmsAvgVoltageMinStr_Object = MibTableColumn
acpmsAvgVoltageMinStr = _AcpmsAvgVoltageMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 4),
    _AcpmsAvgVoltageMinStr_Type()
)
acpmsAvgVoltageMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageMinStr.setStatus("current")
_AcpmsAvgVoltageMaxStr_Type = DisplayString
_AcpmsAvgVoltageMaxStr_Object = MibTableColumn
acpmsAvgVoltageMaxStr = _AcpmsAvgVoltageMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 5),
    _AcpmsAvgVoltageMaxStr_Type()
)
acpmsAvgVoltageMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageMaxStr.setStatus("current")
_AcpmsAvgVoltageAvgStr_Type = DisplayString
_AcpmsAvgVoltageAvgStr_Object = MibTableColumn
acpmsAvgVoltageAvgStr = _AcpmsAvgVoltageAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 6),
    _AcpmsAvgVoltageAvgStr_Type()
)
acpmsAvgVoltageAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageAvgStr.setStatus("current")
_AcpmsAvgVoltageInEventState_Type = DisplayString
_AcpmsAvgVoltageInEventState_Object = MibTableColumn
acpmsAvgVoltageInEventState = _AcpmsAvgVoltageInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 7),
    _AcpmsAvgVoltageInEventState_Type()
)
acpmsAvgVoltageInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageInEventState.setStatus("current")
_AcpmsVoltagePhaseAValueStr_Type = DisplayString
_AcpmsVoltagePhaseAValueStr_Object = MibTableColumn
acpmsVoltagePhaseAValueStr = _AcpmsVoltagePhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 8),
    _AcpmsVoltagePhaseAValueStr_Type()
)
acpmsVoltagePhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsVoltagePhaseAValueStr.setStatus("current")
_AcpmsVoltagePhaseBValueStr_Type = DisplayString
_AcpmsVoltagePhaseBValueStr_Object = MibTableColumn
acpmsVoltagePhaseBValueStr = _AcpmsVoltagePhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 9),
    _AcpmsVoltagePhaseBValueStr_Type()
)
acpmsVoltagePhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsVoltagePhaseBValueStr.setStatus("current")
_AcpmsVoltagePhaseCValueStr_Type = DisplayString
_AcpmsVoltagePhaseCValueStr_Object = MibTableColumn
acpmsVoltagePhaseCValueStr = _AcpmsVoltagePhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 10),
    _AcpmsVoltagePhaseCValueStr_Type()
)
acpmsVoltagePhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsVoltagePhaseCValueStr.setStatus("current")
_AcpmsAvgCurrentValueStr_Type = DisplayString
_AcpmsAvgCurrentValueStr_Object = MibTableColumn
acpmsAvgCurrentValueStr = _AcpmsAvgCurrentValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 11),
    _AcpmsAvgCurrentValueStr_Type()
)
acpmsAvgCurrentValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentValueStr.setStatus("current")
_AcpmsAvgCurrentMinStr_Type = DisplayString
_AcpmsAvgCurrentMinStr_Object = MibTableColumn
acpmsAvgCurrentMinStr = _AcpmsAvgCurrentMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 12),
    _AcpmsAvgCurrentMinStr_Type()
)
acpmsAvgCurrentMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentMinStr.setStatus("current")
_AcpmsAvgCurrentMaxStr_Type = DisplayString
_AcpmsAvgCurrentMaxStr_Object = MibTableColumn
acpmsAvgCurrentMaxStr = _AcpmsAvgCurrentMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 13),
    _AcpmsAvgCurrentMaxStr_Type()
)
acpmsAvgCurrentMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentMaxStr.setStatus("current")
_AcpmsAvgCurrentAvgStr_Type = DisplayString
_AcpmsAvgCurrentAvgStr_Object = MibTableColumn
acpmsAvgCurrentAvgStr = _AcpmsAvgCurrentAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 14),
    _AcpmsAvgCurrentAvgStr_Type()
)
acpmsAvgCurrentAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentAvgStr.setStatus("current")
_AcpmsAvgCurrentInEventState_Type = DisplayString
_AcpmsAvgCurrentInEventState_Object = MibTableColumn
acpmsAvgCurrentInEventState = _AcpmsAvgCurrentInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 15),
    _AcpmsAvgCurrentInEventState_Type()
)
acpmsAvgCurrentInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentInEventState.setStatus("current")
_AcpmsCurrentPhaseAValueStr_Type = DisplayString
_AcpmsCurrentPhaseAValueStr_Object = MibTableColumn
acpmsCurrentPhaseAValueStr = _AcpmsCurrentPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 16),
    _AcpmsCurrentPhaseAValueStr_Type()
)
acpmsCurrentPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCurrentPhaseAValueStr.setStatus("current")
_AcpmsCurrentPhaseBValueStr_Type = DisplayString
_AcpmsCurrentPhaseBValueStr_Object = MibTableColumn
acpmsCurrentPhaseBValueStr = _AcpmsCurrentPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 17),
    _AcpmsCurrentPhaseBValueStr_Type()
)
acpmsCurrentPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCurrentPhaseBValueStr.setStatus("current")
_AcpmsCurrentPhaseCValueStr_Type = DisplayString
_AcpmsCurrentPhaseCValueStr_Object = MibTableColumn
acpmsCurrentPhaseCValueStr = _AcpmsCurrentPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 18),
    _AcpmsCurrentPhaseCValueStr_Type()
)
acpmsCurrentPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCurrentPhaseCValueStr.setStatus("current")
_AcpmsAvgFreqValueStr_Type = DisplayString
_AcpmsAvgFreqValueStr_Object = MibTableColumn
acpmsAvgFreqValueStr = _AcpmsAvgFreqValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 19),
    _AcpmsAvgFreqValueStr_Type()
)
acpmsAvgFreqValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqValueStr.setStatus("current")
_AcpmsAvgFreqMinStr_Type = DisplayString
_AcpmsAvgFreqMinStr_Object = MibTableColumn
acpmsAvgFreqMinStr = _AcpmsAvgFreqMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 20),
    _AcpmsAvgFreqMinStr_Type()
)
acpmsAvgFreqMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqMinStr.setStatus("current")
_AcpmsAvgFreqMaxStr_Type = DisplayString
_AcpmsAvgFreqMaxStr_Object = MibTableColumn
acpmsAvgFreqMaxStr = _AcpmsAvgFreqMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 21),
    _AcpmsAvgFreqMaxStr_Type()
)
acpmsAvgFreqMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqMaxStr.setStatus("current")
_AcpmsAvgFreqAvgStr_Type = DisplayString
_AcpmsAvgFreqAvgStr_Object = MibTableColumn
acpmsAvgFreqAvgStr = _AcpmsAvgFreqAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 22),
    _AcpmsAvgFreqAvgStr_Type()
)
acpmsAvgFreqAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqAvgStr.setStatus("current")
_AcpmsAvgFreqInEventState_Type = DisplayString
_AcpmsAvgFreqInEventState_Object = MibTableColumn
acpmsAvgFreqInEventState = _AcpmsAvgFreqInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 23),
    _AcpmsAvgFreqInEventState_Type()
)
acpmsAvgFreqInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqInEventState.setStatus("current")
_AcpmsTRPValueStr_Type = DisplayString
_AcpmsTRPValueStr_Object = MibTableColumn
acpmsTRPValueStr = _AcpmsTRPValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 24),
    _AcpmsTRPValueStr_Type()
)
acpmsTRPValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPValueStr.setStatus("current")
_AcpmsTRPMinStr_Type = DisplayString
_AcpmsTRPMinStr_Object = MibTableColumn
acpmsTRPMinStr = _AcpmsTRPMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 25),
    _AcpmsTRPMinStr_Type()
)
acpmsTRPMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPMinStr.setStatus("current")
_AcpmsTRPMaxStr_Type = DisplayString
_AcpmsTRPMaxStr_Object = MibTableColumn
acpmsTRPMaxStr = _AcpmsTRPMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 26),
    _AcpmsTRPMaxStr_Type()
)
acpmsTRPMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPMaxStr.setStatus("current")
_AcpmsTRPAvgStr_Type = DisplayString
_AcpmsTRPAvgStr_Object = MibTableColumn
acpmsTRPAvgStr = _AcpmsTRPAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 27),
    _AcpmsTRPAvgStr_Type()
)
acpmsTRPAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPAvgStr.setStatus("current")
_AcpmsTRPInEventState_Type = DisplayString
_AcpmsTRPInEventState_Object = MibTableColumn
acpmsTRPInEventState = _AcpmsTRPInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 28),
    _AcpmsTRPInEventState_Type()
)
acpmsTRPInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPInEventState.setStatus("current")
_AcpmsRPPhaseAValueStr_Type = DisplayString
_AcpmsRPPhaseAValueStr_Object = MibTableColumn
acpmsRPPhaseAValueStr = _AcpmsRPPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 29),
    _AcpmsRPPhaseAValueStr_Type()
)
acpmsRPPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRPPhaseAValueStr.setStatus("current")
_AcpmsRPPhaseBValueStr_Type = DisplayString
_AcpmsRPPhaseBValueStr_Object = MibTableColumn
acpmsRPPhaseBValueStr = _AcpmsRPPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 30),
    _AcpmsRPPhaseBValueStr_Type()
)
acpmsRPPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRPPhaseBValueStr.setStatus("current")
_AcpmsRPPhaseCValueStr_Type = DisplayString
_AcpmsRPPhaseCValueStr_Object = MibTableColumn
acpmsRPPhaseCValueStr = _AcpmsRPPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 31),
    _AcpmsRPPhaseCValueStr_Type()
)
acpmsRPPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRPPhaseCValueStr.setStatus("current")
_AcpmsCombined_Type = DisplayString
_AcpmsCombined_Object = MibTableColumn
acpmsCombined = _AcpmsCombined_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 32),
    _AcpmsCombined_Type()
)
acpmsCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCombined.setStatus("current")
_AcpmsTPFValueStr_Type = DisplayString
_AcpmsTPFValueStr_Object = MibTableColumn
acpmsTPFValueStr = _AcpmsTPFValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 33),
    _AcpmsTPFValueStr_Type()
)
acpmsTPFValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFValueStr.setStatus("current")
_AcpmsTPFMinStr_Type = DisplayString
_AcpmsTPFMinStr_Object = MibTableColumn
acpmsTPFMinStr = _AcpmsTPFMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 34),
    _AcpmsTPFMinStr_Type()
)
acpmsTPFMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFMinStr.setStatus("current")
_AcpmsTPFMaxStr_Type = DisplayString
_AcpmsTPFMaxStr_Object = MibTableColumn
acpmsTPFMaxStr = _AcpmsTPFMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 35),
    _AcpmsTPFMaxStr_Type()
)
acpmsTPFMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFMaxStr.setStatus("current")
_AcpmsTPFAvgStr_Type = DisplayString
_AcpmsTPFAvgStr_Object = MibTableColumn
acpmsTPFAvgStr = _AcpmsTPFAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 36),
    _AcpmsTPFAvgStr_Type()
)
acpmsTPFAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFAvgStr.setStatus("current")
_AcpmsTPFInEventState_Type = DisplayString
_AcpmsTPFInEventState_Object = MibTableColumn
acpmsTPFInEventState = _AcpmsTPFInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 37),
    _AcpmsTPFInEventState_Type()
)
acpmsTPFInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFInEventState.setStatus("current")
_AcpmsPFPhaseAValueStr_Type = DisplayString
_AcpmsPFPhaseAValueStr_Object = MibTableColumn
acpmsPFPhaseAValueStr = _AcpmsPFPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 38),
    _AcpmsPFPhaseAValueStr_Type()
)
acpmsPFPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsPFPhaseAValueStr.setStatus("current")
_AcpmsPFPhaseBValueStr_Type = DisplayString
_AcpmsPFPhaseBValueStr_Object = MibTableColumn
acpmsPFPhaseBValueStr = _AcpmsPFPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 39),
    _AcpmsPFPhaseBValueStr_Type()
)
acpmsPFPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsPFPhaseBValueStr.setStatus("current")
_AcpmsPFPhaseCValueStr_Type = DisplayString
_AcpmsPFPhaseCValueStr_Object = MibTableColumn
acpmsPFPhaseCValueStr = _AcpmsPFPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 40),
    _AcpmsPFPhaseCValueStr_Type()
)
acpmsPFPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsPFPhaseCValueStr.setStatus("current")
_AcpmsTRcPValueStr_Type = DisplayString
_AcpmsTRcPValueStr_Object = MibTableColumn
acpmsTRcPValueStr = _AcpmsTRcPValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 41),
    _AcpmsTRcPValueStr_Type()
)
acpmsTRcPValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPValueStr.setStatus("current")
_AcpmsTRcPMinStr_Type = DisplayString
_AcpmsTRcPMinStr_Object = MibTableColumn
acpmsTRcPMinStr = _AcpmsTRcPMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 42),
    _AcpmsTRcPMinStr_Type()
)
acpmsTRcPMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPMinStr.setStatus("current")
_AcpmsTRcPMaxStr_Type = DisplayString
_AcpmsTRcPMaxStr_Object = MibTableColumn
acpmsTRcPMaxStr = _AcpmsTRcPMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 43),
    _AcpmsTRcPMaxStr_Type()
)
acpmsTRcPMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPMaxStr.setStatus("current")
_AcpmsTRcPAvgStr_Type = DisplayString
_AcpmsTRcPAvgStr_Object = MibTableColumn
acpmsTRcPAvgStr = _AcpmsTRcPAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 44),
    _AcpmsTRcPAvgStr_Type()
)
acpmsTRcPAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPAvgStr.setStatus("current")
_AcpmsRcPPhaseAValueStr_Type = DisplayString
_AcpmsRcPPhaseAValueStr_Object = MibTableColumn
acpmsRcPPhaseAValueStr = _AcpmsRcPPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 45),
    _AcpmsRcPPhaseAValueStr_Type()
)
acpmsRcPPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRcPPhaseAValueStr.setStatus("current")
_AcpmsRcPPhaseBValueStr_Type = DisplayString
_AcpmsRcPPhaseBValueStr_Object = MibTableColumn
acpmsRcPPhaseBValueStr = _AcpmsRcPPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 46),
    _AcpmsRcPPhaseBValueStr_Type()
)
acpmsRcPPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRcPPhaseBValueStr.setStatus("current")
_AcpmsRcPPhaseCValueStr_Type = DisplayString
_AcpmsRcPPhaseCValueStr_Object = MibTableColumn
acpmsRcPPhaseCValueStr = _AcpmsRcPPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 47),
    _AcpmsRcPPhaseCValueStr_Type()
)
acpmsRcPPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRcPPhaseCValueStr.setStatus("current")
_AcpmsTAPValueStr_Type = DisplayString
_AcpmsTAPValueStr_Object = MibTableColumn
acpmsTAPValueStr = _AcpmsTAPValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 48),
    _AcpmsTAPValueStr_Type()
)
acpmsTAPValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPValueStr.setStatus("current")
_AcpmsTAPMinStr_Type = DisplayString
_AcpmsTAPMinStr_Object = MibTableColumn
acpmsTAPMinStr = _AcpmsTAPMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 49),
    _AcpmsTAPMinStr_Type()
)
acpmsTAPMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPMinStr.setStatus("current")
_AcpmsTAPMaxStr_Type = DisplayString
_AcpmsTAPMaxStr_Object = MibTableColumn
acpmsTAPMaxStr = _AcpmsTAPMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 50),
    _AcpmsTAPMaxStr_Type()
)
acpmsTAPMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPMaxStr.setStatus("current")
_AcpmsTAPAvgStr_Type = DisplayString
_AcpmsTAPAvgStr_Object = MibTableColumn
acpmsTAPAvgStr = _AcpmsTAPAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 51),
    _AcpmsTAPAvgStr_Type()
)
acpmsTAPAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPAvgStr.setStatus("current")
_AcpmsAPPhaseAValueStr_Type = DisplayString
_AcpmsAPPhaseAValueStr_Object = MibTableColumn
acpmsAPPhaseAValueStr = _AcpmsAPPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 52),
    _AcpmsAPPhaseAValueStr_Type()
)
acpmsAPPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAPPhaseAValueStr.setStatus("current")
_AcpmsAPPhaseBValueStr_Type = DisplayString
_AcpmsAPPhaseBValueStr_Object = MibTableColumn
acpmsAPPhaseBValueStr = _AcpmsAPPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 53),
    _AcpmsAPPhaseBValueStr_Type()
)
acpmsAPPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAPPhaseBValueStr.setStatus("current")
_AcpmsAPPhaseCValueStr_Type = DisplayString
_AcpmsAPPhaseCValueStr_Object = MibTableColumn
acpmsAPPhaseCValueStr = _AcpmsAPPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 54),
    _AcpmsAPPhaseCValueStr_Type()
)
acpmsAPPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAPPhaseCValueStr.setStatus("current")
_AcpmsTotalEnergyWh_Type = Integer32
_AcpmsTotalEnergyWh_Object = MibTableColumn
acpmsTotalEnergyWh = _AcpmsTotalEnergyWh_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 55),
    _AcpmsTotalEnergyWh_Type()
)
acpmsTotalEnergyWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTotalEnergyWh.setStatus("current")
_AcpmsTotalEnergyVAR_Type = Integer32
_AcpmsTotalEnergyVAR_Object = MibTableColumn
acpmsTotalEnergyVAR = _AcpmsTotalEnergyVAR_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 56),
    _AcpmsTotalEnergyVAR_Type()
)
acpmsTotalEnergyVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTotalEnergyVAR.setStatus("current")
_AcpmsTotalEnergyVA_Type = Integer32
_AcpmsTotalEnergyVA_Object = MibTableColumn
acpmsTotalEnergyVA = _AcpmsTotalEnergyVA_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1, 8, 1, 1, 57),
    _AcpmsTotalEnergyVA_Type()
)
acpmsTotalEnergyVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTotalEnergyVA.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2)
)
_EventSensorBasics_ObjectIdentity = ObjectIdentity
eventSensorBasics = _EventSensorBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1)
)
_EsNumberEventSensors_Type = Integer32
_EsNumberEventSensors_Object = MibScalar
esNumberEventSensors = _EsNumberEventSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 1),
    _EsNumberEventSensors_Type()
)
esNumberEventSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberEventSensors.setStatus("current")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2)
)
if mibBuilder.loadTexts:
    esTable.setStatus("current")
_EsEntry_Object = MibTableRow
esEntry = _EsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1)
)
esEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "esIndex"),
)
if mibBuilder.loadTexts:
    esEntry.setStatus("current")


class _EsIndex_Type(Integer32):
    """Custom type esIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EsIndex_Type.__name__ = "Integer32"
_EsIndex_Object = MibTableColumn
esIndex = _EsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 1),
    _EsIndex_Type()
)
esIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndex.setStatus("current")
_EsName_Type = DisplayString
_EsName_Object = MibTableColumn
esName = _EsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 2),
    _EsName_Type()
)
esName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esName.setStatus("current")
_EsID_Type = DisplayString
_EsID_Object = MibTableColumn
esID = _EsID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 3),
    _EsID_Type()
)
esID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esID.setStatus("current")
_EsNumberTempSensors_Type = Integer32
_EsNumberTempSensors_Object = MibTableColumn
esNumberTempSensors = _EsNumberTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 4),
    _EsNumberTempSensors_Type()
)
esNumberTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberTempSensors.setStatus("current")
_EsTempReportingMode_Type = DisplayString
_EsTempReportingMode_Object = MibTableColumn
esTempReportingMode = _EsTempReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 5),
    _EsTempReportingMode_Type()
)
esTempReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTempReportingMode.setStatus("current")
_EsNumberCCs_Type = Integer32
_EsNumberCCs_Object = MibTableColumn
esNumberCCs = _EsNumberCCs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 6),
    _EsNumberCCs_Type()
)
esNumberCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberCCs.setStatus("current")
_EsCCReportingMode_Type = DisplayString
_EsCCReportingMode_Object = MibTableColumn
esCCReportingMode = _EsCCReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 7),
    _EsCCReportingMode_Type()
)
esCCReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCReportingMode.setStatus("current")
_EsNumberHumidSensors_Type = Integer32
_EsNumberHumidSensors_Object = MibTableColumn
esNumberHumidSensors = _EsNumberHumidSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 8),
    _EsNumberHumidSensors_Type()
)
esNumberHumidSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberHumidSensors.setStatus("current")
_EsHumidReportingMode_Type = DisplayString
_EsHumidReportingMode_Object = MibTableColumn
esHumidReportingMode = _EsHumidReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 9),
    _EsHumidReportingMode_Type()
)
esHumidReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHumidReportingMode.setStatus("current")
_EsNumberNoiseSensors_Type = Integer32
_EsNumberNoiseSensors_Object = MibTableColumn
esNumberNoiseSensors = _EsNumberNoiseSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 10),
    _EsNumberNoiseSensors_Type()
)
esNumberNoiseSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberNoiseSensors.setStatus("current")
_EsNoiseReportingMode_Type = DisplayString
_EsNoiseReportingMode_Object = MibTableColumn
esNoiseReportingMode = _EsNoiseReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 11),
    _EsNoiseReportingMode_Type()
)
esNoiseReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNoiseReportingMode.setStatus("current")
_EsNumberAirflowSensors_Type = Integer32
_EsNumberAirflowSensors_Object = MibTableColumn
esNumberAirflowSensors = _EsNumberAirflowSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 12),
    _EsNumberAirflowSensors_Type()
)
esNumberAirflowSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAirflowSensors.setStatus("current")
_EsAirflowReportingMode_Type = DisplayString
_EsAirflowReportingMode_Object = MibTableColumn
esAirflowReportingMode = _EsAirflowReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 13),
    _EsAirflowReportingMode_Type()
)
esAirflowReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAirflowReportingMode.setStatus("current")
_EsNumberAnalog_Type = Integer32
_EsNumberAnalog_Object = MibTableColumn
esNumberAnalog = _EsNumberAnalog_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 14),
    _EsNumberAnalog_Type()
)
esNumberAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAnalog.setStatus("current")
_EsAnalogReportingMode_Type = DisplayString
_EsAnalogReportingMode_Object = MibTableColumn
esAnalogReportingMode = _EsAnalogReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 15),
    _EsAnalogReportingMode_Type()
)
esAnalogReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogReportingMode.setStatus("current")
_EsNumberOutputs_Type = Integer32
_EsNumberOutputs_Object = MibTableColumn
esNumberOutputs = _EsNumberOutputs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 16),
    _EsNumberOutputs_Type()
)
esNumberOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberOutputs.setStatus("current")
_EsOutputReportingMode_Type = DisplayString
_EsOutputReportingMode_Object = MibTableColumn
esOutputReportingMode = _EsOutputReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 17),
    _EsOutputReportingMode_Type()
)
esOutputReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esOutputReportingMode.setStatus("current")
_EsTempCombinedStatus_Type = DisplayString
_EsTempCombinedStatus_Object = MibTableColumn
esTempCombinedStatus = _EsTempCombinedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 18),
    _EsTempCombinedStatus_Type()
)
esTempCombinedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTempCombinedStatus.setStatus("current")
_EsCCCombinedStatusBlock1_Type = DisplayString
_EsCCCombinedStatusBlock1_Object = MibTableColumn
esCCCombinedStatusBlock1 = _EsCCCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 19),
    _EsCCCombinedStatusBlock1_Type()
)
esCCCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock1.setStatus("current")
_EsCCCombinedStatusBlock2_Type = DisplayString
_EsCCCombinedStatusBlock2_Object = MibTableColumn
esCCCombinedStatusBlock2 = _EsCCCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 20),
    _EsCCCombinedStatusBlock2_Type()
)
esCCCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock2.setStatus("current")
_EsCCCombinedStatusBlock3_Type = DisplayString
_EsCCCombinedStatusBlock3_Object = MibTableColumn
esCCCombinedStatusBlock3 = _EsCCCombinedStatusBlock3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 21),
    _EsCCCombinedStatusBlock3_Type()
)
esCCCombinedStatusBlock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock3.setStatus("current")
_EsCCCombinedStatusBlock4_Type = DisplayString
_EsCCCombinedStatusBlock4_Object = MibTableColumn
esCCCombinedStatusBlock4 = _EsCCCombinedStatusBlock4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 22),
    _EsCCCombinedStatusBlock4_Type()
)
esCCCombinedStatusBlock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock4.setStatus("current")
_EsCCCombinedStatusBlock5_Type = DisplayString
_EsCCCombinedStatusBlock5_Object = MibTableColumn
esCCCombinedStatusBlock5 = _EsCCCombinedStatusBlock5_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 23),
    _EsCCCombinedStatusBlock5_Type()
)
esCCCombinedStatusBlock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock5.setStatus("current")
_EsCCCombinedStatusBlock6_Type = DisplayString
_EsCCCombinedStatusBlock6_Object = MibTableColumn
esCCCombinedStatusBlock6 = _EsCCCombinedStatusBlock6_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 24),
    _EsCCCombinedStatusBlock6_Type()
)
esCCCombinedStatusBlock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock6.setStatus("current")
_EsCCCombinedStatusBlock7_Type = DisplayString
_EsCCCombinedStatusBlock7_Object = MibTableColumn
esCCCombinedStatusBlock7 = _EsCCCombinedStatusBlock7_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 25),
    _EsCCCombinedStatusBlock7_Type()
)
esCCCombinedStatusBlock7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock7.setStatus("current")
_EsCCCombinedStatusBlock8_Type = DisplayString
_EsCCCombinedStatusBlock8_Object = MibTableColumn
esCCCombinedStatusBlock8 = _EsCCCombinedStatusBlock8_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 26),
    _EsCCCombinedStatusBlock8_Type()
)
esCCCombinedStatusBlock8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock8.setStatus("current")
_EsHumidCombinedStatus_Type = DisplayString
_EsHumidCombinedStatus_Object = MibTableColumn
esHumidCombinedStatus = _EsHumidCombinedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 27),
    _EsHumidCombinedStatus_Type()
)
esHumidCombinedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHumidCombinedStatus.setStatus("current")
_EsAnalogCombinedStatusBlock1_Type = DisplayString
_EsAnalogCombinedStatusBlock1_Object = MibTableColumn
esAnalogCombinedStatusBlock1 = _EsAnalogCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 28),
    _EsAnalogCombinedStatusBlock1_Type()
)
esAnalogCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock1.setStatus("current")
_EsAnalogCombinedStatusBlock2_Type = DisplayString
_EsAnalogCombinedStatusBlock2_Object = MibTableColumn
esAnalogCombinedStatusBlock2 = _EsAnalogCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 29),
    _EsAnalogCombinedStatusBlock2_Type()
)
esAnalogCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock2.setStatus("current")
_EsAnalogCombinedStatusBlock3_Type = DisplayString
_EsAnalogCombinedStatusBlock3_Object = MibTableColumn
esAnalogCombinedStatusBlock3 = _EsAnalogCombinedStatusBlock3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 30),
    _EsAnalogCombinedStatusBlock3_Type()
)
esAnalogCombinedStatusBlock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock3.setStatus("current")
_EsAnalogCombinedStatusBlock4_Type = DisplayString
_EsAnalogCombinedStatusBlock4_Object = MibTableColumn
esAnalogCombinedStatusBlock4 = _EsAnalogCombinedStatusBlock4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 31),
    _EsAnalogCombinedStatusBlock4_Type()
)
esAnalogCombinedStatusBlock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock4.setStatus("current")
_EsAnalogCombinedStatusBlock5_Type = DisplayString
_EsAnalogCombinedStatusBlock5_Object = MibTableColumn
esAnalogCombinedStatusBlock5 = _EsAnalogCombinedStatusBlock5_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 32),
    _EsAnalogCombinedStatusBlock5_Type()
)
esAnalogCombinedStatusBlock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock5.setStatus("current")
_EsAnalogCombinedStatusBlock6_Type = DisplayString
_EsAnalogCombinedStatusBlock6_Object = MibTableColumn
esAnalogCombinedStatusBlock6 = _EsAnalogCombinedStatusBlock6_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 33),
    _EsAnalogCombinedStatusBlock6_Type()
)
esAnalogCombinedStatusBlock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock6.setStatus("current")
_EsOutputCombinedStatusBlock1_Type = DisplayString
_EsOutputCombinedStatusBlock1_Object = MibTableColumn
esOutputCombinedStatusBlock1 = _EsOutputCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 34),
    _EsOutputCombinedStatusBlock1_Type()
)
esOutputCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esOutputCombinedStatusBlock1.setStatus("current")
_EsOutputCombinedStatusBlock2_Type = DisplayString
_EsOutputCombinedStatusBlock2_Object = MibTableColumn
esOutputCombinedStatusBlock2 = _EsOutputCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 2, 1, 35),
    _EsOutputCombinedStatusBlock2_Type()
)
esOutputCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esOutputCombinedStatusBlock2.setStatus("current")
_EsNewSensors_Type = DisplayString
_EsNewSensors_Object = MibScalar
esNewSensors = _EsNewSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 1, 3),
    _EsNewSensors_Type()
)
esNewSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNewSensors.setStatus("current")
_EventSensorPointConfig_ObjectIdentity = ObjectIdentity
eventSensorPointConfig = _EventSensorPointConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2)
)
_EsPointConfigTempTable_Object = MibTable
esPointConfigTempTable = _EsPointConfigTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1)
)
if mibBuilder.loadTexts:
    esPointConfigTempTable.setStatus("current")
_EsPointConfigTempEntry_Object = MibTableRow
esPointConfigTempEntry = _EsPointConfigTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1)
)
esPointConfigTempEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "espcTempIndexES"),
    (0, "SITEBOSS-570-STD-MIB", "espcTempIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigTempEntry.setStatus("current")


class _EspcTempIndexES_Type(Integer32):
    """Custom type espcTempIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcTempIndexES_Type.__name__ = "Integer32"
_EspcTempIndexES_Object = MibTableColumn
espcTempIndexES = _EspcTempIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 1),
    _EspcTempIndexES_Type()
)
espcTempIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcTempIndexES.setStatus("current")


class _EspcTempIndexPoint_Type(Integer32):
    """Custom type espcTempIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcTempIndexPoint_Type.__name__ = "Integer32"
_EspcTempIndexPoint_Object = MibTableColumn
espcTempIndexPoint = _EspcTempIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 2),
    _EspcTempIndexPoint_Type()
)
espcTempIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcTempIndexPoint.setStatus("current")
_EspcTempEnable_Type = DisplayString
_EspcTempEnable_Object = MibTableColumn
espcTempEnable = _EspcTempEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 3),
    _EspcTempEnable_Type()
)
espcTempEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempEnable.setStatus("current")
_EspcTempScale_Type = DisplayString
_EspcTempScale_Object = MibTableColumn
espcTempScale = _EspcTempScale_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 4),
    _EspcTempScale_Type()
)
espcTempScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempScale.setStatus("current")
_EspcTempDeadband_Type = DisplayString
_EspcTempDeadband_Object = MibTableColumn
espcTempDeadband = _EspcTempDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 5),
    _EspcTempDeadband_Type()
)
espcTempDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempDeadband.setStatus("current")
_EspcTempVHighTemp_Type = DisplayString
_EspcTempVHighTemp_Object = MibTableColumn
espcTempVHighTemp = _EspcTempVHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 6),
    _EspcTempVHighTemp_Type()
)
espcTempVHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighTemp.setStatus("current")
_EspcTempVHighActions_Type = DisplayString
_EspcTempVHighActions_Object = MibTableColumn
espcTempVHighActions = _EspcTempVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 7),
    _EspcTempVHighActions_Type()
)
espcTempVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighActions.setStatus("current")
_EspcTempVHighTrapnum_Type = Integer32
_EspcTempVHighTrapnum_Object = MibTableColumn
espcTempVHighTrapnum = _EspcTempVHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 8),
    _EspcTempVHighTrapnum_Type()
)
espcTempVHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighTrapnum.setStatus("current")
_EspcTempVHighClass_Type = DisplayString
_EspcTempVHighClass_Object = MibTableColumn
espcTempVHighClass = _EspcTempVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 9),
    _EspcTempVHighClass_Type()
)
espcTempVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighClass.setStatus("current")
_EspcTempHighTemp_Type = DisplayString
_EspcTempHighTemp_Object = MibTableColumn
espcTempHighTemp = _EspcTempHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 10),
    _EspcTempHighTemp_Type()
)
espcTempHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighTemp.setStatus("current")
_EspcTempHighActions_Type = DisplayString
_EspcTempHighActions_Object = MibTableColumn
espcTempHighActions = _EspcTempHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 11),
    _EspcTempHighActions_Type()
)
espcTempHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighActions.setStatus("current")
_EspcTempHighTrapnum_Type = Integer32
_EspcTempHighTrapnum_Object = MibTableColumn
espcTempHighTrapnum = _EspcTempHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 12),
    _EspcTempHighTrapnum_Type()
)
espcTempHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighTrapnum.setStatus("current")
_EspcTempHighClass_Type = DisplayString
_EspcTempHighClass_Object = MibTableColumn
espcTempHighClass = _EspcTempHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 13),
    _EspcTempHighClass_Type()
)
espcTempHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighClass.setStatus("current")
_EspcTempNormalActions_Type = DisplayString
_EspcTempNormalActions_Object = MibTableColumn
espcTempNormalActions = _EspcTempNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 14),
    _EspcTempNormalActions_Type()
)
espcTempNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempNormalActions.setStatus("current")
_EspcTempNormalTrapnum_Type = Integer32
_EspcTempNormalTrapnum_Object = MibTableColumn
espcTempNormalTrapnum = _EspcTempNormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 15),
    _EspcTempNormalTrapnum_Type()
)
espcTempNormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempNormalTrapnum.setStatus("current")
_EspcTempNormalClass_Type = DisplayString
_EspcTempNormalClass_Object = MibTableColumn
espcTempNormalClass = _EspcTempNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 16),
    _EspcTempNormalClass_Type()
)
espcTempNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempNormalClass.setStatus("current")
_EspcTempLowTemp_Type = DisplayString
_EspcTempLowTemp_Object = MibTableColumn
espcTempLowTemp = _EspcTempLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 17),
    _EspcTempLowTemp_Type()
)
espcTempLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowTemp.setStatus("current")
_EspcTempLowActions_Type = DisplayString
_EspcTempLowActions_Object = MibTableColumn
espcTempLowActions = _EspcTempLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 18),
    _EspcTempLowActions_Type()
)
espcTempLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowActions.setStatus("current")
_EspcTempLowTrapnum_Type = Integer32
_EspcTempLowTrapnum_Object = MibTableColumn
espcTempLowTrapnum = _EspcTempLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 19),
    _EspcTempLowTrapnum_Type()
)
espcTempLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowTrapnum.setStatus("current")
_EspcTempLowClass_Type = DisplayString
_EspcTempLowClass_Object = MibTableColumn
espcTempLowClass = _EspcTempLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 20),
    _EspcTempLowClass_Type()
)
espcTempLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowClass.setStatus("current")
_EspcTempVLowTemp_Type = DisplayString
_EspcTempVLowTemp_Object = MibTableColumn
espcTempVLowTemp = _EspcTempVLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 21),
    _EspcTempVLowTemp_Type()
)
espcTempVLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowTemp.setStatus("current")
_EspcTempVLowActions_Type = DisplayString
_EspcTempVLowActions_Object = MibTableColumn
espcTempVLowActions = _EspcTempVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 22),
    _EspcTempVLowActions_Type()
)
espcTempVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowActions.setStatus("current")
_EspcTempVLowTrapnum_Type = Integer32
_EspcTempVLowTrapnum_Object = MibTableColumn
espcTempVLowTrapnum = _EspcTempVLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 23),
    _EspcTempVLowTrapnum_Type()
)
espcTempVLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowTrapnum.setStatus("current")
_EspcTempVLowClass_Type = DisplayString
_EspcTempVLowClass_Object = MibTableColumn
espcTempVLowClass = _EspcTempVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 1, 1, 24),
    _EspcTempVLowClass_Type()
)
espcTempVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowClass.setStatus("current")
_EsPointConfigCCTable_Object = MibTable
esPointConfigCCTable = _EsPointConfigCCTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2)
)
if mibBuilder.loadTexts:
    esPointConfigCCTable.setStatus("current")
_EsPointConfigCCEntry_Object = MibTableRow
esPointConfigCCEntry = _EsPointConfigCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1)
)
esPointConfigCCEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "espcCCIndexES"),
    (0, "SITEBOSS-570-STD-MIB", "espcCCIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigCCEntry.setStatus("current")


class _EspcCCIndexES_Type(Integer32):
    """Custom type espcCCIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcCCIndexES_Type.__name__ = "Integer32"
_EspcCCIndexES_Object = MibTableColumn
espcCCIndexES = _EspcCCIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 1),
    _EspcCCIndexES_Type()
)
espcCCIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcCCIndexES.setStatus("current")


class _EspcCCIndexPoint_Type(Integer32):
    """Custom type espcCCIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcCCIndexPoint_Type.__name__ = "Integer32"
_EspcCCIndexPoint_Object = MibTableColumn
espcCCIndexPoint = _EspcCCIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 2),
    _EspcCCIndexPoint_Type()
)
espcCCIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcCCIndexPoint.setStatus("current")
_EspcCCEnable_Type = DisplayString
_EspcCCEnable_Object = MibTableColumn
espcCCEnable = _EspcCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 3),
    _EspcCCEnable_Type()
)
espcCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEnable.setStatus("current")
_EspcCCName_Type = DisplayString
_EspcCCName_Object = MibTableColumn
espcCCName = _EspcCCName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 4),
    _EspcCCName_Type()
)
espcCCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCName.setStatus("current")
_EspcCCEventState_Type = DisplayString
_EspcCCEventState_Object = MibTableColumn
espcCCEventState = _EspcCCEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 5),
    _EspcCCEventState_Type()
)
espcCCEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventState.setStatus("current")


class _EspcCCThreshold_Type(Integer32):
    """Custom type espcCCThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EspcCCThreshold_Type.__name__ = "Integer32"
_EspcCCThreshold_Object = MibTableColumn
espcCCThreshold = _EspcCCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 6),
    _EspcCCThreshold_Type()
)
espcCCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCThreshold.setStatus("current")
_EspcCCEventActions_Type = DisplayString
_EspcCCEventActions_Object = MibTableColumn
espcCCEventActions = _EspcCCEventActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 7),
    _EspcCCEventActions_Type()
)
espcCCEventActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventActions.setStatus("current")
_EspcCCEventTrapnum_Type = Integer32
_EspcCCEventTrapnum_Object = MibTableColumn
espcCCEventTrapnum = _EspcCCEventTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 8),
    _EspcCCEventTrapnum_Type()
)
espcCCEventTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventTrapnum.setStatus("current")
_EspcCCEventClass_Type = DisplayString
_EspcCCEventClass_Object = MibTableColumn
espcCCEventClass = _EspcCCEventClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 9),
    _EspcCCEventClass_Type()
)
espcCCEventClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventClass.setStatus("current")
_EspcCCNormalActions_Type = DisplayString
_EspcCCNormalActions_Object = MibTableColumn
espcCCNormalActions = _EspcCCNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 10),
    _EspcCCNormalActions_Type()
)
espcCCNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalActions.setStatus("current")
_EspcCCNormalTrapnum_Type = Integer32
_EspcCCNormalTrapnum_Object = MibTableColumn
espcCCNormalTrapnum = _EspcCCNormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 11),
    _EspcCCNormalTrapnum_Type()
)
espcCCNormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalTrapnum.setStatus("current")
_EspcCCNormalClass_Type = DisplayString
_EspcCCNormalClass_Object = MibTableColumn
espcCCNormalClass = _EspcCCNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 12),
    _EspcCCNormalClass_Type()
)
espcCCNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalClass.setStatus("current")
_EspcCCAlarmAlias_Type = DisplayString
_EspcCCAlarmAlias_Object = MibTableColumn
espcCCAlarmAlias = _EspcCCAlarmAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 13),
    _EspcCCAlarmAlias_Type()
)
espcCCAlarmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCAlarmAlias.setStatus("current")
_EspcCCNormalAlias_Type = DisplayString
_EspcCCNormalAlias_Object = MibTableColumn
espcCCNormalAlias = _EspcCCNormalAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 14),
    _EspcCCNormalAlias_Type()
)
espcCCNormalAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalAlias.setStatus("current")


class _EspcCCNormalThreshold_Type(Integer32):
    """Custom type espcCCNormalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EspcCCNormalThreshold_Type.__name__ = "Integer32"
_EspcCCNormalThreshold_Object = MibTableColumn
espcCCNormalThreshold = _EspcCCNormalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 15),
    _EspcCCNormalThreshold_Type()
)
espcCCNormalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalThreshold.setStatus("current")
_EspcCCOverrideGlobalReminder_Type = DisplayString
_EspcCCOverrideGlobalReminder_Object = MibTableColumn
espcCCOverrideGlobalReminder = _EspcCCOverrideGlobalReminder_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 16),
    _EspcCCOverrideGlobalReminder_Type()
)
espcCCOverrideGlobalReminder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCOverrideGlobalReminder.setStatus("current")
_EspcCCReminderInterval_Type = Integer32
_EspcCCReminderInterval_Object = MibTableColumn
espcCCReminderInterval = _EspcCCReminderInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 2, 1, 17),
    _EspcCCReminderInterval_Type()
)
espcCCReminderInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCReminderInterval.setStatus("current")
_EsPointConfigHumidTable_Object = MibTable
esPointConfigHumidTable = _EsPointConfigHumidTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3)
)
if mibBuilder.loadTexts:
    esPointConfigHumidTable.setStatus("current")
_EsPointConfigHumidEntry_Object = MibTableRow
esPointConfigHumidEntry = _EsPointConfigHumidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1)
)
esPointConfigHumidEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "espcHumidIndexES"),
    (0, "SITEBOSS-570-STD-MIB", "espcHumidIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigHumidEntry.setStatus("current")


class _EspcHumidIndexES_Type(Integer32):
    """Custom type espcHumidIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcHumidIndexES_Type.__name__ = "Integer32"
_EspcHumidIndexES_Object = MibTableColumn
espcHumidIndexES = _EspcHumidIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 1),
    _EspcHumidIndexES_Type()
)
espcHumidIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcHumidIndexES.setStatus("current")


class _EspcHumidIndexPoint_Type(Integer32):
    """Custom type espcHumidIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcHumidIndexPoint_Type.__name__ = "Integer32"
_EspcHumidIndexPoint_Object = MibTableColumn
espcHumidIndexPoint = _EspcHumidIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 2),
    _EspcHumidIndexPoint_Type()
)
espcHumidIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcHumidIndexPoint.setStatus("current")
_EspcHumidEnable_Type = DisplayString
_EspcHumidEnable_Object = MibTableColumn
espcHumidEnable = _EspcHumidEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 3),
    _EspcHumidEnable_Type()
)
espcHumidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidEnable.setStatus("current")
_EspcHumidDeadband_Type = Integer32
_EspcHumidDeadband_Object = MibTableColumn
espcHumidDeadband = _EspcHumidDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 4),
    _EspcHumidDeadband_Type()
)
espcHumidDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidDeadband.setStatus("current")
_EspcHumidVHighHumid_Type = Integer32
_EspcHumidVHighHumid_Object = MibTableColumn
espcHumidVHighHumid = _EspcHumidVHighHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 5),
    _EspcHumidVHighHumid_Type()
)
espcHumidVHighHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighHumid.setStatus("current")
_EspcHumidVHighActions_Type = DisplayString
_EspcHumidVHighActions_Object = MibTableColumn
espcHumidVHighActions = _EspcHumidVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 6),
    _EspcHumidVHighActions_Type()
)
espcHumidVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighActions.setStatus("current")
_EspcHumidVHighTrapnum_Type = Integer32
_EspcHumidVHighTrapnum_Object = MibTableColumn
espcHumidVHighTrapnum = _EspcHumidVHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 7),
    _EspcHumidVHighTrapnum_Type()
)
espcHumidVHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighTrapnum.setStatus("current")
_EspcHumidVHighClass_Type = DisplayString
_EspcHumidVHighClass_Object = MibTableColumn
espcHumidVHighClass = _EspcHumidVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 8),
    _EspcHumidVHighClass_Type()
)
espcHumidVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighClass.setStatus("current")
_EspcHumidHighHumid_Type = Integer32
_EspcHumidHighHumid_Object = MibTableColumn
espcHumidHighHumid = _EspcHumidHighHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 9),
    _EspcHumidHighHumid_Type()
)
espcHumidHighHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighHumid.setStatus("current")
_EspcHumidHighActions_Type = DisplayString
_EspcHumidHighActions_Object = MibTableColumn
espcHumidHighActions = _EspcHumidHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 10),
    _EspcHumidHighActions_Type()
)
espcHumidHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighActions.setStatus("current")
_EspcHumidHighTrapnum_Type = Integer32
_EspcHumidHighTrapnum_Object = MibTableColumn
espcHumidHighTrapnum = _EspcHumidHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 11),
    _EspcHumidHighTrapnum_Type()
)
espcHumidHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighTrapnum.setStatus("current")
_EspcHumidHighClass_Type = DisplayString
_EspcHumidHighClass_Object = MibTableColumn
espcHumidHighClass = _EspcHumidHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 12),
    _EspcHumidHighClass_Type()
)
espcHumidHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighClass.setStatus("current")
_EspcHumidNormalActions_Type = DisplayString
_EspcHumidNormalActions_Object = MibTableColumn
espcHumidNormalActions = _EspcHumidNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 13),
    _EspcHumidNormalActions_Type()
)
espcHumidNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidNormalActions.setStatus("current")
_EspcHumidNormalTrapnum_Type = Integer32
_EspcHumidNormalTrapnum_Object = MibTableColumn
espcHumidNormalTrapnum = _EspcHumidNormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 14),
    _EspcHumidNormalTrapnum_Type()
)
espcHumidNormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidNormalTrapnum.setStatus("current")
_EspcHumidNormalClass_Type = DisplayString
_EspcHumidNormalClass_Object = MibTableColumn
espcHumidNormalClass = _EspcHumidNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 15),
    _EspcHumidNormalClass_Type()
)
espcHumidNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidNormalClass.setStatus("current")
_EspcHumidLowHumid_Type = Integer32
_EspcHumidLowHumid_Object = MibTableColumn
espcHumidLowHumid = _EspcHumidLowHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 16),
    _EspcHumidLowHumid_Type()
)
espcHumidLowHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowHumid.setStatus("current")
_EspcHumidLowActions_Type = DisplayString
_EspcHumidLowActions_Object = MibTableColumn
espcHumidLowActions = _EspcHumidLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 17),
    _EspcHumidLowActions_Type()
)
espcHumidLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowActions.setStatus("current")
_EspcHumidLowTrapnum_Type = Integer32
_EspcHumidLowTrapnum_Object = MibTableColumn
espcHumidLowTrapnum = _EspcHumidLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 18),
    _EspcHumidLowTrapnum_Type()
)
espcHumidLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowTrapnum.setStatus("current")
_EspcHumidLowClass_Type = DisplayString
_EspcHumidLowClass_Object = MibTableColumn
espcHumidLowClass = _EspcHumidLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 19),
    _EspcHumidLowClass_Type()
)
espcHumidLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowClass.setStatus("current")
_EspcHumidVLowHumid_Type = Integer32
_EspcHumidVLowHumid_Object = MibTableColumn
espcHumidVLowHumid = _EspcHumidVLowHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 20),
    _EspcHumidVLowHumid_Type()
)
espcHumidVLowHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowHumid.setStatus("current")
_EspcHumidVLowActions_Type = DisplayString
_EspcHumidVLowActions_Object = MibTableColumn
espcHumidVLowActions = _EspcHumidVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 21),
    _EspcHumidVLowActions_Type()
)
espcHumidVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowActions.setStatus("current")
_EspcHumidVLowTrapnum_Type = Integer32
_EspcHumidVLowTrapnum_Object = MibTableColumn
espcHumidVLowTrapnum = _EspcHumidVLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 22),
    _EspcHumidVLowTrapnum_Type()
)
espcHumidVLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowTrapnum.setStatus("current")
_EspcHumidVLowClass_Type = DisplayString
_EspcHumidVLowClass_Object = MibTableColumn
espcHumidVLowClass = _EspcHumidVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 3, 1, 23),
    _EspcHumidVLowClass_Type()
)
espcHumidVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowClass.setStatus("current")
_EsPointConfigAITable_Object = MibTable
esPointConfigAITable = _EsPointConfigAITable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5)
)
if mibBuilder.loadTexts:
    esPointConfigAITable.setStatus("current")
_EsPointConfigAIEntry_Object = MibTableRow
esPointConfigAIEntry = _EsPointConfigAIEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1)
)
esPointConfigAIEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "espcHumidIndexES"),
    (0, "SITEBOSS-570-STD-MIB", "espcHumidIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigAIEntry.setStatus("current")


class _EspcAIIndexES_Type(Integer32):
    """Custom type espcAIIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcAIIndexES_Type.__name__ = "Integer32"
_EspcAIIndexES_Object = MibTableColumn
espcAIIndexES = _EspcAIIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 1),
    _EspcAIIndexES_Type()
)
espcAIIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcAIIndexES.setStatus("current")


class _EspcAIIndexPoint_Type(Integer32):
    """Custom type espcAIIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcAIIndexPoint_Type.__name__ = "Integer32"
_EspcAIIndexPoint_Object = MibTableColumn
espcAIIndexPoint = _EspcAIIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 2),
    _EspcAIIndexPoint_Type()
)
espcAIIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcAIIndexPoint.setStatus("current")
_EspcAIEnable_Type = DisplayString
_EspcAIEnable_Object = MibTableColumn
espcAIEnable = _EspcAIEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 3),
    _EspcAIEnable_Type()
)
espcAIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIEnable.setStatus("current")
_EspcAIDeadband_Type = DisplayString
_EspcAIDeadband_Object = MibTableColumn
espcAIDeadband = _EspcAIDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 5),
    _EspcAIDeadband_Type()
)
espcAIDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIDeadband.setStatus("current")
_EspcAIVhighValue_Type = DisplayString
_EspcAIVhighValue_Object = MibTableColumn
espcAIVhighValue = _EspcAIVhighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 6),
    _EspcAIVhighValue_Type()
)
espcAIVhighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighValue.setStatus("current")
_EspcAIVhighActions_Type = DisplayString
_EspcAIVhighActions_Object = MibTableColumn
espcAIVhighActions = _EspcAIVhighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 7),
    _EspcAIVhighActions_Type()
)
espcAIVhighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighActions.setStatus("current")
_EspcAIVhighTrapnum_Type = Integer32
_EspcAIVhighTrapnum_Object = MibTableColumn
espcAIVhighTrapnum = _EspcAIVhighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 8),
    _EspcAIVhighTrapnum_Type()
)
espcAIVhighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighTrapnum.setStatus("current")
_EspcAIVhighClass_Type = DisplayString
_EspcAIVhighClass_Object = MibTableColumn
espcAIVhighClass = _EspcAIVhighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 9),
    _EspcAIVhighClass_Type()
)
espcAIVhighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighClass.setStatus("current")
_EspcAIHighValue_Type = DisplayString
_EspcAIHighValue_Object = MibTableColumn
espcAIHighValue = _EspcAIHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 10),
    _EspcAIHighValue_Type()
)
espcAIHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighValue.setStatus("current")
_EspcAIHighActions_Type = DisplayString
_EspcAIHighActions_Object = MibTableColumn
espcAIHighActions = _EspcAIHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 11),
    _EspcAIHighActions_Type()
)
espcAIHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighActions.setStatus("current")
_EspcAIHighTrapnum_Type = Integer32
_EspcAIHighTrapnum_Object = MibTableColumn
espcAIHighTrapnum = _EspcAIHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 12),
    _EspcAIHighTrapnum_Type()
)
espcAIHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighTrapnum.setStatus("current")
_EspcAIHighClass_Type = DisplayString
_EspcAIHighClass_Object = MibTableColumn
espcAIHighClass = _EspcAIHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 13),
    _EspcAIHighClass_Type()
)
espcAIHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighClass.setStatus("current")
_EspcAINormalActions_Type = DisplayString
_EspcAINormalActions_Object = MibTableColumn
espcAINormalActions = _EspcAINormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 14),
    _EspcAINormalActions_Type()
)
espcAINormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAINormalActions.setStatus("current")
_EspcAINormalTrapnum_Type = Integer32
_EspcAINormalTrapnum_Object = MibTableColumn
espcAINormalTrapnum = _EspcAINormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 15),
    _EspcAINormalTrapnum_Type()
)
espcAINormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAINormalTrapnum.setStatus("current")
_EspcAINormalClass_Type = DisplayString
_EspcAINormalClass_Object = MibTableColumn
espcAINormalClass = _EspcAINormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 16),
    _EspcAINormalClass_Type()
)
espcAINormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAINormalClass.setStatus("current")
_EspcAILowValue_Type = DisplayString
_EspcAILowValue_Object = MibTableColumn
espcAILowValue = _EspcAILowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 17),
    _EspcAILowValue_Type()
)
espcAILowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowValue.setStatus("current")
_EspcAILowActions_Type = DisplayString
_EspcAILowActions_Object = MibTableColumn
espcAILowActions = _EspcAILowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 18),
    _EspcAILowActions_Type()
)
espcAILowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowActions.setStatus("current")
_EspcAILowTrapnum_Type = Integer32
_EspcAILowTrapnum_Object = MibTableColumn
espcAILowTrapnum = _EspcAILowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 19),
    _EspcAILowTrapnum_Type()
)
espcAILowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowTrapnum.setStatus("current")
_EspcAILowClass_Type = DisplayString
_EspcAILowClass_Object = MibTableColumn
espcAILowClass = _EspcAILowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 20),
    _EspcAILowClass_Type()
)
espcAILowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowClass.setStatus("current")
_EspcAIVlowValue_Type = DisplayString
_EspcAIVlowValue_Object = MibTableColumn
espcAIVlowValue = _EspcAIVlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 21),
    _EspcAIVlowValue_Type()
)
espcAIVlowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowValue.setStatus("current")
_EspcAIVlowActions_Type = DisplayString
_EspcAIVlowActions_Object = MibTableColumn
espcAIVlowActions = _EspcAIVlowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 22),
    _EspcAIVlowActions_Type()
)
espcAIVlowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowActions.setStatus("current")
_EspcAIVlowTrapnum_Type = Integer32
_EspcAIVlowTrapnum_Object = MibTableColumn
espcAIVlowTrapnum = _EspcAIVlowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 23),
    _EspcAIVlowTrapnum_Type()
)
espcAIVlowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowTrapnum.setStatus("current")
_EspcAIVlowClass_Type = DisplayString
_EspcAIVlowClass_Object = MibTableColumn
espcAIVlowClass = _EspcAIVlowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 24),
    _EspcAIVlowClass_Type()
)
espcAIVlowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowClass.setStatus("current")
_EspcAIConvUnitName_Type = DisplayString
_EspcAIConvUnitName_Object = MibTableColumn
espcAIConvUnitName = _EspcAIConvUnitName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 25),
    _EspcAIConvUnitName_Type()
)
espcAIConvUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvUnitName.setStatus("current")
_EspcAIConvHighValue_Type = DisplayString
_EspcAIConvHighValue_Object = MibTableColumn
espcAIConvHighValue = _EspcAIConvHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 26),
    _EspcAIConvHighValue_Type()
)
espcAIConvHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvHighValue.setStatus("current")
_EspcAIConvHighUnit_Type = DisplayString
_EspcAIConvHighUnit_Object = MibTableColumn
espcAIConvHighUnit = _EspcAIConvHighUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 27),
    _EspcAIConvHighUnit_Type()
)
espcAIConvHighUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvHighUnit.setStatus("current")
_EspcAIConvLowValue_Type = DisplayString
_EspcAIConvLowValue_Object = MibTableColumn
espcAIConvLowValue = _EspcAIConvLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 29),
    _EspcAIConvLowValue_Type()
)
espcAIConvLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvLowValue.setStatus("current")
_EspcAIConvLowUnit_Type = DisplayString
_EspcAIConvLowUnit_Object = MibTableColumn
espcAIConvLowUnit = _EspcAIConvLowUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 30),
    _EspcAIConvLowUnit_Type()
)
espcAIConvLowUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvLowUnit.setStatus("current")
_EspcAIDisplayFormat_Type = DisplayString
_EspcAIDisplayFormat_Object = MibTableColumn
espcAIDisplayFormat = _EspcAIDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 5, 1, 32),
    _EspcAIDisplayFormat_Type()
)
espcAIDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIDisplayFormat.setStatus("current")
_EsPointConfigOutputTable_Object = MibTable
esPointConfigOutputTable = _EsPointConfigOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6)
)
if mibBuilder.loadTexts:
    esPointConfigOutputTable.setStatus("current")
_EsPointConfigOutputEntry_Object = MibTableRow
esPointConfigOutputEntry = _EsPointConfigOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1)
)
esPointConfigOutputEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "espcOutputIndexES"),
    (0, "SITEBOSS-570-STD-MIB", "espcOutputIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigOutputEntry.setStatus("current")


class _EspcOutputIndexES_Type(Integer32):
    """Custom type espcOutputIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcOutputIndexES_Type.__name__ = "Integer32"
_EspcOutputIndexES_Object = MibTableColumn
espcOutputIndexES = _EspcOutputIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 1),
    _EspcOutputIndexES_Type()
)
espcOutputIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputIndexES.setStatus("current")


class _EspcOutputIndexPoint_Type(Integer32):
    """Custom type espcOutputIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcOutputIndexPoint_Type.__name__ = "Integer32"
_EspcOutputIndexPoint_Object = MibTableColumn
espcOutputIndexPoint = _EspcOutputIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 2),
    _EspcOutputIndexPoint_Type()
)
espcOutputIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputIndexPoint.setStatus("current")
_EspcOutputEnable_Type = DisplayString
_EspcOutputEnable_Object = MibTableColumn
espcOutputEnable = _EspcOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 3),
    _EspcOutputEnable_Type()
)
espcOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputEnable.setStatus("current")
_EspcOutputActiveState_Type = DisplayString
_EspcOutputActiveState_Object = MibTableColumn
espcOutputActiveState = _EspcOutputActiveState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 4),
    _EspcOutputActiveState_Type()
)
espcOutputActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveState.setStatus("current")
_EspcOutputType_Type = DisplayString
_EspcOutputType_Object = MibTableColumn
espcOutputType = _EspcOutputType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 5),
    _EspcOutputType_Type()
)
espcOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputType.setStatus("current")
_EspcOutputAliasValue_Type = DisplayString
_EspcOutputAliasValue_Object = MibTableColumn
espcOutputAliasValue = _EspcOutputAliasValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 6),
    _EspcOutputAliasValue_Type()
)
espcOutputAliasValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputAliasValue.setStatus("current")
_EspcOutputAliasColor_Type = DisplayString
_EspcOutputAliasColor_Object = MibTableColumn
espcOutputAliasColor = _EspcOutputAliasColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 7),
    _EspcOutputAliasColor_Type()
)
espcOutputAliasColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputAliasColor.setStatus("current")
_EspcOutputActiveAlias_Type = DisplayString
_EspcOutputActiveAlias_Object = MibTableColumn
espcOutputActiveAlias = _EspcOutputActiveAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 10),
    _EspcOutputActiveAlias_Type()
)
espcOutputActiveAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveAlias.setStatus("current")
_EspcOutputActiveColor_Type = DisplayString
_EspcOutputActiveColor_Object = MibTableColumn
espcOutputActiveColor = _EspcOutputActiveColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 11),
    _EspcOutputActiveColor_Type()
)
espcOutputActiveColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveColor.setStatus("current")
_EspcOutputActiveActions_Type = DisplayString
_EspcOutputActiveActions_Object = MibTableColumn
espcOutputActiveActions = _EspcOutputActiveActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 12),
    _EspcOutputActiveActions_Type()
)
espcOutputActiveActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveActions.setStatus("current")


class _EspcOutputActiveTrapnum_Type(Integer32):
    """Custom type espcOutputActiveTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1199),
    )


_EspcOutputActiveTrapnum_Type.__name__ = "Integer32"
_EspcOutputActiveTrapnum_Object = MibTableColumn
espcOutputActiveTrapnum = _EspcOutputActiveTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 13),
    _EspcOutputActiveTrapnum_Type()
)
espcOutputActiveTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveTrapnum.setStatus("current")
_EspcOutputActiveClass_Type = DisplayString
_EspcOutputActiveClass_Object = MibTableColumn
espcOutputActiveClass = _EspcOutputActiveClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 14),
    _EspcOutputActiveClass_Type()
)
espcOutputActiveClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveClass.setStatus("current")
_EspcOutputInactiveAlias_Type = DisplayString
_EspcOutputInactiveAlias_Object = MibTableColumn
espcOutputInactiveAlias = _EspcOutputInactiveAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 20),
    _EspcOutputInactiveAlias_Type()
)
espcOutputInactiveAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveAlias.setStatus("current")
_EspcOutputInactiveColor_Type = DisplayString
_EspcOutputInactiveColor_Object = MibTableColumn
espcOutputInactiveColor = _EspcOutputInactiveColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 21),
    _EspcOutputInactiveColor_Type()
)
espcOutputInactiveColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveColor.setStatus("current")
_EspcOutputInactiveActions_Type = DisplayString
_EspcOutputInactiveActions_Object = MibTableColumn
espcOutputInactiveActions = _EspcOutputInactiveActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 22),
    _EspcOutputInactiveActions_Type()
)
espcOutputInactiveActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveActions.setStatus("current")


class _EspcOutputInactiveTrapnum_Type(Integer32):
    """Custom type espcOutputInactiveTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1199),
    )


_EspcOutputInactiveTrapnum_Type.__name__ = "Integer32"
_EspcOutputInactiveTrapnum_Object = MibTableColumn
espcOutputInactiveTrapnum = _EspcOutputInactiveTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 23),
    _EspcOutputInactiveTrapnum_Type()
)
espcOutputInactiveTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveTrapnum.setStatus("current")
_EspcOutputInactiveClass_Type = DisplayString
_EspcOutputInactiveClass_Object = MibTableColumn
espcOutputInactiveClass = _EspcOutputInactiveClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 2, 6, 1, 24),
    _EspcOutputInactiveClass_Type()
)
espcOutputInactiveClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveClass.setStatus("current")
_SerialPorts_ObjectIdentity = ObjectIdentity
serialPorts = _SerialPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3)
)
_NumberPorts_Type = Integer32
_NumberPorts_Object = MibScalar
numberPorts = _NumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 1),
    _NumberPorts_Type()
)
numberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberPorts.setStatus("current")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1)
)
portConfigEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "portConfigIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")


class _PortConfigIndex_Type(Integer32):
    """Custom type portConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortConfigIndex_Type.__name__ = "Integer32"
_PortConfigIndex_Object = MibTableColumn
portConfigIndex = _PortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 1),
    _PortConfigIndex_Type()
)
portConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigIndex.setStatus("current")
_PortConfigBaud_Type = Integer32
_PortConfigBaud_Object = MibTableColumn
portConfigBaud = _PortConfigBaud_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 2),
    _PortConfigBaud_Type()
)
portConfigBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBaud.setStatus("current")
_PortConfigDataFormat_Type = Integer32
_PortConfigDataFormat_Object = MibTableColumn
portConfigDataFormat = _PortConfigDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 3),
    _PortConfigDataFormat_Type()
)
portConfigDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDataFormat.setStatus("current")
_PortConfigStripPtOutputLfs_Type = Integer32
_PortConfigStripPtOutputLfs_Object = MibTableColumn
portConfigStripPtOutputLfs = _PortConfigStripPtOutputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 4),
    _PortConfigStripPtOutputLfs_Type()
)
portConfigStripPtOutputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStripPtOutputLfs.setStatus("current")
_PortConfigStripPtInputLfs_Type = Integer32
_PortConfigStripPtInputLfs_Object = MibTableColumn
portConfigStripPtInputLfs = _PortConfigStripPtInputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 5),
    _PortConfigStripPtInputLfs_Type()
)
portConfigStripPtInputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStripPtInputLfs.setStatus("current")
_PortConfigMaskEnable_Type = Integer32
_PortConfigMaskEnable_Object = MibTableColumn
portConfigMaskEnable = _PortConfigMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 7),
    _PortConfigMaskEnable_Type()
)
portConfigMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMaskEnable.setStatus("current")
_PortConfigDAEnable_Type = Integer32
_PortConfigDAEnable_Object = MibTableColumn
portConfigDAEnable = _PortConfigDAEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 8),
    _PortConfigDAEnable_Type()
)
portConfigDAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDAEnable.setStatus("current")
_PortConfigStoreAlarmsDPT_Type = DisplayString
_PortConfigStoreAlarmsDPT_Object = MibTableColumn
portConfigStoreAlarmsDPT = _PortConfigStoreAlarmsDPT_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 9),
    _PortConfigStoreAlarmsDPT_Type()
)
portConfigStoreAlarmsDPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStoreAlarmsDPT.setStatus("current")
_PortConfigRecordTimeout_Type = Integer32
_PortConfigRecordTimeout_Object = MibTableColumn
portConfigRecordTimeout = _PortConfigRecordTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 10),
    _PortConfigRecordTimeout_Type()
)
portConfigRecordTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigRecordTimeout.setStatus("current")
_PortConfigDataType_Type = DisplayString
_PortConfigDataType_Object = MibTableColumn
portConfigDataType = _PortConfigDataType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 11),
    _PortConfigDataType_Type()
)
portConfigDataType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDataType.setStatus("current")
_PortConfigEtxToCRLF_Type = DisplayString
_PortConfigEtxToCRLF_Object = MibTableColumn
portConfigEtxToCRLF = _PortConfigEtxToCRLF_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 12),
    _PortConfigEtxToCRLF_Type()
)
portConfigEtxToCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigEtxToCRLF.setStatus("current")
_PortConfigMLREnable_Type = DisplayString
_PortConfigMLREnable_Object = MibTableColumn
portConfigMLREnable = _PortConfigMLREnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 13),
    _PortConfigMLREnable_Type()
)
portConfigMLREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLREnable.setStatus("current")
_PortConfigMLRStartField1Pos_Type = Integer32
_PortConfigMLRStartField1Pos_Object = MibTableColumn
portConfigMLRStartField1Pos = _PortConfigMLRStartField1Pos_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 14),
    _PortConfigMLRStartField1Pos_Type()
)
portConfigMLRStartField1Pos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRStartField1Pos.setStatus("current")
_PortConfigMLRStartField1Text_Type = DisplayString
_PortConfigMLRStartField1Text_Object = MibTableColumn
portConfigMLRStartField1Text = _PortConfigMLRStartField1Text_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 15),
    _PortConfigMLRStartField1Text_Type()
)
portConfigMLRStartField1Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRStartField1Text.setStatus("current")
_PortConfigMLRStartField2Pos_Type = Integer32
_PortConfigMLRStartField2Pos_Object = MibTableColumn
portConfigMLRStartField2Pos = _PortConfigMLRStartField2Pos_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 16),
    _PortConfigMLRStartField2Pos_Type()
)
portConfigMLRStartField2Pos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRStartField2Pos.setStatus("current")
_PortConfigMLRStartField2Text_Type = DisplayString
_PortConfigMLRStartField2Text_Object = MibTableColumn
portConfigMLRStartField2Text = _PortConfigMLRStartField2Text_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 17),
    _PortConfigMLRStartField2Text_Type()
)
portConfigMLRStartField2Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRStartField2Text.setStatus("current")
_PortConfigMLRNumLinesBefore_Type = Integer32
_PortConfigMLRNumLinesBefore_Object = MibTableColumn
portConfigMLRNumLinesBefore = _PortConfigMLRNumLinesBefore_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 18),
    _PortConfigMLRNumLinesBefore_Type()
)
portConfigMLRNumLinesBefore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRNumLinesBefore.setStatus("current")
_PortConfigMLREndDetection_Type = DisplayString
_PortConfigMLREndDetection_Object = MibTableColumn
portConfigMLREndDetection = _PortConfigMLREndDetection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 19),
    _PortConfigMLREndDetection_Type()
)
portConfigMLREndDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLREndDetection.setStatus("current")
_PortConfigMLRLineCount_Type = Integer32
_PortConfigMLRLineCount_Object = MibTableColumn
portConfigMLRLineCount = _PortConfigMLRLineCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 20),
    _PortConfigMLRLineCount_Type()
)
portConfigMLRLineCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRLineCount.setStatus("current")
_PortConfigMLREndField1Pos_Type = Integer32
_PortConfigMLREndField1Pos_Object = MibTableColumn
portConfigMLREndField1Pos = _PortConfigMLREndField1Pos_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 21),
    _PortConfigMLREndField1Pos_Type()
)
portConfigMLREndField1Pos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLREndField1Pos.setStatus("current")
_PortConfigMLREndField1Text_Type = DisplayString
_PortConfigMLREndField1Text_Object = MibTableColumn
portConfigMLREndField1Text = _PortConfigMLREndField1Text_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 22),
    _PortConfigMLREndField1Text_Type()
)
portConfigMLREndField1Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLREndField1Text.setStatus("current")
_PortConfigMLREndField2Pos_Type = Integer32
_PortConfigMLREndField2Pos_Object = MibTableColumn
portConfigMLREndField2Pos = _PortConfigMLREndField2Pos_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 23),
    _PortConfigMLREndField2Pos_Type()
)
portConfigMLREndField2Pos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLREndField2Pos.setStatus("current")
_PortConfigMLREndField2Text_Type = DisplayString
_PortConfigMLREndField2Text_Object = MibTableColumn
portConfigMLREndField2Text = _PortConfigMLREndField2Text_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 24),
    _PortConfigMLREndField2Text_Type()
)
portConfigMLREndField2Text.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLREndField2Text.setStatus("current")
_PortConfigMLRUseComplexRules_Type = DisplayString
_PortConfigMLRUseComplexRules_Object = MibTableColumn
portConfigMLRUseComplexRules = _PortConfigMLRUseComplexRules_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 25),
    _PortConfigMLRUseComplexRules_Type()
)
portConfigMLRUseComplexRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMLRUseComplexRules.setStatus("current")
_PortConfigBufferPT_Type = DisplayString
_PortConfigBufferPT_Object = MibTableColumn
portConfigBufferPT = _PortConfigBufferPT_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 26),
    _PortConfigBufferPT_Type()
)
portConfigBufferPT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBufferPT.setStatus("current")
_PortConfigId_Type = DisplayString
_PortConfigId_Object = MibTableColumn
portConfigId = _PortConfigId_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 27),
    _PortConfigId_Type()
)
portConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigId.setStatus("current")
_PortConfigMode_Type = DisplayString
_PortConfigMode_Object = MibTableColumn
portConfigMode = _PortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 28),
    _PortConfigMode_Type()
)
portConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMode.setStatus("current")
_PortConfigHsk_Type = DisplayString
_PortConfigHsk_Object = MibTableColumn
portConfigHsk = _PortConfigHsk_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 3, 2, 1, 29),
    _PortConfigHsk_Type()
)
portConfigHsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigHsk.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1)
)
_Ethernet1_ObjectIdentity = ObjectIdentity
ethernet1 = _Ethernet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1)
)
_Eth1Mode_Type = DisplayString
_Eth1Mode_Object = MibScalar
eth1Mode = _Eth1Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 1),
    _Eth1Mode_Type()
)
eth1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1Mode.setStatus("current")
_Eth1Address_Type = IpAddress
_Eth1Address_Object = MibScalar
eth1Address = _Eth1Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 2),
    _Eth1Address_Type()
)
eth1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1Address.setStatus("current")
_Eth1SubnetMask_Type = IpAddress
_Eth1SubnetMask_Object = MibScalar
eth1SubnetMask = _Eth1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 3),
    _Eth1SubnetMask_Type()
)
eth1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1SubnetMask.setStatus("current")
_Eth1Router_Type = IpAddress
_Eth1Router_Object = MibScalar
eth1Router = _Eth1Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 4),
    _Eth1Router_Type()
)
eth1Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1Router.setStatus("current")
_Eth1VLAN_ObjectIdentity = ObjectIdentity
eth1VLAN = _Eth1VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5)
)
_Eth1VLAN1_ObjectIdentity = ObjectIdentity
eth1VLAN1 = _Eth1VLAN1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 1)
)
_Eth1VLAN1ID_Type = Integer32
_Eth1VLAN1ID_Object = MibScalar
eth1VLAN1ID = _Eth1VLAN1ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 1, 1),
    _Eth1VLAN1ID_Type()
)
eth1VLAN1ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1ID.setStatus("current")
_Eth1VLAN1Priority_Type = Integer32
_Eth1VLAN1Priority_Object = MibScalar
eth1VLAN1Priority = _Eth1VLAN1Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 1, 2),
    _Eth1VLAN1Priority_Type()
)
eth1VLAN1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1Priority.setStatus("current")
_Eth1VLAN1Address_Type = IpAddress
_Eth1VLAN1Address_Object = MibScalar
eth1VLAN1Address = _Eth1VLAN1Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 1, 3),
    _Eth1VLAN1Address_Type()
)
eth1VLAN1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1Address.setStatus("current")
_Eth1VLAN1SubnetMask_Type = IpAddress
_Eth1VLAN1SubnetMask_Object = MibScalar
eth1VLAN1SubnetMask = _Eth1VLAN1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 1, 4),
    _Eth1VLAN1SubnetMask_Type()
)
eth1VLAN1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1SubnetMask.setStatus("current")
_Eth1VLAN1Router_Type = IpAddress
_Eth1VLAN1Router_Object = MibScalar
eth1VLAN1Router = _Eth1VLAN1Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 1, 5),
    _Eth1VLAN1Router_Type()
)
eth1VLAN1Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1Router.setStatus("current")
_Eth1VLAN2_ObjectIdentity = ObjectIdentity
eth1VLAN2 = _Eth1VLAN2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 2)
)
_Eth1VLAN2ID_Type = Integer32
_Eth1VLAN2ID_Object = MibScalar
eth1VLAN2ID = _Eth1VLAN2ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 2, 1),
    _Eth1VLAN2ID_Type()
)
eth1VLAN2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2ID.setStatus("current")
_Eth1VLAN2Priority_Type = Integer32
_Eth1VLAN2Priority_Object = MibScalar
eth1VLAN2Priority = _Eth1VLAN2Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 2, 2),
    _Eth1VLAN2Priority_Type()
)
eth1VLAN2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2Priority.setStatus("current")
_Eth1VLAN2Address_Type = IpAddress
_Eth1VLAN2Address_Object = MibScalar
eth1VLAN2Address = _Eth1VLAN2Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 2, 3),
    _Eth1VLAN2Address_Type()
)
eth1VLAN2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2Address.setStatus("current")
_Eth1VLAN2SubnetMask_Type = IpAddress
_Eth1VLAN2SubnetMask_Object = MibScalar
eth1VLAN2SubnetMask = _Eth1VLAN2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 2, 4),
    _Eth1VLAN2SubnetMask_Type()
)
eth1VLAN2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2SubnetMask.setStatus("current")
_Eth1VLAN2Router_Type = IpAddress
_Eth1VLAN2Router_Object = MibScalar
eth1VLAN2Router = _Eth1VLAN2Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 2, 5),
    _Eth1VLAN2Router_Type()
)
eth1VLAN2Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2Router.setStatus("current")
_Eth1VLAN3_ObjectIdentity = ObjectIdentity
eth1VLAN3 = _Eth1VLAN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 3)
)
_Eth1VLAN3ID_Type = Integer32
_Eth1VLAN3ID_Object = MibScalar
eth1VLAN3ID = _Eth1VLAN3ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 3, 1),
    _Eth1VLAN3ID_Type()
)
eth1VLAN3ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3ID.setStatus("current")
_Eth1VLAN3Priority_Type = Integer32
_Eth1VLAN3Priority_Object = MibScalar
eth1VLAN3Priority = _Eth1VLAN3Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 3, 2),
    _Eth1VLAN3Priority_Type()
)
eth1VLAN3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3Priority.setStatus("current")
_Eth1VLAN3Address_Type = IpAddress
_Eth1VLAN3Address_Object = MibScalar
eth1VLAN3Address = _Eth1VLAN3Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 3, 3),
    _Eth1VLAN3Address_Type()
)
eth1VLAN3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3Address.setStatus("current")
_Eth1VLAN3SubnetMask_Type = IpAddress
_Eth1VLAN3SubnetMask_Object = MibScalar
eth1VLAN3SubnetMask = _Eth1VLAN3SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 3, 4),
    _Eth1VLAN3SubnetMask_Type()
)
eth1VLAN3SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3SubnetMask.setStatus("current")
_Eth1VLAN3Router_Type = IpAddress
_Eth1VLAN3Router_Object = MibScalar
eth1VLAN3Router = _Eth1VLAN3Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 3, 5),
    _Eth1VLAN3Router_Type()
)
eth1VLAN3Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3Router.setStatus("current")
_Eth1VLAN4_ObjectIdentity = ObjectIdentity
eth1VLAN4 = _Eth1VLAN4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 4)
)
_Eth1VLAN4ID_Type = Integer32
_Eth1VLAN4ID_Object = MibScalar
eth1VLAN4ID = _Eth1VLAN4ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 4, 1),
    _Eth1VLAN4ID_Type()
)
eth1VLAN4ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4ID.setStatus("current")
_Eth1VLAN4Priority_Type = Integer32
_Eth1VLAN4Priority_Object = MibScalar
eth1VLAN4Priority = _Eth1VLAN4Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 4, 2),
    _Eth1VLAN4Priority_Type()
)
eth1VLAN4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4Priority.setStatus("current")
_Eth1VLAN4Address_Type = IpAddress
_Eth1VLAN4Address_Object = MibScalar
eth1VLAN4Address = _Eth1VLAN4Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 4, 3),
    _Eth1VLAN4Address_Type()
)
eth1VLAN4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4Address.setStatus("current")
_Eth1VLAN4SubnetMask_Type = IpAddress
_Eth1VLAN4SubnetMask_Object = MibScalar
eth1VLAN4SubnetMask = _Eth1VLAN4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 4, 4),
    _Eth1VLAN4SubnetMask_Type()
)
eth1VLAN4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4SubnetMask.setStatus("current")
_Eth1VLAN4Router_Type = IpAddress
_Eth1VLAN4Router_Object = MibScalar
eth1VLAN4Router = _Eth1VLAN4Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 4, 5),
    _Eth1VLAN4Router_Type()
)
eth1VLAN4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4Router.setStatus("current")
_Eth1VLAN5_ObjectIdentity = ObjectIdentity
eth1VLAN5 = _Eth1VLAN5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 5)
)
_Eth1VLAN5ID_Type = Integer32
_Eth1VLAN5ID_Object = MibScalar
eth1VLAN5ID = _Eth1VLAN5ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 5, 1),
    _Eth1VLAN5ID_Type()
)
eth1VLAN5ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5ID.setStatus("current")
_Eth1VLAN5Priority_Type = Integer32
_Eth1VLAN5Priority_Object = MibScalar
eth1VLAN5Priority = _Eth1VLAN5Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 5, 2),
    _Eth1VLAN5Priority_Type()
)
eth1VLAN5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5Priority.setStatus("current")
_Eth1VLAN5Address_Type = IpAddress
_Eth1VLAN5Address_Object = MibScalar
eth1VLAN5Address = _Eth1VLAN5Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 5, 3),
    _Eth1VLAN5Address_Type()
)
eth1VLAN5Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5Address.setStatus("current")
_Eth1VLAN5SubnetMask_Type = IpAddress
_Eth1VLAN5SubnetMask_Object = MibScalar
eth1VLAN5SubnetMask = _Eth1VLAN5SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 5, 4),
    _Eth1VLAN5SubnetMask_Type()
)
eth1VLAN5SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5SubnetMask.setStatus("current")
_Eth1VLAN5Router_Type = IpAddress
_Eth1VLAN5Router_Object = MibScalar
eth1VLAN5Router = _Eth1VLAN5Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 5, 5),
    _Eth1VLAN5Router_Type()
)
eth1VLAN5Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5Router.setStatus("current")
_Eth1VLAN6_ObjectIdentity = ObjectIdentity
eth1VLAN6 = _Eth1VLAN6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 6)
)
_Eth1VLAN6ID_Type = Integer32
_Eth1VLAN6ID_Object = MibScalar
eth1VLAN6ID = _Eth1VLAN6ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 6, 1),
    _Eth1VLAN6ID_Type()
)
eth1VLAN6ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6ID.setStatus("current")
_Eth1VLAN6Priority_Type = Integer32
_Eth1VLAN6Priority_Object = MibScalar
eth1VLAN6Priority = _Eth1VLAN6Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 6, 2),
    _Eth1VLAN6Priority_Type()
)
eth1VLAN6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6Priority.setStatus("current")
_Eth1VLAN6Address_Type = IpAddress
_Eth1VLAN6Address_Object = MibScalar
eth1VLAN6Address = _Eth1VLAN6Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 6, 3),
    _Eth1VLAN6Address_Type()
)
eth1VLAN6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6Address.setStatus("current")
_Eth1VLAN6SubnetMask_Type = IpAddress
_Eth1VLAN6SubnetMask_Object = MibScalar
eth1VLAN6SubnetMask = _Eth1VLAN6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 6, 4),
    _Eth1VLAN6SubnetMask_Type()
)
eth1VLAN6SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6SubnetMask.setStatus("current")
_Eth1VLAN6Router_Type = IpAddress
_Eth1VLAN6Router_Object = MibScalar
eth1VLAN6Router = _Eth1VLAN6Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 5, 6, 5),
    _Eth1VLAN6Router_Type()
)
eth1VLAN6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6Router.setStatus("current")
_Eth1MAC_Type = DisplayString
_Eth1MAC_Object = MibScalar
eth1MAC = _Eth1MAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 6),
    _Eth1MAC_Type()
)
eth1MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1MAC.setStatus("current")
_Eth1IPv6_ObjectIdentity = ObjectIdentity
eth1IPv6 = _Eth1IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7)
)
_Eth1IPv6Mode_Type = DisplayString
_Eth1IPv6Mode_Object = MibScalar
eth1IPv6Mode = _Eth1IPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 1),
    _Eth1IPv6Mode_Type()
)
eth1IPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1IPv6Mode.setStatus("current")
_Eth1IPv6Static_ObjectIdentity = ObjectIdentity
eth1IPv6Static = _Eth1IPv6Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 2)
)
_Eth1IPv6StaticAddress_Type = DisplayString
_Eth1IPv6StaticAddress_Object = MibScalar
eth1IPv6StaticAddress = _Eth1IPv6StaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 2, 1),
    _Eth1IPv6StaticAddress_Type()
)
eth1IPv6StaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1IPv6StaticAddress.setStatus("current")
_Eth1IPv6StaticRouter_Type = DisplayString
_Eth1IPv6StaticRouter_Object = MibScalar
eth1IPv6StaticRouter = _Eth1IPv6StaticRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 2, 2),
    _Eth1IPv6StaticRouter_Type()
)
eth1IPv6StaticRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1IPv6StaticRouter.setStatus("current")
_Eth1IPv6Auto_ObjectIdentity = ObjectIdentity
eth1IPv6Auto = _Eth1IPv6Auto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 3)
)
_Eth1IPv6AutoAddress1_Type = DisplayString
_Eth1IPv6AutoAddress1_Object = MibScalar
eth1IPv6AutoAddress1 = _Eth1IPv6AutoAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 3, 1),
    _Eth1IPv6AutoAddress1_Type()
)
eth1IPv6AutoAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress1.setStatus("current")
_Eth1IPv6AutoAddress2_Type = DisplayString
_Eth1IPv6AutoAddress2_Object = MibScalar
eth1IPv6AutoAddress2 = _Eth1IPv6AutoAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 3, 2),
    _Eth1IPv6AutoAddress2_Type()
)
eth1IPv6AutoAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress2.setStatus("current")
_Eth1IPv6AutoAddress3_Type = DisplayString
_Eth1IPv6AutoAddress3_Object = MibScalar
eth1IPv6AutoAddress3 = _Eth1IPv6AutoAddress3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 3, 3),
    _Eth1IPv6AutoAddress3_Type()
)
eth1IPv6AutoAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress3.setStatus("current")
_Eth1IPv6AutoAddress4_Type = DisplayString
_Eth1IPv6AutoAddress4_Object = MibScalar
eth1IPv6AutoAddress4 = _Eth1IPv6AutoAddress4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 3, 4),
    _Eth1IPv6AutoAddress4_Type()
)
eth1IPv6AutoAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress4.setStatus("current")
_Eth1LinkLocalAddress_Type = DisplayString
_Eth1LinkLocalAddress_Object = MibScalar
eth1LinkLocalAddress = _Eth1LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 1, 7, 4),
    _Eth1LinkLocalAddress_Type()
)
eth1LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1LinkLocalAddress.setStatus("current")
_Ethernet2_ObjectIdentity = ObjectIdentity
ethernet2 = _Ethernet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2)
)
_Eth2Mode_Type = DisplayString
_Eth2Mode_Object = MibScalar
eth2Mode = _Eth2Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 1),
    _Eth2Mode_Type()
)
eth2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2Mode.setStatus("current")
_Eth2Address_Type = IpAddress
_Eth2Address_Object = MibScalar
eth2Address = _Eth2Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 2),
    _Eth2Address_Type()
)
eth2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2Address.setStatus("current")
_Eth2SubnetMask_Type = IpAddress
_Eth2SubnetMask_Object = MibScalar
eth2SubnetMask = _Eth2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 3),
    _Eth2SubnetMask_Type()
)
eth2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2SubnetMask.setStatus("current")
_Eth2Router_Type = IpAddress
_Eth2Router_Object = MibScalar
eth2Router = _Eth2Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 4),
    _Eth2Router_Type()
)
eth2Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2Router.setStatus("current")
_Eth2VLAN_ObjectIdentity = ObjectIdentity
eth2VLAN = _Eth2VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5)
)
_Eth2VLAN1_ObjectIdentity = ObjectIdentity
eth2VLAN1 = _Eth2VLAN1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 1)
)
_Eth2VLAN1ID_Type = Integer32
_Eth2VLAN1ID_Object = MibScalar
eth2VLAN1ID = _Eth2VLAN1ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 1, 1),
    _Eth2VLAN1ID_Type()
)
eth2VLAN1ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1ID.setStatus("current")
_Eth2VLAN1Priority_Type = Integer32
_Eth2VLAN1Priority_Object = MibScalar
eth2VLAN1Priority = _Eth2VLAN1Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 1, 2),
    _Eth2VLAN1Priority_Type()
)
eth2VLAN1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1Priority.setStatus("current")
_Eth2VLAN1Address_Type = IpAddress
_Eth2VLAN1Address_Object = MibScalar
eth2VLAN1Address = _Eth2VLAN1Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 1, 3),
    _Eth2VLAN1Address_Type()
)
eth2VLAN1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1Address.setStatus("current")
_Eth2VLAN1SubnetMask_Type = IpAddress
_Eth2VLAN1SubnetMask_Object = MibScalar
eth2VLAN1SubnetMask = _Eth2VLAN1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 1, 4),
    _Eth2VLAN1SubnetMask_Type()
)
eth2VLAN1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1SubnetMask.setStatus("current")
_Eth2VLAN1Router_Type = IpAddress
_Eth2VLAN1Router_Object = MibScalar
eth2VLAN1Router = _Eth2VLAN1Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 1, 5),
    _Eth2VLAN1Router_Type()
)
eth2VLAN1Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1Router.setStatus("current")
_Eth2VLAN2_ObjectIdentity = ObjectIdentity
eth2VLAN2 = _Eth2VLAN2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 2)
)
_Eth2VLAN2ID_Type = Integer32
_Eth2VLAN2ID_Object = MibScalar
eth2VLAN2ID = _Eth2VLAN2ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 2, 1),
    _Eth2VLAN2ID_Type()
)
eth2VLAN2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2ID.setStatus("current")
_Eth2VLAN2Priority_Type = Integer32
_Eth2VLAN2Priority_Object = MibScalar
eth2VLAN2Priority = _Eth2VLAN2Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 2, 2),
    _Eth2VLAN2Priority_Type()
)
eth2VLAN2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2Priority.setStatus("current")
_Eth2VLAN2Address_Type = IpAddress
_Eth2VLAN2Address_Object = MibScalar
eth2VLAN2Address = _Eth2VLAN2Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 2, 3),
    _Eth2VLAN2Address_Type()
)
eth2VLAN2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2Address.setStatus("current")
_Eth2VLAN2SubnetMask_Type = IpAddress
_Eth2VLAN2SubnetMask_Object = MibScalar
eth2VLAN2SubnetMask = _Eth2VLAN2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 2, 4),
    _Eth2VLAN2SubnetMask_Type()
)
eth2VLAN2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2SubnetMask.setStatus("current")
_Eth2VLAN2Router_Type = IpAddress
_Eth2VLAN2Router_Object = MibScalar
eth2VLAN2Router = _Eth2VLAN2Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 2, 5),
    _Eth2VLAN2Router_Type()
)
eth2VLAN2Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2Router.setStatus("current")
_Eth2VLAN3_ObjectIdentity = ObjectIdentity
eth2VLAN3 = _Eth2VLAN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 3)
)
_Eth2VLAN3ID_Type = Integer32
_Eth2VLAN3ID_Object = MibScalar
eth2VLAN3ID = _Eth2VLAN3ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 3, 1),
    _Eth2VLAN3ID_Type()
)
eth2VLAN3ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3ID.setStatus("current")
_Eth2VLAN3Priority_Type = Integer32
_Eth2VLAN3Priority_Object = MibScalar
eth2VLAN3Priority = _Eth2VLAN3Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 3, 2),
    _Eth2VLAN3Priority_Type()
)
eth2VLAN3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3Priority.setStatus("current")
_Eth2VLAN3Address_Type = IpAddress
_Eth2VLAN3Address_Object = MibScalar
eth2VLAN3Address = _Eth2VLAN3Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 3, 3),
    _Eth2VLAN3Address_Type()
)
eth2VLAN3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3Address.setStatus("current")
_Eth2VLAN3SubnetMask_Type = IpAddress
_Eth2VLAN3SubnetMask_Object = MibScalar
eth2VLAN3SubnetMask = _Eth2VLAN3SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 3, 4),
    _Eth2VLAN3SubnetMask_Type()
)
eth2VLAN3SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3SubnetMask.setStatus("current")
_Eth2VLAN3Router_Type = IpAddress
_Eth2VLAN3Router_Object = MibScalar
eth2VLAN3Router = _Eth2VLAN3Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 3, 5),
    _Eth2VLAN3Router_Type()
)
eth2VLAN3Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3Router.setStatus("current")
_Eth2VLAN4_ObjectIdentity = ObjectIdentity
eth2VLAN4 = _Eth2VLAN4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 4)
)
_Eth2VLAN4ID_Type = Integer32
_Eth2VLAN4ID_Object = MibScalar
eth2VLAN4ID = _Eth2VLAN4ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 4, 1),
    _Eth2VLAN4ID_Type()
)
eth2VLAN4ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4ID.setStatus("current")
_Eth2VLAN4Priority_Type = Integer32
_Eth2VLAN4Priority_Object = MibScalar
eth2VLAN4Priority = _Eth2VLAN4Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 4, 2),
    _Eth2VLAN4Priority_Type()
)
eth2VLAN4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4Priority.setStatus("current")
_Eth2VLAN4Address_Type = IpAddress
_Eth2VLAN4Address_Object = MibScalar
eth2VLAN4Address = _Eth2VLAN4Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 4, 3),
    _Eth2VLAN4Address_Type()
)
eth2VLAN4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4Address.setStatus("current")
_Eth2VLAN4SubnetMask_Type = IpAddress
_Eth2VLAN4SubnetMask_Object = MibScalar
eth2VLAN4SubnetMask = _Eth2VLAN4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 4, 4),
    _Eth2VLAN4SubnetMask_Type()
)
eth2VLAN4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4SubnetMask.setStatus("current")
_Eth2VLAN4Router_Type = IpAddress
_Eth2VLAN4Router_Object = MibScalar
eth2VLAN4Router = _Eth2VLAN4Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 4, 5),
    _Eth2VLAN4Router_Type()
)
eth2VLAN4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4Router.setStatus("current")
_Eth2VLAN5_ObjectIdentity = ObjectIdentity
eth2VLAN5 = _Eth2VLAN5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 5)
)
_Eth2VLAN5ID_Type = Integer32
_Eth2VLAN5ID_Object = MibScalar
eth2VLAN5ID = _Eth2VLAN5ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 5, 1),
    _Eth2VLAN5ID_Type()
)
eth2VLAN5ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5ID.setStatus("current")
_Eth2VLAN5Priority_Type = Integer32
_Eth2VLAN5Priority_Object = MibScalar
eth2VLAN5Priority = _Eth2VLAN5Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 5, 2),
    _Eth2VLAN5Priority_Type()
)
eth2VLAN5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5Priority.setStatus("current")
_Eth2VLAN5Address_Type = IpAddress
_Eth2VLAN5Address_Object = MibScalar
eth2VLAN5Address = _Eth2VLAN5Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 5, 3),
    _Eth2VLAN5Address_Type()
)
eth2VLAN5Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5Address.setStatus("current")
_Eth2VLAN5SubnetMask_Type = IpAddress
_Eth2VLAN5SubnetMask_Object = MibScalar
eth2VLAN5SubnetMask = _Eth2VLAN5SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 5, 4),
    _Eth2VLAN5SubnetMask_Type()
)
eth2VLAN5SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5SubnetMask.setStatus("current")
_Eth2VLAN5Router_Type = IpAddress
_Eth2VLAN5Router_Object = MibScalar
eth2VLAN5Router = _Eth2VLAN5Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 5, 5),
    _Eth2VLAN5Router_Type()
)
eth2VLAN5Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5Router.setStatus("current")
_Eth2VLAN6_ObjectIdentity = ObjectIdentity
eth2VLAN6 = _Eth2VLAN6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 6)
)
_Eth2VLAN6ID_Type = Integer32
_Eth2VLAN6ID_Object = MibScalar
eth2VLAN6ID = _Eth2VLAN6ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 6, 1),
    _Eth2VLAN6ID_Type()
)
eth2VLAN6ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6ID.setStatus("current")
_Eth2VLAN6Priority_Type = Integer32
_Eth2VLAN6Priority_Object = MibScalar
eth2VLAN6Priority = _Eth2VLAN6Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 6, 2),
    _Eth2VLAN6Priority_Type()
)
eth2VLAN6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6Priority.setStatus("current")
_Eth2VLAN6Address_Type = IpAddress
_Eth2VLAN6Address_Object = MibScalar
eth2VLAN6Address = _Eth2VLAN6Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 6, 3),
    _Eth2VLAN6Address_Type()
)
eth2VLAN6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6Address.setStatus("current")
_Eth2VLAN6SubnetMask_Type = IpAddress
_Eth2VLAN6SubnetMask_Object = MibScalar
eth2VLAN6SubnetMask = _Eth2VLAN6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 6, 4),
    _Eth2VLAN6SubnetMask_Type()
)
eth2VLAN6SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6SubnetMask.setStatus("current")
_Eth2VLAN6Router_Type = IpAddress
_Eth2VLAN6Router_Object = MibScalar
eth2VLAN6Router = _Eth2VLAN6Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 5, 6, 5),
    _Eth2VLAN6Router_Type()
)
eth2VLAN6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6Router.setStatus("current")
_Eth2MAC_Type = DisplayString
_Eth2MAC_Object = MibScalar
eth2MAC = _Eth2MAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 6),
    _Eth2MAC_Type()
)
eth2MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2MAC.setStatus("current")
_Eth2IPv6_ObjectIdentity = ObjectIdentity
eth2IPv6 = _Eth2IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7)
)
_Eth2IPv6Mode_Type = DisplayString
_Eth2IPv6Mode_Object = MibScalar
eth2IPv6Mode = _Eth2IPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 1),
    _Eth2IPv6Mode_Type()
)
eth2IPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2IPv6Mode.setStatus("current")
_Eth2IPv6Static_ObjectIdentity = ObjectIdentity
eth2IPv6Static = _Eth2IPv6Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 2)
)
_Eth2IPv6StaticAddress_Type = DisplayString
_Eth2IPv6StaticAddress_Object = MibScalar
eth2IPv6StaticAddress = _Eth2IPv6StaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 2, 1),
    _Eth2IPv6StaticAddress_Type()
)
eth2IPv6StaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2IPv6StaticAddress.setStatus("current")
_Eth2IPv6StaticRouter_Type = DisplayString
_Eth2IPv6StaticRouter_Object = MibScalar
eth2IPv6StaticRouter = _Eth2IPv6StaticRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 2, 2),
    _Eth2IPv6StaticRouter_Type()
)
eth2IPv6StaticRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2IPv6StaticRouter.setStatus("current")
_Eth2IPv6Auto_ObjectIdentity = ObjectIdentity
eth2IPv6Auto = _Eth2IPv6Auto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 3)
)
_Eth2IPv6AutoAddress1_Type = DisplayString
_Eth2IPv6AutoAddress1_Object = MibScalar
eth2IPv6AutoAddress1 = _Eth2IPv6AutoAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 3, 1),
    _Eth2IPv6AutoAddress1_Type()
)
eth2IPv6AutoAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress1.setStatus("current")
_Eth2IPv6AutoAddress2_Type = DisplayString
_Eth2IPv6AutoAddress2_Object = MibScalar
eth2IPv6AutoAddress2 = _Eth2IPv6AutoAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 3, 2),
    _Eth2IPv6AutoAddress2_Type()
)
eth2IPv6AutoAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress2.setStatus("current")
_Eth2IPv6AutoAddress3_Type = DisplayString
_Eth2IPv6AutoAddress3_Object = MibScalar
eth2IPv6AutoAddress3 = _Eth2IPv6AutoAddress3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 3, 3),
    _Eth2IPv6AutoAddress3_Type()
)
eth2IPv6AutoAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress3.setStatus("current")
_Eth2IPv6AutoAddress4_Type = DisplayString
_Eth2IPv6AutoAddress4_Object = MibScalar
eth2IPv6AutoAddress4 = _Eth2IPv6AutoAddress4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 3, 4),
    _Eth2IPv6AutoAddress4_Type()
)
eth2IPv6AutoAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress4.setStatus("current")
_Eth2LinkLocalAddress_Type = DisplayString
_Eth2LinkLocalAddress_Object = MibScalar
eth2LinkLocalAddress = _Eth2LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 1, 1, 2, 7, 4),
    _Eth2LinkLocalAddress_Type()
)
eth2LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2LinkLocalAddress.setStatus("current")
_DefaultRouter_Type = DisplayString
_DefaultRouter_Object = MibScalar
defaultRouter = _DefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 2),
    _DefaultRouter_Type()
)
defaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRouter.setStatus("current")
_DnsTable_Object = MibTable
dnsTable = _DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 3)
)
if mibBuilder.loadTexts:
    dnsTable.setStatus("current")
_DnsEntry_Object = MibTableRow
dnsEntry = _DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 3, 1)
)
dnsEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "dnsIndex"),
)
if mibBuilder.loadTexts:
    dnsEntry.setStatus("current")


class _DnsIndex_Type(Integer32):
    """Custom type dnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DnsIndex_Type.__name__ = "Integer32"
_DnsIndex_Object = MibTableColumn
dnsIndex = _DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 3, 1, 1),
    _DnsIndex_Type()
)
dnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsIndex.setStatus("current")
_DnsAddress_Type = IpAddress
_DnsAddress_Object = MibTableColumn
dnsAddress = _DnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 3, 1, 2),
    _DnsAddress_Type()
)
dnsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsAddress.setStatus("current")
_Hostname_Type = DisplayString
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 4),
    _Hostname_Type()
)
hostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostname.setStatus("current")
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 5)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 5, 1)
)
hostEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("current")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 5, 1, 1),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIndex.setStatus("current")
_HostDeclaration_Type = DisplayString
_HostDeclaration_Object = MibTableColumn
hostDeclaration = _HostDeclaration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 5, 1, 2),
    _HostDeclaration_Type()
)
hostDeclaration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostDeclaration.setStatus("current")
_NcpDuplex_Type = Integer32
_NcpDuplex_Object = MibScalar
ncpDuplex = _NcpDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 6),
    _NcpDuplex_Type()
)
ncpDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpDuplex.setStatus("current")
_NcpTimeout_Type = Integer32
_NcpTimeout_Object = MibScalar
ncpTimeout = _NcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 7),
    _NcpTimeout_Type()
)
ncpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpTimeout.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8)
)
_SnmpAgentEnable_Type = DisplayString
_SnmpAgentEnable_Object = MibScalar
snmpAgentEnable = _SnmpAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 1),
    _SnmpAgentEnable_Type()
)
snmpAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentEnable.setStatus("current")
_SnmpNotificationCaptureEnable_Type = DisplayString
_SnmpNotificationCaptureEnable_Object = MibScalar
snmpNotificationCaptureEnable = _SnmpNotificationCaptureEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 5),
    _SnmpNotificationCaptureEnable_Type()
)
snmpNotificationCaptureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNotificationCaptureEnable.setStatus("current")
_SnmpNotificationCaptureFile_Type = DisplayString
_SnmpNotificationCaptureFile_Object = MibScalar
snmpNotificationCaptureFile = _SnmpNotificationCaptureFile_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 6),
    _SnmpNotificationCaptureFile_Type()
)
snmpNotificationCaptureFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNotificationCaptureFile.setStatus("current")
_SnmpNotificationTx_ObjectIdentity = ObjectIdentity
snmpNotificationTx = _SnmpNotificationTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 7)
)
_SnmpNtfnAttempts_Type = Integer32
_SnmpNtfnAttempts_Object = MibScalar
snmpNtfnAttempts = _SnmpNtfnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 7, 1),
    _SnmpNtfnAttempts_Type()
)
snmpNtfnAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnAttempts.setStatus("current")
_SnmpNtfnTimeout_Type = Integer32
_SnmpNtfnTimeout_Object = MibScalar
snmpNtfnTimeout = _SnmpNtfnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 7, 2),
    _SnmpNtfnTimeout_Type()
)
snmpNtfnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnTimeout.setStatus("current")
_SnmpNtfnCycles_Type = Integer32
_SnmpNtfnCycles_Object = MibScalar
snmpNtfnCycles = _SnmpNtfnCycles_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 7, 3),
    _SnmpNtfnCycles_Type()
)
snmpNtfnCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnCycles.setStatus("current")
_SnmpNtfnSnooze_Type = Integer32
_SnmpNtfnSnooze_Object = MibScalar
snmpNtfnSnooze = _SnmpNtfnSnooze_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 8, 7, 4),
    _SnmpNtfnSnooze_Type()
)
snmpNtfnSnooze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnSnooze.setStatus("current")
_FtpPush_ObjectIdentity = ObjectIdentity
ftpPush = _FtpPush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9)
)
_FtpPushEnable_Type = DisplayString
_FtpPushEnable_Object = MibScalar
ftpPushEnable = _FtpPushEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 1),
    _FtpPushEnable_Type()
)
ftpPushEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushEnable.setStatus("current")
_FtpPushServer_Type = DisplayString
_FtpPushServer_Object = MibScalar
ftpPushServer = _FtpPushServer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 2),
    _FtpPushServer_Type()
)
ftpPushServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushServer.setStatus("current")
_FtpPushAccount_Type = DisplayString
_FtpPushAccount_Object = MibScalar
ftpPushAccount = _FtpPushAccount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 5),
    _FtpPushAccount_Type()
)
ftpPushAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushAccount.setStatus("current")
_FtpPushDirectory_Type = DisplayString
_FtpPushDirectory_Object = MibScalar
ftpPushDirectory = _FtpPushDirectory_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 6),
    _FtpPushDirectory_Type()
)
ftpPushDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushDirectory.setStatus("current")
_FtpPushperiod_Type = Integer32
_FtpPushperiod_Object = MibScalar
ftpPushperiod = _FtpPushperiod_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 7),
    _FtpPushperiod_Type()
)
ftpPushperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushperiod.setStatus("current")
_FtpPushPushFileTable_Object = MibTable
ftpPushPushFileTable = _FtpPushPushFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 8)
)
if mibBuilder.loadTexts:
    ftpPushPushFileTable.setStatus("current")
_FtpPushPushFileEntry_Object = MibTableRow
ftpPushPushFileEntry = _FtpPushPushFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 8, 1)
)
ftpPushPushFileEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "ftpPushPushFileIndex"),
)
if mibBuilder.loadTexts:
    ftpPushPushFileEntry.setStatus("current")


class _FtpPushPushFileIndex_Type(Integer32):
    """Custom type ftpPushPushFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FtpPushPushFileIndex_Type.__name__ = "Integer32"
_FtpPushPushFileIndex_Object = MibTableColumn
ftpPushPushFileIndex = _FtpPushPushFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 8, 1, 1),
    _FtpPushPushFileIndex_Type()
)
ftpPushPushFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPushPushFileIndex.setStatus("current")
_FtpPushPushFile_Type = DisplayString
_FtpPushPushFile_Object = MibTableColumn
ftpPushPushFile = _FtpPushPushFile_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 8, 1, 2),
    _FtpPushPushFile_Type()
)
ftpPushPushFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPushFile.setStatus("current")
_FtpPushPushAudit_Type = DisplayString
_FtpPushPushAudit_Object = MibScalar
ftpPushPushAudit = _FtpPushPushAudit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 9),
    _FtpPushPushAudit_Type()
)
ftpPushPushAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPushAudit.setStatus("current")
_FtpPushPushAlarms_Type = DisplayString
_FtpPushPushAlarms_Object = MibScalar
ftpPushPushAlarms = _FtpPushPushAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 10),
    _FtpPushPushAlarms_Type()
)
ftpPushPushAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPushAlarms.setStatus("current")
_FtpPushRemoteFileTable_Object = MibTable
ftpPushRemoteFileTable = _FtpPushRemoteFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 11)
)
if mibBuilder.loadTexts:
    ftpPushRemoteFileTable.setStatus("current")
_FtpPushRemoteFileEntry_Object = MibTableRow
ftpPushRemoteFileEntry = _FtpPushRemoteFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 11, 1)
)
ftpPushRemoteFileEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "ftpPushRemoteFileIndex"),
)
if mibBuilder.loadTexts:
    ftpPushRemoteFileEntry.setStatus("current")


class _FtpPushRemoteFileIndex_Type(Integer32):
    """Custom type ftpPushRemoteFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FtpPushRemoteFileIndex_Type.__name__ = "Integer32"
_FtpPushRemoteFileIndex_Object = MibTableColumn
ftpPushRemoteFileIndex = _FtpPushRemoteFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 11, 1, 1),
    _FtpPushRemoteFileIndex_Type()
)
ftpPushRemoteFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPushRemoteFileIndex.setStatus("current")
_FtpPushRemoteFileName_Type = DisplayString
_FtpPushRemoteFileName_Object = MibTableColumn
ftpPushRemoteFileName = _FtpPushRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 11, 1, 2),
    _FtpPushRemoteFileName_Type()
)
ftpPushRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushRemoteFileName.setStatus("current")
_FtpPushRemoteAlarmName_Type = DisplayString
_FtpPushRemoteAlarmName_Object = MibScalar
ftpPushRemoteAlarmName = _FtpPushRemoteAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 12),
    _FtpPushRemoteAlarmName_Type()
)
ftpPushRemoteAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushRemoteAlarmName.setStatus("current")
_FtpPushPassive_Type = DisplayString
_FtpPushPassive_Object = MibScalar
ftpPushPassive = _FtpPushPassive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 13),
    _FtpPushPassive_Type()
)
ftpPushPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPassive.setStatus("current")
_FtpPushIncludeDate_Type = DisplayString
_FtpPushIncludeDate_Object = MibScalar
ftpPushIncludeDate = _FtpPushIncludeDate_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 14),
    _FtpPushIncludeDate_Type()
)
ftpPushIncludeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIncludeDate.setStatus("current")
_FtpPushIncludeTime_Type = DisplayString
_FtpPushIncludeTime_Object = MibScalar
ftpPushIncludeTime = _FtpPushIncludeTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 15),
    _FtpPushIncludeTime_Type()
)
ftpPushIncludeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIncludeTime.setStatus("current")
_FtpPushIncludeSeq_Type = DisplayString
_FtpPushIncludeSeq_Object = MibScalar
ftpPushIncludeSeq = _FtpPushIncludeSeq_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 9, 16),
    _FtpPushIncludeSeq_Type()
)
ftpPushIncludeSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIncludeSeq.setStatus("current")
_Ppp_ObjectIdentity = ObjectIdentity
ppp = _Ppp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10)
)
_PppDial_ObjectIdentity = ObjectIdentity
pppDial = _PppDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1)
)
_PppDialEnable_Type = DisplayString
_PppDialEnable_Object = MibScalar
pppDialEnable = _PppDialEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 1),
    _PppDialEnable_Type()
)
pppDialEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialEnable.setStatus("current")
_PppDialNumber_Type = DisplayString
_PppDialNumber_Object = MibScalar
pppDialNumber = _PppDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 2),
    _PppDialNumber_Type()
)
pppDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialNumber.setStatus("current")
_PppDialIdleTimeout_Type = Integer32
_PppDialIdleTimeout_Object = MibScalar
pppDialIdleTimeout = _PppDialIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 5),
    _PppDialIdleTimeout_Type()
)
pppDialIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialIdleTimeout.setStatus("current")
_PppDialRetries_Type = Integer32
_PppDialRetries_Object = MibScalar
pppDialRetries = _PppDialRetries_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 6),
    _PppDialRetries_Type()
)
pppDialRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialRetries.setStatus("current")
_PppDialCDTimeout_Type = Integer32
_PppDialCDTimeout_Object = MibScalar
pppDialCDTimeout = _PppDialCDTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 7),
    _PppDialCDTimeout_Type()
)
pppDialCDTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialCDTimeout.setStatus("current")
_PppDialLoginTimeout_Type = Integer32
_PppDialLoginTimeout_Object = MibScalar
pppDialLoginTimeout = _PppDialLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 8),
    _PppDialLoginTimeout_Type()
)
pppDialLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialLoginTimeout.setStatus("current")
_PppDialMdmInit_Type = DisplayString
_PppDialMdmInit_Object = MibScalar
pppDialMdmInit = _PppDialMdmInit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 9),
    _PppDialMdmInit_Type()
)
pppDialMdmInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialMdmInit.setStatus("current")
_PppDialSuggestIP_Type = IpAddress
_PppDialSuggestIP_Object = MibScalar
pppDialSuggestIP = _PppDialSuggestIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 10),
    _PppDialSuggestIP_Type()
)
pppDialSuggestIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialSuggestIP.setStatus("current")
_PppDialPlainLogin_Type = DisplayString
_PppDialPlainLogin_Object = MibScalar
pppDialPlainLogin = _PppDialPlainLogin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 1, 11),
    _PppDialPlainLogin_Type()
)
pppDialPlainLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppDialPlainLogin.setStatus("current")
_PppHost_ObjectIdentity = ObjectIdentity
pppHost = _PppHost_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 2)
)
_PppHostEnable_Type = DisplayString
_PppHostEnable_Object = MibScalar
pppHostEnable = _PppHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 2, 1),
    _PppHostEnable_Type()
)
pppHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppHostEnable.setStatus("current")
_PppHostIdleTimeout_Type = Integer32
_PppHostIdleTimeout_Object = MibScalar
pppHostIdleTimeout = _PppHostIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 2, 2),
    _PppHostIdleTimeout_Type()
)
pppHostIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppHostIdleTimeout.setStatus("current")
_PppHostLocalIP_Type = IpAddress
_PppHostLocalIP_Object = MibScalar
pppHostLocalIP = _PppHostLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 2, 3),
    _PppHostLocalIP_Type()
)
pppHostLocalIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppHostLocalIP.setStatus("current")
_PppHostRemoteIP_Type = IpAddress
_PppHostRemoteIP_Object = MibScalar
pppHostRemoteIP = _PppHostRemoteIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 10, 2, 4),
    _PppHostRemoteIP_Type()
)
pppHostRemoteIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppHostRemoteIP.setStatus("current")
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 11)
)
_PppRoutingEnable_Type = DisplayString
_PppRoutingEnable_Object = MibScalar
pppRoutingEnable = _PppRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 11, 1),
    _PppRoutingEnable_Type()
)
pppRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppRoutingEnable.setStatus("current")
_EthRoutingEnable_Type = DisplayString
_EthRoutingEnable_Object = MibScalar
ethRoutingEnable = _EthRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 11, 2),
    _EthRoutingEnable_Type()
)
ethRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRoutingEnable.setStatus("current")
_EthRoutingNATEnable_Type = DisplayString
_EthRoutingNATEnable_Object = MibScalar
ethRoutingNATEnable = _EthRoutingNATEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 11, 3),
    _EthRoutingNATEnable_Type()
)
ethRoutingNATEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRoutingNATEnable.setStatus("current")
_RoutingInterface_Type = DisplayString
_RoutingInterface_Object = MibScalar
routingInterface = _RoutingInterface_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 11, 4),
    _RoutingInterface_Type()
)
routingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routingInterface.setStatus("current")
_Eth2WanRoutingEnable_Type = DisplayString
_Eth2WanRoutingEnable_Object = MibScalar
eth2WanRoutingEnable = _Eth2WanRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 11, 5),
    _Eth2WanRoutingEnable_Type()
)
eth2WanRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2WanRoutingEnable.setStatus("current")
_NetSecurity_ObjectIdentity = ObjectIdentity
netSecurity = _NetSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12)
)
_IpRestriction_ObjectIdentity = ObjectIdentity
ipRestriction = _IpRestriction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12, 1)
)
_IpRestrictionTable_Object = MibTable
ipRestrictionTable = _IpRestrictionTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ipRestrictionTable.setStatus("current")
_IpRestrictionEntry_Object = MibTableRow
ipRestrictionEntry = _IpRestrictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12, 1, 1, 1)
)
ipRestrictionEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "ipRestrictionIndex"),
)
if mibBuilder.loadTexts:
    ipRestrictionEntry.setStatus("current")


class _IpRestrictionIndex_Type(Integer32):
    """Custom type ipRestrictionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IpRestrictionIndex_Type.__name__ = "Integer32"
_IpRestrictionIndex_Object = MibTableColumn
ipRestrictionIndex = _IpRestrictionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12, 1, 1, 1, 1),
    _IpRestrictionIndex_Type()
)
ipRestrictionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRestrictionIndex.setStatus("current")
_IpRestrictionEnable_Type = DisplayString
_IpRestrictionEnable_Object = MibTableColumn
ipRestrictionEnable = _IpRestrictionEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12, 1, 1, 1, 2),
    _IpRestrictionEnable_Type()
)
ipRestrictionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRestrictionEnable.setStatus("current")
_IpRestrictionMask_Type = DisplayString
_IpRestrictionMask_Object = MibTableColumn
ipRestrictionMask = _IpRestrictionMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 12, 1, 1, 1, 3),
    _IpRestrictionMask_Type()
)
ipRestrictionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRestrictionMask.setStatus("current")
_Rts_ObjectIdentity = ObjectIdentity
rts = _Rts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13)
)
_RtsFileTable_Object = MibTable
rtsFileTable = _RtsFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1)
)
if mibBuilder.loadTexts:
    rtsFileTable.setStatus("current")
_RtsFileEntry_Object = MibTableRow
rtsFileEntry = _RtsFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1)
)
rtsFileEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "rtsFileIndex"),
)
if mibBuilder.loadTexts:
    rtsFileEntry.setStatus("current")


class _RtsFileIndex_Type(Integer32):
    """Custom type rtsFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RtsFileIndex_Type.__name__ = "Integer32"
_RtsFileIndex_Object = MibTableColumn
rtsFileIndex = _RtsFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 1),
    _RtsFileIndex_Type()
)
rtsFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtsFileIndex.setStatus("current")
_RtsFileMode_Type = DisplayString
_RtsFileMode_Object = MibTableColumn
rtsFileMode = _RtsFileMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 2),
    _RtsFileMode_Type()
)
rtsFileMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFileMode.setStatus("current")
_RtsFileShowAnswer_Type = DisplayString
_RtsFileShowAnswer_Object = MibTableColumn
rtsFileShowAnswer = _RtsFileShowAnswer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 3),
    _RtsFileShowAnswer_Type()
)
rtsFileShowAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFileShowAnswer.setStatus("current")
_RtsFileReqXON_Type = DisplayString
_RtsFileReqXON_Object = MibTableColumn
rtsFileReqXON = _RtsFileReqXON_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 4),
    _RtsFileReqXON_Type()
)
rtsFileReqXON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFileReqXON.setStatus("current")
_RtsFileTimeout_Type = Integer32
_RtsFileTimeout_Object = MibTableColumn
rtsFileTimeout = _RtsFileTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 5),
    _RtsFileTimeout_Type()
)
rtsFileTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFileTimeout.setStatus("current")
_RtsFileEmptyClose_Type = DisplayString
_RtsFileEmptyClose_Object = MibTableColumn
rtsFileEmptyClose = _RtsFileEmptyClose_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 6),
    _RtsFileEmptyClose_Type()
)
rtsFileEmptyClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFileEmptyClose.setStatus("current")
_RtsFilePushHost_Type = DisplayString
_RtsFilePushHost_Object = MibTableColumn
rtsFilePushHost = _RtsFilePushHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 7),
    _RtsFilePushHost_Type()
)
rtsFilePushHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFilePushHost.setStatus("current")
_RtsFilePushPort_Type = Integer32
_RtsFilePushPort_Object = MibTableColumn
rtsFilePushPort = _RtsFilePushPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 8),
    _RtsFilePushPort_Type()
)
rtsFilePushPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFilePushPort.setStatus("current")
_RtsFilePushRetryTimer_Type = Integer32
_RtsFilePushRetryTimer_Object = MibTableColumn
rtsFilePushRetryTimer = _RtsFilePushRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 1, 1, 9),
    _RtsFilePushRetryTimer_Type()
)
rtsFilePushRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsFilePushRetryTimer.setStatus("current")
_RtsAlarms_ObjectIdentity = ObjectIdentity
rtsAlarms = _RtsAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2)
)
_RtsAlarmsMode_Type = DisplayString
_RtsAlarmsMode_Object = MibScalar
rtsAlarmsMode = _RtsAlarmsMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 1),
    _RtsAlarmsMode_Type()
)
rtsAlarmsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsMode.setStatus("current")
_RtsAlarmsShowAnswer_Type = DisplayString
_RtsAlarmsShowAnswer_Object = MibScalar
rtsAlarmsShowAnswer = _RtsAlarmsShowAnswer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 2),
    _RtsAlarmsShowAnswer_Type()
)
rtsAlarmsShowAnswer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsShowAnswer.setStatus("current")
_RtsAlarmsReqXON_Type = DisplayString
_RtsAlarmsReqXON_Object = MibScalar
rtsAlarmsReqXON = _RtsAlarmsReqXON_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 3),
    _RtsAlarmsReqXON_Type()
)
rtsAlarmsReqXON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsReqXON.setStatus("current")
_RtsAlarmsTimeout_Type = Integer32
_RtsAlarmsTimeout_Object = MibScalar
rtsAlarmsTimeout = _RtsAlarmsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 4),
    _RtsAlarmsTimeout_Type()
)
rtsAlarmsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsTimeout.setStatus("current")
_RtsAlarmsEmptyClose_Type = DisplayString
_RtsAlarmsEmptyClose_Object = MibScalar
rtsAlarmsEmptyClose = _RtsAlarmsEmptyClose_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 5),
    _RtsAlarmsEmptyClose_Type()
)
rtsAlarmsEmptyClose.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsEmptyClose.setStatus("current")
_RtsAlarmsPushHost_Type = DisplayString
_RtsAlarmsPushHost_Object = MibScalar
rtsAlarmsPushHost = _RtsAlarmsPushHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 6),
    _RtsAlarmsPushHost_Type()
)
rtsAlarmsPushHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsPushHost.setStatus("current")
_RtsAlarmsPushPort_Type = Integer32
_RtsAlarmsPushPort_Object = MibScalar
rtsAlarmsPushPort = _RtsAlarmsPushPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 7),
    _RtsAlarmsPushPort_Type()
)
rtsAlarmsPushPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsPushPort.setStatus("current")
_RtsAlarmsPushRetryTimer_Type = Integer32
_RtsAlarmsPushRetryTimer_Object = MibScalar
rtsAlarmsPushRetryTimer = _RtsAlarmsPushRetryTimer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 13, 2, 8),
    _RtsAlarmsPushRetryTimer_Type()
)
rtsAlarmsPushRetryTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtsAlarmsPushRetryTimer.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14)
)
_TrapInclude_ObjectIdentity = ObjectIdentity
trapInclude = _TrapInclude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1)
)
_TrapIncludeDateTime_Type = DisplayString
_TrapIncludeDateTime_Object = MibScalar
trapIncludeDateTime = _TrapIncludeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1, 1),
    _TrapIncludeDateTime_Type()
)
trapIncludeDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeDateTime.setStatus("current")
_TrapIncludeSiteName_Type = DisplayString
_TrapIncludeSiteName_Object = MibScalar
trapIncludeSiteName = _TrapIncludeSiteName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1, 2),
    _TrapIncludeSiteName_Type()
)
trapIncludeSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeSiteName.setStatus("current")
_TrapIncludeSensorID_Type = DisplayString
_TrapIncludeSensorID_Object = MibScalar
trapIncludeSensorID = _TrapIncludeSensorID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1, 3),
    _TrapIncludeSensorID_Type()
)
trapIncludeSensorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeSensorID.setStatus("current")
_TrapIncludeUDName_Type = DisplayString
_TrapIncludeUDName_Object = MibScalar
trapIncludeUDName = _TrapIncludeUDName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1, 4),
    _TrapIncludeUDName_Type()
)
trapIncludeUDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeUDName.setStatus("current")
_TrapIncludeUDState_Type = DisplayString
_TrapIncludeUDState_Object = MibScalar
trapIncludeUDState = _TrapIncludeUDState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1, 5),
    _TrapIncludeUDState_Type()
)
trapIncludeUDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeUDState.setStatus("current")
_TrapIncludeSourceAddress_Type = IpAddress
_TrapIncludeSourceAddress_Object = MibScalar
trapIncludeSourceAddress = _TrapIncludeSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 1, 6),
    _TrapIncludeSourceAddress_Type()
)
trapIncludeSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeSourceAddress.setStatus("current")
_TrapAuthFailEnable_Type = DisplayString
_TrapAuthFailEnable_Object = MibScalar
trapAuthFailEnable = _TrapAuthFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 14, 2),
    _TrapAuthFailEnable_Type()
)
trapAuthFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAuthFailEnable.setStatus("current")
_RouteTest_ObjectIdentity = ObjectIdentity
routeTest = _RouteTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15)
)
_RouteTestEnable_Type = DisplayString
_RouteTestEnable_Object = MibScalar
routeTestEnable = _RouteTestEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15, 1),
    _RouteTestEnable_Type()
)
routeTestEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTestEnable.setStatus("current")
_RouteTestPeriod_Type = Integer32
_RouteTestPeriod_Object = MibScalar
routeTestPeriod = _RouteTestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15, 2),
    _RouteTestPeriod_Type()
)
routeTestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTestPeriod.setStatus("current")
_RouteTestAddressTable_Object = MibTable
routeTestAddressTable = _RouteTestAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15, 3)
)
if mibBuilder.loadTexts:
    routeTestAddressTable.setStatus("current")
_RouteTestAddressEntry_Object = MibTableRow
routeTestAddressEntry = _RouteTestAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15, 3, 1)
)
routeTestAddressEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "routeTestAddressIndex"),
)
if mibBuilder.loadTexts:
    routeTestAddressEntry.setStatus("current")


class _RouteTestAddressIndex_Type(Integer32):
    """Custom type routeTestAddressIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_RouteTestAddressIndex_Type.__name__ = "Integer32"
_RouteTestAddressIndex_Object = MibTableColumn
routeTestAddressIndex = _RouteTestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15, 3, 1, 1),
    _RouteTestAddressIndex_Type()
)
routeTestAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeTestAddressIndex.setStatus("current")
_RouteTestAddress_Type = DisplayString
_RouteTestAddress_Object = MibTableColumn
routeTestAddress = _RouteTestAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 15, 3, 1, 2),
    _RouteTestAddress_Type()
)
routeTestAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeTestAddress.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16)
)
_WirelessMode_Type = DisplayString
_WirelessMode_Object = MibScalar
wirelessMode = _WirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 1),
    _WirelessMode_Type()
)
wirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMode.setStatus("current")
_WirelessAPN_Type = DisplayString
_WirelessAPN_Object = MibScalar
wirelessAPN = _WirelessAPN_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 2),
    _WirelessAPN_Type()
)
wirelessAPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPN.setStatus("current")
_WirelessIdleTimeout_Type = Integer32
_WirelessIdleTimeout_Object = MibScalar
wirelessIdleTimeout = _WirelessIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 3),
    _WirelessIdleTimeout_Type()
)
wirelessIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIdleTimeout.setStatus("current")
_WirelessPIN_Type = DisplayString
_WirelessPIN_Object = MibScalar
wirelessPIN = _WirelessPIN_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 5),
    _WirelessPIN_Type()
)
wirelessPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPIN.setStatus("current")
_WirelessDRE_Type = DisplayString
_WirelessDRE_Object = MibScalar
wirelessDRE = _WirelessDRE_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 9),
    _WirelessDRE_Type()
)
wirelessDRE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDRE.setStatus("current")
_WirelessPPPUsername_Type = DisplayString
_WirelessPPPUsername_Object = MibScalar
wirelessPPPUsername = _WirelessPPPUsername_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 10),
    _WirelessPPPUsername_Type()
)
wirelessPPPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPPPUsername.setStatus("current")
_WirelessFirewall_Type = DisplayString
_WirelessFirewall_Object = MibScalar
wirelessFirewall = _WirelessFirewall_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 11),
    _WirelessFirewall_Type()
)
wirelessFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFirewall.setStatus("current")
_WirelessKeepaliveThreshold_Type = Integer32
_WirelessKeepaliveThreshold_Object = MibScalar
wirelessKeepaliveThreshold = _WirelessKeepaliveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 12),
    _WirelessKeepaliveThreshold_Type()
)
wirelessKeepaliveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessKeepaliveThreshold.setStatus("current")
_WirelessPPPDebug_Type = DisplayString
_WirelessPPPDebug_Object = MibScalar
wirelessPPPDebug = _WirelessPPPDebug_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 13),
    _WirelessPPPDebug_Type()
)
wirelessPPPDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPPPDebug.setStatus("current")
_WirelessConnectivity_ObjectIdentity = ObjectIdentity
wirelessConnectivity = _WirelessConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 20)
)
_WirelessConnEnable_Type = DisplayString
_WirelessConnEnable_Object = MibScalar
wirelessConnEnable = _WirelessConnEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 20, 1),
    _WirelessConnEnable_Type()
)
wirelessConnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnEnable.setStatus("current")
_WirelessConnCheckInterval_Type = Integer32
_WirelessConnCheckInterval_Object = MibScalar
wirelessConnCheckInterval = _WirelessConnCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 20, 2),
    _WirelessConnCheckInterval_Type()
)
wirelessConnCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnCheckInterval.setStatus("current")
_WirelessConnFailThreshold_Type = Integer32
_WirelessConnFailThreshold_Object = MibScalar
wirelessConnFailThreshold = _WirelessConnFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 20, 3),
    _WirelessConnFailThreshold_Type()
)
wirelessConnFailThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnFailThreshold.setStatus("current")
_WirelessConnIP1_Type = IpAddress
_WirelessConnIP1_Object = MibScalar
wirelessConnIP1 = _WirelessConnIP1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 20, 10),
    _WirelessConnIP1_Type()
)
wirelessConnIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnIP1.setStatus("current")
_WirelessConnIP2_Type = IpAddress
_WirelessConnIP2_Object = MibScalar
wirelessConnIP2 = _WirelessConnIP2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 16, 20, 11),
    _WirelessConnIP2_Type()
)
wirelessConnIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnIP2.setStatus("current")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 17)
)
_EmailServer_Type = DisplayString
_EmailServer_Object = MibScalar
emailServer = _EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 17, 1),
    _EmailServer_Type()
)
emailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailServer.setStatus("current")
_EmailDomain_Type = DisplayString
_EmailDomain_Object = MibScalar
emailDomain = _EmailDomain_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 17, 2),
    _EmailDomain_Type()
)
emailDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailDomain.setStatus("current")
_EmailAuthEnable_Type = DisplayString
_EmailAuthEnable_Object = MibScalar
emailAuthEnable = _EmailAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 17, 3),
    _EmailAuthEnable_Type()
)
emailAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAuthEnable.setStatus("current")
_NetAdvanced_ObjectIdentity = ObjectIdentity
netAdvanced = _NetAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 18)
)
_ArpFilter_Type = Integer32
_ArpFilter_Object = MibScalar
arpFilter = _ArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 18, 1),
    _ArpFilter_Type()
)
arpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpFilter.setStatus("current")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 19)
)
_WebEnable_Type = DisplayString
_WebEnable_Object = MibScalar
webEnable = _WebEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 19, 1),
    _WebEnable_Type()
)
webEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnable.setStatus("current")
_WebPort_Type = Integer32
_WebPort_Object = MibScalar
webPort = _WebPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 19, 2),
    _WebPort_Type()
)
webPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webPort.setStatus("current")
_WebTimeout_Type = Integer32
_WebTimeout_Object = MibScalar
webTimeout = _WebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 19, 3),
    _WebTimeout_Type()
)
webTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webTimeout.setStatus("current")
_EthExpan_ObjectIdentity = ObjectIdentity
ethExpan = _EthExpan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20)
)
_EthExpanIp_Type = IpAddress
_EthExpanIp_Object = MibScalar
ethExpanIp = _EthExpanIp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 1),
    _EthExpanIp_Type()
)
ethExpanIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethExpanIp.setStatus("current")
_EthExpanMask_Type = IpAddress
_EthExpanMask_Object = MibScalar
ethExpanMask = _EthExpanMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 2),
    _EthExpanMask_Type()
)
ethExpanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethExpanMask.setStatus("current")
_EthExpanCardTable_Object = MibTable
ethExpanCardTable = _EthExpanCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 3)
)
if mibBuilder.loadTexts:
    ethExpanCardTable.setStatus("current")
_EthExpanCardEntry_Object = MibTableRow
ethExpanCardEntry = _EthExpanCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 3, 1)
)
ethExpanCardEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "ethExpanCardIndex"),
)
if mibBuilder.loadTexts:
    ethExpanCardEntry.setStatus("current")


class _EthExpanCardIndex_Type(Integer32):
    """Custom type ethExpanCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EthExpanCardIndex_Type.__name__ = "Integer32"
_EthExpanCardIndex_Object = MibTableColumn
ethExpanCardIndex = _EthExpanCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 3, 1, 1),
    _EthExpanCardIndex_Type()
)
ethExpanCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethExpanCardIndex.setStatus("current")
_EthExpanCardMAC_Type = DisplayString
_EthExpanCardMAC_Object = MibTableColumn
ethExpanCardMAC = _EthExpanCardMAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 3, 1, 2),
    _EthExpanCardMAC_Type()
)
ethExpanCardMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethExpanCardMAC.setStatus("current")
_EthExpanDHCP_ObjectIdentity = ObjectIdentity
ethExpanDHCP = _EthExpanDHCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 6)
)
_EthExpanDHCPStartIp_Type = IpAddress
_EthExpanDHCPStartIp_Object = MibScalar
ethExpanDHCPStartIp = _EthExpanDHCPStartIp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 6, 1),
    _EthExpanDHCPStartIp_Type()
)
ethExpanDHCPStartIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethExpanDHCPStartIp.setStatus("current")
_EthExpanDHCPLeaseTime_Type = Integer32
_EthExpanDHCPLeaseTime_Object = MibScalar
ethExpanDHCPLeaseTime = _EthExpanDHCPLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 20, 6, 2),
    _EthExpanDHCPLeaseTime_Type()
)
ethExpanDHCPLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethExpanDHCPLeaseTime.setStatus("current")
_Ipv6_ObjectIdentity = ObjectIdentity
ipv6 = _Ipv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 21)
)
_Ipv6DefaultRouter_Type = DisplayString
_Ipv6DefaultRouter_Object = MibScalar
ipv6DefaultRouter = _Ipv6DefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 21, 1),
    _Ipv6DefaultRouter_Type()
)
ipv6DefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultRouter.setStatus("current")
_Cpe_ObjectIdentity = ObjectIdentity
cpe = _Cpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22)
)
_CpeTable_Object = MibTable
cpeTable = _CpeTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1)
)
if mibBuilder.loadTexts:
    cpeTable.setStatus("current")
_CpeEntry_Object = MibTableRow
cpeEntry = _CpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1)
)
cpeEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "cpeIndex"),
)
if mibBuilder.loadTexts:
    cpeEntry.setStatus("current")


class _CpeIndex_Type(Integer32):
    """Custom type cpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CpeIndex_Type.__name__ = "Integer32"
_CpeIndex_Object = MibTableColumn
cpeIndex = _CpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 1),
    _CpeIndex_Type()
)
cpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeIndex.setStatus("current")
_CpeHost_Type = DisplayString
_CpeHost_Object = MibTableColumn
cpeHost = _CpeHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 2),
    _CpeHost_Type()
)
cpeHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeHost.setStatus("current")
_CpeName_Type = DisplayString
_CpeName_Object = MibTableColumn
cpeName = _CpeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 3),
    _CpeName_Type()
)
cpeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeName.setStatus("current")
_CpeDescription_Type = DisplayString
_CpeDescription_Object = MibTableColumn
cpeDescription = _CpeDescription_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 4),
    _CpeDescription_Type()
)
cpeDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeDescription.setStatus("current")
_CpeKeepalive_Type = Integer32
_CpeKeepalive_Object = MibTableColumn
cpeKeepalive = _CpeKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 5),
    _CpeKeepalive_Type()
)
cpeKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeKeepalive.setStatus("current")
_CpeThreshold_Type = Integer32
_CpeThreshold_Object = MibTableColumn
cpeThreshold = _CpeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 6),
    _CpeThreshold_Type()
)
cpeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeThreshold.setStatus("current")
_CpeEventReminderInterval_Type = Integer32
_CpeEventReminderInterval_Object = MibTableColumn
cpeEventReminderInterval = _CpeEventReminderInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 7),
    _CpeEventReminderInterval_Type()
)
cpeEventReminderInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeEventReminderInterval.setStatus("current")
_CpeKeepaliveTicks_Type = Integer32
_CpeKeepaliveTicks_Object = MibTableColumn
cpeKeepaliveTicks = _CpeKeepaliveTicks_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 20),
    _CpeKeepaliveTicks_Type()
)
cpeKeepaliveTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeKeepaliveTicks.setStatus("current")
_CpePingSize_Type = Integer32
_CpePingSize_Object = MibTableColumn
cpePingSize = _CpePingSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 21),
    _CpePingSize_Type()
)
cpePingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpePingSize.setStatus("current")
_CpeInfoReset_Type = Integer32
_CpeInfoReset_Object = MibTableColumn
cpeInfoReset = _CpeInfoReset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 30),
    _CpeInfoReset_Type()
)
cpeInfoReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoReset.setStatus("current")
_CpeInfoNumReq_Type = Integer32
_CpeInfoNumReq_Object = MibTableColumn
cpeInfoNumReq = _CpeInfoNumReq_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 31),
    _CpeInfoNumReq_Type()
)
cpeInfoNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumReq.setStatus("current")
_CpeInfoNumGoodResp_Type = Integer32
_CpeInfoNumGoodResp_Object = MibTableColumn
cpeInfoNumGoodResp = _CpeInfoNumGoodResp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 32),
    _CpeInfoNumGoodResp_Type()
)
cpeInfoNumGoodResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumGoodResp.setStatus("current")
_CpeInfoNumBadResp_Type = Integer32
_CpeInfoNumBadResp_Object = MibTableColumn
cpeInfoNumBadResp = _CpeInfoNumBadResp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 33),
    _CpeInfoNumBadResp_Type()
)
cpeInfoNumBadResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumBadResp.setStatus("current")
_CpeInfoNumLostResp_Type = Integer32
_CpeInfoNumLostResp_Object = MibTableColumn
cpeInfoNumLostResp = _CpeInfoNumLostResp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 34),
    _CpeInfoNumLostResp_Type()
)
cpeInfoNumLostResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumLostResp.setStatus("current")
_CpeInfoPercentLoss_Type = DisplayString
_CpeInfoPercentLoss_Object = MibTableColumn
cpeInfoPercentLoss = _CpeInfoPercentLoss_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 35),
    _CpeInfoPercentLoss_Type()
)
cpeInfoPercentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoPercentLoss.setStatus("current")
_CpeInfoPercentBad_Type = DisplayString
_CpeInfoPercentBad_Object = MibTableColumn
cpeInfoPercentBad = _CpeInfoPercentBad_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 4, 22, 1, 1, 36),
    _CpeInfoPercentBad_Type()
)
cpeInfoPercentBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoPercentBad.setStatus("current")
_Modem_ObjectIdentity = ObjectIdentity
modem = _Modem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5)
)
_ModemFormat_Type = DisplayString
_ModemFormat_Object = MibScalar
modemFormat = _ModemFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 1),
    _ModemFormat_Type()
)
modemFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemFormat.setStatus("current")
_ModemInitString_Type = DisplayString
_ModemInitString_Object = MibScalar
modemInitString = _ModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 2),
    _ModemInitString_Type()
)
modemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemInitString.setStatus("current")
_ModemCallAttempts_Type = Integer32
_ModemCallAttempts_Object = MibScalar
modemCallAttempts = _ModemCallAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 4),
    _ModemCallAttempts_Type()
)
modemCallAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCallAttempts.setStatus("current")
_ModemCallDelay_Type = Integer32
_ModemCallDelay_Object = MibScalar
modemCallDelay = _ModemCallDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 5),
    _ModemCallDelay_Type()
)
modemCallDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCallDelay.setStatus("current")
_ModemCmdTimout_Type = Integer32
_ModemCmdTimout_Object = MibScalar
modemCmdTimout = _ModemCmdTimout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 6),
    _ModemCmdTimout_Type()
)
modemCmdTimout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCmdTimout.setStatus("current")
_ModemGoto_Type = DisplayString
_ModemGoto_Object = MibScalar
modemGoto = _ModemGoto_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 7),
    _ModemGoto_Type()
)
modemGoto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemGoto.setStatus("current")
_ModemClid_ObjectIdentity = ObjectIdentity
modemClid = _ModemClid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 8)
)
_ModemCLIDEnable_Type = DisplayString
_ModemCLIDEnable_Object = MibScalar
modemCLIDEnable = _ModemCLIDEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 8, 1),
    _ModemCLIDEnable_Type()
)
modemCLIDEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCLIDEnable.setStatus("current")
_ModemCLIDNumberTable_Object = MibTable
modemCLIDNumberTable = _ModemCLIDNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 8, 2)
)
if mibBuilder.loadTexts:
    modemCLIDNumberTable.setStatus("current")
_ModemCLIDNumberEntry_Object = MibTableRow
modemCLIDNumberEntry = _ModemCLIDNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 8, 2, 1)
)
modemCLIDNumberEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "modemCLIDNumberIndex"),
)
if mibBuilder.loadTexts:
    modemCLIDNumberEntry.setStatus("current")


class _ModemCLIDNumberIndex_Type(Integer32):
    """Custom type modemCLIDNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ModemCLIDNumberIndex_Type.__name__ = "Integer32"
_ModemCLIDNumberIndex_Object = MibTableColumn
modemCLIDNumberIndex = _ModemCLIDNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 8, 2, 1, 1),
    _ModemCLIDNumberIndex_Type()
)
modemCLIDNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modemCLIDNumberIndex.setStatus("current")
_ModemCLIDNumber_Type = DisplayString
_ModemCLIDNumber_Object = MibTableColumn
modemCLIDNumber = _ModemCLIDNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 8, 2, 1, 2),
    _ModemCLIDNumber_Type()
)
modemCLIDNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemCLIDNumber.setStatus("current")
_ModemTAPInitString_Type = DisplayString
_ModemTAPInitString_Object = MibScalar
modemTAPInitString = _ModemTAPInitString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 9),
    _ModemTAPInitString_Type()
)
modemTAPInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTAPInitString.setStatus("current")
_ModemTAP8N1_Type = DisplayString
_ModemTAP8N1_Object = MibScalar
modemTAP8N1 = _ModemTAP8N1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 5, 10),
    _ModemTAP8N1_Type()
)
modemTAP8N1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modemTAP8N1.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 8)
)
_Clock_Type = DisplayString
_Clock_Object = MibScalar
clock = _Clock_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 8, 1),
    _Clock_Type()
)
clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clock.setStatus("current")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10)
)
_ConsoleDuplex_Type = DisplayString
_ConsoleDuplex_Object = MibScalar
consoleDuplex = _ConsoleDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10, 1),
    _ConsoleDuplex_Type()
)
consoleDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleDuplex.setStatus("current")
_ConsoleTimeout_Type = Integer32
_ConsoleTimeout_Object = MibScalar
consoleTimeout = _ConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10, 2),
    _ConsoleTimeout_Type()
)
consoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleTimeout.setStatus("current")
_ConsoleBaud_Type = Integer32
_ConsoleBaud_Object = MibScalar
consoleBaud = _ConsoleBaud_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10, 4),
    _ConsoleBaud_Type()
)
consoleBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleBaud.setStatus("current")
_ConsoleFormat_Type = DisplayString
_ConsoleFormat_Object = MibScalar
consoleFormat = _ConsoleFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10, 5),
    _ConsoleFormat_Type()
)
consoleFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleFormat.setStatus("current")
_ConsoleHsk_Type = DisplayString
_ConsoleHsk_Object = MibScalar
consoleHsk = _ConsoleHsk_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10, 6),
    _ConsoleHsk_Type()
)
consoleHsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleHsk.setStatus("current")
_ConsoleConfirm_Type = DisplayString
_ConsoleConfirm_Object = MibScalar
consoleConfirm = _ConsoleConfirm_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 10, 7),
    _ConsoleConfirm_Type()
)
consoleConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleConfirm.setStatus("current")
_UnitSecurity_ObjectIdentity = ObjectIdentity
unitSecurity = _UnitSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11)
)
_SecCore_ObjectIdentity = ObjectIdentity
secCore = _SecCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1)
)
_ScShowPasswordPrompt_Type = DisplayString
_ScShowPasswordPrompt_Object = MibScalar
scShowPasswordPrompt = _ScShowPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 1),
    _ScShowPasswordPrompt_Type()
)
scShowPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scShowPasswordPrompt.setStatus("current")
_ScConsoleLoginRequired_Type = DisplayString
_ScConsoleLoginRequired_Object = MibScalar
scConsoleLoginRequired = _ScConsoleLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 2),
    _ScConsoleLoginRequired_Type()
)
scConsoleLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scConsoleLoginRequired.setStatus("current")
_ScModemLoginRequired_Type = DisplayString
_ScModemLoginRequired_Object = MibScalar
scModemLoginRequired = _ScModemLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 3),
    _ScModemLoginRequired_Type()
)
scModemLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scModemLoginRequired.setStatus("current")
_ScTelnetLoginRequired_Type = DisplayString
_ScTelnetLoginRequired_Object = MibScalar
scTelnetLoginRequired = _ScTelnetLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 4),
    _ScTelnetLoginRequired_Type()
)
scTelnetLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scTelnetLoginRequired.setStatus("current")
_ScTelnetPTLoginRequired_Type = DisplayString
_ScTelnetPTLoginRequired_Object = MibScalar
scTelnetPTLoginRequired = _ScTelnetPTLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 5),
    _ScTelnetPTLoginRequired_Type()
)
scTelnetPTLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scTelnetPTLoginRequired.setStatus("current")
_ScRTSLoginRequired_Type = DisplayString
_ScRTSLoginRequired_Object = MibScalar
scRTSLoginRequired = _ScRTSLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 6),
    _ScRTSLoginRequired_Type()
)
scRTSLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scRTSLoginRequired.setStatus("current")
_ScAuthMode_Type = DisplayString
_ScAuthMode_Object = MibScalar
scAuthMode = _ScAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 7),
    _ScAuthMode_Type()
)
scAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scAuthMode.setStatus("current")
_ScRightsGroup_Type = DisplayString
_ScRightsGroup_Object = MibScalar
scRightsGroup = _ScRightsGroup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 8),
    _ScRightsGroup_Type()
)
scRightsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scRightsGroup.setStatus("current")
_ScSecret_Type = DisplayString
_ScSecret_Object = MibScalar
scSecret = _ScSecret_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 1, 9),
    _ScSecret_Type()
)
scSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSecret.setStatus("current")
_SecUserTable_Object = MibTable
secUserTable = _SecUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2)
)
if mibBuilder.loadTexts:
    secUserTable.setStatus("current")
_SecUserEntry_Object = MibTableRow
secUserEntry = _SecUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1)
)
secUserEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "secUserIndex"),
)
if mibBuilder.loadTexts:
    secUserEntry.setStatus("current")


class _SecUserIndex_Type(Integer32):
    """Custom type secUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SecUserIndex_Type.__name__ = "Integer32"
_SecUserIndex_Object = MibTableColumn
secUserIndex = _SecUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 1),
    _SecUserIndex_Type()
)
secUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserIndex.setStatus("current")
_SecUserEnable_Type = DisplayString
_SecUserEnable_Object = MibTableColumn
secUserEnable = _SecUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 2),
    _SecUserEnable_Type()
)
secUserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserEnable.setStatus("current")
_SecUserConnectVia_Type = DisplayString
_SecUserConnectVia_Object = MibTableColumn
secUserConnectVia = _SecUserConnectVia_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 5),
    _SecUserConnectVia_Type()
)
secUserConnectVia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserConnectVia.setStatus("current")
_SecUserLoginTo_Type = DisplayString
_SecUserLoginTo_Object = MibTableColumn
secUserLoginTo = _SecUserLoginTo_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 6),
    _SecUserLoginTo_Type()
)
secUserLoginTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserLoginTo.setStatus("current")
_SecUserAccessFile_Type = DisplayString
_SecUserAccessFile_Object = MibTableColumn
secUserAccessFile = _SecUserAccessFile_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 7),
    _SecUserAccessFile_Type()
)
secUserAccessFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserAccessFile.setStatus("current")
_SecUserPTEscapeTo_Type = DisplayString
_SecUserPTEscapeTo_Object = MibTableColumn
secUserPTEscapeTo = _SecUserPTEscapeTo_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 9),
    _SecUserPTEscapeTo_Type()
)
secUserPTEscapeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserPTEscapeTo.setStatus("current")
_SecUserPPPType_Type = DisplayString
_SecUserPPPType_Object = MibTableColumn
secUserPPPType = _SecUserPPPType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 10),
    _SecUserPPPType_Type()
)
secUserPPPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserPPPType.setStatus("current")
_SecUserRights_Type = DisplayString
_SecUserRights_Object = MibTableColumn
secUserRights = _SecUserRights_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 11),
    _SecUserRights_Type()
)
secUserRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserRights.setStatus("current")
_SecUserEventsReadAccess_Type = DisplayString
_SecUserEventsReadAccess_Object = MibTableColumn
secUserEventsReadAccess = _SecUserEventsReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 13),
    _SecUserEventsReadAccess_Type()
)
secUserEventsReadAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserEventsReadAccess.setStatus("current")
_SecUserAuditReadAccess_Type = DisplayString
_SecUserAuditReadAccess_Object = MibTableColumn
secUserAuditReadAccess = _SecUserAuditReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 14),
    _SecUserAuditReadAccess_Type()
)
secUserAuditReadAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserAuditReadAccess.setStatus("current")
_SecUserEventsWriteAccess_Type = DisplayString
_SecUserEventsWriteAccess_Object = MibTableColumn
secUserEventsWriteAccess = _SecUserEventsWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 16),
    _SecUserEventsWriteAccess_Type()
)
secUserEventsWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserEventsWriteAccess.setStatus("current")
_SecUserAuditWriteAccess_Type = DisplayString
_SecUserAuditWriteAccess_Object = MibTableColumn
secUserAuditWriteAccess = _SecUserAuditWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 17),
    _SecUserAuditWriteAccess_Type()
)
secUserAuditWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserAuditWriteAccess.setStatus("current")
_SecUserExpiration_Type = DisplayString
_SecUserExpiration_Object = MibTableColumn
secUserExpiration = _SecUserExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 18),
    _SecUserExpiration_Type()
)
secUserExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserExpiration.setStatus("current")
_SecUserCallbackNumber1_Type = DisplayString
_SecUserCallbackNumber1_Object = MibTableColumn
secUserCallbackNumber1 = _SecUserCallbackNumber1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 19),
    _SecUserCallbackNumber1_Type()
)
secUserCallbackNumber1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserCallbackNumber1.setStatus("current")
_SecUserCallbackNumber2_Type = DisplayString
_SecUserCallbackNumber2_Object = MibTableColumn
secUserCallbackNumber2 = _SecUserCallbackNumber2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 20),
    _SecUserCallbackNumber2_Type()
)
secUserCallbackNumber2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserCallbackNumber2.setStatus("current")
_SecUserCallbackNumber3_Type = DisplayString
_SecUserCallbackNumber3_Object = MibTableColumn
secUserCallbackNumber3 = _SecUserCallbackNumber3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 21),
    _SecUserCallbackNumber3_Type()
)
secUserCallbackNumber3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserCallbackNumber3.setStatus("current")
_SecUserChallengeTelnetMode_Type = DisplayString
_SecUserChallengeTelnetMode_Object = MibTableColumn
secUserChallengeTelnetMode = _SecUserChallengeTelnetMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 22),
    _SecUserChallengeTelnetMode_Type()
)
secUserChallengeTelnetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeTelnetMode.setStatus("current")
_SecUserChallengeModemMode_Type = DisplayString
_SecUserChallengeModemMode_Object = MibTableColumn
secUserChallengeModemMode = _SecUserChallengeModemMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 23),
    _SecUserChallengeModemMode_Type()
)
secUserChallengeModemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeModemMode.setStatus("current")
_SecUserChallengeConsoleMode_Type = DisplayString
_SecUserChallengeConsoleMode_Object = MibTableColumn
secUserChallengeConsoleMode = _SecUserChallengeConsoleMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 24),
    _SecUserChallengeConsoleMode_Type()
)
secUserChallengeConsoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeConsoleMode.setStatus("current")
_SecUserChallengeTelnetSendTo_Type = DisplayString
_SecUserChallengeTelnetSendTo_Object = MibTableColumn
secUserChallengeTelnetSendTo = _SecUserChallengeTelnetSendTo_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 25),
    _SecUserChallengeTelnetSendTo_Type()
)
secUserChallengeTelnetSendTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeTelnetSendTo.setStatus("current")
_SecUserChallengeModemSendTo_Type = DisplayString
_SecUserChallengeModemSendTo_Object = MibTableColumn
secUserChallengeModemSendTo = _SecUserChallengeModemSendTo_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 26),
    _SecUserChallengeModemSendTo_Type()
)
secUserChallengeModemSendTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeModemSendTo.setStatus("current")


class _SecUserChallengeExpiration_Type(Integer32):
    """Custom type secUserChallengeExpiration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_SecUserChallengeExpiration_Type.__name__ = "Integer32"
_SecUserChallengeExpiration_Object = MibTableColumn
secUserChallengeExpiration = _SecUserChallengeExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 2, 1, 27),
    _SecUserChallengeExpiration_Type()
)
secUserChallengeExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeExpiration.setStatus("current")
_SecFactory_ObjectIdentity = ObjectIdentity
secFactory = _SecFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 3)
)
_SfEnable_Type = DisplayString
_SfEnable_Object = MibScalar
sfEnable = _SfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 3, 1),
    _SfEnable_Type()
)
sfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfEnable.setStatus("current")
_SfSecret_Type = DisplayString
_SfSecret_Object = MibScalar
sfSecret = _SfSecret_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 3, 2),
    _SfSecret_Type()
)
sfSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfSecret.setStatus("current")
_SecSSH_ObjectIdentity = ObjectIdentity
secSSH = _SecSSH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 4)
)
_SecVPN_ObjectIdentity = ObjectIdentity
secVPN = _SecVPN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 11, 5)
)
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12)
)
_EvCore_ObjectIdentity = ObjectIdentity
evCore = _EvCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1)
)
_EvClassNameTable_Object = MibTable
evClassNameTable = _EvClassNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    evClassNameTable.setStatus("current")
_EvClassNameEntry_Object = MibTableRow
evClassNameEntry = _EvClassNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 1, 1)
)
evClassNameEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evClassNameIndex"),
)
if mibBuilder.loadTexts:
    evClassNameEntry.setStatus("current")


class _EvClassNameIndex_Type(Integer32):
    """Custom type evClassNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EvClassNameIndex_Type.__name__ = "Integer32"
_EvClassNameIndex_Object = MibTableColumn
evClassNameIndex = _EvClassNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 1, 1, 1),
    _EvClassNameIndex_Type()
)
evClassNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evClassNameIndex.setStatus("current")
_EvClassName_Type = DisplayString
_EvClassName_Object = MibTableColumn
evClassName = _EvClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 1, 1, 2),
    _EvClassName_Type()
)
evClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evClassName.setStatus("current")


class _EvReminderInterval_Type(Integer32):
    """Custom type evReminderInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvReminderInterval_Type.__name__ = "Integer32"
_EvReminderInterval_Object = MibScalar
evReminderInterval = _EvReminderInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 2),
    _EvReminderInterval_Type()
)
evReminderInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evReminderInterval.setStatus("current")
_EvLog_ObjectIdentity = ObjectIdentity
evLog = _EvLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3)
)
_EvLogEnable_Type = DisplayString
_EvLogEnable_Object = MibScalar
evLogEnable = _EvLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3, 1),
    _EvLogEnable_Type()
)
evLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogEnable.setStatus("current")
_EvLogStoreAlarm_Type = DisplayString
_EvLogStoreAlarm_Object = MibScalar
evLogStoreAlarm = _EvLogStoreAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3, 2),
    _EvLogStoreAlarm_Type()
)
evLogStoreAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogStoreAlarm.setStatus("current")
_EvLogMaxSize_Type = Integer32
_EvLogMaxSize_Object = MibScalar
evLogMaxSize = _EvLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3, 3),
    _EvLogMaxSize_Type()
)
evLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogMaxSize.setStatus("current")
_EvLogStoreSensor_Type = DisplayString
_EvLogStoreSensor_Object = MibScalar
evLogStoreSensor = _EvLogStoreSensor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3, 4),
    _EvLogStoreSensor_Type()
)
evLogStoreSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogStoreSensor.setStatus("current")
_EvLogTimeStampAlarms_Type = DisplayString
_EvLogTimeStampAlarms_Object = MibScalar
evLogTimeStampAlarms = _EvLogTimeStampAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3, 5),
    _EvLogTimeStampAlarms_Type()
)
evLogTimeStampAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogTimeStampAlarms.setStatus("current")
_EvLogPrependName_Type = DisplayString
_EvLogPrependName_Object = MibScalar
evLogPrependName = _EvLogPrependName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 3, 6),
    _EvLogPrependName_Type()
)
evLogPrependName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogPrependName.setStatus("current")
_EvMgmt_ObjectIdentity = ObjectIdentity
evMgmt = _EvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 4)
)
_EvMgmtReprocess_Type = DisplayString
_EvMgmtReprocess_Object = MibScalar
evMgmtReprocess = _EvMgmtReprocess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 1, 4, 3),
    _EvMgmtReprocess_Type()
)
evMgmtReprocess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evMgmtReprocess.setStatus("current")
_EvData_ObjectIdentity = ObjectIdentity
evData = _EvData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2)
)
_EvdCore_ObjectIdentity = ObjectIdentity
evdCore = _EvdCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 1)
)
_EvdExitOnTrue_Type = DisplayString
_EvdExitOnTrue_Object = MibScalar
evdExitOnTrue = _EvdExitOnTrue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 1, 1),
    _EvdExitOnTrue_Type()
)
evdExitOnTrue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdExitOnTrue.setStatus("current")
_EvdFilterAction_Type = DisplayString
_EvdFilterAction_Object = MibScalar
evdFilterAction = _EvdFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 1, 2),
    _EvdFilterAction_Type()
)
evdFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdFilterAction.setStatus("current")
_EvdWildCardChar_Type = Integer32
_EvdWildCardChar_Object = MibScalar
evdWildCardChar = _EvdWildCardChar_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 1, 3),
    _EvdWildCardChar_Type()
)
evdWildCardChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdWildCardChar.setStatus("current")
_EvdTable_Object = MibTable
evdTable = _EvdTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2)
)
if mibBuilder.loadTexts:
    evdTable.setStatus("current")
_EvdEntry_Object = MibTableRow
evdEntry = _EvdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1)
)
evdEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evdIndex"),
)
if mibBuilder.loadTexts:
    evdEntry.setStatus("current")


class _EvdIndex_Type(Integer32):
    """Custom type evdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_EvdIndex_Type.__name__ = "Integer32"
_EvdIndex_Object = MibTableColumn
evdIndex = _EvdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 1),
    _EvdIndex_Type()
)
evdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evdIndex.setStatus("current")
_EvdEnable_Type = DisplayString
_EvdEnable_Object = MibTableColumn
evdEnable = _EvdEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 2),
    _EvdEnable_Type()
)
evdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdEnable.setStatus("current")
_EvdName_Type = DisplayString
_EvdName_Object = MibTableColumn
evdName = _EvdName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 3),
    _EvdName_Type()
)
evdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdName.setStatus("current")
_EvdEquation_Type = DisplayString
_EvdEquation_Object = MibTableColumn
evdEquation = _EvdEquation_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 4),
    _EvdEquation_Type()
)
evdEquation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdEquation.setStatus("current")
_EvdThreshold_Type = Integer32
_EvdThreshold_Object = MibTableColumn
evdThreshold = _EvdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 5),
    _EvdThreshold_Type()
)
evdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdThreshold.setStatus("current")
_EvdAutoClear_Type = DisplayString
_EvdAutoClear_Object = MibTableColumn
evdAutoClear = _EvdAutoClear_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 6),
    _EvdAutoClear_Type()
)
evdAutoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdAutoClear.setStatus("current")
_EvdClearInterval_Type = DisplayString
_EvdClearInterval_Object = MibTableColumn
evdClearInterval = _EvdClearInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 7),
    _EvdClearInterval_Type()
)
evdClearInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdClearInterval.setStatus("current")
_EvdClearTime_Type = DisplayString
_EvdClearTime_Object = MibTableColumn
evdClearTime = _EvdClearTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 8),
    _EvdClearTime_Type()
)
evdClearTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdClearTime.setStatus("current")
_EvdActions_Type = DisplayString
_EvdActions_Object = MibTableColumn
evdActions = _EvdActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 9),
    _EvdActions_Type()
)
evdActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdActions.setStatus("current")
_EvdClass_Type = DisplayString
_EvdClass_Object = MibTableColumn
evdClass = _EvdClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 10),
    _EvdClass_Type()
)
evdClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdClass.setStatus("current")
_EvdTrapNum_Type = Integer32
_EvdTrapNum_Object = MibTableColumn
evdTrapNum = _EvdTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 11),
    _EvdTrapNum_Type()
)
evdTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdTrapNum.setStatus("current")
_EvdMode_Type = DisplayString
_EvdMode_Object = MibTableColumn
evdMode = _EvdMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 2, 1, 12),
    _EvdMode_Type()
)
evdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdMode.setStatus("current")
_EvdFieldTable_Object = MibTable
evdFieldTable = _EvdFieldTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3)
)
if mibBuilder.loadTexts:
    evdFieldTable.setStatus("current")
_EvdFieldEntry_Object = MibTableRow
evdFieldEntry = _EvdFieldEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1)
)
evdFieldEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evdFieldIndex"),
)
if mibBuilder.loadTexts:
    evdFieldEntry.setStatus("current")


class _EvdFieldIndex_Type(Integer32):
    """Custom type evdFieldIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvdFieldIndex_Type.__name__ = "Integer32"
_EvdFieldIndex_Object = MibTableColumn
evdFieldIndex = _EvdFieldIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1, 1),
    _EvdFieldIndex_Type()
)
evdFieldIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evdFieldIndex.setStatus("current")
_EvdFieldStart_Type = Integer32
_EvdFieldStart_Object = MibTableColumn
evdFieldStart = _EvdFieldStart_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1, 2),
    _EvdFieldStart_Type()
)
evdFieldStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdFieldStart.setStatus("current")
_EvdFieldLength_Type = Integer32
_EvdFieldLength_Object = MibTableColumn
evdFieldLength = _EvdFieldLength_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1, 3),
    _EvdFieldLength_Type()
)
evdFieldLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdFieldLength.setStatus("current")
_EvdFieldName_Type = DisplayString
_EvdFieldName_Object = MibTableColumn
evdFieldName = _EvdFieldName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1, 4),
    _EvdFieldName_Type()
)
evdFieldName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdFieldName.setStatus("current")
_EvdFieldLine_Type = Integer32
_EvdFieldLine_Object = MibTableColumn
evdFieldLine = _EvdFieldLine_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1, 5),
    _EvdFieldLine_Type()
)
evdFieldLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdFieldLine.setStatus("current")
_EvdFieldType_Type = DisplayString
_EvdFieldType_Object = MibTableColumn
evdFieldType = _EvdFieldType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 3, 1, 6),
    _EvdFieldType_Type()
)
evdFieldType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdFieldType.setStatus("current")
_EvdMacroTable_Object = MibTable
evdMacroTable = _EvdMacroTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 4)
)
if mibBuilder.loadTexts:
    evdMacroTable.setStatus("current")
_EvdMacroEntry_Object = MibTableRow
evdMacroEntry = _EvdMacroEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 4, 1)
)
evdMacroEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evdMacroIndex"),
)
if mibBuilder.loadTexts:
    evdMacroEntry.setStatus("current")


class _EvdMacroIndex_Type(Integer32):
    """Custom type evdMacroIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_EvdMacroIndex_Type.__name__ = "Integer32"
_EvdMacroIndex_Object = MibTableColumn
evdMacroIndex = _EvdMacroIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 4, 1, 1),
    _EvdMacroIndex_Type()
)
evdMacroIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evdMacroIndex.setStatus("current")
_EvdMacroName_Type = DisplayString
_EvdMacroName_Object = MibTableColumn
evdMacroName = _EvdMacroName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 4, 1, 2),
    _EvdMacroName_Type()
)
evdMacroName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdMacroName.setStatus("current")
_EvdMacroEquation_Type = DisplayString
_EvdMacroEquation_Object = MibTableColumn
evdMacroEquation = _EvdMacroEquation_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 2, 4, 1, 3),
    _EvdMacroEquation_Type()
)
evdMacroEquation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evdMacroEquation.setStatus("current")
_EvNoData1_ObjectIdentity = ObjectIdentity
evNoData1 = _EvNoData1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3)
)
_EvNoData1Enable_Type = DisplayString
_EvNoData1Enable_Object = MibScalar
evNoData1Enable = _EvNoData1Enable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 1),
    _EvNoData1Enable_Type()
)
evNoData1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Enable.setStatus("current")
_EvNoData1Actions_Type = DisplayString
_EvNoData1Actions_Object = MibScalar
evNoData1Actions = _EvNoData1Actions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 2),
    _EvNoData1Actions_Type()
)
evNoData1Actions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Actions.setStatus("current")
_EvNoData1Message_Type = DisplayString
_EvNoData1Message_Object = MibScalar
evNoData1Message = _EvNoData1Message_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 3),
    _EvNoData1Message_Type()
)
evNoData1Message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Message.setStatus("current")


class _EvNoData1TrapNum_Type(Integer32):
    """Custom type evNoData1TrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(505, 1199),
    )


_EvNoData1TrapNum_Type.__name__ = "Integer32"
_EvNoData1TrapNum_Object = MibScalar
evNoData1TrapNum = _EvNoData1TrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 4),
    _EvNoData1TrapNum_Type()
)
evNoData1TrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1TrapNum.setStatus("current")
_EvNoData1Class_Type = DisplayString
_EvNoData1Class_Object = MibScalar
evNoData1Class = _EvNoData1Class_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 5),
    _EvNoData1Class_Type()
)
evNoData1Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Class.setStatus("current")
_EvNoData1Sched1Begin_Type = DisplayString
_EvNoData1Sched1Begin_Object = MibScalar
evNoData1Sched1Begin = _EvNoData1Sched1Begin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 6),
    _EvNoData1Sched1Begin_Type()
)
evNoData1Sched1Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Sched1Begin.setStatus("current")
_EvNoData1Sched1End_Type = DisplayString
_EvNoData1Sched1End_Object = MibScalar
evNoData1Sched1End = _EvNoData1Sched1End_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 7),
    _EvNoData1Sched1End_Type()
)
evNoData1Sched1End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Sched1End.setStatus("current")


class _EvNoData1Sched1Duration_Type(Integer32):
    """Custom type evNoData1Sched1Duration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvNoData1Sched1Duration_Type.__name__ = "Integer32"
_EvNoData1Sched1Duration_Object = MibScalar
evNoData1Sched1Duration = _EvNoData1Sched1Duration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 8),
    _EvNoData1Sched1Duration_Type()
)
evNoData1Sched1Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Sched1Duration.setStatus("current")
_EvNoData1Sched2Begin_Type = DisplayString
_EvNoData1Sched2Begin_Object = MibScalar
evNoData1Sched2Begin = _EvNoData1Sched2Begin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 9),
    _EvNoData1Sched2Begin_Type()
)
evNoData1Sched2Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Sched2Begin.setStatus("current")
_EvNoData1Sched2End_Type = DisplayString
_EvNoData1Sched2End_Object = MibScalar
evNoData1Sched2End = _EvNoData1Sched2End_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 10),
    _EvNoData1Sched2End_Type()
)
evNoData1Sched2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Sched2End.setStatus("current")


class _EvNoData1Sched2Duration_Type(Integer32):
    """Custom type evNoData1Sched2Duration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvNoData1Sched2Duration_Type.__name__ = "Integer32"
_EvNoData1Sched2Duration_Object = MibScalar
evNoData1Sched2Duration = _EvNoData1Sched2Duration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 11),
    _EvNoData1Sched2Duration_Type()
)
evNoData1Sched2Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Sched2Duration.setStatus("current")
_EvNoData1PortEnableTable_Object = MibTable
evNoData1PortEnableTable = _EvNoData1PortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 12)
)
if mibBuilder.loadTexts:
    evNoData1PortEnableTable.setStatus("current")
_EvNoData1PortEnableEntry_Object = MibTableRow
evNoData1PortEnableEntry = _EvNoData1PortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 12, 1)
)
evNoData1PortEnableEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evNoData1PortEnableIndex"),
)
if mibBuilder.loadTexts:
    evNoData1PortEnableEntry.setStatus("current")


class _EvNoData1PortEnableIndex_Type(Integer32):
    """Custom type evNoData1PortEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvNoData1PortEnableIndex_Type.__name__ = "Integer32"
_EvNoData1PortEnableIndex_Object = MibTableColumn
evNoData1PortEnableIndex = _EvNoData1PortEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 12, 1, 1),
    _EvNoData1PortEnableIndex_Type()
)
evNoData1PortEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evNoData1PortEnableIndex.setStatus("current")
_EvNoData1PortEnable_Type = DisplayString
_EvNoData1PortEnable_Object = MibTableColumn
evNoData1PortEnable = _EvNoData1PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 12, 1, 2),
    _EvNoData1PortEnable_Type()
)
evNoData1PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1PortEnable.setStatus("current")
_EvNoData1Exclusions_Type = DisplayString
_EvNoData1Exclusions_Object = MibScalar
evNoData1Exclusions = _EvNoData1Exclusions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 13),
    _EvNoData1Exclusions_Type()
)
evNoData1Exclusions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Exclusions.setStatus("current")
_EvNoData1Days_Type = DisplayString
_EvNoData1Days_Object = MibScalar
evNoData1Days = _EvNoData1Days_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 3, 14),
    _EvNoData1Days_Type()
)
evNoData1Days.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData1Days.setStatus("current")
_EvNoData2_ObjectIdentity = ObjectIdentity
evNoData2 = _EvNoData2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4)
)
_EvNoData2Enable_Type = DisplayString
_EvNoData2Enable_Object = MibScalar
evNoData2Enable = _EvNoData2Enable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 1),
    _EvNoData2Enable_Type()
)
evNoData2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Enable.setStatus("current")
_EvNoData2Actions_Type = DisplayString
_EvNoData2Actions_Object = MibScalar
evNoData2Actions = _EvNoData2Actions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 2),
    _EvNoData2Actions_Type()
)
evNoData2Actions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Actions.setStatus("current")
_EvNoData2Message_Type = DisplayString
_EvNoData2Message_Object = MibScalar
evNoData2Message = _EvNoData2Message_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 3),
    _EvNoData2Message_Type()
)
evNoData2Message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Message.setStatus("current")


class _EvNoData2TrapNum_Type(Integer32):
    """Custom type evNoData2TrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(505, 1199),
    )


_EvNoData2TrapNum_Type.__name__ = "Integer32"
_EvNoData2TrapNum_Object = MibScalar
evNoData2TrapNum = _EvNoData2TrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 4),
    _EvNoData2TrapNum_Type()
)
evNoData2TrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2TrapNum.setStatus("current")
_EvNoData2Class_Type = DisplayString
_EvNoData2Class_Object = MibScalar
evNoData2Class = _EvNoData2Class_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 5),
    _EvNoData2Class_Type()
)
evNoData2Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Class.setStatus("current")
_EvNoData2Sched1Begin_Type = DisplayString
_EvNoData2Sched1Begin_Object = MibScalar
evNoData2Sched1Begin = _EvNoData2Sched1Begin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 6),
    _EvNoData2Sched1Begin_Type()
)
evNoData2Sched1Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Sched1Begin.setStatus("current")
_EvNoData2Sched1End_Type = DisplayString
_EvNoData2Sched1End_Object = MibScalar
evNoData2Sched1End = _EvNoData2Sched1End_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 7),
    _EvNoData2Sched1End_Type()
)
evNoData2Sched1End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Sched1End.setStatus("current")


class _EvNoData2Sched1Duration_Type(Integer32):
    """Custom type evNoData2Sched1Duration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvNoData2Sched1Duration_Type.__name__ = "Integer32"
_EvNoData2Sched1Duration_Object = MibScalar
evNoData2Sched1Duration = _EvNoData2Sched1Duration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 8),
    _EvNoData2Sched1Duration_Type()
)
evNoData2Sched1Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Sched1Duration.setStatus("current")
_EvNoData2Sched2Begin_Type = DisplayString
_EvNoData2Sched2Begin_Object = MibScalar
evNoData2Sched2Begin = _EvNoData2Sched2Begin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 9),
    _EvNoData2Sched2Begin_Type()
)
evNoData2Sched2Begin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Sched2Begin.setStatus("current")
_EvNoData2Sched2End_Type = DisplayString
_EvNoData2Sched2End_Object = MibScalar
evNoData2Sched2End = _EvNoData2Sched2End_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 10),
    _EvNoData2Sched2End_Type()
)
evNoData2Sched2End.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Sched2End.setStatus("current")


class _EvNoData2Sched2Duration_Type(Integer32):
    """Custom type evNoData2Sched2Duration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvNoData2Sched2Duration_Type.__name__ = "Integer32"
_EvNoData2Sched2Duration_Object = MibScalar
evNoData2Sched2Duration = _EvNoData2Sched2Duration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 11),
    _EvNoData2Sched2Duration_Type()
)
evNoData2Sched2Duration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Sched2Duration.setStatus("current")
_EvNoData2PortEnableTable_Object = MibTable
evNoData2PortEnableTable = _EvNoData2PortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 12)
)
if mibBuilder.loadTexts:
    evNoData2PortEnableTable.setStatus("current")
_EvNoData2PortEnableEntry_Object = MibTableRow
evNoData2PortEnableEntry = _EvNoData2PortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 12, 1)
)
evNoData2PortEnableEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evNoData2PortEnableIndex"),
)
if mibBuilder.loadTexts:
    evNoData2PortEnableEntry.setStatus("current")


class _EvNoData2PortEnableIndex_Type(Integer32):
    """Custom type evNoData2PortEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvNoData2PortEnableIndex_Type.__name__ = "Integer32"
_EvNoData2PortEnableIndex_Object = MibTableColumn
evNoData2PortEnableIndex = _EvNoData2PortEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 12, 1, 1),
    _EvNoData2PortEnableIndex_Type()
)
evNoData2PortEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evNoData2PortEnableIndex.setStatus("current")
_EvNoData2PortEnable_Type = DisplayString
_EvNoData2PortEnable_Object = MibTableColumn
evNoData2PortEnable = _EvNoData2PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 12, 1, 2),
    _EvNoData2PortEnable_Type()
)
evNoData2PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2PortEnable.setStatus("current")
_EvNoData2Exclusions_Type = DisplayString
_EvNoData2Exclusions_Object = MibScalar
evNoData2Exclusions = _EvNoData2Exclusions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 13),
    _EvNoData2Exclusions_Type()
)
evNoData2Exclusions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Exclusions.setStatus("current")
_EvNoData2Days_Type = DisplayString
_EvNoData2Days_Object = MibScalar
evNoData2Days = _EvNoData2Days_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 4, 14),
    _EvNoData2Days_Type()
)
evNoData2Days.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoData2Days.setStatus("current")
_EvSched1_ObjectIdentity = ObjectIdentity
evSched1 = _EvSched1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5)
)
_EvSched1Enable_Type = DisplayString
_EvSched1Enable_Object = MibScalar
evSched1Enable = _EvSched1Enable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 1),
    _EvSched1Enable_Type()
)
evSched1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Enable.setStatus("current")
_EvSched1Actions_Type = DisplayString
_EvSched1Actions_Object = MibScalar
evSched1Actions = _EvSched1Actions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 2),
    _EvSched1Actions_Type()
)
evSched1Actions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Actions.setStatus("current")
_EvSched1Message_Type = DisplayString
_EvSched1Message_Object = MibScalar
evSched1Message = _EvSched1Message_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 3),
    _EvSched1Message_Type()
)
evSched1Message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Message.setStatus("current")
_EvSched1TrapNum_Type = Integer32
_EvSched1TrapNum_Object = MibScalar
evSched1TrapNum = _EvSched1TrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 4),
    _EvSched1TrapNum_Type()
)
evSched1TrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1TrapNum.setStatus("current")
_EvSched1Class_Type = DisplayString
_EvSched1Class_Object = MibScalar
evSched1Class = _EvSched1Class_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 5),
    _EvSched1Class_Type()
)
evSched1Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Class.setStatus("current")
_EvSched1Sunday_Type = DisplayString
_EvSched1Sunday_Object = MibScalar
evSched1Sunday = _EvSched1Sunday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 6),
    _EvSched1Sunday_Type()
)
evSched1Sunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Sunday.setStatus("current")
_EvSched1Monday_Type = DisplayString
_EvSched1Monday_Object = MibScalar
evSched1Monday = _EvSched1Monday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 7),
    _EvSched1Monday_Type()
)
evSched1Monday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Monday.setStatus("current")
_EvSched1Tuesday_Type = DisplayString
_EvSched1Tuesday_Object = MibScalar
evSched1Tuesday = _EvSched1Tuesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 8),
    _EvSched1Tuesday_Type()
)
evSched1Tuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Tuesday.setStatus("current")
_EvSched1Wednesday_Type = DisplayString
_EvSched1Wednesday_Object = MibScalar
evSched1Wednesday = _EvSched1Wednesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 9),
    _EvSched1Wednesday_Type()
)
evSched1Wednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Wednesday.setStatus("current")
_EvSched1Thursday_Type = DisplayString
_EvSched1Thursday_Object = MibScalar
evSched1Thursday = _EvSched1Thursday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 10),
    _EvSched1Thursday_Type()
)
evSched1Thursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Thursday.setStatus("current")
_EvSched1Friday_Type = DisplayString
_EvSched1Friday_Object = MibScalar
evSched1Friday = _EvSched1Friday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 11),
    _EvSched1Friday_Type()
)
evSched1Friday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Friday.setStatus("current")
_EvSched1Saturday_Type = DisplayString
_EvSched1Saturday_Object = MibScalar
evSched1Saturday = _EvSched1Saturday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 12),
    _EvSched1Saturday_Type()
)
evSched1Saturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Saturday.setStatus("current")
_EvSched1Exclusions_Type = DisplayString
_EvSched1Exclusions_Object = MibScalar
evSched1Exclusions = _EvSched1Exclusions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 5, 13),
    _EvSched1Exclusions_Type()
)
evSched1Exclusions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Exclusions.setStatus("current")
_EvSched2_ObjectIdentity = ObjectIdentity
evSched2 = _EvSched2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6)
)
_EvSched2Enable_Type = DisplayString
_EvSched2Enable_Object = MibScalar
evSched2Enable = _EvSched2Enable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 1),
    _EvSched2Enable_Type()
)
evSched2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Enable.setStatus("current")
_EvSched2Actions_Type = DisplayString
_EvSched2Actions_Object = MibScalar
evSched2Actions = _EvSched2Actions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 2),
    _EvSched2Actions_Type()
)
evSched2Actions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Actions.setStatus("current")
_EvSched2Message_Type = DisplayString
_EvSched2Message_Object = MibScalar
evSched2Message = _EvSched2Message_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 3),
    _EvSched2Message_Type()
)
evSched2Message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Message.setStatus("current")
_EvSched2TrapNum_Type = Integer32
_EvSched2TrapNum_Object = MibScalar
evSched2TrapNum = _EvSched2TrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 4),
    _EvSched2TrapNum_Type()
)
evSched2TrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2TrapNum.setStatus("current")
_EvSched2Class_Type = DisplayString
_EvSched2Class_Object = MibScalar
evSched2Class = _EvSched2Class_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 5),
    _EvSched2Class_Type()
)
evSched2Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Class.setStatus("current")
_EvSched2Sunday_Type = DisplayString
_EvSched2Sunday_Object = MibScalar
evSched2Sunday = _EvSched2Sunday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 6),
    _EvSched2Sunday_Type()
)
evSched2Sunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Sunday.setStatus("current")
_EvSched2Monday_Type = DisplayString
_EvSched2Monday_Object = MibScalar
evSched2Monday = _EvSched2Monday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 7),
    _EvSched2Monday_Type()
)
evSched2Monday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Monday.setStatus("current")
_EvSched2Tuesday_Type = DisplayString
_EvSched2Tuesday_Object = MibScalar
evSched2Tuesday = _EvSched2Tuesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 8),
    _EvSched2Tuesday_Type()
)
evSched2Tuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Tuesday.setStatus("current")
_EvSched2Wednesday_Type = DisplayString
_EvSched2Wednesday_Object = MibScalar
evSched2Wednesday = _EvSched2Wednesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 9),
    _EvSched2Wednesday_Type()
)
evSched2Wednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Wednesday.setStatus("current")
_EvSched2Thursday_Type = DisplayString
_EvSched2Thursday_Object = MibScalar
evSched2Thursday = _EvSched2Thursday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 10),
    _EvSched2Thursday_Type()
)
evSched2Thursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Thursday.setStatus("current")
_EvSched2Friday_Type = DisplayString
_EvSched2Friday_Object = MibScalar
evSched2Friday = _EvSched2Friday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 11),
    _EvSched2Friday_Type()
)
evSched2Friday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Friday.setStatus("current")
_EvSched2Saturday_Type = DisplayString
_EvSched2Saturday_Object = MibScalar
evSched2Saturday = _EvSched2Saturday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 12),
    _EvSched2Saturday_Type()
)
evSched2Saturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Saturday.setStatus("current")
_EvSched2Exclusions_Type = DisplayString
_EvSched2Exclusions_Object = MibScalar
evSched2Exclusions = _EvSched2Exclusions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 6, 13),
    _EvSched2Exclusions_Type()
)
evSched2Exclusions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Exclusions.setStatus("current")
_EvShskLowTable_Object = MibTable
evShskLowTable = _EvShskLowTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7)
)
if mibBuilder.loadTexts:
    evShskLowTable.setStatus("current")
_EvShskLowEntry_Object = MibTableRow
evShskLowEntry = _EvShskLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1)
)
evShskLowEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evShskLowIndex"),
)
if mibBuilder.loadTexts:
    evShskLowEntry.setStatus("current")


class _EvShskLowIndex_Type(Integer32):
    """Custom type evShskLowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvShskLowIndex_Type.__name__ = "Integer32"
_EvShskLowIndex_Object = MibTableColumn
evShskLowIndex = _EvShskLowIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1, 1),
    _EvShskLowIndex_Type()
)
evShskLowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evShskLowIndex.setStatus("current")
_EvShskLowEnable_Type = DisplayString
_EvShskLowEnable_Object = MibTableColumn
evShskLowEnable = _EvShskLowEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1, 2),
    _EvShskLowEnable_Type()
)
evShskLowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowEnable.setStatus("current")
_EvShskLowActions_Type = DisplayString
_EvShskLowActions_Object = MibTableColumn
evShskLowActions = _EvShskLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1, 3),
    _EvShskLowActions_Type()
)
evShskLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowActions.setStatus("current")
_EvShskLowMessage_Type = DisplayString
_EvShskLowMessage_Object = MibTableColumn
evShskLowMessage = _EvShskLowMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1, 4),
    _EvShskLowMessage_Type()
)
evShskLowMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowMessage.setStatus("current")
_EvShskLowClass_Type = DisplayString
_EvShskLowClass_Object = MibTableColumn
evShskLowClass = _EvShskLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1, 5),
    _EvShskLowClass_Type()
)
evShskLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowClass.setStatus("current")
_EvShskLowTrapNum_Type = Integer32
_EvShskLowTrapNum_Object = MibTableColumn
evShskLowTrapNum = _EvShskLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 7, 1, 6),
    _EvShskLowTrapNum_Type()
)
evShskLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowTrapNum.setStatus("current")
_EvShskHighTable_Object = MibTable
evShskHighTable = _EvShskHighTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8)
)
if mibBuilder.loadTexts:
    evShskHighTable.setStatus("current")
_EvShskHighEntry_Object = MibTableRow
evShskHighEntry = _EvShskHighEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1)
)
evShskHighEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "evShskHighIndex"),
)
if mibBuilder.loadTexts:
    evShskHighEntry.setStatus("current")


class _EvShskHighIndex_Type(Integer32):
    """Custom type evShskHighIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvShskHighIndex_Type.__name__ = "Integer32"
_EvShskHighIndex_Object = MibTableColumn
evShskHighIndex = _EvShskHighIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1, 1),
    _EvShskHighIndex_Type()
)
evShskHighIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evShskHighIndex.setStatus("current")
_EvShskHighEnable_Type = DisplayString
_EvShskHighEnable_Object = MibTableColumn
evShskHighEnable = _EvShskHighEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1, 2),
    _EvShskHighEnable_Type()
)
evShskHighEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighEnable.setStatus("current")
_EvShskHighActions_Type = DisplayString
_EvShskHighActions_Object = MibTableColumn
evShskHighActions = _EvShskHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1, 3),
    _EvShskHighActions_Type()
)
evShskHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighActions.setStatus("current")
_EvShskHighMessage_Type = DisplayString
_EvShskHighMessage_Object = MibTableColumn
evShskHighMessage = _EvShskHighMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1, 4),
    _EvShskHighMessage_Type()
)
evShskHighMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighMessage.setStatus("current")
_EvShskHighClass_Type = DisplayString
_EvShskHighClass_Object = MibTableColumn
evShskHighClass = _EvShskHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1, 5),
    _EvShskHighClass_Type()
)
evShskHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighClass.setStatus("current")
_EvShskHighTrapNum_Type = Integer32
_EvShskHighTrapNum_Object = MibTableColumn
evShskHighTrapNum = _EvShskHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 8, 1, 6),
    _EvShskHighTrapNum_Type()
)
evShskHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighTrapNum.setStatus("current")
_EvNoSensor_ObjectIdentity = ObjectIdentity
evNoSensor = _EvNoSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 9)
)
_EvNoSensorTimeout_Type = Integer32
_EvNoSensorTimeout_Object = MibScalar
evNoSensorTimeout = _EvNoSensorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 9, 1),
    _EvNoSensorTimeout_Type()
)
evNoSensorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorTimeout.setStatus("current")
_EvNoSensorActions_Type = DisplayString
_EvNoSensorActions_Object = MibScalar
evNoSensorActions = _EvNoSensorActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 9, 2),
    _EvNoSensorActions_Type()
)
evNoSensorActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorActions.setStatus("current")
_EvNoSensorTrapNum_Type = Integer32
_EvNoSensorTrapNum_Object = MibScalar
evNoSensorTrapNum = _EvNoSensorTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 9, 3),
    _EvNoSensorTrapNum_Type()
)
evNoSensorTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorTrapNum.setStatus("current")
_EvNoSensorClass_Type = DisplayString
_EvNoSensorClass_Object = MibScalar
evNoSensorClass = _EvNoSensorClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 9, 4),
    _EvNoSensorClass_Type()
)
evNoSensorClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorClass.setStatus("current")
_FuelSensor_ObjectIdentity = ObjectIdentity
fuelSensor = _FuelSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11)
)
_FuelSensorGeneralTable_Object = MibTable
fuelSensorGeneralTable = _FuelSensorGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1)
)
if mibBuilder.loadTexts:
    fuelSensorGeneralTable.setStatus("current")
_FsGenEntry_Object = MibTableRow
fsGenEntry = _FsGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1)
)
fsGenEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "fsGenIndex"),
)
if mibBuilder.loadTexts:
    fsGenEntry.setStatus("current")


class _FsGenIndex_Type(Integer32):
    """Custom type fsGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsGenIndex_Type.__name__ = "Integer32"
_FsGenIndex_Object = MibTableColumn
fsGenIndex = _FsGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 1),
    _FsGenIndex_Type()
)
fsGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGenIndex.setStatus("current")
_FsGenName_Type = DisplayString
_FsGenName_Object = MibTableColumn
fsGenName = _FsGenName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 2),
    _FsGenName_Type()
)
fsGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenName.setStatus("current")
_FsGenSensorType_Type = DisplayString
_FsGenSensorType_Object = MibTableColumn
fsGenSensorType = _FsGenSensorType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 3),
    _FsGenSensorType_Type()
)
fsGenSensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSensorType.setStatus("current")
_FsGenDistanceUnit_Type = DisplayString
_FsGenDistanceUnit_Object = MibTableColumn
fsGenDistanceUnit = _FsGenDistanceUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 4),
    _FsGenDistanceUnit_Type()
)
fsGenDistanceUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenDistanceUnit.setStatus("current")
_FsGenRawValueTop_Type = DisplayString
_FsGenRawValueTop_Object = MibTableColumn
fsGenRawValueTop = _FsGenRawValueTop_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 5),
    _FsGenRawValueTop_Type()
)
fsGenRawValueTop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenRawValueTop.setStatus("current")
_FsGenTopOffset_Type = DisplayString
_FsGenTopOffset_Object = MibTableColumn
fsGenTopOffset = _FsGenTopOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 6),
    _FsGenTopOffset_Type()
)
fsGenTopOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenTopOffset.setStatus("current")
_FsGenRawValueBottom_Type = DisplayString
_FsGenRawValueBottom_Object = MibTableColumn
fsGenRawValueBottom = _FsGenRawValueBottom_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 7),
    _FsGenRawValueBottom_Type()
)
fsGenRawValueBottom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenRawValueBottom.setStatus("current")
_FsGenBottomOffset_Type = DisplayString
_FsGenBottomOffset_Object = MibTableColumn
fsGenBottomOffset = _FsGenBottomOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 8),
    _FsGenBottomOffset_Type()
)
fsGenBottomOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenBottomOffset.setStatus("current")


class _FsGenInputES_Type(Integer32):
    """Custom type fsGenInputES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FsGenInputES_Type.__name__ = "Integer32"
_FsGenInputES_Object = MibTableColumn
fsGenInputES = _FsGenInputES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 9),
    _FsGenInputES_Type()
)
fsGenInputES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenInputES.setStatus("current")


class _FsGenInputPoint_Type(Integer32):
    """Custom type fsGenInputPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsGenInputPoint_Type.__name__ = "Integer32"
_FsGenInputPoint_Object = MibTableColumn
fsGenInputPoint = _FsGenInputPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 10),
    _FsGenInputPoint_Type()
)
fsGenInputPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenInputPoint.setStatus("current")
_FsGenFilterAveraging_Type = Integer32
_FsGenFilterAveraging_Object = MibTableColumn
fsGenFilterAveraging = _FsGenFilterAveraging_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 11),
    _FsGenFilterAveraging_Type()
)
fsGenFilterAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenFilterAveraging.setStatus("current")
_FsGenSysrepEnable_Type = DisplayString
_FsGenSysrepEnable_Object = MibTableColumn
fsGenSysrepEnable = _FsGenSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 12),
    _FsGenSysrepEnable_Type()
)
fsGenSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepEnable.setStatus("current")
_FsGenSysrepThreshold_Type = DisplayString
_FsGenSysrepThreshold_Object = MibTableColumn
fsGenSysrepThreshold = _FsGenSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 13),
    _FsGenSysrepThreshold_Type()
)
fsGenSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepThreshold.setStatus("current")
_FsGenSysrepLimit_Type = Integer32
_FsGenSysrepLimit_Object = MibTableColumn
fsGenSysrepLimit = _FsGenSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 14),
    _FsGenSysrepLimit_Type()
)
fsGenSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepLimit.setStatus("current")


class _FsGenSysrepPackage_Type(Integer32):
    """Custom type fsGenSysrepPackage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsGenSysrepPackage_Type.__name__ = "Integer32"
_FsGenSysrepPackage_Object = MibTableColumn
fsGenSysrepPackage = _FsGenSysrepPackage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 15),
    _FsGenSysrepPackage_Type()
)
fsGenSysrepPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepPackage.setStatus("current")
_FsGenSysrepType_Type = DisplayString
_FsGenSysrepType_Object = MibTableColumn
fsGenSysrepType = _FsGenSysrepType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 1, 1, 16),
    _FsGenSysrepType_Type()
)
fsGenSysrepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepType.setStatus("current")
_FuelSensorTankTable_Object = MibTable
fuelSensorTankTable = _FuelSensorTankTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2)
)
if mibBuilder.loadTexts:
    fuelSensorTankTable.setStatus("current")
_FsTankEntry_Object = MibTableRow
fsTankEntry = _FsTankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1)
)
fsTankEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "fsTankIndex"),
)
if mibBuilder.loadTexts:
    fsTankEntry.setStatus("current")


class _FsTankIndex_Type(Integer32):
    """Custom type fsTankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsTankIndex_Type.__name__ = "Integer32"
_FsTankIndex_Object = MibTableColumn
fsTankIndex = _FsTankIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 1),
    _FsTankIndex_Type()
)
fsTankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTankIndex.setStatus("current")
_FsTankHeight_Type = DisplayString
_FsTankHeight_Object = MibTableColumn
fsTankHeight = _FsTankHeight_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 2),
    _FsTankHeight_Type()
)
fsTankHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankHeight.setStatus("current")
_FsTankDimA_Type = DisplayString
_FsTankDimA_Object = MibTableColumn
fsTankDimA = _FsTankDimA_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 3),
    _FsTankDimA_Type()
)
fsTankDimA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankDimA.setStatus("current")
_FsTankDimB_Type = DisplayString
_FsTankDimB_Object = MibTableColumn
fsTankDimB = _FsTankDimB_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 4),
    _FsTankDimB_Type()
)
fsTankDimB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankDimB.setStatus("current")
_FsTankVolume_Type = DisplayString
_FsTankVolume_Object = MibTableColumn
fsTankVolume = _FsTankVolume_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 5),
    _FsTankVolume_Type()
)
fsTankVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankVolume.setStatus("current")
_FsTankVolumeUnit_Type = DisplayString
_FsTankVolumeUnit_Object = MibTableColumn
fsTankVolumeUnit = _FsTankVolumeUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 6),
    _FsTankVolumeUnit_Type()
)
fsTankVolumeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankVolumeUnit.setStatus("current")
_FsTankShape_Type = DisplayString
_FsTankShape_Object = MibTableColumn
fsTankShape = _FsTankShape_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 2, 1, 7),
    _FsTankShape_Type()
)
fsTankShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankShape.setStatus("current")
_FuelSensorCustomTankTable_Object = MibTable
fuelSensorCustomTankTable = _FuelSensorCustomTankTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 3)
)
if mibBuilder.loadTexts:
    fuelSensorCustomTankTable.setStatus("current")
_FsCustomTankEntry_Object = MibTableRow
fsCustomTankEntry = _FsCustomTankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 3, 1)
)
fsCustomTankEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "fsCustomTankIndexFS"),
    (0, "SITEBOSS-570-STD-MIB", "fsCustomTankIndexDatum"),
)
if mibBuilder.loadTexts:
    fsCustomTankEntry.setStatus("current")


class _FsCustomTankIndexFS_Type(Integer32):
    """Custom type fsCustomTankIndexFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsCustomTankIndexFS_Type.__name__ = "Integer32"
_FsCustomTankIndexFS_Object = MibTableColumn
fsCustomTankIndexFS = _FsCustomTankIndexFS_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 3, 1, 1),
    _FsCustomTankIndexFS_Type()
)
fsCustomTankIndexFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCustomTankIndexFS.setStatus("current")


class _FsCustomTankIndexDatum_Type(Integer32):
    """Custom type fsCustomTankIndexDatum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsCustomTankIndexDatum_Type.__name__ = "Integer32"
_FsCustomTankIndexDatum_Object = MibTableColumn
fsCustomTankIndexDatum = _FsCustomTankIndexDatum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 3, 1, 2),
    _FsCustomTankIndexDatum_Type()
)
fsCustomTankIndexDatum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCustomTankIndexDatum.setStatus("current")
_FsCustomTankHeight_Type = DisplayString
_FsCustomTankHeight_Object = MibTableColumn
fsCustomTankHeight = _FsCustomTankHeight_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 3, 1, 3),
    _FsCustomTankHeight_Type()
)
fsCustomTankHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCustomTankHeight.setStatus("current")
_FsCustomTankVolume_Type = DisplayString
_FsCustomTankVolume_Object = MibTableColumn
fsCustomTankVolume = _FsCustomTankVolume_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 3, 1, 4),
    _FsCustomTankVolume_Type()
)
fsCustomTankVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCustomTankVolume.setStatus("current")
_FuelSensorVolumeTable_Object = MibTable
fuelSensorVolumeTable = _FuelSensorVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4)
)
if mibBuilder.loadTexts:
    fuelSensorVolumeTable.setStatus("current")
_FsVolumeEntry_Object = MibTableRow
fsVolumeEntry = _FsVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1)
)
fsVolumeEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "fsVolumeIndex"),
)
if mibBuilder.loadTexts:
    fsVolumeEntry.setStatus("current")


class _FsVolumeIndex_Type(Integer32):
    """Custom type fsVolumeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsVolumeIndex_Type.__name__ = "Integer32"
_FsVolumeIndex_Object = MibTableColumn
fsVolumeIndex = _FsVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 1),
    _FsVolumeIndex_Type()
)
fsVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVolumeIndex.setStatus("current")
_FsVolumeEnable_Type = DisplayString
_FsVolumeEnable_Object = MibTableColumn
fsVolumeEnable = _FsVolumeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 2),
    _FsVolumeEnable_Type()
)
fsVolumeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeEnable.setStatus("current")
_FsVolumeDeadband_Type = DisplayString
_FsVolumeDeadband_Object = MibTableColumn
fsVolumeDeadband = _FsVolumeDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 3),
    _FsVolumeDeadband_Type()
)
fsVolumeDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeDeadband.setStatus("current")
_FsVolumeVHighValue_Type = DisplayString
_FsVolumeVHighValue_Object = MibTableColumn
fsVolumeVHighValue = _FsVolumeVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 4),
    _FsVolumeVHighValue_Type()
)
fsVolumeVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighValue.setStatus("current")
_FsVolumeVHighActions_Type = DisplayString
_FsVolumeVHighActions_Object = MibTableColumn
fsVolumeVHighActions = _FsVolumeVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 5),
    _FsVolumeVHighActions_Type()
)
fsVolumeVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighActions.setStatus("current")


class _FsVolumeVHighTrapNum_Type(Integer32):
    """Custom type fsVolumeVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeVHighTrapNum_Type.__name__ = "Integer32"
_FsVolumeVHighTrapNum_Object = MibTableColumn
fsVolumeVHighTrapNum = _FsVolumeVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 6),
    _FsVolumeVHighTrapNum_Type()
)
fsVolumeVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighTrapNum.setStatus("current")
_FsVolumeVHighClass_Type = DisplayString
_FsVolumeVHighClass_Object = MibTableColumn
fsVolumeVHighClass = _FsVolumeVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 7),
    _FsVolumeVHighClass_Type()
)
fsVolumeVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighClass.setStatus("current")
_FsVolumeHighValue_Type = DisplayString
_FsVolumeHighValue_Object = MibTableColumn
fsVolumeHighValue = _FsVolumeHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 8),
    _FsVolumeHighValue_Type()
)
fsVolumeHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighValue.setStatus("current")
_FsVolumeHighActions_Type = DisplayString
_FsVolumeHighActions_Object = MibTableColumn
fsVolumeHighActions = _FsVolumeHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 9),
    _FsVolumeHighActions_Type()
)
fsVolumeHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighActions.setStatus("current")


class _FsVolumeHighTrapNum_Type(Integer32):
    """Custom type fsVolumeHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeHighTrapNum_Type.__name__ = "Integer32"
_FsVolumeHighTrapNum_Object = MibTableColumn
fsVolumeHighTrapNum = _FsVolumeHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 10),
    _FsVolumeHighTrapNum_Type()
)
fsVolumeHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighTrapNum.setStatus("current")
_FsVolumeHighClass_Type = DisplayString
_FsVolumeHighClass_Object = MibTableColumn
fsVolumeHighClass = _FsVolumeHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 11),
    _FsVolumeHighClass_Type()
)
fsVolumeHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighClass.setStatus("current")
_FsVolumeNormalActions_Type = DisplayString
_FsVolumeNormalActions_Object = MibTableColumn
fsVolumeNormalActions = _FsVolumeNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 12),
    _FsVolumeNormalActions_Type()
)
fsVolumeNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeNormalActions.setStatus("current")


class _FsVolumeNormalTrapNum_Type(Integer32):
    """Custom type fsVolumeNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeNormalTrapNum_Type.__name__ = "Integer32"
_FsVolumeNormalTrapNum_Object = MibTableColumn
fsVolumeNormalTrapNum = _FsVolumeNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 13),
    _FsVolumeNormalTrapNum_Type()
)
fsVolumeNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeNormalTrapNum.setStatus("current")
_FsVolumeNormalClass_Type = DisplayString
_FsVolumeNormalClass_Object = MibTableColumn
fsVolumeNormalClass = _FsVolumeNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 14),
    _FsVolumeNormalClass_Type()
)
fsVolumeNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeNormalClass.setStatus("current")
_FsVolumeLowValue_Type = DisplayString
_FsVolumeLowValue_Object = MibTableColumn
fsVolumeLowValue = _FsVolumeLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 15),
    _FsVolumeLowValue_Type()
)
fsVolumeLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowValue.setStatus("current")
_FsVolumeLowActions_Type = DisplayString
_FsVolumeLowActions_Object = MibTableColumn
fsVolumeLowActions = _FsVolumeLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 16),
    _FsVolumeLowActions_Type()
)
fsVolumeLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowActions.setStatus("current")


class _FsVolumeLowTrapNum_Type(Integer32):
    """Custom type fsVolumeLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeLowTrapNum_Type.__name__ = "Integer32"
_FsVolumeLowTrapNum_Object = MibTableColumn
fsVolumeLowTrapNum = _FsVolumeLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 17),
    _FsVolumeLowTrapNum_Type()
)
fsVolumeLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowTrapNum.setStatus("current")
_FsVolumeLowClass_Type = DisplayString
_FsVolumeLowClass_Object = MibTableColumn
fsVolumeLowClass = _FsVolumeLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 18),
    _FsVolumeLowClass_Type()
)
fsVolumeLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowClass.setStatus("current")
_FsVolumeVLowValue_Type = DisplayString
_FsVolumeVLowValue_Object = MibTableColumn
fsVolumeVLowValue = _FsVolumeVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 19),
    _FsVolumeVLowValue_Type()
)
fsVolumeVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowValue.setStatus("current")
_FsVolumeVLowActions_Type = DisplayString
_FsVolumeVLowActions_Object = MibTableColumn
fsVolumeVLowActions = _FsVolumeVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 20),
    _FsVolumeVLowActions_Type()
)
fsVolumeVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowActions.setStatus("current")


class _FsVolumeVLowTrapNum_Type(Integer32):
    """Custom type fsVolumeVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeVLowTrapNum_Type.__name__ = "Integer32"
_FsVolumeVLowTrapNum_Object = MibTableColumn
fsVolumeVLowTrapNum = _FsVolumeVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 21),
    _FsVolumeVLowTrapNum_Type()
)
fsVolumeVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowTrapNum.setStatus("current")
_FsVolumeVLowClass_Type = DisplayString
_FsVolumeVLowClass_Object = MibTableColumn
fsVolumeVLowClass = _FsVolumeVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 4, 1, 22),
    _FsVolumeVLowClass_Type()
)
fsVolumeVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowClass.setStatus("current")
_FuelSensorDisconnectTable_Object = MibTable
fuelSensorDisconnectTable = _FuelSensorDisconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5)
)
if mibBuilder.loadTexts:
    fuelSensorDisconnectTable.setStatus("current")
_FsDiscEntry_Object = MibTableRow
fsDiscEntry = _FsDiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1)
)
fsDiscEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "fsDiscIndex"),
)
if mibBuilder.loadTexts:
    fsDiscEntry.setStatus("current")


class _FsDiscIndex_Type(Integer32):
    """Custom type fsDiscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsDiscIndex_Type.__name__ = "Integer32"
_FsDiscIndex_Object = MibTableColumn
fsDiscIndex = _FsDiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 1),
    _FsDiscIndex_Type()
)
fsDiscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiscIndex.setStatus("current")
_FsDiscEnable_Type = DisplayString
_FsDiscEnable_Object = MibTableColumn
fsDiscEnable = _FsDiscEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 2),
    _FsDiscEnable_Type()
)
fsDiscEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscEnable.setStatus("current")
_FsDiscHighValue_Type = DisplayString
_FsDiscHighValue_Object = MibTableColumn
fsDiscHighValue = _FsDiscHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 3),
    _FsDiscHighValue_Type()
)
fsDiscHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscHighValue.setStatus("current")
_FsDiscLowValue_Type = DisplayString
_FsDiscLowValue_Object = MibTableColumn
fsDiscLowValue = _FsDiscLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 4),
    _FsDiscLowValue_Type()
)
fsDiscLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscLowValue.setStatus("current")
_FsDiscActions_Type = DisplayString
_FsDiscActions_Object = MibTableColumn
fsDiscActions = _FsDiscActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 5),
    _FsDiscActions_Type()
)
fsDiscActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscActions.setStatus("current")


class _FsDiscTrapNum_Type(Integer32):
    """Custom type fsDiscTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(515, 1199),
    )


_FsDiscTrapNum_Type.__name__ = "Integer32"
_FsDiscTrapNum_Object = MibTableColumn
fsDiscTrapNum = _FsDiscTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 6),
    _FsDiscTrapNum_Type()
)
fsDiscTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscTrapNum.setStatus("current")
_FsDiscClass_Type = DisplayString
_FsDiscClass_Object = MibTableColumn
fsDiscClass = _FsDiscClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 7),
    _FsDiscClass_Type()
)
fsDiscClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscClass.setStatus("current")
_FsDiscNormalActions_Type = DisplayString
_FsDiscNormalActions_Object = MibTableColumn
fsDiscNormalActions = _FsDiscNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 8),
    _FsDiscNormalActions_Type()
)
fsDiscNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscNormalActions.setStatus("current")


class _FsDiscNormalTrapNum_Type(Integer32):
    """Custom type fsDiscNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(515, 1199),
    )


_FsDiscNormalTrapNum_Type.__name__ = "Integer32"
_FsDiscNormalTrapNum_Object = MibTableColumn
fsDiscNormalTrapNum = _FsDiscNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 9),
    _FsDiscNormalTrapNum_Type()
)
fsDiscNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscNormalTrapNum.setStatus("current")
_FsDiscNormalClass_Type = DisplayString
_FsDiscNormalClass_Object = MibTableColumn
fsDiscNormalClass = _FsDiscNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 11, 5, 1, 10),
    _FsDiscNormalClass_Type()
)
fsDiscNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscNormalClass.setStatus("current")
_AcPowerMonitor_ObjectIdentity = ObjectIdentity
acPowerMonitor = _AcPowerMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12)
)
_AcpmGeneralTable_Object = MibTable
acpmGeneralTable = _AcpmGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1)
)
if mibBuilder.loadTexts:
    acpmGeneralTable.setStatus("current")
_AcpmGenEntry_Object = MibTableRow
acpmGenEntry = _AcpmGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1)
)
acpmGenEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmGenIndex"),
)
if mibBuilder.loadTexts:
    acpmGenEntry.setStatus("current")


class _AcpmGenIndex_Type(Integer32):
    """Custom type acpmGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmGenIndex_Type.__name__ = "Integer32"
_AcpmGenIndex_Object = MibTableColumn
acpmGenIndex = _AcpmGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 1),
    _AcpmGenIndex_Type()
)
acpmGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmGenIndex.setStatus("current")
_AcpmGenDevice_Type = DisplayString
_AcpmGenDevice_Object = MibTableColumn
acpmGenDevice = _AcpmGenDevice_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 2),
    _AcpmGenDevice_Type()
)
acpmGenDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenDevice.setStatus("current")
_AcpmGenName_Type = DisplayString
_AcpmGenName_Object = MibTableColumn
acpmGenName = _AcpmGenName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 3),
    _AcpmGenName_Type()
)
acpmGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenName.setStatus("current")


class _AcpmGenAddress_Type(Integer32):
    """Custom type acpmGenAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 247),
    )


_AcpmGenAddress_Type.__name__ = "Integer32"
_AcpmGenAddress_Object = MibTableColumn
acpmGenAddress = _AcpmGenAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 4),
    _AcpmGenAddress_Type()
)
acpmGenAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenAddress.setStatus("current")


class _AcpmGenPtRatio_Type(Integer32):
    """Custom type acpmGenPtRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AcpmGenPtRatio_Type.__name__ = "Integer32"
_AcpmGenPtRatio_Object = MibTableColumn
acpmGenPtRatio = _AcpmGenPtRatio_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 5),
    _AcpmGenPtRatio_Type()
)
acpmGenPtRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenPtRatio.setStatus("current")


class _AcpmGenCtRatio_Type(Integer32):
    """Custom type acpmGenCtRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AcpmGenCtRatio_Type.__name__ = "Integer32"
_AcpmGenCtRatio_Object = MibTableColumn
acpmGenCtRatio = _AcpmGenCtRatio_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 6),
    _AcpmGenCtRatio_Type()
)
acpmGenCtRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenCtRatio.setStatus("current")
_AcpmGenPowerType_Type = DisplayString
_AcpmGenPowerType_Object = MibTableColumn
acpmGenPowerType = _AcpmGenPowerType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 7),
    _AcpmGenPowerType_Type()
)
acpmGenPowerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenPowerType.setStatus("current")


class _AcpmGenSysrepPackage_Type(Integer32):
    """Custom type acpmGenSysrepPackage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AcpmGenSysrepPackage_Type.__name__ = "Integer32"
_AcpmGenSysrepPackage_Object = MibTableColumn
acpmGenSysrepPackage = _AcpmGenSysrepPackage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 8),
    _AcpmGenSysrepPackage_Type()
)
acpmGenSysrepPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenSysrepPackage.setStatus("current")
_AcpmGenSysrepType_Type = DisplayString
_AcpmGenSysrepType_Object = MibTableColumn
acpmGenSysrepType = _AcpmGenSysrepType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 9),
    _AcpmGenSysrepType_Type()
)
acpmGenSysrepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenSysrepType.setStatus("current")
_AcpmGenEnable_Type = DisplayString
_AcpmGenEnable_Object = MibTableColumn
acpmGenEnable = _AcpmGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 1, 1, 10),
    _AcpmGenEnable_Type()
)
acpmGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenEnable.setStatus("current")
_AcpmAvgVoltageTable_Object = MibTable
acpmAvgVoltageTable = _AcpmAvgVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2)
)
if mibBuilder.loadTexts:
    acpmAvgVoltageTable.setStatus("current")
_AcpmAvgVoltageEntry_Object = MibTableRow
acpmAvgVoltageEntry = _AcpmAvgVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1)
)
acpmAvgVoltageEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmAvgVoltageIndex"),
)
if mibBuilder.loadTexts:
    acpmAvgVoltageEntry.setStatus("current")


class _AcpmAvgVoltageIndex_Type(Integer32):
    """Custom type acpmAvgVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmAvgVoltageIndex_Type.__name__ = "Integer32"
_AcpmAvgVoltageIndex_Object = MibTableColumn
acpmAvgVoltageIndex = _AcpmAvgVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 1),
    _AcpmAvgVoltageIndex_Type()
)
acpmAvgVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmAvgVoltageIndex.setStatus("current")
_AcpmAvgVoltageEnable_Type = DisplayString
_AcpmAvgVoltageEnable_Object = MibTableColumn
acpmAvgVoltageEnable = _AcpmAvgVoltageEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 2),
    _AcpmAvgVoltageEnable_Type()
)
acpmAvgVoltageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageEnable.setStatus("current")
_AcpmAvgVoltageDeadband_Type = DisplayString
_AcpmAvgVoltageDeadband_Object = MibTableColumn
acpmAvgVoltageDeadband = _AcpmAvgVoltageDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 3),
    _AcpmAvgVoltageDeadband_Type()
)
acpmAvgVoltageDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageDeadband.setStatus("current")
_AcpmAvgVoltageVHighValue_Type = DisplayString
_AcpmAvgVoltageVHighValue_Object = MibTableColumn
acpmAvgVoltageVHighValue = _AcpmAvgVoltageVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 4),
    _AcpmAvgVoltageVHighValue_Type()
)
acpmAvgVoltageVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighValue.setStatus("current")
_AcpmAvgVoltageVHighActions_Type = DisplayString
_AcpmAvgVoltageVHighActions_Object = MibTableColumn
acpmAvgVoltageVHighActions = _AcpmAvgVoltageVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 5),
    _AcpmAvgVoltageVHighActions_Type()
)
acpmAvgVoltageVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighActions.setStatus("current")


class _AcpmAvgVoltageVHighTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageVHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageVHighTrapNum_Object = MibTableColumn
acpmAvgVoltageVHighTrapNum = _AcpmAvgVoltageVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 6),
    _AcpmAvgVoltageVHighTrapNum_Type()
)
acpmAvgVoltageVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighTrapNum.setStatus("current")
_AcpmAvgVoltageVHighClass_Type = DisplayString
_AcpmAvgVoltageVHighClass_Object = MibTableColumn
acpmAvgVoltageVHighClass = _AcpmAvgVoltageVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 7),
    _AcpmAvgVoltageVHighClass_Type()
)
acpmAvgVoltageVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighClass.setStatus("current")
_AcpmAvgVoltageHighValue_Type = DisplayString
_AcpmAvgVoltageHighValue_Object = MibTableColumn
acpmAvgVoltageHighValue = _AcpmAvgVoltageHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 8),
    _AcpmAvgVoltageHighValue_Type()
)
acpmAvgVoltageHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighValue.setStatus("current")
_AcpmAvgVoltageHighActions_Type = DisplayString
_AcpmAvgVoltageHighActions_Object = MibTableColumn
acpmAvgVoltageHighActions = _AcpmAvgVoltageHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 9),
    _AcpmAvgVoltageHighActions_Type()
)
acpmAvgVoltageHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighActions.setStatus("current")


class _AcpmAvgVoltageHighTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageHighTrapNum_Object = MibTableColumn
acpmAvgVoltageHighTrapNum = _AcpmAvgVoltageHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 10),
    _AcpmAvgVoltageHighTrapNum_Type()
)
acpmAvgVoltageHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighTrapNum.setStatus("current")
_AcpmAvgVoltageHighClass_Type = DisplayString
_AcpmAvgVoltageHighClass_Object = MibTableColumn
acpmAvgVoltageHighClass = _AcpmAvgVoltageHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 11),
    _AcpmAvgVoltageHighClass_Type()
)
acpmAvgVoltageHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighClass.setStatus("current")
_AcpmAvgVoltageNormalActions_Type = DisplayString
_AcpmAvgVoltageNormalActions_Object = MibTableColumn
acpmAvgVoltageNormalActions = _AcpmAvgVoltageNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 12),
    _AcpmAvgVoltageNormalActions_Type()
)
acpmAvgVoltageNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageNormalActions.setStatus("current")


class _AcpmAvgVoltageNormalTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageNormalTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageNormalTrapNum_Object = MibTableColumn
acpmAvgVoltageNormalTrapNum = _AcpmAvgVoltageNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 13),
    _AcpmAvgVoltageNormalTrapNum_Type()
)
acpmAvgVoltageNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageNormalTrapNum.setStatus("current")
_AcpmAvgVoltageNormalClass_Type = DisplayString
_AcpmAvgVoltageNormalClass_Object = MibTableColumn
acpmAvgVoltageNormalClass = _AcpmAvgVoltageNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 14),
    _AcpmAvgVoltageNormalClass_Type()
)
acpmAvgVoltageNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageNormalClass.setStatus("current")
_AcpmAvgVoltageLowValue_Type = DisplayString
_AcpmAvgVoltageLowValue_Object = MibTableColumn
acpmAvgVoltageLowValue = _AcpmAvgVoltageLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 15),
    _AcpmAvgVoltageLowValue_Type()
)
acpmAvgVoltageLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowValue.setStatus("current")
_AcpmAvgVoltageLowActions_Type = DisplayString
_AcpmAvgVoltageLowActions_Object = MibTableColumn
acpmAvgVoltageLowActions = _AcpmAvgVoltageLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 16),
    _AcpmAvgVoltageLowActions_Type()
)
acpmAvgVoltageLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowActions.setStatus("current")


class _AcpmAvgVoltageLowTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageLowTrapNum_Object = MibTableColumn
acpmAvgVoltageLowTrapNum = _AcpmAvgVoltageLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 17),
    _AcpmAvgVoltageLowTrapNum_Type()
)
acpmAvgVoltageLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowTrapNum.setStatus("current")
_AcpmAvgVoltageLowClass_Type = DisplayString
_AcpmAvgVoltageLowClass_Object = MibTableColumn
acpmAvgVoltageLowClass = _AcpmAvgVoltageLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 18),
    _AcpmAvgVoltageLowClass_Type()
)
acpmAvgVoltageLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowClass.setStatus("current")
_AcpmAvgVoltageVLowValue_Type = DisplayString
_AcpmAvgVoltageVLowValue_Object = MibTableColumn
acpmAvgVoltageVLowValue = _AcpmAvgVoltageVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 19),
    _AcpmAvgVoltageVLowValue_Type()
)
acpmAvgVoltageVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowValue.setStatus("current")
_AcpmAvgVoltageVLowActions_Type = DisplayString
_AcpmAvgVoltageVLowActions_Object = MibTableColumn
acpmAvgVoltageVLowActions = _AcpmAvgVoltageVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 20),
    _AcpmAvgVoltageVLowActions_Type()
)
acpmAvgVoltageVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowActions.setStatus("current")


class _AcpmAvgVoltageVLowTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageVLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageVLowTrapNum_Object = MibTableColumn
acpmAvgVoltageVLowTrapNum = _AcpmAvgVoltageVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 21),
    _AcpmAvgVoltageVLowTrapNum_Type()
)
acpmAvgVoltageVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowTrapNum.setStatus("current")
_AcpmAvgVoltageVLowClass_Type = DisplayString
_AcpmAvgVoltageVLowClass_Object = MibTableColumn
acpmAvgVoltageVLowClass = _AcpmAvgVoltageVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 22),
    _AcpmAvgVoltageVLowClass_Type()
)
acpmAvgVoltageVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowClass.setStatus("current")
_AcpmAvgVoltageSysrepEnable_Type = DisplayString
_AcpmAvgVoltageSysrepEnable_Object = MibTableColumn
acpmAvgVoltageSysrepEnable = _AcpmAvgVoltageSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 23),
    _AcpmAvgVoltageSysrepEnable_Type()
)
acpmAvgVoltageSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageSysrepEnable.setStatus("current")
_AcpmAvgVoltageSysrepThreshold_Type = DisplayString
_AcpmAvgVoltageSysrepThreshold_Object = MibTableColumn
acpmAvgVoltageSysrepThreshold = _AcpmAvgVoltageSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 24),
    _AcpmAvgVoltageSysrepThreshold_Type()
)
acpmAvgVoltageSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageSysrepThreshold.setStatus("current")
_AcpmAvgVoltageSysrepLimit_Type = Integer32
_AcpmAvgVoltageSysrepLimit_Object = MibTableColumn
acpmAvgVoltageSysrepLimit = _AcpmAvgVoltageSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 2, 1, 25),
    _AcpmAvgVoltageSysrepLimit_Type()
)
acpmAvgVoltageSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageSysrepLimit.setStatus("current")
_AcpmAvgCurrentTable_Object = MibTable
acpmAvgCurrentTable = _AcpmAvgCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3)
)
if mibBuilder.loadTexts:
    acpmAvgCurrentTable.setStatus("current")
_AcpmAvgCurrentEntry_Object = MibTableRow
acpmAvgCurrentEntry = _AcpmAvgCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1)
)
acpmAvgCurrentEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmAvgCurrentIndex"),
)
if mibBuilder.loadTexts:
    acpmAvgCurrentEntry.setStatus("current")


class _AcpmAvgCurrentIndex_Type(Integer32):
    """Custom type acpmAvgCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmAvgCurrentIndex_Type.__name__ = "Integer32"
_AcpmAvgCurrentIndex_Object = MibTableColumn
acpmAvgCurrentIndex = _AcpmAvgCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 1),
    _AcpmAvgCurrentIndex_Type()
)
acpmAvgCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmAvgCurrentIndex.setStatus("current")
_AcpmAvgCurrentEnable_Type = DisplayString
_AcpmAvgCurrentEnable_Object = MibTableColumn
acpmAvgCurrentEnable = _AcpmAvgCurrentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 2),
    _AcpmAvgCurrentEnable_Type()
)
acpmAvgCurrentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentEnable.setStatus("current")
_AcpmAvgCurrentDeadband_Type = DisplayString
_AcpmAvgCurrentDeadband_Object = MibTableColumn
acpmAvgCurrentDeadband = _AcpmAvgCurrentDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 3),
    _AcpmAvgCurrentDeadband_Type()
)
acpmAvgCurrentDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentDeadband.setStatus("current")
_AcpmAvgCurrentVHighValue_Type = DisplayString
_AcpmAvgCurrentVHighValue_Object = MibTableColumn
acpmAvgCurrentVHighValue = _AcpmAvgCurrentVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 4),
    _AcpmAvgCurrentVHighValue_Type()
)
acpmAvgCurrentVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighValue.setStatus("current")
_AcpmAvgCurrentVHighActions_Type = DisplayString
_AcpmAvgCurrentVHighActions_Object = MibTableColumn
acpmAvgCurrentVHighActions = _AcpmAvgCurrentVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 5),
    _AcpmAvgCurrentVHighActions_Type()
)
acpmAvgCurrentVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighActions.setStatus("current")


class _AcpmAvgCurrentVHighTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentVHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentVHighTrapNum_Object = MibTableColumn
acpmAvgCurrentVHighTrapNum = _AcpmAvgCurrentVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 6),
    _AcpmAvgCurrentVHighTrapNum_Type()
)
acpmAvgCurrentVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighTrapNum.setStatus("current")
_AcpmAvgCurrentVHighClass_Type = DisplayString
_AcpmAvgCurrentVHighClass_Object = MibTableColumn
acpmAvgCurrentVHighClass = _AcpmAvgCurrentVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 7),
    _AcpmAvgCurrentVHighClass_Type()
)
acpmAvgCurrentVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighClass.setStatus("current")
_AcpmAvgCurrentHighValue_Type = DisplayString
_AcpmAvgCurrentHighValue_Object = MibTableColumn
acpmAvgCurrentHighValue = _AcpmAvgCurrentHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 8),
    _AcpmAvgCurrentHighValue_Type()
)
acpmAvgCurrentHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighValue.setStatus("current")
_AcpmAvgCurrentHighActions_Type = DisplayString
_AcpmAvgCurrentHighActions_Object = MibTableColumn
acpmAvgCurrentHighActions = _AcpmAvgCurrentHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 9),
    _AcpmAvgCurrentHighActions_Type()
)
acpmAvgCurrentHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighActions.setStatus("current")


class _AcpmAvgCurrentHighTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentHighTrapNum_Object = MibTableColumn
acpmAvgCurrentHighTrapNum = _AcpmAvgCurrentHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 10),
    _AcpmAvgCurrentHighTrapNum_Type()
)
acpmAvgCurrentHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighTrapNum.setStatus("current")
_AcpmAvgCurrentHighClass_Type = DisplayString
_AcpmAvgCurrentHighClass_Object = MibTableColumn
acpmAvgCurrentHighClass = _AcpmAvgCurrentHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 11),
    _AcpmAvgCurrentHighClass_Type()
)
acpmAvgCurrentHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighClass.setStatus("current")
_AcpmAvgCurrentNormalActions_Type = DisplayString
_AcpmAvgCurrentNormalActions_Object = MibTableColumn
acpmAvgCurrentNormalActions = _AcpmAvgCurrentNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 12),
    _AcpmAvgCurrentNormalActions_Type()
)
acpmAvgCurrentNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentNormalActions.setStatus("current")


class _AcpmAvgCurrentNormalTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentNormalTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentNormalTrapNum_Object = MibTableColumn
acpmAvgCurrentNormalTrapNum = _AcpmAvgCurrentNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 13),
    _AcpmAvgCurrentNormalTrapNum_Type()
)
acpmAvgCurrentNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentNormalTrapNum.setStatus("current")
_AcpmAvgCurrentNormalClass_Type = DisplayString
_AcpmAvgCurrentNormalClass_Object = MibTableColumn
acpmAvgCurrentNormalClass = _AcpmAvgCurrentNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 14),
    _AcpmAvgCurrentNormalClass_Type()
)
acpmAvgCurrentNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentNormalClass.setStatus("current")
_AcpmAvgCurrentLowValue_Type = DisplayString
_AcpmAvgCurrentLowValue_Object = MibTableColumn
acpmAvgCurrentLowValue = _AcpmAvgCurrentLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 15),
    _AcpmAvgCurrentLowValue_Type()
)
acpmAvgCurrentLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowValue.setStatus("current")
_AcpmAvgCurrentLowActions_Type = DisplayString
_AcpmAvgCurrentLowActions_Object = MibTableColumn
acpmAvgCurrentLowActions = _AcpmAvgCurrentLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 16),
    _AcpmAvgCurrentLowActions_Type()
)
acpmAvgCurrentLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowActions.setStatus("current")


class _AcpmAvgCurrentLowTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentLowTrapNum_Object = MibTableColumn
acpmAvgCurrentLowTrapNum = _AcpmAvgCurrentLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 17),
    _AcpmAvgCurrentLowTrapNum_Type()
)
acpmAvgCurrentLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowTrapNum.setStatus("current")
_AcpmAvgCurrentLowClass_Type = DisplayString
_AcpmAvgCurrentLowClass_Object = MibTableColumn
acpmAvgCurrentLowClass = _AcpmAvgCurrentLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 18),
    _AcpmAvgCurrentLowClass_Type()
)
acpmAvgCurrentLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowClass.setStatus("current")
_AcpmAvgCurrentVLowValue_Type = DisplayString
_AcpmAvgCurrentVLowValue_Object = MibTableColumn
acpmAvgCurrentVLowValue = _AcpmAvgCurrentVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 19),
    _AcpmAvgCurrentVLowValue_Type()
)
acpmAvgCurrentVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowValue.setStatus("current")
_AcpmAvgCurrentVLowActions_Type = DisplayString
_AcpmAvgCurrentVLowActions_Object = MibTableColumn
acpmAvgCurrentVLowActions = _AcpmAvgCurrentVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 20),
    _AcpmAvgCurrentVLowActions_Type()
)
acpmAvgCurrentVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowActions.setStatus("current")


class _AcpmAvgCurrentVLowTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentVLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentVLowTrapNum_Object = MibTableColumn
acpmAvgCurrentVLowTrapNum = _AcpmAvgCurrentVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 21),
    _AcpmAvgCurrentVLowTrapNum_Type()
)
acpmAvgCurrentVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowTrapNum.setStatus("current")
_AcpmAvgCurrentVLowClass_Type = DisplayString
_AcpmAvgCurrentVLowClass_Object = MibTableColumn
acpmAvgCurrentVLowClass = _AcpmAvgCurrentVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 22),
    _AcpmAvgCurrentVLowClass_Type()
)
acpmAvgCurrentVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowClass.setStatus("current")
_AcpmAvgCurrentSysrepEnable_Type = DisplayString
_AcpmAvgCurrentSysrepEnable_Object = MibTableColumn
acpmAvgCurrentSysrepEnable = _AcpmAvgCurrentSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 23),
    _AcpmAvgCurrentSysrepEnable_Type()
)
acpmAvgCurrentSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentSysrepEnable.setStatus("current")
_AcpmAvgCurrentSysrepThreshold_Type = DisplayString
_AcpmAvgCurrentSysrepThreshold_Object = MibTableColumn
acpmAvgCurrentSysrepThreshold = _AcpmAvgCurrentSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 24),
    _AcpmAvgCurrentSysrepThreshold_Type()
)
acpmAvgCurrentSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentSysrepThreshold.setStatus("current")
_AcpmAvgCurrentSysrepLimit_Type = Integer32
_AcpmAvgCurrentSysrepLimit_Object = MibTableColumn
acpmAvgCurrentSysrepLimit = _AcpmAvgCurrentSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 3, 1, 25),
    _AcpmAvgCurrentSysrepLimit_Type()
)
acpmAvgCurrentSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentSysrepLimit.setStatus("current")
_AcpmFreqTable_Object = MibTable
acpmFreqTable = _AcpmFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4)
)
if mibBuilder.loadTexts:
    acpmFreqTable.setStatus("current")
_AcpmFreqEntry_Object = MibTableRow
acpmFreqEntry = _AcpmFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1)
)
acpmFreqEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmFreqIndex"),
)
if mibBuilder.loadTexts:
    acpmFreqEntry.setStatus("current")


class _AcpmFreqIndex_Type(Integer32):
    """Custom type acpmFreqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmFreqIndex_Type.__name__ = "Integer32"
_AcpmFreqIndex_Object = MibTableColumn
acpmFreqIndex = _AcpmFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 1),
    _AcpmFreqIndex_Type()
)
acpmFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmFreqIndex.setStatus("current")
_AcpmFreqEnable_Type = DisplayString
_AcpmFreqEnable_Object = MibTableColumn
acpmFreqEnable = _AcpmFreqEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 2),
    _AcpmFreqEnable_Type()
)
acpmFreqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqEnable.setStatus("current")
_AcpmFreqDeadband_Type = DisplayString
_AcpmFreqDeadband_Object = MibTableColumn
acpmFreqDeadband = _AcpmFreqDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 3),
    _AcpmFreqDeadband_Type()
)
acpmFreqDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqDeadband.setStatus("current")
_AcpmFreqVHighValue_Type = DisplayString
_AcpmFreqVHighValue_Object = MibTableColumn
acpmFreqVHighValue = _AcpmFreqVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 4),
    _AcpmFreqVHighValue_Type()
)
acpmFreqVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighValue.setStatus("current")
_AcpmFreqVHighActions_Type = DisplayString
_AcpmFreqVHighActions_Object = MibTableColumn
acpmFreqVHighActions = _AcpmFreqVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 5),
    _AcpmFreqVHighActions_Type()
)
acpmFreqVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighActions.setStatus("current")


class _AcpmFreqVHighTrapNum_Type(Integer32):
    """Custom type acpmFreqVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqVHighTrapNum_Type.__name__ = "Integer32"
_AcpmFreqVHighTrapNum_Object = MibTableColumn
acpmFreqVHighTrapNum = _AcpmFreqVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 6),
    _AcpmFreqVHighTrapNum_Type()
)
acpmFreqVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighTrapNum.setStatus("current")
_AcpmFreqVHighClass_Type = DisplayString
_AcpmFreqVHighClass_Object = MibTableColumn
acpmFreqVHighClass = _AcpmFreqVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 7),
    _AcpmFreqVHighClass_Type()
)
acpmFreqVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighClass.setStatus("current")
_AcpmFreqHighValue_Type = DisplayString
_AcpmFreqHighValue_Object = MibTableColumn
acpmFreqHighValue = _AcpmFreqHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 8),
    _AcpmFreqHighValue_Type()
)
acpmFreqHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighValue.setStatus("current")
_AcpmFreqHighActions_Type = DisplayString
_AcpmFreqHighActions_Object = MibTableColumn
acpmFreqHighActions = _AcpmFreqHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 9),
    _AcpmFreqHighActions_Type()
)
acpmFreqHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighActions.setStatus("current")


class _AcpmFreqHighTrapNum_Type(Integer32):
    """Custom type acpmFreqHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqHighTrapNum_Type.__name__ = "Integer32"
_AcpmFreqHighTrapNum_Object = MibTableColumn
acpmFreqHighTrapNum = _AcpmFreqHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 10),
    _AcpmFreqHighTrapNum_Type()
)
acpmFreqHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighTrapNum.setStatus("current")
_AcpmFreqHighClass_Type = DisplayString
_AcpmFreqHighClass_Object = MibTableColumn
acpmFreqHighClass = _AcpmFreqHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 11),
    _AcpmFreqHighClass_Type()
)
acpmFreqHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighClass.setStatus("current")
_AcpmFreqNormalActions_Type = DisplayString
_AcpmFreqNormalActions_Object = MibTableColumn
acpmFreqNormalActions = _AcpmFreqNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 12),
    _AcpmFreqNormalActions_Type()
)
acpmFreqNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqNormalActions.setStatus("current")


class _AcpmFreqNormalTrapNum_Type(Integer32):
    """Custom type acpmFreqNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqNormalTrapNum_Type.__name__ = "Integer32"
_AcpmFreqNormalTrapNum_Object = MibTableColumn
acpmFreqNormalTrapNum = _AcpmFreqNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 13),
    _AcpmFreqNormalTrapNum_Type()
)
acpmFreqNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqNormalTrapNum.setStatus("current")
_AcpmFreqNormalClass_Type = DisplayString
_AcpmFreqNormalClass_Object = MibTableColumn
acpmFreqNormalClass = _AcpmFreqNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 14),
    _AcpmFreqNormalClass_Type()
)
acpmFreqNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqNormalClass.setStatus("current")
_AcpmFreqLowValue_Type = DisplayString
_AcpmFreqLowValue_Object = MibTableColumn
acpmFreqLowValue = _AcpmFreqLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 15),
    _AcpmFreqLowValue_Type()
)
acpmFreqLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowValue.setStatus("current")
_AcpmFreqLowActions_Type = DisplayString
_AcpmFreqLowActions_Object = MibTableColumn
acpmFreqLowActions = _AcpmFreqLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 16),
    _AcpmFreqLowActions_Type()
)
acpmFreqLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowActions.setStatus("current")


class _AcpmFreqLowTrapNum_Type(Integer32):
    """Custom type acpmFreqLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqLowTrapNum_Type.__name__ = "Integer32"
_AcpmFreqLowTrapNum_Object = MibTableColumn
acpmFreqLowTrapNum = _AcpmFreqLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 17),
    _AcpmFreqLowTrapNum_Type()
)
acpmFreqLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowTrapNum.setStatus("current")
_AcpmFreqLowClass_Type = DisplayString
_AcpmFreqLowClass_Object = MibTableColumn
acpmFreqLowClass = _AcpmFreqLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 18),
    _AcpmFreqLowClass_Type()
)
acpmFreqLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowClass.setStatus("current")
_AcpmFreqVLowValue_Type = DisplayString
_AcpmFreqVLowValue_Object = MibTableColumn
acpmFreqVLowValue = _AcpmFreqVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 19),
    _AcpmFreqVLowValue_Type()
)
acpmFreqVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowValue.setStatus("current")
_AcpmFreqVLowActions_Type = DisplayString
_AcpmFreqVLowActions_Object = MibTableColumn
acpmFreqVLowActions = _AcpmFreqVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 20),
    _AcpmFreqVLowActions_Type()
)
acpmFreqVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowActions.setStatus("current")


class _AcpmFreqVLowTrapNum_Type(Integer32):
    """Custom type acpmFreqVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqVLowTrapNum_Type.__name__ = "Integer32"
_AcpmFreqVLowTrapNum_Object = MibTableColumn
acpmFreqVLowTrapNum = _AcpmFreqVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 21),
    _AcpmFreqVLowTrapNum_Type()
)
acpmFreqVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowTrapNum.setStatus("current")
_AcpmFreqVLowClass_Type = DisplayString
_AcpmFreqVLowClass_Object = MibTableColumn
acpmFreqVLowClass = _AcpmFreqVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 22),
    _AcpmFreqVLowClass_Type()
)
acpmFreqVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowClass.setStatus("current")
_AcpmFreqSysrepEnable_Type = DisplayString
_AcpmFreqSysrepEnable_Object = MibTableColumn
acpmFreqSysrepEnable = _AcpmFreqSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 23),
    _AcpmFreqSysrepEnable_Type()
)
acpmFreqSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqSysrepEnable.setStatus("current")
_AcpmFreqSysrepThreshold_Type = DisplayString
_AcpmFreqSysrepThreshold_Object = MibTableColumn
acpmFreqSysrepThreshold = _AcpmFreqSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 24),
    _AcpmFreqSysrepThreshold_Type()
)
acpmFreqSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqSysrepThreshold.setStatus("current")
_AcpmFreqSysrepLimit_Type = Integer32
_AcpmFreqSysrepLimit_Object = MibTableColumn
acpmFreqSysrepLimit = _AcpmFreqSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 4, 1, 25),
    _AcpmFreqSysrepLimit_Type()
)
acpmFreqSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqSysrepLimit.setStatus("current")
_AcpmTotalRealPowerTable_Object = MibTable
acpmTotalRealPowerTable = _AcpmTotalRealPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5)
)
if mibBuilder.loadTexts:
    acpmTotalRealPowerTable.setStatus("current")
_AcpmTRPEntry_Object = MibTableRow
acpmTRPEntry = _AcpmTRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1)
)
acpmTRPEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmTRPIndex"),
)
if mibBuilder.loadTexts:
    acpmTRPEntry.setStatus("current")


class _AcpmTRPIndex_Type(Integer32):
    """Custom type acpmTRPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmTRPIndex_Type.__name__ = "Integer32"
_AcpmTRPIndex_Object = MibTableColumn
acpmTRPIndex = _AcpmTRPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 1),
    _AcpmTRPIndex_Type()
)
acpmTRPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmTRPIndex.setStatus("current")
_AcpmTRPEnable_Type = DisplayString
_AcpmTRPEnable_Object = MibTableColumn
acpmTRPEnable = _AcpmTRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 2),
    _AcpmTRPEnable_Type()
)
acpmTRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPEnable.setStatus("current")
_AcpmTRPDeadband_Type = DisplayString
_AcpmTRPDeadband_Object = MibTableColumn
acpmTRPDeadband = _AcpmTRPDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 3),
    _AcpmTRPDeadband_Type()
)
acpmTRPDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPDeadband.setStatus("current")
_AcpmTRPVHighValue_Type = DisplayString
_AcpmTRPVHighValue_Object = MibTableColumn
acpmTRPVHighValue = _AcpmTRPVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 4),
    _AcpmTRPVHighValue_Type()
)
acpmTRPVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighValue.setStatus("current")
_AcpmTRPVHighActions_Type = DisplayString
_AcpmTRPVHighActions_Object = MibTableColumn
acpmTRPVHighActions = _AcpmTRPVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 5),
    _AcpmTRPVHighActions_Type()
)
acpmTRPVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighActions.setStatus("current")


class _AcpmTRPVHighTrapNum_Type(Integer32):
    """Custom type acpmTRPVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPVHighTrapNum_Type.__name__ = "Integer32"
_AcpmTRPVHighTrapNum_Object = MibTableColumn
acpmTRPVHighTrapNum = _AcpmTRPVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 6),
    _AcpmTRPVHighTrapNum_Type()
)
acpmTRPVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighTrapNum.setStatus("current")
_AcpmTRPVHighClass_Type = DisplayString
_AcpmTRPVHighClass_Object = MibTableColumn
acpmTRPVHighClass = _AcpmTRPVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 7),
    _AcpmTRPVHighClass_Type()
)
acpmTRPVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighClass.setStatus("current")
_AcpmTRPHighValue_Type = DisplayString
_AcpmTRPHighValue_Object = MibTableColumn
acpmTRPHighValue = _AcpmTRPHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 8),
    _AcpmTRPHighValue_Type()
)
acpmTRPHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighValue.setStatus("current")
_AcpmTRPHighActions_Type = DisplayString
_AcpmTRPHighActions_Object = MibTableColumn
acpmTRPHighActions = _AcpmTRPHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 9),
    _AcpmTRPHighActions_Type()
)
acpmTRPHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighActions.setStatus("current")


class _AcpmTRPHighTrapNum_Type(Integer32):
    """Custom type acpmTRPHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPHighTrapNum_Type.__name__ = "Integer32"
_AcpmTRPHighTrapNum_Object = MibTableColumn
acpmTRPHighTrapNum = _AcpmTRPHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 10),
    _AcpmTRPHighTrapNum_Type()
)
acpmTRPHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighTrapNum.setStatus("current")
_AcpmTRPHighClass_Type = DisplayString
_AcpmTRPHighClass_Object = MibTableColumn
acpmTRPHighClass = _AcpmTRPHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 11),
    _AcpmTRPHighClass_Type()
)
acpmTRPHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighClass.setStatus("current")
_AcpmTRPNormalActions_Type = DisplayString
_AcpmTRPNormalActions_Object = MibTableColumn
acpmTRPNormalActions = _AcpmTRPNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 12),
    _AcpmTRPNormalActions_Type()
)
acpmTRPNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPNormalActions.setStatus("current")


class _AcpmTRPNormalTrapNum_Type(Integer32):
    """Custom type acpmTRPNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPNormalTrapNum_Type.__name__ = "Integer32"
_AcpmTRPNormalTrapNum_Object = MibTableColumn
acpmTRPNormalTrapNum = _AcpmTRPNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 13),
    _AcpmTRPNormalTrapNum_Type()
)
acpmTRPNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPNormalTrapNum.setStatus("current")
_AcpmTRPNormalClass_Type = DisplayString
_AcpmTRPNormalClass_Object = MibTableColumn
acpmTRPNormalClass = _AcpmTRPNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 14),
    _AcpmTRPNormalClass_Type()
)
acpmTRPNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPNormalClass.setStatus("current")
_AcpmTRPLowValue_Type = DisplayString
_AcpmTRPLowValue_Object = MibTableColumn
acpmTRPLowValue = _AcpmTRPLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 15),
    _AcpmTRPLowValue_Type()
)
acpmTRPLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowValue.setStatus("current")
_AcpmTRPLowActions_Type = DisplayString
_AcpmTRPLowActions_Object = MibTableColumn
acpmTRPLowActions = _AcpmTRPLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 16),
    _AcpmTRPLowActions_Type()
)
acpmTRPLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowActions.setStatus("current")


class _AcpmTRPLowTrapNum_Type(Integer32):
    """Custom type acpmTRPLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPLowTrapNum_Type.__name__ = "Integer32"
_AcpmTRPLowTrapNum_Object = MibTableColumn
acpmTRPLowTrapNum = _AcpmTRPLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 17),
    _AcpmTRPLowTrapNum_Type()
)
acpmTRPLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowTrapNum.setStatus("current")
_AcpmTRPLowClass_Type = DisplayString
_AcpmTRPLowClass_Object = MibTableColumn
acpmTRPLowClass = _AcpmTRPLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 18),
    _AcpmTRPLowClass_Type()
)
acpmTRPLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowClass.setStatus("current")
_AcpmTRPVLowValue_Type = DisplayString
_AcpmTRPVLowValue_Object = MibTableColumn
acpmTRPVLowValue = _AcpmTRPVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 19),
    _AcpmTRPVLowValue_Type()
)
acpmTRPVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowValue.setStatus("current")
_AcpmTRPVLowActions_Type = DisplayString
_AcpmTRPVLowActions_Object = MibTableColumn
acpmTRPVLowActions = _AcpmTRPVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 20),
    _AcpmTRPVLowActions_Type()
)
acpmTRPVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowActions.setStatus("current")


class _AcpmTRPVLowTrapNum_Type(Integer32):
    """Custom type acpmTRPVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPVLowTrapNum_Type.__name__ = "Integer32"
_AcpmTRPVLowTrapNum_Object = MibTableColumn
acpmTRPVLowTrapNum = _AcpmTRPVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 21),
    _AcpmTRPVLowTrapNum_Type()
)
acpmTRPVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowTrapNum.setStatus("current")
_AcpmTRPVLowClass_Type = DisplayString
_AcpmTRPVLowClass_Object = MibTableColumn
acpmTRPVLowClass = _AcpmTRPVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 22),
    _AcpmTRPVLowClass_Type()
)
acpmTRPVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowClass.setStatus("current")
_AcpmTRPSysrepEnable_Type = DisplayString
_AcpmTRPSysrepEnable_Object = MibTableColumn
acpmTRPSysrepEnable = _AcpmTRPSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 23),
    _AcpmTRPSysrepEnable_Type()
)
acpmTRPSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPSysrepEnable.setStatus("current")
_AcpmTRPSysrepThreshold_Type = DisplayString
_AcpmTRPSysrepThreshold_Object = MibTableColumn
acpmTRPSysrepThreshold = _AcpmTRPSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 24),
    _AcpmTRPSysrepThreshold_Type()
)
acpmTRPSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPSysrepThreshold.setStatus("current")
_AcpmTRPSysrepLimit_Type = Integer32
_AcpmTRPSysrepLimit_Object = MibTableColumn
acpmTRPSysrepLimit = _AcpmTRPSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 5, 1, 25),
    _AcpmTRPSysrepLimit_Type()
)
acpmTRPSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPSysrepLimit.setStatus("current")
_AcpmDisconnectTable_Object = MibTable
acpmDisconnectTable = _AcpmDisconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6)
)
if mibBuilder.loadTexts:
    acpmDisconnectTable.setStatus("current")
_AcpmDisconnectEntry_Object = MibTableRow
acpmDisconnectEntry = _AcpmDisconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1)
)
acpmDisconnectEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmDisconnectIndex"),
)
if mibBuilder.loadTexts:
    acpmDisconnectEntry.setStatus("current")


class _AcpmDisconnectIndex_Type(Integer32):
    """Custom type acpmDisconnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmDisconnectIndex_Type.__name__ = "Integer32"
_AcpmDisconnectIndex_Object = MibTableColumn
acpmDisconnectIndex = _AcpmDisconnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 1),
    _AcpmDisconnectIndex_Type()
)
acpmDisconnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmDisconnectIndex.setStatus("current")
_AcpmDisconnectEnable_Type = DisplayString
_AcpmDisconnectEnable_Object = MibTableColumn
acpmDisconnectEnable = _AcpmDisconnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 2),
    _AcpmDisconnectEnable_Type()
)
acpmDisconnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectEnable.setStatus("current")
_AcpmDisconnectActions_Type = DisplayString
_AcpmDisconnectActions_Object = MibTableColumn
acpmDisconnectActions = _AcpmDisconnectActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 3),
    _AcpmDisconnectActions_Type()
)
acpmDisconnectActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectActions.setStatus("current")


class _AcpmDisconnectTrapNum_Type(Integer32):
    """Custom type acpmDisconnectTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(524, 1199),
    )


_AcpmDisconnectTrapNum_Type.__name__ = "Integer32"
_AcpmDisconnectTrapNum_Object = MibTableColumn
acpmDisconnectTrapNum = _AcpmDisconnectTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 4),
    _AcpmDisconnectTrapNum_Type()
)
acpmDisconnectTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectTrapNum.setStatus("current")
_AcpmDisconnectClass_Type = DisplayString
_AcpmDisconnectClass_Object = MibTableColumn
acpmDisconnectClass = _AcpmDisconnectClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 5),
    _AcpmDisconnectClass_Type()
)
acpmDisconnectClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectClass.setStatus("current")
_AcpmDisconnectNormalActions_Type = DisplayString
_AcpmDisconnectNormalActions_Object = MibTableColumn
acpmDisconnectNormalActions = _AcpmDisconnectNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 6),
    _AcpmDisconnectNormalActions_Type()
)
acpmDisconnectNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectNormalActions.setStatus("current")


class _AcpmDisconnectNormalTrapNum_Type(Integer32):
    """Custom type acpmDisconnectNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(524, 1199),
    )


_AcpmDisconnectNormalTrapNum_Type.__name__ = "Integer32"
_AcpmDisconnectNormalTrapNum_Object = MibTableColumn
acpmDisconnectNormalTrapNum = _AcpmDisconnectNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 7),
    _AcpmDisconnectNormalTrapNum_Type()
)
acpmDisconnectNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectNormalTrapNum.setStatus("current")
_AcpmDisconnectNormalClass_Type = DisplayString
_AcpmDisconnectNormalClass_Object = MibTableColumn
acpmDisconnectNormalClass = _AcpmDisconnectNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 6, 1, 8),
    _AcpmDisconnectNormalClass_Type()
)
acpmDisconnectNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectNormalClass.setStatus("current")
_AcpmTotalPowerFactorTable_Object = MibTable
acpmTotalPowerFactorTable = _AcpmTotalPowerFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7)
)
if mibBuilder.loadTexts:
    acpmTotalPowerFactorTable.setStatus("current")
_AcpmTPFEntry_Object = MibTableRow
acpmTPFEntry = _AcpmTPFEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1)
)
acpmTPFEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "acpmTPFIndex"),
)
if mibBuilder.loadTexts:
    acpmTPFEntry.setStatus("current")


class _AcpmTPFIndex_Type(Integer32):
    """Custom type acpmTPFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmTPFIndex_Type.__name__ = "Integer32"
_AcpmTPFIndex_Object = MibTableColumn
acpmTPFIndex = _AcpmTPFIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 1),
    _AcpmTPFIndex_Type()
)
acpmTPFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmTPFIndex.setStatus("current")
_AcpmTPFEnable_Type = DisplayString
_AcpmTPFEnable_Object = MibTableColumn
acpmTPFEnable = _AcpmTPFEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 2),
    _AcpmTPFEnable_Type()
)
acpmTPFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFEnable.setStatus("current")
_AcpmTPFDeadband_Type = DisplayString
_AcpmTPFDeadband_Object = MibTableColumn
acpmTPFDeadband = _AcpmTPFDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 3),
    _AcpmTPFDeadband_Type()
)
acpmTPFDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFDeadband.setStatus("current")
_AcpmTPFNormalActions_Type = DisplayString
_AcpmTPFNormalActions_Object = MibTableColumn
acpmTPFNormalActions = _AcpmTPFNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 4),
    _AcpmTPFNormalActions_Type()
)
acpmTPFNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFNormalActions.setStatus("current")
_AcpmTPFNormalTrapNum_Type = Integer32
_AcpmTPFNormalTrapNum_Object = MibTableColumn
acpmTPFNormalTrapNum = _AcpmTPFNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 5),
    _AcpmTPFNormalTrapNum_Type()
)
acpmTPFNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFNormalTrapNum.setStatus("current")
_AcpmTPFNormalClass_Type = DisplayString
_AcpmTPFNormalClass_Object = MibTableColumn
acpmTPFNormalClass = _AcpmTPFNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 6),
    _AcpmTPFNormalClass_Type()
)
acpmTPFNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFNormalClass.setStatus("current")
_AcpmTPFLowValue_Type = DisplayString
_AcpmTPFLowValue_Object = MibTableColumn
acpmTPFLowValue = _AcpmTPFLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 7),
    _AcpmTPFLowValue_Type()
)
acpmTPFLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowValue.setStatus("current")
_AcpmTPFLowActions_Type = DisplayString
_AcpmTPFLowActions_Object = MibTableColumn
acpmTPFLowActions = _AcpmTPFLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 8),
    _AcpmTPFLowActions_Type()
)
acpmTPFLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowActions.setStatus("current")
_AcpmTPFLowTrapNum_Type = Integer32
_AcpmTPFLowTrapNum_Object = MibTableColumn
acpmTPFLowTrapNum = _AcpmTPFLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 9),
    _AcpmTPFLowTrapNum_Type()
)
acpmTPFLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowTrapNum.setStatus("current")
_AcpmTPFLowClass_Type = DisplayString
_AcpmTPFLowClass_Object = MibTableColumn
acpmTPFLowClass = _AcpmTPFLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 10),
    _AcpmTPFLowClass_Type()
)
acpmTPFLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowClass.setStatus("current")
_AcpmTPFVLowValue_Type = DisplayString
_AcpmTPFVLowValue_Object = MibTableColumn
acpmTPFVLowValue = _AcpmTPFVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 11),
    _AcpmTPFVLowValue_Type()
)
acpmTPFVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowValue.setStatus("current")
_AcpmTPFVLowActions_Type = DisplayString
_AcpmTPFVLowActions_Object = MibTableColumn
acpmTPFVLowActions = _AcpmTPFVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 12),
    _AcpmTPFVLowActions_Type()
)
acpmTPFVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowActions.setStatus("current")
_AcpmTPFVLowTrapNum_Type = Integer32
_AcpmTPFVLowTrapNum_Object = MibTableColumn
acpmTPFVLowTrapNum = _AcpmTPFVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 13),
    _AcpmTPFVLowTrapNum_Type()
)
acpmTPFVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowTrapNum.setStatus("current")
_AcpmTPFVLowClass_Type = DisplayString
_AcpmTPFVLowClass_Object = MibTableColumn
acpmTPFVLowClass = _AcpmTPFVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 14),
    _AcpmTPFVLowClass_Type()
)
acpmTPFVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowClass.setStatus("current")
_AcpmTPFSysrepEnable_Type = DisplayString
_AcpmTPFSysrepEnable_Object = MibTableColumn
acpmTPFSysrepEnable = _AcpmTPFSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 15),
    _AcpmTPFSysrepEnable_Type()
)
acpmTPFSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFSysrepEnable.setStatus("current")
_AcpmTPFSysrepThreshold_Type = DisplayString
_AcpmTPFSysrepThreshold_Object = MibTableColumn
acpmTPFSysrepThreshold = _AcpmTPFSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 16),
    _AcpmTPFSysrepThreshold_Type()
)
acpmTPFSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFSysrepThreshold.setStatus("current")
_AcpmTPFSysrepLimit_Type = Integer32
_AcpmTPFSysrepLimit_Object = MibTableColumn
acpmTPFSysrepLimit = _AcpmTPFSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 12, 7, 1, 17),
    _AcpmTPFSysrepLimit_Type()
)
acpmTPFSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFSysrepLimit.setStatus("current")
_EvReset_ObjectIdentity = ObjectIdentity
evReset = _EvReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16)
)
_EvResetEnable_Type = DisplayString
_EvResetEnable_Object = MibScalar
evResetEnable = _EvResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16, 1),
    _EvResetEnable_Type()
)
evResetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetEnable.setStatus("current")


class _EvResetDelay_Type(Integer32):
    """Custom type evResetDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_EvResetDelay_Type.__name__ = "Integer32"
_EvResetDelay_Object = MibScalar
evResetDelay = _EvResetDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16, 2),
    _EvResetDelay_Type()
)
evResetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetDelay.setStatus("current")
_EvResetActions_Type = DisplayString
_EvResetActions_Object = MibScalar
evResetActions = _EvResetActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16, 3),
    _EvResetActions_Type()
)
evResetActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetActions.setStatus("current")
_EvResetMessage_Type = DisplayString
_EvResetMessage_Object = MibScalar
evResetMessage = _EvResetMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16, 4),
    _EvResetMessage_Type()
)
evResetMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetMessage.setStatus("current")


class _EvResetTrapnum_Type(Integer32):
    """Custom type evResetTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(543, 1199),
    )


_EvResetTrapnum_Type.__name__ = "Integer32"
_EvResetTrapnum_Object = MibScalar
evResetTrapnum = _EvResetTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16, 5),
    _EvResetTrapnum_Type()
)
evResetTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetTrapnum.setStatus("current")
_EvResetClass_Type = DisplayString
_EvResetClass_Object = MibScalar
evResetClass = _EvResetClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 12, 16, 6),
    _EvResetClass_Type()
)
evResetClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetClass.setStatus("current")
_Action_ObjectIdentity = ObjectIdentity
action = _Action_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14)
)
_ActionCallNumberTable_Object = MibTable
actionCallNumberTable = _ActionCallNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 1)
)
if mibBuilder.loadTexts:
    actionCallNumberTable.setStatus("current")
_ActionCallNumberEntry_Object = MibTableRow
actionCallNumberEntry = _ActionCallNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 1, 1)
)
actionCallNumberEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "actionCallNumberIndex"),
)
if mibBuilder.loadTexts:
    actionCallNumberEntry.setStatus("current")


class _ActionCallNumberIndex_Type(Integer32):
    """Custom type actionCallNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ActionCallNumberIndex_Type.__name__ = "Integer32"
_ActionCallNumberIndex_Object = MibTableColumn
actionCallNumberIndex = _ActionCallNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 1, 1, 1),
    _ActionCallNumberIndex_Type()
)
actionCallNumberIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionCallNumberIndex.setStatus("current")
_ActionCallNumber_Type = DisplayString
_ActionCallNumber_Object = MibTableColumn
actionCallNumber = _ActionCallNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 1, 1, 2),
    _ActionCallNumber_Type()
)
actionCallNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionCallNumber.setStatus("current")
_ActionPagerTable_Object = MibTable
actionPagerTable = _ActionPagerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2)
)
if mibBuilder.loadTexts:
    actionPagerTable.setStatus("current")
_ActionPagerEntry_Object = MibTableRow
actionPagerEntry = _ActionPagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1)
)
actionPagerEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "actionPagerIndex"),
)
if mibBuilder.loadTexts:
    actionPagerEntry.setStatus("current")


class _ActionPagerIndex_Type(Integer32):
    """Custom type actionPagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ActionPagerIndex_Type.__name__ = "Integer32"
_ActionPagerIndex_Object = MibTableColumn
actionPagerIndex = _ActionPagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 1),
    _ActionPagerIndex_Type()
)
actionPagerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionPagerIndex.setStatus("current")
_ActionPagerType_Type = DisplayString
_ActionPagerType_Object = MibTableColumn
actionPagerType = _ActionPagerType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 2),
    _ActionPagerType_Type()
)
actionPagerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPagerType.setStatus("current")
_ActionPagerNumber_Type = DisplayString
_ActionPagerNumber_Object = MibTableColumn
actionPagerNumber = _ActionPagerNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 3),
    _ActionPagerNumber_Type()
)
actionPagerNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPagerNumber.setStatus("current")
_ActionPagerID_Type = DisplayString
_ActionPagerID_Object = MibTableColumn
actionPagerID = _ActionPagerID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 4),
    _ActionPagerID_Type()
)
actionPagerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPagerID.setStatus("current")
_ActionPagerMessage_Type = DisplayString
_ActionPagerMessage_Object = MibTableColumn
actionPagerMessage = _ActionPagerMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 5),
    _ActionPagerMessage_Type()
)
actionPagerMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPagerMessage.setStatus("current")


class _ActionPagerPostCalloutDelay_Type(Integer32):
    """Custom type actionPagerPostCalloutDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ActionPagerPostCalloutDelay_Type.__name__ = "Integer32"
_ActionPagerPostCalloutDelay_Object = MibTableColumn
actionPagerPostCalloutDelay = _ActionPagerPostCalloutDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 6),
    _ActionPagerPostCalloutDelay_Type()
)
actionPagerPostCalloutDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPagerPostCalloutDelay.setStatus("current")


class _ActionPagerPostIDDelay_Type(Integer32):
    """Custom type actionPagerPostIDDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ActionPagerPostIDDelay_Type.__name__ = "Integer32"
_ActionPagerPostIDDelay_Object = MibTableColumn
actionPagerPostIDDelay = _ActionPagerPostIDDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 2, 1, 7),
    _ActionPagerPostIDDelay_Type()
)
actionPagerPostIDDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPagerPostIDDelay.setStatus("current")
_ActionSched_ObjectIdentity = ObjectIdentity
actionSched = _ActionSched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 3)
)
_ActionSchedEnable_Type = DisplayString
_ActionSchedEnable_Object = MibScalar
actionSchedEnable = _ActionSchedEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 3, 1),
    _ActionSchedEnable_Type()
)
actionSchedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedEnable.setStatus("current")
_ActionSchedBegin_Type = DisplayString
_ActionSchedBegin_Object = MibScalar
actionSchedBegin = _ActionSchedBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 3, 2),
    _ActionSchedBegin_Type()
)
actionSchedBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedBegin.setStatus("current")
_ActionSchedEnd_Type = DisplayString
_ActionSchedEnd_Object = MibScalar
actionSchedEnd = _ActionSchedEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 3, 3),
    _ActionSchedEnd_Type()
)
actionSchedEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedEnd.setStatus("current")
_ActionSchedWeekdaysOnly_Type = DisplayString
_ActionSchedWeekdaysOnly_Object = MibScalar
actionSchedWeekdaysOnly = _ActionSchedWeekdaysOnly_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 3, 4),
    _ActionSchedWeekdaysOnly_Type()
)
actionSchedWeekdaysOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedWeekdaysOnly.setStatus("current")
_ActionAsentria_ObjectIdentity = ObjectIdentity
actionAsentria = _ActionAsentria_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 4)
)
_ActionAsentriaRequireAck_Type = DisplayString
_ActionAsentriaRequireAck_Object = MibScalar
actionAsentriaRequireAck = _ActionAsentriaRequireAck_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 4, 1),
    _ActionAsentriaRequireAck_Type()
)
actionAsentriaRequireAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAsentriaRequireAck.setStatus("current")
_ActionAsentriaVersion_Type = DisplayString
_ActionAsentriaVersion_Object = MibScalar
actionAsentriaVersion = _ActionAsentriaVersion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 4, 2),
    _ActionAsentriaVersion_Type()
)
actionAsentriaVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAsentriaVersion.setStatus("current")
_ActionAsentriaTCPPort_Type = Integer32
_ActionAsentriaTCPPort_Object = MibScalar
actionAsentriaTCPPort = _ActionAsentriaTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 4, 3),
    _ActionAsentriaTCPPort_Type()
)
actionAsentriaTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAsentriaTCPPort.setStatus("current")
_ActionHostTable_Object = MibTable
actionHostTable = _ActionHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 6)
)
if mibBuilder.loadTexts:
    actionHostTable.setStatus("current")
_ActionHostEntry_Object = MibTableRow
actionHostEntry = _ActionHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 6, 1)
)
actionHostEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "actionHostIndex"),
)
if mibBuilder.loadTexts:
    actionHostEntry.setStatus("current")


class _ActionHostIndex_Type(Integer32):
    """Custom type actionHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ActionHostIndex_Type.__name__ = "Integer32"
_ActionHostIndex_Object = MibTableColumn
actionHostIndex = _ActionHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 6, 1, 1),
    _ActionHostIndex_Type()
)
actionHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionHostIndex.setStatus("current")
_ActionHost_Type = DisplayString
_ActionHost_Object = MibTableColumn
actionHost = _ActionHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 6, 1, 2),
    _ActionHost_Type()
)
actionHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionHost.setStatus("current")
_ActionEmailTable_Object = MibTable
actionEmailTable = _ActionEmailTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 7)
)
if mibBuilder.loadTexts:
    actionEmailTable.setStatus("current")
_ActionEmailEntry_Object = MibTableRow
actionEmailEntry = _ActionEmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 7, 1)
)
actionEmailEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "actionEmailIndex"),
)
if mibBuilder.loadTexts:
    actionEmailEntry.setStatus("current")


class _ActionEmailIndex_Type(Integer32):
    """Custom type actionEmailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ActionEmailIndex_Type.__name__ = "Integer32"
_ActionEmailIndex_Object = MibTableColumn
actionEmailIndex = _ActionEmailIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 7, 1, 1),
    _ActionEmailIndex_Type()
)
actionEmailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionEmailIndex.setStatus("current")
_ActionEmail_Type = DisplayString
_ActionEmail_Object = MibTableColumn
actionEmail = _ActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 7, 1, 2),
    _ActionEmail_Type()
)
actionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionEmail.setStatus("current")
_ActionParseError_Type = DisplayString
_ActionParseError_Object = MibScalar
actionParseError = _ActionParseError_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 14, 8),
    _ActionParseError_Type()
)
actionParseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionParseError.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16)
)
_SysTime_ObjectIdentity = ObjectIdentity
sysTime = _SysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1)
)
_SysTimeAutoDST_Type = DisplayString
_SysTimeAutoDST_Object = MibScalar
sysTimeAutoDST = _SysTimeAutoDST_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 1),
    _SysTimeAutoDST_Type()
)
sysTimeAutoDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeAutoDST.setStatus("current")
_SysTimeGMTOffset_Type = Integer32
_SysTimeGMTOffset_Object = MibScalar
sysTimeGMTOffset = _SysTimeGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 2),
    _SysTimeGMTOffset_Type()
)
sysTimeGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeGMTOffset.setStatus("current")
_SysTimeGMTDirection_Type = DisplayString
_SysTimeGMTDirection_Object = MibScalar
sysTimeGMTDirection = _SysTimeGMTDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 3),
    _SysTimeGMTDirection_Type()
)
sysTimeGMTDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeGMTDirection.setStatus("current")
_SysTimeNet_ObjectIdentity = ObjectIdentity
sysTimeNet = _SysTimeNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 4)
)
_SysTimeNetEnable_Type = DisplayString
_SysTimeNetEnable_Object = MibScalar
sysTimeNetEnable = _SysTimeNetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 4, 1),
    _SysTimeNetEnable_Type()
)
sysTimeNetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeNetEnable.setStatus("current")
_SysTimeNetHostTable_Object = MibTable
sysTimeNetHostTable = _SysTimeNetHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sysTimeNetHostTable.setStatus("current")
_SysTimeNetHostEntry_Object = MibTableRow
sysTimeNetHostEntry = _SysTimeNetHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 4, 2, 1)
)
sysTimeNetHostEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "sysTimeNetHostIndex"),
)
if mibBuilder.loadTexts:
    sysTimeNetHostEntry.setStatus("current")


class _SysTimeNetHostIndex_Type(Integer32):
    """Custom type sysTimeNetHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SysTimeNetHostIndex_Type.__name__ = "Integer32"
_SysTimeNetHostIndex_Object = MibTableColumn
sysTimeNetHostIndex = _SysTimeNetHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 4, 2, 1, 1),
    _SysTimeNetHostIndex_Type()
)
sysTimeNetHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeNetHostIndex.setStatus("current")
_SysTimeNetHost_Type = DisplayString
_SysTimeNetHost_Object = MibTableColumn
sysTimeNetHost = _SysTimeNetHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 1, 4, 2, 1, 2),
    _SysTimeNetHost_Type()
)
sysTimeNetHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeNetHost.setStatus("current")
_SysPT_ObjectIdentity = ObjectIdentity
sysPT = _SysPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 2)
)
_SysPTTimeout_Type = Integer32
_SysPTTimeout_Object = MibScalar
sysPTTimeout = _SysPTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 2, 1),
    _SysPTTimeout_Type()
)
sysPTTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPTTimeout.setStatus("current")
_SysPTEndPause_Type = Integer32
_SysPTEndPause_Object = MibScalar
sysPTEndPause = _SysPTEndPause_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 2, 2),
    _SysPTEndPause_Type()
)
sysPTEndPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPTEndPause.setStatus("current")
_SysPTJoinable_Type = DisplayString
_SysPTJoinable_Object = MibScalar
sysPTJoinable = _SysPTJoinable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 2, 3),
    _SysPTJoinable_Type()
)
sysPTJoinable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPTJoinable.setStatus("current")
_SysMTU_Type = Integer32
_SysMTU_Object = MibScalar
sysMTU = _SysMTU_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 3),
    _SysMTU_Type()
)
sysMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMTU.setStatus("current")
_SysAnswerString_Type = DisplayString
_SysAnswerString_Object = MibScalar
sysAnswerString = _SysAnswerString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 4),
    _SysAnswerString_Type()
)
sysAnswerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAnswerString.setStatus("current")
_SysEventFileID_Type = DisplayString
_SysEventFileID_Object = MibScalar
sysEventFileID = _SysEventFileID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 6),
    _SysEventFileID_Type()
)
sysEventFileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEventFileID.setStatus("current")
_SysEscapeCharacter_Type = Integer32
_SysEscapeCharacter_Object = MibScalar
sysEscapeCharacter = _SysEscapeCharacter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 7),
    _SysEscapeCharacter_Type()
)
sysEscapeCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEscapeCharacter.setStatus("current")
_SysTimeStamp_ObjectIdentity = ObjectIdentity
sysTimeStamp = _SysTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 8)
)
_SysTimeStampTimeFormat_Type = DisplayString
_SysTimeStampTimeFormat_Object = MibScalar
sysTimeStampTimeFormat = _SysTimeStampTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 8, 1),
    _SysTimeStampTimeFormat_Type()
)
sysTimeStampTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeStampTimeFormat.setStatus("current")
_SysTimeStampDateFormat_Type = DisplayString
_SysTimeStampDateFormat_Object = MibScalar
sysTimeStampDateFormat = _SysTimeStampDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 8, 2),
    _SysTimeStampDateFormat_Type()
)
sysTimeStampDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeStampDateFormat.setStatus("current")
_SysTimeStampSpaceAfter_Type = DisplayString
_SysTimeStampSpaceAfter_Object = MibScalar
sysTimeStampSpaceAfter = _SysTimeStampSpaceAfter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 8, 3),
    _SysTimeStampSpaceAfter_Type()
)
sysTimeStampSpaceAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeStampSpaceAfter.setStatus("current")
_SysLog_ObjectIdentity = ObjectIdentity
sysLog = _SysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9)
)
_SysLogMode_Type = DisplayString
_SysLogMode_Object = MibScalar
sysLogMode = _SysLogMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9, 1),
    _SysLogMode_Type()
)
sysLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogMode.setStatus("current")
_SysLoghost_Type = DisplayString
_SysLoghost_Object = MibScalar
sysLoghost = _SysLoghost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9, 2),
    _SysLoghost_Type()
)
sysLoghost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoghost.setStatus("current")
_SysLogFilter_Type = DisplayString
_SysLogFilter_Object = MibScalar
sysLogFilter = _SysLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9, 3),
    _SysLogFilter_Type()
)
sysLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFilter.setStatus("current")
_SysLogFileSize_Type = Integer32
_SysLogFileSize_Object = MibScalar
sysLogFileSize = _SysLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9, 4),
    _SysLogFileSize_Type()
)
sysLogFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFileSize.setStatus("current")
_SysLogFileCount_Type = Integer32
_SysLogFileCount_Object = MibScalar
sysLogFileCount = _SysLogFileCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9, 5),
    _SysLogFileCount_Type()
)
sysLogFileCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFileCount.setStatus("current")
_SysLogListenPort_Type = Integer32
_SysLogListenPort_Object = MibScalar
sysLogListenPort = _SysLogListenPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 9, 6),
    _SysLogListenPort_Type()
)
sysLogListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogListenPort.setStatus("current")
_SysCRDB_ObjectIdentity = ObjectIdentity
sysCRDB = _SysCRDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10)
)
_SysCRDBCapacity_Type = Integer32
_SysCRDBCapacity_Object = MibScalar
sysCRDBCapacity = _SysCRDBCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 1),
    _SysCRDBCapacity_Type()
)
sysCRDBCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBCapacity.setStatus("current")
_SysCRDBPercentFull_Type = Integer32
_SysCRDBPercentFull_Object = MibScalar
sysCRDBPercentFull = _SysCRDBPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 2),
    _SysCRDBPercentFull_Type()
)
sysCRDBPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBPercentFull.setStatus("current")
_SysCRDBFileIDTable_Object = MibTable
sysCRDBFileIDTable = _SysCRDBFileIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 3)
)
if mibBuilder.loadTexts:
    sysCRDBFileIDTable.setStatus("current")
_SysCRDBFileIDEntry_Object = MibTableRow
sysCRDBFileIDEntry = _SysCRDBFileIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 3, 1)
)
sysCRDBFileIDEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "sysCRDBFileIDIndex"),
)
if mibBuilder.loadTexts:
    sysCRDBFileIDEntry.setStatus("current")


class _SysCRDBFileIDIndex_Type(Integer32):
    """Custom type sysCRDBFileIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SysCRDBFileIDIndex_Type.__name__ = "Integer32"
_SysCRDBFileIDIndex_Object = MibTableColumn
sysCRDBFileIDIndex = _SysCRDBFileIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 3, 1, 1),
    _SysCRDBFileIDIndex_Type()
)
sysCRDBFileIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBFileIDIndex.setStatus("current")
_SysCRDBFileID_Type = DisplayString
_SysCRDBFileID_Object = MibTableColumn
sysCRDBFileID = _SysCRDBFileID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 3, 1, 2),
    _SysCRDBFileID_Type()
)
sysCRDBFileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCRDBFileID.setStatus("current")
_SysCRDBFileEnforceMinTable_Object = MibTable
sysCRDBFileEnforceMinTable = _SysCRDBFileEnforceMinTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 4)
)
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMinTable.setStatus("current")
_SysCRDBFileEnforceMinEntry_Object = MibTableRow
sysCRDBFileEnforceMinEntry = _SysCRDBFileEnforceMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 4, 1)
)
sysCRDBFileEnforceMinEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "sysCRDBFileEnforceMinIndex"),
)
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMinEntry.setStatus("current")


class _SysCRDBFileEnforceMinIndex_Type(Integer32):
    """Custom type sysCRDBFileEnforceMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SysCRDBFileEnforceMinIndex_Type.__name__ = "Integer32"
_SysCRDBFileEnforceMinIndex_Object = MibTableColumn
sysCRDBFileEnforceMinIndex = _SysCRDBFileEnforceMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 4, 1, 1),
    _SysCRDBFileEnforceMinIndex_Type()
)
sysCRDBFileEnforceMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMinIndex.setStatus("current")
_SysCRDBFileEnforceMin_Type = DisplayString
_SysCRDBFileEnforceMin_Object = MibTableColumn
sysCRDBFileEnforceMin = _SysCRDBFileEnforceMin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 10, 4, 1, 2),
    _SysCRDBFileEnforceMin_Type()
)
sysCRDBFileEnforceMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMin.setStatus("current")
_SysCharMask_Type = OctetString
_SysCharMask_Object = MibScalar
sysCharMask = _SysCharMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 11),
    _SysCharMask_Type()
)
sysCharMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCharMask.setStatus("current")
_SysPrompt_Type = DisplayString
_SysPrompt_Object = MibScalar
sysPrompt = _SysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 12),
    _SysPrompt_Type()
)
sysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPrompt.setStatus("current")
_SysBootStatus_Type = DisplayString
_SysBootStatus_Object = MibScalar
sysBootStatus = _SysBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 13),
    _SysBootStatus_Type()
)
sysBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootStatus.setStatus("current")
_SysLoc_ObjectIdentity = ObjectIdentity
sysLoc = _SysLoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14)
)
_SysLocLatitude_Type = DisplayString
_SysLocLatitude_Object = MibScalar
sysLocLatitude = _SysLocLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14, 1),
    _SysLocLatitude_Type()
)
sysLocLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocLatitude.setStatus("current")
_SysLocLongitude_Type = DisplayString
_SysLocLongitude_Object = MibScalar
sysLocLongitude = _SysLocLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14, 2),
    _SysLocLongitude_Type()
)
sysLocLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocLongitude.setStatus("current")
_SysLocXOffset_Type = DisplayString
_SysLocXOffset_Object = MibScalar
sysLocXOffset = _SysLocXOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14, 3),
    _SysLocXOffset_Type()
)
sysLocXOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocXOffset.setStatus("current")
_SysLocYOffset_Type = DisplayString
_SysLocYOffset_Object = MibScalar
sysLocYOffset = _SysLocYOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14, 4),
    _SysLocYOffset_Type()
)
sysLocYOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocYOffset.setStatus("current")
_SysLocAngle_Type = DisplayString
_SysLocAngle_Object = MibScalar
sysLocAngle = _SysLocAngle_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14, 5),
    _SysLocAngle_Type()
)
sysLocAngle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocAngle.setStatus("current")
_SysLocAltitude_Type = DisplayString
_SysLocAltitude_Object = MibScalar
sysLocAltitude = _SysLocAltitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 14, 6),
    _SysLocAltitude_Type()
)
sysLocAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocAltitude.setStatus("current")
_SysAssetMgmt_ObjectIdentity = ObjectIdentity
sysAssetMgmt = _SysAssetMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15)
)
_SysAMManufacturer_Type = DisplayString
_SysAMManufacturer_Object = MibScalar
sysAMManufacturer = _SysAMManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15, 1),
    _SysAMManufacturer_Type()
)
sysAMManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAMManufacturer.setStatus("current")
_SysAMProduct_Type = DisplayString
_SysAMProduct_Object = MibScalar
sysAMProduct = _SysAMProduct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15, 2),
    _SysAMProduct_Type()
)
sysAMProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAMProduct.setStatus("current")
_SysAMSerialNumber_Type = DisplayString
_SysAMSerialNumber_Object = MibScalar
sysAMSerialNumber = _SysAMSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15, 3),
    _SysAMSerialNumber_Type()
)
sysAMSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAMSerialNumber.setStatus("current")
_SysAMHardwareOptions_Type = DisplayString
_SysAMHardwareOptions_Object = MibScalar
sysAMHardwareOptions = _SysAMHardwareOptions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15, 4),
    _SysAMHardwareOptions_Type()
)
sysAMHardwareOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAMHardwareOptions.setStatus("current")
_SysAMSoftwareVersion_Type = DisplayString
_SysAMSoftwareVersion_Object = MibScalar
sysAMSoftwareVersion = _SysAMSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15, 5),
    _SysAMSoftwareVersion_Type()
)
sysAMSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAMSoftwareVersion.setStatus("current")
_SysAMSiteName_Type = DisplayString
_SysAMSiteName_Object = MibScalar
sysAMSiteName = _SysAMSiteName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 16, 15, 6),
    _SysAMSiteName_Type()
)
sysAMSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAMSiteName.setStatus("current")
_AuditLog_ObjectIdentity = ObjectIdentity
auditLog = _AuditLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17)
)
_AuditLogEnable_Type = DisplayString
_AuditLogEnable_Object = MibScalar
auditLogEnable = _AuditLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 1),
    _AuditLogEnable_Type()
)
auditLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogEnable.setStatus("current")
_AuditLogStoreResets_Type = DisplayString
_AuditLogStoreResets_Object = MibScalar
auditLogStoreResets = _AuditLogStoreResets_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 2),
    _AuditLogStoreResets_Type()
)
auditLogStoreResets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreResets.setStatus("current")
_AuditLogStoreCommands_Type = DisplayString
_AuditLogStoreCommands_Object = MibScalar
auditLogStoreCommands = _AuditLogStoreCommands_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 3),
    _AuditLogStoreCommands_Type()
)
auditLogStoreCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreCommands.setStatus("current")
_AuditLogStoreOutputs_Type = DisplayString
_AuditLogStoreOutputs_Object = MibScalar
auditLogStoreOutputs = _AuditLogStoreOutputs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 4),
    _AuditLogStoreOutputs_Type()
)
auditLogStoreOutputs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreOutputs.setStatus("current")
_AuditLogStoreAlarmActions_Type = DisplayString
_AuditLogStoreAlarmActions_Object = MibScalar
auditLogStoreAlarmActions = _AuditLogStoreAlarmActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 5),
    _AuditLogStoreAlarmActions_Type()
)
auditLogStoreAlarmActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreAlarmActions.setStatus("current")
_AuditLogStorePwdFailures_Type = DisplayString
_AuditLogStorePwdFailures_Object = MibScalar
auditLogStorePwdFailures = _AuditLogStorePwdFailures_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 6),
    _AuditLogStorePwdFailures_Type()
)
auditLogStorePwdFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStorePwdFailures.setStatus("current")
_AuditLogStoreLogins_Type = DisplayString
_AuditLogStoreLogins_Object = MibScalar
auditLogStoreLogins = _AuditLogStoreLogins_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 7),
    _AuditLogStoreLogins_Type()
)
auditLogStoreLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreLogins.setStatus("current")
_AuditLogStoreSHSK_Type = DisplayString
_AuditLogStoreSHSK_Object = MibScalar
auditLogStoreSHSK = _AuditLogStoreSHSK_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 8),
    _AuditLogStoreSHSK_Type()
)
auditLogStoreSHSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreSHSK.setStatus("current")
_AuditLogStorePassthrough_Type = DisplayString
_AuditLogStorePassthrough_Object = MibScalar
auditLogStorePassthrough = _AuditLogStorePassthrough_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 9),
    _AuditLogStorePassthrough_Type()
)
auditLogStorePassthrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStorePassthrough.setStatus("current")
_AuditLogStoreInactivity_Type = DisplayString
_AuditLogStoreInactivity_Object = MibScalar
auditLogStoreInactivity = _AuditLogStoreInactivity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 10),
    _AuditLogStoreInactivity_Type()
)
auditLogStoreInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreInactivity.setStatus("current")
_AuditLogStorePolling_Type = DisplayString
_AuditLogStorePolling_Object = MibScalar
auditLogStorePolling = _AuditLogStorePolling_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 11),
    _AuditLogStorePolling_Type()
)
auditLogStorePolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStorePolling.setStatus("current")
_AuditLogMaxSize_Type = Integer32
_AuditLogMaxSize_Object = MibScalar
auditLogMaxSize = _AuditLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 17, 12),
    _AuditLogMaxSize_Type()
)
auditLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogMaxSize.setStatus("current")
_Scripting_ObjectIdentity = ObjectIdentity
scripting = _Scripting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18)
)
_ScrGlobalEnable_Type = DisplayString
_ScrGlobalEnable_Object = MibScalar
scrGlobalEnable = _ScrGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 1),
    _ScrGlobalEnable_Type()
)
scrGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrGlobalEnable.setStatus("current")
_ScrDTRCtrlPortEnableTable_Object = MibTable
scrDTRCtrlPortEnableTable = _ScrDTRCtrlPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 2)
)
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnableTable.setStatus("current")
_ScrDTRCtrlPortEnableEntry_Object = MibTableRow
scrDTRCtrlPortEnableEntry = _ScrDTRCtrlPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 2, 1)
)
scrDTRCtrlPortEnableEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "scrDTRCtrlPortEnableIndex"),
)
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnableEntry.setStatus("current")


class _ScrDTRCtrlPortEnableIndex_Type(Integer32):
    """Custom type scrDTRCtrlPortEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScrDTRCtrlPortEnableIndex_Type.__name__ = "Integer32"
_ScrDTRCtrlPortEnableIndex_Object = MibTableColumn
scrDTRCtrlPortEnableIndex = _ScrDTRCtrlPortEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 2, 1, 1),
    _ScrDTRCtrlPortEnableIndex_Type()
)
scrDTRCtrlPortEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnableIndex.setStatus("current")
_ScrDTRCtrlPortEnable_Type = DisplayString
_ScrDTRCtrlPortEnable_Object = MibTableColumn
scrDTRCtrlPortEnable = _ScrDTRCtrlPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 2, 1, 2),
    _ScrDTRCtrlPortEnable_Type()
)
scrDTRCtrlPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnable.setStatus("current")
_ScrTable_Object = MibTable
scrTable = _ScrTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3)
)
if mibBuilder.loadTexts:
    scrTable.setStatus("current")
_ScrEntry_Object = MibTableRow
scrEntry = _ScrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1)
)
scrEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "scrIndex"),
)
if mibBuilder.loadTexts:
    scrEntry.setStatus("current")


class _ScrIndex_Type(Integer32):
    """Custom type scrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ScrIndex_Type.__name__ = "Integer32"
_ScrIndex_Object = MibTableColumn
scrIndex = _ScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 1),
    _ScrIndex_Type()
)
scrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrIndex.setStatus("current")
_ScrEnable_Type = DisplayString
_ScrEnable_Object = MibTableColumn
scrEnable = _ScrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 2),
    _ScrEnable_Type()
)
scrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrEnable.setStatus("current")
_ScrName_Type = DisplayString
_ScrName_Object = MibTableColumn
scrName = _ScrName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 3),
    _ScrName_Type()
)
scrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrName.setStatus("current")
_ScrFilename_Type = DisplayString
_ScrFilename_Object = MibTableColumn
scrFilename = _ScrFilename_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 4),
    _ScrFilename_Type()
)
scrFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrFilename.setStatus("current")
_ScrRunAlways_Type = DisplayString
_ScrRunAlways_Object = MibTableColumn
scrRunAlways = _ScrRunAlways_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 5),
    _ScrRunAlways_Type()
)
scrRunAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRunAlways.setStatus("current")
_ScrRunAtStartup_Type = DisplayString
_ScrRunAtStartup_Object = MibTableColumn
scrRunAtStartup = _ScrRunAtStartup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 6),
    _ScrRunAtStartup_Type()
)
scrRunAtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRunAtStartup.setStatus("current")
_ScrRunScheduled_Type = DisplayString
_ScrRunScheduled_Object = MibTableColumn
scrRunScheduled = _ScrRunScheduled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 7),
    _ScrRunScheduled_Type()
)
scrRunScheduled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRunScheduled.setStatus("current")
_ScrScheduleTime_Type = DisplayString
_ScrScheduleTime_Object = MibTableColumn
scrScheduleTime = _ScrScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 8),
    _ScrScheduleTime_Type()
)
scrScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrScheduleTime.setStatus("current")
_ScrArguments_Type = DisplayString
_ScrArguments_Object = MibTableColumn
scrArguments = _ScrArguments_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 9),
    _ScrArguments_Type()
)
scrArguments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrArguments.setStatus("current")
_ScrRepeatInterval_Type = Integer32
_ScrRepeatInterval_Object = MibTableColumn
scrRepeatInterval = _ScrRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 3, 1, 10),
    _ScrRepeatInterval_Type()
)
scrRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRepeatInterval.setStatus("current")
_ScrVolatileStringTable_Object = MibTable
scrVolatileStringTable = _ScrVolatileStringTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 4)
)
if mibBuilder.loadTexts:
    scrVolatileStringTable.setStatus("current")
_ScrVolatileStringEntry_Object = MibTableRow
scrVolatileStringEntry = _ScrVolatileStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 4, 1)
)
scrVolatileStringEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "scrVolatileStringIndex"),
)
if mibBuilder.loadTexts:
    scrVolatileStringEntry.setStatus("current")


class _ScrVolatileStringIndex_Type(Integer32):
    """Custom type scrVolatileStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrVolatileStringIndex_Type.__name__ = "Integer32"
_ScrVolatileStringIndex_Object = MibTableColumn
scrVolatileStringIndex = _ScrVolatileStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 4, 1, 1),
    _ScrVolatileStringIndex_Type()
)
scrVolatileStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrVolatileStringIndex.setStatus("current")
_ScrVolatileString_Type = DisplayString
_ScrVolatileString_Object = MibTableColumn
scrVolatileString = _ScrVolatileString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 4, 1, 2),
    _ScrVolatileString_Type()
)
scrVolatileString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrVolatileString.setStatus("current")
_ScrVolatileIntTable_Object = MibTable
scrVolatileIntTable = _ScrVolatileIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 5)
)
if mibBuilder.loadTexts:
    scrVolatileIntTable.setStatus("current")
_ScrVolatileIntEntry_Object = MibTableRow
scrVolatileIntEntry = _ScrVolatileIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 5, 1)
)
scrVolatileIntEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "scrVolatileIntIndex"),
)
if mibBuilder.loadTexts:
    scrVolatileIntEntry.setStatus("current")


class _ScrVolatileIntIndex_Type(Integer32):
    """Custom type scrVolatileIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrVolatileIntIndex_Type.__name__ = "Integer32"
_ScrVolatileIntIndex_Object = MibTableColumn
scrVolatileIntIndex = _ScrVolatileIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 5, 1, 1),
    _ScrVolatileIntIndex_Type()
)
scrVolatileIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrVolatileIntIndex.setStatus("current")


class _ScrVolatileInt_Type(Integer32):
    """Custom type scrVolatileInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ScrVolatileInt_Type.__name__ = "Integer32"
_ScrVolatileInt_Object = MibTableColumn
scrVolatileInt = _ScrVolatileInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 5, 1, 2),
    _ScrVolatileInt_Type()
)
scrVolatileInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrVolatileInt.setStatus("current")
_ScrNonVolatileStringTable_Object = MibTable
scrNonVolatileStringTable = _ScrNonVolatileStringTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 6)
)
if mibBuilder.loadTexts:
    scrNonVolatileStringTable.setStatus("current")
_ScrNonVolatileStringEntry_Object = MibTableRow
scrNonVolatileStringEntry = _ScrNonVolatileStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 6, 1)
)
scrNonVolatileStringEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "scrNonVolatileStringIndex"),
)
if mibBuilder.loadTexts:
    scrNonVolatileStringEntry.setStatus("current")


class _ScrNonVolatileStringIndex_Type(Integer32):
    """Custom type scrNonVolatileStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrNonVolatileStringIndex_Type.__name__ = "Integer32"
_ScrNonVolatileStringIndex_Object = MibTableColumn
scrNonVolatileStringIndex = _ScrNonVolatileStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 6, 1, 1),
    _ScrNonVolatileStringIndex_Type()
)
scrNonVolatileStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrNonVolatileStringIndex.setStatus("current")
_ScrNonVolatileString_Type = DisplayString
_ScrNonVolatileString_Object = MibTableColumn
scrNonVolatileString = _ScrNonVolatileString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 6, 1, 2),
    _ScrNonVolatileString_Type()
)
scrNonVolatileString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrNonVolatileString.setStatus("current")
_ScrNonVolatileIntTable_Object = MibTable
scrNonVolatileIntTable = _ScrNonVolatileIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 7)
)
if mibBuilder.loadTexts:
    scrNonVolatileIntTable.setStatus("current")
_ScrNonVolatileIntEntry_Object = MibTableRow
scrNonVolatileIntEntry = _ScrNonVolatileIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 7, 1)
)
scrNonVolatileIntEntry.setIndexNames(
    (0, "SITEBOSS-570-STD-MIB", "scrNonVolatileIntIndex"),
)
if mibBuilder.loadTexts:
    scrNonVolatileIntEntry.setStatus("current")


class _ScrNonVolatileIntIndex_Type(Integer32):
    """Custom type scrNonVolatileIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrNonVolatileIntIndex_Type.__name__ = "Integer32"
_ScrNonVolatileIntIndex_Object = MibTableColumn
scrNonVolatileIntIndex = _ScrNonVolatileIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 7, 1, 1),
    _ScrNonVolatileIntIndex_Type()
)
scrNonVolatileIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrNonVolatileIntIndex.setStatus("current")


class _ScrNonVolatileInt_Type(Integer32):
    """Custom type scrNonVolatileInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ScrNonVolatileInt_Type.__name__ = "Integer32"
_ScrNonVolatileInt_Object = MibTableColumn
scrNonVolatileInt = _ScrNonVolatileInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 2, 18, 7, 1, 2),
    _ScrNonVolatileInt_Type()
)
scrNonVolatileInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrNonVolatileInt.setStatus("current")
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3)
)
_SiteName_Type = DisplayString
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 1),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_ThisProduct_Type = DisplayString
_ThisProduct_Object = MibScalar
thisProduct = _ThisProduct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 2),
    _ThisProduct_Type()
)
thisProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thisProduct.setStatus("current")
_StockTrapString_Type = DisplayString
_StockTrapString_Object = MibScalar
stockTrapString = _StockTrapString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 3),
    _StockTrapString_Type()
)
stockTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stockTrapString.setStatus("current")
_TrapEventTypeNumber_Type = Integer32
_TrapEventTypeNumber_Object = MibScalar
trapEventTypeNumber = _TrapEventTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 4),
    _TrapEventTypeNumber_Type()
)
trapEventTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeNumber.setStatus("current")
_TrapEventTypeName_Type = DisplayString
_TrapEventTypeName_Object = MibScalar
trapEventTypeName = _TrapEventTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 5),
    _TrapEventTypeName_Type()
)
trapEventTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeName.setStatus("current")


class _TrapIncludedValue_Type(Integer32):
    """Custom type trapIncludedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_TrapIncludedValue_Type.__name__ = "Integer32"
_TrapIncludedValue_Object = MibScalar
trapIncludedValue = _TrapIncludedValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 6),
    _TrapIncludedValue_Type()
)
trapIncludedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedValue.setStatus("current")
_TrapIncludedString_Type = DisplayString
_TrapIncludedString_Object = MibScalar
trapIncludedString = _TrapIncludedString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 7),
    _TrapIncludedString_Type()
)
trapIncludedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedString.setStatus("current")
_TrapTypeString_Type = DisplayString
_TrapTypeString_Object = MibScalar
trapTypeString = _TrapTypeString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 8),
    _TrapTypeString_Type()
)
trapTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTypeString.setStatus("current")
_TrapEventClassNumber_Type = Integer32
_TrapEventClassNumber_Object = MibScalar
trapEventClassNumber = _TrapEventClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 9),
    _TrapEventClassNumber_Type()
)
trapEventClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventClassNumber.setStatus("current")
_TrapEventClassName_Type = DisplayString
_TrapEventClassName_Object = MibScalar
trapEventClassName = _TrapEventClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 3, 10),
    _TrapEventClassName_Type()
)
trapEventClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventClassName.setStatus("current")
_KeyInterface_Type = DisplayString
_KeyInterface_Object = MibScalar
keyInterface = _KeyInterface_Object(
    (1, 3, 6, 1, 4, 1, 3052, 8, 4),
    _KeyInterface_Type()
)
keyInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyInterface.setStatus("current")

# Managed Objects groups


# Notification objects

s570StockContactClosureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 110)
)
s570StockContactClosureTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockContactClosureTrap.setStatus(
        "current"
    )

s570StockTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 120)
)
s570StockTempTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockTempTrap.setStatus(
        "current"
    )

s570StockHumidityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 130)
)
s570StockHumidityTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockHumidityTrap.setStatus(
        "current"
    )

s570StockAnalogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 140)
)
s570StockAnalogTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockAnalogTrap.setStatus(
        "current"
    )

s570StockOutputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 150)
)
s570StockOutputTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockOutputTrap.setStatus(
        "current"
    )

s570StockDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 503)
)
s570StockDataAlarmTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockDataAlarmTrap.setStatus(
        "current"
    )

s570StockNoDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 505)
)
s570StockNoDataAlarmTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockNoDataAlarmTrap.setStatus(
        "current"
    )

s570StockSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 506)
)
s570StockSchedTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockSchedTrap.setStatus(
        "current"
    )

s570StockImmediateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 507)
)
s570StockImmediateTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockImmediateTrap.setStatus(
        "current"
    )

s570StockCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 510)
)
s570StockCTSTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockCTSTrap.setStatus(
        "current"
    )

s570CPEDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 511)
)
s570CPEDownTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570CPEDownTrap.setStatus(
        "current"
    )

s570FuelSensorDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 515)
)
s570FuelSensorDisconnectTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570FuelSensorDisconnectTrap.setStatus(
        "current"
    )

s570FuelSensorVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 519)
)
s570FuelSensorVolumeTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570FuelSensorVolumeTrap.setStatus(
        "current"
    )

s570ACPowerMonitorAvgVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 520)
)
s570ACPowerMonitorAvgVoltageTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ACPowerMonitorAvgVoltageTrap.setStatus(
        "current"
    )

s570ACPowerMonitorAvgCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 521)
)
s570ACPowerMonitorAvgCurrentTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ACPowerMonitorAvgCurrentTrap.setStatus(
        "current"
    )

s570ACPowerMonitorFrequencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 522)
)
s570ACPowerMonitorFrequencyTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ACPowerMonitorFrequencyTrap.setStatus(
        "current"
    )

s570ACPowerMonitorTRPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 523)
)
s570ACPowerMonitorTRPTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ACPowerMonitorTRPTrap.setStatus(
        "current"
    )

s570ACPowerMonitorDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 524)
)
s570ACPowerMonitorDisconnectTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ACPowerMonitorDisconnectTrap.setStatus(
        "current"
    )

s570StockLoadSheddingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 525)
)
s570StockLoadSheddingTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockLoadSheddingTrap.setStatus(
        "current"
    )

s570StockScriptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 526)
)
s570StockScriptTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570StockScriptTrap.setStatus(
        "current"
    )

s570ACTotalPowerFactorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 540)
)
s570ACTotalPowerFactorTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ACTotalPowerFactorTrap.setStatus(
        "current"
    )

s570ResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 543)
)
s570ResetTrap.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "stockTrapString"),
        ("SITEBOSS-570-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s570ResetTrap.setStatus(
        "current"
    )

s570UserTrap1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1000)
)
s570UserTrap1000.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1000.setStatus(
        "current"
    )

s570UserTrap1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1001)
)
s570UserTrap1001.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1001.setStatus(
        "current"
    )

s570UserTrap1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1002)
)
s570UserTrap1002.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1002.setStatus(
        "current"
    )

s570UserTrap1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1003)
)
s570UserTrap1003.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1003.setStatus(
        "current"
    )

s570UserTrap1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1004)
)
s570UserTrap1004.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1004.setStatus(
        "current"
    )

s570UserTrap1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1005)
)
s570UserTrap1005.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1005.setStatus(
        "current"
    )

s570UserTrap1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1006)
)
s570UserTrap1006.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1006.setStatus(
        "current"
    )

s570UserTrap1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1007)
)
s570UserTrap1007.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1007.setStatus(
        "current"
    )

s570UserTrap1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1008)
)
s570UserTrap1008.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1008.setStatus(
        "current"
    )

s570UserTrap1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1009)
)
s570UserTrap1009.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1009.setStatus(
        "current"
    )

s570UserTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1010)
)
s570UserTrap1010.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1010.setStatus(
        "current"
    )

s570UserTrap1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1011)
)
s570UserTrap1011.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1011.setStatus(
        "current"
    )

s570UserTrap1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1012)
)
s570UserTrap1012.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1012.setStatus(
        "current"
    )

s570UserTrap1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1013)
)
s570UserTrap1013.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1013.setStatus(
        "current"
    )

s570UserTrap1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1014)
)
s570UserTrap1014.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1014.setStatus(
        "current"
    )

s570UserTrap1015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1015)
)
s570UserTrap1015.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1015.setStatus(
        "current"
    )

s570UserTrap1016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1016)
)
s570UserTrap1016.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1016.setStatus(
        "current"
    )

s570UserTrap1017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1017)
)
s570UserTrap1017.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1017.setStatus(
        "current"
    )

s570UserTrap1018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1018)
)
s570UserTrap1018.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1018.setStatus(
        "current"
    )

s570UserTrap1019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1019)
)
s570UserTrap1019.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1019.setStatus(
        "current"
    )

s570UserTrap1020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1020)
)
s570UserTrap1020.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1020.setStatus(
        "current"
    )

s570UserTrap1021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1021)
)
s570UserTrap1021.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1021.setStatus(
        "current"
    )

s570UserTrap1022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1022)
)
s570UserTrap1022.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1022.setStatus(
        "current"
    )

s570UserTrap1023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1023)
)
s570UserTrap1023.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1023.setStatus(
        "current"
    )

s570UserTrap1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1024)
)
s570UserTrap1024.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1024.setStatus(
        "current"
    )

s570UserTrap1025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1025)
)
s570UserTrap1025.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1025.setStatus(
        "current"
    )

s570UserTrap1026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1026)
)
s570UserTrap1026.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1026.setStatus(
        "current"
    )

s570UserTrap1027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1027)
)
s570UserTrap1027.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1027.setStatus(
        "current"
    )

s570UserTrap1028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1028)
)
s570UserTrap1028.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1028.setStatus(
        "current"
    )

s570UserTrap1029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1029)
)
s570UserTrap1029.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1029.setStatus(
        "current"
    )

s570UserTrap1030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1030)
)
s570UserTrap1030.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1030.setStatus(
        "current"
    )

s570UserTrap1031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1031)
)
s570UserTrap1031.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1031.setStatus(
        "current"
    )

s570UserTrap1032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1032)
)
s570UserTrap1032.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1032.setStatus(
        "current"
    )

s570UserTrap1033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1033)
)
s570UserTrap1033.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1033.setStatus(
        "current"
    )

s570UserTrap1034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1034)
)
s570UserTrap1034.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1034.setStatus(
        "current"
    )

s570UserTrap1035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1035)
)
s570UserTrap1035.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1035.setStatus(
        "current"
    )

s570UserTrap1036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1036)
)
s570UserTrap1036.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1036.setStatus(
        "current"
    )

s570UserTrap1037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1037)
)
s570UserTrap1037.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1037.setStatus(
        "current"
    )

s570UserTrap1038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1038)
)
s570UserTrap1038.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1038.setStatus(
        "current"
    )

s570UserTrap1039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1039)
)
s570UserTrap1039.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1039.setStatus(
        "current"
    )

s570UserTrap1040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1040)
)
s570UserTrap1040.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1040.setStatus(
        "current"
    )

s570UserTrap1041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1041)
)
s570UserTrap1041.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1041.setStatus(
        "current"
    )

s570UserTrap1042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1042)
)
s570UserTrap1042.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1042.setStatus(
        "current"
    )

s570UserTrap1043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1043)
)
s570UserTrap1043.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1043.setStatus(
        "current"
    )

s570UserTrap1044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1044)
)
s570UserTrap1044.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1044.setStatus(
        "current"
    )

s570UserTrap1045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1045)
)
s570UserTrap1045.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1045.setStatus(
        "current"
    )

s570UserTrap1046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1046)
)
s570UserTrap1046.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1046.setStatus(
        "current"
    )

s570UserTrap1047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1047)
)
s570UserTrap1047.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1047.setStatus(
        "current"
    )

s570UserTrap1048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1048)
)
s570UserTrap1048.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1048.setStatus(
        "current"
    )

s570UserTrap1049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1049)
)
s570UserTrap1049.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1049.setStatus(
        "current"
    )

s570UserTrap1050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1050)
)
s570UserTrap1050.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1050.setStatus(
        "current"
    )

s570UserTrap1051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1051)
)
s570UserTrap1051.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1051.setStatus(
        "current"
    )

s570UserTrap1052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1052)
)
s570UserTrap1052.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1052.setStatus(
        "current"
    )

s570UserTrap1053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1053)
)
s570UserTrap1053.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1053.setStatus(
        "current"
    )

s570UserTrap1054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1054)
)
s570UserTrap1054.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1054.setStatus(
        "current"
    )

s570UserTrap1055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1055)
)
s570UserTrap1055.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1055.setStatus(
        "current"
    )

s570UserTrap1056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1056)
)
s570UserTrap1056.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1056.setStatus(
        "current"
    )

s570UserTrap1057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1057)
)
s570UserTrap1057.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1057.setStatus(
        "current"
    )

s570UserTrap1058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1058)
)
s570UserTrap1058.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1058.setStatus(
        "current"
    )

s570UserTrap1059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1059)
)
s570UserTrap1059.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1059.setStatus(
        "current"
    )

s570UserTrap1060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1060)
)
s570UserTrap1060.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1060.setStatus(
        "current"
    )

s570UserTrap1061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1061)
)
s570UserTrap1061.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1061.setStatus(
        "current"
    )

s570UserTrap1062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1062)
)
s570UserTrap1062.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1062.setStatus(
        "current"
    )

s570UserTrap1063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1063)
)
s570UserTrap1063.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1063.setStatus(
        "current"
    )

s570UserTrap1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1064)
)
s570UserTrap1064.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1064.setStatus(
        "current"
    )

s570UserTrap1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1065)
)
s570UserTrap1065.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1065.setStatus(
        "current"
    )

s570UserTrap1066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1066)
)
s570UserTrap1066.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1066.setStatus(
        "current"
    )

s570UserTrap1067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1067)
)
s570UserTrap1067.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1067.setStatus(
        "current"
    )

s570UserTrap1068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1068)
)
s570UserTrap1068.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1068.setStatus(
        "current"
    )

s570UserTrap1069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1069)
)
s570UserTrap1069.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1069.setStatus(
        "current"
    )

s570UserTrap1070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1070)
)
s570UserTrap1070.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1070.setStatus(
        "current"
    )

s570UserTrap1071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1071)
)
s570UserTrap1071.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1071.setStatus(
        "current"
    )

s570UserTrap1072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1072)
)
s570UserTrap1072.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1072.setStatus(
        "current"
    )

s570UserTrap1073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1073)
)
s570UserTrap1073.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1073.setStatus(
        "current"
    )

s570UserTrap1074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1074)
)
s570UserTrap1074.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1074.setStatus(
        "current"
    )

s570UserTrap1075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1075)
)
s570UserTrap1075.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1075.setStatus(
        "current"
    )

s570UserTrap1076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1076)
)
s570UserTrap1076.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1076.setStatus(
        "current"
    )

s570UserTrap1077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1077)
)
s570UserTrap1077.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1077.setStatus(
        "current"
    )

s570UserTrap1078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1078)
)
s570UserTrap1078.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1078.setStatus(
        "current"
    )

s570UserTrap1079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1079)
)
s570UserTrap1079.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1079.setStatus(
        "current"
    )

s570UserTrap1080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1080)
)
s570UserTrap1080.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1080.setStatus(
        "current"
    )

s570UserTrap1081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1081)
)
s570UserTrap1081.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1081.setStatus(
        "current"
    )

s570UserTrap1082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1082)
)
s570UserTrap1082.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1082.setStatus(
        "current"
    )

s570UserTrap1083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1083)
)
s570UserTrap1083.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1083.setStatus(
        "current"
    )

s570UserTrap1084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1084)
)
s570UserTrap1084.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1084.setStatus(
        "current"
    )

s570UserTrap1085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1085)
)
s570UserTrap1085.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1085.setStatus(
        "current"
    )

s570UserTrap1086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1086)
)
s570UserTrap1086.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1086.setStatus(
        "current"
    )

s570UserTrap1087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1087)
)
s570UserTrap1087.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1087.setStatus(
        "current"
    )

s570UserTrap1088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1088)
)
s570UserTrap1088.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1088.setStatus(
        "current"
    )

s570UserTrap1089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1089)
)
s570UserTrap1089.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1089.setStatus(
        "current"
    )

s570UserTrap1090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1090)
)
s570UserTrap1090.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1090.setStatus(
        "current"
    )

s570UserTrap1091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1091)
)
s570UserTrap1091.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1091.setStatus(
        "current"
    )

s570UserTrap1092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1092)
)
s570UserTrap1092.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1092.setStatus(
        "current"
    )

s570UserTrap1093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1093)
)
s570UserTrap1093.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1093.setStatus(
        "current"
    )

s570UserTrap1094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1094)
)
s570UserTrap1094.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1094.setStatus(
        "current"
    )

s570UserTrap1095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1095)
)
s570UserTrap1095.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1095.setStatus(
        "current"
    )

s570UserTrap1096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1096)
)
s570UserTrap1096.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1096.setStatus(
        "current"
    )

s570UserTrap1097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1097)
)
s570UserTrap1097.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1097.setStatus(
        "current"
    )

s570UserTrap1098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1098)
)
s570UserTrap1098.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1098.setStatus(
        "current"
    )

s570UserTrap1099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1099)
)
s570UserTrap1099.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1099.setStatus(
        "current"
    )

s570UserTrap1100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1100)
)
s570UserTrap1100.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1100.setStatus(
        "current"
    )

s570UserTrap1101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1101)
)
s570UserTrap1101.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1101.setStatus(
        "current"
    )

s570UserTrap1102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1102)
)
s570UserTrap1102.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1102.setStatus(
        "current"
    )

s570UserTrap1103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1103)
)
s570UserTrap1103.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1103.setStatus(
        "current"
    )

s570UserTrap1104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1104)
)
s570UserTrap1104.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1104.setStatus(
        "current"
    )

s570UserTrap1105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1105)
)
s570UserTrap1105.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1105.setStatus(
        "current"
    )

s570UserTrap1106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1106)
)
s570UserTrap1106.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1106.setStatus(
        "current"
    )

s570UserTrap1107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1107)
)
s570UserTrap1107.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1107.setStatus(
        "current"
    )

s570UserTrap1108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1108)
)
s570UserTrap1108.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1108.setStatus(
        "current"
    )

s570UserTrap1109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1109)
)
s570UserTrap1109.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1109.setStatus(
        "current"
    )

s570UserTrap1110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1110)
)
s570UserTrap1110.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1110.setStatus(
        "current"
    )

s570UserTrap1111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1111)
)
s570UserTrap1111.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1111.setStatus(
        "current"
    )

s570UserTrap1112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1112)
)
s570UserTrap1112.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1112.setStatus(
        "current"
    )

s570UserTrap1113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1113)
)
s570UserTrap1113.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1113.setStatus(
        "current"
    )

s570UserTrap1114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1114)
)
s570UserTrap1114.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1114.setStatus(
        "current"
    )

s570UserTrap1115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1115)
)
s570UserTrap1115.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1115.setStatus(
        "current"
    )

s570UserTrap1116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1116)
)
s570UserTrap1116.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1116.setStatus(
        "current"
    )

s570UserTrap1117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1117)
)
s570UserTrap1117.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1117.setStatus(
        "current"
    )

s570UserTrap1118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1118)
)
s570UserTrap1118.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1118.setStatus(
        "current"
    )

s570UserTrap1119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1119)
)
s570UserTrap1119.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1119.setStatus(
        "current"
    )

s570UserTrap1120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1120)
)
s570UserTrap1120.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1120.setStatus(
        "current"
    )

s570UserTrap1121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1121)
)
s570UserTrap1121.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1121.setStatus(
        "current"
    )

s570UserTrap1122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1122)
)
s570UserTrap1122.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1122.setStatus(
        "current"
    )

s570UserTrap1123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1123)
)
s570UserTrap1123.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1123.setStatus(
        "current"
    )

s570UserTrap1124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1124)
)
s570UserTrap1124.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1124.setStatus(
        "current"
    )

s570UserTrap1125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1125)
)
s570UserTrap1125.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1125.setStatus(
        "current"
    )

s570UserTrap1126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1126)
)
s570UserTrap1126.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1126.setStatus(
        "current"
    )

s570UserTrap1127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1127)
)
s570UserTrap1127.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1127.setStatus(
        "current"
    )

s570UserTrap1128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1128)
)
s570UserTrap1128.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1128.setStatus(
        "current"
    )

s570UserTrap1129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1129)
)
s570UserTrap1129.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1129.setStatus(
        "current"
    )

s570UserTrap1130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1130)
)
s570UserTrap1130.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1130.setStatus(
        "current"
    )

s570UserTrap1131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1131)
)
s570UserTrap1131.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1131.setStatus(
        "current"
    )

s570UserTrap1132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1132)
)
s570UserTrap1132.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1132.setStatus(
        "current"
    )

s570UserTrap1133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1133)
)
s570UserTrap1133.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1133.setStatus(
        "current"
    )

s570UserTrap1134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1134)
)
s570UserTrap1134.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1134.setStatus(
        "current"
    )

s570UserTrap1135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1135)
)
s570UserTrap1135.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1135.setStatus(
        "current"
    )

s570UserTrap1136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1136)
)
s570UserTrap1136.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1136.setStatus(
        "current"
    )

s570UserTrap1137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1137)
)
s570UserTrap1137.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1137.setStatus(
        "current"
    )

s570UserTrap1138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1138)
)
s570UserTrap1138.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1138.setStatus(
        "current"
    )

s570UserTrap1139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1139)
)
s570UserTrap1139.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1139.setStatus(
        "current"
    )

s570UserTrap1140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1140)
)
s570UserTrap1140.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1140.setStatus(
        "current"
    )

s570UserTrap1141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1141)
)
s570UserTrap1141.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1141.setStatus(
        "current"
    )

s570UserTrap1142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1142)
)
s570UserTrap1142.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1142.setStatus(
        "current"
    )

s570UserTrap1143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1143)
)
s570UserTrap1143.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1143.setStatus(
        "current"
    )

s570UserTrap1144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1144)
)
s570UserTrap1144.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1144.setStatus(
        "current"
    )

s570UserTrap1145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1145)
)
s570UserTrap1145.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1145.setStatus(
        "current"
    )

s570UserTrap1146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1146)
)
s570UserTrap1146.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1146.setStatus(
        "current"
    )

s570UserTrap1147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1147)
)
s570UserTrap1147.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1147.setStatus(
        "current"
    )

s570UserTrap1148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1148)
)
s570UserTrap1148.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1148.setStatus(
        "current"
    )

s570UserTrap1149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1149)
)
s570UserTrap1149.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1149.setStatus(
        "current"
    )

s570UserTrap1150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1150)
)
s570UserTrap1150.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1150.setStatus(
        "current"
    )

s570UserTrap1151 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1151)
)
s570UserTrap1151.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1151.setStatus(
        "current"
    )

s570UserTrap1152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1152)
)
s570UserTrap1152.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1152.setStatus(
        "current"
    )

s570UserTrap1153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1153)
)
s570UserTrap1153.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1153.setStatus(
        "current"
    )

s570UserTrap1154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1154)
)
s570UserTrap1154.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1154.setStatus(
        "current"
    )

s570UserTrap1155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1155)
)
s570UserTrap1155.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1155.setStatus(
        "current"
    )

s570UserTrap1156 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1156)
)
s570UserTrap1156.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1156.setStatus(
        "current"
    )

s570UserTrap1157 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1157)
)
s570UserTrap1157.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1157.setStatus(
        "current"
    )

s570UserTrap1158 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1158)
)
s570UserTrap1158.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1158.setStatus(
        "current"
    )

s570UserTrap1159 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1159)
)
s570UserTrap1159.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1159.setStatus(
        "current"
    )

s570UserTrap1160 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1160)
)
s570UserTrap1160.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1160.setStatus(
        "current"
    )

s570UserTrap1161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1161)
)
s570UserTrap1161.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1161.setStatus(
        "current"
    )

s570UserTrap1162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1162)
)
s570UserTrap1162.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1162.setStatus(
        "current"
    )

s570UserTrap1163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1163)
)
s570UserTrap1163.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1163.setStatus(
        "current"
    )

s570UserTrap1164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1164)
)
s570UserTrap1164.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1164.setStatus(
        "current"
    )

s570UserTrap1165 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1165)
)
s570UserTrap1165.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1165.setStatus(
        "current"
    )

s570UserTrap1166 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1166)
)
s570UserTrap1166.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1166.setStatus(
        "current"
    )

s570UserTrap1167 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1167)
)
s570UserTrap1167.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1167.setStatus(
        "current"
    )

s570UserTrap1168 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1168)
)
s570UserTrap1168.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1168.setStatus(
        "current"
    )

s570UserTrap1169 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1169)
)
s570UserTrap1169.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1169.setStatus(
        "current"
    )

s570UserTrap1170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1170)
)
s570UserTrap1170.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1170.setStatus(
        "current"
    )

s570UserTrap1171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1171)
)
s570UserTrap1171.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1171.setStatus(
        "current"
    )

s570UserTrap1172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1172)
)
s570UserTrap1172.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1172.setStatus(
        "current"
    )

s570UserTrap1173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1173)
)
s570UserTrap1173.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1173.setStatus(
        "current"
    )

s570UserTrap1174 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1174)
)
s570UserTrap1174.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1174.setStatus(
        "current"
    )

s570UserTrap1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1175)
)
s570UserTrap1175.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1175.setStatus(
        "current"
    )

s570UserTrap1176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1176)
)
s570UserTrap1176.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1176.setStatus(
        "current"
    )

s570UserTrap1177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1177)
)
s570UserTrap1177.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1177.setStatus(
        "current"
    )

s570UserTrap1178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1178)
)
s570UserTrap1178.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1178.setStatus(
        "current"
    )

s570UserTrap1179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1179)
)
s570UserTrap1179.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1179.setStatus(
        "current"
    )

s570UserTrap1180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1180)
)
s570UserTrap1180.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1180.setStatus(
        "current"
    )

s570UserTrap1181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1181)
)
s570UserTrap1181.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1181.setStatus(
        "current"
    )

s570UserTrap1182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1182)
)
s570UserTrap1182.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1182.setStatus(
        "current"
    )

s570UserTrap1183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1183)
)
s570UserTrap1183.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1183.setStatus(
        "current"
    )

s570UserTrap1184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1184)
)
s570UserTrap1184.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1184.setStatus(
        "current"
    )

s570UserTrap1185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1185)
)
s570UserTrap1185.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1185.setStatus(
        "current"
    )

s570UserTrap1186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1186)
)
s570UserTrap1186.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1186.setStatus(
        "current"
    )

s570UserTrap1187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1187)
)
s570UserTrap1187.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1187.setStatus(
        "current"
    )

s570UserTrap1188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1188)
)
s570UserTrap1188.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1188.setStatus(
        "current"
    )

s570UserTrap1189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1189)
)
s570UserTrap1189.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1189.setStatus(
        "current"
    )

s570UserTrap1190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1190)
)
s570UserTrap1190.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1190.setStatus(
        "current"
    )

s570UserTrap1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1191)
)
s570UserTrap1191.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1191.setStatus(
        "current"
    )

s570UserTrap1192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1192)
)
s570UserTrap1192.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1192.setStatus(
        "current"
    )

s570UserTrap1193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1193)
)
s570UserTrap1193.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1193.setStatus(
        "current"
    )

s570UserTrap1194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1194)
)
s570UserTrap1194.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1194.setStatus(
        "current"
    )

s570UserTrap1195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1195)
)
s570UserTrap1195.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1195.setStatus(
        "current"
    )

s570UserTrap1196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1196)
)
s570UserTrap1196.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1196.setStatus(
        "current"
    )

s570UserTrap1197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1197)
)
s570UserTrap1197.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1197.setStatus(
        "current"
    )

s570UserTrap1198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1198)
)
s570UserTrap1198.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1198.setStatus(
        "current"
    )

s570UserTrap1199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 8, 1199)
)
s570UserTrap1199.setObjects(
      *(("SITEBOSS-570-STD-MIB", "siteName"),
        ("SITEBOSS-570-STD-MIB", "esIndex"),
        ("SITEBOSS-570-STD-MIB", "esName"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-570-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-570-STD-MIB", "esPointName"),
        ("SITEBOSS-570-STD-MIB", "esID"),
        ("SITEBOSS-570-STD-MIB", "clock"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-570-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-570-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s570UserTrap1199.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SITEBOSS-570-STD-MIB",
    **{"s570": s570,
       "status": status,
       "eventSensorStatus": eventSensorStatus,
       "esPointTable": esPointTable,
       "esPointEntry": esPointEntry,
       "esIndexES": esIndexES,
       "esIndexPC": esIndexPC,
       "esIndexPoint": esIndexPoint,
       "esPointName": esPointName,
       "esPointInEventState": esPointInEventState,
       "esPointValueInt": esPointValueInt,
       "esPointValueStr": esPointValueStr,
       "esPointTimeLastChange": esPointTimeLastChange,
       "esPointTimetickLastChange": esPointTimetickLastChange,
       "dataEventStatus": dataEventStatus,
       "deStatusTable": deStatusTable,
       "deStatusEntry": deStatusEntry,
       "deStatusIndex": deStatusIndex,
       "deStatusName": deStatusName,
       "deStatusCounter": deStatusCounter,
       "deStatusThreshold": deStatusThreshold,
       "modemStatus": modemStatus,
       "modemCLIDLogTable": modemCLIDLogTable,
       "modemCLIDLogEntry": modemCLIDLogEntry,
       "modemCLIDLogIndex": modemCLIDLogIndex,
       "modemCLIDLogNumber": modemCLIDLogNumber,
       "fuelSensorStatus": fuelSensorStatus,
       "fsStatusTable": fsStatusTable,
       "fsStatusEntry": fsStatusEntry,
       "fsStatusIndex": fsStatusIndex,
       "fsStatusName": fsStatusName,
       "fsStatusDeviceState": fsStatusDeviceState,
       "fsStatusVolumeValueString": fsStatusVolumeValueString,
       "fsStatusVolumePercentLevel": fsStatusVolumePercentLevel,
       "fsStatusVolumeInEventState": fsStatusVolumeInEventState,
       "fsStatusCombined": fsStatusCombined,
       "wirelessModemStatus": wirelessModemStatus,
       "wmsStatus": wmsStatus,
       "wmsSignal": wmsSignal,
       "wmsRSSI": wmsRSSI,
       "wmsBER": wmsBER,
       "wmsUpdated": wmsUpdated,
       "wmsRegistration": wmsRegistration,
       "wmsLAC": wmsLAC,
       "wmsCellID": wmsCellID,
       "wmsIMSI": wmsIMSI,
       "wmsPhnum": wmsPhnum,
       "wmsLocalIP": wmsLocalIP,
       "wmsMgfID": wmsMgfID,
       "wmsModelID": wmsModelID,
       "wmsIMEI": wmsIMEI,
       "wmsRevID": wmsRevID,
       "wmsNetName": wmsNetName,
       "wmsGPRSStatus": wmsGPRSStatus,
       "wmsBand": wmsBand,
       "wmsChannel": wmsChannel,
       "wmsCountryCode": wmsCountryCode,
       "wmsNetCode": wmsNetCode,
       "wmsPLMNColor": wmsPLMNColor,
       "wmsBScolor": wmsBScolor,
       "wmsMpRACH": wmsMpRACH,
       "wmsMinRxLevel": wmsMinRxLevel,
       "wmsBaseCoeff": wmsBaseCoeff,
       "wmsSIMStatus": wmsSIMStatus,
       "wmsICCID": wmsICCID,
       "wmsModemType": wmsModemType,
       "acPowerMonitorStatus": acPowerMonitorStatus,
       "acpmStatusTable": acpmStatusTable,
       "acpmStatusEntry": acpmStatusEntry,
       "acpmsIndex": acpmsIndex,
       "acpmsName": acpmsName,
       "acpmsAvgVoltageValueStr": acpmsAvgVoltageValueStr,
       "acpmsAvgVoltageMinStr": acpmsAvgVoltageMinStr,
       "acpmsAvgVoltageMaxStr": acpmsAvgVoltageMaxStr,
       "acpmsAvgVoltageAvgStr": acpmsAvgVoltageAvgStr,
       "acpmsAvgVoltageInEventState": acpmsAvgVoltageInEventState,
       "acpmsVoltagePhaseAValueStr": acpmsVoltagePhaseAValueStr,
       "acpmsVoltagePhaseBValueStr": acpmsVoltagePhaseBValueStr,
       "acpmsVoltagePhaseCValueStr": acpmsVoltagePhaseCValueStr,
       "acpmsAvgCurrentValueStr": acpmsAvgCurrentValueStr,
       "acpmsAvgCurrentMinStr": acpmsAvgCurrentMinStr,
       "acpmsAvgCurrentMaxStr": acpmsAvgCurrentMaxStr,
       "acpmsAvgCurrentAvgStr": acpmsAvgCurrentAvgStr,
       "acpmsAvgCurrentInEventState": acpmsAvgCurrentInEventState,
       "acpmsCurrentPhaseAValueStr": acpmsCurrentPhaseAValueStr,
       "acpmsCurrentPhaseBValueStr": acpmsCurrentPhaseBValueStr,
       "acpmsCurrentPhaseCValueStr": acpmsCurrentPhaseCValueStr,
       "acpmsAvgFreqValueStr": acpmsAvgFreqValueStr,
       "acpmsAvgFreqMinStr": acpmsAvgFreqMinStr,
       "acpmsAvgFreqMaxStr": acpmsAvgFreqMaxStr,
       "acpmsAvgFreqAvgStr": acpmsAvgFreqAvgStr,
       "acpmsAvgFreqInEventState": acpmsAvgFreqInEventState,
       "acpmsTRPValueStr": acpmsTRPValueStr,
       "acpmsTRPMinStr": acpmsTRPMinStr,
       "acpmsTRPMaxStr": acpmsTRPMaxStr,
       "acpmsTRPAvgStr": acpmsTRPAvgStr,
       "acpmsTRPInEventState": acpmsTRPInEventState,
       "acpmsRPPhaseAValueStr": acpmsRPPhaseAValueStr,
       "acpmsRPPhaseBValueStr": acpmsRPPhaseBValueStr,
       "acpmsRPPhaseCValueStr": acpmsRPPhaseCValueStr,
       "acpmsCombined": acpmsCombined,
       "acpmsTPFValueStr": acpmsTPFValueStr,
       "acpmsTPFMinStr": acpmsTPFMinStr,
       "acpmsTPFMaxStr": acpmsTPFMaxStr,
       "acpmsTPFAvgStr": acpmsTPFAvgStr,
       "acpmsTPFInEventState": acpmsTPFInEventState,
       "acpmsPFPhaseAValueStr": acpmsPFPhaseAValueStr,
       "acpmsPFPhaseBValueStr": acpmsPFPhaseBValueStr,
       "acpmsPFPhaseCValueStr": acpmsPFPhaseCValueStr,
       "acpmsTRcPValueStr": acpmsTRcPValueStr,
       "acpmsTRcPMinStr": acpmsTRcPMinStr,
       "acpmsTRcPMaxStr": acpmsTRcPMaxStr,
       "acpmsTRcPAvgStr": acpmsTRcPAvgStr,
       "acpmsRcPPhaseAValueStr": acpmsRcPPhaseAValueStr,
       "acpmsRcPPhaseBValueStr": acpmsRcPPhaseBValueStr,
       "acpmsRcPPhaseCValueStr": acpmsRcPPhaseCValueStr,
       "acpmsTAPValueStr": acpmsTAPValueStr,
       "acpmsTAPMinStr": acpmsTAPMinStr,
       "acpmsTAPMaxStr": acpmsTAPMaxStr,
       "acpmsTAPAvgStr": acpmsTAPAvgStr,
       "acpmsAPPhaseAValueStr": acpmsAPPhaseAValueStr,
       "acpmsAPPhaseBValueStr": acpmsAPPhaseBValueStr,
       "acpmsAPPhaseCValueStr": acpmsAPPhaseCValueStr,
       "acpmsTotalEnergyWh": acpmsTotalEnergyWh,
       "acpmsTotalEnergyVAR": acpmsTotalEnergyVAR,
       "acpmsTotalEnergyVA": acpmsTotalEnergyVA,
       "config": config,
       "eventSensorBasics": eventSensorBasics,
       "esNumberEventSensors": esNumberEventSensors,
       "esTable": esTable,
       "esEntry": esEntry,
       "esIndex": esIndex,
       "esName": esName,
       "esID": esID,
       "esNumberTempSensors": esNumberTempSensors,
       "esTempReportingMode": esTempReportingMode,
       "esNumberCCs": esNumberCCs,
       "esCCReportingMode": esCCReportingMode,
       "esNumberHumidSensors": esNumberHumidSensors,
       "esHumidReportingMode": esHumidReportingMode,
       "esNumberNoiseSensors": esNumberNoiseSensors,
       "esNoiseReportingMode": esNoiseReportingMode,
       "esNumberAirflowSensors": esNumberAirflowSensors,
       "esAirflowReportingMode": esAirflowReportingMode,
       "esNumberAnalog": esNumberAnalog,
       "esAnalogReportingMode": esAnalogReportingMode,
       "esNumberOutputs": esNumberOutputs,
       "esOutputReportingMode": esOutputReportingMode,
       "esTempCombinedStatus": esTempCombinedStatus,
       "esCCCombinedStatusBlock1": esCCCombinedStatusBlock1,
       "esCCCombinedStatusBlock2": esCCCombinedStatusBlock2,
       "esCCCombinedStatusBlock3": esCCCombinedStatusBlock3,
       "esCCCombinedStatusBlock4": esCCCombinedStatusBlock4,
       "esCCCombinedStatusBlock5": esCCCombinedStatusBlock5,
       "esCCCombinedStatusBlock6": esCCCombinedStatusBlock6,
       "esCCCombinedStatusBlock7": esCCCombinedStatusBlock7,
       "esCCCombinedStatusBlock8": esCCCombinedStatusBlock8,
       "esHumidCombinedStatus": esHumidCombinedStatus,
       "esAnalogCombinedStatusBlock1": esAnalogCombinedStatusBlock1,
       "esAnalogCombinedStatusBlock2": esAnalogCombinedStatusBlock2,
       "esAnalogCombinedStatusBlock3": esAnalogCombinedStatusBlock3,
       "esAnalogCombinedStatusBlock4": esAnalogCombinedStatusBlock4,
       "esAnalogCombinedStatusBlock5": esAnalogCombinedStatusBlock5,
       "esAnalogCombinedStatusBlock6": esAnalogCombinedStatusBlock6,
       "esOutputCombinedStatusBlock1": esOutputCombinedStatusBlock1,
       "esOutputCombinedStatusBlock2": esOutputCombinedStatusBlock2,
       "esNewSensors": esNewSensors,
       "eventSensorPointConfig": eventSensorPointConfig,
       "esPointConfigTempTable": esPointConfigTempTable,
       "esPointConfigTempEntry": esPointConfigTempEntry,
       "espcTempIndexES": espcTempIndexES,
       "espcTempIndexPoint": espcTempIndexPoint,
       "espcTempEnable": espcTempEnable,
       "espcTempScale": espcTempScale,
       "espcTempDeadband": espcTempDeadband,
       "espcTempVHighTemp": espcTempVHighTemp,
       "espcTempVHighActions": espcTempVHighActions,
       "espcTempVHighTrapnum": espcTempVHighTrapnum,
       "espcTempVHighClass": espcTempVHighClass,
       "espcTempHighTemp": espcTempHighTemp,
       "espcTempHighActions": espcTempHighActions,
       "espcTempHighTrapnum": espcTempHighTrapnum,
       "espcTempHighClass": espcTempHighClass,
       "espcTempNormalActions": espcTempNormalActions,
       "espcTempNormalTrapnum": espcTempNormalTrapnum,
       "espcTempNormalClass": espcTempNormalClass,
       "espcTempLowTemp": espcTempLowTemp,
       "espcTempLowActions": espcTempLowActions,
       "espcTempLowTrapnum": espcTempLowTrapnum,
       "espcTempLowClass": espcTempLowClass,
       "espcTempVLowTemp": espcTempVLowTemp,
       "espcTempVLowActions": espcTempVLowActions,
       "espcTempVLowTrapnum": espcTempVLowTrapnum,
       "espcTempVLowClass": espcTempVLowClass,
       "esPointConfigCCTable": esPointConfigCCTable,
       "esPointConfigCCEntry": esPointConfigCCEntry,
       "espcCCIndexES": espcCCIndexES,
       "espcCCIndexPoint": espcCCIndexPoint,
       "espcCCEnable": espcCCEnable,
       "espcCCName": espcCCName,
       "espcCCEventState": espcCCEventState,
       "espcCCThreshold": espcCCThreshold,
       "espcCCEventActions": espcCCEventActions,
       "espcCCEventTrapnum": espcCCEventTrapnum,
       "espcCCEventClass": espcCCEventClass,
       "espcCCNormalActions": espcCCNormalActions,
       "espcCCNormalTrapnum": espcCCNormalTrapnum,
       "espcCCNormalClass": espcCCNormalClass,
       "espcCCAlarmAlias": espcCCAlarmAlias,
       "espcCCNormalAlias": espcCCNormalAlias,
       "espcCCNormalThreshold": espcCCNormalThreshold,
       "espcCCOverrideGlobalReminder": espcCCOverrideGlobalReminder,
       "espcCCReminderInterval": espcCCReminderInterval,
       "esPointConfigHumidTable": esPointConfigHumidTable,
       "esPointConfigHumidEntry": esPointConfigHumidEntry,
       "espcHumidIndexES": espcHumidIndexES,
       "espcHumidIndexPoint": espcHumidIndexPoint,
       "espcHumidEnable": espcHumidEnable,
       "espcHumidDeadband": espcHumidDeadband,
       "espcHumidVHighHumid": espcHumidVHighHumid,
       "espcHumidVHighActions": espcHumidVHighActions,
       "espcHumidVHighTrapnum": espcHumidVHighTrapnum,
       "espcHumidVHighClass": espcHumidVHighClass,
       "espcHumidHighHumid": espcHumidHighHumid,
       "espcHumidHighActions": espcHumidHighActions,
       "espcHumidHighTrapnum": espcHumidHighTrapnum,
       "espcHumidHighClass": espcHumidHighClass,
       "espcHumidNormalActions": espcHumidNormalActions,
       "espcHumidNormalTrapnum": espcHumidNormalTrapnum,
       "espcHumidNormalClass": espcHumidNormalClass,
       "espcHumidLowHumid": espcHumidLowHumid,
       "espcHumidLowActions": espcHumidLowActions,
       "espcHumidLowTrapnum": espcHumidLowTrapnum,
       "espcHumidLowClass": espcHumidLowClass,
       "espcHumidVLowHumid": espcHumidVLowHumid,
       "espcHumidVLowActions": espcHumidVLowActions,
       "espcHumidVLowTrapnum": espcHumidVLowTrapnum,
       "espcHumidVLowClass": espcHumidVLowClass,
       "esPointConfigAITable": esPointConfigAITable,
       "esPointConfigAIEntry": esPointConfigAIEntry,
       "espcAIIndexES": espcAIIndexES,
       "espcAIIndexPoint": espcAIIndexPoint,
       "espcAIEnable": espcAIEnable,
       "espcAIDeadband": espcAIDeadband,
       "espcAIVhighValue": espcAIVhighValue,
       "espcAIVhighActions": espcAIVhighActions,
       "espcAIVhighTrapnum": espcAIVhighTrapnum,
       "espcAIVhighClass": espcAIVhighClass,
       "espcAIHighValue": espcAIHighValue,
       "espcAIHighActions": espcAIHighActions,
       "espcAIHighTrapnum": espcAIHighTrapnum,
       "espcAIHighClass": espcAIHighClass,
       "espcAINormalActions": espcAINormalActions,
       "espcAINormalTrapnum": espcAINormalTrapnum,
       "espcAINormalClass": espcAINormalClass,
       "espcAILowValue": espcAILowValue,
       "espcAILowActions": espcAILowActions,
       "espcAILowTrapnum": espcAILowTrapnum,
       "espcAILowClass": espcAILowClass,
       "espcAIVlowValue": espcAIVlowValue,
       "espcAIVlowActions": espcAIVlowActions,
       "espcAIVlowTrapnum": espcAIVlowTrapnum,
       "espcAIVlowClass": espcAIVlowClass,
       "espcAIConvUnitName": espcAIConvUnitName,
       "espcAIConvHighValue": espcAIConvHighValue,
       "espcAIConvHighUnit": espcAIConvHighUnit,
       "espcAIConvLowValue": espcAIConvLowValue,
       "espcAIConvLowUnit": espcAIConvLowUnit,
       "espcAIDisplayFormat": espcAIDisplayFormat,
       "esPointConfigOutputTable": esPointConfigOutputTable,
       "esPointConfigOutputEntry": esPointConfigOutputEntry,
       "espcOutputIndexES": espcOutputIndexES,
       "espcOutputIndexPoint": espcOutputIndexPoint,
       "espcOutputEnable": espcOutputEnable,
       "espcOutputActiveState": espcOutputActiveState,
       "espcOutputType": espcOutputType,
       "espcOutputAliasValue": espcOutputAliasValue,
       "espcOutputAliasColor": espcOutputAliasColor,
       "espcOutputActiveAlias": espcOutputActiveAlias,
       "espcOutputActiveColor": espcOutputActiveColor,
       "espcOutputActiveActions": espcOutputActiveActions,
       "espcOutputActiveTrapnum": espcOutputActiveTrapnum,
       "espcOutputActiveClass": espcOutputActiveClass,
       "espcOutputInactiveAlias": espcOutputInactiveAlias,
       "espcOutputInactiveColor": espcOutputInactiveColor,
       "espcOutputInactiveActions": espcOutputInactiveActions,
       "espcOutputInactiveTrapnum": espcOutputInactiveTrapnum,
       "espcOutputInactiveClass": espcOutputInactiveClass,
       "serialPorts": serialPorts,
       "numberPorts": numberPorts,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigIndex": portConfigIndex,
       "portConfigBaud": portConfigBaud,
       "portConfigDataFormat": portConfigDataFormat,
       "portConfigStripPtOutputLfs": portConfigStripPtOutputLfs,
       "portConfigStripPtInputLfs": portConfigStripPtInputLfs,
       "portConfigMaskEnable": portConfigMaskEnable,
       "portConfigDAEnable": portConfigDAEnable,
       "portConfigStoreAlarmsDPT": portConfigStoreAlarmsDPT,
       "portConfigRecordTimeout": portConfigRecordTimeout,
       "portConfigDataType": portConfigDataType,
       "portConfigEtxToCRLF": portConfigEtxToCRLF,
       "portConfigMLREnable": portConfigMLREnable,
       "portConfigMLRStartField1Pos": portConfigMLRStartField1Pos,
       "portConfigMLRStartField1Text": portConfigMLRStartField1Text,
       "portConfigMLRStartField2Pos": portConfigMLRStartField2Pos,
       "portConfigMLRStartField2Text": portConfigMLRStartField2Text,
       "portConfigMLRNumLinesBefore": portConfigMLRNumLinesBefore,
       "portConfigMLREndDetection": portConfigMLREndDetection,
       "portConfigMLRLineCount": portConfigMLRLineCount,
       "portConfigMLREndField1Pos": portConfigMLREndField1Pos,
       "portConfigMLREndField1Text": portConfigMLREndField1Text,
       "portConfigMLREndField2Pos": portConfigMLREndField2Pos,
       "portConfigMLREndField2Text": portConfigMLREndField2Text,
       "portConfigMLRUseComplexRules": portConfigMLRUseComplexRules,
       "portConfigBufferPT": portConfigBufferPT,
       "portConfigId": portConfigId,
       "portConfigMode": portConfigMode,
       "portConfigHsk": portConfigHsk,
       "network": network,
       "interface": interface,
       "ethernet": ethernet,
       "ethernet1": ethernet1,
       "eth1Mode": eth1Mode,
       "eth1Address": eth1Address,
       "eth1SubnetMask": eth1SubnetMask,
       "eth1Router": eth1Router,
       "eth1VLAN": eth1VLAN,
       "eth1VLAN1": eth1VLAN1,
       "eth1VLAN1ID": eth1VLAN1ID,
       "eth1VLAN1Priority": eth1VLAN1Priority,
       "eth1VLAN1Address": eth1VLAN1Address,
       "eth1VLAN1SubnetMask": eth1VLAN1SubnetMask,
       "eth1VLAN1Router": eth1VLAN1Router,
       "eth1VLAN2": eth1VLAN2,
       "eth1VLAN2ID": eth1VLAN2ID,
       "eth1VLAN2Priority": eth1VLAN2Priority,
       "eth1VLAN2Address": eth1VLAN2Address,
       "eth1VLAN2SubnetMask": eth1VLAN2SubnetMask,
       "eth1VLAN2Router": eth1VLAN2Router,
       "eth1VLAN3": eth1VLAN3,
       "eth1VLAN3ID": eth1VLAN3ID,
       "eth1VLAN3Priority": eth1VLAN3Priority,
       "eth1VLAN3Address": eth1VLAN3Address,
       "eth1VLAN3SubnetMask": eth1VLAN3SubnetMask,
       "eth1VLAN3Router": eth1VLAN3Router,
       "eth1VLAN4": eth1VLAN4,
       "eth1VLAN4ID": eth1VLAN4ID,
       "eth1VLAN4Priority": eth1VLAN4Priority,
       "eth1VLAN4Address": eth1VLAN4Address,
       "eth1VLAN4SubnetMask": eth1VLAN4SubnetMask,
       "eth1VLAN4Router": eth1VLAN4Router,
       "eth1VLAN5": eth1VLAN5,
       "eth1VLAN5ID": eth1VLAN5ID,
       "eth1VLAN5Priority": eth1VLAN5Priority,
       "eth1VLAN5Address": eth1VLAN5Address,
       "eth1VLAN5SubnetMask": eth1VLAN5SubnetMask,
       "eth1VLAN5Router": eth1VLAN5Router,
       "eth1VLAN6": eth1VLAN6,
       "eth1VLAN6ID": eth1VLAN6ID,
       "eth1VLAN6Priority": eth1VLAN6Priority,
       "eth1VLAN6Address": eth1VLAN6Address,
       "eth1VLAN6SubnetMask": eth1VLAN6SubnetMask,
       "eth1VLAN6Router": eth1VLAN6Router,
       "eth1MAC": eth1MAC,
       "eth1IPv6": eth1IPv6,
       "eth1IPv6Mode": eth1IPv6Mode,
       "eth1IPv6Static": eth1IPv6Static,
       "eth1IPv6StaticAddress": eth1IPv6StaticAddress,
       "eth1IPv6StaticRouter": eth1IPv6StaticRouter,
       "eth1IPv6Auto": eth1IPv6Auto,
       "eth1IPv6AutoAddress1": eth1IPv6AutoAddress1,
       "eth1IPv6AutoAddress2": eth1IPv6AutoAddress2,
       "eth1IPv6AutoAddress3": eth1IPv6AutoAddress3,
       "eth1IPv6AutoAddress4": eth1IPv6AutoAddress4,
       "eth1LinkLocalAddress": eth1LinkLocalAddress,
       "ethernet2": ethernet2,
       "eth2Mode": eth2Mode,
       "eth2Address": eth2Address,
       "eth2SubnetMask": eth2SubnetMask,
       "eth2Router": eth2Router,
       "eth2VLAN": eth2VLAN,
       "eth2VLAN1": eth2VLAN1,
       "eth2VLAN1ID": eth2VLAN1ID,
       "eth2VLAN1Priority": eth2VLAN1Priority,
       "eth2VLAN1Address": eth2VLAN1Address,
       "eth2VLAN1SubnetMask": eth2VLAN1SubnetMask,
       "eth2VLAN1Router": eth2VLAN1Router,
       "eth2VLAN2": eth2VLAN2,
       "eth2VLAN2ID": eth2VLAN2ID,
       "eth2VLAN2Priority": eth2VLAN2Priority,
       "eth2VLAN2Address": eth2VLAN2Address,
       "eth2VLAN2SubnetMask": eth2VLAN2SubnetMask,
       "eth2VLAN2Router": eth2VLAN2Router,
       "eth2VLAN3": eth2VLAN3,
       "eth2VLAN3ID": eth2VLAN3ID,
       "eth2VLAN3Priority": eth2VLAN3Priority,
       "eth2VLAN3Address": eth2VLAN3Address,
       "eth2VLAN3SubnetMask": eth2VLAN3SubnetMask,
       "eth2VLAN3Router": eth2VLAN3Router,
       "eth2VLAN4": eth2VLAN4,
       "eth2VLAN4ID": eth2VLAN4ID,
       "eth2VLAN4Priority": eth2VLAN4Priority,
       "eth2VLAN4Address": eth2VLAN4Address,
       "eth2VLAN4SubnetMask": eth2VLAN4SubnetMask,
       "eth2VLAN4Router": eth2VLAN4Router,
       "eth2VLAN5": eth2VLAN5,
       "eth2VLAN5ID": eth2VLAN5ID,
       "eth2VLAN5Priority": eth2VLAN5Priority,
       "eth2VLAN5Address": eth2VLAN5Address,
       "eth2VLAN5SubnetMask": eth2VLAN5SubnetMask,
       "eth2VLAN5Router": eth2VLAN5Router,
       "eth2VLAN6": eth2VLAN6,
       "eth2VLAN6ID": eth2VLAN6ID,
       "eth2VLAN6Priority": eth2VLAN6Priority,
       "eth2VLAN6Address": eth2VLAN6Address,
       "eth2VLAN6SubnetMask": eth2VLAN6SubnetMask,
       "eth2VLAN6Router": eth2VLAN6Router,
       "eth2MAC": eth2MAC,
       "eth2IPv6": eth2IPv6,
       "eth2IPv6Mode": eth2IPv6Mode,
       "eth2IPv6Static": eth2IPv6Static,
       "eth2IPv6StaticAddress": eth2IPv6StaticAddress,
       "eth2IPv6StaticRouter": eth2IPv6StaticRouter,
       "eth2IPv6Auto": eth2IPv6Auto,
       "eth2IPv6AutoAddress1": eth2IPv6AutoAddress1,
       "eth2IPv6AutoAddress2": eth2IPv6AutoAddress2,
       "eth2IPv6AutoAddress3": eth2IPv6AutoAddress3,
       "eth2IPv6AutoAddress4": eth2IPv6AutoAddress4,
       "eth2LinkLocalAddress": eth2LinkLocalAddress,
       "defaultRouter": defaultRouter,
       "dnsTable": dnsTable,
       "dnsEntry": dnsEntry,
       "dnsIndex": dnsIndex,
       "dnsAddress": dnsAddress,
       "hostname": hostname,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostIndex": hostIndex,
       "hostDeclaration": hostDeclaration,
       "ncpDuplex": ncpDuplex,
       "ncpTimeout": ncpTimeout,
       "snmp": snmp,
       "snmpAgentEnable": snmpAgentEnable,
       "snmpNotificationCaptureEnable": snmpNotificationCaptureEnable,
       "snmpNotificationCaptureFile": snmpNotificationCaptureFile,
       "snmpNotificationTx": snmpNotificationTx,
       "snmpNtfnAttempts": snmpNtfnAttempts,
       "snmpNtfnTimeout": snmpNtfnTimeout,
       "snmpNtfnCycles": snmpNtfnCycles,
       "snmpNtfnSnooze": snmpNtfnSnooze,
       "ftpPush": ftpPush,
       "ftpPushEnable": ftpPushEnable,
       "ftpPushServer": ftpPushServer,
       "ftpPushAccount": ftpPushAccount,
       "ftpPushDirectory": ftpPushDirectory,
       "ftpPushperiod": ftpPushperiod,
       "ftpPushPushFileTable": ftpPushPushFileTable,
       "ftpPushPushFileEntry": ftpPushPushFileEntry,
       "ftpPushPushFileIndex": ftpPushPushFileIndex,
       "ftpPushPushFile": ftpPushPushFile,
       "ftpPushPushAudit": ftpPushPushAudit,
       "ftpPushPushAlarms": ftpPushPushAlarms,
       "ftpPushRemoteFileTable": ftpPushRemoteFileTable,
       "ftpPushRemoteFileEntry": ftpPushRemoteFileEntry,
       "ftpPushRemoteFileIndex": ftpPushRemoteFileIndex,
       "ftpPushRemoteFileName": ftpPushRemoteFileName,
       "ftpPushRemoteAlarmName": ftpPushRemoteAlarmName,
       "ftpPushPassive": ftpPushPassive,
       "ftpPushIncludeDate": ftpPushIncludeDate,
       "ftpPushIncludeTime": ftpPushIncludeTime,
       "ftpPushIncludeSeq": ftpPushIncludeSeq,
       "ppp": ppp,
       "pppDial": pppDial,
       "pppDialEnable": pppDialEnable,
       "pppDialNumber": pppDialNumber,
       "pppDialIdleTimeout": pppDialIdleTimeout,
       "pppDialRetries": pppDialRetries,
       "pppDialCDTimeout": pppDialCDTimeout,
       "pppDialLoginTimeout": pppDialLoginTimeout,
       "pppDialMdmInit": pppDialMdmInit,
       "pppDialSuggestIP": pppDialSuggestIP,
       "pppDialPlainLogin": pppDialPlainLogin,
       "pppHost": pppHost,
       "pppHostEnable": pppHostEnable,
       "pppHostIdleTimeout": pppHostIdleTimeout,
       "pppHostLocalIP": pppHostLocalIP,
       "pppHostRemoteIP": pppHostRemoteIP,
       "routing": routing,
       "pppRoutingEnable": pppRoutingEnable,
       "ethRoutingEnable": ethRoutingEnable,
       "ethRoutingNATEnable": ethRoutingNATEnable,
       "routingInterface": routingInterface,
       "eth2WanRoutingEnable": eth2WanRoutingEnable,
       "netSecurity": netSecurity,
       "ipRestriction": ipRestriction,
       "ipRestrictionTable": ipRestrictionTable,
       "ipRestrictionEntry": ipRestrictionEntry,
       "ipRestrictionIndex": ipRestrictionIndex,
       "ipRestrictionEnable": ipRestrictionEnable,
       "ipRestrictionMask": ipRestrictionMask,
       "rts": rts,
       "rtsFileTable": rtsFileTable,
       "rtsFileEntry": rtsFileEntry,
       "rtsFileIndex": rtsFileIndex,
       "rtsFileMode": rtsFileMode,
       "rtsFileShowAnswer": rtsFileShowAnswer,
       "rtsFileReqXON": rtsFileReqXON,
       "rtsFileTimeout": rtsFileTimeout,
       "rtsFileEmptyClose": rtsFileEmptyClose,
       "rtsFilePushHost": rtsFilePushHost,
       "rtsFilePushPort": rtsFilePushPort,
       "rtsFilePushRetryTimer": rtsFilePushRetryTimer,
       "rtsAlarms": rtsAlarms,
       "rtsAlarmsMode": rtsAlarmsMode,
       "rtsAlarmsShowAnswer": rtsAlarmsShowAnswer,
       "rtsAlarmsReqXON": rtsAlarmsReqXON,
       "rtsAlarmsTimeout": rtsAlarmsTimeout,
       "rtsAlarmsEmptyClose": rtsAlarmsEmptyClose,
       "rtsAlarmsPushHost": rtsAlarmsPushHost,
       "rtsAlarmsPushPort": rtsAlarmsPushPort,
       "rtsAlarmsPushRetryTimer": rtsAlarmsPushRetryTimer,
       "trap": trap,
       "trapInclude": trapInclude,
       "trapIncludeDateTime": trapIncludeDateTime,
       "trapIncludeSiteName": trapIncludeSiteName,
       "trapIncludeSensorID": trapIncludeSensorID,
       "trapIncludeUDName": trapIncludeUDName,
       "trapIncludeUDState": trapIncludeUDState,
       "trapIncludeSourceAddress": trapIncludeSourceAddress,
       "trapAuthFailEnable": trapAuthFailEnable,
       "routeTest": routeTest,
       "routeTestEnable": routeTestEnable,
       "routeTestPeriod": routeTestPeriod,
       "routeTestAddressTable": routeTestAddressTable,
       "routeTestAddressEntry": routeTestAddressEntry,
       "routeTestAddressIndex": routeTestAddressIndex,
       "routeTestAddress": routeTestAddress,
       "wireless": wireless,
       "wirelessMode": wirelessMode,
       "wirelessAPN": wirelessAPN,
       "wirelessIdleTimeout": wirelessIdleTimeout,
       "wirelessPIN": wirelessPIN,
       "wirelessDRE": wirelessDRE,
       "wirelessPPPUsername": wirelessPPPUsername,
       "wirelessFirewall": wirelessFirewall,
       "wirelessKeepaliveThreshold": wirelessKeepaliveThreshold,
       "wirelessPPPDebug": wirelessPPPDebug,
       "wirelessConnectivity": wirelessConnectivity,
       "wirelessConnEnable": wirelessConnEnable,
       "wirelessConnCheckInterval": wirelessConnCheckInterval,
       "wirelessConnFailThreshold": wirelessConnFailThreshold,
       "wirelessConnIP1": wirelessConnIP1,
       "wirelessConnIP2": wirelessConnIP2,
       "email": email,
       "emailServer": emailServer,
       "emailDomain": emailDomain,
       "emailAuthEnable": emailAuthEnable,
       "netAdvanced": netAdvanced,
       "arpFilter": arpFilter,
       "web": web,
       "webEnable": webEnable,
       "webPort": webPort,
       "webTimeout": webTimeout,
       "ethExpan": ethExpan,
       "ethExpanIp": ethExpanIp,
       "ethExpanMask": ethExpanMask,
       "ethExpanCardTable": ethExpanCardTable,
       "ethExpanCardEntry": ethExpanCardEntry,
       "ethExpanCardIndex": ethExpanCardIndex,
       "ethExpanCardMAC": ethExpanCardMAC,
       "ethExpanDHCP": ethExpanDHCP,
       "ethExpanDHCPStartIp": ethExpanDHCPStartIp,
       "ethExpanDHCPLeaseTime": ethExpanDHCPLeaseTime,
       "ipv6": ipv6,
       "ipv6DefaultRouter": ipv6DefaultRouter,
       "cpe": cpe,
       "cpeTable": cpeTable,
       "cpeEntry": cpeEntry,
       "cpeIndex": cpeIndex,
       "cpeHost": cpeHost,
       "cpeName": cpeName,
       "cpeDescription": cpeDescription,
       "cpeKeepalive": cpeKeepalive,
       "cpeThreshold": cpeThreshold,
       "cpeEventReminderInterval": cpeEventReminderInterval,
       "cpeKeepaliveTicks": cpeKeepaliveTicks,
       "cpePingSize": cpePingSize,
       "cpeInfoReset": cpeInfoReset,
       "cpeInfoNumReq": cpeInfoNumReq,
       "cpeInfoNumGoodResp": cpeInfoNumGoodResp,
       "cpeInfoNumBadResp": cpeInfoNumBadResp,
       "cpeInfoNumLostResp": cpeInfoNumLostResp,
       "cpeInfoPercentLoss": cpeInfoPercentLoss,
       "cpeInfoPercentBad": cpeInfoPercentBad,
       "modem": modem,
       "modemFormat": modemFormat,
       "modemInitString": modemInitString,
       "modemCallAttempts": modemCallAttempts,
       "modemCallDelay": modemCallDelay,
       "modemCmdTimout": modemCmdTimout,
       "modemGoto": modemGoto,
       "modemClid": modemClid,
       "modemCLIDEnable": modemCLIDEnable,
       "modemCLIDNumberTable": modemCLIDNumberTable,
       "modemCLIDNumberEntry": modemCLIDNumberEntry,
       "modemCLIDNumberIndex": modemCLIDNumberIndex,
       "modemCLIDNumber": modemCLIDNumber,
       "modemTAPInitString": modemTAPInitString,
       "modemTAP8N1": modemTAP8N1,
       "time": time,
       "clock": clock,
       "console": console,
       "consoleDuplex": consoleDuplex,
       "consoleTimeout": consoleTimeout,
       "consoleBaud": consoleBaud,
       "consoleFormat": consoleFormat,
       "consoleHsk": consoleHsk,
       "consoleConfirm": consoleConfirm,
       "unitSecurity": unitSecurity,
       "secCore": secCore,
       "scShowPasswordPrompt": scShowPasswordPrompt,
       "scConsoleLoginRequired": scConsoleLoginRequired,
       "scModemLoginRequired": scModemLoginRequired,
       "scTelnetLoginRequired": scTelnetLoginRequired,
       "scTelnetPTLoginRequired": scTelnetPTLoginRequired,
       "scRTSLoginRequired": scRTSLoginRequired,
       "scAuthMode": scAuthMode,
       "scRightsGroup": scRightsGroup,
       "scSecret": scSecret,
       "secUserTable": secUserTable,
       "secUserEntry": secUserEntry,
       "secUserIndex": secUserIndex,
       "secUserEnable": secUserEnable,
       "secUserConnectVia": secUserConnectVia,
       "secUserLoginTo": secUserLoginTo,
       "secUserAccessFile": secUserAccessFile,
       "secUserPTEscapeTo": secUserPTEscapeTo,
       "secUserPPPType": secUserPPPType,
       "secUserRights": secUserRights,
       "secUserEventsReadAccess": secUserEventsReadAccess,
       "secUserAuditReadAccess": secUserAuditReadAccess,
       "secUserEventsWriteAccess": secUserEventsWriteAccess,
       "secUserAuditWriteAccess": secUserAuditWriteAccess,
       "secUserExpiration": secUserExpiration,
       "secUserCallbackNumber1": secUserCallbackNumber1,
       "secUserCallbackNumber2": secUserCallbackNumber2,
       "secUserCallbackNumber3": secUserCallbackNumber3,
       "secUserChallengeTelnetMode": secUserChallengeTelnetMode,
       "secUserChallengeModemMode": secUserChallengeModemMode,
       "secUserChallengeConsoleMode": secUserChallengeConsoleMode,
       "secUserChallengeTelnetSendTo": secUserChallengeTelnetSendTo,
       "secUserChallengeModemSendTo": secUserChallengeModemSendTo,
       "secUserChallengeExpiration": secUserChallengeExpiration,
       "secFactory": secFactory,
       "sfEnable": sfEnable,
       "sfSecret": sfSecret,
       "secSSH": secSSH,
       "secVPN": secVPN,
       "event": event,
       "evCore": evCore,
       "evClassNameTable": evClassNameTable,
       "evClassNameEntry": evClassNameEntry,
       "evClassNameIndex": evClassNameIndex,
       "evClassName": evClassName,
       "evReminderInterval": evReminderInterval,
       "evLog": evLog,
       "evLogEnable": evLogEnable,
       "evLogStoreAlarm": evLogStoreAlarm,
       "evLogMaxSize": evLogMaxSize,
       "evLogStoreSensor": evLogStoreSensor,
       "evLogTimeStampAlarms": evLogTimeStampAlarms,
       "evLogPrependName": evLogPrependName,
       "evMgmt": evMgmt,
       "evMgmtReprocess": evMgmtReprocess,
       "evData": evData,
       "evdCore": evdCore,
       "evdExitOnTrue": evdExitOnTrue,
       "evdFilterAction": evdFilterAction,
       "evdWildCardChar": evdWildCardChar,
       "evdTable": evdTable,
       "evdEntry": evdEntry,
       "evdIndex": evdIndex,
       "evdEnable": evdEnable,
       "evdName": evdName,
       "evdEquation": evdEquation,
       "evdThreshold": evdThreshold,
       "evdAutoClear": evdAutoClear,
       "evdClearInterval": evdClearInterval,
       "evdClearTime": evdClearTime,
       "evdActions": evdActions,
       "evdClass": evdClass,
       "evdTrapNum": evdTrapNum,
       "evdMode": evdMode,
       "evdFieldTable": evdFieldTable,
       "evdFieldEntry": evdFieldEntry,
       "evdFieldIndex": evdFieldIndex,
       "evdFieldStart": evdFieldStart,
       "evdFieldLength": evdFieldLength,
       "evdFieldName": evdFieldName,
       "evdFieldLine": evdFieldLine,
       "evdFieldType": evdFieldType,
       "evdMacroTable": evdMacroTable,
       "evdMacroEntry": evdMacroEntry,
       "evdMacroIndex": evdMacroIndex,
       "evdMacroName": evdMacroName,
       "evdMacroEquation": evdMacroEquation,
       "evNoData1": evNoData1,
       "evNoData1Enable": evNoData1Enable,
       "evNoData1Actions": evNoData1Actions,
       "evNoData1Message": evNoData1Message,
       "evNoData1TrapNum": evNoData1TrapNum,
       "evNoData1Class": evNoData1Class,
       "evNoData1Sched1Begin": evNoData1Sched1Begin,
       "evNoData1Sched1End": evNoData1Sched1End,
       "evNoData1Sched1Duration": evNoData1Sched1Duration,
       "evNoData1Sched2Begin": evNoData1Sched2Begin,
       "evNoData1Sched2End": evNoData1Sched2End,
       "evNoData1Sched2Duration": evNoData1Sched2Duration,
       "evNoData1PortEnableTable": evNoData1PortEnableTable,
       "evNoData1PortEnableEntry": evNoData1PortEnableEntry,
       "evNoData1PortEnableIndex": evNoData1PortEnableIndex,
       "evNoData1PortEnable": evNoData1PortEnable,
       "evNoData1Exclusions": evNoData1Exclusions,
       "evNoData1Days": evNoData1Days,
       "evNoData2": evNoData2,
       "evNoData2Enable": evNoData2Enable,
       "evNoData2Actions": evNoData2Actions,
       "evNoData2Message": evNoData2Message,
       "evNoData2TrapNum": evNoData2TrapNum,
       "evNoData2Class": evNoData2Class,
       "evNoData2Sched1Begin": evNoData2Sched1Begin,
       "evNoData2Sched1End": evNoData2Sched1End,
       "evNoData2Sched1Duration": evNoData2Sched1Duration,
       "evNoData2Sched2Begin": evNoData2Sched2Begin,
       "evNoData2Sched2End": evNoData2Sched2End,
       "evNoData2Sched2Duration": evNoData2Sched2Duration,
       "evNoData2PortEnableTable": evNoData2PortEnableTable,
       "evNoData2PortEnableEntry": evNoData2PortEnableEntry,
       "evNoData2PortEnableIndex": evNoData2PortEnableIndex,
       "evNoData2PortEnable": evNoData2PortEnable,
       "evNoData2Exclusions": evNoData2Exclusions,
       "evNoData2Days": evNoData2Days,
       "evSched1": evSched1,
       "evSched1Enable": evSched1Enable,
       "evSched1Actions": evSched1Actions,
       "evSched1Message": evSched1Message,
       "evSched1TrapNum": evSched1TrapNum,
       "evSched1Class": evSched1Class,
       "evSched1Sunday": evSched1Sunday,
       "evSched1Monday": evSched1Monday,
       "evSched1Tuesday": evSched1Tuesday,
       "evSched1Wednesday": evSched1Wednesday,
       "evSched1Thursday": evSched1Thursday,
       "evSched1Friday": evSched1Friday,
       "evSched1Saturday": evSched1Saturday,
       "evSched1Exclusions": evSched1Exclusions,
       "evSched2": evSched2,
       "evSched2Enable": evSched2Enable,
       "evSched2Actions": evSched2Actions,
       "evSched2Message": evSched2Message,
       "evSched2TrapNum": evSched2TrapNum,
       "evSched2Class": evSched2Class,
       "evSched2Sunday": evSched2Sunday,
       "evSched2Monday": evSched2Monday,
       "evSched2Tuesday": evSched2Tuesday,
       "evSched2Wednesday": evSched2Wednesday,
       "evSched2Thursday": evSched2Thursday,
       "evSched2Friday": evSched2Friday,
       "evSched2Saturday": evSched2Saturday,
       "evSched2Exclusions": evSched2Exclusions,
       "evShskLowTable": evShskLowTable,
       "evShskLowEntry": evShskLowEntry,
       "evShskLowIndex": evShskLowIndex,
       "evShskLowEnable": evShskLowEnable,
       "evShskLowActions": evShskLowActions,
       "evShskLowMessage": evShskLowMessage,
       "evShskLowClass": evShskLowClass,
       "evShskLowTrapNum": evShskLowTrapNum,
       "evShskHighTable": evShskHighTable,
       "evShskHighEntry": evShskHighEntry,
       "evShskHighIndex": evShskHighIndex,
       "evShskHighEnable": evShskHighEnable,
       "evShskHighActions": evShskHighActions,
       "evShskHighMessage": evShskHighMessage,
       "evShskHighClass": evShskHighClass,
       "evShskHighTrapNum": evShskHighTrapNum,
       "evNoSensor": evNoSensor,
       "evNoSensorTimeout": evNoSensorTimeout,
       "evNoSensorActions": evNoSensorActions,
       "evNoSensorTrapNum": evNoSensorTrapNum,
       "evNoSensorClass": evNoSensorClass,
       "fuelSensor": fuelSensor,
       "fuelSensorGeneralTable": fuelSensorGeneralTable,
       "fsGenEntry": fsGenEntry,
       "fsGenIndex": fsGenIndex,
       "fsGenName": fsGenName,
       "fsGenSensorType": fsGenSensorType,
       "fsGenDistanceUnit": fsGenDistanceUnit,
       "fsGenRawValueTop": fsGenRawValueTop,
       "fsGenTopOffset": fsGenTopOffset,
       "fsGenRawValueBottom": fsGenRawValueBottom,
       "fsGenBottomOffset": fsGenBottomOffset,
       "fsGenInputES": fsGenInputES,
       "fsGenInputPoint": fsGenInputPoint,
       "fsGenFilterAveraging": fsGenFilterAveraging,
       "fsGenSysrepEnable": fsGenSysrepEnable,
       "fsGenSysrepThreshold": fsGenSysrepThreshold,
       "fsGenSysrepLimit": fsGenSysrepLimit,
       "fsGenSysrepPackage": fsGenSysrepPackage,
       "fsGenSysrepType": fsGenSysrepType,
       "fuelSensorTankTable": fuelSensorTankTable,
       "fsTankEntry": fsTankEntry,
       "fsTankIndex": fsTankIndex,
       "fsTankHeight": fsTankHeight,
       "fsTankDimA": fsTankDimA,
       "fsTankDimB": fsTankDimB,
       "fsTankVolume": fsTankVolume,
       "fsTankVolumeUnit": fsTankVolumeUnit,
       "fsTankShape": fsTankShape,
       "fuelSensorCustomTankTable": fuelSensorCustomTankTable,
       "fsCustomTankEntry": fsCustomTankEntry,
       "fsCustomTankIndexFS": fsCustomTankIndexFS,
       "fsCustomTankIndexDatum": fsCustomTankIndexDatum,
       "fsCustomTankHeight": fsCustomTankHeight,
       "fsCustomTankVolume": fsCustomTankVolume,
       "fuelSensorVolumeTable": fuelSensorVolumeTable,
       "fsVolumeEntry": fsVolumeEntry,
       "fsVolumeIndex": fsVolumeIndex,
       "fsVolumeEnable": fsVolumeEnable,
       "fsVolumeDeadband": fsVolumeDeadband,
       "fsVolumeVHighValue": fsVolumeVHighValue,
       "fsVolumeVHighActions": fsVolumeVHighActions,
       "fsVolumeVHighTrapNum": fsVolumeVHighTrapNum,
       "fsVolumeVHighClass": fsVolumeVHighClass,
       "fsVolumeHighValue": fsVolumeHighValue,
       "fsVolumeHighActions": fsVolumeHighActions,
       "fsVolumeHighTrapNum": fsVolumeHighTrapNum,
       "fsVolumeHighClass": fsVolumeHighClass,
       "fsVolumeNormalActions": fsVolumeNormalActions,
       "fsVolumeNormalTrapNum": fsVolumeNormalTrapNum,
       "fsVolumeNormalClass": fsVolumeNormalClass,
       "fsVolumeLowValue": fsVolumeLowValue,
       "fsVolumeLowActions": fsVolumeLowActions,
       "fsVolumeLowTrapNum": fsVolumeLowTrapNum,
       "fsVolumeLowClass": fsVolumeLowClass,
       "fsVolumeVLowValue": fsVolumeVLowValue,
       "fsVolumeVLowActions": fsVolumeVLowActions,
       "fsVolumeVLowTrapNum": fsVolumeVLowTrapNum,
       "fsVolumeVLowClass": fsVolumeVLowClass,
       "fuelSensorDisconnectTable": fuelSensorDisconnectTable,
       "fsDiscEntry": fsDiscEntry,
       "fsDiscIndex": fsDiscIndex,
       "fsDiscEnable": fsDiscEnable,
       "fsDiscHighValue": fsDiscHighValue,
       "fsDiscLowValue": fsDiscLowValue,
       "fsDiscActions": fsDiscActions,
       "fsDiscTrapNum": fsDiscTrapNum,
       "fsDiscClass": fsDiscClass,
       "fsDiscNormalActions": fsDiscNormalActions,
       "fsDiscNormalTrapNum": fsDiscNormalTrapNum,
       "fsDiscNormalClass": fsDiscNormalClass,
       "acPowerMonitor": acPowerMonitor,
       "acpmGeneralTable": acpmGeneralTable,
       "acpmGenEntry": acpmGenEntry,
       "acpmGenIndex": acpmGenIndex,
       "acpmGenDevice": acpmGenDevice,
       "acpmGenName": acpmGenName,
       "acpmGenAddress": acpmGenAddress,
       "acpmGenPtRatio": acpmGenPtRatio,
       "acpmGenCtRatio": acpmGenCtRatio,
       "acpmGenPowerType": acpmGenPowerType,
       "acpmGenSysrepPackage": acpmGenSysrepPackage,
       "acpmGenSysrepType": acpmGenSysrepType,
       "acpmGenEnable": acpmGenEnable,
       "acpmAvgVoltageTable": acpmAvgVoltageTable,
       "acpmAvgVoltageEntry": acpmAvgVoltageEntry,
       "acpmAvgVoltageIndex": acpmAvgVoltageIndex,
       "acpmAvgVoltageEnable": acpmAvgVoltageEnable,
       "acpmAvgVoltageDeadband": acpmAvgVoltageDeadband,
       "acpmAvgVoltageVHighValue": acpmAvgVoltageVHighValue,
       "acpmAvgVoltageVHighActions": acpmAvgVoltageVHighActions,
       "acpmAvgVoltageVHighTrapNum": acpmAvgVoltageVHighTrapNum,
       "acpmAvgVoltageVHighClass": acpmAvgVoltageVHighClass,
       "acpmAvgVoltageHighValue": acpmAvgVoltageHighValue,
       "acpmAvgVoltageHighActions": acpmAvgVoltageHighActions,
       "acpmAvgVoltageHighTrapNum": acpmAvgVoltageHighTrapNum,
       "acpmAvgVoltageHighClass": acpmAvgVoltageHighClass,
       "acpmAvgVoltageNormalActions": acpmAvgVoltageNormalActions,
       "acpmAvgVoltageNormalTrapNum": acpmAvgVoltageNormalTrapNum,
       "acpmAvgVoltageNormalClass": acpmAvgVoltageNormalClass,
       "acpmAvgVoltageLowValue": acpmAvgVoltageLowValue,
       "acpmAvgVoltageLowActions": acpmAvgVoltageLowActions,
       "acpmAvgVoltageLowTrapNum": acpmAvgVoltageLowTrapNum,
       "acpmAvgVoltageLowClass": acpmAvgVoltageLowClass,
       "acpmAvgVoltageVLowValue": acpmAvgVoltageVLowValue,
       "acpmAvgVoltageVLowActions": acpmAvgVoltageVLowActions,
       "acpmAvgVoltageVLowTrapNum": acpmAvgVoltageVLowTrapNum,
       "acpmAvgVoltageVLowClass": acpmAvgVoltageVLowClass,
       "acpmAvgVoltageSysrepEnable": acpmAvgVoltageSysrepEnable,
       "acpmAvgVoltageSysrepThreshold": acpmAvgVoltageSysrepThreshold,
       "acpmAvgVoltageSysrepLimit": acpmAvgVoltageSysrepLimit,
       "acpmAvgCurrentTable": acpmAvgCurrentTable,
       "acpmAvgCurrentEntry": acpmAvgCurrentEntry,
       "acpmAvgCurrentIndex": acpmAvgCurrentIndex,
       "acpmAvgCurrentEnable": acpmAvgCurrentEnable,
       "acpmAvgCurrentDeadband": acpmAvgCurrentDeadband,
       "acpmAvgCurrentVHighValue": acpmAvgCurrentVHighValue,
       "acpmAvgCurrentVHighActions": acpmAvgCurrentVHighActions,
       "acpmAvgCurrentVHighTrapNum": acpmAvgCurrentVHighTrapNum,
       "acpmAvgCurrentVHighClass": acpmAvgCurrentVHighClass,
       "acpmAvgCurrentHighValue": acpmAvgCurrentHighValue,
       "acpmAvgCurrentHighActions": acpmAvgCurrentHighActions,
       "acpmAvgCurrentHighTrapNum": acpmAvgCurrentHighTrapNum,
       "acpmAvgCurrentHighClass": acpmAvgCurrentHighClass,
       "acpmAvgCurrentNormalActions": acpmAvgCurrentNormalActions,
       "acpmAvgCurrentNormalTrapNum": acpmAvgCurrentNormalTrapNum,
       "acpmAvgCurrentNormalClass": acpmAvgCurrentNormalClass,
       "acpmAvgCurrentLowValue": acpmAvgCurrentLowValue,
       "acpmAvgCurrentLowActions": acpmAvgCurrentLowActions,
       "acpmAvgCurrentLowTrapNum": acpmAvgCurrentLowTrapNum,
       "acpmAvgCurrentLowClass": acpmAvgCurrentLowClass,
       "acpmAvgCurrentVLowValue": acpmAvgCurrentVLowValue,
       "acpmAvgCurrentVLowActions": acpmAvgCurrentVLowActions,
       "acpmAvgCurrentVLowTrapNum": acpmAvgCurrentVLowTrapNum,
       "acpmAvgCurrentVLowClass": acpmAvgCurrentVLowClass,
       "acpmAvgCurrentSysrepEnable": acpmAvgCurrentSysrepEnable,
       "acpmAvgCurrentSysrepThreshold": acpmAvgCurrentSysrepThreshold,
       "acpmAvgCurrentSysrepLimit": acpmAvgCurrentSysrepLimit,
       "acpmFreqTable": acpmFreqTable,
       "acpmFreqEntry": acpmFreqEntry,
       "acpmFreqIndex": acpmFreqIndex,
       "acpmFreqEnable": acpmFreqEnable,
       "acpmFreqDeadband": acpmFreqDeadband,
       "acpmFreqVHighValue": acpmFreqVHighValue,
       "acpmFreqVHighActions": acpmFreqVHighActions,
       "acpmFreqVHighTrapNum": acpmFreqVHighTrapNum,
       "acpmFreqVHighClass": acpmFreqVHighClass,
       "acpmFreqHighValue": acpmFreqHighValue,
       "acpmFreqHighActions": acpmFreqHighActions,
       "acpmFreqHighTrapNum": acpmFreqHighTrapNum,
       "acpmFreqHighClass": acpmFreqHighClass,
       "acpmFreqNormalActions": acpmFreqNormalActions,
       "acpmFreqNormalTrapNum": acpmFreqNormalTrapNum,
       "acpmFreqNormalClass": acpmFreqNormalClass,
       "acpmFreqLowValue": acpmFreqLowValue,
       "acpmFreqLowActions": acpmFreqLowActions,
       "acpmFreqLowTrapNum": acpmFreqLowTrapNum,
       "acpmFreqLowClass": acpmFreqLowClass,
       "acpmFreqVLowValue": acpmFreqVLowValue,
       "acpmFreqVLowActions": acpmFreqVLowActions,
       "acpmFreqVLowTrapNum": acpmFreqVLowTrapNum,
       "acpmFreqVLowClass": acpmFreqVLowClass,
       "acpmFreqSysrepEnable": acpmFreqSysrepEnable,
       "acpmFreqSysrepThreshold": acpmFreqSysrepThreshold,
       "acpmFreqSysrepLimit": acpmFreqSysrepLimit,
       "acpmTotalRealPowerTable": acpmTotalRealPowerTable,
       "acpmTRPEntry": acpmTRPEntry,
       "acpmTRPIndex": acpmTRPIndex,
       "acpmTRPEnable": acpmTRPEnable,
       "acpmTRPDeadband": acpmTRPDeadband,
       "acpmTRPVHighValue": acpmTRPVHighValue,
       "acpmTRPVHighActions": acpmTRPVHighActions,
       "acpmTRPVHighTrapNum": acpmTRPVHighTrapNum,
       "acpmTRPVHighClass": acpmTRPVHighClass,
       "acpmTRPHighValue": acpmTRPHighValue,
       "acpmTRPHighActions": acpmTRPHighActions,
       "acpmTRPHighTrapNum": acpmTRPHighTrapNum,
       "acpmTRPHighClass": acpmTRPHighClass,
       "acpmTRPNormalActions": acpmTRPNormalActions,
       "acpmTRPNormalTrapNum": acpmTRPNormalTrapNum,
       "acpmTRPNormalClass": acpmTRPNormalClass,
       "acpmTRPLowValue": acpmTRPLowValue,
       "acpmTRPLowActions": acpmTRPLowActions,
       "acpmTRPLowTrapNum": acpmTRPLowTrapNum,
       "acpmTRPLowClass": acpmTRPLowClass,
       "acpmTRPVLowValue": acpmTRPVLowValue,
       "acpmTRPVLowActions": acpmTRPVLowActions,
       "acpmTRPVLowTrapNum": acpmTRPVLowTrapNum,
       "acpmTRPVLowClass": acpmTRPVLowClass,
       "acpmTRPSysrepEnable": acpmTRPSysrepEnable,
       "acpmTRPSysrepThreshold": acpmTRPSysrepThreshold,
       "acpmTRPSysrepLimit": acpmTRPSysrepLimit,
       "acpmDisconnectTable": acpmDisconnectTable,
       "acpmDisconnectEntry": acpmDisconnectEntry,
       "acpmDisconnectIndex": acpmDisconnectIndex,
       "acpmDisconnectEnable": acpmDisconnectEnable,
       "acpmDisconnectActions": acpmDisconnectActions,
       "acpmDisconnectTrapNum": acpmDisconnectTrapNum,
       "acpmDisconnectClass": acpmDisconnectClass,
       "acpmDisconnectNormalActions": acpmDisconnectNormalActions,
       "acpmDisconnectNormalTrapNum": acpmDisconnectNormalTrapNum,
       "acpmDisconnectNormalClass": acpmDisconnectNormalClass,
       "acpmTotalPowerFactorTable": acpmTotalPowerFactorTable,
       "acpmTPFEntry": acpmTPFEntry,
       "acpmTPFIndex": acpmTPFIndex,
       "acpmTPFEnable": acpmTPFEnable,
       "acpmTPFDeadband": acpmTPFDeadband,
       "acpmTPFNormalActions": acpmTPFNormalActions,
       "acpmTPFNormalTrapNum": acpmTPFNormalTrapNum,
       "acpmTPFNormalClass": acpmTPFNormalClass,
       "acpmTPFLowValue": acpmTPFLowValue,
       "acpmTPFLowActions": acpmTPFLowActions,
       "acpmTPFLowTrapNum": acpmTPFLowTrapNum,
       "acpmTPFLowClass": acpmTPFLowClass,
       "acpmTPFVLowValue": acpmTPFVLowValue,
       "acpmTPFVLowActions": acpmTPFVLowActions,
       "acpmTPFVLowTrapNum": acpmTPFVLowTrapNum,
       "acpmTPFVLowClass": acpmTPFVLowClass,
       "acpmTPFSysrepEnable": acpmTPFSysrepEnable,
       "acpmTPFSysrepThreshold": acpmTPFSysrepThreshold,
       "acpmTPFSysrepLimit": acpmTPFSysrepLimit,
       "evReset": evReset,
       "evResetEnable": evResetEnable,
       "evResetDelay": evResetDelay,
       "evResetActions": evResetActions,
       "evResetMessage": evResetMessage,
       "evResetTrapnum": evResetTrapnum,
       "evResetClass": evResetClass,
       "action": action,
       "actionCallNumberTable": actionCallNumberTable,
       "actionCallNumberEntry": actionCallNumberEntry,
       "actionCallNumberIndex": actionCallNumberIndex,
       "actionCallNumber": actionCallNumber,
       "actionPagerTable": actionPagerTable,
       "actionPagerEntry": actionPagerEntry,
       "actionPagerIndex": actionPagerIndex,
       "actionPagerType": actionPagerType,
       "actionPagerNumber": actionPagerNumber,
       "actionPagerID": actionPagerID,
       "actionPagerMessage": actionPagerMessage,
       "actionPagerPostCalloutDelay": actionPagerPostCalloutDelay,
       "actionPagerPostIDDelay": actionPagerPostIDDelay,
       "actionSched": actionSched,
       "actionSchedEnable": actionSchedEnable,
       "actionSchedBegin": actionSchedBegin,
       "actionSchedEnd": actionSchedEnd,
       "actionSchedWeekdaysOnly": actionSchedWeekdaysOnly,
       "actionAsentria": actionAsentria,
       "actionAsentriaRequireAck": actionAsentriaRequireAck,
       "actionAsentriaVersion": actionAsentriaVersion,
       "actionAsentriaTCPPort": actionAsentriaTCPPort,
       "actionHostTable": actionHostTable,
       "actionHostEntry": actionHostEntry,
       "actionHostIndex": actionHostIndex,
       "actionHost": actionHost,
       "actionEmailTable": actionEmailTable,
       "actionEmailEntry": actionEmailEntry,
       "actionEmailIndex": actionEmailIndex,
       "actionEmail": actionEmail,
       "actionParseError": actionParseError,
       "sys": sys,
       "sysTime": sysTime,
       "sysTimeAutoDST": sysTimeAutoDST,
       "sysTimeGMTOffset": sysTimeGMTOffset,
       "sysTimeGMTDirection": sysTimeGMTDirection,
       "sysTimeNet": sysTimeNet,
       "sysTimeNetEnable": sysTimeNetEnable,
       "sysTimeNetHostTable": sysTimeNetHostTable,
       "sysTimeNetHostEntry": sysTimeNetHostEntry,
       "sysTimeNetHostIndex": sysTimeNetHostIndex,
       "sysTimeNetHost": sysTimeNetHost,
       "sysPT": sysPT,
       "sysPTTimeout": sysPTTimeout,
       "sysPTEndPause": sysPTEndPause,
       "sysPTJoinable": sysPTJoinable,
       "sysMTU": sysMTU,
       "sysAnswerString": sysAnswerString,
       "sysEventFileID": sysEventFileID,
       "sysEscapeCharacter": sysEscapeCharacter,
       "sysTimeStamp": sysTimeStamp,
       "sysTimeStampTimeFormat": sysTimeStampTimeFormat,
       "sysTimeStampDateFormat": sysTimeStampDateFormat,
       "sysTimeStampSpaceAfter": sysTimeStampSpaceAfter,
       "sysLog": sysLog,
       "sysLogMode": sysLogMode,
       "sysLoghost": sysLoghost,
       "sysLogFilter": sysLogFilter,
       "sysLogFileSize": sysLogFileSize,
       "sysLogFileCount": sysLogFileCount,
       "sysLogListenPort": sysLogListenPort,
       "sysCRDB": sysCRDB,
       "sysCRDBCapacity": sysCRDBCapacity,
       "sysCRDBPercentFull": sysCRDBPercentFull,
       "sysCRDBFileIDTable": sysCRDBFileIDTable,
       "sysCRDBFileIDEntry": sysCRDBFileIDEntry,
       "sysCRDBFileIDIndex": sysCRDBFileIDIndex,
       "sysCRDBFileID": sysCRDBFileID,
       "sysCRDBFileEnforceMinTable": sysCRDBFileEnforceMinTable,
       "sysCRDBFileEnforceMinEntry": sysCRDBFileEnforceMinEntry,
       "sysCRDBFileEnforceMinIndex": sysCRDBFileEnforceMinIndex,
       "sysCRDBFileEnforceMin": sysCRDBFileEnforceMin,
       "sysCharMask": sysCharMask,
       "sysPrompt": sysPrompt,
       "sysBootStatus": sysBootStatus,
       "sysLoc": sysLoc,
       "sysLocLatitude": sysLocLatitude,
       "sysLocLongitude": sysLocLongitude,
       "sysLocXOffset": sysLocXOffset,
       "sysLocYOffset": sysLocYOffset,
       "sysLocAngle": sysLocAngle,
       "sysLocAltitude": sysLocAltitude,
       "sysAssetMgmt": sysAssetMgmt,
       "sysAMManufacturer": sysAMManufacturer,
       "sysAMProduct": sysAMProduct,
       "sysAMSerialNumber": sysAMSerialNumber,
       "sysAMHardwareOptions": sysAMHardwareOptions,
       "sysAMSoftwareVersion": sysAMSoftwareVersion,
       "sysAMSiteName": sysAMSiteName,
       "auditLog": auditLog,
       "auditLogEnable": auditLogEnable,
       "auditLogStoreResets": auditLogStoreResets,
       "auditLogStoreCommands": auditLogStoreCommands,
       "auditLogStoreOutputs": auditLogStoreOutputs,
       "auditLogStoreAlarmActions": auditLogStoreAlarmActions,
       "auditLogStorePwdFailures": auditLogStorePwdFailures,
       "auditLogStoreLogins": auditLogStoreLogins,
       "auditLogStoreSHSK": auditLogStoreSHSK,
       "auditLogStorePassthrough": auditLogStorePassthrough,
       "auditLogStoreInactivity": auditLogStoreInactivity,
       "auditLogStorePolling": auditLogStorePolling,
       "auditLogMaxSize": auditLogMaxSize,
       "scripting": scripting,
       "scrGlobalEnable": scrGlobalEnable,
       "scrDTRCtrlPortEnableTable": scrDTRCtrlPortEnableTable,
       "scrDTRCtrlPortEnableEntry": scrDTRCtrlPortEnableEntry,
       "scrDTRCtrlPortEnableIndex": scrDTRCtrlPortEnableIndex,
       "scrDTRCtrlPortEnable": scrDTRCtrlPortEnable,
       "scrTable": scrTable,
       "scrEntry": scrEntry,
       "scrIndex": scrIndex,
       "scrEnable": scrEnable,
       "scrName": scrName,
       "scrFilename": scrFilename,
       "scrRunAlways": scrRunAlways,
       "scrRunAtStartup": scrRunAtStartup,
       "scrRunScheduled": scrRunScheduled,
       "scrScheduleTime": scrScheduleTime,
       "scrArguments": scrArguments,
       "scrRepeatInterval": scrRepeatInterval,
       "scrVolatileStringTable": scrVolatileStringTable,
       "scrVolatileStringEntry": scrVolatileStringEntry,
       "scrVolatileStringIndex": scrVolatileStringIndex,
       "scrVolatileString": scrVolatileString,
       "scrVolatileIntTable": scrVolatileIntTable,
       "scrVolatileIntEntry": scrVolatileIntEntry,
       "scrVolatileIntIndex": scrVolatileIntIndex,
       "scrVolatileInt": scrVolatileInt,
       "scrNonVolatileStringTable": scrNonVolatileStringTable,
       "scrNonVolatileStringEntry": scrNonVolatileStringEntry,
       "scrNonVolatileStringIndex": scrNonVolatileStringIndex,
       "scrNonVolatileString": scrNonVolatileString,
       "scrNonVolatileIntTable": scrNonVolatileIntTable,
       "scrNonVolatileIntEntry": scrNonVolatileIntEntry,
       "scrNonVolatileIntIndex": scrNonVolatileIntIndex,
       "scrNonVolatileInt": scrNonVolatileInt,
       "productIds": productIds,
       "siteName": siteName,
       "thisProduct": thisProduct,
       "stockTrapString": stockTrapString,
       "trapEventTypeNumber": trapEventTypeNumber,
       "trapEventTypeName": trapEventTypeName,
       "trapIncludedValue": trapIncludedValue,
       "trapIncludedString": trapIncludedString,
       "trapTypeString": trapTypeString,
       "trapEventClassNumber": trapEventClassNumber,
       "trapEventClassName": trapEventClassName,
       "keyInterface": keyInterface,
       "s570StockContactClosureTrap": s570StockContactClosureTrap,
       "s570StockTempTrap": s570StockTempTrap,
       "s570StockHumidityTrap": s570StockHumidityTrap,
       "s570StockAnalogTrap": s570StockAnalogTrap,
       "s570StockOutputTrap": s570StockOutputTrap,
       "s570StockDataAlarmTrap": s570StockDataAlarmTrap,
       "s570StockNoDataAlarmTrap": s570StockNoDataAlarmTrap,
       "s570StockSchedTrap": s570StockSchedTrap,
       "s570StockImmediateTrap": s570StockImmediateTrap,
       "s570StockCTSTrap": s570StockCTSTrap,
       "s570CPEDownTrap": s570CPEDownTrap,
       "s570FuelSensorDisconnectTrap": s570FuelSensorDisconnectTrap,
       "s570FuelSensorVolumeTrap": s570FuelSensorVolumeTrap,
       "s570ACPowerMonitorAvgVoltageTrap": s570ACPowerMonitorAvgVoltageTrap,
       "s570ACPowerMonitorAvgCurrentTrap": s570ACPowerMonitorAvgCurrentTrap,
       "s570ACPowerMonitorFrequencyTrap": s570ACPowerMonitorFrequencyTrap,
       "s570ACPowerMonitorTRPTrap": s570ACPowerMonitorTRPTrap,
       "s570ACPowerMonitorDisconnectTrap": s570ACPowerMonitorDisconnectTrap,
       "s570StockLoadSheddingTrap": s570StockLoadSheddingTrap,
       "s570StockScriptTrap": s570StockScriptTrap,
       "s570ACTotalPowerFactorTrap": s570ACTotalPowerFactorTrap,
       "s570ResetTrap": s570ResetTrap,
       "s570UserTrap1000": s570UserTrap1000,
       "s570UserTrap1001": s570UserTrap1001,
       "s570UserTrap1002": s570UserTrap1002,
       "s570UserTrap1003": s570UserTrap1003,
       "s570UserTrap1004": s570UserTrap1004,
       "s570UserTrap1005": s570UserTrap1005,
       "s570UserTrap1006": s570UserTrap1006,
       "s570UserTrap1007": s570UserTrap1007,
       "s570UserTrap1008": s570UserTrap1008,
       "s570UserTrap1009": s570UserTrap1009,
       "s570UserTrap1010": s570UserTrap1010,
       "s570UserTrap1011": s570UserTrap1011,
       "s570UserTrap1012": s570UserTrap1012,
       "s570UserTrap1013": s570UserTrap1013,
       "s570UserTrap1014": s570UserTrap1014,
       "s570UserTrap1015": s570UserTrap1015,
       "s570UserTrap1016": s570UserTrap1016,
       "s570UserTrap1017": s570UserTrap1017,
       "s570UserTrap1018": s570UserTrap1018,
       "s570UserTrap1019": s570UserTrap1019,
       "s570UserTrap1020": s570UserTrap1020,
       "s570UserTrap1021": s570UserTrap1021,
       "s570UserTrap1022": s570UserTrap1022,
       "s570UserTrap1023": s570UserTrap1023,
       "s570UserTrap1024": s570UserTrap1024,
       "s570UserTrap1025": s570UserTrap1025,
       "s570UserTrap1026": s570UserTrap1026,
       "s570UserTrap1027": s570UserTrap1027,
       "s570UserTrap1028": s570UserTrap1028,
       "s570UserTrap1029": s570UserTrap1029,
       "s570UserTrap1030": s570UserTrap1030,
       "s570UserTrap1031": s570UserTrap1031,
       "s570UserTrap1032": s570UserTrap1032,
       "s570UserTrap1033": s570UserTrap1033,
       "s570UserTrap1034": s570UserTrap1034,
       "s570UserTrap1035": s570UserTrap1035,
       "s570UserTrap1036": s570UserTrap1036,
       "s570UserTrap1037": s570UserTrap1037,
       "s570UserTrap1038": s570UserTrap1038,
       "s570UserTrap1039": s570UserTrap1039,
       "s570UserTrap1040": s570UserTrap1040,
       "s570UserTrap1041": s570UserTrap1041,
       "s570UserTrap1042": s570UserTrap1042,
       "s570UserTrap1043": s570UserTrap1043,
       "s570UserTrap1044": s570UserTrap1044,
       "s570UserTrap1045": s570UserTrap1045,
       "s570UserTrap1046": s570UserTrap1046,
       "s570UserTrap1047": s570UserTrap1047,
       "s570UserTrap1048": s570UserTrap1048,
       "s570UserTrap1049": s570UserTrap1049,
       "s570UserTrap1050": s570UserTrap1050,
       "s570UserTrap1051": s570UserTrap1051,
       "s570UserTrap1052": s570UserTrap1052,
       "s570UserTrap1053": s570UserTrap1053,
       "s570UserTrap1054": s570UserTrap1054,
       "s570UserTrap1055": s570UserTrap1055,
       "s570UserTrap1056": s570UserTrap1056,
       "s570UserTrap1057": s570UserTrap1057,
       "s570UserTrap1058": s570UserTrap1058,
       "s570UserTrap1059": s570UserTrap1059,
       "s570UserTrap1060": s570UserTrap1060,
       "s570UserTrap1061": s570UserTrap1061,
       "s570UserTrap1062": s570UserTrap1062,
       "s570UserTrap1063": s570UserTrap1063,
       "s570UserTrap1064": s570UserTrap1064,
       "s570UserTrap1065": s570UserTrap1065,
       "s570UserTrap1066": s570UserTrap1066,
       "s570UserTrap1067": s570UserTrap1067,
       "s570UserTrap1068": s570UserTrap1068,
       "s570UserTrap1069": s570UserTrap1069,
       "s570UserTrap1070": s570UserTrap1070,
       "s570UserTrap1071": s570UserTrap1071,
       "s570UserTrap1072": s570UserTrap1072,
       "s570UserTrap1073": s570UserTrap1073,
       "s570UserTrap1074": s570UserTrap1074,
       "s570UserTrap1075": s570UserTrap1075,
       "s570UserTrap1076": s570UserTrap1076,
       "s570UserTrap1077": s570UserTrap1077,
       "s570UserTrap1078": s570UserTrap1078,
       "s570UserTrap1079": s570UserTrap1079,
       "s570UserTrap1080": s570UserTrap1080,
       "s570UserTrap1081": s570UserTrap1081,
       "s570UserTrap1082": s570UserTrap1082,
       "s570UserTrap1083": s570UserTrap1083,
       "s570UserTrap1084": s570UserTrap1084,
       "s570UserTrap1085": s570UserTrap1085,
       "s570UserTrap1086": s570UserTrap1086,
       "s570UserTrap1087": s570UserTrap1087,
       "s570UserTrap1088": s570UserTrap1088,
       "s570UserTrap1089": s570UserTrap1089,
       "s570UserTrap1090": s570UserTrap1090,
       "s570UserTrap1091": s570UserTrap1091,
       "s570UserTrap1092": s570UserTrap1092,
       "s570UserTrap1093": s570UserTrap1093,
       "s570UserTrap1094": s570UserTrap1094,
       "s570UserTrap1095": s570UserTrap1095,
       "s570UserTrap1096": s570UserTrap1096,
       "s570UserTrap1097": s570UserTrap1097,
       "s570UserTrap1098": s570UserTrap1098,
       "s570UserTrap1099": s570UserTrap1099,
       "s570UserTrap1100": s570UserTrap1100,
       "s570UserTrap1101": s570UserTrap1101,
       "s570UserTrap1102": s570UserTrap1102,
       "s570UserTrap1103": s570UserTrap1103,
       "s570UserTrap1104": s570UserTrap1104,
       "s570UserTrap1105": s570UserTrap1105,
       "s570UserTrap1106": s570UserTrap1106,
       "s570UserTrap1107": s570UserTrap1107,
       "s570UserTrap1108": s570UserTrap1108,
       "s570UserTrap1109": s570UserTrap1109,
       "s570UserTrap1110": s570UserTrap1110,
       "s570UserTrap1111": s570UserTrap1111,
       "s570UserTrap1112": s570UserTrap1112,
       "s570UserTrap1113": s570UserTrap1113,
       "s570UserTrap1114": s570UserTrap1114,
       "s570UserTrap1115": s570UserTrap1115,
       "s570UserTrap1116": s570UserTrap1116,
       "s570UserTrap1117": s570UserTrap1117,
       "s570UserTrap1118": s570UserTrap1118,
       "s570UserTrap1119": s570UserTrap1119,
       "s570UserTrap1120": s570UserTrap1120,
       "s570UserTrap1121": s570UserTrap1121,
       "s570UserTrap1122": s570UserTrap1122,
       "s570UserTrap1123": s570UserTrap1123,
       "s570UserTrap1124": s570UserTrap1124,
       "s570UserTrap1125": s570UserTrap1125,
       "s570UserTrap1126": s570UserTrap1126,
       "s570UserTrap1127": s570UserTrap1127,
       "s570UserTrap1128": s570UserTrap1128,
       "s570UserTrap1129": s570UserTrap1129,
       "s570UserTrap1130": s570UserTrap1130,
       "s570UserTrap1131": s570UserTrap1131,
       "s570UserTrap1132": s570UserTrap1132,
       "s570UserTrap1133": s570UserTrap1133,
       "s570UserTrap1134": s570UserTrap1134,
       "s570UserTrap1135": s570UserTrap1135,
       "s570UserTrap1136": s570UserTrap1136,
       "s570UserTrap1137": s570UserTrap1137,
       "s570UserTrap1138": s570UserTrap1138,
       "s570UserTrap1139": s570UserTrap1139,
       "s570UserTrap1140": s570UserTrap1140,
       "s570UserTrap1141": s570UserTrap1141,
       "s570UserTrap1142": s570UserTrap1142,
       "s570UserTrap1143": s570UserTrap1143,
       "s570UserTrap1144": s570UserTrap1144,
       "s570UserTrap1145": s570UserTrap1145,
       "s570UserTrap1146": s570UserTrap1146,
       "s570UserTrap1147": s570UserTrap1147,
       "s570UserTrap1148": s570UserTrap1148,
       "s570UserTrap1149": s570UserTrap1149,
       "s570UserTrap1150": s570UserTrap1150,
       "s570UserTrap1151": s570UserTrap1151,
       "s570UserTrap1152": s570UserTrap1152,
       "s570UserTrap1153": s570UserTrap1153,
       "s570UserTrap1154": s570UserTrap1154,
       "s570UserTrap1155": s570UserTrap1155,
       "s570UserTrap1156": s570UserTrap1156,
       "s570UserTrap1157": s570UserTrap1157,
       "s570UserTrap1158": s570UserTrap1158,
       "s570UserTrap1159": s570UserTrap1159,
       "s570UserTrap1160": s570UserTrap1160,
       "s570UserTrap1161": s570UserTrap1161,
       "s570UserTrap1162": s570UserTrap1162,
       "s570UserTrap1163": s570UserTrap1163,
       "s570UserTrap1164": s570UserTrap1164,
       "s570UserTrap1165": s570UserTrap1165,
       "s570UserTrap1166": s570UserTrap1166,
       "s570UserTrap1167": s570UserTrap1167,
       "s570UserTrap1168": s570UserTrap1168,
       "s570UserTrap1169": s570UserTrap1169,
       "s570UserTrap1170": s570UserTrap1170,
       "s570UserTrap1171": s570UserTrap1171,
       "s570UserTrap1172": s570UserTrap1172,
       "s570UserTrap1173": s570UserTrap1173,
       "s570UserTrap1174": s570UserTrap1174,
       "s570UserTrap1175": s570UserTrap1175,
       "s570UserTrap1176": s570UserTrap1176,
       "s570UserTrap1177": s570UserTrap1177,
       "s570UserTrap1178": s570UserTrap1178,
       "s570UserTrap1179": s570UserTrap1179,
       "s570UserTrap1180": s570UserTrap1180,
       "s570UserTrap1181": s570UserTrap1181,
       "s570UserTrap1182": s570UserTrap1182,
       "s570UserTrap1183": s570UserTrap1183,
       "s570UserTrap1184": s570UserTrap1184,
       "s570UserTrap1185": s570UserTrap1185,
       "s570UserTrap1186": s570UserTrap1186,
       "s570UserTrap1187": s570UserTrap1187,
       "s570UserTrap1188": s570UserTrap1188,
       "s570UserTrap1189": s570UserTrap1189,
       "s570UserTrap1190": s570UserTrap1190,
       "s570UserTrap1191": s570UserTrap1191,
       "s570UserTrap1192": s570UserTrap1192,
       "s570UserTrap1193": s570UserTrap1193,
       "s570UserTrap1194": s570UserTrap1194,
       "s570UserTrap1195": s570UserTrap1195,
       "s570UserTrap1196": s570UserTrap1196,
       "s570UserTrap1197": s570UserTrap1197,
       "s570UserTrap1198": s570UserTrap1198,
       "s570UserTrap1199": s570UserTrap1199}
)
