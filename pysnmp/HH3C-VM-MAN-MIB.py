# SNMP MIB module (HH3C-VM-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-VM-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:55:14 2024
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

(entPhysicalAssetID,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalAssetID")

(hh3cSurveillanceMIB,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cSurveillanceMIB")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hh3cVMMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cVMManMIBObjects_ObjectIdentity = ObjectIdentity
hh3cVMManMIBObjects = _Hh3cVMManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1)
)


class _Hh3cVMCapabilitySet_Type(Bits):
    """Custom type hh3cVMCapabilitySet based on Bits"""
    namedValues = NamedValues(
        *(("cms", 0),
          ("css", 1),
          ("dm", 2))
    )

_Hh3cVMCapabilitySet_Type.__name__ = "Bits"
_Hh3cVMCapabilitySet_Object = MibScalar
hh3cVMCapabilitySet = _Hh3cVMCapabilitySet_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 1),
    _Hh3cVMCapabilitySet_Type()
)
hh3cVMCapabilitySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMCapabilitySet.setStatus("current")
_Hh3cVMStat_ObjectIdentity = ObjectIdentity
hh3cVMStat = _Hh3cVMStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2)
)
_Hh3cVMStatTotalConnEstablishRequests_Type = Counter32
_Hh3cVMStatTotalConnEstablishRequests_Object = MibScalar
hh3cVMStatTotalConnEstablishRequests = _Hh3cVMStatTotalConnEstablishRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 1),
    _Hh3cVMStatTotalConnEstablishRequests_Type()
)
hh3cVMStatTotalConnEstablishRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatTotalConnEstablishRequests.setStatus("current")
_Hh3cVMStatSuccConnEstablishRequests_Type = Counter32
_Hh3cVMStatSuccConnEstablishRequests_Object = MibScalar
hh3cVMStatSuccConnEstablishRequests = _Hh3cVMStatSuccConnEstablishRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 2),
    _Hh3cVMStatSuccConnEstablishRequests_Type()
)
hh3cVMStatSuccConnEstablishRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatSuccConnEstablishRequests.setStatus("current")
_Hh3cVMStatFailConnEstablishRequests_Type = Counter32
_Hh3cVMStatFailConnEstablishRequests_Object = MibScalar
hh3cVMStatFailConnEstablishRequests = _Hh3cVMStatFailConnEstablishRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 3),
    _Hh3cVMStatFailConnEstablishRequests_Type()
)
hh3cVMStatFailConnEstablishRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatFailConnEstablishRequests.setStatus("current")
_Hh3cVMStatTotalConnReleaseRequests_Type = Counter32
_Hh3cVMStatTotalConnReleaseRequests_Object = MibScalar
hh3cVMStatTotalConnReleaseRequests = _Hh3cVMStatTotalConnReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 4),
    _Hh3cVMStatTotalConnReleaseRequests_Type()
)
hh3cVMStatTotalConnReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatTotalConnReleaseRequests.setStatus("current")
_Hh3cVMStatSuccConnReleaseRequests_Type = Counter32
_Hh3cVMStatSuccConnReleaseRequests_Object = MibScalar
hh3cVMStatSuccConnReleaseRequests = _Hh3cVMStatSuccConnReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 5),
    _Hh3cVMStatSuccConnReleaseRequests_Type()
)
hh3cVMStatSuccConnReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatSuccConnReleaseRequests.setStatus("current")
_Hh3cVMStatFailConnReleaseRequests_Type = Counter32
_Hh3cVMStatFailConnReleaseRequests_Object = MibScalar
hh3cVMStatFailConnReleaseRequests = _Hh3cVMStatFailConnReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 6),
    _Hh3cVMStatFailConnReleaseRequests_Type()
)
hh3cVMStatFailConnReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatFailConnReleaseRequests.setStatus("current")
_Hh3cVMStatExceptionTerminationConn_Type = Counter32
_Hh3cVMStatExceptionTerminationConn_Object = MibScalar
hh3cVMStatExceptionTerminationConn = _Hh3cVMStatExceptionTerminationConn_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 1, 2, 7),
    _Hh3cVMStatExceptionTerminationConn_Type()
)
hh3cVMStatExceptionTerminationConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cVMStatExceptionTerminationConn.setStatus("current")
_Hh3cVMManMIBTrap_ObjectIdentity = ObjectIdentity
hh3cVMManMIBTrap = _Hh3cVMManMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2)
)
_Hh3cVMManTrapPrex_ObjectIdentity = ObjectIdentity
hh3cVMManTrapPrex = _Hh3cVMManTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0)
)
_Hh3cVMManTrapObjects_ObjectIdentity = ObjectIdentity
hh3cVMManTrapObjects = _Hh3cVMManTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1)
)
_Hh3cVMManIPSANDevIP_Type = IpAddress
_Hh3cVMManIPSANDevIP_Object = MibScalar
hh3cVMManIPSANDevIP = _Hh3cVMManIPSANDevIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 1),
    _Hh3cVMManIPSANDevIP_Type()
)
hh3cVMManIPSANDevIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManIPSANDevIP.setStatus("current")
_Hh3cVMManRegDevIP_Type = IpAddress
_Hh3cVMManRegDevIP_Object = MibScalar
hh3cVMManRegDevIP = _Hh3cVMManRegDevIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 2),
    _Hh3cVMManRegDevIP_Type()
)
hh3cVMManRegDevIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManRegDevIP.setStatus("current")


class _Hh3cVMManRegDevName_Type(DisplayString):
    """Custom type hh3cVMManRegDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_Hh3cVMManRegDevName_Type.__name__ = "DisplayString"
_Hh3cVMManRegDevName_Object = MibScalar
hh3cVMManRegDevName = _Hh3cVMManRegDevName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 3),
    _Hh3cVMManRegDevName_Type()
)
hh3cVMManRegDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManRegDevName.setStatus("current")
_Hh3cVMManRegionCoordinateX1_Type = Unsigned32
_Hh3cVMManRegionCoordinateX1_Object = MibScalar
hh3cVMManRegionCoordinateX1 = _Hh3cVMManRegionCoordinateX1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 4),
    _Hh3cVMManRegionCoordinateX1_Type()
)
hh3cVMManRegionCoordinateX1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManRegionCoordinateX1.setStatus("current")
_Hh3cVMManRegionCoordinateY1_Type = Unsigned32
_Hh3cVMManRegionCoordinateY1_Object = MibScalar
hh3cVMManRegionCoordinateY1 = _Hh3cVMManRegionCoordinateY1_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 5),
    _Hh3cVMManRegionCoordinateY1_Type()
)
hh3cVMManRegionCoordinateY1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManRegionCoordinateY1.setStatus("current")
_Hh3cVMManRegionCoordinateX2_Type = Unsigned32
_Hh3cVMManRegionCoordinateX2_Object = MibScalar
hh3cVMManRegionCoordinateX2 = _Hh3cVMManRegionCoordinateX2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 6),
    _Hh3cVMManRegionCoordinateX2_Type()
)
hh3cVMManRegionCoordinateX2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManRegionCoordinateX2.setStatus("current")
_Hh3cVMManRegionCoordinateY2_Type = Unsigned32
_Hh3cVMManRegionCoordinateY2_Object = MibScalar
hh3cVMManRegionCoordinateY2 = _Hh3cVMManRegionCoordinateY2_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 7),
    _Hh3cVMManRegionCoordinateY2_Type()
)
hh3cVMManRegionCoordinateY2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManRegionCoordinateY2.setStatus("current")


class _Hh3cVMManCpuUsage_Type(Unsigned32):
    """Custom type hh3cVMManCpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVMManCpuUsage_Type.__name__ = "Unsigned32"
_Hh3cVMManCpuUsage_Object = MibScalar
hh3cVMManCpuUsage = _Hh3cVMManCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 8),
    _Hh3cVMManCpuUsage_Type()
)
hh3cVMManCpuUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManCpuUsage.setStatus("current")


class _Hh3cVMManCpuUsageThreshold_Type(Unsigned32):
    """Custom type hh3cVMManCpuUsageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVMManCpuUsageThreshold_Type.__name__ = "Unsigned32"
_Hh3cVMManCpuUsageThreshold_Object = MibScalar
hh3cVMManCpuUsageThreshold = _Hh3cVMManCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 9),
    _Hh3cVMManCpuUsageThreshold_Type()
)
hh3cVMManCpuUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManCpuUsageThreshold.setStatus("current")


class _Hh3cVMManMemUsage_Type(Unsigned32):
    """Custom type hh3cVMManMemUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVMManMemUsage_Type.__name__ = "Unsigned32"
_Hh3cVMManMemUsage_Object = MibScalar
hh3cVMManMemUsage = _Hh3cVMManMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 10),
    _Hh3cVMManMemUsage_Type()
)
hh3cVMManMemUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManMemUsage.setStatus("current")


class _Hh3cVMManMemUsageThreshold_Type(Unsigned32):
    """Custom type hh3cVMManMemUsageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVMManMemUsageThreshold_Type.__name__ = "Unsigned32"
_Hh3cVMManMemUsageThreshold_Object = MibScalar
hh3cVMManMemUsageThreshold = _Hh3cVMManMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 11),
    _Hh3cVMManMemUsageThreshold_Type()
)
hh3cVMManMemUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManMemUsageThreshold.setStatus("current")


class _Hh3cVMManHardDiskUsage_Type(Unsigned32):
    """Custom type hh3cVMManHardDiskUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVMManHardDiskUsage_Type.__name__ = "Unsigned32"
_Hh3cVMManHardDiskUsage_Object = MibScalar
hh3cVMManHardDiskUsage = _Hh3cVMManHardDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 12),
    _Hh3cVMManHardDiskUsage_Type()
)
hh3cVMManHardDiskUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManHardDiskUsage.setStatus("current")


class _Hh3cVMManHardDiskUsageThreshold_Type(Unsigned32):
    """Custom type hh3cVMManHardDiskUsageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Hh3cVMManHardDiskUsageThreshold_Type.__name__ = "Unsigned32"
_Hh3cVMManHardDiskUsageThreshold_Object = MibScalar
hh3cVMManHardDiskUsageThreshold = _Hh3cVMManHardDiskUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 13),
    _Hh3cVMManHardDiskUsageThreshold_Type()
)
hh3cVMManHardDiskUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManHardDiskUsageThreshold.setStatus("current")
_Hh3cVMManTemperature_Type = Integer32
_Hh3cVMManTemperature_Object = MibScalar
hh3cVMManTemperature = _Hh3cVMManTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 14),
    _Hh3cVMManTemperature_Type()
)
hh3cVMManTemperature.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManTemperature.setStatus("current")
_Hh3cVMManTemperatureThreshold_Type = Integer32
_Hh3cVMManTemperatureThreshold_Object = MibScalar
hh3cVMManTemperatureThreshold = _Hh3cVMManTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 15),
    _Hh3cVMManTemperatureThreshold_Type()
)
hh3cVMManTemperatureThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManTemperatureThreshold.setStatus("current")
_Hh3cVMManClientIP_Type = IpAddress
_Hh3cVMManClientIP_Object = MibScalar
hh3cVMManClientIP = _Hh3cVMManClientIP_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 16),
    _Hh3cVMManClientIP_Type()
)
hh3cVMManClientIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientIP.setStatus("current")


class _Hh3cVMManUserName_Type(DisplayString):
    """Custom type hh3cVMManUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cVMManUserName_Type.__name__ = "DisplayString"
_Hh3cVMManUserName_Object = MibScalar
hh3cVMManUserName = _Hh3cVMManUserName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 17),
    _Hh3cVMManUserName_Type()
)
hh3cVMManUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManUserName.setStatus("current")


class _Hh3cVMManReportContent_Type(DisplayString):
    """Custom type hh3cVMManReportContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_Hh3cVMManReportContent_Type.__name__ = "DisplayString"
_Hh3cVMManReportContent_Object = MibScalar
hh3cVMManReportContent = _Hh3cVMManReportContent_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 18),
    _Hh3cVMManReportContent_Type()
)
hh3cVMManReportContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManReportContent.setStatus("current")
_Hh3cVMManClientVideoStreamDiscontinuityInterval_Type = Unsigned32
_Hh3cVMManClientVideoStreamDiscontinuityInterval_Object = MibScalar
hh3cVMManClientVideoStreamDiscontinuityInterval = _Hh3cVMManClientVideoStreamDiscontinuityInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 19),
    _Hh3cVMManClientVideoStreamDiscontinuityInterval_Type()
)
hh3cVMManClientVideoStreamDiscontinuityInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientVideoStreamDiscontinuityInterval.setStatus("current")
_Hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Type = Unsigned32
_Hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Object = MibScalar
hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold = _Hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 20),
    _Hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Type()
)
hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setStatus("current")
_Hh3cVMManClientStatPeriod_Type = Unsigned32
_Hh3cVMManClientStatPeriod_Object = MibScalar
hh3cVMManClientStatPeriod = _Hh3cVMManClientStatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 21),
    _Hh3cVMManClientStatPeriod_Type()
)
hh3cVMManClientStatPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientStatPeriod.setStatus("current")
_Hh3cVMManClientLoginFailNum_Type = Unsigned32
_Hh3cVMManClientLoginFailNum_Object = MibScalar
hh3cVMManClientLoginFailNum = _Hh3cVMManClientLoginFailNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 22),
    _Hh3cVMManClientLoginFailNum_Type()
)
hh3cVMManClientLoginFailNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientLoginFailNum.setStatus("current")
_Hh3cVMManClientLoginFailNumThreshold_Type = Unsigned32
_Hh3cVMManClientLoginFailNumThreshold_Object = MibScalar
hh3cVMManClientLoginFailNumThreshold = _Hh3cVMManClientLoginFailNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 23),
    _Hh3cVMManClientLoginFailNumThreshold_Type()
)
hh3cVMManClientLoginFailNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientLoginFailNumThreshold.setStatus("current")
_Hh3cVMManClientVODFailNum_Type = Unsigned32
_Hh3cVMManClientVODFailNum_Object = MibScalar
hh3cVMManClientVODFailNum = _Hh3cVMManClientVODFailNum_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 24),
    _Hh3cVMManClientVODFailNum_Type()
)
hh3cVMManClientVODFailNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientVODFailNum.setStatus("current")
_Hh3cVMManClientVODFailNumThreshold_Type = Unsigned32
_Hh3cVMManClientVODFailNumThreshold_Object = MibScalar
hh3cVMManClientVODFailNumThreshold = _Hh3cVMManClientVODFailNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 25),
    _Hh3cVMManClientVODFailNumThreshold_Type()
)
hh3cVMManClientVODFailNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientVODFailNumThreshold.setStatus("current")
_Hh3cVMManClientVODStart_Type = DateAndTime
_Hh3cVMManClientVODStart_Object = MibScalar
hh3cVMManClientVODStart = _Hh3cVMManClientVODStart_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 26),
    _Hh3cVMManClientVODStart_Type()
)
hh3cVMManClientVODStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientVODStart.setStatus("current")
_Hh3cVMManClientVODEnd_Type = DateAndTime
_Hh3cVMManClientVODEnd_Object = MibScalar
hh3cVMManClientVODEnd = _Hh3cVMManClientVODEnd_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 27),
    _Hh3cVMManClientVODEnd_Type()
)
hh3cVMManClientVODEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManClientVODEnd.setStatus("current")
_Hh3cVMManPUExternalInputAlarmChannelID_Type = Unsigned32
_Hh3cVMManPUExternalInputAlarmChannelID_Object = MibScalar
hh3cVMManPUExternalInputAlarmChannelID = _Hh3cVMManPUExternalInputAlarmChannelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 28),
    _Hh3cVMManPUExternalInputAlarmChannelID_Type()
)
hh3cVMManPUExternalInputAlarmChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManPUExternalInputAlarmChannelID.setStatus("current")


class _Hh3cVMManPUECVideoChannelName_Type(DisplayString):
    """Custom type hh3cVMManPUECVideoChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Hh3cVMManPUECVideoChannelName_Type.__name__ = "DisplayString"
_Hh3cVMManPUECVideoChannelName_Object = MibScalar
hh3cVMManPUECVideoChannelName = _Hh3cVMManPUECVideoChannelName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 1, 29),
    _Hh3cVMManPUECVideoChannelName_Type()
)
hh3cVMManPUECVideoChannelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hh3cVMManPUECVideoChannelName.setStatus("current")

# Managed Objects groups


# Notification objects

hh3cVMManDeviceOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 1)
)
hh3cVMManDeviceOnlineTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"))
)
if mibBuilder.loadTexts:
    hh3cVMManDeviceOnlineTrap.setStatus(
        "current"
    )

hh3cVMManDeviceOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 2)
)
hh3cVMManDeviceOfflineTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"))
)
if mibBuilder.loadTexts:
    hh3cVMManDeviceOfflineTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceExternalSemaphoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 3)
)
hh3cVMManForwardDeviceExternalSemaphoreTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUExternalInputAlarmChannelID"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceExternalSemaphoreTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceVideoLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 4)
)
hh3cVMManForwardDeviceVideoLossTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceVideoLossTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceVideoRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 5)
)
hh3cVMManForwardDeviceVideoRecoverTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceVideoRecoverTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceMotionDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 6)
)
hh3cVMManForwardDeviceMotionDetectTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX1"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY1"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX2"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceMotionDetectTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceCoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 7)
)
hh3cVMManForwardDeviceCoverTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX1"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY1"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateX2"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceCoverTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceCpuUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 8)
)
hh3cVMManForwardDeviceCpuUsageThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManCpuUsage"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManCpuUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceCpuUsageThresholdTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceMemUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 9)
)
hh3cVMManForwardDeviceMemUsageThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManMemUsage"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceMemUsageThresholdTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceHardDiskUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 10)
)
hh3cVMManForwardDeviceHardDiskUsageThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManHardDiskUsage"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManHardDiskUsageThreshold"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceHardDiskUsageThresholdTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceTemperatureThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 11)
)
hh3cVMManForwardDeviceTemperatureThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManTemperature"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceTemperatureThresholdTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceStartKinescopeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 12)
)
hh3cVMManForwardDeviceStartKinescopeTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceStartKinescopeTrap.setStatus(
        "current"
    )

hh3cVMManForwardDeviceStopKinescopeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 13)
)
hh3cVMManForwardDeviceStopKinescopeTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManForwardDeviceStopKinescopeTrap.setStatus(
        "current"
    )

hh3cVMManClientReportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 14)
)
hh3cVMManClientReportTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManReportContent"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientReportTrap.setStatus(
        "current"
    )

hh3cVMManClientRealtimeSurveillanceNoVideoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 15)
)
hh3cVMManClientRealtimeSurveillanceNoVideoTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientRealtimeSurveillanceNoVideoTrap.setStatus(
        "current"
    )

hh3cVMManClientVODNoVideoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 16)
)
hh3cVMManClientVODNoVideoTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODStart"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODEnd"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManIPSANDevIP"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientVODNoVideoTrap.setStatus(
        "current"
    )

hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 17)
)
hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityInterval"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setStatus(
        "current"
    )

hh3cVMManClientVODVideoStreamDiscontinuityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 18)
)
hh3cVMManClientVODVideoStreamDiscontinuityTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODStart"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODEnd"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManIPSANDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityInterval"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientVODVideoStreamDiscontinuityTrap.setStatus(
        "current"
    )

hh3cVMManClientCtlConnExceptionTerminationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 19)
)
hh3cVMManClientCtlConnExceptionTerminationTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientCtlConnExceptionTerminationTrap.setStatus(
        "current"
    )

hh3cVMManClientFrequencyLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 20)
)
hh3cVMManClientFrequencyLoginFailTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientLoginFailNum"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientLoginFailNumThreshold"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientFrequencyLoginFailTrap.setStatus(
        "current"
    )

hh3cVMManClientFrequencyVODFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 21)
)
hh3cVMManClientFrequencyVODFailTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManUserName"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODFailNum"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientVODFailNumThreshold"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    hh3cVMManClientFrequencyVODFailTrap.setStatus(
        "current"
    )

hh3cVMManDMECDisobeyStorageScheduleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 22)
)
hh3cVMManDMECDisobeyStorageScheduleTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManDMECDisobeyStorageScheduleTrap.setStatus(
        "current"
    )

hh3cVMManDMECDisobeyStorageScheduleRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 9, 1, 2, 0, 23)
)
hh3cVMManDMECDisobeyStorageScheduleRecoverTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManRegDevIP"),
        ("HH3C-VM-MAN-MIB", "hh3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    hh3cVMManDMECDisobeyStorageScheduleRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-VM-MAN-MIB",
    **{"hh3cVMMan": hh3cVMMan,
       "hh3cVMManMIBObjects": hh3cVMManMIBObjects,
       "hh3cVMCapabilitySet": hh3cVMCapabilitySet,
       "hh3cVMStat": hh3cVMStat,
       "hh3cVMStatTotalConnEstablishRequests": hh3cVMStatTotalConnEstablishRequests,
       "hh3cVMStatSuccConnEstablishRequests": hh3cVMStatSuccConnEstablishRequests,
       "hh3cVMStatFailConnEstablishRequests": hh3cVMStatFailConnEstablishRequests,
       "hh3cVMStatTotalConnReleaseRequests": hh3cVMStatTotalConnReleaseRequests,
       "hh3cVMStatSuccConnReleaseRequests": hh3cVMStatSuccConnReleaseRequests,
       "hh3cVMStatFailConnReleaseRequests": hh3cVMStatFailConnReleaseRequests,
       "hh3cVMStatExceptionTerminationConn": hh3cVMStatExceptionTerminationConn,
       "hh3cVMManMIBTrap": hh3cVMManMIBTrap,
       "hh3cVMManTrapPrex": hh3cVMManTrapPrex,
       "hh3cVMManDeviceOnlineTrap": hh3cVMManDeviceOnlineTrap,
       "hh3cVMManDeviceOfflineTrap": hh3cVMManDeviceOfflineTrap,
       "hh3cVMManForwardDeviceExternalSemaphoreTrap": hh3cVMManForwardDeviceExternalSemaphoreTrap,
       "hh3cVMManForwardDeviceVideoLossTrap": hh3cVMManForwardDeviceVideoLossTrap,
       "hh3cVMManForwardDeviceVideoRecoverTrap": hh3cVMManForwardDeviceVideoRecoverTrap,
       "hh3cVMManForwardDeviceMotionDetectTrap": hh3cVMManForwardDeviceMotionDetectTrap,
       "hh3cVMManForwardDeviceCoverTrap": hh3cVMManForwardDeviceCoverTrap,
       "hh3cVMManForwardDeviceCpuUsageThresholdTrap": hh3cVMManForwardDeviceCpuUsageThresholdTrap,
       "hh3cVMManForwardDeviceMemUsageThresholdTrap": hh3cVMManForwardDeviceMemUsageThresholdTrap,
       "hh3cVMManForwardDeviceHardDiskUsageThresholdTrap": hh3cVMManForwardDeviceHardDiskUsageThresholdTrap,
       "hh3cVMManForwardDeviceTemperatureThresholdTrap": hh3cVMManForwardDeviceTemperatureThresholdTrap,
       "hh3cVMManForwardDeviceStartKinescopeTrap": hh3cVMManForwardDeviceStartKinescopeTrap,
       "hh3cVMManForwardDeviceStopKinescopeTrap": hh3cVMManForwardDeviceStopKinescopeTrap,
       "hh3cVMManClientReportTrap": hh3cVMManClientReportTrap,
       "hh3cVMManClientRealtimeSurveillanceNoVideoTrap": hh3cVMManClientRealtimeSurveillanceNoVideoTrap,
       "hh3cVMManClientVODNoVideoTrap": hh3cVMManClientVODNoVideoTrap,
       "hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap": hh3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap,
       "hh3cVMManClientVODVideoStreamDiscontinuityTrap": hh3cVMManClientVODVideoStreamDiscontinuityTrap,
       "hh3cVMManClientCtlConnExceptionTerminationTrap": hh3cVMManClientCtlConnExceptionTerminationTrap,
       "hh3cVMManClientFrequencyLoginFailTrap": hh3cVMManClientFrequencyLoginFailTrap,
       "hh3cVMManClientFrequencyVODFailTrap": hh3cVMManClientFrequencyVODFailTrap,
       "hh3cVMManDMECDisobeyStorageScheduleTrap": hh3cVMManDMECDisobeyStorageScheduleTrap,
       "hh3cVMManDMECDisobeyStorageScheduleRecoverTrap": hh3cVMManDMECDisobeyStorageScheduleRecoverTrap,
       "hh3cVMManTrapObjects": hh3cVMManTrapObjects,
       "hh3cVMManIPSANDevIP": hh3cVMManIPSANDevIP,
       "hh3cVMManRegDevIP": hh3cVMManRegDevIP,
       "hh3cVMManRegDevName": hh3cVMManRegDevName,
       "hh3cVMManRegionCoordinateX1": hh3cVMManRegionCoordinateX1,
       "hh3cVMManRegionCoordinateY1": hh3cVMManRegionCoordinateY1,
       "hh3cVMManRegionCoordinateX2": hh3cVMManRegionCoordinateX2,
       "hh3cVMManRegionCoordinateY2": hh3cVMManRegionCoordinateY2,
       "hh3cVMManCpuUsage": hh3cVMManCpuUsage,
       "hh3cVMManCpuUsageThreshold": hh3cVMManCpuUsageThreshold,
       "hh3cVMManMemUsage": hh3cVMManMemUsage,
       "hh3cVMManMemUsageThreshold": hh3cVMManMemUsageThreshold,
       "hh3cVMManHardDiskUsage": hh3cVMManHardDiskUsage,
       "hh3cVMManHardDiskUsageThreshold": hh3cVMManHardDiskUsageThreshold,
       "hh3cVMManTemperature": hh3cVMManTemperature,
       "hh3cVMManTemperatureThreshold": hh3cVMManTemperatureThreshold,
       "hh3cVMManClientIP": hh3cVMManClientIP,
       "hh3cVMManUserName": hh3cVMManUserName,
       "hh3cVMManReportContent": hh3cVMManReportContent,
       "hh3cVMManClientVideoStreamDiscontinuityInterval": hh3cVMManClientVideoStreamDiscontinuityInterval,
       "hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold": hh3cVMManClientVideoStreamDiscontinuityIntervalThreshold,
       "hh3cVMManClientStatPeriod": hh3cVMManClientStatPeriod,
       "hh3cVMManClientLoginFailNum": hh3cVMManClientLoginFailNum,
       "hh3cVMManClientLoginFailNumThreshold": hh3cVMManClientLoginFailNumThreshold,
       "hh3cVMManClientVODFailNum": hh3cVMManClientVODFailNum,
       "hh3cVMManClientVODFailNumThreshold": hh3cVMManClientVODFailNumThreshold,
       "hh3cVMManClientVODStart": hh3cVMManClientVODStart,
       "hh3cVMManClientVODEnd": hh3cVMManClientVODEnd,
       "hh3cVMManPUExternalInputAlarmChannelID": hh3cVMManPUExternalInputAlarmChannelID,
       "hh3cVMManPUECVideoChannelName": hh3cVMManPUECVideoChannelName}
)
