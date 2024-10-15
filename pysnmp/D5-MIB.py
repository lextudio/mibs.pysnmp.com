# SNMP MIB module (D5-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/D5-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:22:52 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ipAdEntAddr,) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipAdEntAddr")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmp,
 sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmp",
    "sysDescr",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Symplex_ObjectIdentity = ObjectIdentity
symplex = _Symplex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1)
)
_DatamizerHseries_ObjectIdentity = ObjectIdentity
datamizerHseries = _DatamizerHseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 1)
)
_DirectrouteSeries_ObjectIdentity = ObjectIdentity
directrouteSeries = _DirectrouteSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 2)
)
_Directroute4Series_ObjectIdentity = ObjectIdentity
directroute4Series = _Directroute4Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 3)
)
_DatamizerVseries_ObjectIdentity = ObjectIdentity
datamizerVseries = _DatamizerVseries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 4)
)
_Drcalldata_ObjectIdentity = ObjectIdentity
drcalldata = _Drcalldata_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1)
)
_CallDataTrapAddr_Type = IpAddress
_CallDataTrapAddr_Object = MibScalar
callDataTrapAddr = _CallDataTrapAddr_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 1),
    _CallDataTrapAddr_Type()
)
callDataTrapAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataTrapAddr.setStatus("mandatory")
_CallDataTotalActiveCalls_Type = Integer32
_CallDataTotalActiveCalls_Object = MibScalar
callDataTotalActiveCalls = _CallDataTotalActiveCalls_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 2),
    _CallDataTotalActiveCalls_Type()
)
callDataTotalActiveCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataTotalActiveCalls.setStatus("mandatory")
_CallDataActvTable_Object = MibTable
callDataActvTable = _CallDataActvTable_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3)
)
if mibBuilder.loadTexts:
    callDataActvTable.setStatus("mandatory")
_CallDataActvEntry_Object = MibTableRow
callDataActvEntry = _CallDataActvEntry_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1)
)
callDataActvEntry.setIndexNames(
    (0, "D5-MIB", "callDataActvIndex"),
)
if mibBuilder.loadTexts:
    callDataActvEntry.setStatus("mandatory")
_CallDataActvIndex_Type = Integer32
_CallDataActvIndex_Object = MibTableColumn
callDataActvIndex = _CallDataActvIndex_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 1),
    _CallDataActvIndex_Type()
)
callDataActvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvIndex.setStatus("mandatory")
_CallDataActvReqTime_Type = DisplayString
_CallDataActvReqTime_Object = MibTableColumn
callDataActvReqTime = _CallDataActvReqTime_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 2),
    _CallDataActvReqTime_Type()
)
callDataActvReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvReqTime.setStatus("mandatory")
_CallDataActvEstTime_Type = DisplayString
_CallDataActvEstTime_Object = MibTableColumn
callDataActvEstTime = _CallDataActvEstTime_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 3),
    _CallDataActvEstTime_Type()
)
callDataActvEstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvEstTime.setStatus("mandatory")
_CallDataActvCurrTime_Type = DisplayString
_CallDataActvCurrTime_Object = MibTableColumn
callDataActvCurrTime = _CallDataActvCurrTime_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 4),
    _CallDataActvCurrTime_Type()
)
callDataActvCurrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvCurrTime.setStatus("mandatory")
_CallDataActvSourceSys_Type = DisplayString
_CallDataActvSourceSys_Object = MibTableColumn
callDataActvSourceSys = _CallDataActvSourceSys_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 5),
    _CallDataActvSourceSys_Type()
)
callDataActvSourceSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvSourceSys.setStatus("mandatory")
_CallDataActvDestSys_Type = DisplayString
_CallDataActvDestSys_Object = MibTableColumn
callDataActvDestSys = _CallDataActvDestSys_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 6),
    _CallDataActvDestSys_Type()
)
callDataActvDestSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvDestSys.setStatus("mandatory")
_CallDataActvPhoneNum_Type = DisplayString
_CallDataActvPhoneNum_Object = MibTableColumn
callDataActvPhoneNum = _CallDataActvPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 7),
    _CallDataActvPhoneNum_Type()
)
callDataActvPhoneNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvPhoneNum.setStatus("mandatory")
_CallDataActvBandwidth_Type = Integer32
_CallDataActvBandwidth_Object = MibTableColumn
callDataActvBandwidth = _CallDataActvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 8),
    _CallDataActvBandwidth_Type()
)
callDataActvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvBandwidth.setStatus("mandatory")


class _CallDataActvStatus_Type(Integer32):
    """Custom type callDataActvStatus based on Integer32"""
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
        *(("active", 3),
          ("complete", 4),
          ("failed", 5),
          ("inactive", 1),
          ("requested", 2))
    )


_CallDataActvStatus_Type.__name__ = "Integer32"
_CallDataActvStatus_Object = MibTableColumn
callDataActvStatus = _CallDataActvStatus_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 3, 1, 9),
    _CallDataActvStatus_Type()
)
callDataActvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataActvStatus.setStatus("mandatory")
_CallDataCompTable_Object = MibTable
callDataCompTable = _CallDataCompTable_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4)
)
if mibBuilder.loadTexts:
    callDataCompTable.setStatus("mandatory")
_CallDataCompEntry_Object = MibTableRow
callDataCompEntry = _CallDataCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1)
)
callDataCompEntry.setIndexNames(
    (0, "D5-MIB", "callDataCompIndex"),
)
if mibBuilder.loadTexts:
    callDataCompEntry.setStatus("mandatory")
_CallDataCompIndex_Type = Integer32
_CallDataCompIndex_Object = MibTableColumn
callDataCompIndex = _CallDataCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 1),
    _CallDataCompIndex_Type()
)
callDataCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompIndex.setStatus("mandatory")
_CallDataCompReqTime_Type = DisplayString
_CallDataCompReqTime_Object = MibTableColumn
callDataCompReqTime = _CallDataCompReqTime_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 2),
    _CallDataCompReqTime_Type()
)
callDataCompReqTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompReqTime.setStatus("mandatory")
_CallDataCompEstTime_Type = DisplayString
_CallDataCompEstTime_Object = MibTableColumn
callDataCompEstTime = _CallDataCompEstTime_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 3),
    _CallDataCompEstTime_Type()
)
callDataCompEstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompEstTime.setStatus("mandatory")
_CallDataCompRelTime_Type = DisplayString
_CallDataCompRelTime_Object = MibTableColumn
callDataCompRelTime = _CallDataCompRelTime_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 4),
    _CallDataCompRelTime_Type()
)
callDataCompRelTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompRelTime.setStatus("mandatory")
_CallDataCompSourceSys_Type = DisplayString
_CallDataCompSourceSys_Object = MibTableColumn
callDataCompSourceSys = _CallDataCompSourceSys_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 5),
    _CallDataCompSourceSys_Type()
)
callDataCompSourceSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompSourceSys.setStatus("mandatory")
_CallDataCompDestSys_Type = DisplayString
_CallDataCompDestSys_Object = MibTableColumn
callDataCompDestSys = _CallDataCompDestSys_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 6),
    _CallDataCompDestSys_Type()
)
callDataCompDestSys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompDestSys.setStatus("mandatory")
_CallDataCompPhoneNum_Type = DisplayString
_CallDataCompPhoneNum_Object = MibTableColumn
callDataCompPhoneNum = _CallDataCompPhoneNum_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 7),
    _CallDataCompPhoneNum_Type()
)
callDataCompPhoneNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompPhoneNum.setStatus("mandatory")
_CallDataCompBandwidth_Type = Integer32
_CallDataCompBandwidth_Object = MibTableColumn
callDataCompBandwidth = _CallDataCompBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 8),
    _CallDataCompBandwidth_Type()
)
callDataCompBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompBandwidth.setStatus("mandatory")


class _CallDataCompStatus_Type(Integer32):
    """Custom type callDataCompStatus based on Integer32"""
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
        *(("active", 3),
          ("complete", 4),
          ("failed", 5),
          ("inactive", 1),
          ("requested", 2))
    )


_CallDataCompStatus_Type.__name__ = "Integer32"
_CallDataCompStatus_Object = MibTableColumn
callDataCompStatus = _CallDataCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 1, 4, 1, 9),
    _CallDataCompStatus_Type()
)
callDataCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callDataCompStatus.setStatus("mandatory")
_D5system_ObjectIdentity = ObjectIdentity
d5system = _D5system_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 2)
)


class _DrProdType_Type(Integer32):
    """Custom type drProdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("datamizer-5", 1)
    )


_DrProdType_Type.__name__ = "Integer32"
_DrProdType_Object = MibScalar
drProdType = _DrProdType_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 2, 1),
    _DrProdType_Type()
)
drProdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drProdType.setStatus("mandatory")
_DrSoftVersion_Type = DisplayString
_DrSoftVersion_Object = MibScalar
drSoftVersion = _DrSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 2, 2),
    _DrSoftVersion_Type()
)
drSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drSoftVersion.setStatus("mandatory")
_D5stats_ObjectIdentity = ObjectIdentity
d5stats = _D5stats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3)
)
_D5PortStatsTable_Object = MibTable
d5PortStatsTable = _D5PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1)
)
if mibBuilder.loadTexts:
    d5PortStatsTable.setStatus("mandatory")
_D5PortStatsEntry_Object = MibTableRow
d5PortStatsEntry = _D5PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1)
)
d5PortStatsEntry.setIndexNames(
    (0, "D5-MIB", "d5StatsPortIndex"),
)
if mibBuilder.loadTexts:
    d5PortStatsEntry.setStatus("mandatory")


class _D5StatsPortIndex_Type(Integer32):
    """Custom type d5StatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("briA", 1),
          ("briB", 2),
          ("briC", 3),
          ("briD", 4),
          ("lanE", 5),
          ("serialHostF", 6),
          ("serialTrunkG", 7))
    )


_D5StatsPortIndex_Type.__name__ = "Integer32"
_D5StatsPortIndex_Object = MibTableColumn
d5StatsPortIndex = _D5StatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 1),
    _D5StatsPortIndex_Type()
)
d5StatsPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortIndex.setStatus("mandatory")
_D5StatsPortPacketsIn_Type = Counter32
_D5StatsPortPacketsIn_Object = MibTableColumn
d5StatsPortPacketsIn = _D5StatsPortPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 2),
    _D5StatsPortPacketsIn_Type()
)
d5StatsPortPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortPacketsIn.setStatus("mandatory")
_D5StatsPortPacketsOut_Type = Counter32
_D5StatsPortPacketsOut_Object = MibTableColumn
d5StatsPortPacketsOut = _D5StatsPortPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 3),
    _D5StatsPortPacketsOut_Type()
)
d5StatsPortPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortPacketsOut.setStatus("mandatory")
_D5StatsPortPPSIn_Type = Integer32
_D5StatsPortPPSIn_Object = MibTableColumn
d5StatsPortPPSIn = _D5StatsPortPPSIn_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 4),
    _D5StatsPortPPSIn_Type()
)
d5StatsPortPPSIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortPPSIn.setStatus("mandatory")
_D5StatsPortPPSOut_Type = Integer32
_D5StatsPortPPSOut_Object = MibTableColumn
d5StatsPortPPSOut = _D5StatsPortPPSOut_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 5),
    _D5StatsPortPPSOut_Type()
)
d5StatsPortPPSOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortPPSOut.setStatus("mandatory")
_D5StatsPortBPSIn_Type = Integer32
_D5StatsPortBPSIn_Object = MibTableColumn
d5StatsPortBPSIn = _D5StatsPortBPSIn_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 6),
    _D5StatsPortBPSIn_Type()
)
d5StatsPortBPSIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortBPSIn.setStatus("mandatory")
_D5StatsPortBPSOut_Type = Integer32
_D5StatsPortBPSOut_Object = MibTableColumn
d5StatsPortBPSOut = _D5StatsPortBPSOut_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 1, 1, 7),
    _D5StatsPortBPSOut_Type()
)
d5StatsPortBPSOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5StatsPortBPSOut.setStatus("mandatory")


class _D5PortStatsInterval_Type(Integer32):
    """Custom type d5PortStatsInterval based on Integer32"""
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
        *(("fifteen-minutes", 2),
          ("one-minute", 1),
          ("sixty-minutes", 4),
          ("thirty-minutes", 3))
    )


_D5PortStatsInterval_Type.__name__ = "Integer32"
_D5PortStatsInterval_Object = MibScalar
d5PortStatsInterval = _D5PortStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 2),
    _D5PortStatsInterval_Type()
)
d5PortStatsInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d5PortStatsInterval.setStatus("mandatory")
_D5SystemStatsTable_Object = MibTable
d5SystemStatsTable = _D5SystemStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3)
)
if mibBuilder.loadTexts:
    d5SystemStatsTable.setStatus("mandatory")
_D5SystemStatsEntry_Object = MibTableRow
d5SystemStatsEntry = _D5SystemStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3, 1)
)
d5SystemStatsEntry.setIndexNames(
    (0, "D5-MIB", "d5SystemStatsIndex"),
)
if mibBuilder.loadTexts:
    d5SystemStatsEntry.setStatus("mandatory")


class _D5SystemStatsIndex_Type(Integer32):
    """Custom type d5SystemStatsIndex based on Integer32"""
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
        *(("congestionDetection", 4),
          ("lanDataErrors", 3),
          ("serialHostDataErrors", 2),
          ("wanDataErrors", 1))
    )


_D5SystemStatsIndex_Type.__name__ = "Integer32"
_D5SystemStatsIndex_Object = MibTableColumn
d5SystemStatsIndex = _D5SystemStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3, 1, 1),
    _D5SystemStatsIndex_Type()
)
d5SystemStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5SystemStatsIndex.setStatus("mandatory")
_D5SystemStatsCount_Type = Counter32
_D5SystemStatsCount_Object = MibTableColumn
d5SystemStatsCount = _D5SystemStatsCount_Object(
    (1, 3, 6, 1, 4, 1, 385, 1, 4, 3, 3, 1, 2),
    _D5SystemStatsCount_Type()
)
d5SystemStatsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d5SystemStatsCount.setStatus("mandatory")

# Managed Objects groups


# Notification objects

coldStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 0)
)
coldStart.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    coldStart.setStatus(
        ""
    )

warmStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    warmStart.setStatus(
        ""
    )

linkDown = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 2)
)
linkDown.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkDown.setStatus(
        ""
    )

linkUp = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 3)
)
linkUp.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    linkUp.setStatus(
        ""
    )

authenticationFailure = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 4)
)
authenticationFailure.setObjects(
    ("IP-MIB", "ipAdEntAddr")
)
if mibBuilder.loadTexts:
    authenticationFailure.setStatus(
        ""
    )

egpNeighborLoss = NotificationType(
    (1, 3, 6, 1, 2, 1, 11, 0, 5)
)
egpNeighborLoss.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    egpNeighborLoss.setStatus(
        ""
    )

unspecifiedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 1)
)
unspecifiedTrap.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    unspecifiedTrap.setStatus(
        ""
    )

startDisasterRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 2)
)
startDisasterRecovery.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    startDisasterRecovery.setStatus(
        ""
    )

stopDisasterRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 3)
)
stopDisasterRecovery.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    stopDisasterRecovery.setStatus(
        ""
    )

noBChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 4)
)
noBChannel.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    noBChannel.setStatus(
        ""
    )

dailyConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 5)
)
dailyConnLimit.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    dailyConnLimit.setStatus(
        ""
    )

monthlyConnLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 6)
)
monthlyConnLimit.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    monthlyConnLimit.setStatus(
        ""
    )

dataErrorBChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 7)
)
dataErrorBChannel.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    dataErrorBChannel.setStatus(
        ""
    )

pppVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 8)
)
pppVersion.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    pppVersion.setStatus(
        ""
    )

ipTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 9)
)
ipTableFull.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    ipTableFull.setStatus(
        ""
    )

macTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 10)
)
macTableFull.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    macTableFull.setStatus(
        ""
    )

routeTableFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 11)
)
routeTableFull.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    routeTableFull.setStatus(
        ""
    )

duplicateItem = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 12)
)
duplicateItem.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    duplicateItem.setStatus(
        ""
    )

noDChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 13)
)
noDChannel.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    noDChannel.setStatus(
        ""
    )

lostDedicated = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 14)
)
lostDedicated.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    lostDedicated.setStatus(
        ""
    )

compCallData = NotificationType(
    (1, 3, 6, 1, 4, 1, 385, 0, 15)
)
compCallData.setObjects(
    ("SNMPv2-MIB", "sysDescr")
)
if mibBuilder.loadTexts:
    compCallData.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "D5-MIB",
    **{"DisplayString": DisplayString,
       "coldStart": coldStart,
       "warmStart": warmStart,
       "linkDown": linkDown,
       "linkUp": linkUp,
       "authenticationFailure": authenticationFailure,
       "egpNeighborLoss": egpNeighborLoss,
       "symplex": symplex,
       "unspecifiedTrap": unspecifiedTrap,
       "startDisasterRecovery": startDisasterRecovery,
       "stopDisasterRecovery": stopDisasterRecovery,
       "noBChannel": noBChannel,
       "dailyConnLimit": dailyConnLimit,
       "monthlyConnLimit": monthlyConnLimit,
       "dataErrorBChannel": dataErrorBChannel,
       "pppVersion": pppVersion,
       "ipTableFull": ipTableFull,
       "macTableFull": macTableFull,
       "routeTableFull": routeTableFull,
       "duplicateItem": duplicateItem,
       "noDChannel": noDChannel,
       "lostDedicated": lostDedicated,
       "compCallData": compCallData,
       "products": products,
       "datamizerHseries": datamizerHseries,
       "directrouteSeries": directrouteSeries,
       "directroute4Series": directroute4Series,
       "datamizerVseries": datamizerVseries,
       "drcalldata": drcalldata,
       "callDataTrapAddr": callDataTrapAddr,
       "callDataTotalActiveCalls": callDataTotalActiveCalls,
       "callDataActvTable": callDataActvTable,
       "callDataActvEntry": callDataActvEntry,
       "callDataActvIndex": callDataActvIndex,
       "callDataActvReqTime": callDataActvReqTime,
       "callDataActvEstTime": callDataActvEstTime,
       "callDataActvCurrTime": callDataActvCurrTime,
       "callDataActvSourceSys": callDataActvSourceSys,
       "callDataActvDestSys": callDataActvDestSys,
       "callDataActvPhoneNum": callDataActvPhoneNum,
       "callDataActvBandwidth": callDataActvBandwidth,
       "callDataActvStatus": callDataActvStatus,
       "callDataCompTable": callDataCompTable,
       "callDataCompEntry": callDataCompEntry,
       "callDataCompIndex": callDataCompIndex,
       "callDataCompReqTime": callDataCompReqTime,
       "callDataCompEstTime": callDataCompEstTime,
       "callDataCompRelTime": callDataCompRelTime,
       "callDataCompSourceSys": callDataCompSourceSys,
       "callDataCompDestSys": callDataCompDestSys,
       "callDataCompPhoneNum": callDataCompPhoneNum,
       "callDataCompBandwidth": callDataCompBandwidth,
       "callDataCompStatus": callDataCompStatus,
       "d5system": d5system,
       "drProdType": drProdType,
       "drSoftVersion": drSoftVersion,
       "d5stats": d5stats,
       "d5PortStatsTable": d5PortStatsTable,
       "d5PortStatsEntry": d5PortStatsEntry,
       "d5StatsPortIndex": d5StatsPortIndex,
       "d5StatsPortPacketsIn": d5StatsPortPacketsIn,
       "d5StatsPortPacketsOut": d5StatsPortPacketsOut,
       "d5StatsPortPPSIn": d5StatsPortPPSIn,
       "d5StatsPortPPSOut": d5StatsPortPPSOut,
       "d5StatsPortBPSIn": d5StatsPortBPSIn,
       "d5StatsPortBPSOut": d5StatsPortBPSOut,
       "d5PortStatsInterval": d5PortStatsInterval,
       "d5SystemStatsTable": d5SystemStatsTable,
       "d5SystemStatsEntry": d5SystemStatsEntry,
       "d5SystemStatsIndex": d5SystemStatsIndex,
       "d5SystemStatsCount": d5SystemStatsCount}
)
