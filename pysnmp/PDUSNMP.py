# SNMP MIB module (PDUSNMP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDUSNMP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:38:18 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pdu_SNMP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1)
)
pdu_SNMP.setRevisions(
        ("2015-11-27 17:12",
         "2015-11-20 17:12",
         "2015-09-02 17:12",
         "2013-09-20 17:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ipt_pdu_SNMP_ObjectIdentity = ObjectIdentity
ipt_pdu_SNMP = _Ipt_pdu_SNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218)
)
_Slave_SiteTotals_ObjectIdentity = ObjectIdentity
slave_SiteTotals = _Slave_SiteTotals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 1)
)
_Slave_SiteTotalkWh_Type = Integer32
_Slave_SiteTotalkWh_Object = MibScalar
slave_SiteTotalkWh = _Slave_SiteTotalkWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 1, 1),
    _Slave_SiteTotalkWh_Type()
)
slave_SiteTotalkWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_SiteTotalkWh.setStatus("current")
_Slave_SiteTotalBtu_Type = Integer32
_Slave_SiteTotalBtu_Object = MibScalar
slave_SiteTotalBtu = _Slave_SiteTotalBtu_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 1, 2),
    _Slave_SiteTotalBtu_Type()
)
slave_SiteTotalBtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_SiteTotalBtu.setStatus("current")
_Slave_SiteTotalKgCO2_Type = Integer32
_Slave_SiteTotalKgCO2_Object = MibScalar
slave_SiteTotalKgCO2 = _Slave_SiteTotalKgCO2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 1, 3),
    _Slave_SiteTotalKgCO2_Type()
)
slave_SiteTotalKgCO2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_SiteTotalKgCO2.setStatus("current")
_Slave_Server_ObjectIdentity = ObjectIdentity
slave_Server = _Slave_Server_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 2)
)


class _Slave_Nopdus_Type(Integer32):
    """Custom type slave_Nopdus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Slave_Nopdus_Type.__name__ = "Integer32"
_Slave_Nopdus_Object = MibScalar
slave_Nopdus = _Slave_Nopdus_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 2, 1),
    _Slave_Nopdus_Type()
)
slave_Nopdus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Nopdus.setStatus("current")


class _Slaves_Online_Type(Integer32):
    """Custom type slaves_Online based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Slaves_Online_Type.__name__ = "Integer32"
_Slaves_Online_Object = MibScalar
slaves_Online = _Slaves_Online_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 2, 2),
    _Slaves_Online_Type()
)
slaves_Online.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slaves_Online.setStatus("current")


class _Slave_ServerStatus_Type(Integer32):
    """Custom type slave_ServerStatus based on Integer32"""
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
        *(("getinfo", 3),
          ("listening", 4),
          ("running", 1),
          ("searching", 2),
          ("stopped", 0))
    )


_Slave_ServerStatus_Type.__name__ = "Integer32"
_Slave_ServerStatus_Object = MibScalar
slave_ServerStatus = _Slave_ServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 2, 3),
    _Slave_ServerStatus_Type()
)
slave_ServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_ServerStatus.setStatus("current")
_Pdu_Configuration_ObjectIdentity = ObjectIdentity
pdu_Configuration = _Pdu_Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3)
)
_Pdu_ClientName_Type = DisplayString
_Pdu_ClientName_Object = MibScalar
pdu_ClientName = _Pdu_ClientName_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 1),
    _Pdu_ClientName_Type()
)
pdu_ClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_ClientName.setStatus("current")
_Pdu_LocationName_Type = DisplayString
_Pdu_LocationName_Object = MibScalar
pdu_LocationName = _Pdu_LocationName_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 2),
    _Pdu_LocationName_Type()
)
pdu_LocationName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_LocationName.setStatus("current")
_Pdu_FirmwareVersion_Type = DisplayString
_Pdu_FirmwareVersion_Object = MibScalar
pdu_FirmwareVersion = _Pdu_FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 3),
    _Pdu_FirmwareVersion_Type()
)
pdu_FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_FirmwareVersion.setStatus("current")


class _Pdu_KgCO2Conversion_Type(Integer32):
    """Custom type pdu_KgCO2Conversion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Pdu_KgCO2Conversion_Type.__name__ = "Integer32"
_Pdu_KgCO2Conversion_Object = MibScalar
pdu_KgCO2Conversion = _Pdu_KgCO2Conversion_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 4),
    _Pdu_KgCO2Conversion_Type()
)
pdu_KgCO2Conversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_KgCO2Conversion.setStatus("current")


class _Pdu_MODBUSTimeout_Type(Integer32):
    """Custom type pdu_MODBUSTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 5000),
    )


_Pdu_MODBUSTimeout_Type.__name__ = "Integer32"
_Pdu_MODBUSTimeout_Object = MibScalar
pdu_MODBUSTimeout = _Pdu_MODBUSTimeout_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 5),
    _Pdu_MODBUSTimeout_Type()
)
pdu_MODBUSTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_MODBUSTimeout.setStatus("current")


class _Pdu_MODBUSRetry_Type(Integer32):
    """Custom type pdu_MODBUSRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Pdu_MODBUSRetry_Type.__name__ = "Integer32"
_Pdu_MODBUSRetry_Object = MibScalar
pdu_MODBUSRetry = _Pdu_MODBUSRetry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 6),
    _Pdu_MODBUSRetry_Type()
)
pdu_MODBUSRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_MODBUSRetry.setStatus("current")


class _Pdu_NotUsed1_Type(Integer32):
    """Custom type pdu_NotUsed1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_Pdu_NotUsed1_Type.__name__ = "Integer32"
_Pdu_NotUsed1_Object = MibScalar
pdu_NotUsed1 = _Pdu_NotUsed1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 7),
    _Pdu_NotUsed1_Type()
)
pdu_NotUsed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_NotUsed1.setStatus("current")


class _Pdu_AlarmPeriod_Type(Integer32):
    """Custom type pdu_AlarmPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_Pdu_AlarmPeriod_Type.__name__ = "Integer32"
_Pdu_AlarmPeriod_Object = MibScalar
pdu_AlarmPeriod = _Pdu_AlarmPeriod_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 8),
    _Pdu_AlarmPeriod_Type()
)
pdu_AlarmPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_AlarmPeriod.setStatus("current")


class _Pdu_DHCPStatus_Type(Integer32):
    """Custom type pdu_DHCPStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pdu_DHCPStatus_Type.__name__ = "Integer32"
_Pdu_DHCPStatus_Object = MibScalar
pdu_DHCPStatus = _Pdu_DHCPStatus_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 9),
    _Pdu_DHCPStatus_Type()
)
pdu_DHCPStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_DHCPStatus.setStatus("current")
_Pdu_IPAddress_Type = IpAddress
_Pdu_IPAddress_Object = MibScalar
pdu_IPAddress = _Pdu_IPAddress_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 10),
    _Pdu_IPAddress_Type()
)
pdu_IPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_IPAddress.setStatus("current")
_Pdu_SubNetMask_Type = IpAddress
_Pdu_SubNetMask_Object = MibScalar
pdu_SubNetMask = _Pdu_SubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 11),
    _Pdu_SubNetMask_Type()
)
pdu_SubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_SubNetMask.setStatus("current")
_Pdu_CabinetID_Type = DisplayString
_Pdu_CabinetID_Object = MibScalar
pdu_CabinetID = _Pdu_CabinetID_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 12),
    _Pdu_CabinetID_Type()
)
pdu_CabinetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_CabinetID.setStatus("current")


class _Pdu_socketPeriod_Type(Integer32):
    """Custom type pdu_socketPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_Pdu_socketPeriod_Type.__name__ = "Integer32"
_Pdu_socketPeriod_Object = MibScalar
pdu_socketPeriod = _Pdu_socketPeriod_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 13),
    _Pdu_socketPeriod_Type()
)
pdu_socketPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_socketPeriod.setStatus("current")


class _Pdu_LockPeriod_Type(Integer32):
    """Custom type pdu_LockPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_Pdu_LockPeriod_Type.__name__ = "Integer32"
_Pdu_LockPeriod_Object = MibScalar
pdu_LockPeriod = _Pdu_LockPeriod_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 14),
    _Pdu_LockPeriod_Type()
)
pdu_LockPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_LockPeriod.setStatus("current")


class _Pdu_RTC_Hour_Type(Integer32):
    """Custom type pdu_RTC_Hour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_Pdu_RTC_Hour_Type.__name__ = "Integer32"
_Pdu_RTC_Hour_Object = MibScalar
pdu_RTC_Hour = _Pdu_RTC_Hour_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 15),
    _Pdu_RTC_Hour_Type()
)
pdu_RTC_Hour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_RTC_Hour.setStatus("current")


class _Pdu_RTC_Minute_Type(Integer32):
    """Custom type pdu_RTC_Minute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 59),
    )


_Pdu_RTC_Minute_Type.__name__ = "Integer32"
_Pdu_RTC_Minute_Object = MibScalar
pdu_RTC_Minute = _Pdu_RTC_Minute_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 16),
    _Pdu_RTC_Minute_Type()
)
pdu_RTC_Minute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_RTC_Minute.setStatus("current")


class _Pdu_RTC_Date_Type(Integer32):
    """Custom type pdu_RTC_Date based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_Pdu_RTC_Date_Type.__name__ = "Integer32"
_Pdu_RTC_Date_Object = MibScalar
pdu_RTC_Date = _Pdu_RTC_Date_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 17),
    _Pdu_RTC_Date_Type()
)
pdu_RTC_Date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_RTC_Date.setStatus("current")


class _Pdu_RTC_Month_Type(Integer32):
    """Custom type pdu_RTC_Month based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_Pdu_RTC_Month_Type.__name__ = "Integer32"
_Pdu_RTC_Month_Object = MibScalar
pdu_RTC_Month = _Pdu_RTC_Month_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 18),
    _Pdu_RTC_Month_Type()
)
pdu_RTC_Month.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_RTC_Month.setStatus("current")


class _Pdu_RTC_Year_Type(Integer32):
    """Custom type pdu_RTC_Year based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_Pdu_RTC_Year_Type.__name__ = "Integer32"
_Pdu_RTC_Year_Object = MibScalar
pdu_RTC_Year = _Pdu_RTC_Year_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 3, 19),
    _Pdu_RTC_Year_Type()
)
pdu_RTC_Year.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_RTC_Year.setStatus("current")
_Trap_Destinations_ObjectIdentity = ObjectIdentity
trap_Destinations = _Trap_Destinations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4)
)
_TrapDestinationsTable_Object = MibTable
trapDestinationsTable = _TrapDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4, 1)
)
if mibBuilder.loadTexts:
    trapDestinationsTable.setStatus("current")
_TrapDestinationsEntry_Object = MibTableRow
trapDestinationsEntry = _TrapDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4, 1, 1)
)
trapDestinationsEntry.setIndexNames(
    (0, "PDUSNMP", "trapDestinationsIndex"),
)
if mibBuilder.loadTexts:
    trapDestinationsEntry.setStatus("current")


class _TrapDestinationsIndex_Type(Integer32):
    """Custom type trapDestinationsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_TrapDestinationsIndex_Type.__name__ = "Integer32"
_TrapDestinationsIndex_Object = MibTableColumn
trapDestinationsIndex = _TrapDestinationsIndex_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4, 1, 1, 1),
    _TrapDestinationsIndex_Type()
)
trapDestinationsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestinationsIndex.setStatus("current")


class _TrapDestinationsStatus_Type(Integer32):
    """Custom type trapDestinationsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_TrapDestinationsStatus_Type.__name__ = "Integer32"
_TrapDestinationsStatus_Object = MibTableColumn
trapDestinationsStatus = _TrapDestinationsStatus_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4, 1, 1, 2),
    _TrapDestinationsStatus_Type()
)
trapDestinationsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestinationsStatus.setStatus("current")
_TrapDestinationsIP_Type = IpAddress
_TrapDestinationsIP_Object = MibTableColumn
trapDestinationsIP = _TrapDestinationsIP_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4, 1, 1, 3),
    _TrapDestinationsIP_Type()
)
trapDestinationsIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestinationsIP.setStatus("current")
_TrapDestinationsCommunity_Type = DisplayString
_TrapDestinationsCommunity_Object = MibTableColumn
trapDestinationsCommunity = _TrapDestinationsCommunity_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 4, 1, 1, 4),
    _TrapDestinationsCommunity_Type()
)
trapDestinationsCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapDestinationsCommunity.setStatus("current")
_Pdu_Information_ObjectIdentity = ObjectIdentity
pdu_Information = _Pdu_Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 5)
)
_Pdu_Firmware_Type = DisplayString
_Pdu_Firmware_Object = MibScalar
pdu_Firmware = _Pdu_Firmware_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 5, 1),
    _Pdu_Firmware_Type()
)
pdu_Firmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_Firmware.setStatus("current")


class _Pdu_Nosockets_Type(Integer32):
    """Custom type pdu_Nosockets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_Pdu_Nosockets_Type.__name__ = "Integer32"
_Pdu_Nosockets_Object = MibScalar
pdu_Nosockets = _Pdu_Nosockets_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 5, 2),
    _Pdu_Nosockets_Type()
)
pdu_Nosockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_Nosockets.setStatus("current")
_Pdu_ProductName_Type = DisplayString
_Pdu_ProductName_Object = MibScalar
pdu_ProductName = _Pdu_ProductName_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 5, 3),
    _Pdu_ProductName_Type()
)
pdu_ProductName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_ProductName.setStatus("current")
_Pdu_SerialNumber_Type = DisplayString
_Pdu_SerialNumber_Object = MibScalar
pdu_SerialNumber = _Pdu_SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 5, 4),
    _Pdu_SerialNumber_Type()
)
pdu_SerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_SerialNumber.setStatus("current")
_Pdu_Meters_ObjectIdentity = ObjectIdentity
pdu_Meters = _Pdu_Meters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6)
)
_Pdu_meter1_VRMS_Type = Integer32
_Pdu_meter1_VRMS_Object = MibScalar
pdu_meter1_VRMS = _Pdu_meter1_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 1),
    _Pdu_meter1_VRMS_Type()
)
pdu_meter1_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_VRMS.setStatus("current")
_Pdu_meter1_IRMS_Type = Integer32
_Pdu_meter1_IRMS_Object = MibScalar
pdu_meter1_IRMS = _Pdu_meter1_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 2),
    _Pdu_meter1_IRMS_Type()
)
pdu_meter1_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_IRMS.setStatus("current")
_Pdu_meter1_KWH_Type = Integer32
_Pdu_meter1_KWH_Object = MibScalar
pdu_meter1_KWH = _Pdu_meter1_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 3),
    _Pdu_meter1_KWH_Type()
)
pdu_meter1_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_KWH.setStatus("current")
_Pdu_meter1_KW_Type = Integer32
_Pdu_meter1_KW_Object = MibScalar
pdu_meter1_KW = _Pdu_meter1_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 4),
    _Pdu_meter1_KW_Type()
)
pdu_meter1_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_KW.setStatus("current")
_Pdu_meter1_TPMU_Type = Integer32
_Pdu_meter1_TPMU_Object = MibScalar
pdu_meter1_TPMU = _Pdu_meter1_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 5),
    _Pdu_meter1_TPMU_Type()
)
pdu_meter1_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_TPMU.setStatus("current")
_Pdu_meter1_IPK_Type = Integer32
_Pdu_meter1_IPK_Object = MibScalar
pdu_meter1_IPK = _Pdu_meter1_IPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 6),
    _Pdu_meter1_IPK_Type()
)
pdu_meter1_IPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_IPK.setStatus("current")
_Pdu_meter1_VPK_Type = Integer32
_Pdu_meter1_VPK_Object = MibScalar
pdu_meter1_VPK = _Pdu_meter1_VPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 7),
    _Pdu_meter1_VPK_Type()
)
pdu_meter1_VPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_VPK.setStatus("current")
_Pdu_meter1_PF_Type = Integer32
_Pdu_meter1_PF_Object = MibScalar
pdu_meter1_PF = _Pdu_meter1_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 8),
    _Pdu_meter1_PF_Type()
)
pdu_meter1_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_PF.setStatus("current")
_Pdu_meter1_Freq_Type = Integer32
_Pdu_meter1_Freq_Object = MibScalar
pdu_meter1_Freq = _Pdu_meter1_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 9),
    _Pdu_meter1_Freq_Type()
)
pdu_meter1_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter1_Freq.setStatus("current")
_Pdu_meter2_VRMS_Type = Integer32
_Pdu_meter2_VRMS_Object = MibScalar
pdu_meter2_VRMS = _Pdu_meter2_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 10),
    _Pdu_meter2_VRMS_Type()
)
pdu_meter2_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_VRMS.setStatus("current")
_Pdu_meter2_IRMS_Type = Integer32
_Pdu_meter2_IRMS_Object = MibScalar
pdu_meter2_IRMS = _Pdu_meter2_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 11),
    _Pdu_meter2_IRMS_Type()
)
pdu_meter2_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_IRMS.setStatus("current")
_Pdu_meter2_KWH_Type = Integer32
_Pdu_meter2_KWH_Object = MibScalar
pdu_meter2_KWH = _Pdu_meter2_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 12),
    _Pdu_meter2_KWH_Type()
)
pdu_meter2_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_KWH.setStatus("current")
_Pdu_meter2_KW_Type = Integer32
_Pdu_meter2_KW_Object = MibScalar
pdu_meter2_KW = _Pdu_meter2_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 13),
    _Pdu_meter2_KW_Type()
)
pdu_meter2_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_KW.setStatus("current")
_Pdu_meter2_TPMU_Type = Integer32
_Pdu_meter2_TPMU_Object = MibScalar
pdu_meter2_TPMU = _Pdu_meter2_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 14),
    _Pdu_meter2_TPMU_Type()
)
pdu_meter2_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_TPMU.setStatus("current")
_Pdu_meter2_IPK_Type = Integer32
_Pdu_meter2_IPK_Object = MibScalar
pdu_meter2_IPK = _Pdu_meter2_IPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 15),
    _Pdu_meter2_IPK_Type()
)
pdu_meter2_IPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_IPK.setStatus("current")
_Pdu_meter2_VPK_Type = Integer32
_Pdu_meter2_VPK_Object = MibScalar
pdu_meter2_VPK = _Pdu_meter2_VPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 16),
    _Pdu_meter2_VPK_Type()
)
pdu_meter2_VPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_VPK.setStatus("current")
_Pdu_meter2_PF_Type = Integer32
_Pdu_meter2_PF_Object = MibScalar
pdu_meter2_PF = _Pdu_meter2_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 17),
    _Pdu_meter2_PF_Type()
)
pdu_meter2_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_PF.setStatus("current")
_Pdu_meter2_Freq_Type = Integer32
_Pdu_meter2_Freq_Object = MibScalar
pdu_meter2_Freq = _Pdu_meter2_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 18),
    _Pdu_meter2_Freq_Type()
)
pdu_meter2_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter2_Freq.setStatus("current")
_Pdu_meter3_VRMS_Type = Integer32
_Pdu_meter3_VRMS_Object = MibScalar
pdu_meter3_VRMS = _Pdu_meter3_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 19),
    _Pdu_meter3_VRMS_Type()
)
pdu_meter3_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_VRMS.setStatus("current")
_Pdu_meter3_IRMS_Type = Integer32
_Pdu_meter3_IRMS_Object = MibScalar
pdu_meter3_IRMS = _Pdu_meter3_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 20),
    _Pdu_meter3_IRMS_Type()
)
pdu_meter3_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_IRMS.setStatus("current")
_Pdu_meter3_KWH_Type = Integer32
_Pdu_meter3_KWH_Object = MibScalar
pdu_meter3_KWH = _Pdu_meter3_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 21),
    _Pdu_meter3_KWH_Type()
)
pdu_meter3_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_KWH.setStatus("current")
_Pdu_meter3_KW_Type = Integer32
_Pdu_meter3_KW_Object = MibScalar
pdu_meter3_KW = _Pdu_meter3_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 22),
    _Pdu_meter3_KW_Type()
)
pdu_meter3_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_KW.setStatus("current")
_Pdu_meter3_TPMU_Type = Integer32
_Pdu_meter3_TPMU_Object = MibScalar
pdu_meter3_TPMU = _Pdu_meter3_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 23),
    _Pdu_meter3_TPMU_Type()
)
pdu_meter3_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_TPMU.setStatus("current")
_Pdu_meter3_IPK_Type = Integer32
_Pdu_meter3_IPK_Object = MibScalar
pdu_meter3_IPK = _Pdu_meter3_IPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 24),
    _Pdu_meter3_IPK_Type()
)
pdu_meter3_IPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_IPK.setStatus("current")
_Pdu_meter3_VPK_Type = Integer32
_Pdu_meter3_VPK_Object = MibScalar
pdu_meter3_VPK = _Pdu_meter3_VPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 25),
    _Pdu_meter3_VPK_Type()
)
pdu_meter3_VPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_VPK.setStatus("current")
_Pdu_meter3_PF_Type = Integer32
_Pdu_meter3_PF_Object = MibScalar
pdu_meter3_PF = _Pdu_meter3_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 26),
    _Pdu_meter3_PF_Type()
)
pdu_meter3_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_PF.setStatus("current")
_Pdu_meter3_Freq_Type = Integer32
_Pdu_meter3_Freq_Object = MibScalar
pdu_meter3_Freq = _Pdu_meter3_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 6, 27),
    _Pdu_meter3_Freq_Type()
)
pdu_meter3_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_meter3_Freq.setStatus("current")
_Pdu_sockets_ObjectIdentity = ObjectIdentity
pdu_sockets = _Pdu_sockets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7)
)
_Pdu_socketsTable_Object = MibTable
pdu_socketsTable = _Pdu_socketsTable_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1)
)
if mibBuilder.loadTexts:
    pdu_socketsTable.setStatus("current")
_Pdu_socketsEntry_Object = MibTableRow
pdu_socketsEntry = _Pdu_socketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1)
)
pdu_socketsEntry.setIndexNames(
    (0, "PDUSNMP", "socket-Index"),
)
if mibBuilder.loadTexts:
    pdu_socketsEntry.setStatus("current")


class _Socket_Index_Type(Integer32):
    """Custom type socket_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 47),
    )


_Socket_Index_Type.__name__ = "Integer32"
_Socket_Index_Object = MibScalar
socket_Index = _Socket_Index_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 1),
    _Socket_Index_Type()
)
socket_Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    socket_Index.setStatus("current")
_Socket_Number_Type = Integer32
_Socket_Number_Object = MibScalar
socket_Number = _Socket_Number_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 2),
    _Socket_Number_Type()
)
socket_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socket_Number.setStatus("current")
_Socket_Equipment_Type = DisplayString
_Socket_Equipment_Object = MibScalar
socket_Equipment = _Socket_Equipment_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 3),
    _Socket_Equipment_Type()
)
socket_Equipment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_Equipment.setStatus("current")


class _Socket_ONOFF_Type(Integer32):
    """Custom type socket_ONOFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Socket_ONOFF_Type.__name__ = "Integer32"
_Socket_ONOFF_Object = MibScalar
socket_ONOFF = _Socket_ONOFF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 4),
    _Socket_ONOFF_Type()
)
socket_ONOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_ONOFF.setStatus("current")
_Socket_AMPS_Type = Integer32
_Socket_AMPS_Object = MibScalar
socket_AMPS = _Socket_AMPS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 5),
    _Socket_AMPS_Type()
)
socket_AMPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socket_AMPS.setStatus("current")
_Socket_KWH_Type = Integer32
_Socket_KWH_Object = MibScalar
socket_KWH = _Socket_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 6),
    _Socket_KWH_Type()
)
socket_KWH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_KWH.setStatus("current")
_Socket_INFO_Type = Integer32
_Socket_INFO_Object = MibScalar
socket_INFO = _Socket_INFO_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 7, 1, 1, 7),
    _Socket_INFO_Type()
)
socket_INFO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    socket_INFO.setStatus("current")
_Pdu_Environmental_ObjectIdentity = ObjectIdentity
pdu_Environmental = _Pdu_Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8)
)
_Pdu_environmental_Temp1_Type = Integer32
_Pdu_environmental_Temp1_Object = MibScalar
pdu_environmental_Temp1 = _Pdu_environmental_Temp1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 1),
    _Pdu_environmental_Temp1_Type()
)
pdu_environmental_Temp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp1.setStatus("current")
_Pdu_environmental_Temp1_Location_Type = DisplayString
_Pdu_environmental_Temp1_Location_Object = MibScalar
pdu_environmental_Temp1_Location = _Pdu_environmental_Temp1_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 2),
    _Pdu_environmental_Temp1_Location_Type()
)
pdu_environmental_Temp1_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp1_Location.setStatus("current")
_Pdu_environmental_Temp2_Type = Integer32
_Pdu_environmental_Temp2_Object = MibScalar
pdu_environmental_Temp2 = _Pdu_environmental_Temp2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 3),
    _Pdu_environmental_Temp2_Type()
)
pdu_environmental_Temp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp2.setStatus("current")
_Pdu_environmental_Temp2_Location_Type = DisplayString
_Pdu_environmental_Temp2_Location_Object = MibScalar
pdu_environmental_Temp2_Location = _Pdu_environmental_Temp2_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 4),
    _Pdu_environmental_Temp2_Location_Type()
)
pdu_environmental_Temp2_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp2_Location.setStatus("current")
_Pdu_environmental_Temp3_Type = Integer32
_Pdu_environmental_Temp3_Object = MibScalar
pdu_environmental_Temp3 = _Pdu_environmental_Temp3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 5),
    _Pdu_environmental_Temp3_Type()
)
pdu_environmental_Temp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp3.setStatus("current")
_Pdu_environmental_Temp3_Location_Type = DisplayString
_Pdu_environmental_Temp3_Location_Object = MibScalar
pdu_environmental_Temp3_Location = _Pdu_environmental_Temp3_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 6),
    _Pdu_environmental_Temp3_Location_Type()
)
pdu_environmental_Temp3_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp3_Location.setStatus("current")
_Pdu_environmental_Temp4_Type = Integer32
_Pdu_environmental_Temp4_Object = MibScalar
pdu_environmental_Temp4 = _Pdu_environmental_Temp4_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 7),
    _Pdu_environmental_Temp4_Type()
)
pdu_environmental_Temp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp4.setStatus("current")
_Pdu_environmental_Temp4_Location_Type = DisplayString
_Pdu_environmental_Temp4_Location_Object = MibScalar
pdu_environmental_Temp4_Location = _Pdu_environmental_Temp4_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 8),
    _Pdu_environmental_Temp4_Location_Type()
)
pdu_environmental_Temp4_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp4_Location.setStatus("current")
_Pdu_environmental_Temp5_Type = Integer32
_Pdu_environmental_Temp5_Object = MibScalar
pdu_environmental_Temp5 = _Pdu_environmental_Temp5_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 9),
    _Pdu_environmental_Temp5_Type()
)
pdu_environmental_Temp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp5.setStatus("current")
_Pdu_environmental_Temp5_Location_Type = DisplayString
_Pdu_environmental_Temp5_Location_Object = MibScalar
pdu_environmental_Temp5_Location = _Pdu_environmental_Temp5_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 10),
    _Pdu_environmental_Temp5_Location_Type()
)
pdu_environmental_Temp5_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp5_Location.setStatus("current")
_Pdu_environmental_Temp6_Type = Integer32
_Pdu_environmental_Temp6_Object = MibScalar
pdu_environmental_Temp6 = _Pdu_environmental_Temp6_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 11),
    _Pdu_environmental_Temp6_Type()
)
pdu_environmental_Temp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp6.setStatus("current")
_Pdu_environmental_Temp6_Location_Type = DisplayString
_Pdu_environmental_Temp6_Location_Object = MibScalar
pdu_environmental_Temp6_Location = _Pdu_environmental_Temp6_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 12),
    _Pdu_environmental_Temp6_Location_Type()
)
pdu_environmental_Temp6_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp6_Location.setStatus("current")
_Pdu_environmental_Temp7_Type = Integer32
_Pdu_environmental_Temp7_Object = MibScalar
pdu_environmental_Temp7 = _Pdu_environmental_Temp7_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 13),
    _Pdu_environmental_Temp7_Type()
)
pdu_environmental_Temp7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp7.setStatus("current")
_Pdu_environmental_Temp7_Location_Type = DisplayString
_Pdu_environmental_Temp7_Location_Object = MibScalar
pdu_environmental_Temp7_Location = _Pdu_environmental_Temp7_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 14),
    _Pdu_environmental_Temp7_Location_Type()
)
pdu_environmental_Temp7_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp7_Location.setStatus("current")
_Pdu_environmental_Temp8_Type = Integer32
_Pdu_environmental_Temp8_Object = MibScalar
pdu_environmental_Temp8 = _Pdu_environmental_Temp8_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 15),
    _Pdu_environmental_Temp8_Type()
)
pdu_environmental_Temp8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Temp8.setStatus("current")
_Pdu_environmental_Temp8_Location_Type = DisplayString
_Pdu_environmental_Temp8_Location_Object = MibScalar
pdu_environmental_Temp8_Location = _Pdu_environmental_Temp8_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 16),
    _Pdu_environmental_Temp8_Location_Type()
)
pdu_environmental_Temp8_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Temp8_Location.setStatus("current")
_Pdu_environmental_HumidityTemp_Type = Integer32
_Pdu_environmental_HumidityTemp_Object = MibScalar
pdu_environmental_HumidityTemp = _Pdu_environmental_HumidityTemp_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 17),
    _Pdu_environmental_HumidityTemp_Type()
)
pdu_environmental_HumidityTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_HumidityTemp.setStatus("current")
_Pdu_environmental_Humidity_Type = Integer32
_Pdu_environmental_Humidity_Object = MibScalar
pdu_environmental_Humidity = _Pdu_environmental_Humidity_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 18),
    _Pdu_environmental_Humidity_Type()
)
pdu_environmental_Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Humidity.setStatus("current")


class _Pdu_environmental_Contact1_Type(Integer32):
    """Custom type pdu_environmental_Contact1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Pdu_environmental_Contact1_Type.__name__ = "Integer32"
_Pdu_environmental_Contact1_Object = MibScalar
pdu_environmental_Contact1 = _Pdu_environmental_Contact1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 19),
    _Pdu_environmental_Contact1_Type()
)
pdu_environmental_Contact1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Contact1.setStatus("current")
_Pdu_environmental_Contact1_Location_Type = DisplayString
_Pdu_environmental_Contact1_Location_Object = MibScalar
pdu_environmental_Contact1_Location = _Pdu_environmental_Contact1_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 20),
    _Pdu_environmental_Contact1_Location_Type()
)
pdu_environmental_Contact1_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Contact1_Location.setStatus("current")


class _Pdu_environmental_Contact2_Type(Integer32):
    """Custom type pdu_environmental_Contact2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Pdu_environmental_Contact2_Type.__name__ = "Integer32"
_Pdu_environmental_Contact2_Object = MibScalar
pdu_environmental_Contact2 = _Pdu_environmental_Contact2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 21),
    _Pdu_environmental_Contact2_Type()
)
pdu_environmental_Contact2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Contact2.setStatus("current")
_Pdu_environmental_Contact2_Location_Type = DisplayString
_Pdu_environmental_Contact2_Location_Object = MibScalar
pdu_environmental_Contact2_Location = _Pdu_environmental_Contact2_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 22),
    _Pdu_environmental_Contact2_Location_Type()
)
pdu_environmental_Contact2_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Contact2_Location.setStatus("current")


class _Pdu_environmental_Contact3_Type(Integer32):
    """Custom type pdu_environmental_Contact3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Pdu_environmental_Contact3_Type.__name__ = "Integer32"
_Pdu_environmental_Contact3_Object = MibScalar
pdu_environmental_Contact3 = _Pdu_environmental_Contact3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 23),
    _Pdu_environmental_Contact3_Type()
)
pdu_environmental_Contact3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_environmental_Contact3.setStatus("current")
_Pdu_environmental_Contact3_Location_Type = DisplayString
_Pdu_environmental_Contact3_Location_Object = MibScalar
pdu_environmental_Contact3_Location = _Pdu_environmental_Contact3_Location_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 8, 24),
    _Pdu_environmental_Contact3_Location_Type()
)
pdu_environmental_Contact3_Location.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_environmental_Contact3_Location.setStatus("current")
_Pdu_Security_ObjectIdentity = ObjectIdentity
pdu_Security = _Pdu_Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9)
)


class _Pdu_Security_Door_Type(Integer32):
    """Custom type pdu_Security_Door based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Pdu_Security_Door_Type.__name__ = "Integer32"
_Pdu_Security_Door_Object = MibScalar
pdu_Security_Door = _Pdu_Security_Door_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 1),
    _Pdu_Security_Door_Type()
)
pdu_Security_Door.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_Security_Door.setStatus("current")


class _Pdu_Security_Lock_Type(Integer32):
    """Custom type pdu_Security_Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Pdu_Security_Lock_Type.__name__ = "Integer32"
_Pdu_Security_Lock_Object = MibScalar
pdu_Security_Lock = _Pdu_Security_Lock_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 2),
    _Pdu_Security_Lock_Type()
)
pdu_Security_Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_Security_Lock.setStatus("current")


class _Pdu_Security_Wild_Type(Integer32):
    """Custom type pdu_Security_Wild based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Pdu_Security_Wild_Type.__name__ = "Integer32"
_Pdu_Security_Wild_Object = MibScalar
pdu_Security_Wild = _Pdu_Security_Wild_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 3),
    _Pdu_Security_Wild_Type()
)
pdu_Security_Wild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_Security_Wild.setStatus("current")
_Pdu_Security_UnlockTimeDate_Type = DisplayString
_Pdu_Security_UnlockTimeDate_Object = MibScalar
pdu_Security_UnlockTimeDate = _Pdu_Security_UnlockTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 4),
    _Pdu_Security_UnlockTimeDate_Type()
)
pdu_Security_UnlockTimeDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_Security_UnlockTimeDate.setStatus("current")
_Pdu_SecurityTable_Object = MibTable
pdu_SecurityTable = _Pdu_SecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 5)
)
if mibBuilder.loadTexts:
    pdu_SecurityTable.setStatus("current")
_Pdu_SecurityEntry_Object = MibTableRow
pdu_SecurityEntry = _Pdu_SecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 5, 1)
)
pdu_SecurityEntry.setIndexNames(
    (0, "PDUSNMP", "pdu-Security-Index"),
)
if mibBuilder.loadTexts:
    pdu_SecurityEntry.setStatus("current")


class _Pdu_Security_Index_Type(Integer32):
    """Custom type pdu_Security_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Pdu_Security_Index_Type.__name__ = "Integer32"
_Pdu_Security_Index_Object = MibScalar
pdu_Security_Index = _Pdu_Security_Index_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 5, 1, 1),
    _Pdu_Security_Index_Type()
)
pdu_Security_Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdu_Security_Index.setStatus("current")
_Pdu_Security_Code_Type = Integer32
_Pdu_Security_Code_Object = MibScalar
pdu_Security_Code = _Pdu_Security_Code_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 9, 5, 1, 2),
    _Pdu_Security_Code_Type()
)
pdu_Security_Code.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_Security_Code.setStatus("current")
_Pdu_Logs_ObjectIdentity = ObjectIdentity
pdu_Logs = _Pdu_Logs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 10)
)
_Pdu_Logs_Number_Type = Integer32
_Pdu_Logs_Number_Object = MibScalar
pdu_Logs_Number = _Pdu_Logs_Number_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 10, 1),
    _Pdu_Logs_Number_Type()
)
pdu_Logs_Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_Logs_Number.setStatus("current")
_Pdu_Logs_Index_Type = Integer32
_Pdu_Logs_Index_Object = MibScalar
pdu_Logs_Index = _Pdu_Logs_Index_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 10, 2),
    _Pdu_Logs_Index_Type()
)
pdu_Logs_Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_Logs_Index.setStatus("current")
_Pdu_Logs_Data_Type = DisplayString
_Pdu_Logs_Data_Object = MibScalar
pdu_Logs_Data = _Pdu_Logs_Data_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 10, 3),
    _Pdu_Logs_Data_Type()
)
pdu_Logs_Data.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdu_Logs_Data.setStatus("current")


class _Pdu_Logs_Clear_Type(Integer32):
    """Custom type pdu_Logs_Clear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_Pdu_Logs_Clear_Type.__name__ = "Integer32"
_Pdu_Logs_Clear_Object = MibScalar
pdu_Logs_Clear = _Pdu_Logs_Clear_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 10, 4),
    _Pdu_Logs_Clear_Type()
)
pdu_Logs_Clear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdu_Logs_Clear.setStatus("current")
_Pdu_Traps_ObjectIdentity = ObjectIdentity
pdu_Traps = _Pdu_Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11)
)
_Pdu_TrapThresholds_ObjectIdentity = ObjectIdentity
pdu_TrapThresholds = _Pdu_TrapThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1)
)


class _Meter1_VRMSLowAlarm_Type(Integer32):
    """Custom type meter1_VRMSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_VRMSLowAlarm_Type.__name__ = "Integer32"
_Meter1_VRMSLowAlarm_Object = MibScalar
meter1_VRMSLowAlarm = _Meter1_VRMSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 1),
    _Meter1_VRMSLowAlarm_Type()
)
meter1_VRMSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_VRMSLowAlarm.setStatus("current")
_Meter1_VRMSLow_Type = Integer32
_Meter1_VRMSLow_Object = MibScalar
meter1_VRMSLow = _Meter1_VRMSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 2),
    _Meter1_VRMSLow_Type()
)
meter1_VRMSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_VRMSLow.setStatus("current")


class _Meter1_VRMSHighAlarm_Type(Integer32):
    """Custom type meter1_VRMSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_VRMSHighAlarm_Type.__name__ = "Integer32"
_Meter1_VRMSHighAlarm_Object = MibScalar
meter1_VRMSHighAlarm = _Meter1_VRMSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 3),
    _Meter1_VRMSHighAlarm_Type()
)
meter1_VRMSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_VRMSHighAlarm.setStatus("current")
_Meter1_VRMSHigh_Type = Integer32
_Meter1_VRMSHigh_Object = MibScalar
meter1_VRMSHigh = _Meter1_VRMSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 4),
    _Meter1_VRMSHigh_Type()
)
meter1_VRMSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_VRMSHigh.setStatus("current")


class _Meter1_IRMSLowAlarm_Type(Integer32):
    """Custom type meter1_IRMSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_IRMSLowAlarm_Type.__name__ = "Integer32"
_Meter1_IRMSLowAlarm_Object = MibScalar
meter1_IRMSLowAlarm = _Meter1_IRMSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 5),
    _Meter1_IRMSLowAlarm_Type()
)
meter1_IRMSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_IRMSLowAlarm.setStatus("current")
_Meter1_IRMSLow_Type = Integer32
_Meter1_IRMSLow_Object = MibScalar
meter1_IRMSLow = _Meter1_IRMSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 6),
    _Meter1_IRMSLow_Type()
)
meter1_IRMSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_IRMSLow.setStatus("current")


class _Meter1_IRMSHighAlarm_Type(Integer32):
    """Custom type meter1_IRMSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_IRMSHighAlarm_Type.__name__ = "Integer32"
_Meter1_IRMSHighAlarm_Object = MibScalar
meter1_IRMSHighAlarm = _Meter1_IRMSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 7),
    _Meter1_IRMSHighAlarm_Type()
)
meter1_IRMSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_IRMSHighAlarm.setStatus("current")
_Meter1_IRMSHigh_Type = Integer32
_Meter1_IRMSHigh_Object = MibScalar
meter1_IRMSHigh = _Meter1_IRMSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 8),
    _Meter1_IRMSHigh_Type()
)
meter1_IRMSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_IRMSHigh.setStatus("current")


class _Meter1_KWSLowAlarm_Type(Integer32):
    """Custom type meter1_KWSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_KWSLowAlarm_Type.__name__ = "Integer32"
_Meter1_KWSLowAlarm_Object = MibScalar
meter1_KWSLowAlarm = _Meter1_KWSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 9),
    _Meter1_KWSLowAlarm_Type()
)
meter1_KWSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_KWSLowAlarm.setStatus("current")
_Meter1_KWSLow_Type = Integer32
_Meter1_KWSLow_Object = MibScalar
meter1_KWSLow = _Meter1_KWSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 10),
    _Meter1_KWSLow_Type()
)
meter1_KWSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_KWSLow.setStatus("current")


class _Meter1_KWSHighAlarm_Type(Integer32):
    """Custom type meter1_KWSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_KWSHighAlarm_Type.__name__ = "Integer32"
_Meter1_KWSHighAlarm_Object = MibScalar
meter1_KWSHighAlarm = _Meter1_KWSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 11),
    _Meter1_KWSHighAlarm_Type()
)
meter1_KWSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_KWSHighAlarm.setStatus("current")
_Meter1_KWSHigh_Type = Integer32
_Meter1_KWSHigh_Object = MibScalar
meter1_KWSHigh = _Meter1_KWSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 12),
    _Meter1_KWSHigh_Type()
)
meter1_KWSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_KWSHigh.setStatus("current")


class _Meter1_TempLowAlarm_Type(Integer32):
    """Custom type meter1_TempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_TempLowAlarm_Type.__name__ = "Integer32"
_Meter1_TempLowAlarm_Object = MibScalar
meter1_TempLowAlarm = _Meter1_TempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 13),
    _Meter1_TempLowAlarm_Type()
)
meter1_TempLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_TempLowAlarm.setStatus("current")
_Meter1_TempLow_Type = Integer32
_Meter1_TempLow_Object = MibScalar
meter1_TempLow = _Meter1_TempLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 14),
    _Meter1_TempLow_Type()
)
meter1_TempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_TempLow.setStatus("current")


class _Meter1_TempHighAlarm_Type(Integer32):
    """Custom type meter1_TempHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_TempHighAlarm_Type.__name__ = "Integer32"
_Meter1_TempHighAlarm_Object = MibScalar
meter1_TempHighAlarm = _Meter1_TempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 15),
    _Meter1_TempHighAlarm_Type()
)
meter1_TempHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_TempHighAlarm.setStatus("current")
_Meter1_TempHigh_Type = Integer32
_Meter1_TempHigh_Object = MibScalar
meter1_TempHigh = _Meter1_TempHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 16),
    _Meter1_TempHigh_Type()
)
meter1_TempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_TempHigh.setStatus("current")


class _Meter1_PFLowAlarm_Type(Integer32):
    """Custom type meter1_PFLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_PFLowAlarm_Type.__name__ = "Integer32"
_Meter1_PFLowAlarm_Object = MibScalar
meter1_PFLowAlarm = _Meter1_PFLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 17),
    _Meter1_PFLowAlarm_Type()
)
meter1_PFLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_PFLowAlarm.setStatus("current")
_Meter1_PFLow_Type = Integer32
_Meter1_PFLow_Object = MibScalar
meter1_PFLow = _Meter1_PFLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 18),
    _Meter1_PFLow_Type()
)
meter1_PFLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_PFLow.setStatus("current")


class _Meter1_PFHighAlarm_Type(Integer32):
    """Custom type meter1_PFHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_PFHighAlarm_Type.__name__ = "Integer32"
_Meter1_PFHighAlarm_Object = MibScalar
meter1_PFHighAlarm = _Meter1_PFHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 19),
    _Meter1_PFHighAlarm_Type()
)
meter1_PFHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_PFHighAlarm.setStatus("current")
_Meter1_PFHigh_Type = Integer32
_Meter1_PFHigh_Object = MibScalar
meter1_PFHigh = _Meter1_PFHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 20),
    _Meter1_PFHigh_Type()
)
meter1_PFHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_PFHigh.setStatus("current")


class _Meter1_FreqLowAlarm_Type(Integer32):
    """Custom type meter1_FreqLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_FreqLowAlarm_Type.__name__ = "Integer32"
_Meter1_FreqLowAlarm_Object = MibScalar
meter1_FreqLowAlarm = _Meter1_FreqLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 21),
    _Meter1_FreqLowAlarm_Type()
)
meter1_FreqLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_FreqLowAlarm.setStatus("current")
_Meter1_FreqLow_Type = Integer32
_Meter1_FreqLow_Object = MibScalar
meter1_FreqLow = _Meter1_FreqLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 22),
    _Meter1_FreqLow_Type()
)
meter1_FreqLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_FreqLow.setStatus("current")


class _Meter1_FreqHighAlarm_Type(Integer32):
    """Custom type meter1_FreqHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter1_FreqHighAlarm_Type.__name__ = "Integer32"
_Meter1_FreqHighAlarm_Object = MibScalar
meter1_FreqHighAlarm = _Meter1_FreqHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 23),
    _Meter1_FreqHighAlarm_Type()
)
meter1_FreqHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_FreqHighAlarm.setStatus("current")
_Meter1_FreqHigh_Type = Integer32
_Meter1_FreqHigh_Object = MibScalar
meter1_FreqHigh = _Meter1_FreqHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 24),
    _Meter1_FreqHigh_Type()
)
meter1_FreqHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter1_FreqHigh.setStatus("current")


class _Meter2_VRMSLowAlarm_Type(Integer32):
    """Custom type meter2_VRMSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_VRMSLowAlarm_Type.__name__ = "Integer32"
_Meter2_VRMSLowAlarm_Object = MibScalar
meter2_VRMSLowAlarm = _Meter2_VRMSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 25),
    _Meter2_VRMSLowAlarm_Type()
)
meter2_VRMSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_VRMSLowAlarm.setStatus("current")
_Meter2_VRMSLow_Type = Integer32
_Meter2_VRMSLow_Object = MibScalar
meter2_VRMSLow = _Meter2_VRMSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 26),
    _Meter2_VRMSLow_Type()
)
meter2_VRMSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_VRMSLow.setStatus("current")


class _Meter2_VRMSHighAlarm_Type(Integer32):
    """Custom type meter2_VRMSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_VRMSHighAlarm_Type.__name__ = "Integer32"
_Meter2_VRMSHighAlarm_Object = MibScalar
meter2_VRMSHighAlarm = _Meter2_VRMSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 27),
    _Meter2_VRMSHighAlarm_Type()
)
meter2_VRMSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_VRMSHighAlarm.setStatus("current")
_Meter2_VRMSHigh_Type = Integer32
_Meter2_VRMSHigh_Object = MibScalar
meter2_VRMSHigh = _Meter2_VRMSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 28),
    _Meter2_VRMSHigh_Type()
)
meter2_VRMSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_VRMSHigh.setStatus("current")


class _Meter2_IRMSLowAlarm_Type(Integer32):
    """Custom type meter2_IRMSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_IRMSLowAlarm_Type.__name__ = "Integer32"
_Meter2_IRMSLowAlarm_Object = MibScalar
meter2_IRMSLowAlarm = _Meter2_IRMSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 29),
    _Meter2_IRMSLowAlarm_Type()
)
meter2_IRMSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_IRMSLowAlarm.setStatus("current")
_Meter2_IRMSLow_Type = Integer32
_Meter2_IRMSLow_Object = MibScalar
meter2_IRMSLow = _Meter2_IRMSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 30),
    _Meter2_IRMSLow_Type()
)
meter2_IRMSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_IRMSLow.setStatus("current")


class _Meter2_IRMSHighAlarm_Type(Integer32):
    """Custom type meter2_IRMSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_IRMSHighAlarm_Type.__name__ = "Integer32"
_Meter2_IRMSHighAlarm_Object = MibScalar
meter2_IRMSHighAlarm = _Meter2_IRMSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 31),
    _Meter2_IRMSHighAlarm_Type()
)
meter2_IRMSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_IRMSHighAlarm.setStatus("current")
_Meter2_IRMSHigh_Type = Integer32
_Meter2_IRMSHigh_Object = MibScalar
meter2_IRMSHigh = _Meter2_IRMSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 32),
    _Meter2_IRMSHigh_Type()
)
meter2_IRMSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_IRMSHigh.setStatus("current")


class _Meter2_KWSLowAlarm_Type(Integer32):
    """Custom type meter2_KWSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_KWSLowAlarm_Type.__name__ = "Integer32"
_Meter2_KWSLowAlarm_Object = MibScalar
meter2_KWSLowAlarm = _Meter2_KWSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 33),
    _Meter2_KWSLowAlarm_Type()
)
meter2_KWSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_KWSLowAlarm.setStatus("current")
_Meter2_KWSLow_Type = Integer32
_Meter2_KWSLow_Object = MibScalar
meter2_KWSLow = _Meter2_KWSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 34),
    _Meter2_KWSLow_Type()
)
meter2_KWSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_KWSLow.setStatus("current")


class _Meter2_KWSHighAlarm_Type(Integer32):
    """Custom type meter2_KWSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_KWSHighAlarm_Type.__name__ = "Integer32"
_Meter2_KWSHighAlarm_Object = MibScalar
meter2_KWSHighAlarm = _Meter2_KWSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 35),
    _Meter2_KWSHighAlarm_Type()
)
meter2_KWSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_KWSHighAlarm.setStatus("current")
_Meter2_KWSHigh_Type = Integer32
_Meter2_KWSHigh_Object = MibScalar
meter2_KWSHigh = _Meter2_KWSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 36),
    _Meter2_KWSHigh_Type()
)
meter2_KWSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_KWSHigh.setStatus("current")


class _Meter2_TempLowAlarm_Type(Integer32):
    """Custom type meter2_TempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_TempLowAlarm_Type.__name__ = "Integer32"
_Meter2_TempLowAlarm_Object = MibScalar
meter2_TempLowAlarm = _Meter2_TempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 37),
    _Meter2_TempLowAlarm_Type()
)
meter2_TempLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_TempLowAlarm.setStatus("current")
_Meter2_TempLow_Type = Integer32
_Meter2_TempLow_Object = MibScalar
meter2_TempLow = _Meter2_TempLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 38),
    _Meter2_TempLow_Type()
)
meter2_TempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_TempLow.setStatus("current")


class _Meter2_TempHighAlarm_Type(Integer32):
    """Custom type meter2_TempHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_TempHighAlarm_Type.__name__ = "Integer32"
_Meter2_TempHighAlarm_Object = MibScalar
meter2_TempHighAlarm = _Meter2_TempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 39),
    _Meter2_TempHighAlarm_Type()
)
meter2_TempHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_TempHighAlarm.setStatus("current")
_Meter2_TempHigh_Type = Integer32
_Meter2_TempHigh_Object = MibScalar
meter2_TempHigh = _Meter2_TempHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 40),
    _Meter2_TempHigh_Type()
)
meter2_TempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_TempHigh.setStatus("current")


class _Meter2_PFLowAlarm_Type(Integer32):
    """Custom type meter2_PFLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_PFLowAlarm_Type.__name__ = "Integer32"
_Meter2_PFLowAlarm_Object = MibScalar
meter2_PFLowAlarm = _Meter2_PFLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 41),
    _Meter2_PFLowAlarm_Type()
)
meter2_PFLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_PFLowAlarm.setStatus("current")
_Meter2_PFLow_Type = Integer32
_Meter2_PFLow_Object = MibScalar
meter2_PFLow = _Meter2_PFLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 42),
    _Meter2_PFLow_Type()
)
meter2_PFLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_PFLow.setStatus("current")


class _Meter2_PFHighAlarm_Type(Integer32):
    """Custom type meter2_PFHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_PFHighAlarm_Type.__name__ = "Integer32"
_Meter2_PFHighAlarm_Object = MibScalar
meter2_PFHighAlarm = _Meter2_PFHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 43),
    _Meter2_PFHighAlarm_Type()
)
meter2_PFHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_PFHighAlarm.setStatus("current")
_Meter2_PFHigh_Type = Integer32
_Meter2_PFHigh_Object = MibScalar
meter2_PFHigh = _Meter2_PFHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 44),
    _Meter2_PFHigh_Type()
)
meter2_PFHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_PFHigh.setStatus("current")


class _Meter2_FreqLowAlarm_Type(Integer32):
    """Custom type meter2_FreqLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_FreqLowAlarm_Type.__name__ = "Integer32"
_Meter2_FreqLowAlarm_Object = MibScalar
meter2_FreqLowAlarm = _Meter2_FreqLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 45),
    _Meter2_FreqLowAlarm_Type()
)
meter2_FreqLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_FreqLowAlarm.setStatus("current")
_Meter2_FreqLow_Type = Integer32
_Meter2_FreqLow_Object = MibScalar
meter2_FreqLow = _Meter2_FreqLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 46),
    _Meter2_FreqLow_Type()
)
meter2_FreqLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_FreqLow.setStatus("current")


class _Meter2_FreqHighAlarm_Type(Integer32):
    """Custom type meter2_FreqHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter2_FreqHighAlarm_Type.__name__ = "Integer32"
_Meter2_FreqHighAlarm_Object = MibScalar
meter2_FreqHighAlarm = _Meter2_FreqHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 47),
    _Meter2_FreqHighAlarm_Type()
)
meter2_FreqHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_FreqHighAlarm.setStatus("current")
_Meter2_FreqHigh_Type = Integer32
_Meter2_FreqHigh_Object = MibScalar
meter2_FreqHigh = _Meter2_FreqHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 48),
    _Meter2_FreqHigh_Type()
)
meter2_FreqHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter2_FreqHigh.setStatus("current")


class _Meter3_VRMSLowAlarm_Type(Integer32):
    """Custom type meter3_VRMSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_VRMSLowAlarm_Type.__name__ = "Integer32"
_Meter3_VRMSLowAlarm_Object = MibScalar
meter3_VRMSLowAlarm = _Meter3_VRMSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 49),
    _Meter3_VRMSLowAlarm_Type()
)
meter3_VRMSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_VRMSLowAlarm.setStatus("current")
_Meter3_VRMSLow_Type = Integer32
_Meter3_VRMSLow_Object = MibScalar
meter3_VRMSLow = _Meter3_VRMSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 50),
    _Meter3_VRMSLow_Type()
)
meter3_VRMSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_VRMSLow.setStatus("current")


class _Meter3_VRMSHighAlarm_Type(Integer32):
    """Custom type meter3_VRMSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_VRMSHighAlarm_Type.__name__ = "Integer32"
_Meter3_VRMSHighAlarm_Object = MibScalar
meter3_VRMSHighAlarm = _Meter3_VRMSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 51),
    _Meter3_VRMSHighAlarm_Type()
)
meter3_VRMSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_VRMSHighAlarm.setStatus("current")
_Meter3_VRMSHigh_Type = Integer32
_Meter3_VRMSHigh_Object = MibScalar
meter3_VRMSHigh = _Meter3_VRMSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 52),
    _Meter3_VRMSHigh_Type()
)
meter3_VRMSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_VRMSHigh.setStatus("current")


class _Meter3_IRMSLowAlarm_Type(Integer32):
    """Custom type meter3_IRMSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_IRMSLowAlarm_Type.__name__ = "Integer32"
_Meter3_IRMSLowAlarm_Object = MibScalar
meter3_IRMSLowAlarm = _Meter3_IRMSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 53),
    _Meter3_IRMSLowAlarm_Type()
)
meter3_IRMSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_IRMSLowAlarm.setStatus("current")
_Meter3_IRMSLow_Type = Integer32
_Meter3_IRMSLow_Object = MibScalar
meter3_IRMSLow = _Meter3_IRMSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 54),
    _Meter3_IRMSLow_Type()
)
meter3_IRMSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_IRMSLow.setStatus("current")


class _Meter3_IRMSHighAlarm_Type(Integer32):
    """Custom type meter3_IRMSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_IRMSHighAlarm_Type.__name__ = "Integer32"
_Meter3_IRMSHighAlarm_Object = MibScalar
meter3_IRMSHighAlarm = _Meter3_IRMSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 55),
    _Meter3_IRMSHighAlarm_Type()
)
meter3_IRMSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_IRMSHighAlarm.setStatus("current")
_Meter3_IRMSHigh_Type = Integer32
_Meter3_IRMSHigh_Object = MibScalar
meter3_IRMSHigh = _Meter3_IRMSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 56),
    _Meter3_IRMSHigh_Type()
)
meter3_IRMSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_IRMSHigh.setStatus("current")


class _Meter3_KWSLowAlarm_Type(Integer32):
    """Custom type meter3_KWSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_KWSLowAlarm_Type.__name__ = "Integer32"
_Meter3_KWSLowAlarm_Object = MibScalar
meter3_KWSLowAlarm = _Meter3_KWSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 57),
    _Meter3_KWSLowAlarm_Type()
)
meter3_KWSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_KWSLowAlarm.setStatus("current")
_Meter3_KWSLow_Type = Integer32
_Meter3_KWSLow_Object = MibScalar
meter3_KWSLow = _Meter3_KWSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 58),
    _Meter3_KWSLow_Type()
)
meter3_KWSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_KWSLow.setStatus("current")


class _Meter3_KWSHighAlarm_Type(Integer32):
    """Custom type meter3_KWSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_KWSHighAlarm_Type.__name__ = "Integer32"
_Meter3_KWSHighAlarm_Object = MibScalar
meter3_KWSHighAlarm = _Meter3_KWSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 59),
    _Meter3_KWSHighAlarm_Type()
)
meter3_KWSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_KWSHighAlarm.setStatus("current")
_Meter3_KWSHigh_Type = Integer32
_Meter3_KWSHigh_Object = MibScalar
meter3_KWSHigh = _Meter3_KWSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 60),
    _Meter3_KWSHigh_Type()
)
meter3_KWSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_KWSHigh.setStatus("current")


class _Meter3_TempLowAlarm_Type(Integer32):
    """Custom type meter3_TempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_TempLowAlarm_Type.__name__ = "Integer32"
_Meter3_TempLowAlarm_Object = MibScalar
meter3_TempLowAlarm = _Meter3_TempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 61),
    _Meter3_TempLowAlarm_Type()
)
meter3_TempLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_TempLowAlarm.setStatus("current")
_Meter3_TempLow_Type = Integer32
_Meter3_TempLow_Object = MibScalar
meter3_TempLow = _Meter3_TempLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 62),
    _Meter3_TempLow_Type()
)
meter3_TempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_TempLow.setStatus("current")


class _Meter3_TempHighAlarm_Type(Integer32):
    """Custom type meter3_TempHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_TempHighAlarm_Type.__name__ = "Integer32"
_Meter3_TempHighAlarm_Object = MibScalar
meter3_TempHighAlarm = _Meter3_TempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 63),
    _Meter3_TempHighAlarm_Type()
)
meter3_TempHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_TempHighAlarm.setStatus("current")
_Meter3_TempHigh_Type = Integer32
_Meter3_TempHigh_Object = MibScalar
meter3_TempHigh = _Meter3_TempHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 64),
    _Meter3_TempHigh_Type()
)
meter3_TempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_TempHigh.setStatus("current")


class _Meter3_PFLowAlarm_Type(Integer32):
    """Custom type meter3_PFLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_PFLowAlarm_Type.__name__ = "Integer32"
_Meter3_PFLowAlarm_Object = MibScalar
meter3_PFLowAlarm = _Meter3_PFLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 65),
    _Meter3_PFLowAlarm_Type()
)
meter3_PFLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_PFLowAlarm.setStatus("current")
_Meter3_PFLow_Type = Integer32
_Meter3_PFLow_Object = MibScalar
meter3_PFLow = _Meter3_PFLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 66),
    _Meter3_PFLow_Type()
)
meter3_PFLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_PFLow.setStatus("current")


class _Meter3_PFHighAlarm_Type(Integer32):
    """Custom type meter3_PFHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_PFHighAlarm_Type.__name__ = "Integer32"
_Meter3_PFHighAlarm_Object = MibScalar
meter3_PFHighAlarm = _Meter3_PFHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 67),
    _Meter3_PFHighAlarm_Type()
)
meter3_PFHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_PFHighAlarm.setStatus("current")
_Meter3_PFHigh_Type = Integer32
_Meter3_PFHigh_Object = MibScalar
meter3_PFHigh = _Meter3_PFHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 68),
    _Meter3_PFHigh_Type()
)
meter3_PFHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_PFHigh.setStatus("current")


class _Meter3_FreqLowAlarm_Type(Integer32):
    """Custom type meter3_FreqLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_FreqLowAlarm_Type.__name__ = "Integer32"
_Meter3_FreqLowAlarm_Object = MibScalar
meter3_FreqLowAlarm = _Meter3_FreqLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 69),
    _Meter3_FreqLowAlarm_Type()
)
meter3_FreqLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_FreqLowAlarm.setStatus("current")
_Meter3_FreqLow_Type = Integer32
_Meter3_FreqLow_Object = MibScalar
meter3_FreqLow = _Meter3_FreqLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 70),
    _Meter3_FreqLow_Type()
)
meter3_FreqLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_FreqLow.setStatus("current")


class _Meter3_FreqHighAlarm_Type(Integer32):
    """Custom type meter3_FreqHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Meter3_FreqHighAlarm_Type.__name__ = "Integer32"
_Meter3_FreqHighAlarm_Object = MibScalar
meter3_FreqHighAlarm = _Meter3_FreqHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 71),
    _Meter3_FreqHighAlarm_Type()
)
meter3_FreqHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_FreqHighAlarm.setStatus("current")
_Meter3_FreqHigh_Type = Integer32
_Meter3_FreqHigh_Object = MibScalar
meter3_FreqHigh = _Meter3_FreqHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 72),
    _Meter3_FreqHigh_Type()
)
meter3_FreqHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    meter3_FreqHigh.setStatus("current")
_Socket_ThresholdsTable_Object = MibTable
socket_ThresholdsTable = _Socket_ThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73)
)
if mibBuilder.loadTexts:
    socket_ThresholdsTable.setStatus("current")
_Socket_ThresholdsEntry_Object = MibTableRow
socket_ThresholdsEntry = _Socket_ThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73, 1)
)
socket_ThresholdsEntry.setIndexNames(
    (0, "PDUSNMP", "socket-ThresholdsNumber"),
)
if mibBuilder.loadTexts:
    socket_ThresholdsEntry.setStatus("current")


class _Socket_ThresholdsNumber_Type(Integer32):
    """Custom type socket_ThresholdsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_Socket_ThresholdsNumber_Type.__name__ = "Integer32"
_Socket_ThresholdsNumber_Object = MibScalar
socket_ThresholdsNumber = _Socket_ThresholdsNumber_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73, 1, 1),
    _Socket_ThresholdsNumber_Type()
)
socket_ThresholdsNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    socket_ThresholdsNumber.setStatus("current")


class _Socket_AMPSLowAlarm_Type(Integer32):
    """Custom type socket_AMPSLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Socket_AMPSLowAlarm_Type.__name__ = "Integer32"
_Socket_AMPSLowAlarm_Object = MibScalar
socket_AMPSLowAlarm = _Socket_AMPSLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73, 1, 2),
    _Socket_AMPSLowAlarm_Type()
)
socket_AMPSLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_AMPSLowAlarm.setStatus("current")
_Socket_AMPSLow_Type = Integer32
_Socket_AMPSLow_Object = MibScalar
socket_AMPSLow = _Socket_AMPSLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73, 1, 3),
    _Socket_AMPSLow_Type()
)
socket_AMPSLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_AMPSLow.setStatus("current")


class _Socket_AMPSHighAlarm_Type(Integer32):
    """Custom type socket_AMPSHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Socket_AMPSHighAlarm_Type.__name__ = "Integer32"
_Socket_AMPSHighAlarm_Object = MibScalar
socket_AMPSHighAlarm = _Socket_AMPSHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73, 1, 4),
    _Socket_AMPSHighAlarm_Type()
)
socket_AMPSHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_AMPSHighAlarm.setStatus("current")
_Socket_AMPSHigh_Type = Integer32
_Socket_AMPSHigh_Object = MibScalar
socket_AMPSHigh = _Socket_AMPSHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 73, 1, 5),
    _Socket_AMPSHigh_Type()
)
socket_AMPSHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_AMPSHigh.setStatus("current")


class _Environmental_Temp1LowAlarm_Type(Integer32):
    """Custom type environmental_Temp1LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp1LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp1LowAlarm_Object = MibScalar
environmental_Temp1LowAlarm = _Environmental_Temp1LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 74),
    _Environmental_Temp1LowAlarm_Type()
)
environmental_Temp1LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp1LowAlarm.setStatus("current")
_Environmental_Temp1Low_Type = Integer32
_Environmental_Temp1Low_Object = MibScalar
environmental_Temp1Low = _Environmental_Temp1Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 75),
    _Environmental_Temp1Low_Type()
)
environmental_Temp1Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp1Low.setStatus("current")


class _Environmental_Temp1HighAlarm_Type(Integer32):
    """Custom type environmental_Temp1HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp1HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp1HighAlarm_Object = MibScalar
environmental_Temp1HighAlarm = _Environmental_Temp1HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 76),
    _Environmental_Temp1HighAlarm_Type()
)
environmental_Temp1HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp1HighAlarm.setStatus("current")
_Environmental_Temp1High_Type = Integer32
_Environmental_Temp1High_Object = MibScalar
environmental_Temp1High = _Environmental_Temp1High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 77),
    _Environmental_Temp1High_Type()
)
environmental_Temp1High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp1High.setStatus("current")


class _Environmental_Temp2LowAlarm_Type(Integer32):
    """Custom type environmental_Temp2LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp2LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp2LowAlarm_Object = MibScalar
environmental_Temp2LowAlarm = _Environmental_Temp2LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 78),
    _Environmental_Temp2LowAlarm_Type()
)
environmental_Temp2LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp2LowAlarm.setStatus("current")
_Environmental_Temp2Low_Type = Integer32
_Environmental_Temp2Low_Object = MibScalar
environmental_Temp2Low = _Environmental_Temp2Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 79),
    _Environmental_Temp2Low_Type()
)
environmental_Temp2Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp2Low.setStatus("current")


class _Environmental_Temp2HighAlarm_Type(Integer32):
    """Custom type environmental_Temp2HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp2HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp2HighAlarm_Object = MibScalar
environmental_Temp2HighAlarm = _Environmental_Temp2HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 80),
    _Environmental_Temp2HighAlarm_Type()
)
environmental_Temp2HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp2HighAlarm.setStatus("current")
_Environmental_Temp2High_Type = Integer32
_Environmental_Temp2High_Object = MibScalar
environmental_Temp2High = _Environmental_Temp2High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 81),
    _Environmental_Temp2High_Type()
)
environmental_Temp2High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp2High.setStatus("current")


class _Environmental_Temp3LowAlarm_Type(Integer32):
    """Custom type environmental_Temp3LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp3LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp3LowAlarm_Object = MibScalar
environmental_Temp3LowAlarm = _Environmental_Temp3LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 82),
    _Environmental_Temp3LowAlarm_Type()
)
environmental_Temp3LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp3LowAlarm.setStatus("current")
_Environmental_Temp3Low_Type = Integer32
_Environmental_Temp3Low_Object = MibScalar
environmental_Temp3Low = _Environmental_Temp3Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 83),
    _Environmental_Temp3Low_Type()
)
environmental_Temp3Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp3Low.setStatus("current")


class _Environmental_Temp3HighAlarm_Type(Integer32):
    """Custom type environmental_Temp3HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp3HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp3HighAlarm_Object = MibScalar
environmental_Temp3HighAlarm = _Environmental_Temp3HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 84),
    _Environmental_Temp3HighAlarm_Type()
)
environmental_Temp3HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp3HighAlarm.setStatus("current")
_Environmental_Temp3High_Type = Integer32
_Environmental_Temp3High_Object = MibScalar
environmental_Temp3High = _Environmental_Temp3High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 85),
    _Environmental_Temp3High_Type()
)
environmental_Temp3High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp3High.setStatus("current")


class _Environmental_Temp4LowAlarm_Type(Integer32):
    """Custom type environmental_Temp4LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp4LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp4LowAlarm_Object = MibScalar
environmental_Temp4LowAlarm = _Environmental_Temp4LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 86),
    _Environmental_Temp4LowAlarm_Type()
)
environmental_Temp4LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp4LowAlarm.setStatus("current")
_Environmental_Temp4Low_Type = Integer32
_Environmental_Temp4Low_Object = MibScalar
environmental_Temp4Low = _Environmental_Temp4Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 87),
    _Environmental_Temp4Low_Type()
)
environmental_Temp4Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp4Low.setStatus("current")


class _Environmental_Temp4HighAlarm_Type(Integer32):
    """Custom type environmental_Temp4HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp4HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp4HighAlarm_Object = MibScalar
environmental_Temp4HighAlarm = _Environmental_Temp4HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 88),
    _Environmental_Temp4HighAlarm_Type()
)
environmental_Temp4HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp4HighAlarm.setStatus("current")
_Environmental_Temp4High_Type = Integer32
_Environmental_Temp4High_Object = MibScalar
environmental_Temp4High = _Environmental_Temp4High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 89),
    _Environmental_Temp4High_Type()
)
environmental_Temp4High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp4High.setStatus("current")


class _Environmental_Temp5LowAlarm_Type(Integer32):
    """Custom type environmental_Temp5LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp5LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp5LowAlarm_Object = MibScalar
environmental_Temp5LowAlarm = _Environmental_Temp5LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 90),
    _Environmental_Temp5LowAlarm_Type()
)
environmental_Temp5LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp5LowAlarm.setStatus("current")
_Environmental_Temp5Low_Type = Integer32
_Environmental_Temp5Low_Object = MibScalar
environmental_Temp5Low = _Environmental_Temp5Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 91),
    _Environmental_Temp5Low_Type()
)
environmental_Temp5Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp5Low.setStatus("current")


class _Environmental_Temp5HighAlarm_Type(Integer32):
    """Custom type environmental_Temp5HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp5HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp5HighAlarm_Object = MibScalar
environmental_Temp5HighAlarm = _Environmental_Temp5HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 92),
    _Environmental_Temp5HighAlarm_Type()
)
environmental_Temp5HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp5HighAlarm.setStatus("current")
_Environmental_Temp5High_Type = Integer32
_Environmental_Temp5High_Object = MibScalar
environmental_Temp5High = _Environmental_Temp5High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 93),
    _Environmental_Temp5High_Type()
)
environmental_Temp5High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp5High.setStatus("current")


class _Environmental_Temp6LowAlarm_Type(Integer32):
    """Custom type environmental_Temp6LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp6LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp6LowAlarm_Object = MibScalar
environmental_Temp6LowAlarm = _Environmental_Temp6LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 94),
    _Environmental_Temp6LowAlarm_Type()
)
environmental_Temp6LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp6LowAlarm.setStatus("current")
_Environmental_Temp6Low_Type = Integer32
_Environmental_Temp6Low_Object = MibScalar
environmental_Temp6Low = _Environmental_Temp6Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 95),
    _Environmental_Temp6Low_Type()
)
environmental_Temp6Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp6Low.setStatus("current")


class _Environmental_Temp6HighAlarm_Type(Integer32):
    """Custom type environmental_Temp6HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp6HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp6HighAlarm_Object = MibScalar
environmental_Temp6HighAlarm = _Environmental_Temp6HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 96),
    _Environmental_Temp6HighAlarm_Type()
)
environmental_Temp6HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp6HighAlarm.setStatus("current")
_Environmental_Temp6High_Type = Integer32
_Environmental_Temp6High_Object = MibScalar
environmental_Temp6High = _Environmental_Temp6High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 97),
    _Environmental_Temp6High_Type()
)
environmental_Temp6High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp6High.setStatus("current")


class _Environmental_Temp7LowAlarm_Type(Integer32):
    """Custom type environmental_Temp7LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp7LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp7LowAlarm_Object = MibScalar
environmental_Temp7LowAlarm = _Environmental_Temp7LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 98),
    _Environmental_Temp7LowAlarm_Type()
)
environmental_Temp7LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp7LowAlarm.setStatus("current")
_Environmental_Temp7Low_Type = Integer32
_Environmental_Temp7Low_Object = MibScalar
environmental_Temp7Low = _Environmental_Temp7Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 99),
    _Environmental_Temp7Low_Type()
)
environmental_Temp7Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp7Low.setStatus("current")


class _Environmental_Temp7HighAlarm_Type(Integer32):
    """Custom type environmental_Temp7HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp7HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp7HighAlarm_Object = MibScalar
environmental_Temp7HighAlarm = _Environmental_Temp7HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 100),
    _Environmental_Temp7HighAlarm_Type()
)
environmental_Temp7HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp7HighAlarm.setStatus("current")
_Environmental_Temp7High_Type = Integer32
_Environmental_Temp7High_Object = MibScalar
environmental_Temp7High = _Environmental_Temp7High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 101),
    _Environmental_Temp7High_Type()
)
environmental_Temp7High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp7High.setStatus("current")


class _Environmental_Temp8LowAlarm_Type(Integer32):
    """Custom type environmental_Temp8LowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp8LowAlarm_Type.__name__ = "Integer32"
_Environmental_Temp8LowAlarm_Object = MibScalar
environmental_Temp8LowAlarm = _Environmental_Temp8LowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 102),
    _Environmental_Temp8LowAlarm_Type()
)
environmental_Temp8LowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp8LowAlarm.setStatus("current")
_Environmental_Temp8Low_Type = Integer32
_Environmental_Temp8Low_Object = MibScalar
environmental_Temp8Low = _Environmental_Temp8Low_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 103),
    _Environmental_Temp8Low_Type()
)
environmental_Temp8Low.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp8Low.setStatus("current")


class _Environmental_Temp8HighAlarm_Type(Integer32):
    """Custom type environmental_Temp8HighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Temp8HighAlarm_Type.__name__ = "Integer32"
_Environmental_Temp8HighAlarm_Object = MibScalar
environmental_Temp8HighAlarm = _Environmental_Temp8HighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 104),
    _Environmental_Temp8HighAlarm_Type()
)
environmental_Temp8HighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp8HighAlarm.setStatus("current")
_Environmental_Temp8High_Type = Integer32
_Environmental_Temp8High_Object = MibScalar
environmental_Temp8High = _Environmental_Temp8High_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 105),
    _Environmental_Temp8High_Type()
)
environmental_Temp8High.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Temp8High.setStatus("current")


class _Environmental_HumidityTempLowAlarm_Type(Integer32):
    """Custom type environmental_HumidityTempLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_HumidityTempLowAlarm_Type.__name__ = "Integer32"
_Environmental_HumidityTempLowAlarm_Object = MibScalar
environmental_HumidityTempLowAlarm = _Environmental_HumidityTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 106),
    _Environmental_HumidityTempLowAlarm_Type()
)
environmental_HumidityTempLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityTempLowAlarm.setStatus("current")
_Environmental_HumidityTempLow_Type = Integer32
_Environmental_HumidityTempLow_Object = MibScalar
environmental_HumidityTempLow = _Environmental_HumidityTempLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 107),
    _Environmental_HumidityTempLow_Type()
)
environmental_HumidityTempLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityTempLow.setStatus("current")


class _Environmental_HumidityTempHighAlarm_Type(Integer32):
    """Custom type environmental_HumidityTempHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_HumidityTempHighAlarm_Type.__name__ = "Integer32"
_Environmental_HumidityTempHighAlarm_Object = MibScalar
environmental_HumidityTempHighAlarm = _Environmental_HumidityTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 108),
    _Environmental_HumidityTempHighAlarm_Type()
)
environmental_HumidityTempHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityTempHighAlarm.setStatus("current")
_Environmental_HumidityTempHigh_Type = Integer32
_Environmental_HumidityTempHigh_Object = MibScalar
environmental_HumidityTempHigh = _Environmental_HumidityTempHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 109),
    _Environmental_HumidityTempHigh_Type()
)
environmental_HumidityTempHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityTempHigh.setStatus("current")


class _Environmental_HumidityLowAlarm_Type(Integer32):
    """Custom type environmental_HumidityLowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_HumidityLowAlarm_Type.__name__ = "Integer32"
_Environmental_HumidityLowAlarm_Object = MibScalar
environmental_HumidityLowAlarm = _Environmental_HumidityLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 110),
    _Environmental_HumidityLowAlarm_Type()
)
environmental_HumidityLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityLowAlarm.setStatus("current")
_Environmental_HumidityLow_Type = Integer32
_Environmental_HumidityLow_Object = MibScalar
environmental_HumidityLow = _Environmental_HumidityLow_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 111),
    _Environmental_HumidityLow_Type()
)
environmental_HumidityLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityLow.setStatus("current")


class _Environmental_HumidityHighAlarm_Type(Integer32):
    """Custom type environmental_HumidityHighAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_HumidityHighAlarm_Type.__name__ = "Integer32"
_Environmental_HumidityHighAlarm_Object = MibScalar
environmental_HumidityHighAlarm = _Environmental_HumidityHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 112),
    _Environmental_HumidityHighAlarm_Type()
)
environmental_HumidityHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityHighAlarm.setStatus("current")
_Environmental_HumidityHigh_Type = Integer32
_Environmental_HumidityHigh_Object = MibScalar
environmental_HumidityHigh = _Environmental_HumidityHigh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 113),
    _Environmental_HumidityHigh_Type()
)
environmental_HumidityHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_HumidityHigh.setStatus("current")


class _Environmental_Contact1OpenedAlarm_Type(Integer32):
    """Custom type environmental_Contact1OpenedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Contact1OpenedAlarm_Type.__name__ = "Integer32"
_Environmental_Contact1OpenedAlarm_Object = MibScalar
environmental_Contact1OpenedAlarm = _Environmental_Contact1OpenedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 114),
    _Environmental_Contact1OpenedAlarm_Type()
)
environmental_Contact1OpenedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Contact1OpenedAlarm.setStatus("current")


class _Environmental_Contact1ClosedAlarm_Type(Integer32):
    """Custom type environmental_Contact1ClosedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Contact1ClosedAlarm_Type.__name__ = "Integer32"
_Environmental_Contact1ClosedAlarm_Object = MibScalar
environmental_Contact1ClosedAlarm = _Environmental_Contact1ClosedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 115),
    _Environmental_Contact1ClosedAlarm_Type()
)
environmental_Contact1ClosedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Contact1ClosedAlarm.setStatus("current")


class _Environmental_Contact2OpenedAlarm_Type(Integer32):
    """Custom type environmental_Contact2OpenedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Contact2OpenedAlarm_Type.__name__ = "Integer32"
_Environmental_Contact2OpenedAlarm_Object = MibScalar
environmental_Contact2OpenedAlarm = _Environmental_Contact2OpenedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 116),
    _Environmental_Contact2OpenedAlarm_Type()
)
environmental_Contact2OpenedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Contact2OpenedAlarm.setStatus("current")


class _Environmental_Contact2ClosedAlarm_Type(Integer32):
    """Custom type environmental_Contact2ClosedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Contact2ClosedAlarm_Type.__name__ = "Integer32"
_Environmental_Contact2ClosedAlarm_Object = MibScalar
environmental_Contact2ClosedAlarm = _Environmental_Contact2ClosedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 117),
    _Environmental_Contact2ClosedAlarm_Type()
)
environmental_Contact2ClosedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Contact2ClosedAlarm.setStatus("current")


class _Environmental_Contact3OpenedAlarm_Type(Integer32):
    """Custom type environmental_Contact3OpenedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Contact3OpenedAlarm_Type.__name__ = "Integer32"
_Environmental_Contact3OpenedAlarm_Object = MibScalar
environmental_Contact3OpenedAlarm = _Environmental_Contact3OpenedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 118),
    _Environmental_Contact3OpenedAlarm_Type()
)
environmental_Contact3OpenedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Contact3OpenedAlarm.setStatus("current")


class _Environmental_Contact3ClosedAlarm_Type(Integer32):
    """Custom type environmental_Contact3ClosedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Environmental_Contact3ClosedAlarm_Type.__name__ = "Integer32"
_Environmental_Contact3ClosedAlarm_Object = MibScalar
environmental_Contact3ClosedAlarm = _Environmental_Contact3ClosedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 119),
    _Environmental_Contact3ClosedAlarm_Type()
)
environmental_Contact3ClosedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    environmental_Contact3ClosedAlarm.setStatus("current")


class _Security_DoorOpenedAlarm_Type(Integer32):
    """Custom type security_DoorOpenedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Security_DoorOpenedAlarm_Type.__name__ = "Integer32"
_Security_DoorOpenedAlarm_Object = MibScalar
security_DoorOpenedAlarm = _Security_DoorOpenedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 120),
    _Security_DoorOpenedAlarm_Type()
)
security_DoorOpenedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    security_DoorOpenedAlarm.setStatus("current")


class _Security_DoorClosedAlarm_Type(Integer32):
    """Custom type security_DoorClosedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Security_DoorClosedAlarm_Type.__name__ = "Integer32"
_Security_DoorClosedAlarm_Object = MibScalar
security_DoorClosedAlarm = _Security_DoorClosedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 121),
    _Security_DoorClosedAlarm_Type()
)
security_DoorClosedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    security_DoorClosedAlarm.setStatus("current")


class _Security_LockUnlockedAlarm_Type(Integer32):
    """Custom type security_LockUnlockedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Security_LockUnlockedAlarm_Type.__name__ = "Integer32"
_Security_LockUnlockedAlarm_Object = MibScalar
security_LockUnlockedAlarm = _Security_LockUnlockedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 122),
    _Security_LockUnlockedAlarm_Type()
)
security_LockUnlockedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    security_LockUnlockedAlarm.setStatus("current")


class _Security_LockLockedAlarm_Type(Integer32):
    """Custom type security_LockLockedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Security_LockLockedAlarm_Type.__name__ = "Integer32"
_Security_LockLockedAlarm_Object = MibScalar
security_LockLockedAlarm = _Security_LockLockedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 38218, 1, 11, 1, 123),
    _Security_LockLockedAlarm_Type()
)
security_LockLockedAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    security_LockLockedAlarm.setStatus("current")
_Slave_pdus_ObjectIdentity = ObjectIdentity
slave_pdus = _Slave_pdus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2)
)


class _Slave_slaveSelected_Type(Integer32):
    """Custom type slave_slaveSelected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Slave_slaveSelected_Type.__name__ = "Integer32"
_Slave_slaveSelected_Object = MibScalar
slave_slaveSelected = _Slave_slaveSelected_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 1),
    _Slave_slaveSelected_Type()
)
slave_slaveSelected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_slaveSelected.setStatus("current")
_Slave_Information_ObjectIdentity = ObjectIdentity
slave_Information = _Slave_Information_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2)
)
_Slave_pduName_Type = DisplayString
_Slave_pduName_Object = MibScalar
slave_pduName = _Slave_pduName_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 1),
    _Slave_pduName_Type()
)
slave_pduName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_pduName.setStatus("current")


class _Slave_pduStatus_Type(Integer32):
    """Custom type slave_pduStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("offline", 0),
          ("online", 1))
    )


_Slave_pduStatus_Type.__name__ = "Integer32"
_Slave_pduStatus_Object = MibScalar
slave_pduStatus = _Slave_pduStatus_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 2),
    _Slave_pduStatus_Type()
)
slave_pduStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_pduStatus.setStatus("current")


class _Slave_pduAddress_Type(Integer32):
    """Custom type slave_pduAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Slave_pduAddress_Type.__name__ = "Integer32"
_Slave_pduAddress_Object = MibScalar
slave_pduAddress = _Slave_pduAddress_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 3),
    _Slave_pduAddress_Type()
)
slave_pduAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_pduAddress.setStatus("current")
_Slave_pduFirmware_Type = DisplayString
_Slave_pduFirmware_Object = MibScalar
slave_pduFirmware = _Slave_pduFirmware_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 4),
    _Slave_pduFirmware_Type()
)
slave_pduFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_pduFirmware.setStatus("current")
_Slave_Info_NotUsed2_Type = DisplayString
_Slave_Info_NotUsed2_Object = MibScalar
slave_Info_NotUsed2 = _Slave_Info_NotUsed2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 5),
    _Slave_Info_NotUsed2_Type()
)
slave_Info_NotUsed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Info_NotUsed2.setStatus("current")


class _Slave_pduNosockets_Type(Integer32):
    """Custom type slave_pduNosockets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_Slave_pduNosockets_Type.__name__ = "Integer32"
_Slave_pduNosockets_Object = MibScalar
slave_pduNosockets = _Slave_pduNosockets_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 6),
    _Slave_pduNosockets_Type()
)
slave_pduNosockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_pduNosockets.setStatus("current")
_Slave_Info_NotUsed3_Type = Integer32
_Slave_Info_NotUsed3_Object = MibScalar
slave_Info_NotUsed3 = _Slave_Info_NotUsed3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 7),
    _Slave_Info_NotUsed3_Type()
)
slave_Info_NotUsed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Info_NotUsed3.setStatus("current")
_Slave_Info_NotUsed4_Type = Integer32
_Slave_Info_NotUsed4_Object = MibScalar
slave_Info_NotUsed4 = _Slave_Info_NotUsed4_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 8),
    _Slave_Info_NotUsed4_Type()
)
slave_Info_NotUsed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Info_NotUsed4.setStatus("current")
_Slave_Info_pduReset_Type = Integer32
_Slave_Info_pduReset_Object = MibScalar
slave_Info_pduReset = _Slave_Info_pduReset_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 9),
    _Slave_Info_pduReset_Type()
)
slave_Info_pduReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Info_pduReset.setStatus("current")
_Slave_Info_pdukWhReset_Type = Integer32
_Slave_Info_pdukWhReset_Object = MibScalar
slave_Info_pdukWhReset = _Slave_Info_pdukWhReset_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 2, 10),
    _Slave_Info_pdukWhReset_Type()
)
slave_Info_pdukWhReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Info_pdukWhReset.setStatus("current")
_Slave_Status_ObjectIdentity = ObjectIdentity
slave_Status = _Slave_Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3)
)
_Slave_meter1_VRMS_Type = Integer32
_Slave_meter1_VRMS_Object = MibScalar
slave_meter1_VRMS = _Slave_meter1_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 1),
    _Slave_meter1_VRMS_Type()
)
slave_meter1_VRMS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_meter1_VRMS.setStatus("current")
_Slave_meter1_IRMS_Type = Integer32
_Slave_meter1_IRMS_Object = MibScalar
slave_meter1_IRMS = _Slave_meter1_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 2),
    _Slave_meter1_IRMS_Type()
)
slave_meter1_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_IRMS.setStatus("current")
_Slave_meter1_KWH_Type = Integer32
_Slave_meter1_KWH_Object = MibScalar
slave_meter1_KWH = _Slave_meter1_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 3),
    _Slave_meter1_KWH_Type()
)
slave_meter1_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_KWH.setStatus("current")
_Slave_meter1_KW_Type = Integer32
_Slave_meter1_KW_Object = MibScalar
slave_meter1_KW = _Slave_meter1_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 4),
    _Slave_meter1_KW_Type()
)
slave_meter1_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_KW.setStatus("current")
_Slave_meter1_TPMU_Type = Integer32
_Slave_meter1_TPMU_Object = MibScalar
slave_meter1_TPMU = _Slave_meter1_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 5),
    _Slave_meter1_TPMU_Type()
)
slave_meter1_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_TPMU.setStatus("current")
_Slave_Status_NotUsed1_Type = Integer32
_Slave_Status_NotUsed1_Object = MibScalar
slave_Status_NotUsed1 = _Slave_Status_NotUsed1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 6),
    _Slave_Status_NotUsed1_Type()
)
slave_Status_NotUsed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Status_NotUsed1.setStatus("current")
_Slave_Status_NotUsed2_Type = Integer32
_Slave_Status_NotUsed2_Object = MibScalar
slave_Status_NotUsed2 = _Slave_Status_NotUsed2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 7),
    _Slave_Status_NotUsed2_Type()
)
slave_Status_NotUsed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Status_NotUsed2.setStatus("current")
_Slave_meter1_IPK_Type = Integer32
_Slave_meter1_IPK_Object = MibScalar
slave_meter1_IPK = _Slave_meter1_IPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 8),
    _Slave_meter1_IPK_Type()
)
slave_meter1_IPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_IPK.setStatus("current")
_Slave_meter1_VPK_Type = Integer32
_Slave_meter1_VPK_Object = MibScalar
slave_meter1_VPK = _Slave_meter1_VPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 9),
    _Slave_meter1_VPK_Type()
)
slave_meter1_VPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_VPK.setStatus("current")
_Slave_meter1_PF_Type = Integer32
_Slave_meter1_PF_Object = MibScalar
slave_meter1_PF = _Slave_meter1_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 10),
    _Slave_meter1_PF_Type()
)
slave_meter1_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_PF.setStatus("current")
_Slave_Status_NotUsed3_Type = Integer32
_Slave_Status_NotUsed3_Object = MibScalar
slave_Status_NotUsed3 = _Slave_Status_NotUsed3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 11),
    _Slave_Status_NotUsed3_Type()
)
slave_Status_NotUsed3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Status_NotUsed3.setStatus("current")
_Slave_Status_NotUsed4_Type = Integer32
_Slave_Status_NotUsed4_Object = MibScalar
slave_Status_NotUsed4 = _Slave_Status_NotUsed4_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 12),
    _Slave_Status_NotUsed4_Type()
)
slave_Status_NotUsed4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Status_NotUsed4.setStatus("current")
_Slave_Status_NotUsed5_Type = Integer32
_Slave_Status_NotUsed5_Object = MibScalar
slave_Status_NotUsed5 = _Slave_Status_NotUsed5_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 13),
    _Slave_Status_NotUsed5_Type()
)
slave_Status_NotUsed5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Status_NotUsed5.setStatus("current")
_Slave_meter1_Freq_Type = Integer32
_Slave_meter1_Freq_Object = MibScalar
slave_meter1_Freq = _Slave_meter1_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 14),
    _Slave_meter1_Freq_Type()
)
slave_meter1_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter1_Freq.setStatus("current")
_Slave_meter2_VRMS_Type = Integer32
_Slave_meter2_VRMS_Object = MibScalar
slave_meter2_VRMS = _Slave_meter2_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 15),
    _Slave_meter2_VRMS_Type()
)
slave_meter2_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_VRMS.setStatus("current")
_Slave_meter2_IRMS_Type = Integer32
_Slave_meter2_IRMS_Object = MibScalar
slave_meter2_IRMS = _Slave_meter2_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 16),
    _Slave_meter2_IRMS_Type()
)
slave_meter2_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_IRMS.setStatus("current")
_Slave_meter2_KWH_Type = Integer32
_Slave_meter2_KWH_Object = MibScalar
slave_meter2_KWH = _Slave_meter2_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 17),
    _Slave_meter2_KWH_Type()
)
slave_meter2_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_KWH.setStatus("current")
_Slave_meter2_KW_Type = Integer32
_Slave_meter2_KW_Object = MibScalar
slave_meter2_KW = _Slave_meter2_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 18),
    _Slave_meter2_KW_Type()
)
slave_meter2_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_KW.setStatus("current")
_Slave_meter2_TPMU_Type = Integer32
_Slave_meter2_TPMU_Object = MibScalar
slave_meter2_TPMU = _Slave_meter2_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 19),
    _Slave_meter2_TPMU_Type()
)
slave_meter2_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_TPMU.setStatus("current")
_Slave_meter2_IPK_Type = Integer32
_Slave_meter2_IPK_Object = MibScalar
slave_meter2_IPK = _Slave_meter2_IPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 20),
    _Slave_meter2_IPK_Type()
)
slave_meter2_IPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_IPK.setStatus("current")
_Slave_meter2_VPK_Type = Integer32
_Slave_meter2_VPK_Object = MibScalar
slave_meter2_VPK = _Slave_meter2_VPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 21),
    _Slave_meter2_VPK_Type()
)
slave_meter2_VPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_VPK.setStatus("current")
_Slave_meter2_PF_Type = Integer32
_Slave_meter2_PF_Object = MibScalar
slave_meter2_PF = _Slave_meter2_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 22),
    _Slave_meter2_PF_Type()
)
slave_meter2_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_PF.setStatus("current")
_Slave_meter2_Freq_Type = Integer32
_Slave_meter2_Freq_Object = MibScalar
slave_meter2_Freq = _Slave_meter2_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 23),
    _Slave_meter2_Freq_Type()
)
slave_meter2_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter2_Freq.setStatus("current")
_Slave_meter3_VRMS_Type = Integer32
_Slave_meter3_VRMS_Object = MibScalar
slave_meter3_VRMS = _Slave_meter3_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 24),
    _Slave_meter3_VRMS_Type()
)
slave_meter3_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_VRMS.setStatus("current")
_Slave_meter3_IRMS_Type = Integer32
_Slave_meter3_IRMS_Object = MibScalar
slave_meter3_IRMS = _Slave_meter3_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 25),
    _Slave_meter3_IRMS_Type()
)
slave_meter3_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_IRMS.setStatus("current")
_Slave_meter3_KWH_Type = Integer32
_Slave_meter3_KWH_Object = MibScalar
slave_meter3_KWH = _Slave_meter3_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 26),
    _Slave_meter3_KWH_Type()
)
slave_meter3_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_KWH.setStatus("current")
_Slave_meter3_KW_Type = Integer32
_Slave_meter3_KW_Object = MibScalar
slave_meter3_KW = _Slave_meter3_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 27),
    _Slave_meter3_KW_Type()
)
slave_meter3_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_KW.setStatus("current")
_Slave_meter3_TPMU_Type = Integer32
_Slave_meter3_TPMU_Object = MibScalar
slave_meter3_TPMU = _Slave_meter3_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 28),
    _Slave_meter3_TPMU_Type()
)
slave_meter3_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_TPMU.setStatus("current")
_Slave_meter3_IPK_Type = Integer32
_Slave_meter3_IPK_Object = MibScalar
slave_meter3_IPK = _Slave_meter3_IPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 29),
    _Slave_meter3_IPK_Type()
)
slave_meter3_IPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_IPK.setStatus("current")
_Slave_meter3_VPK_Type = Integer32
_Slave_meter3_VPK_Object = MibScalar
slave_meter3_VPK = _Slave_meter3_VPK_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 30),
    _Slave_meter3_VPK_Type()
)
slave_meter3_VPK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_VPK.setStatus("current")
_Slave_meter3_PF_Type = Integer32
_Slave_meter3_PF_Object = MibScalar
slave_meter3_PF = _Slave_meter3_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 31),
    _Slave_meter3_PF_Type()
)
slave_meter3_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_PF.setStatus("current")
_Slave_meter3_Freq_Type = Integer32
_Slave_meter3_Freq_Object = MibScalar
slave_meter3_Freq = _Slave_meter3_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 3, 32),
    _Slave_meter3_Freq_Type()
)
slave_meter3_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_meter3_Freq.setStatus("current")
_Slave_sockets_ObjectIdentity = ObjectIdentity
slave_sockets = _Slave_sockets_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4)
)
_Slave_socketsTable_Object = MibTable
slave_socketsTable = _Slave_socketsTable_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1)
)
if mibBuilder.loadTexts:
    slave_socketsTable.setStatus("current")
_Slave_socketsEntry_Object = MibTableRow
slave_socketsEntry = _Slave_socketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1)
)
slave_socketsEntry.setIndexNames(
    (0, "PDUSNMP", "slave-socket-Index"),
)
if mibBuilder.loadTexts:
    slave_socketsEntry.setStatus("current")


class _Slave_socket_Index_Type(Integer32):
    """Custom type slave_socket_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_Slave_socket_Index_Type.__name__ = "Integer32"
_Slave_socket_Index_Object = MibScalar
slave_socket_Index = _Slave_socket_Index_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1, 1),
    _Slave_socket_Index_Type()
)
slave_socket_Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slave_socket_Index.setStatus("current")
_Slave_socket_Number_Type = Integer32
_Slave_socket_Number_Object = MibScalar
slave_socket_Number = _Slave_socket_Number_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1, 2),
    _Slave_socket_Number_Type()
)
slave_socket_Number.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slave_socket_Number.setStatus("current")
_Slave_socket_NotUsed1_Type = DisplayString
_Slave_socket_NotUsed1_Object = MibScalar
slave_socket_NotUsed1 = _Slave_socket_NotUsed1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1, 3),
    _Slave_socket_NotUsed1_Type()
)
slave_socket_NotUsed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_socket_NotUsed1.setStatus("current")


class _Slave_socket_ONOFF_Type(Integer32):
    """Custom type slave_socket_ONOFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_Slave_socket_ONOFF_Type.__name__ = "Integer32"
_Slave_socket_ONOFF_Object = MibScalar
slave_socket_ONOFF = _Slave_socket_ONOFF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1, 4),
    _Slave_socket_ONOFF_Type()
)
slave_socket_ONOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_socket_ONOFF.setStatus("current")
_Slave_socket_AMPS_Type = Integer32
_Slave_socket_AMPS_Object = MibScalar
slave_socket_AMPS = _Slave_socket_AMPS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1, 5),
    _Slave_socket_AMPS_Type()
)
slave_socket_AMPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_socket_AMPS.setStatus("current")
_Slave_socket_KWH_Type = Integer32
_Slave_socket_KWH_Object = MibScalar
slave_socket_KWH = _Slave_socket_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 1, 1, 6),
    _Slave_socket_KWH_Type()
)
slave_socket_KWH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_socket_KWH.setStatus("current")


class _Socket_Selected_Type(Integer32):
    """Custom type socket_Selected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_Socket_Selected_Type.__name__ = "Integer32"
_Socket_Selected_Object = MibScalar
socket_Selected = _Socket_Selected_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 2),
    _Socket_Selected_Type()
)
socket_Selected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_Selected.setStatus("current")


class _Socket_AllON_Type(Integer32):
    """Custom type socket_AllON based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Socket_AllON_Type.__name__ = "Integer32"
_Socket_AllON_Object = MibScalar
socket_AllON = _Socket_AllON_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 3),
    _Socket_AllON_Type()
)
socket_AllON.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_AllON.setStatus("current")


class _Socket_AllOFF_Type(Integer32):
    """Custom type socket_AllOFF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Socket_AllOFF_Type.__name__ = "Integer32"
_Socket_AllOFF_Object = MibScalar
socket_AllOFF = _Socket_AllOFF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 4, 4),
    _Socket_AllOFF_Type()
)
socket_AllOFF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    socket_AllOFF.setStatus("current")
_Slave_Environmental_ObjectIdentity = ObjectIdentity
slave_Environmental = _Slave_Environmental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5)
)
_Slave_environmental_Temp1_Type = Integer32
_Slave_environmental_Temp1_Object = MibScalar
slave_environmental_Temp1 = _Slave_environmental_Temp1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 1),
    _Slave_environmental_Temp1_Type()
)
slave_environmental_Temp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp1.setStatus("current")
_Slave_environmental_Temp2_Type = Integer32
_Slave_environmental_Temp2_Object = MibScalar
slave_environmental_Temp2 = _Slave_environmental_Temp2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 2),
    _Slave_environmental_Temp2_Type()
)
slave_environmental_Temp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp2.setStatus("current")
_Slave_environmental_Temp3_Type = Integer32
_Slave_environmental_Temp3_Object = MibScalar
slave_environmental_Temp3 = _Slave_environmental_Temp3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 3),
    _Slave_environmental_Temp3_Type()
)
slave_environmental_Temp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp3.setStatus("current")
_Slave_environmental_Temp4_Type = Integer32
_Slave_environmental_Temp4_Object = MibScalar
slave_environmental_Temp4 = _Slave_environmental_Temp4_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 4),
    _Slave_environmental_Temp4_Type()
)
slave_environmental_Temp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp4.setStatus("current")
_Slave_environmental_Temp5_Type = Integer32
_Slave_environmental_Temp5_Object = MibScalar
slave_environmental_Temp5 = _Slave_environmental_Temp5_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 5),
    _Slave_environmental_Temp5_Type()
)
slave_environmental_Temp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp5.setStatus("current")
_Slave_environmental_Temp6_Type = Integer32
_Slave_environmental_Temp6_Object = MibScalar
slave_environmental_Temp6 = _Slave_environmental_Temp6_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 6),
    _Slave_environmental_Temp6_Type()
)
slave_environmental_Temp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp6.setStatus("current")
_Slave_environmental_Temp7_Type = Integer32
_Slave_environmental_Temp7_Object = MibScalar
slave_environmental_Temp7 = _Slave_environmental_Temp7_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 7),
    _Slave_environmental_Temp7_Type()
)
slave_environmental_Temp7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp7.setStatus("current")
_Slave_environmental_Temp8_Type = Integer32
_Slave_environmental_Temp8_Object = MibScalar
slave_environmental_Temp8 = _Slave_environmental_Temp8_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 8),
    _Slave_environmental_Temp8_Type()
)
slave_environmental_Temp8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Temp8.setStatus("current")
_Slave_environmental_HumidityTemp_Type = Integer32
_Slave_environmental_HumidityTemp_Object = MibScalar
slave_environmental_HumidityTemp = _Slave_environmental_HumidityTemp_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 9),
    _Slave_environmental_HumidityTemp_Type()
)
slave_environmental_HumidityTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_HumidityTemp.setStatus("current")
_Slave_environmental_Humidity_Type = Integer32
_Slave_environmental_Humidity_Object = MibScalar
slave_environmental_Humidity = _Slave_environmental_Humidity_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 10),
    _Slave_environmental_Humidity_Type()
)
slave_environmental_Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_environmental_Humidity.setStatus("current")


class _Slave_environmental_Contact1_Type(Integer32):
    """Custom type slave_environmental_Contact1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_environmental_Contact1_Type.__name__ = "Integer32"
_Slave_environmental_Contact1_Object = MibScalar
slave_environmental_Contact1 = _Slave_environmental_Contact1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 11),
    _Slave_environmental_Contact1_Type()
)
slave_environmental_Contact1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_environmental_Contact1.setStatus("current")


class _Slave_environmental_Contact2_Type(Integer32):
    """Custom type slave_environmental_Contact2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_environmental_Contact2_Type.__name__ = "Integer32"
_Slave_environmental_Contact2_Object = MibScalar
slave_environmental_Contact2 = _Slave_environmental_Contact2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 12),
    _Slave_environmental_Contact2_Type()
)
slave_environmental_Contact2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_environmental_Contact2.setStatus("current")


class _Slave_environmental_Contact3_Type(Integer32):
    """Custom type slave_environmental_Contact3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_environmental_Contact3_Type.__name__ = "Integer32"
_Slave_environmental_Contact3_Object = MibScalar
slave_environmental_Contact3 = _Slave_environmental_Contact3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 5, 13),
    _Slave_environmental_Contact3_Type()
)
slave_environmental_Contact3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_environmental_Contact3.setStatus("current")
_Slave_Security_ObjectIdentity = ObjectIdentity
slave_Security = _Slave_Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 6)
)


class _Slave_Security_Door_Type(Integer32):
    """Custom type slave_Security_Door based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_Security_Door_Type.__name__ = "Integer32"
_Slave_Security_Door_Object = MibScalar
slave_Security_Door = _Slave_Security_Door_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 6, 1),
    _Slave_Security_Door_Type()
)
slave_Security_Door.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Security_Door.setStatus("current")


class _Slave_Security_Lock_Type(Integer32):
    """Custom type slave_Security_Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Slave_Security_Lock_Type.__name__ = "Integer32"
_Slave_Security_Lock_Object = MibScalar
slave_Security_Lock = _Slave_Security_Lock_Object(
    (1, 3, 6, 1, 4, 1, 38218, 2, 6, 2),
    _Slave_Security_Lock_Type()
)
slave_Security_Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Security_Lock.setStatus("current")
_Slave_Traps_ObjectIdentity = ObjectIdentity
slave_Traps = _Slave_Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7)
)
_Slave_TrapSetNotifications_ObjectIdentity = ObjectIdentity
slave_TrapSetNotifications = _Slave_TrapSetNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1)
)
_Slave_TrapClearNotifications_ObjectIdentity = ObjectIdentity
slave_TrapClearNotifications = _Slave_TrapClearNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2)
)
_Slave_Global_ObjectIdentity = ObjectIdentity
slave_Global = _Slave_Global_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 38218, 3)
)
_Slave_Global_Table_Object = MibTable
slave_Global_Table = _Slave_Global_Table_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1)
)
if mibBuilder.loadTexts:
    slave_Global_Table.setStatus("current")
_Slave_Global_Entry_Object = MibTableRow
slave_Global_Entry = _Slave_Global_Entry_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1)
)
slave_Global_Entry.setIndexNames(
    (0, "PDUSNMP", "slave-Global-Index"),
)
if mibBuilder.loadTexts:
    slave_Global_Entry.setStatus("current")


class _Slave_Global_Index_Type(Integer32):
    """Custom type slave_Global_Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_Slave_Global_Index_Type.__name__ = "Integer32"
_Slave_Global_Index_Object = MibScalar
slave_Global_Index = _Slave_Global_Index_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 1),
    _Slave_Global_Index_Type()
)
slave_Global_Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    slave_Global_Index.setStatus("current")


class _Slave_Global_Status_Type(Integer32):
    """Custom type slave_Global_Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("offline", 0),
          ("online", 1))
    )


_Slave_Global_Status_Type.__name__ = "Integer32"
_Slave_Global_Status_Object = MibScalar
slave_Global_Status = _Slave_Global_Status_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 2),
    _Slave_Global_Status_Type()
)
slave_Global_Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_Status.setStatus("current")


class _Slave_Global_Address_Type(Integer32):
    """Custom type slave_Global_Address based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_Slave_Global_Address_Type.__name__ = "Integer32"
_Slave_Global_Address_Object = MibScalar
slave_Global_Address = _Slave_Global_Address_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 3),
    _Slave_Global_Address_Type()
)
slave_Global_Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_Address.setStatus("current")


class _Slave_Global_Nosockets_Type(Integer32):
    """Custom type slave_Global_Nosockets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_Slave_Global_Nosockets_Type.__name__ = "Integer32"
_Slave_Global_Nosockets_Object = MibScalar
slave_Global_Nosockets = _Slave_Global_Nosockets_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 4),
    _Slave_Global_Nosockets_Type()
)
slave_Global_Nosockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_Nosockets.setStatus("current")
_Slave_Global_meter1_VRMS_Type = Integer32
_Slave_Global_meter1_VRMS_Object = MibScalar
slave_Global_meter1_VRMS = _Slave_Global_meter1_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 5),
    _Slave_Global_meter1_VRMS_Type()
)
slave_Global_meter1_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_VRMS.setStatus("current")
_Slave_Global_meter1_IRMS_Type = Integer32
_Slave_Global_meter1_IRMS_Object = MibScalar
slave_Global_meter1_IRMS = _Slave_Global_meter1_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 6),
    _Slave_Global_meter1_IRMS_Type()
)
slave_Global_meter1_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_IRMS.setStatus("current")
_Slave_Global_meter1_KWH_Type = Integer32
_Slave_Global_meter1_KWH_Object = MibScalar
slave_Global_meter1_KWH = _Slave_Global_meter1_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 7),
    _Slave_Global_meter1_KWH_Type()
)
slave_Global_meter1_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_KWH.setStatus("current")
_Slave_Global_meter1_KW_Type = Integer32
_Slave_Global_meter1_KW_Object = MibScalar
slave_Global_meter1_KW = _Slave_Global_meter1_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 8),
    _Slave_Global_meter1_KW_Type()
)
slave_Global_meter1_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_KW.setStatus("current")
_Slave_Global_meter1_TPMU_Type = Integer32
_Slave_Global_meter1_TPMU_Object = MibScalar
slave_Global_meter1_TPMU = _Slave_Global_meter1_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 9),
    _Slave_Global_meter1_TPMU_Type()
)
slave_Global_meter1_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_TPMU.setStatus("current")
_Slave_Global_meter1_PF_Type = Integer32
_Slave_Global_meter1_PF_Object = MibScalar
slave_Global_meter1_PF = _Slave_Global_meter1_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 10),
    _Slave_Global_meter1_PF_Type()
)
slave_Global_meter1_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_PF.setStatus("current")
_Slave_Global_environmental_Temp1_Type = Integer32
_Slave_Global_environmental_Temp1_Object = MibScalar
slave_Global_environmental_Temp1 = _Slave_Global_environmental_Temp1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 11),
    _Slave_Global_environmental_Temp1_Type()
)
slave_Global_environmental_Temp1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp1.setStatus("current")
_Slave_Global_environmental_Temp2_Type = Integer32
_Slave_Global_environmental_Temp2_Object = MibScalar
slave_Global_environmental_Temp2 = _Slave_Global_environmental_Temp2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 12),
    _Slave_Global_environmental_Temp2_Type()
)
slave_Global_environmental_Temp2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp2.setStatus("current")
_Slave_Global_environmental_Temp3_Type = Integer32
_Slave_Global_environmental_Temp3_Object = MibScalar
slave_Global_environmental_Temp3 = _Slave_Global_environmental_Temp3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 13),
    _Slave_Global_environmental_Temp3_Type()
)
slave_Global_environmental_Temp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp3.setStatus("current")
_Slave_Global_environmental_Temp4_Type = Integer32
_Slave_Global_environmental_Temp4_Object = MibScalar
slave_Global_environmental_Temp4 = _Slave_Global_environmental_Temp4_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 14),
    _Slave_Global_environmental_Temp4_Type()
)
slave_Global_environmental_Temp4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp4.setStatus("current")
_Slave_Global_environmental_Temp5_Type = Integer32
_Slave_Global_environmental_Temp5_Object = MibScalar
slave_Global_environmental_Temp5 = _Slave_Global_environmental_Temp5_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 15),
    _Slave_Global_environmental_Temp5_Type()
)
slave_Global_environmental_Temp5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp5.setStatus("current")
_Slave_Global_environmental_Temp6_Type = Integer32
_Slave_Global_environmental_Temp6_Object = MibScalar
slave_Global_environmental_Temp6 = _Slave_Global_environmental_Temp6_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 16),
    _Slave_Global_environmental_Temp6_Type()
)
slave_Global_environmental_Temp6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp6.setStatus("current")
_Slave_Global_environmental_Temp7_Type = Integer32
_Slave_Global_environmental_Temp7_Object = MibScalar
slave_Global_environmental_Temp7 = _Slave_Global_environmental_Temp7_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 17),
    _Slave_Global_environmental_Temp7_Type()
)
slave_Global_environmental_Temp7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp7.setStatus("current")
_Slave_Global_environmental_Temp8_Type = Integer32
_Slave_Global_environmental_Temp8_Object = MibScalar
slave_Global_environmental_Temp8 = _Slave_Global_environmental_Temp8_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 18),
    _Slave_Global_environmental_Temp8_Type()
)
slave_Global_environmental_Temp8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Temp8.setStatus("current")
_Slave_Global_environmental_HumidityTemp_Type = Integer32
_Slave_Global_environmental_HumidityTemp_Object = MibScalar
slave_Global_environmental_HumidityTemp = _Slave_Global_environmental_HumidityTemp_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 19),
    _Slave_Global_environmental_HumidityTemp_Type()
)
slave_Global_environmental_HumidityTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_HumidityTemp.setStatus("current")
_Slave_Global_environmental_Humidity_Type = Integer32
_Slave_Global_environmental_Humidity_Object = MibScalar
slave_Global_environmental_Humidity = _Slave_Global_environmental_Humidity_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 20),
    _Slave_Global_environmental_Humidity_Type()
)
slave_Global_environmental_Humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_environmental_Humidity.setStatus("current")


class _Slave_Global_environmental_Contact1_Type(Integer32):
    """Custom type slave_Global_environmental_Contact1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("none", 3),
          ("open", 0))
    )


_Slave_Global_environmental_Contact1_Type.__name__ = "Integer32"
_Slave_Global_environmental_Contact1_Object = MibScalar
slave_Global_environmental_Contact1 = _Slave_Global_environmental_Contact1_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 21),
    _Slave_Global_environmental_Contact1_Type()
)
slave_Global_environmental_Contact1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_environmental_Contact1.setStatus("current")


class _Slave_Global_environmental_Contact2_Type(Integer32):
    """Custom type slave_Global_environmental_Contact2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_Global_environmental_Contact2_Type.__name__ = "Integer32"
_Slave_Global_environmental_Contact2_Object = MibScalar
slave_Global_environmental_Contact2 = _Slave_Global_environmental_Contact2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 22),
    _Slave_Global_environmental_Contact2_Type()
)
slave_Global_environmental_Contact2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_environmental_Contact2.setStatus("current")


class _Slave_Global_environmental_Contact3_Type(Integer32):
    """Custom type slave_Global_environmental_Contact3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_Global_environmental_Contact3_Type.__name__ = "Integer32"
_Slave_Global_environmental_Contact3_Object = MibScalar
slave_Global_environmental_Contact3 = _Slave_Global_environmental_Contact3_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 23),
    _Slave_Global_environmental_Contact3_Type()
)
slave_Global_environmental_Contact3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_environmental_Contact3.setStatus("current")


class _Slave_Global_Security_Door_Type(Integer32):
    """Custom type slave_Global_Security_Door based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("open", 0))
    )


_Slave_Global_Security_Door_Type.__name__ = "Integer32"
_Slave_Global_Security_Door_Object = MibScalar
slave_Global_Security_Door = _Slave_Global_Security_Door_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 24),
    _Slave_Global_Security_Door_Type()
)
slave_Global_Security_Door.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_Security_Door.setStatus("current")


class _Slave_Global_Security_Lock_Type(Integer32):
    """Custom type slave_Global_Security_Lock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("unlocked", 1))
    )


_Slave_Global_Security_Lock_Type.__name__ = "Integer32"
_Slave_Global_Security_Lock_Object = MibScalar
slave_Global_Security_Lock = _Slave_Global_Security_Lock_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 25),
    _Slave_Global_Security_Lock_Type()
)
slave_Global_Security_Lock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_Security_Lock.setStatus("current")
_Slave_Global_sockets_Type = Integer32
_Slave_Global_sockets_Object = MibScalar
slave_Global_sockets = _Slave_Global_sockets_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 26),
    _Slave_Global_sockets_Type()
)
slave_Global_sockets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_sockets.setStatus("current")
_Slave_Global_socket1Amps_Type = Integer32
_Slave_Global_socket1Amps_Object = MibScalar
slave_Global_socket1Amps = _Slave_Global_socket1Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 27),
    _Slave_Global_socket1Amps_Type()
)
slave_Global_socket1Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket1Amps.setStatus("current")
_Slave_Global_socket2Amps_Type = Integer32
_Slave_Global_socket2Amps_Object = MibScalar
slave_Global_socket2Amps = _Slave_Global_socket2Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 28),
    _Slave_Global_socket2Amps_Type()
)
slave_Global_socket2Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket2Amps.setStatus("current")
_Slave_Global_socket3Amps_Type = Integer32
_Slave_Global_socket3Amps_Object = MibScalar
slave_Global_socket3Amps = _Slave_Global_socket3Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 29),
    _Slave_Global_socket3Amps_Type()
)
slave_Global_socket3Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket3Amps.setStatus("current")
_Slave_Global_socket4Amps_Type = Integer32
_Slave_Global_socket4Amps_Object = MibScalar
slave_Global_socket4Amps = _Slave_Global_socket4Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 30),
    _Slave_Global_socket4Amps_Type()
)
slave_Global_socket4Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket4Amps.setStatus("current")
_Slave_Global_socket5Amps_Type = Integer32
_Slave_Global_socket5Amps_Object = MibScalar
slave_Global_socket5Amps = _Slave_Global_socket5Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 31),
    _Slave_Global_socket5Amps_Type()
)
slave_Global_socket5Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket5Amps.setStatus("current")
_Slave_Global_socket6Amps_Type = Integer32
_Slave_Global_socket6Amps_Object = MibScalar
slave_Global_socket6Amps = _Slave_Global_socket6Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 32),
    _Slave_Global_socket6Amps_Type()
)
slave_Global_socket6Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket6Amps.setStatus("current")
_Slave_Global_socket7Amps_Type = Integer32
_Slave_Global_socket7Amps_Object = MibScalar
slave_Global_socket7Amps = _Slave_Global_socket7Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 33),
    _Slave_Global_socket7Amps_Type()
)
slave_Global_socket7Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket7Amps.setStatus("current")
_Slave_Global_socket8Amps_Type = Integer32
_Slave_Global_socket8Amps_Object = MibScalar
slave_Global_socket8Amps = _Slave_Global_socket8Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 34),
    _Slave_Global_socket8Amps_Type()
)
slave_Global_socket8Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket8Amps.setStatus("current")
_Slave_Global_socket9Amps_Type = Integer32
_Slave_Global_socket9Amps_Object = MibScalar
slave_Global_socket9Amps = _Slave_Global_socket9Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 35),
    _Slave_Global_socket9Amps_Type()
)
slave_Global_socket9Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket9Amps.setStatus("current")
_Slave_Global_socket10Amps_Type = Integer32
_Slave_Global_socket10Amps_Object = MibScalar
slave_Global_socket10Amps = _Slave_Global_socket10Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 36),
    _Slave_Global_socket10Amps_Type()
)
slave_Global_socket10Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket10Amps.setStatus("current")
_Slave_Global_socket11Amps_Type = Integer32
_Slave_Global_socket11Amps_Object = MibScalar
slave_Global_socket11Amps = _Slave_Global_socket11Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 37),
    _Slave_Global_socket11Amps_Type()
)
slave_Global_socket11Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket11Amps.setStatus("current")
_Slave_Global_socket12Amps_Type = Integer32
_Slave_Global_socket12Amps_Object = MibScalar
slave_Global_socket12Amps = _Slave_Global_socket12Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 38),
    _Slave_Global_socket12Amps_Type()
)
slave_Global_socket12Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket12Amps.setStatus("current")
_Slave_Global_socket13Amps_Type = Integer32
_Slave_Global_socket13Amps_Object = MibScalar
slave_Global_socket13Amps = _Slave_Global_socket13Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 39),
    _Slave_Global_socket13Amps_Type()
)
slave_Global_socket13Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket13Amps.setStatus("current")
_Slave_Global_socket14Amps_Type = Integer32
_Slave_Global_socket14Amps_Object = MibScalar
slave_Global_socket14Amps = _Slave_Global_socket14Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 40),
    _Slave_Global_socket14Amps_Type()
)
slave_Global_socket14Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket14Amps.setStatus("current")
_Slave_Global_socket15Amps_Type = Integer32
_Slave_Global_socket15Amps_Object = MibScalar
slave_Global_socket15Amps = _Slave_Global_socket15Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 41),
    _Slave_Global_socket15Amps_Type()
)
slave_Global_socket15Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket15Amps.setStatus("current")
_Slave_Global_socket16Amps_Type = Integer32
_Slave_Global_socket16Amps_Object = MibScalar
slave_Global_socket16Amps = _Slave_Global_socket16Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 42),
    _Slave_Global_socket16Amps_Type()
)
slave_Global_socket16Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket16Amps.setStatus("current")
_Slave_Global_socket17Amps_Type = Integer32
_Slave_Global_socket17Amps_Object = MibScalar
slave_Global_socket17Amps = _Slave_Global_socket17Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 43),
    _Slave_Global_socket17Amps_Type()
)
slave_Global_socket17Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket17Amps.setStatus("current")
_Slave_Global_socket18Amps_Type = Integer32
_Slave_Global_socket18Amps_Object = MibScalar
slave_Global_socket18Amps = _Slave_Global_socket18Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 44),
    _Slave_Global_socket18Amps_Type()
)
slave_Global_socket18Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket18Amps.setStatus("current")
_Slave_Global_socket19Amps_Type = Integer32
_Slave_Global_socket19Amps_Object = MibScalar
slave_Global_socket19Amps = _Slave_Global_socket19Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 45),
    _Slave_Global_socket19Amps_Type()
)
slave_Global_socket19Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket19Amps.setStatus("current")
_Slave_Global_socket20Amps_Type = Integer32
_Slave_Global_socket20Amps_Object = MibScalar
slave_Global_socket20Amps = _Slave_Global_socket20Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 46),
    _Slave_Global_socket20Amps_Type()
)
slave_Global_socket20Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket20Amps.setStatus("current")
_Slave_Global_socket21Amps_Type = Integer32
_Slave_Global_socket21Amps_Object = MibScalar
slave_Global_socket21Amps = _Slave_Global_socket21Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 47),
    _Slave_Global_socket21Amps_Type()
)
slave_Global_socket21Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket21Amps.setStatus("current")
_Slave_Global_socket22Amps_Type = Integer32
_Slave_Global_socket22Amps_Object = MibScalar
slave_Global_socket22Amps = _Slave_Global_socket22Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 48),
    _Slave_Global_socket22Amps_Type()
)
slave_Global_socket22Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket22Amps.setStatus("current")
_Slave_Global_socket23Amps_Type = Integer32
_Slave_Global_socket23Amps_Object = MibScalar
slave_Global_socket23Amps = _Slave_Global_socket23Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 49),
    _Slave_Global_socket23Amps_Type()
)
slave_Global_socket23Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket23Amps.setStatus("current")
_Slave_Global_socket24Amps_Type = Integer32
_Slave_Global_socket24Amps_Object = MibScalar
slave_Global_socket24Amps = _Slave_Global_socket24Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 50),
    _Slave_Global_socket24Amps_Type()
)
slave_Global_socket24Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket24Amps.setStatus("current")
_Slave_Global_socket25Amps_Type = Integer32
_Slave_Global_socket25Amps_Object = MibScalar
slave_Global_socket25Amps = _Slave_Global_socket25Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 51),
    _Slave_Global_socket25Amps_Type()
)
slave_Global_socket25Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket25Amps.setStatus("current")
_Slave_Global_socket26Amps_Type = Integer32
_Slave_Global_socket26Amps_Object = MibScalar
slave_Global_socket26Amps = _Slave_Global_socket26Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 52),
    _Slave_Global_socket26Amps_Type()
)
slave_Global_socket26Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket26Amps.setStatus("current")
_Slave_Global_socket27Amps_Type = Integer32
_Slave_Global_socket27Amps_Object = MibScalar
slave_Global_socket27Amps = _Slave_Global_socket27Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 53),
    _Slave_Global_socket27Amps_Type()
)
slave_Global_socket27Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket27Amps.setStatus("current")
_Slave_Global_socket28Amps_Type = Integer32
_Slave_Global_socket28Amps_Object = MibScalar
slave_Global_socket28Amps = _Slave_Global_socket28Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 54),
    _Slave_Global_socket28Amps_Type()
)
slave_Global_socket28Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket28Amps.setStatus("current")
_Slave_Global_socket29Amps_Type = Integer32
_Slave_Global_socket29Amps_Object = MibScalar
slave_Global_socket29Amps = _Slave_Global_socket29Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 55),
    _Slave_Global_socket29Amps_Type()
)
slave_Global_socket29Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket29Amps.setStatus("current")
_Slave_Global_socket30Amps_Type = Integer32
_Slave_Global_socket30Amps_Object = MibScalar
slave_Global_socket30Amps = _Slave_Global_socket30Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 56),
    _Slave_Global_socket30Amps_Type()
)
slave_Global_socket30Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket30Amps.setStatus("current")
_Slave_Global_socket31Amps_Type = Integer32
_Slave_Global_socket31Amps_Object = MibScalar
slave_Global_socket31Amps = _Slave_Global_socket31Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 57),
    _Slave_Global_socket31Amps_Type()
)
slave_Global_socket31Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket31Amps.setStatus("current")
_Slave_Global_socket32Amps_Type = Integer32
_Slave_Global_socket32Amps_Object = MibScalar
slave_Global_socket32Amps = _Slave_Global_socket32Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 58),
    _Slave_Global_socket32Amps_Type()
)
slave_Global_socket32Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket32Amps.setStatus("current")
_Slave_Global_socket1kWh_Type = Integer32
_Slave_Global_socket1kWh_Object = MibScalar
slave_Global_socket1kWh = _Slave_Global_socket1kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 59),
    _Slave_Global_socket1kWh_Type()
)
slave_Global_socket1kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket1kWh.setStatus("current")
_Slave_Global_socket2kWh_Type = Integer32
_Slave_Global_socket2kWh_Object = MibScalar
slave_Global_socket2kWh = _Slave_Global_socket2kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 60),
    _Slave_Global_socket2kWh_Type()
)
slave_Global_socket2kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket2kWh.setStatus("current")
_Slave_Global_socket3kWh_Type = Integer32
_Slave_Global_socket3kWh_Object = MibScalar
slave_Global_socket3kWh = _Slave_Global_socket3kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 61),
    _Slave_Global_socket3kWh_Type()
)
slave_Global_socket3kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket3kWh.setStatus("current")
_Slave_Global_socket4kWh_Type = Integer32
_Slave_Global_socket4kWh_Object = MibScalar
slave_Global_socket4kWh = _Slave_Global_socket4kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 62),
    _Slave_Global_socket4kWh_Type()
)
slave_Global_socket4kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket4kWh.setStatus("current")
_Slave_Global_socket5kWh_Type = Integer32
_Slave_Global_socket5kWh_Object = MibScalar
slave_Global_socket5kWh = _Slave_Global_socket5kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 63),
    _Slave_Global_socket5kWh_Type()
)
slave_Global_socket5kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket5kWh.setStatus("current")
_Slave_Global_socket6kWh_Type = Integer32
_Slave_Global_socket6kWh_Object = MibScalar
slave_Global_socket6kWh = _Slave_Global_socket6kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 64),
    _Slave_Global_socket6kWh_Type()
)
slave_Global_socket6kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket6kWh.setStatus("current")
_Slave_Global_socket7kWh_Type = Integer32
_Slave_Global_socket7kWh_Object = MibScalar
slave_Global_socket7kWh = _Slave_Global_socket7kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 65),
    _Slave_Global_socket7kWh_Type()
)
slave_Global_socket7kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket7kWh.setStatus("current")
_Slave_Global_socket8kWh_Type = Integer32
_Slave_Global_socket8kWh_Object = MibScalar
slave_Global_socket8kWh = _Slave_Global_socket8kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 66),
    _Slave_Global_socket8kWh_Type()
)
slave_Global_socket8kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket8kWh.setStatus("current")
_Slave_Global_socket9kWh_Type = Integer32
_Slave_Global_socket9kWh_Object = MibScalar
slave_Global_socket9kWh = _Slave_Global_socket9kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 67),
    _Slave_Global_socket9kWh_Type()
)
slave_Global_socket9kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket9kWh.setStatus("current")
_Slave_Global_socket10kWh_Type = Integer32
_Slave_Global_socket10kWh_Object = MibScalar
slave_Global_socket10kWh = _Slave_Global_socket10kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 68),
    _Slave_Global_socket10kWh_Type()
)
slave_Global_socket10kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket10kWh.setStatus("current")
_Slave_Global_socket11kWh_Type = Integer32
_Slave_Global_socket11kWh_Object = MibScalar
slave_Global_socket11kWh = _Slave_Global_socket11kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 69),
    _Slave_Global_socket11kWh_Type()
)
slave_Global_socket11kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket11kWh.setStatus("current")
_Slave_Global_socket12kWh_Type = Integer32
_Slave_Global_socket12kWh_Object = MibScalar
slave_Global_socket12kWh = _Slave_Global_socket12kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 70),
    _Slave_Global_socket12kWh_Type()
)
slave_Global_socket12kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket12kWh.setStatus("current")
_Slave_Global_socket13kWh_Type = Integer32
_Slave_Global_socket13kWh_Object = MibScalar
slave_Global_socket13kWh = _Slave_Global_socket13kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 71),
    _Slave_Global_socket13kWh_Type()
)
slave_Global_socket13kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket13kWh.setStatus("current")
_Slave_Global_socket14kWh_Type = Integer32
_Slave_Global_socket14kWh_Object = MibScalar
slave_Global_socket14kWh = _Slave_Global_socket14kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 72),
    _Slave_Global_socket14kWh_Type()
)
slave_Global_socket14kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket14kWh.setStatus("current")
_Slave_Global_socket15kWh_Type = Integer32
_Slave_Global_socket15kWh_Object = MibScalar
slave_Global_socket15kWh = _Slave_Global_socket15kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 73),
    _Slave_Global_socket15kWh_Type()
)
slave_Global_socket15kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket15kWh.setStatus("current")
_Slave_Global_socket16kWh_Type = Integer32
_Slave_Global_socket16kWh_Object = MibScalar
slave_Global_socket16kWh = _Slave_Global_socket16kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 74),
    _Slave_Global_socket16kWh_Type()
)
slave_Global_socket16kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket16kWh.setStatus("current")
_Slave_Global_socket17kWh_Type = Integer32
_Slave_Global_socket17kWh_Object = MibScalar
slave_Global_socket17kWh = _Slave_Global_socket17kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 75),
    _Slave_Global_socket17kWh_Type()
)
slave_Global_socket17kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket17kWh.setStatus("current")
_Slave_Global_socket18kWh_Type = Integer32
_Slave_Global_socket18kWh_Object = MibScalar
slave_Global_socket18kWh = _Slave_Global_socket18kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 76),
    _Slave_Global_socket18kWh_Type()
)
slave_Global_socket18kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket18kWh.setStatus("current")
_Slave_Global_socket19kWh_Type = Integer32
_Slave_Global_socket19kWh_Object = MibScalar
slave_Global_socket19kWh = _Slave_Global_socket19kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 77),
    _Slave_Global_socket19kWh_Type()
)
slave_Global_socket19kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket19kWh.setStatus("current")
_Slave_Global_socket20kWh_Type = Integer32
_Slave_Global_socket20kWh_Object = MibScalar
slave_Global_socket20kWh = _Slave_Global_socket20kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 78),
    _Slave_Global_socket20kWh_Type()
)
slave_Global_socket20kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket20kWh.setStatus("current")
_Slave_Global_socket21kWh_Type = Integer32
_Slave_Global_socket21kWh_Object = MibScalar
slave_Global_socket21kWh = _Slave_Global_socket21kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 79),
    _Slave_Global_socket21kWh_Type()
)
slave_Global_socket21kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket21kWh.setStatus("current")
_Slave_Global_socket22kWh_Type = Integer32
_Slave_Global_socket22kWh_Object = MibScalar
slave_Global_socket22kWh = _Slave_Global_socket22kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 80),
    _Slave_Global_socket22kWh_Type()
)
slave_Global_socket22kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket22kWh.setStatus("current")
_Slave_Global_socket23kWh_Type = Integer32
_Slave_Global_socket23kWh_Object = MibScalar
slave_Global_socket23kWh = _Slave_Global_socket23kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 81),
    _Slave_Global_socket23kWh_Type()
)
slave_Global_socket23kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket23kWh.setStatus("current")
_Slave_Global_socket24kWh_Type = Integer32
_Slave_Global_socket24kWh_Object = MibScalar
slave_Global_socket24kWh = _Slave_Global_socket24kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 82),
    _Slave_Global_socket24kWh_Type()
)
slave_Global_socket24kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket24kWh.setStatus("current")
_Slave_Global_socket25kWh_Type = Integer32
_Slave_Global_socket25kWh_Object = MibScalar
slave_Global_socket25kWh = _Slave_Global_socket25kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 83),
    _Slave_Global_socket25kWh_Type()
)
slave_Global_socket25kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket25kWh.setStatus("current")
_Slave_Global_socket26kWh_Type = Integer32
_Slave_Global_socket26kWh_Object = MibScalar
slave_Global_socket26kWh = _Slave_Global_socket26kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 84),
    _Slave_Global_socket26kWh_Type()
)
slave_Global_socket26kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket26kWh.setStatus("current")
_Slave_Global_socket27kWh_Type = Integer32
_Slave_Global_socket27kWh_Object = MibScalar
slave_Global_socket27kWh = _Slave_Global_socket27kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 85),
    _Slave_Global_socket27kWh_Type()
)
slave_Global_socket27kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket27kWh.setStatus("current")
_Slave_Global_socket28kWh_Type = Integer32
_Slave_Global_socket28kWh_Object = MibScalar
slave_Global_socket28kWh = _Slave_Global_socket28kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 86),
    _Slave_Global_socket28kWh_Type()
)
slave_Global_socket28kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket28kWh.setStatus("current")
_Slave_Global_socket29kWh_Type = Integer32
_Slave_Global_socket29kWh_Object = MibScalar
slave_Global_socket29kWh = _Slave_Global_socket29kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 87),
    _Slave_Global_socket29kWh_Type()
)
slave_Global_socket29kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket29kWh.setStatus("current")
_Slave_Global_socket30kWh_Type = Integer32
_Slave_Global_socket30kWh_Object = MibScalar
slave_Global_socket30kWh = _Slave_Global_socket30kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 88),
    _Slave_Global_socket30kWh_Type()
)
slave_Global_socket30kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket30kWh.setStatus("current")
_Slave_Global_socket31kWh_Type = Integer32
_Slave_Global_socket31kWh_Object = MibScalar
slave_Global_socket31kWh = _Slave_Global_socket31kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 89),
    _Slave_Global_socket31kWh_Type()
)
slave_Global_socket31kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket31kWh.setStatus("current")
_Slave_Global_socket32kWh_Type = Integer32
_Slave_Global_socket32kWh_Object = MibScalar
slave_Global_socket32kWh = _Slave_Global_socket32kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 90),
    _Slave_Global_socket32kWh_Type()
)
slave_Global_socket32kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket32kWh.setStatus("current")
_Slave_Global_socket33Amps_Type = Integer32
_Slave_Global_socket33Amps_Object = MibScalar
slave_Global_socket33Amps = _Slave_Global_socket33Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 91),
    _Slave_Global_socket33Amps_Type()
)
slave_Global_socket33Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket33Amps.setStatus("current")
_Slave_Global_socket34Amps_Type = Integer32
_Slave_Global_socket34Amps_Object = MibScalar
slave_Global_socket34Amps = _Slave_Global_socket34Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 92),
    _Slave_Global_socket34Amps_Type()
)
slave_Global_socket34Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket34Amps.setStatus("current")
_Slave_Global_socket35Amps_Type = Integer32
_Slave_Global_socket35Amps_Object = MibScalar
slave_Global_socket35Amps = _Slave_Global_socket35Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 93),
    _Slave_Global_socket35Amps_Type()
)
slave_Global_socket35Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket35Amps.setStatus("current")
_Slave_Global_socket36Amps_Type = Integer32
_Slave_Global_socket36Amps_Object = MibScalar
slave_Global_socket36Amps = _Slave_Global_socket36Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 94),
    _Slave_Global_socket36Amps_Type()
)
slave_Global_socket36Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket36Amps.setStatus("current")
_Slave_Global_socket37Amps_Type = Integer32
_Slave_Global_socket37Amps_Object = MibScalar
slave_Global_socket37Amps = _Slave_Global_socket37Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 95),
    _Slave_Global_socket37Amps_Type()
)
slave_Global_socket37Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket37Amps.setStatus("current")
_Slave_Global_socket38Amps_Type = Integer32
_Slave_Global_socket38Amps_Object = MibScalar
slave_Global_socket38Amps = _Slave_Global_socket38Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 96),
    _Slave_Global_socket38Amps_Type()
)
slave_Global_socket38Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket38Amps.setStatus("current")
_Slave_Global_socket39Amps_Type = Integer32
_Slave_Global_socket39Amps_Object = MibScalar
slave_Global_socket39Amps = _Slave_Global_socket39Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 97),
    _Slave_Global_socket39Amps_Type()
)
slave_Global_socket39Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket39Amps.setStatus("current")
_Slave_Global_socket40Amps_Type = Integer32
_Slave_Global_socket40Amps_Object = MibScalar
slave_Global_socket40Amps = _Slave_Global_socket40Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 98),
    _Slave_Global_socket40Amps_Type()
)
slave_Global_socket40Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket40Amps.setStatus("current")
_Slave_Global_socket41Amps_Type = Integer32
_Slave_Global_socket41Amps_Object = MibScalar
slave_Global_socket41Amps = _Slave_Global_socket41Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 99),
    _Slave_Global_socket41Amps_Type()
)
slave_Global_socket41Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket41Amps.setStatus("current")
_Slave_Global_socket42Amps_Type = Integer32
_Slave_Global_socket42Amps_Object = MibScalar
slave_Global_socket42Amps = _Slave_Global_socket42Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 100),
    _Slave_Global_socket42Amps_Type()
)
slave_Global_socket42Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket42Amps.setStatus("current")
_Slave_Global_socket43Amps_Type = Integer32
_Slave_Global_socket43Amps_Object = MibScalar
slave_Global_socket43Amps = _Slave_Global_socket43Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 101),
    _Slave_Global_socket43Amps_Type()
)
slave_Global_socket43Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket43Amps.setStatus("current")
_Slave_Global_socket44Amps_Type = Integer32
_Slave_Global_socket44Amps_Object = MibScalar
slave_Global_socket44Amps = _Slave_Global_socket44Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 102),
    _Slave_Global_socket44Amps_Type()
)
slave_Global_socket44Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket44Amps.setStatus("current")
_Slave_Global_socket45Amps_Type = Integer32
_Slave_Global_socket45Amps_Object = MibScalar
slave_Global_socket45Amps = _Slave_Global_socket45Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 103),
    _Slave_Global_socket45Amps_Type()
)
slave_Global_socket45Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket45Amps.setStatus("current")
_Slave_Global_socket46Amps_Type = Integer32
_Slave_Global_socket46Amps_Object = MibScalar
slave_Global_socket46Amps = _Slave_Global_socket46Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 104),
    _Slave_Global_socket46Amps_Type()
)
slave_Global_socket46Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket46Amps.setStatus("current")
_Slave_Global_socket47Amps_Type = Integer32
_Slave_Global_socket47Amps_Object = MibScalar
slave_Global_socket47Amps = _Slave_Global_socket47Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 105),
    _Slave_Global_socket47Amps_Type()
)
slave_Global_socket47Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket47Amps.setStatus("current")
_Slave_Global_socket48Amps_Type = Integer32
_Slave_Global_socket48Amps_Object = MibScalar
slave_Global_socket48Amps = _Slave_Global_socket48Amps_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 106),
    _Slave_Global_socket48Amps_Type()
)
slave_Global_socket48Amps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket48Amps.setStatus("current")
_Slave_Global_socket33kWh_Type = Integer32
_Slave_Global_socket33kWh_Object = MibScalar
slave_Global_socket33kWh = _Slave_Global_socket33kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 107),
    _Slave_Global_socket33kWh_Type()
)
slave_Global_socket33kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket33kWh.setStatus("current")
_Slave_Global_socket34kWh_Type = Integer32
_Slave_Global_socket34kWh_Object = MibScalar
slave_Global_socket34kWh = _Slave_Global_socket34kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 108),
    _Slave_Global_socket34kWh_Type()
)
slave_Global_socket34kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket34kWh.setStatus("current")
_Slave_Global_socket35kWh_Type = Integer32
_Slave_Global_socket35kWh_Object = MibScalar
slave_Global_socket35kWh = _Slave_Global_socket35kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 109),
    _Slave_Global_socket35kWh_Type()
)
slave_Global_socket35kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket35kWh.setStatus("current")
_Slave_Global_socket36kWh_Type = Integer32
_Slave_Global_socket36kWh_Object = MibScalar
slave_Global_socket36kWh = _Slave_Global_socket36kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 110),
    _Slave_Global_socket36kWh_Type()
)
slave_Global_socket36kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket36kWh.setStatus("current")
_Slave_Global_socket37kWh_Type = Integer32
_Slave_Global_socket37kWh_Object = MibScalar
slave_Global_socket37kWh = _Slave_Global_socket37kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 111),
    _Slave_Global_socket37kWh_Type()
)
slave_Global_socket37kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket37kWh.setStatus("current")
_Slave_Global_socket38kWh_Type = Integer32
_Slave_Global_socket38kWh_Object = MibScalar
slave_Global_socket38kWh = _Slave_Global_socket38kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 112),
    _Slave_Global_socket38kWh_Type()
)
slave_Global_socket38kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket38kWh.setStatus("current")
_Slave_Global_socket39kWh_Type = Integer32
_Slave_Global_socket39kWh_Object = MibScalar
slave_Global_socket39kWh = _Slave_Global_socket39kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 113),
    _Slave_Global_socket39kWh_Type()
)
slave_Global_socket39kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket39kWh.setStatus("current")
_Slave_Global_socket40kWh_Type = Integer32
_Slave_Global_socket40kWh_Object = MibScalar
slave_Global_socket40kWh = _Slave_Global_socket40kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 114),
    _Slave_Global_socket40kWh_Type()
)
slave_Global_socket40kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket40kWh.setStatus("current")
_Slave_Global_socket41kWh_Type = Integer32
_Slave_Global_socket41kWh_Object = MibScalar
slave_Global_socket41kWh = _Slave_Global_socket41kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 115),
    _Slave_Global_socket41kWh_Type()
)
slave_Global_socket41kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket41kWh.setStatus("current")
_Slave_Global_socket42kWh_Type = Integer32
_Slave_Global_socket42kWh_Object = MibScalar
slave_Global_socket42kWh = _Slave_Global_socket42kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 116),
    _Slave_Global_socket42kWh_Type()
)
slave_Global_socket42kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket42kWh.setStatus("current")
_Slave_Global_socket43kWh_Type = Integer32
_Slave_Global_socket43kWh_Object = MibScalar
slave_Global_socket43kWh = _Slave_Global_socket43kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 117),
    _Slave_Global_socket43kWh_Type()
)
slave_Global_socket43kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket43kWh.setStatus("current")
_Slave_Global_socket44kWh_Type = Integer32
_Slave_Global_socket44kWh_Object = MibScalar
slave_Global_socket44kWh = _Slave_Global_socket44kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 118),
    _Slave_Global_socket44kWh_Type()
)
slave_Global_socket44kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket44kWh.setStatus("current")
_Slave_Global_socket45kWh_Type = Integer32
_Slave_Global_socket45kWh_Object = MibScalar
slave_Global_socket45kWh = _Slave_Global_socket45kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 119),
    _Slave_Global_socket45kWh_Type()
)
slave_Global_socket45kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket45kWh.setStatus("current")
_Slave_Global_socket46kWh_Type = Integer32
_Slave_Global_socket46kWh_Object = MibScalar
slave_Global_socket46kWh = _Slave_Global_socket46kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 120),
    _Slave_Global_socket46kWh_Type()
)
slave_Global_socket46kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket46kWh.setStatus("current")
_Slave_Global_socket47kWh_Type = Integer32
_Slave_Global_socket47kWh_Object = MibScalar
slave_Global_socket47kWh = _Slave_Global_socket47kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 121),
    _Slave_Global_socket47kWh_Type()
)
slave_Global_socket47kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket47kWh.setStatus("current")
_Slave_Global_socket48kWh_Type = Integer32
_Slave_Global_socket48kWh_Object = MibScalar
slave_Global_socket48kWh = _Slave_Global_socket48kWh_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 122),
    _Slave_Global_socket48kWh_Type()
)
slave_Global_socket48kWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_socket48kWh.setStatus("current")
_Slave_Global_sockets2_Type = Integer32
_Slave_Global_sockets2_Object = MibScalar
slave_Global_sockets2 = _Slave_Global_sockets2_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 123),
    _Slave_Global_sockets2_Type()
)
slave_Global_sockets2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slave_Global_sockets2.setStatus("current")
_Slave_Global_meter1_Freq_Type = Integer32
_Slave_Global_meter1_Freq_Object = MibScalar
slave_Global_meter1_Freq = _Slave_Global_meter1_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 124),
    _Slave_Global_meter1_Freq_Type()
)
slave_Global_meter1_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter1_Freq.setStatus("current")
_Slave_Global_meter2_VRMS_Type = Integer32
_Slave_Global_meter2_VRMS_Object = MibScalar
slave_Global_meter2_VRMS = _Slave_Global_meter2_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 125),
    _Slave_Global_meter2_VRMS_Type()
)
slave_Global_meter2_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_VRMS.setStatus("current")
_Slave_Global_meter2_IRMS_Type = Integer32
_Slave_Global_meter2_IRMS_Object = MibScalar
slave_Global_meter2_IRMS = _Slave_Global_meter2_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 126),
    _Slave_Global_meter2_IRMS_Type()
)
slave_Global_meter2_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_IRMS.setStatus("current")
_Slave_Global_meter2_KWH_Type = Integer32
_Slave_Global_meter2_KWH_Object = MibScalar
slave_Global_meter2_KWH = _Slave_Global_meter2_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 127),
    _Slave_Global_meter2_KWH_Type()
)
slave_Global_meter2_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_KWH.setStatus("current")
_Slave_Global_meter2_KW_Type = Integer32
_Slave_Global_meter2_KW_Object = MibScalar
slave_Global_meter2_KW = _Slave_Global_meter2_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 128),
    _Slave_Global_meter2_KW_Type()
)
slave_Global_meter2_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_KW.setStatus("current")
_Slave_Global_meter2_TPMU_Type = Integer32
_Slave_Global_meter2_TPMU_Object = MibScalar
slave_Global_meter2_TPMU = _Slave_Global_meter2_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 129),
    _Slave_Global_meter2_TPMU_Type()
)
slave_Global_meter2_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_TPMU.setStatus("current")
_Slave_Global_meter2_PF_Type = Integer32
_Slave_Global_meter2_PF_Object = MibScalar
slave_Global_meter2_PF = _Slave_Global_meter2_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 130),
    _Slave_Global_meter2_PF_Type()
)
slave_Global_meter2_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_PF.setStatus("current")
_Slave_Global_meter2_Freq_Type = Integer32
_Slave_Global_meter2_Freq_Object = MibScalar
slave_Global_meter2_Freq = _Slave_Global_meter2_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 131),
    _Slave_Global_meter2_Freq_Type()
)
slave_Global_meter2_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter2_Freq.setStatus("current")
_Slave_Global_meter3_VRMS_Type = Integer32
_Slave_Global_meter3_VRMS_Object = MibScalar
slave_Global_meter3_VRMS = _Slave_Global_meter3_VRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 132),
    _Slave_Global_meter3_VRMS_Type()
)
slave_Global_meter3_VRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_VRMS.setStatus("current")
_Slave_Global_meter3_IRMS_Type = Integer32
_Slave_Global_meter3_IRMS_Object = MibScalar
slave_Global_meter3_IRMS = _Slave_Global_meter3_IRMS_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 133),
    _Slave_Global_meter3_IRMS_Type()
)
slave_Global_meter3_IRMS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_IRMS.setStatus("current")
_Slave_Global_meter3_KWH_Type = Integer32
_Slave_Global_meter3_KWH_Object = MibScalar
slave_Global_meter3_KWH = _Slave_Global_meter3_KWH_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 134),
    _Slave_Global_meter3_KWH_Type()
)
slave_Global_meter3_KWH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_KWH.setStatus("current")
_Slave_Global_meter3_KW_Type = Integer32
_Slave_Global_meter3_KW_Object = MibScalar
slave_Global_meter3_KW = _Slave_Global_meter3_KW_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 135),
    _Slave_Global_meter3_KW_Type()
)
slave_Global_meter3_KW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_KW.setStatus("current")
_Slave_Global_meter3_TPMU_Type = Integer32
_Slave_Global_meter3_TPMU_Object = MibScalar
slave_Global_meter3_TPMU = _Slave_Global_meter3_TPMU_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 136),
    _Slave_Global_meter3_TPMU_Type()
)
slave_Global_meter3_TPMU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_TPMU.setStatus("current")
_Slave_Global_meter3_PF_Type = Integer32
_Slave_Global_meter3_PF_Object = MibScalar
slave_Global_meter3_PF = _Slave_Global_meter3_PF_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 137),
    _Slave_Global_meter3_PF_Type()
)
slave_Global_meter3_PF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_PF.setStatus("current")
_Slave_Global_meter3_Freq_Type = Integer32
_Slave_Global_meter3_Freq_Object = MibScalar
slave_Global_meter3_Freq = _Slave_Global_meter3_Freq_Object(
    (1, 3, 6, 1, 4, 1, 38218, 3, 1, 1, 138),
    _Slave_Global_meter3_Freq_Type()
)
slave_Global_meter3_Freq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slave_Global_meter3_Freq.setStatus("current")

# Managed Objects groups


# Notification objects

slave_Set_meter1_VRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 1)
)
slave_Set_meter1_VRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_VRMSLow.setStatus(
        "current"
    )

slave_Set_meter1_VRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 2)
)
slave_Set_meter1_VRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_VRMSHigh.setStatus(
        "current"
    )

slave_Set_meter1_IRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 3)
)
slave_Set_meter1_IRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_IRMSLow.setStatus(
        "current"
    )

slave_Set_meter1_IRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 4)
)
slave_Set_meter1_IRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_IRMSHigh.setStatus(
        "current"
    )

slave_Set_meter1_KWSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 5)
)
slave_Set_meter1_KWSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_KW"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_KWSLow.setStatus(
        "current"
    )

slave_Set_meter1_KWSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 6)
)
slave_Set_meter1_KWSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_KW"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_KWSHigh.setStatus(
        "current"
    )

slave_Set_meter1_TempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 7)
)
slave_Set_meter1_TempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_TempLow.setStatus(
        "current"
    )

slave_Set_meter1_TempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 8)
)
slave_Set_meter1_TempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_TempHigh.setStatus(
        "current"
    )

slave_Set_socket_AMPSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 9)
)
slave_Set_socket_AMPSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "socket_Number"))
)
if mibBuilder.loadTexts:
    slave_Set_socket_AMPSLow.setStatus(
        "current"
    )

slave_Set_socket_AMPSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 10)
)
slave_Set_socket_AMPSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "socket_Number"))
)
if mibBuilder.loadTexts:
    slave_Set_socket_AMPSHigh.setStatus(
        "current"
    )

slave_Set_environmental_Temp1Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 11)
)
slave_Set_environmental_Temp1Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp1"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp1Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp1High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 12)
)
slave_Set_environmental_Temp1High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp1"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp1High.setStatus(
        "current"
    )

slave_Set_environmental_Temp2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 13)
)
slave_Set_environmental_Temp2Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp2"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp2Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 14)
)
slave_Set_environmental_Temp2High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp2"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp2High.setStatus(
        "current"
    )

slave_Set_environmental_Temp3Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 15)
)
slave_Set_environmental_Temp3Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp3"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp3Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp3High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 16)
)
slave_Set_environmental_Temp3High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp3"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp3High.setStatus(
        "current"
    )

slave_Set_environmental_Temp4Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 17)
)
slave_Set_environmental_Temp4Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp4"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp4Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp4High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 18)
)
slave_Set_environmental_Temp4High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp4"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp4High.setStatus(
        "current"
    )

slave_Set_environmental_Temp5Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 19)
)
slave_Set_environmental_Temp5Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp5"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp5Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp5High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 20)
)
slave_Set_environmental_Temp5High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp5"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp5High.setStatus(
        "current"
    )

slave_Set_environmental_Temp6Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 21)
)
slave_Set_environmental_Temp6Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp6"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp6Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp6High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 22)
)
slave_Set_environmental_Temp6High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp6"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp6High.setStatus(
        "current"
    )

slave_Set_environmental_Temp7Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 23)
)
slave_Set_environmental_Temp7Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp7"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp7Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp7High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 24)
)
slave_Set_environmental_Temp7High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp7"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp7High.setStatus(
        "current"
    )

slave_Set_environmental_Temp8Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 25)
)
slave_Set_environmental_Temp8Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp8"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp8Low.setStatus(
        "current"
    )

slave_Set_environmental_Temp8High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 26)
)
slave_Set_environmental_Temp8High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp8"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Temp8High.setStatus(
        "current"
    )

slave_Set_environmental_HumidityTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 27)
)
slave_Set_environmental_HumidityTempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_HumidityTemp"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_HumidityTempLow.setStatus(
        "current"
    )

slave_Set_environmental_HumidityTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 28)
)
slave_Set_environmental_HumidityTempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_HumidityTemp"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_HumidityTempHigh.setStatus(
        "current"
    )

slave_Set_environmental_HumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 29)
)
slave_Set_environmental_HumidityLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Humidity"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_HumidityLow.setStatus(
        "current"
    )

slave_Set_environmental_HumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 30)
)
slave_Set_environmental_HumidityHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Humidity"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_HumidityHigh.setStatus(
        "current"
    )

slave_Set_environmental_Contact1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 31)
)
slave_Set_environmental_Contact1Open.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact1"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Contact1Open.setStatus(
        "current"
    )

slave_Set_environmental_Contact1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 32)
)
slave_Set_environmental_Contact1Closed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact1"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Contact1Closed.setStatus(
        "current"
    )

slave_Set_environmental_Contact2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 33)
)
slave_Set_environmental_Contact2Open.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact2"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Contact2Open.setStatus(
        "current"
    )

slave_Set_environmental_Contact2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 34)
)
slave_Set_environmental_Contact2Closed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact2"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Contact2Closed.setStatus(
        "current"
    )

slave_Set_environmental_Contact3Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 35)
)
slave_Set_environmental_Contact3Open.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact3"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Contact3Open.setStatus(
        "current"
    )

slave_Set_environmental_Contact3Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 36)
)
slave_Set_environmental_Contact3Closed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact3"))
)
if mibBuilder.loadTexts:
    slave_Set_environmental_Contact3Closed.setStatus(
        "current"
    )

slave_Set_Security_DoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 37)
)
slave_Set_Security_DoorOpen.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Door"))
)
if mibBuilder.loadTexts:
    slave_Set_Security_DoorOpen.setStatus(
        "current"
    )

slave_Set_Security_DoorClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 38)
)
slave_Set_Security_DoorClosed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Door"))
)
if mibBuilder.loadTexts:
    slave_Set_Security_DoorClosed.setStatus(
        "current"
    )

slave_Set_Security_LockUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 39)
)
slave_Set_Security_LockUnlocked.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Lock"))
)
if mibBuilder.loadTexts:
    slave_Set_Security_LockUnlocked.setStatus(
        "current"
    )

slave_Set_Security_LockLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 40)
)
slave_Set_Security_LockLocked.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Lock"))
)
if mibBuilder.loadTexts:
    slave_Set_Security_LockLocked.setStatus(
        "current"
    )

slave_Set_pduOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 41)
)
slave_Set_pduOffline.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_pduStatus"))
)
if mibBuilder.loadTexts:
    slave_Set_pduOffline.setStatus(
        "current"
    )

slave_Set_meter1_PFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 42)
)
slave_Set_meter1_PFLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_PF"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_PFLow.setStatus(
        "current"
    )

slave_Set_meter1_PFHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 43)
)
slave_Set_meter1_PFHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_PF"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_PFHigh.setStatus(
        "current"
    )

slave_Set_meter1_FreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 44)
)
slave_Set_meter1_FreqLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_Freq"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_FreqLow.setStatus(
        "current"
    )

slave_Set_meter1_FreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 45)
)
slave_Set_meter1_FreqHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_Freq"))
)
if mibBuilder.loadTexts:
    slave_Set_meter1_FreqHigh.setStatus(
        "current"
    )

slave_Set_meter2_VRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 46)
)
slave_Set_meter2_VRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_VRMSLow.setStatus(
        "current"
    )

slave_Set_meter2_VRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 47)
)
slave_Set_meter2_VRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_VRMSHigh.setStatus(
        "current"
    )

slave_Set_meter2_IRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 48)
)
slave_Set_meter2_IRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_IRMSLow.setStatus(
        "current"
    )

slave_Set_meter2_IRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 49)
)
slave_Set_meter2_IRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_IRMSHigh.setStatus(
        "current"
    )

slave_Set_meter2_KWSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 50)
)
slave_Set_meter2_KWSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_KW"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_KWSLow.setStatus(
        "current"
    )

slave_Set_meter2_KWSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 51)
)
slave_Set_meter2_KWSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_KW"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_KWSHigh.setStatus(
        "current"
    )

slave_Set_meter2_TempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 52)
)
slave_Set_meter2_TempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_TempLow.setStatus(
        "current"
    )

slave_Set_meter2_TempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 53)
)
slave_Set_meter2_TempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_TempHigh.setStatus(
        "current"
    )

slave_Set_meter2_PFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 54)
)
slave_Set_meter2_PFLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_PF"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_PFLow.setStatus(
        "current"
    )

slave_Set_meter2_PFHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 55)
)
slave_Set_meter2_PFHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_PF"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_PFHigh.setStatus(
        "current"
    )

slave_Set_meter2_FreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 56)
)
slave_Set_meter2_FreqLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_Freq"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_FreqLow.setStatus(
        "current"
    )

slave_Set_meter2_FreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 57)
)
slave_Set_meter2_FreqHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_Freq"))
)
if mibBuilder.loadTexts:
    slave_Set_meter2_FreqHigh.setStatus(
        "current"
    )

slave_Set_meter3_VRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 58)
)
slave_Set_meter3_VRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_VRMSLow.setStatus(
        "current"
    )

slave_Set_meter3_VRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 59)
)
slave_Set_meter3_VRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_VRMSHigh.setStatus(
        "current"
    )

slave_Set_meter3_IRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 60)
)
slave_Set_meter3_IRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_IRMSLow.setStatus(
        "current"
    )

slave_Set_meter3_IRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 61)
)
slave_Set_meter3_IRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_IRMSHigh.setStatus(
        "current"
    )

slave_Set_meter3_KWSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 62)
)
slave_Set_meter3_KWSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_KW"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_KWSLow.setStatus(
        "current"
    )

slave_Set_meter3_KWSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 63)
)
slave_Set_meter3_KWSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_KW"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_KWSHigh.setStatus(
        "current"
    )

slave_Set_meter3_TempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 64)
)
slave_Set_meter3_TempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_TempLow.setStatus(
        "current"
    )

slave_Set_meter3_TempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 65)
)
slave_Set_meter3_TempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_TempHigh.setStatus(
        "current"
    )

slave_Set_meter3_PFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 66)
)
slave_Set_meter3_PFLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_PF"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_PFLow.setStatus(
        "current"
    )

slave_Set_meter3_PFHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 67)
)
slave_Set_meter3_PFHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_PF"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_PFHigh.setStatus(
        "current"
    )

slave_Set_meter3_FreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 68)
)
slave_Set_meter3_FreqLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_Freq"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_FreqLow.setStatus(
        "current"
    )

slave_Set_meter3_FreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 1, 69)
)
slave_Set_meter3_FreqHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_Freq"))
)
if mibBuilder.loadTexts:
    slave_Set_meter3_FreqHigh.setStatus(
        "current"
    )

slave_Clear_meter1_VRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 1)
)
slave_Clear_meter1_VRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_VRMSLow.setStatus(
        "current"
    )

slave_Clear_meter1_VRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 2)
)
slave_Clear_meter1_VRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_VRMSHigh.setStatus(
        "current"
    )

slave_Clear_meter1_IRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 3)
)
slave_Clear_meter1_IRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_IRMSLow.setStatus(
        "current"
    )

slave_Clear_meter1_IRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 4)
)
slave_Clear_meter1_IRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_IRMSHigh.setStatus(
        "current"
    )

slave_Clear_meter1_KWSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 5)
)
slave_Clear_meter1_KWSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_KW"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_KWSLow.setStatus(
        "current"
    )

slave_Clear_meter1_KWSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 6)
)
slave_Clear_meter1_KWSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_KW"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_KWSHigh.setStatus(
        "current"
    )

slave_Clear_meter1_TempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 7)
)
slave_Clear_meter1_TempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_TempLow.setStatus(
        "current"
    )

slave_Clear_meter1_TempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 8)
)
slave_Clear_meter1_TempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_TempHigh.setStatus(
        "current"
    )

slave_Clear_socket_AMPSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 9)
)
slave_Clear_socket_AMPSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "socket_Number"))
)
if mibBuilder.loadTexts:
    slave_Clear_socket_AMPSLow.setStatus(
        "current"
    )

slave_Clear_socket_AMPSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 10)
)
slave_Clear_socket_AMPSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "socket_Number"))
)
if mibBuilder.loadTexts:
    slave_Clear_socket_AMPSHigh.setStatus(
        "current"
    )

slave_Clear_environmental_Temp1Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 11)
)
slave_Clear_environmental_Temp1Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp1"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp1Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp1High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 12)
)
slave_Clear_environmental_Temp1High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp1"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp1High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp2Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 13)
)
slave_Clear_environmental_Temp2Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp2"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp2Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp2High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 14)
)
slave_Clear_environmental_Temp2High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp2"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp2High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp3Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 15)
)
slave_Clear_environmental_Temp3Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp3"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp3Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp3High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 16)
)
slave_Clear_environmental_Temp3High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp3"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp3High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp4Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 17)
)
slave_Clear_environmental_Temp4Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp4"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp4Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp4High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 18)
)
slave_Clear_environmental_Temp4High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp4"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp4High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp5Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 19)
)
slave_Clear_environmental_Temp5Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp5"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp5Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp5High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 20)
)
slave_Clear_environmental_Temp5High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp5"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp5High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp6Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 21)
)
slave_Clear_environmental_Temp6Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp6"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp6Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp6High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 22)
)
slave_Clear_environmental_Temp6High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp6"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp6High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp7Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 23)
)
slave_Clear_environmental_Temp7Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp7"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp7Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp7High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 24)
)
slave_Clear_environmental_Temp7High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp7"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp7High.setStatus(
        "current"
    )

slave_Clear_environmental_Temp8Low = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 25)
)
slave_Clear_environmental_Temp8Low.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp8"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp8Low.setStatus(
        "current"
    )

slave_Clear_environmental_Temp8High = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 26)
)
slave_Clear_environmental_Temp8High.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Temp8"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Temp8High.setStatus(
        "current"
    )

slave_Clear_environmental_HumidityTempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 27)
)
slave_Clear_environmental_HumidityTempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_HumidityTemp"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_HumidityTempLow.setStatus(
        "current"
    )

slave_Clear_environmental_HumidityTempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 28)
)
slave_Clear_environmental_HumidityTempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_HumidityTemp"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_HumidityTempHigh.setStatus(
        "current"
    )

slave_Clear_environmental_HumidityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 29)
)
slave_Clear_environmental_HumidityLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Humidity"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_HumidityLow.setStatus(
        "current"
    )

slave_Clear_environmental_HumidityHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 30)
)
slave_Clear_environmental_HumidityHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Humidity"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_HumidityHigh.setStatus(
        "current"
    )

slave_Clear_environmental_Contact1Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 31)
)
slave_Clear_environmental_Contact1Open.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact1"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Contact1Open.setStatus(
        "current"
    )

slave_Clear_environmental_Contact1Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 32)
)
slave_Clear_environmental_Contact1Closed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact1"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Contact1Closed.setStatus(
        "current"
    )

slave_Clear_environmental_Contact2Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 33)
)
slave_Clear_environmental_Contact2Open.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact2"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Contact2Open.setStatus(
        "current"
    )

slave_Clear_environmental_Contact2Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 34)
)
slave_Clear_environmental_Contact2Closed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact2"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Contact2Closed.setStatus(
        "current"
    )

slave_Clear_environmental_Contact3Open = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 35)
)
slave_Clear_environmental_Contact3Open.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact3"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Contact3Open.setStatus(
        "current"
    )

slave_Clear_environmental_Contact3Closed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 36)
)
slave_Clear_environmental_Contact3Closed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_environmental_Contact3"))
)
if mibBuilder.loadTexts:
    slave_Clear_environmental_Contact3Closed.setStatus(
        "current"
    )

slave_Clear_Security_DoorOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 37)
)
slave_Clear_Security_DoorOpen.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Door"))
)
if mibBuilder.loadTexts:
    slave_Clear_Security_DoorOpen.setStatus(
        "current"
    )

slave_Clear_Security_DoorClosed = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 38)
)
slave_Clear_Security_DoorClosed.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Door"))
)
if mibBuilder.loadTexts:
    slave_Clear_Security_DoorClosed.setStatus(
        "current"
    )

slave_Clear_Security_LockUnlocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 39)
)
slave_Clear_Security_LockUnlocked.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Lock"))
)
if mibBuilder.loadTexts:
    slave_Clear_Security_LockUnlocked.setStatus(
        "current"
    )

slave_Clear_Security_LockLocked = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 40)
)
slave_Clear_Security_LockLocked.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_Security_Lock"))
)
if mibBuilder.loadTexts:
    slave_Clear_Security_LockLocked.setStatus(
        "current"
    )

slave_Clear_pduOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 41)
)
slave_Clear_pduOffline.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_pduStatus"))
)
if mibBuilder.loadTexts:
    slave_Clear_pduOffline.setStatus(
        "current"
    )

slave_Clear_meter1_PFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 42)
)
slave_Clear_meter1_PFLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_PF"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_PFLow.setStatus(
        "current"
    )

slave_Clear_meter1_PFHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 43)
)
slave_Clear_meter1_PFHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_PF"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_PFHigh.setStatus(
        "current"
    )

slave_Clear_meter1_FreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 44)
)
slave_Clear_meter1_FreqLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_Freq"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_FreqLow.setStatus(
        "current"
    )

slave_Clear_meter1_FreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 45)
)
slave_Clear_meter1_FreqHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter1_Freq"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter1_FreqHigh.setStatus(
        "current"
    )

slave_Clear_meter2_VRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 46)
)
slave_Clear_meter2_VRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_VRMSLow.setStatus(
        "current"
    )

slave_Clear_meter2_VRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 47)
)
slave_Clear_meter2_VRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_VRMSHigh.setStatus(
        "current"
    )

slave_Clear_meter2_IRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 48)
)
slave_Clear_meter2_IRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_IRMSLow.setStatus(
        "current"
    )

slave_Clear_meter2_IRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 49)
)
slave_Clear_meter2_IRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_IRMSHigh.setStatus(
        "current"
    )

slave_Clear_meter2_KWSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 50)
)
slave_Clear_meter2_KWSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_KW"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_KWSLow.setStatus(
        "current"
    )

slave_Clear_meter2_KWSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 51)
)
slave_Clear_meter2_KWSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_KW"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_KWSHigh.setStatus(
        "current"
    )

slave_Clear_meter2_TempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 52)
)
slave_Clear_meter2_TempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_TempLow.setStatus(
        "current"
    )

slave_Clear_meter2_TempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 53)
)
slave_Clear_meter2_TempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_TempHigh.setStatus(
        "current"
    )

slave_Clear_meter2_PFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 54)
)
slave_Clear_meter2_PFLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_PF"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_PFLow.setStatus(
        "current"
    )

slave_Clear_meter2_PFHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 55)
)
slave_Clear_meter2_PFHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_PF"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_PFHigh.setStatus(
        "current"
    )

slave_Clear_meter2_FreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 56)
)
slave_Clear_meter2_FreqLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_Freq"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_FreqLow.setStatus(
        "current"
    )

slave_Clear_meter2_FreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 57)
)
slave_Clear_meter2_FreqHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter2_Freq"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter2_FreqHigh.setStatus(
        "current"
    )

slave_Clear_meter3_VRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 58)
)
slave_Clear_meter3_VRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_VRMSLow.setStatus(
        "current"
    )

slave_Clear_meter3_VRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 59)
)
slave_Clear_meter3_VRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_VRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_VRMSHigh.setStatus(
        "current"
    )

slave_Clear_meter3_IRMSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 60)
)
slave_Clear_meter3_IRMSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_IRMSLow.setStatus(
        "current"
    )

slave_Clear_meter3_IRMSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 61)
)
slave_Clear_meter3_IRMSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_IRMS"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_IRMSHigh.setStatus(
        "current"
    )

slave_Clear_meter3_KWSLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 62)
)
slave_Clear_meter3_KWSLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_KW"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_KWSLow.setStatus(
        "current"
    )

slave_Clear_meter3_KWSHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 63)
)
slave_Clear_meter3_KWSHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_KW"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_KWSHigh.setStatus(
        "current"
    )

slave_Clear_meter3_TempLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 64)
)
slave_Clear_meter3_TempLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_TempLow.setStatus(
        "current"
    )

slave_Clear_meter3_TempHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 65)
)
slave_Clear_meter3_TempHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_TPMU"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_TempHigh.setStatus(
        "current"
    )

slave_Clear_meter3_PFLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 66)
)
slave_Clear_meter3_PFLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_PF"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_PFLow.setStatus(
        "current"
    )

slave_Clear_meter3_PFHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 67)
)
slave_Clear_meter3_PFHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_PF"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_PFHigh.setStatus(
        "current"
    )

slave_Clear_meter3_FreqLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 68)
)
slave_Clear_meter3_FreqLow.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_Freq"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_FreqLow.setStatus(
        "current"
    )

slave_Clear_meter3_FreqHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 38218, 2, 7, 2, 69)
)
slave_Clear_meter3_FreqHigh.setObjects(
      *(("PDUSNMP", "pdu_ClientName"),
        ("PDUSNMP", "pdu_LocationName"),
        ("PDUSNMP", "slave_pduAddress"),
        ("PDUSNMP", "slave_meter3_Freq"))
)
if mibBuilder.loadTexts:
    slave_Clear_meter3_FreqHigh.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDUSNMP",
    **{"ipt-pdu-SNMP": ipt_pdu_SNMP,
       "pdu-SNMP": pdu_SNMP,
       "slave-SiteTotals": slave_SiteTotals,
       "slave-SiteTotalkWh": slave_SiteTotalkWh,
       "slave-SiteTotalBtu": slave_SiteTotalBtu,
       "slave-SiteTotalKgCO2": slave_SiteTotalKgCO2,
       "slave-Server": slave_Server,
       "slave-Nopdus": slave_Nopdus,
       "slaves-Online": slaves_Online,
       "slave-ServerStatus": slave_ServerStatus,
       "pdu-Configuration": pdu_Configuration,
       "pdu-ClientName": pdu_ClientName,
       "pdu-LocationName": pdu_LocationName,
       "pdu-FirmwareVersion": pdu_FirmwareVersion,
       "pdu-KgCO2Conversion": pdu_KgCO2Conversion,
       "pdu-MODBUSTimeout": pdu_MODBUSTimeout,
       "pdu-MODBUSRetry": pdu_MODBUSRetry,
       "pdu-NotUsed1": pdu_NotUsed1,
       "pdu-AlarmPeriod": pdu_AlarmPeriod,
       "pdu-DHCPStatus": pdu_DHCPStatus,
       "pdu-IPAddress": pdu_IPAddress,
       "pdu-SubNetMask": pdu_SubNetMask,
       "pdu-CabinetID": pdu_CabinetID,
       "pdu-socketPeriod": pdu_socketPeriod,
       "pdu-LockPeriod": pdu_LockPeriod,
       "pdu-RTC-Hour": pdu_RTC_Hour,
       "pdu-RTC-Minute": pdu_RTC_Minute,
       "pdu-RTC-Date": pdu_RTC_Date,
       "pdu-RTC-Month": pdu_RTC_Month,
       "pdu-RTC-Year": pdu_RTC_Year,
       "trap-Destinations": trap_Destinations,
       "trapDestinationsTable": trapDestinationsTable,
       "trapDestinationsEntry": trapDestinationsEntry,
       "trapDestinationsIndex": trapDestinationsIndex,
       "trapDestinationsStatus": trapDestinationsStatus,
       "trapDestinationsIP": trapDestinationsIP,
       "trapDestinationsCommunity": trapDestinationsCommunity,
       "pdu-Information": pdu_Information,
       "pdu-Firmware": pdu_Firmware,
       "pdu-Nosockets": pdu_Nosockets,
       "pdu-ProductName": pdu_ProductName,
       "pdu-SerialNumber": pdu_SerialNumber,
       "pdu-Meters": pdu_Meters,
       "pdu-meter1-VRMS": pdu_meter1_VRMS,
       "pdu-meter1-IRMS": pdu_meter1_IRMS,
       "pdu-meter1-KWH": pdu_meter1_KWH,
       "pdu-meter1-KW": pdu_meter1_KW,
       "pdu-meter1-TPMU": pdu_meter1_TPMU,
       "pdu-meter1-IPK": pdu_meter1_IPK,
       "pdu-meter1-VPK": pdu_meter1_VPK,
       "pdu-meter1-PF": pdu_meter1_PF,
       "pdu-meter1-Freq": pdu_meter1_Freq,
       "pdu-meter2-VRMS": pdu_meter2_VRMS,
       "pdu-meter2-IRMS": pdu_meter2_IRMS,
       "pdu-meter2-KWH": pdu_meter2_KWH,
       "pdu-meter2-KW": pdu_meter2_KW,
       "pdu-meter2-TPMU": pdu_meter2_TPMU,
       "pdu-meter2-IPK": pdu_meter2_IPK,
       "pdu-meter2-VPK": pdu_meter2_VPK,
       "pdu-meter2-PF": pdu_meter2_PF,
       "pdu-meter2-Freq": pdu_meter2_Freq,
       "pdu-meter3-VRMS": pdu_meter3_VRMS,
       "pdu-meter3-IRMS": pdu_meter3_IRMS,
       "pdu-meter3-KWH": pdu_meter3_KWH,
       "pdu-meter3-KW": pdu_meter3_KW,
       "pdu-meter3-TPMU": pdu_meter3_TPMU,
       "pdu-meter3-IPK": pdu_meter3_IPK,
       "pdu-meter3-VPK": pdu_meter3_VPK,
       "pdu-meter3-PF": pdu_meter3_PF,
       "pdu-meter3-Freq": pdu_meter3_Freq,
       "pdu-sockets": pdu_sockets,
       "pdu-socketsTable": pdu_socketsTable,
       "pdu-socketsEntry": pdu_socketsEntry,
       "socket-Index": socket_Index,
       "socket-Number": socket_Number,
       "socket-Equipment": socket_Equipment,
       "socket-ONOFF": socket_ONOFF,
       "socket-AMPS": socket_AMPS,
       "socket-KWH": socket_KWH,
       "socket-INFO": socket_INFO,
       "pdu-Environmental": pdu_Environmental,
       "pdu-environmental-Temp1": pdu_environmental_Temp1,
       "pdu-environmental-Temp1-Location": pdu_environmental_Temp1_Location,
       "pdu-environmental-Temp2": pdu_environmental_Temp2,
       "pdu-environmental-Temp2-Location": pdu_environmental_Temp2_Location,
       "pdu-environmental-Temp3": pdu_environmental_Temp3,
       "pdu-environmental-Temp3-Location": pdu_environmental_Temp3_Location,
       "pdu-environmental-Temp4": pdu_environmental_Temp4,
       "pdu-environmental-Temp4-Location": pdu_environmental_Temp4_Location,
       "pdu-environmental-Temp5": pdu_environmental_Temp5,
       "pdu-environmental-Temp5-Location": pdu_environmental_Temp5_Location,
       "pdu-environmental-Temp6": pdu_environmental_Temp6,
       "pdu-environmental-Temp6-Location": pdu_environmental_Temp6_Location,
       "pdu-environmental-Temp7": pdu_environmental_Temp7,
       "pdu-environmental-Temp7-Location": pdu_environmental_Temp7_Location,
       "pdu-environmental-Temp8": pdu_environmental_Temp8,
       "pdu-environmental-Temp8-Location": pdu_environmental_Temp8_Location,
       "pdu-environmental-HumidityTemp": pdu_environmental_HumidityTemp,
       "pdu-environmental-Humidity": pdu_environmental_Humidity,
       "pdu-environmental-Contact1": pdu_environmental_Contact1,
       "pdu-environmental-Contact1-Location": pdu_environmental_Contact1_Location,
       "pdu-environmental-Contact2": pdu_environmental_Contact2,
       "pdu-environmental-Contact2-Location": pdu_environmental_Contact2_Location,
       "pdu-environmental-Contact3": pdu_environmental_Contact3,
       "pdu-environmental-Contact3-Location": pdu_environmental_Contact3_Location,
       "pdu-Security": pdu_Security,
       "pdu-Security-Door": pdu_Security_Door,
       "pdu-Security-Lock": pdu_Security_Lock,
       "pdu-Security-Wild": pdu_Security_Wild,
       "pdu-Security-UnlockTimeDate": pdu_Security_UnlockTimeDate,
       "pdu-SecurityTable": pdu_SecurityTable,
       "pdu-SecurityEntry": pdu_SecurityEntry,
       "pdu-Security-Index": pdu_Security_Index,
       "pdu-Security-Code": pdu_Security_Code,
       "pdu-Logs": pdu_Logs,
       "pdu-Logs-Number": pdu_Logs_Number,
       "pdu-Logs-Index": pdu_Logs_Index,
       "pdu-Logs-Data": pdu_Logs_Data,
       "pdu-Logs-Clear": pdu_Logs_Clear,
       "pdu-Traps": pdu_Traps,
       "pdu-TrapThresholds": pdu_TrapThresholds,
       "meter1-VRMSLowAlarm": meter1_VRMSLowAlarm,
       "meter1-VRMSLow": meter1_VRMSLow,
       "meter1-VRMSHighAlarm": meter1_VRMSHighAlarm,
       "meter1-VRMSHigh": meter1_VRMSHigh,
       "meter1-IRMSLowAlarm": meter1_IRMSLowAlarm,
       "meter1-IRMSLow": meter1_IRMSLow,
       "meter1-IRMSHighAlarm": meter1_IRMSHighAlarm,
       "meter1-IRMSHigh": meter1_IRMSHigh,
       "meter1-KWSLowAlarm": meter1_KWSLowAlarm,
       "meter1-KWSLow": meter1_KWSLow,
       "meter1-KWSHighAlarm": meter1_KWSHighAlarm,
       "meter1-KWSHigh": meter1_KWSHigh,
       "meter1-TempLowAlarm": meter1_TempLowAlarm,
       "meter1-TempLow": meter1_TempLow,
       "meter1-TempHighAlarm": meter1_TempHighAlarm,
       "meter1-TempHigh": meter1_TempHigh,
       "meter1-PFLowAlarm": meter1_PFLowAlarm,
       "meter1-PFLow": meter1_PFLow,
       "meter1-PFHighAlarm": meter1_PFHighAlarm,
       "meter1-PFHigh": meter1_PFHigh,
       "meter1-FreqLowAlarm": meter1_FreqLowAlarm,
       "meter1-FreqLow": meter1_FreqLow,
       "meter1-FreqHighAlarm": meter1_FreqHighAlarm,
       "meter1-FreqHigh": meter1_FreqHigh,
       "meter2-VRMSLowAlarm": meter2_VRMSLowAlarm,
       "meter2-VRMSLow": meter2_VRMSLow,
       "meter2-VRMSHighAlarm": meter2_VRMSHighAlarm,
       "meter2-VRMSHigh": meter2_VRMSHigh,
       "meter2-IRMSLowAlarm": meter2_IRMSLowAlarm,
       "meter2-IRMSLow": meter2_IRMSLow,
       "meter2-IRMSHighAlarm": meter2_IRMSHighAlarm,
       "meter2-IRMSHigh": meter2_IRMSHigh,
       "meter2-KWSLowAlarm": meter2_KWSLowAlarm,
       "meter2-KWSLow": meter2_KWSLow,
       "meter2-KWSHighAlarm": meter2_KWSHighAlarm,
       "meter2-KWSHigh": meter2_KWSHigh,
       "meter2-TempLowAlarm": meter2_TempLowAlarm,
       "meter2-TempLow": meter2_TempLow,
       "meter2-TempHighAlarm": meter2_TempHighAlarm,
       "meter2-TempHigh": meter2_TempHigh,
       "meter2-PFLowAlarm": meter2_PFLowAlarm,
       "meter2-PFLow": meter2_PFLow,
       "meter2-PFHighAlarm": meter2_PFHighAlarm,
       "meter2-PFHigh": meter2_PFHigh,
       "meter2-FreqLowAlarm": meter2_FreqLowAlarm,
       "meter2-FreqLow": meter2_FreqLow,
       "meter2-FreqHighAlarm": meter2_FreqHighAlarm,
       "meter2-FreqHigh": meter2_FreqHigh,
       "meter3-VRMSLowAlarm": meter3_VRMSLowAlarm,
       "meter3-VRMSLow": meter3_VRMSLow,
       "meter3-VRMSHighAlarm": meter3_VRMSHighAlarm,
       "meter3-VRMSHigh": meter3_VRMSHigh,
       "meter3-IRMSLowAlarm": meter3_IRMSLowAlarm,
       "meter3-IRMSLow": meter3_IRMSLow,
       "meter3-IRMSHighAlarm": meter3_IRMSHighAlarm,
       "meter3-IRMSHigh": meter3_IRMSHigh,
       "meter3-KWSLowAlarm": meter3_KWSLowAlarm,
       "meter3-KWSLow": meter3_KWSLow,
       "meter3-KWSHighAlarm": meter3_KWSHighAlarm,
       "meter3-KWSHigh": meter3_KWSHigh,
       "meter3-TempLowAlarm": meter3_TempLowAlarm,
       "meter3-TempLow": meter3_TempLow,
       "meter3-TempHighAlarm": meter3_TempHighAlarm,
       "meter3-TempHigh": meter3_TempHigh,
       "meter3-PFLowAlarm": meter3_PFLowAlarm,
       "meter3-PFLow": meter3_PFLow,
       "meter3-PFHighAlarm": meter3_PFHighAlarm,
       "meter3-PFHigh": meter3_PFHigh,
       "meter3-FreqLowAlarm": meter3_FreqLowAlarm,
       "meter3-FreqLow": meter3_FreqLow,
       "meter3-FreqHighAlarm": meter3_FreqHighAlarm,
       "meter3-FreqHigh": meter3_FreqHigh,
       "socket-ThresholdsTable": socket_ThresholdsTable,
       "socket-ThresholdsEntry": socket_ThresholdsEntry,
       "socket-ThresholdsNumber": socket_ThresholdsNumber,
       "socket-AMPSLowAlarm": socket_AMPSLowAlarm,
       "socket-AMPSLow": socket_AMPSLow,
       "socket-AMPSHighAlarm": socket_AMPSHighAlarm,
       "socket-AMPSHigh": socket_AMPSHigh,
       "environmental-Temp1LowAlarm": environmental_Temp1LowAlarm,
       "environmental-Temp1Low": environmental_Temp1Low,
       "environmental-Temp1HighAlarm": environmental_Temp1HighAlarm,
       "environmental-Temp1High": environmental_Temp1High,
       "environmental-Temp2LowAlarm": environmental_Temp2LowAlarm,
       "environmental-Temp2Low": environmental_Temp2Low,
       "environmental-Temp2HighAlarm": environmental_Temp2HighAlarm,
       "environmental-Temp2High": environmental_Temp2High,
       "environmental-Temp3LowAlarm": environmental_Temp3LowAlarm,
       "environmental-Temp3Low": environmental_Temp3Low,
       "environmental-Temp3HighAlarm": environmental_Temp3HighAlarm,
       "environmental-Temp3High": environmental_Temp3High,
       "environmental-Temp4LowAlarm": environmental_Temp4LowAlarm,
       "environmental-Temp4Low": environmental_Temp4Low,
       "environmental-Temp4HighAlarm": environmental_Temp4HighAlarm,
       "environmental-Temp4High": environmental_Temp4High,
       "environmental-Temp5LowAlarm": environmental_Temp5LowAlarm,
       "environmental-Temp5Low": environmental_Temp5Low,
       "environmental-Temp5HighAlarm": environmental_Temp5HighAlarm,
       "environmental-Temp5High": environmental_Temp5High,
       "environmental-Temp6LowAlarm": environmental_Temp6LowAlarm,
       "environmental-Temp6Low": environmental_Temp6Low,
       "environmental-Temp6HighAlarm": environmental_Temp6HighAlarm,
       "environmental-Temp6High": environmental_Temp6High,
       "environmental-Temp7LowAlarm": environmental_Temp7LowAlarm,
       "environmental-Temp7Low": environmental_Temp7Low,
       "environmental-Temp7HighAlarm": environmental_Temp7HighAlarm,
       "environmental-Temp7High": environmental_Temp7High,
       "environmental-Temp8LowAlarm": environmental_Temp8LowAlarm,
       "environmental-Temp8Low": environmental_Temp8Low,
       "environmental-Temp8HighAlarm": environmental_Temp8HighAlarm,
       "environmental-Temp8High": environmental_Temp8High,
       "environmental-HumidityTempLowAlarm": environmental_HumidityTempLowAlarm,
       "environmental-HumidityTempLow": environmental_HumidityTempLow,
       "environmental-HumidityTempHighAlarm": environmental_HumidityTempHighAlarm,
       "environmental-HumidityTempHigh": environmental_HumidityTempHigh,
       "environmental-HumidityLowAlarm": environmental_HumidityLowAlarm,
       "environmental-HumidityLow": environmental_HumidityLow,
       "environmental-HumidityHighAlarm": environmental_HumidityHighAlarm,
       "environmental-HumidityHigh": environmental_HumidityHigh,
       "environmental-Contact1OpenedAlarm": environmental_Contact1OpenedAlarm,
       "environmental-Contact1ClosedAlarm": environmental_Contact1ClosedAlarm,
       "environmental-Contact2OpenedAlarm": environmental_Contact2OpenedAlarm,
       "environmental-Contact2ClosedAlarm": environmental_Contact2ClosedAlarm,
       "environmental-Contact3OpenedAlarm": environmental_Contact3OpenedAlarm,
       "environmental-Contact3ClosedAlarm": environmental_Contact3ClosedAlarm,
       "security-DoorOpenedAlarm": security_DoorOpenedAlarm,
       "security-DoorClosedAlarm": security_DoorClosedAlarm,
       "security-LockUnlockedAlarm": security_LockUnlockedAlarm,
       "security-LockLockedAlarm": security_LockLockedAlarm,
       "slave-pdus": slave_pdus,
       "slave-slaveSelected": slave_slaveSelected,
       "slave-Information": slave_Information,
       "slave-pduName": slave_pduName,
       "slave-pduStatus": slave_pduStatus,
       "slave-pduAddress": slave_pduAddress,
       "slave-pduFirmware": slave_pduFirmware,
       "slave-Info-NotUsed2": slave_Info_NotUsed2,
       "slave-pduNosockets": slave_pduNosockets,
       "slave-Info-NotUsed3": slave_Info_NotUsed3,
       "slave-Info-NotUsed4": slave_Info_NotUsed4,
       "slave-Info-pduReset": slave_Info_pduReset,
       "slave-Info-pdukWhReset": slave_Info_pdukWhReset,
       "slave-Status": slave_Status,
       "slave-meter1-VRMS": slave_meter1_VRMS,
       "slave-meter1-IRMS": slave_meter1_IRMS,
       "slave-meter1-KWH": slave_meter1_KWH,
       "slave-meter1-KW": slave_meter1_KW,
       "slave-meter1-TPMU": slave_meter1_TPMU,
       "slave-Status-NotUsed1": slave_Status_NotUsed1,
       "slave-Status-NotUsed2": slave_Status_NotUsed2,
       "slave-meter1-IPK": slave_meter1_IPK,
       "slave-meter1-VPK": slave_meter1_VPK,
       "slave-meter1-PF": slave_meter1_PF,
       "slave-Status-NotUsed3": slave_Status_NotUsed3,
       "slave-Status-NotUsed4": slave_Status_NotUsed4,
       "slave-Status-NotUsed5": slave_Status_NotUsed5,
       "slave-meter1-Freq": slave_meter1_Freq,
       "slave-meter2-VRMS": slave_meter2_VRMS,
       "slave-meter2-IRMS": slave_meter2_IRMS,
       "slave-meter2-KWH": slave_meter2_KWH,
       "slave-meter2-KW": slave_meter2_KW,
       "slave-meter2-TPMU": slave_meter2_TPMU,
       "slave-meter2-IPK": slave_meter2_IPK,
       "slave-meter2-VPK": slave_meter2_VPK,
       "slave-meter2-PF": slave_meter2_PF,
       "slave-meter2-Freq": slave_meter2_Freq,
       "slave-meter3-VRMS": slave_meter3_VRMS,
       "slave-meter3-IRMS": slave_meter3_IRMS,
       "slave-meter3-KWH": slave_meter3_KWH,
       "slave-meter3-KW": slave_meter3_KW,
       "slave-meter3-TPMU": slave_meter3_TPMU,
       "slave-meter3-IPK": slave_meter3_IPK,
       "slave-meter3-VPK": slave_meter3_VPK,
       "slave-meter3-PF": slave_meter3_PF,
       "slave-meter3-Freq": slave_meter3_Freq,
       "slave-sockets": slave_sockets,
       "slave-socketsTable": slave_socketsTable,
       "slave-socketsEntry": slave_socketsEntry,
       "slave-socket-Index": slave_socket_Index,
       "slave-socket-Number": slave_socket_Number,
       "slave-socket-NotUsed1": slave_socket_NotUsed1,
       "slave-socket-ONOFF": slave_socket_ONOFF,
       "slave-socket-AMPS": slave_socket_AMPS,
       "slave-socket-KWH": slave_socket_KWH,
       "socket-Selected": socket_Selected,
       "socket-AllON": socket_AllON,
       "socket-AllOFF": socket_AllOFF,
       "slave-Environmental": slave_Environmental,
       "slave-environmental-Temp1": slave_environmental_Temp1,
       "slave-environmental-Temp2": slave_environmental_Temp2,
       "slave-environmental-Temp3": slave_environmental_Temp3,
       "slave-environmental-Temp4": slave_environmental_Temp4,
       "slave-environmental-Temp5": slave_environmental_Temp5,
       "slave-environmental-Temp6": slave_environmental_Temp6,
       "slave-environmental-Temp7": slave_environmental_Temp7,
       "slave-environmental-Temp8": slave_environmental_Temp8,
       "slave-environmental-HumidityTemp": slave_environmental_HumidityTemp,
       "slave-environmental-Humidity": slave_environmental_Humidity,
       "slave-environmental-Contact1": slave_environmental_Contact1,
       "slave-environmental-Contact2": slave_environmental_Contact2,
       "slave-environmental-Contact3": slave_environmental_Contact3,
       "slave-Security": slave_Security,
       "slave-Security-Door": slave_Security_Door,
       "slave-Security-Lock": slave_Security_Lock,
       "slave-Traps": slave_Traps,
       "slave-TrapSetNotifications": slave_TrapSetNotifications,
       "slave-Set-meter1-VRMSLow": slave_Set_meter1_VRMSLow,
       "slave-Set-meter1-VRMSHigh": slave_Set_meter1_VRMSHigh,
       "slave-Set-meter1-IRMSLow": slave_Set_meter1_IRMSLow,
       "slave-Set-meter1-IRMSHigh": slave_Set_meter1_IRMSHigh,
       "slave-Set-meter1-KWSLow": slave_Set_meter1_KWSLow,
       "slave-Set-meter1-KWSHigh": slave_Set_meter1_KWSHigh,
       "slave-Set-meter1-TempLow": slave_Set_meter1_TempLow,
       "slave-Set-meter1-TempHigh": slave_Set_meter1_TempHigh,
       "slave-Set-socket-AMPSLow": slave_Set_socket_AMPSLow,
       "slave-Set-socket-AMPSHigh": slave_Set_socket_AMPSHigh,
       "slave-Set-environmental-Temp1Low": slave_Set_environmental_Temp1Low,
       "slave-Set-environmental-Temp1High": slave_Set_environmental_Temp1High,
       "slave-Set-environmental-Temp2Low": slave_Set_environmental_Temp2Low,
       "slave-Set-environmental-Temp2High": slave_Set_environmental_Temp2High,
       "slave-Set-environmental-Temp3Low": slave_Set_environmental_Temp3Low,
       "slave-Set-environmental-Temp3High": slave_Set_environmental_Temp3High,
       "slave-Set-environmental-Temp4Low": slave_Set_environmental_Temp4Low,
       "slave-Set-environmental-Temp4High": slave_Set_environmental_Temp4High,
       "slave-Set-environmental-Temp5Low": slave_Set_environmental_Temp5Low,
       "slave-Set-environmental-Temp5High": slave_Set_environmental_Temp5High,
       "slave-Set-environmental-Temp6Low": slave_Set_environmental_Temp6Low,
       "slave-Set-environmental-Temp6High": slave_Set_environmental_Temp6High,
       "slave-Set-environmental-Temp7Low": slave_Set_environmental_Temp7Low,
       "slave-Set-environmental-Temp7High": slave_Set_environmental_Temp7High,
       "slave-Set-environmental-Temp8Low": slave_Set_environmental_Temp8Low,
       "slave-Set-environmental-Temp8High": slave_Set_environmental_Temp8High,
       "slave-Set-environmental-HumidityTempLow": slave_Set_environmental_HumidityTempLow,
       "slave-Set-environmental-HumidityTempHigh": slave_Set_environmental_HumidityTempHigh,
       "slave-Set-environmental-HumidityLow": slave_Set_environmental_HumidityLow,
       "slave-Set-environmental-HumidityHigh": slave_Set_environmental_HumidityHigh,
       "slave-Set-environmental-Contact1Open": slave_Set_environmental_Contact1Open,
       "slave-Set-environmental-Contact1Closed": slave_Set_environmental_Contact1Closed,
       "slave-Set-environmental-Contact2Open": slave_Set_environmental_Contact2Open,
       "slave-Set-environmental-Contact2Closed": slave_Set_environmental_Contact2Closed,
       "slave-Set-environmental-Contact3Open": slave_Set_environmental_Contact3Open,
       "slave-Set-environmental-Contact3Closed": slave_Set_environmental_Contact3Closed,
       "slave-Set-Security-DoorOpen": slave_Set_Security_DoorOpen,
       "slave-Set-Security-DoorClosed": slave_Set_Security_DoorClosed,
       "slave-Set-Security-LockUnlocked": slave_Set_Security_LockUnlocked,
       "slave-Set-Security-LockLocked": slave_Set_Security_LockLocked,
       "slave-Set-pduOffline": slave_Set_pduOffline,
       "slave-Set-meter1-PFLow": slave_Set_meter1_PFLow,
       "slave-Set-meter1-PFHigh": slave_Set_meter1_PFHigh,
       "slave-Set-meter1-FreqLow": slave_Set_meter1_FreqLow,
       "slave-Set-meter1-FreqHigh": slave_Set_meter1_FreqHigh,
       "slave-Set-meter2-VRMSLow": slave_Set_meter2_VRMSLow,
       "slave-Set-meter2-VRMSHigh": slave_Set_meter2_VRMSHigh,
       "slave-Set-meter2-IRMSLow": slave_Set_meter2_IRMSLow,
       "slave-Set-meter2-IRMSHigh": slave_Set_meter2_IRMSHigh,
       "slave-Set-meter2-KWSLow": slave_Set_meter2_KWSLow,
       "slave-Set-meter2-KWSHigh": slave_Set_meter2_KWSHigh,
       "slave-Set-meter2-TempLow": slave_Set_meter2_TempLow,
       "slave-Set-meter2-TempHigh": slave_Set_meter2_TempHigh,
       "slave-Set-meter2-PFLow": slave_Set_meter2_PFLow,
       "slave-Set-meter2-PFHigh": slave_Set_meter2_PFHigh,
       "slave-Set-meter2-FreqLow": slave_Set_meter2_FreqLow,
       "slave-Set-meter2-FreqHigh": slave_Set_meter2_FreqHigh,
       "slave-Set-meter3-VRMSLow": slave_Set_meter3_VRMSLow,
       "slave-Set-meter3-VRMSHigh": slave_Set_meter3_VRMSHigh,
       "slave-Set-meter3-IRMSLow": slave_Set_meter3_IRMSLow,
       "slave-Set-meter3-IRMSHigh": slave_Set_meter3_IRMSHigh,
       "slave-Set-meter3-KWSLow": slave_Set_meter3_KWSLow,
       "slave-Set-meter3-KWSHigh": slave_Set_meter3_KWSHigh,
       "slave-Set-meter3-TempLow": slave_Set_meter3_TempLow,
       "slave-Set-meter3-TempHigh": slave_Set_meter3_TempHigh,
       "slave-Set-meter3-PFLow": slave_Set_meter3_PFLow,
       "slave-Set-meter3-PFHigh": slave_Set_meter3_PFHigh,
       "slave-Set-meter3-FreqLow": slave_Set_meter3_FreqLow,
       "slave-Set-meter3-FreqHigh": slave_Set_meter3_FreqHigh,
       "slave-TrapClearNotifications": slave_TrapClearNotifications,
       "slave-Clear-meter1-VRMSLow": slave_Clear_meter1_VRMSLow,
       "slave-Clear-meter1-VRMSHigh": slave_Clear_meter1_VRMSHigh,
       "slave-Clear-meter1-IRMSLow": slave_Clear_meter1_IRMSLow,
       "slave-Clear-meter1-IRMSHigh": slave_Clear_meter1_IRMSHigh,
       "slave-Clear-meter1-KWSLow": slave_Clear_meter1_KWSLow,
       "slave-Clear-meter1-KWSHigh": slave_Clear_meter1_KWSHigh,
       "slave-Clear-meter1-TempLow": slave_Clear_meter1_TempLow,
       "slave-Clear-meter1-TempHigh": slave_Clear_meter1_TempHigh,
       "slave-Clear-socket-AMPSLow": slave_Clear_socket_AMPSLow,
       "slave-Clear-socket-AMPSHigh": slave_Clear_socket_AMPSHigh,
       "slave-Clear-environmental-Temp1Low": slave_Clear_environmental_Temp1Low,
       "slave-Clear-environmental-Temp1High": slave_Clear_environmental_Temp1High,
       "slave-Clear-environmental-Temp2Low": slave_Clear_environmental_Temp2Low,
       "slave-Clear-environmental-Temp2High": slave_Clear_environmental_Temp2High,
       "slave-Clear-environmental-Temp3Low": slave_Clear_environmental_Temp3Low,
       "slave-Clear-environmental-Temp3High": slave_Clear_environmental_Temp3High,
       "slave-Clear-environmental-Temp4Low": slave_Clear_environmental_Temp4Low,
       "slave-Clear-environmental-Temp4High": slave_Clear_environmental_Temp4High,
       "slave-Clear-environmental-Temp5Low": slave_Clear_environmental_Temp5Low,
       "slave-Clear-environmental-Temp5High": slave_Clear_environmental_Temp5High,
       "slave-Clear-environmental-Temp6Low": slave_Clear_environmental_Temp6Low,
       "slave-Clear-environmental-Temp6High": slave_Clear_environmental_Temp6High,
       "slave-Clear-environmental-Temp7Low": slave_Clear_environmental_Temp7Low,
       "slave-Clear-environmental-Temp7High": slave_Clear_environmental_Temp7High,
       "slave-Clear-environmental-Temp8Low": slave_Clear_environmental_Temp8Low,
       "slave-Clear-environmental-Temp8High": slave_Clear_environmental_Temp8High,
       "slave-Clear-environmental-HumidityTempLow": slave_Clear_environmental_HumidityTempLow,
       "slave-Clear-environmental-HumidityTempHigh": slave_Clear_environmental_HumidityTempHigh,
       "slave-Clear-environmental-HumidityLow": slave_Clear_environmental_HumidityLow,
       "slave-Clear-environmental-HumidityHigh": slave_Clear_environmental_HumidityHigh,
       "slave-Clear-environmental-Contact1Open": slave_Clear_environmental_Contact1Open,
       "slave-Clear-environmental-Contact1Closed": slave_Clear_environmental_Contact1Closed,
       "slave-Clear-environmental-Contact2Open": slave_Clear_environmental_Contact2Open,
       "slave-Clear-environmental-Contact2Closed": slave_Clear_environmental_Contact2Closed,
       "slave-Clear-environmental-Contact3Open": slave_Clear_environmental_Contact3Open,
       "slave-Clear-environmental-Contact3Closed": slave_Clear_environmental_Contact3Closed,
       "slave-Clear-Security-DoorOpen": slave_Clear_Security_DoorOpen,
       "slave-Clear-Security-DoorClosed": slave_Clear_Security_DoorClosed,
       "slave-Clear-Security-LockUnlocked": slave_Clear_Security_LockUnlocked,
       "slave-Clear-Security-LockLocked": slave_Clear_Security_LockLocked,
       "slave-Clear-pduOffline": slave_Clear_pduOffline,
       "slave-Clear-meter1-PFLow": slave_Clear_meter1_PFLow,
       "slave-Clear-meter1-PFHigh": slave_Clear_meter1_PFHigh,
       "slave-Clear-meter1-FreqLow": slave_Clear_meter1_FreqLow,
       "slave-Clear-meter1-FreqHigh": slave_Clear_meter1_FreqHigh,
       "slave-Clear-meter2-VRMSLow": slave_Clear_meter2_VRMSLow,
       "slave-Clear-meter2-VRMSHigh": slave_Clear_meter2_VRMSHigh,
       "slave-Clear-meter2-IRMSLow": slave_Clear_meter2_IRMSLow,
       "slave-Clear-meter2-IRMSHigh": slave_Clear_meter2_IRMSHigh,
       "slave-Clear-meter2-KWSLow": slave_Clear_meter2_KWSLow,
       "slave-Clear-meter2-KWSHigh": slave_Clear_meter2_KWSHigh,
       "slave-Clear-meter2-TempLow": slave_Clear_meter2_TempLow,
       "slave-Clear-meter2-TempHigh": slave_Clear_meter2_TempHigh,
       "slave-Clear-meter2-PFLow": slave_Clear_meter2_PFLow,
       "slave-Clear-meter2-PFHigh": slave_Clear_meter2_PFHigh,
       "slave-Clear-meter2-FreqLow": slave_Clear_meter2_FreqLow,
       "slave-Clear-meter2-FreqHigh": slave_Clear_meter2_FreqHigh,
       "slave-Clear-meter3-VRMSLow": slave_Clear_meter3_VRMSLow,
       "slave-Clear-meter3-VRMSHigh": slave_Clear_meter3_VRMSHigh,
       "slave-Clear-meter3-IRMSLow": slave_Clear_meter3_IRMSLow,
       "slave-Clear-meter3-IRMSHigh": slave_Clear_meter3_IRMSHigh,
       "slave-Clear-meter3-KWSLow": slave_Clear_meter3_KWSLow,
       "slave-Clear-meter3-KWSHigh": slave_Clear_meter3_KWSHigh,
       "slave-Clear-meter3-TempLow": slave_Clear_meter3_TempLow,
       "slave-Clear-meter3-TempHigh": slave_Clear_meter3_TempHigh,
       "slave-Clear-meter3-PFLow": slave_Clear_meter3_PFLow,
       "slave-Clear-meter3-PFHigh": slave_Clear_meter3_PFHigh,
       "slave-Clear-meter3-FreqLow": slave_Clear_meter3_FreqLow,
       "slave-Clear-meter3-FreqHigh": slave_Clear_meter3_FreqHigh,
       "slave-Global": slave_Global,
       "slave-Global-Table": slave_Global_Table,
       "slave-Global-Entry": slave_Global_Entry,
       "slave-Global-Index": slave_Global_Index,
       "slave-Global-Status": slave_Global_Status,
       "slave-Global-Address": slave_Global_Address,
       "slave-Global-Nosockets": slave_Global_Nosockets,
       "slave-Global-meter1-VRMS": slave_Global_meter1_VRMS,
       "slave-Global-meter1-IRMS": slave_Global_meter1_IRMS,
       "slave-Global-meter1-KWH": slave_Global_meter1_KWH,
       "slave-Global-meter1-KW": slave_Global_meter1_KW,
       "slave-Global-meter1-TPMU": slave_Global_meter1_TPMU,
       "slave-Global-meter1-PF": slave_Global_meter1_PF,
       "slave-Global-environmental-Temp1": slave_Global_environmental_Temp1,
       "slave-Global-environmental-Temp2": slave_Global_environmental_Temp2,
       "slave-Global-environmental-Temp3": slave_Global_environmental_Temp3,
       "slave-Global-environmental-Temp4": slave_Global_environmental_Temp4,
       "slave-Global-environmental-Temp5": slave_Global_environmental_Temp5,
       "slave-Global-environmental-Temp6": slave_Global_environmental_Temp6,
       "slave-Global-environmental-Temp7": slave_Global_environmental_Temp7,
       "slave-Global-environmental-Temp8": slave_Global_environmental_Temp8,
       "slave-Global-environmental-HumidityTemp": slave_Global_environmental_HumidityTemp,
       "slave-Global-environmental-Humidity": slave_Global_environmental_Humidity,
       "slave-Global-environmental-Contact1": slave_Global_environmental_Contact1,
       "slave-Global-environmental-Contact2": slave_Global_environmental_Contact2,
       "slave-Global-environmental-Contact3": slave_Global_environmental_Contact3,
       "slave-Global-Security-Door": slave_Global_Security_Door,
       "slave-Global-Security-Lock": slave_Global_Security_Lock,
       "slave-Global-sockets": slave_Global_sockets,
       "slave-Global-socket1Amps": slave_Global_socket1Amps,
       "slave-Global-socket2Amps": slave_Global_socket2Amps,
       "slave-Global-socket3Amps": slave_Global_socket3Amps,
       "slave-Global-socket4Amps": slave_Global_socket4Amps,
       "slave-Global-socket5Amps": slave_Global_socket5Amps,
       "slave-Global-socket6Amps": slave_Global_socket6Amps,
       "slave-Global-socket7Amps": slave_Global_socket7Amps,
       "slave-Global-socket8Amps": slave_Global_socket8Amps,
       "slave-Global-socket9Amps": slave_Global_socket9Amps,
       "slave-Global-socket10Amps": slave_Global_socket10Amps,
       "slave-Global-socket11Amps": slave_Global_socket11Amps,
       "slave-Global-socket12Amps": slave_Global_socket12Amps,
       "slave-Global-socket13Amps": slave_Global_socket13Amps,
       "slave-Global-socket14Amps": slave_Global_socket14Amps,
       "slave-Global-socket15Amps": slave_Global_socket15Amps,
       "slave-Global-socket16Amps": slave_Global_socket16Amps,
       "slave-Global-socket17Amps": slave_Global_socket17Amps,
       "slave-Global-socket18Amps": slave_Global_socket18Amps,
       "slave-Global-socket19Amps": slave_Global_socket19Amps,
       "slave-Global-socket20Amps": slave_Global_socket20Amps,
       "slave-Global-socket21Amps": slave_Global_socket21Amps,
       "slave-Global-socket22Amps": slave_Global_socket22Amps,
       "slave-Global-socket23Amps": slave_Global_socket23Amps,
       "slave-Global-socket24Amps": slave_Global_socket24Amps,
       "slave-Global-socket25Amps": slave_Global_socket25Amps,
       "slave-Global-socket26Amps": slave_Global_socket26Amps,
       "slave-Global-socket27Amps": slave_Global_socket27Amps,
       "slave-Global-socket28Amps": slave_Global_socket28Amps,
       "slave-Global-socket29Amps": slave_Global_socket29Amps,
       "slave-Global-socket30Amps": slave_Global_socket30Amps,
       "slave-Global-socket31Amps": slave_Global_socket31Amps,
       "slave-Global-socket32Amps": slave_Global_socket32Amps,
       "slave-Global-socket1kWh": slave_Global_socket1kWh,
       "slave-Global-socket2kWh": slave_Global_socket2kWh,
       "slave-Global-socket3kWh": slave_Global_socket3kWh,
       "slave-Global-socket4kWh": slave_Global_socket4kWh,
       "slave-Global-socket5kWh": slave_Global_socket5kWh,
       "slave-Global-socket6kWh": slave_Global_socket6kWh,
       "slave-Global-socket7kWh": slave_Global_socket7kWh,
       "slave-Global-socket8kWh": slave_Global_socket8kWh,
       "slave-Global-socket9kWh": slave_Global_socket9kWh,
       "slave-Global-socket10kWh": slave_Global_socket10kWh,
       "slave-Global-socket11kWh": slave_Global_socket11kWh,
       "slave-Global-socket12kWh": slave_Global_socket12kWh,
       "slave-Global-socket13kWh": slave_Global_socket13kWh,
       "slave-Global-socket14kWh": slave_Global_socket14kWh,
       "slave-Global-socket15kWh": slave_Global_socket15kWh,
       "slave-Global-socket16kWh": slave_Global_socket16kWh,
       "slave-Global-socket17kWh": slave_Global_socket17kWh,
       "slave-Global-socket18kWh": slave_Global_socket18kWh,
       "slave-Global-socket19kWh": slave_Global_socket19kWh,
       "slave-Global-socket20kWh": slave_Global_socket20kWh,
       "slave-Global-socket21kWh": slave_Global_socket21kWh,
       "slave-Global-socket22kWh": slave_Global_socket22kWh,
       "slave-Global-socket23kWh": slave_Global_socket23kWh,
       "slave-Global-socket24kWh": slave_Global_socket24kWh,
       "slave-Global-socket25kWh": slave_Global_socket25kWh,
       "slave-Global-socket26kWh": slave_Global_socket26kWh,
       "slave-Global-socket27kWh": slave_Global_socket27kWh,
       "slave-Global-socket28kWh": slave_Global_socket28kWh,
       "slave-Global-socket29kWh": slave_Global_socket29kWh,
       "slave-Global-socket30kWh": slave_Global_socket30kWh,
       "slave-Global-socket31kWh": slave_Global_socket31kWh,
       "slave-Global-socket32kWh": slave_Global_socket32kWh,
       "slave-Global-socket33Amps": slave_Global_socket33Amps,
       "slave-Global-socket34Amps": slave_Global_socket34Amps,
       "slave-Global-socket35Amps": slave_Global_socket35Amps,
       "slave-Global-socket36Amps": slave_Global_socket36Amps,
       "slave-Global-socket37Amps": slave_Global_socket37Amps,
       "slave-Global-socket38Amps": slave_Global_socket38Amps,
       "slave-Global-socket39Amps": slave_Global_socket39Amps,
       "slave-Global-socket40Amps": slave_Global_socket40Amps,
       "slave-Global-socket41Amps": slave_Global_socket41Amps,
       "slave-Global-socket42Amps": slave_Global_socket42Amps,
       "slave-Global-socket43Amps": slave_Global_socket43Amps,
       "slave-Global-socket44Amps": slave_Global_socket44Amps,
       "slave-Global-socket45Amps": slave_Global_socket45Amps,
       "slave-Global-socket46Amps": slave_Global_socket46Amps,
       "slave-Global-socket47Amps": slave_Global_socket47Amps,
       "slave-Global-socket48Amps": slave_Global_socket48Amps,
       "slave-Global-socket33kWh": slave_Global_socket33kWh,
       "slave-Global-socket34kWh": slave_Global_socket34kWh,
       "slave-Global-socket35kWh": slave_Global_socket35kWh,
       "slave-Global-socket36kWh": slave_Global_socket36kWh,
       "slave-Global-socket37kWh": slave_Global_socket37kWh,
       "slave-Global-socket38kWh": slave_Global_socket38kWh,
       "slave-Global-socket39kWh": slave_Global_socket39kWh,
       "slave-Global-socket40kWh": slave_Global_socket40kWh,
       "slave-Global-socket41kWh": slave_Global_socket41kWh,
       "slave-Global-socket42kWh": slave_Global_socket42kWh,
       "slave-Global-socket43kWh": slave_Global_socket43kWh,
       "slave-Global-socket44kWh": slave_Global_socket44kWh,
       "slave-Global-socket45kWh": slave_Global_socket45kWh,
       "slave-Global-socket46kWh": slave_Global_socket46kWh,
       "slave-Global-socket47kWh": slave_Global_socket47kWh,
       "slave-Global-socket48kWh": slave_Global_socket48kWh,
       "slave-Global-sockets2": slave_Global_sockets2,
       "slave-Global-meter1-Freq": slave_Global_meter1_Freq,
       "slave-Global-meter2-VRMS": slave_Global_meter2_VRMS,
       "slave-Global-meter2-IRMS": slave_Global_meter2_IRMS,
       "slave-Global-meter2-KWH": slave_Global_meter2_KWH,
       "slave-Global-meter2-KW": slave_Global_meter2_KW,
       "slave-Global-meter2-TPMU": slave_Global_meter2_TPMU,
       "slave-Global-meter2-PF": slave_Global_meter2_PF,
       "slave-Global-meter2-Freq": slave_Global_meter2_Freq,
       "slave-Global-meter3-VRMS": slave_Global_meter3_VRMS,
       "slave-Global-meter3-IRMS": slave_Global_meter3_IRMS,
       "slave-Global-meter3-KWH": slave_Global_meter3_KWH,
       "slave-Global-meter3-KW": slave_Global_meter3_KW,
       "slave-Global-meter3-TPMU": slave_Global_meter3_TPMU,
       "slave-Global-meter3-PF": slave_Global_meter3_PF,
       "slave-Global-meter3-Freq": slave_Global_meter3_Freq}
)
