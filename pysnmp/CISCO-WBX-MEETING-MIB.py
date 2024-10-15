# SNMP MIB module (CISCO-WBX-MEETING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WBX-MEETING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:31 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(AutonomousType,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

ciscoWebExMeetingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809)
)
ciscoWebExMeetingMIB.setRevisions(
        ("2013-05-29 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CiscoWebExCommSysResource(Integer32, TextualConvention):
    status = "current"
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
        *(("cpu", 0),
          ("disk", 4),
          ("fileDescriptor", 3),
          ("memory", 1),
          ("swap", 2))
    )



class CiscoWebExCommSysResMonitoringStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoWebExMeetingMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoWebExMeetingMIBNotifs = _CiscoWebExMeetingMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 0)
)
_CiscoWebExMeetingMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWebExMeetingMIBObjects = _CiscoWebExMeetingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1)
)
_CiscoWebExCommInfo_ObjectIdentity = ObjectIdentity
ciscoWebExCommInfo = _CiscoWebExCommInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 1)
)


class _CwCommSystemVersion_Type(SnmpAdminString):
    """Custom type cwCommSystemVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CwCommSystemVersion_Type.__name__ = "SnmpAdminString"
_CwCommSystemVersion_Object = MibScalar
cwCommSystemVersion = _CwCommSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 1, 1),
    _CwCommSystemVersion_Type()
)
cwCommSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommSystemVersion.setStatus("current")
_CwCommSystemObjectID_Type = AutonomousType
_CwCommSystemObjectID_Object = MibScalar
cwCommSystemObjectID = _CwCommSystemObjectID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 1, 2),
    _CwCommSystemObjectID_Type()
)
cwCommSystemObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommSystemObjectID.setStatus("current")
_CiscoWebExCommSystemResource_ObjectIdentity = ObjectIdentity
ciscoWebExCommSystemResource = _CiscoWebExCommSystemResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2)
)
_CwCommCPUUsageObject_ObjectIdentity = ObjectIdentity
cwCommCPUUsageObject = _CwCommCPUUsageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwCommCPUUsageObject.setStatus("current")


class _CwCommCPUTotalUsage_Type(Gauge32):
    """Custom type cwCommCPUTotalUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwCommCPUTotalUsage_Type.__name__ = "Gauge32"
_CwCommCPUTotalUsage_Object = MibScalar
cwCommCPUTotalUsage = _CwCommCPUTotalUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 1),
    _CwCommCPUTotalUsage_Type()
)
cwCommCPUTotalUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUTotalUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUTotalUsage.setUnits("percent")


class _CwCommCPUUsageWindow_Type(Gauge32):
    """Custom type cwCommCPUUsageWindow based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CwCommCPUUsageWindow_Type.__name__ = "Gauge32"
_CwCommCPUUsageWindow_Object = MibScalar
cwCommCPUUsageWindow = _CwCommCPUUsageWindow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 2),
    _CwCommCPUUsageWindow_Type()
)
cwCommCPUUsageWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwCommCPUUsageWindow.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageWindow.setUnits("Minute")


class _CwCommCPUTotalNumber_Type(Gauge32):
    """Custom type cwCommCPUTotalNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_CwCommCPUTotalNumber_Type.__name__ = "Gauge32"
_CwCommCPUTotalNumber_Object = MibScalar
cwCommCPUTotalNumber = _CwCommCPUTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 3),
    _CwCommCPUTotalNumber_Type()
)
cwCommCPUTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUTotalNumber.setStatus("current")
_CwCommCPUUsageTable_Object = MibTable
cwCommCPUUsageTable = _CwCommCPUUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cwCommCPUUsageTable.setStatus("current")
_CwCommCPUUsageEntry_Object = MibTableRow
cwCommCPUUsageEntry = _CwCommCPUUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1)
)
cwCommCPUUsageEntry.setIndexNames(
    (0, "CISCO-WBX-MEETING-MIB", "cwCommCPUIndex"),
)
if mibBuilder.loadTexts:
    cwCommCPUUsageEntry.setStatus("current")


class _CwCommCPUIndex_Type(Unsigned32):
    """Custom type cwCommCPUIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CwCommCPUIndex_Type.__name__ = "Unsigned32"
_CwCommCPUIndex_Object = MibTableColumn
cwCommCPUIndex = _CwCommCPUIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 1),
    _CwCommCPUIndex_Type()
)
cwCommCPUIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwCommCPUIndex.setStatus("current")


class _CwCommCPUName_Type(SnmpAdminString):
    """Custom type cwCommCPUName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CwCommCPUName_Type.__name__ = "SnmpAdminString"
_CwCommCPUName_Object = MibTableColumn
cwCommCPUName = _CwCommCPUName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 2),
    _CwCommCPUName_Type()
)
cwCommCPUName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUName.setStatus("current")


class _CwCommCPUUsage_Type(Gauge32):
    """Custom type cwCommCPUUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwCommCPUUsage_Type.__name__ = "Gauge32"
_CwCommCPUUsage_Object = MibTableColumn
cwCommCPUUsage = _CwCommCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 3),
    _CwCommCPUUsage_Type()
)
cwCommCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsage.setUnits("percent")


class _CwCommCPUUsageUser_Type(Gauge32):
    """Custom type cwCommCPUUsageUser based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageUser_Type.__name__ = "Gauge32"
_CwCommCPUUsageUser_Object = MibTableColumn
cwCommCPUUsageUser = _CwCommCPUUsageUser_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 4),
    _CwCommCPUUsageUser_Type()
)
cwCommCPUUsageUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageUser.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageUser.setUnits("KHz")


class _CwCommCPUUsageNice_Type(Gauge32):
    """Custom type cwCommCPUUsageNice based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageNice_Type.__name__ = "Gauge32"
_CwCommCPUUsageNice_Object = MibTableColumn
cwCommCPUUsageNice = _CwCommCPUUsageNice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 5),
    _CwCommCPUUsageNice_Type()
)
cwCommCPUUsageNice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageNice.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageNice.setUnits("KHz")


class _CwCommCPUUsageSystem_Type(Gauge32):
    """Custom type cwCommCPUUsageSystem based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageSystem_Type.__name__ = "Gauge32"
_CwCommCPUUsageSystem_Object = MibTableColumn
cwCommCPUUsageSystem = _CwCommCPUUsageSystem_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 6),
    _CwCommCPUUsageSystem_Type()
)
cwCommCPUUsageSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageSystem.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageSystem.setUnits("KHz")


class _CwCommCPUUsageIdle_Type(Gauge32):
    """Custom type cwCommCPUUsageIdle based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageIdle_Type.__name__ = "Gauge32"
_CwCommCPUUsageIdle_Object = MibTableColumn
cwCommCPUUsageIdle = _CwCommCPUUsageIdle_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 7),
    _CwCommCPUUsageIdle_Type()
)
cwCommCPUUsageIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageIdle.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageIdle.setUnits("KHz")


class _CwCommCPUUsageIOWait_Type(Gauge32):
    """Custom type cwCommCPUUsageIOWait based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageIOWait_Type.__name__ = "Gauge32"
_CwCommCPUUsageIOWait_Object = MibTableColumn
cwCommCPUUsageIOWait = _CwCommCPUUsageIOWait_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 8),
    _CwCommCPUUsageIOWait_Type()
)
cwCommCPUUsageIOWait.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageIOWait.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageIOWait.setUnits("KHz")


class _CwCommCPUUsageIRQ_Type(Gauge32):
    """Custom type cwCommCPUUsageIRQ based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageIRQ_Type.__name__ = "Gauge32"
_CwCommCPUUsageIRQ_Object = MibTableColumn
cwCommCPUUsageIRQ = _CwCommCPUUsageIRQ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 9),
    _CwCommCPUUsageIRQ_Type()
)
cwCommCPUUsageIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageIRQ.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageIRQ.setUnits("KHz")


class _CwCommCPUUsageSoftIRQ_Type(Gauge32):
    """Custom type cwCommCPUUsageSoftIRQ based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageSoftIRQ_Type.__name__ = "Gauge32"
_CwCommCPUUsageSoftIRQ_Object = MibTableColumn
cwCommCPUUsageSoftIRQ = _CwCommCPUUsageSoftIRQ_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 10),
    _CwCommCPUUsageSoftIRQ_Type()
)
cwCommCPUUsageSoftIRQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageSoftIRQ.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageSoftIRQ.setUnits("KHz")


class _CwCommCPUUsageSteal_Type(Gauge32):
    """Custom type cwCommCPUUsageSteal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageSteal_Type.__name__ = "Gauge32"
_CwCommCPUUsageSteal_Object = MibTableColumn
cwCommCPUUsageSteal = _CwCommCPUUsageSteal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 11),
    _CwCommCPUUsageSteal_Type()
)
cwCommCPUUsageSteal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageSteal.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageSteal.setUnits("KHz")


class _CwCommCPUUsageCapacitySubTotal_Type(Gauge32):
    """Custom type cwCommCPUUsageCapacitySubTotal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUUsageCapacitySubTotal_Type.__name__ = "Gauge32"
_CwCommCPUUsageCapacitySubTotal_Object = MibTableColumn
cwCommCPUUsageCapacitySubTotal = _CwCommCPUUsageCapacitySubTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 4, 1, 12),
    _CwCommCPUUsageCapacitySubTotal_Type()
)
cwCommCPUUsageCapacitySubTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUUsageCapacitySubTotal.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUUsageCapacitySubTotal.setUnits("KHz")
_CwCommCPUMonitoringStatus_Type = CiscoWebExCommSysResMonitoringStatus
_CwCommCPUMonitoringStatus_Object = MibScalar
cwCommCPUMonitoringStatus = _CwCommCPUMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 5),
    _CwCommCPUMonitoringStatus_Type()
)
cwCommCPUMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUMonitoringStatus.setStatus("current")


class _CwCommCPUCapacityTotal_Type(Gauge32):
    """Custom type cwCommCPUCapacityTotal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommCPUCapacityTotal_Type.__name__ = "Gauge32"
_CwCommCPUCapacityTotal_Object = MibScalar
cwCommCPUCapacityTotal = _CwCommCPUCapacityTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 1, 6),
    _CwCommCPUCapacityTotal_Type()
)
cwCommCPUCapacityTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommCPUCapacityTotal.setStatus("current")
if mibBuilder.loadTexts:
    cwCommCPUCapacityTotal.setUnits("KHz")
_CwCommMEMUsageObject_ObjectIdentity = ObjectIdentity
cwCommMEMUsageObject = _CwCommMEMUsageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwCommMEMUsageObject.setStatus("current")


class _CwCommMEMUsage_Type(Gauge32):
    """Custom type cwCommMEMUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwCommMEMUsage_Type.__name__ = "Gauge32"
_CwCommMEMUsage_Object = MibScalar
cwCommMEMUsage = _CwCommMEMUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2, 1),
    _CwCommMEMUsage_Type()
)
cwCommMEMUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommMEMUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwCommMEMUsage.setUnits("percent")
_CwCommMEMMonitoringStatus_Type = CiscoWebExCommSysResMonitoringStatus
_CwCommMEMMonitoringStatus_Object = MibScalar
cwCommMEMMonitoringStatus = _CwCommMEMMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2, 2),
    _CwCommMEMMonitoringStatus_Type()
)
cwCommMEMMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommMEMMonitoringStatus.setStatus("current")
_CwCommMEMTotal_Type = Gauge32
_CwCommMEMTotal_Object = MibScalar
cwCommMEMTotal = _CwCommMEMTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 2, 3),
    _CwCommMEMTotal_Type()
)
cwCommMEMTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommMEMTotal.setStatus("current")
if mibBuilder.loadTexts:
    cwCommMEMTotal.setUnits("MBytes")
_CwCommMEMSwapUsageObject_ObjectIdentity = ObjectIdentity
cwCommMEMSwapUsageObject = _CwCommMEMSwapUsageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cwCommMEMSwapUsageObject.setStatus("current")


class _CwCommMEMSwapUsage_Type(Gauge32):
    """Custom type cwCommMEMSwapUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwCommMEMSwapUsage_Type.__name__ = "Gauge32"
_CwCommMEMSwapUsage_Object = MibScalar
cwCommMEMSwapUsage = _CwCommMEMSwapUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 3, 1),
    _CwCommMEMSwapUsage_Type()
)
cwCommMEMSwapUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommMEMSwapUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwCommMEMSwapUsage.setUnits("percent")
_CwCommMEMSwapMonitoringStatus_Type = CiscoWebExCommSysResMonitoringStatus
_CwCommMEMSwapMonitoringStatus_Object = MibScalar
cwCommMEMSwapMonitoringStatus = _CwCommMEMSwapMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 3, 2),
    _CwCommMEMSwapMonitoringStatus_Type()
)
cwCommMEMSwapMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommMEMSwapMonitoringStatus.setStatus("current")
_CwCommSysResourceNotificationObject_ObjectIdentity = ObjectIdentity
cwCommSysResourceNotificationObject = _CwCommSysResourceNotificationObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cwCommSysResourceNotificationObject.setStatus("current")
_CwCommNotificationHostAddressType_Type = InetAddressType
_CwCommNotificationHostAddressType_Object = MibScalar
cwCommNotificationHostAddressType = _CwCommNotificationHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 1),
    _CwCommNotificationHostAddressType_Type()
)
cwCommNotificationHostAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cwCommNotificationHostAddressType.setStatus("current")
_CwCommNotificationHostAddress_Type = InetAddress
_CwCommNotificationHostAddress_Object = MibScalar
cwCommNotificationHostAddress = _CwCommNotificationHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 2),
    _CwCommNotificationHostAddress_Type()
)
cwCommNotificationHostAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cwCommNotificationHostAddress.setStatus("current")
_CwCommNotificationResName_Type = CiscoWebExCommSysResource
_CwCommNotificationResName_Object = MibScalar
cwCommNotificationResName = _CwCommNotificationResName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 3),
    _CwCommNotificationResName_Type()
)
cwCommNotificationResName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cwCommNotificationResName.setStatus("current")
_CwCommNotificationResValue_Type = Unsigned32
_CwCommNotificationResValue_Object = MibScalar
cwCommNotificationResValue = _CwCommNotificationResValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 4),
    _CwCommNotificationResValue_Type()
)
cwCommNotificationResValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cwCommNotificationResValue.setStatus("current")
_CwCommNotificationSeqNum_Type = Counter32
_CwCommNotificationSeqNum_Object = MibScalar
cwCommNotificationSeqNum = _CwCommNotificationSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 4, 5),
    _CwCommNotificationSeqNum_Type()
)
cwCommNotificationSeqNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cwCommNotificationSeqNum.setStatus("current")
_CwCommDiskUsageObject_ObjectIdentity = ObjectIdentity
cwCommDiskUsageObject = _CwCommDiskUsageObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5)
)
if mibBuilder.loadTexts:
    cwCommDiskUsageObject.setStatus("current")


class _CwCommDiskUsageCount_Type(Gauge32):
    """Custom type cwCommDiskUsageCount based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CwCommDiskUsageCount_Type.__name__ = "Gauge32"
_CwCommDiskUsageCount_Object = MibScalar
cwCommDiskUsageCount = _CwCommDiskUsageCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 1),
    _CwCommDiskUsageCount_Type()
)
cwCommDiskUsageCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommDiskUsageCount.setStatus("current")
_CwCommDiskUsageTable_Object = MibTable
cwCommDiskUsageTable = _CwCommDiskUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    cwCommDiskUsageTable.setStatus("current")
_CwCommDiskUsageEntry_Object = MibTableRow
cwCommDiskUsageEntry = _CwCommDiskUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1)
)
cwCommDiskUsageEntry.setIndexNames(
    (0, "CISCO-WBX-MEETING-MIB", "cwCommDiskUsageIndex"),
)
if mibBuilder.loadTexts:
    cwCommDiskUsageEntry.setStatus("current")


class _CwCommDiskUsageIndex_Type(Unsigned32):
    """Custom type cwCommDiskUsageIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_CwCommDiskUsageIndex_Type.__name__ = "Unsigned32"
_CwCommDiskUsageIndex_Object = MibTableColumn
cwCommDiskUsageIndex = _CwCommDiskUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 1),
    _CwCommDiskUsageIndex_Type()
)
cwCommDiskUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwCommDiskUsageIndex.setStatus("current")


class _CwCommDiskPartitionName_Type(SnmpAdminString):
    """Custom type cwCommDiskPartitionName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CwCommDiskPartitionName_Type.__name__ = "SnmpAdminString"
_CwCommDiskPartitionName_Object = MibTableColumn
cwCommDiskPartitionName = _CwCommDiskPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 2),
    _CwCommDiskPartitionName_Type()
)
cwCommDiskPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommDiskPartitionName.setStatus("current")


class _CwCommDiskUsage_Type(Gauge32):
    """Custom type cwCommDiskUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CwCommDiskUsage_Type.__name__ = "Gauge32"
_CwCommDiskUsage_Object = MibTableColumn
cwCommDiskUsage = _CwCommDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 3),
    _CwCommDiskUsage_Type()
)
cwCommDiskUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommDiskUsage.setStatus("current")
if mibBuilder.loadTexts:
    cwCommDiskUsage.setUnits("percent")


class _CwCommDiskTotal_Type(Gauge32):
    """Custom type cwCommDiskTotal based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CwCommDiskTotal_Type.__name__ = "Gauge32"
_CwCommDiskTotal_Object = MibTableColumn
cwCommDiskTotal = _CwCommDiskTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 2, 1, 4),
    _CwCommDiskTotal_Type()
)
cwCommDiskTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommDiskTotal.setStatus("current")
if mibBuilder.loadTexts:
    cwCommDiskTotal.setUnits("KB")
_CwCommDiskMonitoringStatus_Type = CiscoWebExCommSysResMonitoringStatus
_CwCommDiskMonitoringStatus_Object = MibScalar
cwCommDiskMonitoringStatus = _CwCommDiskMonitoringStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 1, 2, 5, 3),
    _CwCommDiskMonitoringStatus_Type()
)
cwCommDiskMonitoringStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwCommDiskMonitoringStatus.setStatus("current")
_CiscoWebExMeetingMIBConform_ObjectIdentity = ObjectIdentity
ciscoWebExMeetingMIBConform = _CiscoWebExMeetingMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2)
)
_CwCommMIBCompliances_ObjectIdentity = ObjectIdentity
cwCommMIBCompliances = _CwCommMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 1)
)
_CwCommMIBGroups_ObjectIdentity = ObjectIdentity
cwCommMIBGroups = _CwCommMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2)
)

# Managed Objects groups

ciscoWebExCommInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2, 1)
)
ciscoWebExCommInfoGroup.setObjects(
      *(("CISCO-WBX-MEETING-MIB", "cwCommSystemVersion"),
        ("CISCO-WBX-MEETING-MIB", "cwCommSystemObjectID"))
)
if mibBuilder.loadTexts:
    ciscoWebExCommInfoGroup.setStatus("current")

ciscoWebExCommSystemResourceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2, 2)
)
ciscoWebExCommSystemResourceGroup.setObjects(
      *(("CISCO-WBX-MEETING-MIB", "cwCommCPUTotalUsage"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageWindow"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUTotalNumber"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUName"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsage"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUMonitoringStatus"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageUser"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageNice"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageSystem"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageIdle"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageIOWait"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageIRQ"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageSoftIRQ"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageSteal"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUUsageCapacitySubTotal"),
        ("CISCO-WBX-MEETING-MIB", "cwCommCPUCapacityTotal"),
        ("CISCO-WBX-MEETING-MIB", "cwCommMEMUsage"),
        ("CISCO-WBX-MEETING-MIB", "cwCommMEMMonitoringStatus"),
        ("CISCO-WBX-MEETING-MIB", "cwCommMEMSwapUsage"),
        ("CISCO-WBX-MEETING-MIB", "cwCommMEMSwapMonitoringStatus"),
        ("CISCO-WBX-MEETING-MIB", "cwCommMEMTotal"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"),
        ("CISCO-WBX-MEETING-MIB", "cwCommDiskUsageCount"),
        ("CISCO-WBX-MEETING-MIB", "cwCommDiskPartitionName"),
        ("CISCO-WBX-MEETING-MIB", "cwCommDiskUsage"),
        ("CISCO-WBX-MEETING-MIB", "cwCommDiskTotal"),
        ("CISCO-WBX-MEETING-MIB", "cwCommDiskMonitoringStatus"))
)
if mibBuilder.loadTexts:
    ciscoWebExCommSystemResourceGroup.setStatus("current")


# Notification objects

cwCommSystemResourceUsageNormalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 0, 1)
)
cwCommSystemResourceUsageNormalEvent.setObjects(
      *(("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"))
)
if mibBuilder.loadTexts:
    cwCommSystemResourceUsageNormalEvent.setStatus(
        "current"
    )

cwCommSystemResourceUsageMinorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 0, 2)
)
cwCommSystemResourceUsageMinorEvent.setObjects(
      *(("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"))
)
if mibBuilder.loadTexts:
    cwCommSystemResourceUsageMinorEvent.setStatus(
        "current"
    )

cwCommSystemResourceUsageMajorEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 0, 3)
)
cwCommSystemResourceUsageMajorEvent.setObjects(
      *(("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddressType"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationHostAddress"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResName"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationResValue"),
        ("CISCO-WBX-MEETING-MIB", "cwCommNotificationSeqNum"))
)
if mibBuilder.loadTexts:
    cwCommSystemResourceUsageMajorEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoWebExMeetingMIBNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 2, 3)
)
ciscoWebExMeetingMIBNotifsGroup.setObjects(
      *(("CISCO-WBX-MEETING-MIB", "cwCommSystemResourceUsageNormalEvent"),
        ("CISCO-WBX-MEETING-MIB", "cwCommSystemResourceUsageMinorEvent"),
        ("CISCO-WBX-MEETING-MIB", "cwCommSystemResourceUsageMajorEvent"))
)
if mibBuilder.loadTexts:
    ciscoWebExMeetingMIBNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cwCommMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 809, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwCommMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WBX-MEETING-MIB",
    **{"CiscoWebExCommSysResource": CiscoWebExCommSysResource,
       "CiscoWebExCommSysResMonitoringStatus": CiscoWebExCommSysResMonitoringStatus,
       "ciscoWebExMeetingMIB": ciscoWebExMeetingMIB,
       "ciscoWebExMeetingMIBNotifs": ciscoWebExMeetingMIBNotifs,
       "cwCommSystemResourceUsageNormalEvent": cwCommSystemResourceUsageNormalEvent,
       "cwCommSystemResourceUsageMinorEvent": cwCommSystemResourceUsageMinorEvent,
       "cwCommSystemResourceUsageMajorEvent": cwCommSystemResourceUsageMajorEvent,
       "ciscoWebExMeetingMIBObjects": ciscoWebExMeetingMIBObjects,
       "ciscoWebExCommInfo": ciscoWebExCommInfo,
       "cwCommSystemVersion": cwCommSystemVersion,
       "cwCommSystemObjectID": cwCommSystemObjectID,
       "ciscoWebExCommSystemResource": ciscoWebExCommSystemResource,
       "cwCommCPUUsageObject": cwCommCPUUsageObject,
       "cwCommCPUTotalUsage": cwCommCPUTotalUsage,
       "cwCommCPUUsageWindow": cwCommCPUUsageWindow,
       "cwCommCPUTotalNumber": cwCommCPUTotalNumber,
       "cwCommCPUUsageTable": cwCommCPUUsageTable,
       "cwCommCPUUsageEntry": cwCommCPUUsageEntry,
       "cwCommCPUIndex": cwCommCPUIndex,
       "cwCommCPUName": cwCommCPUName,
       "cwCommCPUUsage": cwCommCPUUsage,
       "cwCommCPUUsageUser": cwCommCPUUsageUser,
       "cwCommCPUUsageNice": cwCommCPUUsageNice,
       "cwCommCPUUsageSystem": cwCommCPUUsageSystem,
       "cwCommCPUUsageIdle": cwCommCPUUsageIdle,
       "cwCommCPUUsageIOWait": cwCommCPUUsageIOWait,
       "cwCommCPUUsageIRQ": cwCommCPUUsageIRQ,
       "cwCommCPUUsageSoftIRQ": cwCommCPUUsageSoftIRQ,
       "cwCommCPUUsageSteal": cwCommCPUUsageSteal,
       "cwCommCPUUsageCapacitySubTotal": cwCommCPUUsageCapacitySubTotal,
       "cwCommCPUMonitoringStatus": cwCommCPUMonitoringStatus,
       "cwCommCPUCapacityTotal": cwCommCPUCapacityTotal,
       "cwCommMEMUsageObject": cwCommMEMUsageObject,
       "cwCommMEMUsage": cwCommMEMUsage,
       "cwCommMEMMonitoringStatus": cwCommMEMMonitoringStatus,
       "cwCommMEMTotal": cwCommMEMTotal,
       "cwCommMEMSwapUsageObject": cwCommMEMSwapUsageObject,
       "cwCommMEMSwapUsage": cwCommMEMSwapUsage,
       "cwCommMEMSwapMonitoringStatus": cwCommMEMSwapMonitoringStatus,
       "cwCommSysResourceNotificationObject": cwCommSysResourceNotificationObject,
       "cwCommNotificationHostAddressType": cwCommNotificationHostAddressType,
       "cwCommNotificationHostAddress": cwCommNotificationHostAddress,
       "cwCommNotificationResName": cwCommNotificationResName,
       "cwCommNotificationResValue": cwCommNotificationResValue,
       "cwCommNotificationSeqNum": cwCommNotificationSeqNum,
       "cwCommDiskUsageObject": cwCommDiskUsageObject,
       "cwCommDiskUsageCount": cwCommDiskUsageCount,
       "cwCommDiskUsageTable": cwCommDiskUsageTable,
       "cwCommDiskUsageEntry": cwCommDiskUsageEntry,
       "cwCommDiskUsageIndex": cwCommDiskUsageIndex,
       "cwCommDiskPartitionName": cwCommDiskPartitionName,
       "cwCommDiskUsage": cwCommDiskUsage,
       "cwCommDiskTotal": cwCommDiskTotal,
       "cwCommDiskMonitoringStatus": cwCommDiskMonitoringStatus,
       "ciscoWebExMeetingMIBConform": ciscoWebExMeetingMIBConform,
       "cwCommMIBCompliances": cwCommMIBCompliances,
       "cwCommMIBCompliance": cwCommMIBCompliance,
       "cwCommMIBGroups": cwCommMIBGroups,
       "ciscoWebExCommInfoGroup": ciscoWebExCommInfoGroup,
       "ciscoWebExCommSystemResourceGroup": ciscoWebExCommSystemResourceGroup,
       "ciscoWebExMeetingMIBNotifsGroup": ciscoWebExMeetingMIBNotifsGroup}
)
