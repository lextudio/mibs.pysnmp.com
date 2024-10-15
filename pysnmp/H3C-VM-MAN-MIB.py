# SNMP MIB module (H3C-VM-MAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-VM-MAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:51:39 2024
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

(h3cSurveillanceMIB,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cSurveillanceMIB")

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

h3cVMMan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cVMManMIBObjects_ObjectIdentity = ObjectIdentity
h3cVMManMIBObjects = _H3cVMManMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1)
)


class _H3cVMCapabilitySet_Type(Bits):
    """Custom type h3cVMCapabilitySet based on Bits"""
    namedValues = NamedValues(
        *(("cms", 0),
          ("css", 1),
          ("dm", 2))
    )

_H3cVMCapabilitySet_Type.__name__ = "Bits"
_H3cVMCapabilitySet_Object = MibScalar
h3cVMCapabilitySet = _H3cVMCapabilitySet_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 1),
    _H3cVMCapabilitySet_Type()
)
h3cVMCapabilitySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMCapabilitySet.setStatus("current")
_H3cVMStat_ObjectIdentity = ObjectIdentity
h3cVMStat = _H3cVMStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2)
)
_H3cVMStatTotalConnEstablishRequests_Type = Counter32
_H3cVMStatTotalConnEstablishRequests_Object = MibScalar
h3cVMStatTotalConnEstablishRequests = _H3cVMStatTotalConnEstablishRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 1),
    _H3cVMStatTotalConnEstablishRequests_Type()
)
h3cVMStatTotalConnEstablishRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatTotalConnEstablishRequests.setStatus("current")
_H3cVMStatSuccConnEstablishRequests_Type = Counter32
_H3cVMStatSuccConnEstablishRequests_Object = MibScalar
h3cVMStatSuccConnEstablishRequests = _H3cVMStatSuccConnEstablishRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 2),
    _H3cVMStatSuccConnEstablishRequests_Type()
)
h3cVMStatSuccConnEstablishRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatSuccConnEstablishRequests.setStatus("current")
_H3cVMStatFailConnEstablishRequests_Type = Counter32
_H3cVMStatFailConnEstablishRequests_Object = MibScalar
h3cVMStatFailConnEstablishRequests = _H3cVMStatFailConnEstablishRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 3),
    _H3cVMStatFailConnEstablishRequests_Type()
)
h3cVMStatFailConnEstablishRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatFailConnEstablishRequests.setStatus("current")
_H3cVMStatTotalConnReleaseRequests_Type = Counter32
_H3cVMStatTotalConnReleaseRequests_Object = MibScalar
h3cVMStatTotalConnReleaseRequests = _H3cVMStatTotalConnReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 4),
    _H3cVMStatTotalConnReleaseRequests_Type()
)
h3cVMStatTotalConnReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatTotalConnReleaseRequests.setStatus("current")
_H3cVMStatSuccConnReleaseRequests_Type = Counter32
_H3cVMStatSuccConnReleaseRequests_Object = MibScalar
h3cVMStatSuccConnReleaseRequests = _H3cVMStatSuccConnReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 5),
    _H3cVMStatSuccConnReleaseRequests_Type()
)
h3cVMStatSuccConnReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatSuccConnReleaseRequests.setStatus("current")
_H3cVMStatFailConnReleaseRequests_Type = Counter32
_H3cVMStatFailConnReleaseRequests_Object = MibScalar
h3cVMStatFailConnReleaseRequests = _H3cVMStatFailConnReleaseRequests_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 6),
    _H3cVMStatFailConnReleaseRequests_Type()
)
h3cVMStatFailConnReleaseRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatFailConnReleaseRequests.setStatus("current")
_H3cVMStatExceptionTerminationConn_Type = Counter32
_H3cVMStatExceptionTerminationConn_Object = MibScalar
h3cVMStatExceptionTerminationConn = _H3cVMStatExceptionTerminationConn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 1, 2, 7),
    _H3cVMStatExceptionTerminationConn_Type()
)
h3cVMStatExceptionTerminationConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cVMStatExceptionTerminationConn.setStatus("current")
_H3cVMManMIBTrap_ObjectIdentity = ObjectIdentity
h3cVMManMIBTrap = _H3cVMManMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2)
)
_H3cVMManTrapPrex_ObjectIdentity = ObjectIdentity
h3cVMManTrapPrex = _H3cVMManTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0)
)
_H3cVMManTrapObjects_ObjectIdentity = ObjectIdentity
h3cVMManTrapObjects = _H3cVMManTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1)
)
_H3cVMManIPSANDevIP_Type = IpAddress
_H3cVMManIPSANDevIP_Object = MibScalar
h3cVMManIPSANDevIP = _H3cVMManIPSANDevIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 1),
    _H3cVMManIPSANDevIP_Type()
)
h3cVMManIPSANDevIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManIPSANDevIP.setStatus("current")
_H3cVMManRegDevIP_Type = IpAddress
_H3cVMManRegDevIP_Object = MibScalar
h3cVMManRegDevIP = _H3cVMManRegDevIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 2),
    _H3cVMManRegDevIP_Type()
)
h3cVMManRegDevIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManRegDevIP.setStatus("current")


class _H3cVMManRegDevName_Type(DisplayString):
    """Custom type h3cVMManRegDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_H3cVMManRegDevName_Type.__name__ = "DisplayString"
_H3cVMManRegDevName_Object = MibScalar
h3cVMManRegDevName = _H3cVMManRegDevName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 3),
    _H3cVMManRegDevName_Type()
)
h3cVMManRegDevName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManRegDevName.setStatus("current")
_H3cVMManRegionCoordinateX1_Type = Unsigned32
_H3cVMManRegionCoordinateX1_Object = MibScalar
h3cVMManRegionCoordinateX1 = _H3cVMManRegionCoordinateX1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 4),
    _H3cVMManRegionCoordinateX1_Type()
)
h3cVMManRegionCoordinateX1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManRegionCoordinateX1.setStatus("current")
_H3cVMManRegionCoordinateY1_Type = Unsigned32
_H3cVMManRegionCoordinateY1_Object = MibScalar
h3cVMManRegionCoordinateY1 = _H3cVMManRegionCoordinateY1_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 5),
    _H3cVMManRegionCoordinateY1_Type()
)
h3cVMManRegionCoordinateY1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManRegionCoordinateY1.setStatus("current")
_H3cVMManRegionCoordinateX2_Type = Unsigned32
_H3cVMManRegionCoordinateX2_Object = MibScalar
h3cVMManRegionCoordinateX2 = _H3cVMManRegionCoordinateX2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 6),
    _H3cVMManRegionCoordinateX2_Type()
)
h3cVMManRegionCoordinateX2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManRegionCoordinateX2.setStatus("current")
_H3cVMManRegionCoordinateY2_Type = Unsigned32
_H3cVMManRegionCoordinateY2_Object = MibScalar
h3cVMManRegionCoordinateY2 = _H3cVMManRegionCoordinateY2_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 7),
    _H3cVMManRegionCoordinateY2_Type()
)
h3cVMManRegionCoordinateY2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManRegionCoordinateY2.setStatus("current")


class _H3cVMManCpuUsage_Type(Unsigned32):
    """Custom type h3cVMManCpuUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVMManCpuUsage_Type.__name__ = "Unsigned32"
_H3cVMManCpuUsage_Object = MibScalar
h3cVMManCpuUsage = _H3cVMManCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 8),
    _H3cVMManCpuUsage_Type()
)
h3cVMManCpuUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManCpuUsage.setStatus("current")


class _H3cVMManCpuUsageThreshold_Type(Unsigned32):
    """Custom type h3cVMManCpuUsageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVMManCpuUsageThreshold_Type.__name__ = "Unsigned32"
_H3cVMManCpuUsageThreshold_Object = MibScalar
h3cVMManCpuUsageThreshold = _H3cVMManCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 9),
    _H3cVMManCpuUsageThreshold_Type()
)
h3cVMManCpuUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManCpuUsageThreshold.setStatus("current")


class _H3cVMManMemUsage_Type(Unsigned32):
    """Custom type h3cVMManMemUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVMManMemUsage_Type.__name__ = "Unsigned32"
_H3cVMManMemUsage_Object = MibScalar
h3cVMManMemUsage = _H3cVMManMemUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 10),
    _H3cVMManMemUsage_Type()
)
h3cVMManMemUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManMemUsage.setStatus("current")


class _H3cVMManMemUsageThreshold_Type(Unsigned32):
    """Custom type h3cVMManMemUsageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVMManMemUsageThreshold_Type.__name__ = "Unsigned32"
_H3cVMManMemUsageThreshold_Object = MibScalar
h3cVMManMemUsageThreshold = _H3cVMManMemUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 11),
    _H3cVMManMemUsageThreshold_Type()
)
h3cVMManMemUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManMemUsageThreshold.setStatus("current")


class _H3cVMManHardDiskUsage_Type(Unsigned32):
    """Custom type h3cVMManHardDiskUsage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVMManHardDiskUsage_Type.__name__ = "Unsigned32"
_H3cVMManHardDiskUsage_Object = MibScalar
h3cVMManHardDiskUsage = _H3cVMManHardDiskUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 12),
    _H3cVMManHardDiskUsage_Type()
)
h3cVMManHardDiskUsage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManHardDiskUsage.setStatus("current")


class _H3cVMManHardDiskUsageThreshold_Type(Unsigned32):
    """Custom type h3cVMManHardDiskUsageThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_H3cVMManHardDiskUsageThreshold_Type.__name__ = "Unsigned32"
_H3cVMManHardDiskUsageThreshold_Object = MibScalar
h3cVMManHardDiskUsageThreshold = _H3cVMManHardDiskUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 13),
    _H3cVMManHardDiskUsageThreshold_Type()
)
h3cVMManHardDiskUsageThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManHardDiskUsageThreshold.setStatus("current")
_H3cVMManTemperature_Type = Integer32
_H3cVMManTemperature_Object = MibScalar
h3cVMManTemperature = _H3cVMManTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 14),
    _H3cVMManTemperature_Type()
)
h3cVMManTemperature.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManTemperature.setStatus("current")
_H3cVMManTemperatureThreshold_Type = Integer32
_H3cVMManTemperatureThreshold_Object = MibScalar
h3cVMManTemperatureThreshold = _H3cVMManTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 15),
    _H3cVMManTemperatureThreshold_Type()
)
h3cVMManTemperatureThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManTemperatureThreshold.setStatus("current")
_H3cVMManClientIP_Type = IpAddress
_H3cVMManClientIP_Object = MibScalar
h3cVMManClientIP = _H3cVMManClientIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 16),
    _H3cVMManClientIP_Type()
)
h3cVMManClientIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientIP.setStatus("current")


class _H3cVMManUserName_Type(DisplayString):
    """Custom type h3cVMManUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cVMManUserName_Type.__name__ = "DisplayString"
_H3cVMManUserName_Object = MibScalar
h3cVMManUserName = _H3cVMManUserName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 17),
    _H3cVMManUserName_Type()
)
h3cVMManUserName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManUserName.setStatus("current")


class _H3cVMManReportContent_Type(DisplayString):
    """Custom type h3cVMManReportContent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_H3cVMManReportContent_Type.__name__ = "DisplayString"
_H3cVMManReportContent_Object = MibScalar
h3cVMManReportContent = _H3cVMManReportContent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 18),
    _H3cVMManReportContent_Type()
)
h3cVMManReportContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManReportContent.setStatus("current")
_H3cVMManClientVideoStreamDiscontinuityInterval_Type = Unsigned32
_H3cVMManClientVideoStreamDiscontinuityInterval_Object = MibScalar
h3cVMManClientVideoStreamDiscontinuityInterval = _H3cVMManClientVideoStreamDiscontinuityInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 19),
    _H3cVMManClientVideoStreamDiscontinuityInterval_Type()
)
h3cVMManClientVideoStreamDiscontinuityInterval.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientVideoStreamDiscontinuityInterval.setStatus("current")
_H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Type = Unsigned32
_H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Object = MibScalar
h3cVMManClientVideoStreamDiscontinuityIntervalThreshold = _H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 20),
    _H3cVMManClientVideoStreamDiscontinuityIntervalThreshold_Type()
)
h3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientVideoStreamDiscontinuityIntervalThreshold.setStatus("current")
_H3cVMManClientStatPeriod_Type = Unsigned32
_H3cVMManClientStatPeriod_Object = MibScalar
h3cVMManClientStatPeriod = _H3cVMManClientStatPeriod_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 21),
    _H3cVMManClientStatPeriod_Type()
)
h3cVMManClientStatPeriod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientStatPeriod.setStatus("current")
_H3cVMManClientLoginFailNum_Type = Unsigned32
_H3cVMManClientLoginFailNum_Object = MibScalar
h3cVMManClientLoginFailNum = _H3cVMManClientLoginFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 22),
    _H3cVMManClientLoginFailNum_Type()
)
h3cVMManClientLoginFailNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientLoginFailNum.setStatus("current")
_H3cVMManClientLoginFailNumThreshold_Type = Unsigned32
_H3cVMManClientLoginFailNumThreshold_Object = MibScalar
h3cVMManClientLoginFailNumThreshold = _H3cVMManClientLoginFailNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 23),
    _H3cVMManClientLoginFailNumThreshold_Type()
)
h3cVMManClientLoginFailNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientLoginFailNumThreshold.setStatus("current")
_H3cVMManClientVODFailNum_Type = Unsigned32
_H3cVMManClientVODFailNum_Object = MibScalar
h3cVMManClientVODFailNum = _H3cVMManClientVODFailNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 24),
    _H3cVMManClientVODFailNum_Type()
)
h3cVMManClientVODFailNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientVODFailNum.setStatus("current")
_H3cVMManClientVODFailNumThreshold_Type = Unsigned32
_H3cVMManClientVODFailNumThreshold_Object = MibScalar
h3cVMManClientVODFailNumThreshold = _H3cVMManClientVODFailNumThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 25),
    _H3cVMManClientVODFailNumThreshold_Type()
)
h3cVMManClientVODFailNumThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientVODFailNumThreshold.setStatus("current")
_H3cVMManClientVODStart_Type = DateAndTime
_H3cVMManClientVODStart_Object = MibScalar
h3cVMManClientVODStart = _H3cVMManClientVODStart_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 26),
    _H3cVMManClientVODStart_Type()
)
h3cVMManClientVODStart.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientVODStart.setStatus("current")
_H3cVMManClientVODEnd_Type = DateAndTime
_H3cVMManClientVODEnd_Object = MibScalar
h3cVMManClientVODEnd = _H3cVMManClientVODEnd_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 27),
    _H3cVMManClientVODEnd_Type()
)
h3cVMManClientVODEnd.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManClientVODEnd.setStatus("current")
_H3cVMManPUExternalInputAlarmChannelID_Type = Unsigned32
_H3cVMManPUExternalInputAlarmChannelID_Object = MibScalar
h3cVMManPUExternalInputAlarmChannelID = _H3cVMManPUExternalInputAlarmChannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 28),
    _H3cVMManPUExternalInputAlarmChannelID_Type()
)
h3cVMManPUExternalInputAlarmChannelID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManPUExternalInputAlarmChannelID.setStatus("current")


class _H3cVMManPUECVideoChannelName_Type(DisplayString):
    """Custom type h3cVMManPUECVideoChannelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_H3cVMManPUECVideoChannelName_Type.__name__ = "DisplayString"
_H3cVMManPUECVideoChannelName_Object = MibScalar
h3cVMManPUECVideoChannelName = _H3cVMManPUECVideoChannelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 1, 29),
    _H3cVMManPUECVideoChannelName_Type()
)
h3cVMManPUECVideoChannelName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cVMManPUECVideoChannelName.setStatus("current")

# Managed Objects groups


# Notification objects

h3cVMManDeviceOnlineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 1)
)
h3cVMManDeviceOnlineTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"))
)
if mibBuilder.loadTexts:
    h3cVMManDeviceOnlineTrap.setStatus(
        "current"
    )

h3cVMManDeviceOfflineTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 2)
)
h3cVMManDeviceOfflineTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"))
)
if mibBuilder.loadTexts:
    h3cVMManDeviceOfflineTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceExternalSemaphoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 3)
)
h3cVMManForwardDeviceExternalSemaphoreTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUExternalInputAlarmChannelID"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceExternalSemaphoreTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceVideoLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 4)
)
h3cVMManForwardDeviceVideoLossTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceVideoLossTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceVideoRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 5)
)
h3cVMManForwardDeviceVideoRecoverTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceVideoRecoverTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceMotionDetectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 6)
)
h3cVMManForwardDeviceMotionDetectTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateX1"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateY1"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateX2"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceMotionDetectTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceCoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 7)
)
h3cVMManForwardDeviceCoverTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateX1"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateY1"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateX2"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegionCoordinateY2"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceCoverTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceCpuUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 8)
)
h3cVMManForwardDeviceCpuUsageThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManCpuUsage"),
        ("H3C-VM-MAN-MIB", "h3cVMManCpuUsageThreshold"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceCpuUsageThresholdTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceMemUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 9)
)
h3cVMManForwardDeviceMemUsageThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManMemUsage"),
        ("H3C-VM-MAN-MIB", "h3cVMManMemUsageThreshold"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceMemUsageThresholdTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceHardDiskUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 10)
)
h3cVMManForwardDeviceHardDiskUsageThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManHardDiskUsage"),
        ("H3C-VM-MAN-MIB", "h3cVMManHardDiskUsageThreshold"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceHardDiskUsageThresholdTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceTemperatureThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 11)
)
h3cVMManForwardDeviceTemperatureThresholdTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManTemperature"),
        ("H3C-VM-MAN-MIB", "h3cVMManTemperatureThreshold"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceTemperatureThresholdTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceStartKinescopeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 12)
)
h3cVMManForwardDeviceStartKinescopeTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceStartKinescopeTrap.setStatus(
        "current"
    )

h3cVMManForwardDeviceStopKinescopeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 13)
)
h3cVMManForwardDeviceStopKinescopeTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManForwardDeviceStopKinescopeTrap.setStatus(
        "current"
    )

h3cVMManClientReportTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 14)
)
h3cVMManClientReportTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManReportContent"))
)
if mibBuilder.loadTexts:
    h3cVMManClientReportTrap.setStatus(
        "current"
    )

h3cVMManClientRealtimeSurveillanceNoVideoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 15)
)
h3cVMManClientRealtimeSurveillanceNoVideoTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManClientRealtimeSurveillanceNoVideoTrap.setStatus(
        "current"
    )

h3cVMManClientVODNoVideoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 16)
)
h3cVMManClientVODNoVideoTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVODStart"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVODEnd"),
        ("H3C-VM-MAN-MIB", "h3cVMManIPSANDevIP"))
)
if mibBuilder.loadTexts:
    h3cVMManClientVODNoVideoTrap.setStatus(
        "current"
    )

h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 17)
)
h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVideoStreamDiscontinuityInterval"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVideoStreamDiscontinuityIntervalThreshold"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap.setStatus(
        "current"
    )

h3cVMManClientVODVideoStreamDiscontinuityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 18)
)
h3cVMManClientVODVideoStreamDiscontinuityTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevName"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVODStart"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVODEnd"),
        ("H3C-VM-MAN-MIB", "h3cVMManIPSANDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVideoStreamDiscontinuityInterval"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVideoStreamDiscontinuityIntervalThreshold"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    h3cVMManClientVODVideoStreamDiscontinuityTrap.setStatus(
        "current"
    )

h3cVMManClientCtlConnExceptionTerminationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 19)
)
h3cVMManClientCtlConnExceptionTerminationTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"))
)
if mibBuilder.loadTexts:
    h3cVMManClientCtlConnExceptionTerminationTrap.setStatus(
        "current"
    )

h3cVMManClientFrequencyLoginFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 20)
)
h3cVMManClientFrequencyLoginFailTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientLoginFailNum"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientLoginFailNumThreshold"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    h3cVMManClientFrequencyLoginFailTrap.setStatus(
        "current"
    )

h3cVMManClientFrequencyVODFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 21)
)
h3cVMManClientFrequencyVODFailTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManUserName"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVODFailNum"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientVODFailNumThreshold"),
        ("H3C-VM-MAN-MIB", "h3cVMManClientStatPeriod"))
)
if mibBuilder.loadTexts:
    h3cVMManClientFrequencyVODFailTrap.setStatus(
        "current"
    )

h3cVMManDMECDisobeyStorageScheduleTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 22)
)
h3cVMManDMECDisobeyStorageScheduleTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManDMECDisobeyStorageScheduleTrap.setStatus(
        "current"
    )

h3cVMManDMECDisobeyStorageScheduleRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 9, 1, 2, 0, 23)
)
h3cVMManDMECDisobeyStorageScheduleRecoverTrap.setObjects(
      *(("ENTITY-MIB", "entPhysicalAssetID"),
        ("H3C-VM-MAN-MIB", "h3cVMManRegDevIP"),
        ("H3C-VM-MAN-MIB", "h3cVMManPUECVideoChannelName"))
)
if mibBuilder.loadTexts:
    h3cVMManDMECDisobeyStorageScheduleRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-VM-MAN-MIB",
    **{"h3cVMMan": h3cVMMan,
       "h3cVMManMIBObjects": h3cVMManMIBObjects,
       "h3cVMCapabilitySet": h3cVMCapabilitySet,
       "h3cVMStat": h3cVMStat,
       "h3cVMStatTotalConnEstablishRequests": h3cVMStatTotalConnEstablishRequests,
       "h3cVMStatSuccConnEstablishRequests": h3cVMStatSuccConnEstablishRequests,
       "h3cVMStatFailConnEstablishRequests": h3cVMStatFailConnEstablishRequests,
       "h3cVMStatTotalConnReleaseRequests": h3cVMStatTotalConnReleaseRequests,
       "h3cVMStatSuccConnReleaseRequests": h3cVMStatSuccConnReleaseRequests,
       "h3cVMStatFailConnReleaseRequests": h3cVMStatFailConnReleaseRequests,
       "h3cVMStatExceptionTerminationConn": h3cVMStatExceptionTerminationConn,
       "h3cVMManMIBTrap": h3cVMManMIBTrap,
       "h3cVMManTrapPrex": h3cVMManTrapPrex,
       "h3cVMManDeviceOnlineTrap": h3cVMManDeviceOnlineTrap,
       "h3cVMManDeviceOfflineTrap": h3cVMManDeviceOfflineTrap,
       "h3cVMManForwardDeviceExternalSemaphoreTrap": h3cVMManForwardDeviceExternalSemaphoreTrap,
       "h3cVMManForwardDeviceVideoLossTrap": h3cVMManForwardDeviceVideoLossTrap,
       "h3cVMManForwardDeviceVideoRecoverTrap": h3cVMManForwardDeviceVideoRecoverTrap,
       "h3cVMManForwardDeviceMotionDetectTrap": h3cVMManForwardDeviceMotionDetectTrap,
       "h3cVMManForwardDeviceCoverTrap": h3cVMManForwardDeviceCoverTrap,
       "h3cVMManForwardDeviceCpuUsageThresholdTrap": h3cVMManForwardDeviceCpuUsageThresholdTrap,
       "h3cVMManForwardDeviceMemUsageThresholdTrap": h3cVMManForwardDeviceMemUsageThresholdTrap,
       "h3cVMManForwardDeviceHardDiskUsageThresholdTrap": h3cVMManForwardDeviceHardDiskUsageThresholdTrap,
       "h3cVMManForwardDeviceTemperatureThresholdTrap": h3cVMManForwardDeviceTemperatureThresholdTrap,
       "h3cVMManForwardDeviceStartKinescopeTrap": h3cVMManForwardDeviceStartKinescopeTrap,
       "h3cVMManForwardDeviceStopKinescopeTrap": h3cVMManForwardDeviceStopKinescopeTrap,
       "h3cVMManClientReportTrap": h3cVMManClientReportTrap,
       "h3cVMManClientRealtimeSurveillanceNoVideoTrap": h3cVMManClientRealtimeSurveillanceNoVideoTrap,
       "h3cVMManClientVODNoVideoTrap": h3cVMManClientVODNoVideoTrap,
       "h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap": h3cVMManClientRealtimeSurveillanceVideoStreamDiscontinuityTrap,
       "h3cVMManClientVODVideoStreamDiscontinuityTrap": h3cVMManClientVODVideoStreamDiscontinuityTrap,
       "h3cVMManClientCtlConnExceptionTerminationTrap": h3cVMManClientCtlConnExceptionTerminationTrap,
       "h3cVMManClientFrequencyLoginFailTrap": h3cVMManClientFrequencyLoginFailTrap,
       "h3cVMManClientFrequencyVODFailTrap": h3cVMManClientFrequencyVODFailTrap,
       "h3cVMManDMECDisobeyStorageScheduleTrap": h3cVMManDMECDisobeyStorageScheduleTrap,
       "h3cVMManDMECDisobeyStorageScheduleRecoverTrap": h3cVMManDMECDisobeyStorageScheduleRecoverTrap,
       "h3cVMManTrapObjects": h3cVMManTrapObjects,
       "h3cVMManIPSANDevIP": h3cVMManIPSANDevIP,
       "h3cVMManRegDevIP": h3cVMManRegDevIP,
       "h3cVMManRegDevName": h3cVMManRegDevName,
       "h3cVMManRegionCoordinateX1": h3cVMManRegionCoordinateX1,
       "h3cVMManRegionCoordinateY1": h3cVMManRegionCoordinateY1,
       "h3cVMManRegionCoordinateX2": h3cVMManRegionCoordinateX2,
       "h3cVMManRegionCoordinateY2": h3cVMManRegionCoordinateY2,
       "h3cVMManCpuUsage": h3cVMManCpuUsage,
       "h3cVMManCpuUsageThreshold": h3cVMManCpuUsageThreshold,
       "h3cVMManMemUsage": h3cVMManMemUsage,
       "h3cVMManMemUsageThreshold": h3cVMManMemUsageThreshold,
       "h3cVMManHardDiskUsage": h3cVMManHardDiskUsage,
       "h3cVMManHardDiskUsageThreshold": h3cVMManHardDiskUsageThreshold,
       "h3cVMManTemperature": h3cVMManTemperature,
       "h3cVMManTemperatureThreshold": h3cVMManTemperatureThreshold,
       "h3cVMManClientIP": h3cVMManClientIP,
       "h3cVMManUserName": h3cVMManUserName,
       "h3cVMManReportContent": h3cVMManReportContent,
       "h3cVMManClientVideoStreamDiscontinuityInterval": h3cVMManClientVideoStreamDiscontinuityInterval,
       "h3cVMManClientVideoStreamDiscontinuityIntervalThreshold": h3cVMManClientVideoStreamDiscontinuityIntervalThreshold,
       "h3cVMManClientStatPeriod": h3cVMManClientStatPeriod,
       "h3cVMManClientLoginFailNum": h3cVMManClientLoginFailNum,
       "h3cVMManClientLoginFailNumThreshold": h3cVMManClientLoginFailNumThreshold,
       "h3cVMManClientVODFailNum": h3cVMManClientVODFailNum,
       "h3cVMManClientVODFailNumThreshold": h3cVMManClientVODFailNumThreshold,
       "h3cVMManClientVODStart": h3cVMManClientVODStart,
       "h3cVMManClientVODEnd": h3cVMManClientVODEnd,
       "h3cVMManPUExternalInputAlarmChannelID": h3cVMManPUExternalInputAlarmChannelID,
       "h3cVMManPUECVideoChannelName": h3cVMManPUECVideoChannelName}
)
