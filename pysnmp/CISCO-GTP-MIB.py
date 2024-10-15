# SNMP MIB module (CISCO-GTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:50 2024
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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

(DisplayString,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cGtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188)
)
cGtpMIB.setRevisions(
        ("2013-06-18 00:00",
         "2013-03-11 00:00",
         "2012-05-21 00:00",
         "2012-03-05 00:00",
         "2011-03-15 00:00",
         "2010-04-27 00:00",
         "2009-02-13 00:00",
         "2007-10-11 18:00",
         "2006-08-07 00:00",
         "2002-11-09 16:00",
         "2002-03-08 16:00",
         "2001-09-13 15:35",
         "2001-06-11 16:00",
         "2001-02-07 13:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CGtpMaxHistNumber(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )



class CGtpVersion(Integer32, TextualConvention):
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
        *(("version0", 1),
          ("version1", 2),
          ("version2", 3))
    )



class CGtpEntities(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("cg", 5),
          ("eNodeB", 7),
          ("mme", 4),
          ("pgw", 2),
          ("rnc", 6),
          ("sgsn", 1),
          ("sgw", 3),
          ("undefined", 0))
    )



# MIB Managed Objects in the order of their OIDs

_CGtpMIBObjects_ObjectIdentity = ObjectIdentity
cGtpMIBObjects = _CGtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1)
)
_CGtpConfigurations_ObjectIdentity = ObjectIdentity
cGtpConfigurations = _CGtpConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1)
)


class _CGtpGSNService_Type(Bits):
    """Custom type cGtpGSNService based on Bits"""
    defaultBinValue = "1"

    namedValues = NamedValues(
        *(("ggsn", 2),
          ("gtpdirector", 3),
          ("pgw", 5),
          ("sgsn", 1),
          ("sgw", 4),
          ("spgw", 6),
          ("undefined", 0))
    )

_CGtpGSNService_Type.__name__ = "Bits"
_CGtpGSNService_Object = MibScalar
cGtpGSNService = _CGtpGSNService_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 1),
    _CGtpGSNService_Type()
)
cGtpGSNService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpGSNService.setStatus("current")
_CGtpVersion_Type = CGtpVersion
_CGtpVersion_Object = MibScalar
cGtpVersion = _CGtpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 2),
    _CGtpVersion_Type()
)
cGtpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpVersion.setStatus("current")


class _CGtpT3TunnelTimer_Type(Integer32):
    """Custom type cGtpT3TunnelTimer based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGtpT3TunnelTimer_Type.__name__ = "Integer32"
_CGtpT3TunnelTimer_Object = MibScalar
cGtpT3TunnelTimer = _CGtpT3TunnelTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 3),
    _CGtpT3TunnelTimer_Type()
)
cGtpT3TunnelTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpT3TunnelTimer.setStatus("obsolete")
if mibBuilder.loadTexts:
    cGtpT3TunnelTimer.setUnits("seconds")


class _CGtpT3ResponseTimer_Type(Integer32):
    """Custom type cGtpT3ResponseTimer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGtpT3ResponseTimer_Type.__name__ = "Integer32"
_CGtpT3ResponseTimer_Object = MibScalar
cGtpT3ResponseTimer = _CGtpT3ResponseTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 4),
    _CGtpT3ResponseTimer_Type()
)
cGtpT3ResponseTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpT3ResponseTimer.setStatus("current")
if mibBuilder.loadTexts:
    cGtpT3ResponseTimer.setUnits("seconds")


class _CGtpN3Request_Type(Integer32):
    """Custom type cGtpN3Request based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGtpN3Request_Type.__name__ = "Integer32"
_CGtpN3Request_Object = MibScalar
cGtpN3Request = _CGtpN3Request_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 5),
    _CGtpN3Request_Type()
)
cGtpN3Request.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpN3Request.setStatus("current")
if mibBuilder.loadTexts:
    cGtpN3Request.setUnits("retransmissions")


class _CGtpN3BufferSize_Type(Integer32):
    """Custom type cGtpN3BufferSize based on Integer32"""
    defaultValue = 8192

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 65535),
    )


_CGtpN3BufferSize_Type.__name__ = "Integer32"
_CGtpN3BufferSize_Object = MibScalar
cGtpN3BufferSize = _CGtpN3BufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 6),
    _CGtpN3BufferSize_Type()
)
cGtpN3BufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpN3BufferSize.setStatus("current")
if mibBuilder.loadTexts:
    cGtpN3BufferSize.setUnits("bytes")


class _CGtpEchoRequestTimerEnable_Type(TruthValue):
    """Custom type cGtpEchoRequestTimerEnable based on TruthValue"""


_CGtpEchoRequestTimerEnable_Object = MibScalar
cGtpEchoRequestTimerEnable = _CGtpEchoRequestTimerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 7),
    _CGtpEchoRequestTimerEnable_Type()
)
cGtpEchoRequestTimerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpEchoRequestTimerEnable.setStatus("current")


class _CGtpEchoRequestTimer_Type(Integer32):
    """Custom type cGtpEchoRequestTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 65535),
    )


_CGtpEchoRequestTimer_Type.__name__ = "Integer32"
_CGtpEchoRequestTimer_Object = MibScalar
cGtpEchoRequestTimer = _CGtpEchoRequestTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 8),
    _CGtpEchoRequestTimer_Type()
)
cGtpEchoRequestTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpEchoRequestTimer.setStatus("current")
if mibBuilder.loadTexts:
    cGtpEchoRequestTimer.setUnits("seconds")


class _CGtpGSNTotalBandwidthResrc_Type(Unsigned32):
    """Custom type cGtpGSNTotalBandwidthResrc based on Unsigned32"""
    defaultValue = 1048576

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CGtpGSNTotalBandwidthResrc_Type.__name__ = "Unsigned32"
_CGtpGSNTotalBandwidthResrc_Object = MibScalar
cGtpGSNTotalBandwidthResrc = _CGtpGSNTotalBandwidthResrc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 9),
    _CGtpGSNTotalBandwidthResrc_Type()
)
cGtpGSNTotalBandwidthResrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpGSNTotalBandwidthResrc.setStatus("obsolete")
if mibBuilder.loadTexts:
    cGtpGSNTotalBandwidthResrc.setUnits("bits/sec")


class _CGtpMaximumPdps_Type(Unsigned32):
    """Custom type cGtpMaximumPdps based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CGtpMaximumPdps_Type.__name__ = "Unsigned32"
_CGtpMaximumPdps_Object = MibScalar
cGtpMaximumPdps = _CGtpMaximumPdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 10),
    _CGtpMaximumPdps_Type()
)
cGtpMaximumPdps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpMaximumPdps.setStatus("current")
if mibBuilder.loadTexts:
    cGtpMaximumPdps.setUnits("PDP contexts")


class _CGtpNotifEnable_Type(TruthValue):
    """Custom type cGtpNotifEnable based on TruthValue"""


_CGtpNotifEnable_Object = MibScalar
cGtpNotifEnable = _CGtpNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 11),
    _CGtpNotifEnable_Type()
)
cGtpNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpNotifEnable.setStatus("current")


class _CGtpDynamicEchoTimerEnable_Type(TruthValue):
    """Custom type cGtpDynamicEchoTimerEnable based on TruthValue"""


_CGtpDynamicEchoTimerEnable_Object = MibScalar
cGtpDynamicEchoTimerEnable = _CGtpDynamicEchoTimerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 12),
    _CGtpDynamicEchoTimerEnable_Type()
)
cGtpDynamicEchoTimerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpDynamicEchoTimerEnable.setStatus("current")


class _CGtpDynamicEchoTimerMinTime_Type(Integer32):
    """Custom type cGtpDynamicEchoTimerMinTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CGtpDynamicEchoTimerMinTime_Type.__name__ = "Integer32"
_CGtpDynamicEchoTimerMinTime_Object = MibScalar
cGtpDynamicEchoTimerMinTime = _CGtpDynamicEchoTimerMinTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 13),
    _CGtpDynamicEchoTimerMinTime_Type()
)
cGtpDynamicEchoTimerMinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpDynamicEchoTimerMinTime.setStatus("current")
if mibBuilder.loadTexts:
    cGtpDynamicEchoTimerMinTime.setUnits("seconds")


class _CGtpDynamicEchoTimerSmoothFactor_Type(Integer32):
    """Custom type cGtpDynamicEchoTimerSmoothFactor based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CGtpDynamicEchoTimerSmoothFactor_Type.__name__ = "Integer32"
_CGtpDynamicEchoTimerSmoothFactor_Object = MibScalar
cGtpDynamicEchoTimerSmoothFactor = _CGtpDynamicEchoTimerSmoothFactor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 14),
    _CGtpDynamicEchoTimerSmoothFactor_Type()
)
cGtpDynamicEchoTimerSmoothFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpDynamicEchoTimerSmoothFactor.setStatus("current")


class _CGtpPathHistoryLimit_Type(CGtpMaxHistNumber):
    """Custom type cGtpPathHistoryLimit based on CGtpMaxHistNumber"""
    defaultValue = 100


_CGtpPathHistoryLimit_Object = MibScalar
cGtpPathHistoryLimit = _CGtpPathHistoryLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 15),
    _CGtpPathHistoryLimit_Type()
)
cGtpPathHistoryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpPathHistoryLimit.setStatus("current")


class _CGtpUpdateFailDelete_Type(TruthValue):
    """Custom type cGtpUpdateFailDelete based on TruthValue"""


_CGtpUpdateFailDelete_Object = MibScalar
cGtpUpdateFailDelete = _CGtpUpdateFailDelete_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 16),
    _CGtpUpdateFailDelete_Type()
)
cGtpUpdateFailDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGtpUpdateFailDelete.setStatus("current")
_CGtpSgsnProfileTable_Object = MibTable
cGtpSgsnProfileTable = _CGtpSgsnProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cGtpSgsnProfileTable.setStatus("current")
_CGtpSgsnProfileEntry_Object = MibTableRow
cGtpSgsnProfileEntry = _CGtpSgsnProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1)
)
cGtpSgsnProfileEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpSgsnProfileIndex"),
)
if mibBuilder.loadTexts:
    cGtpSgsnProfileEntry.setStatus("current")


class _CGtpSgsnProfileIndex_Type(Unsigned32):
    """Custom type cGtpSgsnProfileIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGtpSgsnProfileIndex_Type.__name__ = "Unsigned32"
_CGtpSgsnProfileIndex_Object = MibTableColumn
cGtpSgsnProfileIndex = _CGtpSgsnProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 1),
    _CGtpSgsnProfileIndex_Type()
)
cGtpSgsnProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpSgsnProfileIndex.setStatus("current")
_CGtpSgsnProfileIpAddressType_Type = InetAddressType
_CGtpSgsnProfileIpAddressType_Object = MibTableColumn
cGtpSgsnProfileIpAddressType = _CGtpSgsnProfileIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 2),
    _CGtpSgsnProfileIpAddressType_Type()
)
cGtpSgsnProfileIpAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfileIpAddressType.setStatus("current")


class _CGtpSgsnProfileStartIpAddress_Type(InetAddress):
    """Custom type cGtpSgsnProfileStartIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CGtpSgsnProfileStartIpAddress_Type.__name__ = "InetAddress"
_CGtpSgsnProfileStartIpAddress_Object = MibTableColumn
cGtpSgsnProfileStartIpAddress = _CGtpSgsnProfileStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 3),
    _CGtpSgsnProfileStartIpAddress_Type()
)
cGtpSgsnProfileStartIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfileStartIpAddress.setStatus("current")


class _CGtpSgsnProfileEndIpAddress_Type(InetAddress):
    """Custom type cGtpSgsnProfileEndIpAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CGtpSgsnProfileEndIpAddress_Type.__name__ = "InetAddress"
_CGtpSgsnProfileEndIpAddress_Object = MibTableColumn
cGtpSgsnProfileEndIpAddress = _CGtpSgsnProfileEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 4),
    _CGtpSgsnProfileEndIpAddress_Type()
)
cGtpSgsnProfileEndIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfileEndIpAddress.setStatus("current")
_CGtpSgsnProfilePortNumber_Type = InetPortNumber
_CGtpSgsnProfilePortNumber_Object = MibTableColumn
cGtpSgsnProfilePortNumber = _CGtpSgsnProfilePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 5),
    _CGtpSgsnProfilePortNumber_Type()
)
cGtpSgsnProfilePortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfilePortNumber.setStatus("current")


class _CGtpSgsnProfileEchoDisable_Type(TruthValue):
    """Custom type cGtpSgsnProfileEchoDisable based on TruthValue"""


_CGtpSgsnProfileEchoDisable_Object = MibTableColumn
cGtpSgsnProfileEchoDisable = _CGtpSgsnProfileEchoDisable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 6),
    _CGtpSgsnProfileEchoDisable_Type()
)
cGtpSgsnProfileEchoDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfileEchoDisable.setStatus("current")


class _CGtpSgsnProfileStorageType_Type(StorageType):
    """Custom type cGtpSgsnProfileStorageType based on StorageType"""


_CGtpSgsnProfileStorageType_Object = MibTableColumn
cGtpSgsnProfileStorageType = _CGtpSgsnProfileStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 7),
    _CGtpSgsnProfileStorageType_Type()
)
cGtpSgsnProfileStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfileStorageType.setStatus("current")
_CGtpSgsnProfileRowStatus_Type = RowStatus
_CGtpSgsnProfileRowStatus_Object = MibTableColumn
cGtpSgsnProfileRowStatus = _CGtpSgsnProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 1, 18, 1, 8),
    _CGtpSgsnProfileRowStatus_Type()
)
cGtpSgsnProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGtpSgsnProfileRowStatus.setStatus("current")
_CGtpStatus_ObjectIdentity = ObjectIdentity
cGtpStatus = _CGtpStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2)
)
_CGtpLastNoRespToEchoGSNIpAddrTyp_Type = InetAddressType
_CGtpLastNoRespToEchoGSNIpAddrTyp_Object = MibScalar
cGtpLastNoRespToEchoGSNIpAddrTyp = _CGtpLastNoRespToEchoGSNIpAddrTyp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 1),
    _CGtpLastNoRespToEchoGSNIpAddrTyp_Type()
)
cGtpLastNoRespToEchoGSNIpAddrTyp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpLastNoRespToEchoGSNIpAddrTyp.setStatus("current")
_CGtpLastNoRespToEchoGSNIpAddr_Type = InetAddress
_CGtpLastNoRespToEchoGSNIpAddr_Object = MibScalar
cGtpLastNoRespToEchoGSNIpAddr = _CGtpLastNoRespToEchoGSNIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 2),
    _CGtpLastNoRespToEchoGSNIpAddr_Type()
)
cGtpLastNoRespToEchoGSNIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpLastNoRespToEchoGSNIpAddr.setStatus("current")
_CGtpPremiumQosMeanThroughput_Type = Gauge32
_CGtpPremiumQosMeanThroughput_Object = MibScalar
cGtpPremiumQosMeanThroughput = _CGtpPremiumQosMeanThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 3),
    _CGtpPremiumQosMeanThroughput_Type()
)
cGtpPremiumQosMeanThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPremiumQosMeanThroughput.setStatus("obsolete")
if mibBuilder.loadTexts:
    cGtpPremiumQosMeanThroughput.setUnits("bytes/sec")
_CGtpNormalQosMeanThroughput_Type = Gauge32
_CGtpNormalQosMeanThroughput_Object = MibScalar
cGtpNormalQosMeanThroughput = _CGtpNormalQosMeanThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 4),
    _CGtpNormalQosMeanThroughput_Type()
)
cGtpNormalQosMeanThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpNormalQosMeanThroughput.setStatus("obsolete")
if mibBuilder.loadTexts:
    cGtpNormalQosMeanThroughput.setUnits("bytes/sec")
_CGtpBestEffortQosMeanThroughput_Type = Gauge32
_CGtpBestEffortQosMeanThroughput_Object = MibScalar
cGtpBestEffortQosMeanThroughput = _CGtpBestEffortQosMeanThroughput_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 5),
    _CGtpBestEffortQosMeanThroughput_Type()
)
cGtpBestEffortQosMeanThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpBestEffortQosMeanThroughput.setStatus("obsolete")
if mibBuilder.loadTexts:
    cGtpBestEffortQosMeanThroughput.setUnits("bytes/sec")
_CGtpGSNTable_Object = MibTable
cGtpGSNTable = _CGtpGSNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 6)
)
if mibBuilder.loadTexts:
    cGtpGSNTable.setStatus("deprecated")
_CGtpGSNEntry_Object = MibTableRow
cGtpGSNEntry = _CGtpGSNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 6, 1)
)
cGtpGSNEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpGSNAddressType"),
    (0, "CISCO-GTP-MIB", "cGtpGSNAddress"),
)
if mibBuilder.loadTexts:
    cGtpGSNEntry.setStatus("deprecated")
_CGtpGSNAddressType_Type = InetAddressType
_CGtpGSNAddressType_Object = MibTableColumn
cGtpGSNAddressType = _CGtpGSNAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 6, 1, 1),
    _CGtpGSNAddressType_Type()
)
cGtpGSNAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpGSNAddressType.setStatus("deprecated")
_CGtpGSNAddress_Type = InetAddress
_CGtpGSNAddress_Object = MibTableColumn
cGtpGSNAddress = _CGtpGSNAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 6, 1, 2),
    _CGtpGSNAddress_Type()
)
cGtpGSNAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpGSNAddress.setStatus("deprecated")
_CGtpGSNVersion_Type = CGtpVersion
_CGtpGSNVersion_Object = MibTableColumn
cGtpGSNVersion = _CGtpGSNVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 6, 1, 3),
    _CGtpGSNVersion_Type()
)
cGtpGSNVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpGSNVersion.setStatus("deprecated")
_CGtpPathTable_Object = MibTable
cGtpPathTable = _CGtpPathTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7)
)
if mibBuilder.loadTexts:
    cGtpPathTable.setStatus("current")
_CGtpPathEntry_Object = MibTableRow
cGtpPathEntry = _CGtpPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1)
)
cGtpPathEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpPathAddressType"),
    (0, "CISCO-GTP-MIB", "cGtpPathAddress"),
    (0, "CISCO-GTP-MIB", "cGtpPathPort"),
)
if mibBuilder.loadTexts:
    cGtpPathEntry.setStatus("current")
_CGtpPathAddressType_Type = InetAddressType
_CGtpPathAddressType_Object = MibTableColumn
cGtpPathAddressType = _CGtpPathAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1, 1),
    _CGtpPathAddressType_Type()
)
cGtpPathAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathAddressType.setStatus("current")
_CGtpPathAddress_Type = InetAddress
_CGtpPathAddress_Object = MibTableColumn
cGtpPathAddress = _CGtpPathAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1, 2),
    _CGtpPathAddress_Type()
)
cGtpPathAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathAddress.setStatus("current")
_CGtpPathPort_Type = InetPortNumber
_CGtpPathPort_Object = MibTableColumn
cGtpPathPort = _CGtpPathPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1, 3),
    _CGtpPathPort_Type()
)
cGtpPathPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpPathPort.setStatus("current")
_CGtpPathVersion_Type = CGtpVersion
_CGtpPathVersion_Object = MibTableColumn
cGtpPathVersion = _CGtpPathVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1, 4),
    _CGtpPathVersion_Type()
)
cGtpPathVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathVersion.setStatus("current")
_CGtpPathRemoteNode_Type = CGtpEntities
_CGtpPathRemoteNode_Object = MibTableColumn
cGtpPathRemoteNode = _CGtpPathRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1, 5),
    _CGtpPathRemoteNode_Type()
)
cGtpPathRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathRemoteNode.setStatus("current")
_CGtpPathVrfName_Type = SnmpAdminString
_CGtpPathVrfName_Object = MibTableColumn
cGtpPathVrfName = _CGtpPathVrfName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 7, 1, 6),
    _CGtpPathVrfName_Type()
)
cGtpPathVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathVrfName.setStatus("current")
_CGtpTotalActivePaths_Type = Gauge32
_CGtpTotalActivePaths_Object = MibScalar
cGtpTotalActivePaths = _CGtpTotalActivePaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 8),
    _CGtpTotalActivePaths_Type()
)
cGtpTotalActivePaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalActivePaths.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalActivePaths.setUnits("Paths")
_CGtpTotalActiveGtpv1DataPaths_Type = Gauge32
_CGtpTotalActiveGtpv1DataPaths_Object = MibScalar
cGtpTotalActiveGtpv1DataPaths = _CGtpTotalActiveGtpv1DataPaths_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 2, 9),
    _CGtpTotalActiveGtpv1DataPaths_Type()
)
cGtpTotalActiveGtpv1DataPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalActiveGtpv1DataPaths.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalActiveGtpv1DataPaths.setUnits("Paths")
_CGtpStatistics_ObjectIdentity = ObjectIdentity
cGtpStatistics = _CGtpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3)
)
_CGtpPathFailureOccurrences_Type = Counter32
_CGtpPathFailureOccurrences_Object = MibScalar
cGtpPathFailureOccurrences = _CGtpPathFailureOccurrences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 1),
    _CGtpPathFailureOccurrences_Type()
)
cGtpPathFailureOccurrences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathFailureOccurrences.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathFailureOccurrences.setUnits("times")
_CGtpCurrentUsedBandwidth_Type = Gauge32
_CGtpCurrentUsedBandwidth_Object = MibScalar
cGtpCurrentUsedBandwidth = _CGtpCurrentUsedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 2),
    _CGtpCurrentUsedBandwidth_Type()
)
cGtpCurrentUsedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpCurrentUsedBandwidth.setStatus("obsolete")
if mibBuilder.loadTexts:
    cGtpCurrentUsedBandwidth.setUnits("bits/sec")
_CGtpTotalDroppedPackets_Type = Counter32
_CGtpTotalDroppedPackets_Object = MibScalar
cGtpTotalDroppedPackets = _CGtpTotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 3),
    _CGtpTotalDroppedPackets_Type()
)
cGtpTotalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDroppedPackets.setStatus("current")
_CGtpPathStatisticsTable_Object = MibTable
cGtpPathStatisticsTable = _CGtpPathStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4)
)
if mibBuilder.loadTexts:
    cGtpPathStatisticsTable.setStatus("current")
_CGtpPathStatisticsEntry_Object = MibTableRow
cGtpPathStatisticsEntry = _CGtpPathStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1)
)
cGtpPathStatisticsEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpPathAddressType"),
    (0, "CISCO-GTP-MIB", "cGtpPathAddress"),
    (0, "CISCO-GTP-MIB", "cGtpPathPort"),
)
if mibBuilder.loadTexts:
    cGtpPathStatisticsEntry.setStatus("current")
_CGtpUnexpectedMsgs_Type = Counter32
_CGtpUnexpectedMsgs_Object = MibTableColumn
cGtpUnexpectedMsgs = _CGtpUnexpectedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 1),
    _CGtpUnexpectedMsgs_Type()
)
cGtpUnexpectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpUnexpectedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpUnexpectedMsgs.setUnits("messages")
_CGtpDroppedDataMsgs_Type = Counter32
_CGtpDroppedDataMsgs_Object = MibTableColumn
cGtpDroppedDataMsgs = _CGtpDroppedDataMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 2),
    _CGtpDroppedDataMsgs_Type()
)
cGtpDroppedDataMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpDroppedDataMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpDroppedDataMsgs.setUnits("messages")
_CGtpRcvdPDUMsgs_Type = Counter32
_CGtpRcvdPDUMsgs_Object = MibTableColumn
cGtpRcvdPDUMsgs = _CGtpRcvdPDUMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 3),
    _CGtpRcvdPDUMsgs_Type()
)
cGtpRcvdPDUMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRcvdPDUMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpRcvdPDUMsgs.setUnits("messages")
_CGtpSentPDUMsgs_Type = Counter32
_CGtpSentPDUMsgs_Object = MibTableColumn
cGtpSentPDUMsgs = _CGtpSentPDUMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 4),
    _CGtpSentPDUMsgs_Type()
)
cGtpSentPDUMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpSentPDUMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpSentPDUMsgs.setUnits("messages")
_CGtpRcvdPDUOctets_Type = Counter64
_CGtpRcvdPDUOctets_Object = MibTableColumn
cGtpRcvdPDUOctets = _CGtpRcvdPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 5),
    _CGtpRcvdPDUOctets_Type()
)
cGtpRcvdPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRcvdPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpRcvdPDUOctets.setUnits("bytes")
_CGtpSentPDUOctets_Type = Counter64
_CGtpSentPDUOctets_Object = MibTableColumn
cGtpSentPDUOctets = _CGtpSentPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 6),
    _CGtpSentPDUOctets_Type()
)
cGtpSentPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpSentPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpSentPDUOctets.setUnits("bytes")
_CGtpMsgTooShort_Type = Counter32
_CGtpMsgTooShort_Object = MibTableColumn
cGtpMsgTooShort = _CGtpMsgTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 7),
    _CGtpMsgTooShort_Type()
)
cGtpMsgTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpMsgTooShort.setStatus("current")
if mibBuilder.loadTexts:
    cGtpMsgTooShort.setUnits("messages")
_CGtpUnknownMsgs_Type = Counter32
_CGtpUnknownMsgs_Object = MibTableColumn
cGtpUnknownMsgs = _CGtpUnknownMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 8),
    _CGtpUnknownMsgs_Type()
)
cGtpUnknownMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpUnknownMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpUnknownMsgs.setUnits("messages")
_CGtpUnexpectedSigMsgs_Type = Counter32
_CGtpUnexpectedSigMsgs_Object = MibTableColumn
cGtpUnexpectedSigMsgs = _CGtpUnexpectedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 9),
    _CGtpUnexpectedSigMsgs_Type()
)
cGtpUnexpectedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpUnexpectedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpUnexpectedSigMsgs.setUnits("messages")
_CGtpRoamingPDUs_Type = Counter32
_CGtpRoamingPDUs_Object = MibTableColumn
cGtpRoamingPDUs = _CGtpRoamingPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 10),
    _CGtpRoamingPDUs_Type()
)
cGtpRoamingPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRoamingPDUs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGtpRoamingPDUs.setUnits("pdus")
_CGtpSecurityViolations_Type = Counter32
_CGtpSecurityViolations_Object = MibTableColumn
cGtpSecurityViolations = _CGtpSecurityViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 11),
    _CGtpSecurityViolations_Type()
)
cGtpSecurityViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpSecurityViolations.setStatus("current")
_CGtpUnsupportedExtHdr_Type = Counter32
_CGtpUnsupportedExtHdr_Object = MibTableColumn
cGtpUnsupportedExtHdr = _CGtpUnsupportedExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 12),
    _CGtpUnsupportedExtHdr_Type()
)
cGtpUnsupportedExtHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpUnsupportedExtHdr.setStatus("current")
if mibBuilder.loadTexts:
    cGtpUnsupportedExtHdr.setUnits("pdps")
_CGtpPathFailures_Type = Counter32
_CGtpPathFailures_Object = MibTableColumn
cGtpPathFailures = _CGtpPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 13),
    _CGtpPathFailures_Type()
)
cGtpPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathFailures.setStatus("current")
_CGtpTotalDropped_Type = Counter32
_CGtpTotalDropped_Object = MibTableColumn
cGtpTotalDropped = _CGtpTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 14),
    _CGtpTotalDropped_Type()
)
cGtpTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDropped.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDropped.setUnits("packets")
_CGtpDroppedSigMsgs_Type = Counter32
_CGtpDroppedSigMsgs_Object = MibTableColumn
cGtpDroppedSigMsgs = _CGtpDroppedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 15),
    _CGtpDroppedSigMsgs_Type()
)
cGtpDroppedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpDroppedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpDroppedSigMsgs.setUnits("messages")
_CGtpRcvdSigMsgs_Type = Counter32
_CGtpRcvdSigMsgs_Object = MibTableColumn
cGtpRcvdSigMsgs = _CGtpRcvdSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 16),
    _CGtpRcvdSigMsgs_Type()
)
cGtpRcvdSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRcvdSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpRcvdSigMsgs.setUnits("messages")
_CGtpSentSigMsgs_Type = Counter32
_CGtpSentSigMsgs_Object = MibTableColumn
cGtpSentSigMsgs = _CGtpSentSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 17),
    _CGtpSentSigMsgs_Type()
)
cGtpSentSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpSentSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpSentSigMsgs.setUnits("messages")
_CGtpTotalCreatedPDPs_Type = Counter32
_CGtpTotalCreatedPDPs_Object = MibTableColumn
cGtpTotalCreatedPDPs = _CGtpTotalCreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 18),
    _CGtpTotalCreatedPDPs_Type()
)
cGtpTotalCreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalCreatedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalCreatedPDPs.setUnits("pdps")
_CGtpTotalDeletedPDPs_Type = Counter32
_CGtpTotalDeletedPDPs_Object = MibTableColumn
cGtpTotalDeletedPDPs = _CGtpTotalDeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 19),
    _CGtpTotalDeletedPDPs_Type()
)
cGtpTotalDeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDeletedPDPs.setUnits("pdps")
_CGtpTotalCreatedPppPDPs_Type = Counter32
_CGtpTotalCreatedPppPDPs_Object = MibTableColumn
cGtpTotalCreatedPppPDPs = _CGtpTotalCreatedPppPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 20),
    _CGtpTotalCreatedPppPDPs_Type()
)
cGtpTotalCreatedPppPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalCreatedPppPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalCreatedPppPDPs.setUnits("pdps")
_CGtpTotalDeletedPppPDPs_Type = Counter32
_CGtpTotalDeletedPppPDPs_Object = MibTableColumn
cGtpTotalDeletedPppPDPs = _CGtpTotalDeletedPppPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 21),
    _CGtpTotalDeletedPppPDPs_Type()
)
cGtpTotalDeletedPppPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDeletedPppPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDeletedPppPDPs.setUnits("pdps")
_CGtpSinglePDPSessCleared_Type = Counter32
_CGtpSinglePDPSessCleared_Object = MibTableColumn
cGtpSinglePDPSessCleared = _CGtpSinglePDPSessCleared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 22),
    _CGtpSinglePDPSessCleared_Type()
)
cGtpSinglePDPSessCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpSinglePDPSessCleared.setStatus("current")
if mibBuilder.loadTexts:
    cGtpSinglePDPSessCleared.setUnits("pdps")
_CGtpPathFailLocalDelPDPs_Type = Counter32
_CGtpPathFailLocalDelPDPs_Object = MibTableColumn
cGtpPathFailLocalDelPDPs = _CGtpPathFailLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 23),
    _CGtpPathFailLocalDelPDPs_Type()
)
cGtpPathFailLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpPathFailLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpPathFailLocalDelPDPs.setUnits("pdps")
_CGtpVerUpgradeLocalDelPDPs_Type = Counter32
_CGtpVerUpgradeLocalDelPDPs_Object = MibTableColumn
cGtpVerUpgradeLocalDelPDPs = _CGtpVerUpgradeLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 24),
    _CGtpVerUpgradeLocalDelPDPs_Type()
)
cGtpVerUpgradeLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpVerUpgradeLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpVerUpgradeLocalDelPDPs.setUnits("pdps")
_CGtpNoSgsnLocalDelPDPs_Type = Counter32
_CGtpNoSgsnLocalDelPDPs_Object = MibTableColumn
cGtpNoSgsnLocalDelPDPs = _CGtpNoSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 25),
    _CGtpNoSgsnLocalDelPDPs_Type()
)
cGtpNoSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpNoSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpNoSgsnLocalDelPDPs.setUnits("pdps")
_CGtpVerFallbackLocalDelPDPs_Type = Counter32
_CGtpVerFallbackLocalDelPDPs_Object = MibTableColumn
cGtpVerFallbackLocalDelPDPs = _CGtpVerFallbackLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 26),
    _CGtpVerFallbackLocalDelPDPs_Type()
)
cGtpVerFallbackLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpVerFallbackLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpVerFallbackLocalDelPDPs.setUnits("pdps")
_CGtpCreateCollideWithDel_Type = Counter32
_CGtpCreateCollideWithDel_Object = MibTableColumn
cGtpCreateCollideWithDel = _CGtpCreateCollideWithDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 27),
    _CGtpCreateCollideWithDel_Type()
)
cGtpCreateCollideWithDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpCreateCollideWithDel.setStatus("current")
_CGtpVersionChanges_Type = Counter32
_CGtpVersionChanges_Object = MibTableColumn
cGtpVersionChanges = _CGtpVersionChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 28),
    _CGtpVersionChanges_Type()
)
cGtpVersionChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpVersionChanges.setStatus("current")
_CGtpRetransCreatePDPReqs_Type = Counter32
_CGtpRetransCreatePDPReqs_Object = MibTableColumn
cGtpRetransCreatePDPReqs = _CGtpRetransCreatePDPReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 29),
    _CGtpRetransCreatePDPReqs_Type()
)
cGtpRetransCreatePDPReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRetransCreatePDPReqs.setStatus("current")
_CGtpCreateAsUpdate_Type = Counter32
_CGtpCreateAsUpdate_Object = MibTableColumn
cGtpCreateAsUpdate = _CGtpCreateAsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 30),
    _CGtpCreateAsUpdate_Type()
)
cGtpCreateAsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpCreateAsUpdate.setStatus("current")
_CGtpIpv6PdpActRejects_Type = Counter32
_CGtpIpv6PdpActRejects_Object = MibTableColumn
cGtpIpv6PdpActRejects = _CGtpIpv6PdpActRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 31),
    _CGtpIpv6PdpActRejects_Type()
)
cGtpIpv6PdpActRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6PdpActRejects.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6PdpActRejects.setUnits("pdps")
_CGtpIpv6CreatedPDPs_Type = Counter32
_CGtpIpv6CreatedPDPs_Object = MibTableColumn
cGtpIpv6CreatedPDPs = _CGtpIpv6CreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 32),
    _CGtpIpv6CreatedPDPs_Type()
)
cGtpIpv6CreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6CreatedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6CreatedPDPs.setUnits("pdps")
_CGtpIpv6DeletedPDPs_Type = Counter32
_CGtpIpv6DeletedPDPs_Object = MibTableColumn
cGtpIpv6DeletedPDPs = _CGtpIpv6DeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 33),
    _CGtpIpv6DeletedPDPs_Type()
)
cGtpIpv6DeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6DeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6DeletedPDPs.setUnits("pdps")
_CGtpIpv6RcvdSigMsgs_Type = Counter32
_CGtpIpv6RcvdSigMsgs_Object = MibTableColumn
cGtpIpv6RcvdSigMsgs = _CGtpIpv6RcvdSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 34),
    _CGtpIpv6RcvdSigMsgs_Type()
)
cGtpIpv6RcvdSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6RcvdSigMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGtpIpv6RcvdSigMsgs.setUnits("messages")
_CGtpIpv6SentSigMsgs_Type = Counter32
_CGtpIpv6SentSigMsgs_Object = MibTableColumn
cGtpIpv6SentSigMsgs = _CGtpIpv6SentSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 35),
    _CGtpIpv6SentSigMsgs_Type()
)
cGtpIpv6SentSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6SentSigMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGtpIpv6SentSigMsgs.setUnits("messages")
_CGtpIpv6RcvdPDUs_Type = Counter32
_CGtpIpv6RcvdPDUs_Object = MibTableColumn
cGtpIpv6RcvdPDUs = _CGtpIpv6RcvdPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 36),
    _CGtpIpv6RcvdPDUs_Type()
)
cGtpIpv6RcvdPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6RcvdPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6RcvdPDUs.setUnits("messages")
_CGtpIpv6SentPDUs_Type = Counter32
_CGtpIpv6SentPDUs_Object = MibTableColumn
cGtpIpv6SentPDUs = _CGtpIpv6SentPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 37),
    _CGtpIpv6SentPDUs_Type()
)
cGtpIpv6SentPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6SentPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6SentPDUs.setUnits("messages")
_CGtpIpv6RcvdOctets_Type = Counter64
_CGtpIpv6RcvdOctets_Object = MibTableColumn
cGtpIpv6RcvdOctets = _CGtpIpv6RcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 38),
    _CGtpIpv6RcvdOctets_Type()
)
cGtpIpv6RcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6RcvdOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6RcvdOctets.setUnits("bytes")
_CGtpIpv6SentOctets_Type = Counter64
_CGtpIpv6SentOctets_Object = MibTableColumn
cGtpIpv6SentOctets = _CGtpIpv6SentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 39),
    _CGtpIpv6SentOctets_Type()
)
cGtpIpv6SentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv6SentOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpIpv6SentOctets.setUnits("bytes")
_CGtpNoWaitSgsnLocalDelPDPs_Type = Counter32
_CGtpNoWaitSgsnLocalDelPDPs_Object = MibTableColumn
cGtpNoWaitSgsnLocalDelPDPs = _CGtpNoWaitSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 40),
    _CGtpNoWaitSgsnLocalDelPDPs_Type()
)
cGtpNoWaitSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpNoWaitSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpNoWaitSgsnLocalDelPDPs.setUnits("pdps")
_CGtpNoReqSgsnLocalDelPDPs_Type = Counter32
_CGtpNoReqSgsnLocalDelPDPs_Object = MibTableColumn
cGtpNoReqSgsnLocalDelPDPs = _CGtpNoReqSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 41),
    _CGtpNoReqSgsnLocalDelPDPs_Type()
)
cGtpNoReqSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpNoReqSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpNoReqSgsnLocalDelPDPs.setUnits("pdps")
_CGtpRoamingTrustedPDPs_Type = Counter32
_CGtpRoamingTrustedPDPs_Object = MibTableColumn
cGtpRoamingTrustedPDPs = _CGtpRoamingTrustedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 42),
    _CGtpRoamingTrustedPDPs_Type()
)
cGtpRoamingTrustedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRoamingTrustedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpRoamingTrustedPDPs.setUnits("pdps")
_CGtpRoamingNonTrustedPDPs_Type = Counter32
_CGtpRoamingNonTrustedPDPs_Object = MibTableColumn
cGtpRoamingNonTrustedPDPs = _CGtpRoamingNonTrustedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 43),
    _CGtpRoamingNonTrustedPDPs_Type()
)
cGtpRoamingNonTrustedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRoamingNonTrustedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpRoamingNonTrustedPDPs.setUnits("pdps")
_CGtpNonRoamingPDPs_Type = Counter32
_CGtpNonRoamingPDPs_Object = MibTableColumn
cGtpNonRoamingPDPs = _CGtpNonRoamingPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 44),
    _CGtpNonRoamingPDPs_Type()
)
cGtpNonRoamingPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpNonRoamingPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpNonRoamingPDPs.setUnits("pdps")
_CGtpSentPdpUpdateReqs_Type = Counter32
_CGtpSentPdpUpdateReqs_Object = MibTableColumn
cGtpSentPdpUpdateReqs = _CGtpSentPdpUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 45),
    _CGtpSentPdpUpdateReqs_Type()
)
cGtpSentPdpUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpSentPdpUpdateReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpSentPdpUpdateReqs.setUnits("messages")
_CGtpRcvdPdpUpdateResponses_Type = Counter32
_CGtpRcvdPdpUpdateResponses_Object = MibTableColumn
cGtpRcvdPdpUpdateResponses = _CGtpRcvdPdpUpdateResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 46),
    _CGtpRcvdPdpUpdateResponses_Type()
)
cGtpRcvdPdpUpdateResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpRcvdPdpUpdateResponses.setStatus("current")
if mibBuilder.loadTexts:
    cGtpRcvdPdpUpdateResponses.setUnits("messages")
_CGtpTotalDtEnabled_Type = Counter32
_CGtpTotalDtEnabled_Object = MibTableColumn
cGtpTotalDtEnabled = _CGtpTotalDtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 47),
    _CGtpTotalDtEnabled_Type()
)
cGtpTotalDtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDtEnabled.setStatus("current")
_CGtpIpv4v6CreatedPDPs_Type = Counter32
_CGtpIpv4v6CreatedPDPs_Object = MibTableColumn
cGtpIpv4v6CreatedPDPs = _CGtpIpv4v6CreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 48),
    _CGtpIpv4v6CreatedPDPs_Type()
)
cGtpIpv4v6CreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv4v6CreatedPDPs.setStatus("current")
_CGtpIpv4v6DeletedPDPs_Type = Counter32
_CGtpIpv4v6DeletedPDPs_Object = MibTableColumn
cGtpIpv4v6DeletedPDPs = _CGtpIpv4v6DeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 4, 1, 49),
    _CGtpIpv4v6DeletedPDPs_Type()
)
cGtpIpv4v6DeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpIpv4v6DeletedPDPs.setStatus("current")
_CGtpPathStatisticsHistoryTable_Object = MibTable
cGtpPathStatisticsHistoryTable = _CGtpPathStatisticsHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5)
)
if mibBuilder.loadTexts:
    cGtpPathStatisticsHistoryTable.setStatus("current")
_CGtpPathStatisticsHistEntry_Object = MibTableRow
cGtpPathStatisticsHistEntry = _CGtpPathStatisticsHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1)
)
cGtpPathStatisticsHistEntry.setIndexNames(
    (0, "CISCO-GTP-MIB", "cGtpHistIndex"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemoteAddrType"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemoteAddress"),
    (0, "CISCO-GTP-MIB", "cGtpHistRemotePort"),
)
if mibBuilder.loadTexts:
    cGtpPathStatisticsHistEntry.setStatus("current")
_CGtpHistIndex_Type = CGtpMaxHistNumber
_CGtpHistIndex_Object = MibTableColumn
cGtpHistIndex = _CGtpHistIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 1),
    _CGtpHistIndex_Type()
)
cGtpHistIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpHistIndex.setStatus("current")
_CGtpHistRemoteAddrType_Type = InetAddressType
_CGtpHistRemoteAddrType_Object = MibTableColumn
cGtpHistRemoteAddrType = _CGtpHistRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 2),
    _CGtpHistRemoteAddrType_Type()
)
cGtpHistRemoteAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpHistRemoteAddrType.setStatus("current")
_CGtpHistRemoteAddress_Type = InetAddress
_CGtpHistRemoteAddress_Object = MibTableColumn
cGtpHistRemoteAddress = _CGtpHistRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 3),
    _CGtpHistRemoteAddress_Type()
)
cGtpHistRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpHistRemoteAddress.setStatus("current")
_CGtpHistRemotePort_Type = InetPortNumber
_CGtpHistRemotePort_Object = MibTableColumn
cGtpHistRemotePort = _CGtpHistRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 4),
    _CGtpHistRemotePort_Type()
)
cGtpHistRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGtpHistRemotePort.setStatus("current")
_CGtpHistUnexpectedMsgs_Type = Counter32
_CGtpHistUnexpectedMsgs_Object = MibTableColumn
cGtpHistUnexpectedMsgs = _CGtpHistUnexpectedMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 5),
    _CGtpHistUnexpectedMsgs_Type()
)
cGtpHistUnexpectedMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistUnexpectedMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistUnexpectedMsgs.setUnits("messages")
_CGtpHistDroppedDataMsgs_Type = Counter32
_CGtpHistDroppedDataMsgs_Object = MibTableColumn
cGtpHistDroppedDataMsgs = _CGtpHistDroppedDataMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 6),
    _CGtpHistDroppedDataMsgs_Type()
)
cGtpHistDroppedDataMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistDroppedDataMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistDroppedDataMsgs.setUnits("messages")
_CGtpHistRcvdPDUMsgs_Type = Counter32
_CGtpHistRcvdPDUMsgs_Object = MibTableColumn
cGtpHistRcvdPDUMsgs = _CGtpHistRcvdPDUMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 7),
    _CGtpHistRcvdPDUMsgs_Type()
)
cGtpHistRcvdPDUMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRcvdPDUMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistRcvdPDUMsgs.setUnits("messages")
_CGtpHistSentPDUMsgs_Type = Counter32
_CGtpHistSentPDUMsgs_Object = MibTableColumn
cGtpHistSentPDUMsgs = _CGtpHistSentPDUMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 8),
    _CGtpHistSentPDUMsgs_Type()
)
cGtpHistSentPDUMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistSentPDUMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistSentPDUMsgs.setUnits("messages")
_CGtpHistRcvdPDUOctets_Type = Counter64
_CGtpHistRcvdPDUOctets_Object = MibTableColumn
cGtpHistRcvdPDUOctets = _CGtpHistRcvdPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 9),
    _CGtpHistRcvdPDUOctets_Type()
)
cGtpHistRcvdPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRcvdPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistRcvdPDUOctets.setUnits("bytes")
_CGtpHistSentPDUOctets_Type = Counter64
_CGtpHistSentPDUOctets_Object = MibTableColumn
cGtpHistSentPDUOctets = _CGtpHistSentPDUOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 10),
    _CGtpHistSentPDUOctets_Type()
)
cGtpHistSentPDUOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistSentPDUOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistSentPDUOctets.setUnits("bytes")
_CGtpHistMsgTooShort_Type = Counter32
_CGtpHistMsgTooShort_Object = MibTableColumn
cGtpHistMsgTooShort = _CGtpHistMsgTooShort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 11),
    _CGtpHistMsgTooShort_Type()
)
cGtpHistMsgTooShort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistMsgTooShort.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistMsgTooShort.setUnits("messages")
_CGtpHistUnknownMsgs_Type = Counter32
_CGtpHistUnknownMsgs_Object = MibTableColumn
cGtpHistUnknownMsgs = _CGtpHistUnknownMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 12),
    _CGtpHistUnknownMsgs_Type()
)
cGtpHistUnknownMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistUnknownMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistUnknownMsgs.setUnits("messages")
_CGtpHistUnexpectedSigMsgs_Type = Counter32
_CGtpHistUnexpectedSigMsgs_Object = MibTableColumn
cGtpHistUnexpectedSigMsgs = _CGtpHistUnexpectedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 13),
    _CGtpHistUnexpectedSigMsgs_Type()
)
cGtpHistUnexpectedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistUnexpectedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistUnexpectedSigMsgs.setUnits("messages")
_CGtpHistRoamingPDUs_Type = Counter32
_CGtpHistRoamingPDUs_Object = MibTableColumn
cGtpHistRoamingPDUs = _CGtpHistRoamingPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 14),
    _CGtpHistRoamingPDUs_Type()
)
cGtpHistRoamingPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRoamingPDUs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGtpHistRoamingPDUs.setUnits("pdus")
_CGtpHistSecurityViolations_Type = Counter32
_CGtpHistSecurityViolations_Object = MibTableColumn
cGtpHistSecurityViolations = _CGtpHistSecurityViolations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 15),
    _CGtpHistSecurityViolations_Type()
)
cGtpHistSecurityViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistSecurityViolations.setStatus("current")
_CGtpHistUnsupportedExtHdr_Type = Counter32
_CGtpHistUnsupportedExtHdr_Object = MibTableColumn
cGtpHistUnsupportedExtHdr = _CGtpHistUnsupportedExtHdr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 16),
    _CGtpHistUnsupportedExtHdr_Type()
)
cGtpHistUnsupportedExtHdr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistUnsupportedExtHdr.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistUnsupportedExtHdr.setUnits("pdps")
_CGtpHistPathFailures_Type = Counter32
_CGtpHistPathFailures_Object = MibTableColumn
cGtpHistPathFailures = _CGtpHistPathFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 17),
    _CGtpHistPathFailures_Type()
)
cGtpHistPathFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistPathFailures.setStatus("current")
_CGtpHistTotalDropped_Type = Counter32
_CGtpHistTotalDropped_Object = MibTableColumn
cGtpHistTotalDropped = _CGtpHistTotalDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 18),
    _CGtpHistTotalDropped_Type()
)
cGtpHistTotalDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistTotalDropped.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistTotalDropped.setUnits("packets")
_CGtpHistDroppedSigMsgs_Type = Counter32
_CGtpHistDroppedSigMsgs_Object = MibTableColumn
cGtpHistDroppedSigMsgs = _CGtpHistDroppedSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 19),
    _CGtpHistDroppedSigMsgs_Type()
)
cGtpHistDroppedSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistDroppedSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistDroppedSigMsgs.setUnits("messages")
_CGtpHistRcvdSigMsgs_Type = Counter32
_CGtpHistRcvdSigMsgs_Object = MibTableColumn
cGtpHistRcvdSigMsgs = _CGtpHistRcvdSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 20),
    _CGtpHistRcvdSigMsgs_Type()
)
cGtpHistRcvdSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRcvdSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistRcvdSigMsgs.setUnits("messages")
_CGtpHistSentSigMsgs_Type = Counter32
_CGtpHistSentSigMsgs_Object = MibTableColumn
cGtpHistSentSigMsgs = _CGtpHistSentSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 21),
    _CGtpHistSentSigMsgs_Type()
)
cGtpHistSentSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistSentSigMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistSentSigMsgs.setUnits("messages")
_CGtpHistTotalCreatedPDPs_Type = Counter32
_CGtpHistTotalCreatedPDPs_Object = MibTableColumn
cGtpHistTotalCreatedPDPs = _CGtpHistTotalCreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 22),
    _CGtpHistTotalCreatedPDPs_Type()
)
cGtpHistTotalCreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistTotalCreatedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistTotalCreatedPDPs.setUnits("pdps")
_CGtpHistTotalDeletedPDPs_Type = Counter32
_CGtpHistTotalDeletedPDPs_Object = MibTableColumn
cGtpHistTotalDeletedPDPs = _CGtpHistTotalDeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 23),
    _CGtpHistTotalDeletedPDPs_Type()
)
cGtpHistTotalDeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistTotalDeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistTotalDeletedPDPs.setUnits("pdps")
_CGtpHistTotalCreatedPppPDPs_Type = Counter32
_CGtpHistTotalCreatedPppPDPs_Object = MibTableColumn
cGtpHistTotalCreatedPppPDPs = _CGtpHistTotalCreatedPppPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 24),
    _CGtpHistTotalCreatedPppPDPs_Type()
)
cGtpHistTotalCreatedPppPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistTotalCreatedPppPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistTotalCreatedPppPDPs.setUnits("pdps")
_CGtpHistTotalDeletedPppPDPs_Type = Counter32
_CGtpHistTotalDeletedPppPDPs_Object = MibTableColumn
cGtpHistTotalDeletedPppPDPs = _CGtpHistTotalDeletedPppPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 25),
    _CGtpHistTotalDeletedPppPDPs_Type()
)
cGtpHistTotalDeletedPppPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistTotalDeletedPppPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistTotalDeletedPppPDPs.setUnits("pdps")
_CGtpHistSinglePDPSessCleared_Type = Counter32
_CGtpHistSinglePDPSessCleared_Object = MibTableColumn
cGtpHistSinglePDPSessCleared = _CGtpHistSinglePDPSessCleared_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 26),
    _CGtpHistSinglePDPSessCleared_Type()
)
cGtpHistSinglePDPSessCleared.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistSinglePDPSessCleared.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistSinglePDPSessCleared.setUnits("pdps")
_CGtpHistPathFailLocalDelPDPs_Type = Counter32
_CGtpHistPathFailLocalDelPDPs_Object = MibTableColumn
cGtpHistPathFailLocalDelPDPs = _CGtpHistPathFailLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 27),
    _CGtpHistPathFailLocalDelPDPs_Type()
)
cGtpHistPathFailLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistPathFailLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistPathFailLocalDelPDPs.setUnits("pdps")
_CGtpHistVerUpgradeLocalDel_Type = Counter32
_CGtpHistVerUpgradeLocalDel_Object = MibTableColumn
cGtpHistVerUpgradeLocalDel = _CGtpHistVerUpgradeLocalDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 28),
    _CGtpHistVerUpgradeLocalDel_Type()
)
cGtpHistVerUpgradeLocalDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistVerUpgradeLocalDel.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistVerUpgradeLocalDel.setUnits("pdps")
_CGtpHistNoSgsnLocalDelPDPs_Type = Counter32
_CGtpHistNoSgsnLocalDelPDPs_Object = MibTableColumn
cGtpHistNoSgsnLocalDelPDPs = _CGtpHistNoSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 29),
    _CGtpHistNoSgsnLocalDelPDPs_Type()
)
cGtpHistNoSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistNoSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistNoSgsnLocalDelPDPs.setUnits("pdps")
_CGtpHistVerFallbackLocalDel_Type = Counter32
_CGtpHistVerFallbackLocalDel_Object = MibTableColumn
cGtpHistVerFallbackLocalDel = _CGtpHistVerFallbackLocalDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 30),
    _CGtpHistVerFallbackLocalDel_Type()
)
cGtpHistVerFallbackLocalDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistVerFallbackLocalDel.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistVerFallbackLocalDel.setUnits("pdps")
_CGtpHistCreateCollideWithDel_Type = Counter32
_CGtpHistCreateCollideWithDel_Object = MibTableColumn
cGtpHistCreateCollideWithDel = _CGtpHistCreateCollideWithDel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 31),
    _CGtpHistCreateCollideWithDel_Type()
)
cGtpHistCreateCollideWithDel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistCreateCollideWithDel.setStatus("current")
_CGtpHistVersionChanges_Type = Counter32
_CGtpHistVersionChanges_Object = MibTableColumn
cGtpHistVersionChanges = _CGtpHistVersionChanges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 32),
    _CGtpHistVersionChanges_Type()
)
cGtpHistVersionChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistVersionChanges.setStatus("current")
_CGtpHistRetransCreatePDPReqs_Type = Counter32
_CGtpHistRetransCreatePDPReqs_Object = MibTableColumn
cGtpHistRetransCreatePDPReqs = _CGtpHistRetransCreatePDPReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 33),
    _CGtpHistRetransCreatePDPReqs_Type()
)
cGtpHistRetransCreatePDPReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRetransCreatePDPReqs.setStatus("current")
_CGtpHistCreateAsUpdate_Type = Counter32
_CGtpHistCreateAsUpdate_Object = MibTableColumn
cGtpHistCreateAsUpdate = _CGtpHistCreateAsUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 34),
    _CGtpHistCreateAsUpdate_Type()
)
cGtpHistCreateAsUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistCreateAsUpdate.setStatus("current")
_CGtpHistIpv6PdpActRejects_Type = Counter32
_CGtpHistIpv6PdpActRejects_Object = MibTableColumn
cGtpHistIpv6PdpActRejects = _CGtpHistIpv6PdpActRejects_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 35),
    _CGtpHistIpv6PdpActRejects_Type()
)
cGtpHistIpv6PdpActRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6PdpActRejects.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6PdpActRejects.setUnits("pdps")
_CGtpHistIpv6CreatedPDPs_Type = Counter32
_CGtpHistIpv6CreatedPDPs_Object = MibTableColumn
cGtpHistIpv6CreatedPDPs = _CGtpHistIpv6CreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 36),
    _CGtpHistIpv6CreatedPDPs_Type()
)
cGtpHistIpv6CreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6CreatedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6CreatedPDPs.setUnits("pdps")
_CGtpHistIpv6DeletedPDPs_Type = Counter32
_CGtpHistIpv6DeletedPDPs_Object = MibTableColumn
cGtpHistIpv6DeletedPDPs = _CGtpHistIpv6DeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 37),
    _CGtpHistIpv6DeletedPDPs_Type()
)
cGtpHistIpv6DeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6DeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6DeletedPDPs.setUnits("pdps")
_CGtpHistIpv6RcvdSigMsgs_Type = Counter32
_CGtpHistIpv6RcvdSigMsgs_Object = MibTableColumn
cGtpHistIpv6RcvdSigMsgs = _CGtpHistIpv6RcvdSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 38),
    _CGtpHistIpv6RcvdSigMsgs_Type()
)
cGtpHistIpv6RcvdSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6RcvdSigMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGtpHistIpv6RcvdSigMsgs.setUnits("messages")
_CGtpHistIpv6SentSigMsgs_Type = Counter32
_CGtpHistIpv6SentSigMsgs_Object = MibTableColumn
cGtpHistIpv6SentSigMsgs = _CGtpHistIpv6SentSigMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 39),
    _CGtpHistIpv6SentSigMsgs_Type()
)
cGtpHistIpv6SentSigMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6SentSigMsgs.setStatus("deprecated")
if mibBuilder.loadTexts:
    cGtpHistIpv6SentSigMsgs.setUnits("messages")
_CGtpHistIpv6RcvdPDUs_Type = Counter32
_CGtpHistIpv6RcvdPDUs_Object = MibTableColumn
cGtpHistIpv6RcvdPDUs = _CGtpHistIpv6RcvdPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 40),
    _CGtpHistIpv6RcvdPDUs_Type()
)
cGtpHistIpv6RcvdPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6RcvdPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6RcvdPDUs.setUnits("messages")
_CGtpHistIpv6SentPDUs_Type = Counter32
_CGtpHistIpv6SentPDUs_Object = MibTableColumn
cGtpHistIpv6SentPDUs = _CGtpHistIpv6SentPDUs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 41),
    _CGtpHistIpv6SentPDUs_Type()
)
cGtpHistIpv6SentPDUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6SentPDUs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6SentPDUs.setUnits("messages")
_CGtpHistIpv6RcvdOctets_Type = Counter64
_CGtpHistIpv6RcvdOctets_Object = MibTableColumn
cGtpHistIpv6RcvdOctets = _CGtpHistIpv6RcvdOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 42),
    _CGtpHistIpv6RcvdOctets_Type()
)
cGtpHistIpv6RcvdOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6RcvdOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6RcvdOctets.setUnits("bytes")
_CGtpHistIpv6SentOctets_Type = Counter64
_CGtpHistIpv6SentOctets_Object = MibTableColumn
cGtpHistIpv6SentOctets = _CGtpHistIpv6SentOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 43),
    _CGtpHistIpv6SentOctets_Type()
)
cGtpHistIpv6SentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv6SentOctets.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistIpv6SentOctets.setUnits("bytes")
_CGtpHistNoWaitSgsnLocalDelPDPs_Type = Counter32
_CGtpHistNoWaitSgsnLocalDelPDPs_Object = MibTableColumn
cGtpHistNoWaitSgsnLocalDelPDPs = _CGtpHistNoWaitSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 44),
    _CGtpHistNoWaitSgsnLocalDelPDPs_Type()
)
cGtpHistNoWaitSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistNoWaitSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistNoWaitSgsnLocalDelPDPs.setUnits("pdps")
_CGtpHistNoReqSgsnLocalDelPDPs_Type = Counter32
_CGtpHistNoReqSgsnLocalDelPDPs_Object = MibTableColumn
cGtpHistNoReqSgsnLocalDelPDPs = _CGtpHistNoReqSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 45),
    _CGtpHistNoReqSgsnLocalDelPDPs_Type()
)
cGtpHistNoReqSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistNoReqSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistNoReqSgsnLocalDelPDPs.setUnits("pdps")
_CGtpHistRoamingTrustedPDPs_Type = Counter32
_CGtpHistRoamingTrustedPDPs_Object = MibTableColumn
cGtpHistRoamingTrustedPDPs = _CGtpHistRoamingTrustedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 46),
    _CGtpHistRoamingTrustedPDPs_Type()
)
cGtpHistRoamingTrustedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRoamingTrustedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistRoamingTrustedPDPs.setUnits("pdps")
_CGtpHistRoamingNonTrustedPDPs_Type = Counter32
_CGtpHistRoamingNonTrustedPDPs_Object = MibTableColumn
cGtpHistRoamingNonTrustedPDPs = _CGtpHistRoamingNonTrustedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 47),
    _CGtpHistRoamingNonTrustedPDPs_Type()
)
cGtpHistRoamingNonTrustedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRoamingNonTrustedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistRoamingNonTrustedPDPs.setUnits("pdps")
_CGtpHistNonRoamingPDPs_Type = Counter32
_CGtpHistNonRoamingPDPs_Object = MibTableColumn
cGtpHistNonRoamingPDPs = _CGtpHistNonRoamingPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 48),
    _CGtpHistNonRoamingPDPs_Type()
)
cGtpHistNonRoamingPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistNonRoamingPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistNonRoamingPDPs.setUnits("pdps")
_CGtpHistSentPdpUpdateReqs_Type = Counter32
_CGtpHistSentPdpUpdateReqs_Object = MibTableColumn
cGtpHistSentPdpUpdateReqs = _CGtpHistSentPdpUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 49),
    _CGtpHistSentPdpUpdateReqs_Type()
)
cGtpHistSentPdpUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistSentPdpUpdateReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistSentPdpUpdateReqs.setUnits("messages")
_CGtpHistRcvdPdpUpdateResponses_Type = Counter32
_CGtpHistRcvdPdpUpdateResponses_Object = MibTableColumn
cGtpHistRcvdPdpUpdateResponses = _CGtpHistRcvdPdpUpdateResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 50),
    _CGtpHistRcvdPdpUpdateResponses_Type()
)
cGtpHistRcvdPdpUpdateResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRcvdPdpUpdateResponses.setStatus("current")
if mibBuilder.loadTexts:
    cGtpHistRcvdPdpUpdateResponses.setUnits("messages")
_CGtpHistTotalDtEnabled_Type = Counter32
_CGtpHistTotalDtEnabled_Object = MibTableColumn
cGtpHistTotalDtEnabled = _CGtpHistTotalDtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 51),
    _CGtpHistTotalDtEnabled_Type()
)
cGtpHistTotalDtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistTotalDtEnabled.setStatus("current")
_CGtpHistRemoteNode_Type = CGtpEntities
_CGtpHistRemoteNode_Object = MibTableColumn
cGtpHistRemoteNode = _CGtpHistRemoteNode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 52),
    _CGtpHistRemoteNode_Type()
)
cGtpHistRemoteNode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistRemoteNode.setStatus("current")
_CGtpHistIpv4v6CreatedPDPs_Type = Counter32
_CGtpHistIpv4v6CreatedPDPs_Object = MibTableColumn
cGtpHistIpv4v6CreatedPDPs = _CGtpHistIpv4v6CreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 53),
    _CGtpHistIpv4v6CreatedPDPs_Type()
)
cGtpHistIpv4v6CreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv4v6CreatedPDPs.setStatus("current")
_CGtpHistIpv4v6DeletedPDPs_Type = Counter32
_CGtpHistIpv4v6DeletedPDPs_Object = MibTableColumn
cGtpHistIpv4v6DeletedPDPs = _CGtpHistIpv4v6DeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 5, 1, 54),
    _CGtpHistIpv4v6DeletedPDPs_Type()
)
cGtpHistIpv4v6DeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpHistIpv4v6DeletedPDPs.setStatus("current")
_CGtpNetworkBehindMsApns_Type = Counter32
_CGtpNetworkBehindMsApns_Object = MibScalar
cGtpNetworkBehindMsApns = _CGtpNetworkBehindMsApns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 6),
    _CGtpNetworkBehindMsApns_Type()
)
cGtpNetworkBehindMsApns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpNetworkBehindMsApns.setStatus("current")
if mibBuilder.loadTexts:
    cGtpNetworkBehindMsApns.setUnits("APN")
_CGtpTotalDownldFramedRout_Type = Counter32
_CGtpTotalDownldFramedRout_Object = MibScalar
cGtpTotalDownldFramedRout = _CGtpTotalDownldFramedRout_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 7),
    _CGtpTotalDownldFramedRout_Type()
)
cGtpTotalDownldFramedRout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRout.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRout.setUnits("messages")
_CGtpTotalDownldFramedRoutSavedFail_Type = Counter32
_CGtpTotalDownldFramedRoutSavedFail_Object = MibScalar
cGtpTotalDownldFramedRoutSavedFail = _CGtpTotalDownldFramedRoutSavedFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 8),
    _CGtpTotalDownldFramedRoutSavedFail_Type()
)
cGtpTotalDownldFramedRoutSavedFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutSavedFail.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutSavedFail.setUnits("messages")
_CGtpTotalDownldFramedRoutInsFail_Type = Counter32
_CGtpTotalDownldFramedRoutInsFail_Object = MibScalar
cGtpTotalDownldFramedRoutInsFail = _CGtpTotalDownldFramedRoutInsFail_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 9),
    _CGtpTotalDownldFramedRoutInsFail_Type()
)
cGtpTotalDownldFramedRoutInsFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutInsFail.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutInsFail.setUnits("messages")
_CGtpTotalDownldFramedRoutIns_Type = Counter32
_CGtpTotalDownldFramedRoutIns_Object = MibScalar
cGtpTotalDownldFramedRoutIns = _CGtpTotalDownldFramedRoutIns_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 10),
    _CGtpTotalDownldFramedRoutIns_Type()
)
cGtpTotalDownldFramedRoutIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutIns.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutIns.setUnits("messages")
_CGtpTotalDownldFramedRoutDeleted_Type = Counter32
_CGtpTotalDownldFramedRoutDeleted_Object = MibScalar
cGtpTotalDownldFramedRoutDeleted = _CGtpTotalDownldFramedRoutDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 11),
    _CGtpTotalDownldFramedRoutDeleted_Type()
)
cGtpTotalDownldFramedRoutDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutDeleted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDownldFramedRoutDeleted.setUnits("messages")
_CGtpTotalv0v1SigMsgDropped_Type = Counter32
_CGtpTotalv0v1SigMsgDropped_Object = MibScalar
cGtpTotalv0v1SigMsgDropped = _CGtpTotalv0v1SigMsgDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 12),
    _CGtpTotalv0v1SigMsgDropped_Type()
)
cGtpTotalv0v1SigMsgDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalv0v1SigMsgDropped.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalv0v1SigMsgDropped.setUnits("packets")
_CGtpTotalDataMsgDropped_Type = Counter32
_CGtpTotalDataMsgDropped_Object = MibScalar
cGtpTotalDataMsgDropped = _CGtpTotalDataMsgDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 13),
    _CGtpTotalDataMsgDropped_Type()
)
cGtpTotalDataMsgDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDataMsgDropped.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDataMsgDropped.setUnits("packets")
_CGtpv0PathCreated_Type = Counter32
_CGtpv0PathCreated_Object = MibScalar
cGtpv0PathCreated = _CGtpv0PathCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 14),
    _CGtpv0PathCreated_Type()
)
cGtpv0PathCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv0PathCreated.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv0PathCreated.setUnits("paths")
_CGtpv0PathDeleted_Type = Counter32
_CGtpv0PathDeleted_Object = MibScalar
cGtpv0PathDeleted = _CGtpv0PathDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 15),
    _CGtpv0PathDeleted_Type()
)
cGtpv0PathDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv0PathDeleted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv0PathDeleted.setUnits("paths")
_CGtpv0PathRestarted_Type = Counter32
_CGtpv0PathRestarted_Object = MibScalar
cGtpv0PathRestarted = _CGtpv0PathRestarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 16),
    _CGtpv0PathRestarted_Type()
)
cGtpv0PathRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv0PathRestarted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv0PathRestarted.setUnits("paths")
_CGtpv1SigPathCreated_Type = Counter32
_CGtpv1SigPathCreated_Object = MibScalar
cGtpv1SigPathCreated = _CGtpv1SigPathCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 17),
    _CGtpv1SigPathCreated_Type()
)
cGtpv1SigPathCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv1SigPathCreated.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv1SigPathCreated.setUnits("paths")
_CGtpv1SigPathDeleted_Type = Counter32
_CGtpv1SigPathDeleted_Object = MibScalar
cGtpv1SigPathDeleted = _CGtpv1SigPathDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 18),
    _CGtpv1SigPathDeleted_Type()
)
cGtpv1SigPathDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv1SigPathDeleted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv1SigPathDeleted.setUnits("paths")
_CGtpv1SigPathRestarted_Type = Counter32
_CGtpv1SigPathRestarted_Object = MibScalar
cGtpv1SigPathRestarted = _CGtpv1SigPathRestarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 19),
    _CGtpv1SigPathRestarted_Type()
)
cGtpv1SigPathRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv1SigPathRestarted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv1SigPathRestarted.setUnits("paths")
_CGtpv1DataPathCreated_Type = Counter32
_CGtpv1DataPathCreated_Object = MibScalar
cGtpv1DataPathCreated = _CGtpv1DataPathCreated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 20),
    _CGtpv1DataPathCreated_Type()
)
cGtpv1DataPathCreated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv1DataPathCreated.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv1DataPathCreated.setUnits("paths")
_CGtpv1DataPathDeleted_Type = Counter32
_CGtpv1DataPathDeleted_Object = MibScalar
cGtpv1DataPathDeleted = _CGtpv1DataPathDeleted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 21),
    _CGtpv1DataPathDeleted_Type()
)
cGtpv1DataPathDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv1DataPathDeleted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv1DataPathDeleted.setUnits("paths")
_CGtpv1DataPathRestarted_Type = Counter32
_CGtpv1DataPathRestarted_Object = MibScalar
cGtpv1DataPathRestarted = _CGtpv1DataPathRestarted_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 22),
    _CGtpv1DataPathRestarted_Type()
)
cGtpv1DataPathRestarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpv1DataPathRestarted.setStatus("current")
if mibBuilder.loadTexts:
    cGtpv1DataPathRestarted.setUnits("paths")
_CGtpTotalDownlinkQosFailures_Type = Counter32
_CGtpTotalDownlinkQosFailures_Object = MibScalar
cGtpTotalDownlinkQosFailures = _CGtpTotalDownlinkQosFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 23),
    _CGtpTotalDownlinkQosFailures_Type()
)
cGtpTotalDownlinkQosFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalDownlinkQosFailures.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalDownlinkQosFailures.setUnits("packets")
_CGtpTotalUplinkQosFailures_Type = Counter32
_CGtpTotalUplinkQosFailures_Object = MibScalar
cGtpTotalUplinkQosFailures = _CGtpTotalUplinkQosFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 1, 3, 24),
    _CGtpTotalUplinkQosFailures_Type()
)
cGtpTotalUplinkQosFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGtpTotalUplinkQosFailures.setStatus("current")
if mibBuilder.loadTexts:
    cGtpTotalUplinkQosFailures.setUnits("packets")
_CGtpNotifPrefix_ObjectIdentity = ObjectIdentity
cGtpNotifPrefix = _CGtpNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 2)
)
_CGtpNotifications_ObjectIdentity = ObjectIdentity
cGtpNotifications = _CGtpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 2, 0)
)
_CGtpMIBConformances_ObjectIdentity = ObjectIdentity
cGtpMIBConformances = _CGtpMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3)
)
_CGtpMIBCompliances_ObjectIdentity = ObjectIdentity
cGtpMIBCompliances = _CGtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1)
)
_CGtpMIBGroups_ObjectIdentity = ObjectIdentity
cGtpMIBGroups = _CGtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2)
)

# Managed Objects groups

cGtpConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 1)
)
cGtpConfigurationsGroup.setObjects(
      *(("CISCO-GTP-MIB", "cGtpGSNService"),
        ("CISCO-GTP-MIB", "cGtpVersion"),
        ("CISCO-GTP-MIB", "cGtpT3TunnelTimer"),
        ("CISCO-GTP-MIB", "cGtpT3ResponseTimer"),
        ("CISCO-GTP-MIB", "cGtpN3Request"),
        ("CISCO-GTP-MIB", "cGtpN3BufferSize"),
        ("CISCO-GTP-MIB", "cGtpEchoRequestTimer"),
        ("CISCO-GTP-MIB", "cGtpGSNTotalBandwidthResrc"),
        ("CISCO-GTP-MIB", "cGtpMaximumPdps"),
        ("CISCO-GTP-MIB", "cGtpNotifEnable"))
)
if mibBuilder.loadTexts:
    cGtpConfigurationsGroup.setStatus("obsolete")

cGtpStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 2)
)
cGtpStatusGroup.setObjects(
      *(("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddrTyp"),
        ("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddr"),
        ("CISCO-GTP-MIB", "cGtpPremiumQosMeanThroughput"),
        ("CISCO-GTP-MIB", "cGtpNormalQosMeanThroughput"),
        ("CISCO-GTP-MIB", "cGtpBestEffortQosMeanThroughput"),
        ("CISCO-GTP-MIB", "cGtpGSNAddress"))
)
if mibBuilder.loadTexts:
    cGtpStatusGroup.setStatus("obsolete")

cGtpStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 3)
)
cGtpStatisticsGroup.setObjects(
      *(("CISCO-GTP-MIB", "cGtpPathFailureOccurrences"),
        ("CISCO-GTP-MIB", "cGtpCurrentUsedBandwidth"),
        ("CISCO-GTP-MIB", "cGtpTotalDroppedPackets"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroup.setStatus("obsolete")

cGtpConfigurationsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 4)
)
cGtpConfigurationsGroupRev1.setObjects(
      *(("CISCO-GTP-MIB", "cGtpGSNService"),
        ("CISCO-GTP-MIB", "cGtpVersion"),
        ("CISCO-GTP-MIB", "cGtpT3TunnelTimer"),
        ("CISCO-GTP-MIB", "cGtpT3ResponseTimer"),
        ("CISCO-GTP-MIB", "cGtpN3Request"),
        ("CISCO-GTP-MIB", "cGtpN3BufferSize"),
        ("CISCO-GTP-MIB", "cGtpEchoRequestTimerEnable"),
        ("CISCO-GTP-MIB", "cGtpEchoRequestTimer"),
        ("CISCO-GTP-MIB", "cGtpMaximumPdps"),
        ("CISCO-GTP-MIB", "cGtpNotifEnable"),
        ("CISCO-GTP-MIB", "cGtpDynamicEchoTimerEnable"),
        ("CISCO-GTP-MIB", "cGtpDynamicEchoTimerMinTime"),
        ("CISCO-GTP-MIB", "cGtpDynamicEchoTimerSmoothFactor"))
)
if mibBuilder.loadTexts:
    cGtpConfigurationsGroupRev1.setStatus("obsolete")

cGtpStatusGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 5)
)
cGtpStatusGroupRev1.setObjects(
      *(("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddrTyp"),
        ("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddr"),
        ("CISCO-GTP-MIB", "cGtpGSNAddress"))
)
if mibBuilder.loadTexts:
    cGtpStatusGroupRev1.setStatus("obsolete")

cGtpStatisticsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 6)
)
cGtpStatisticsGroupRev1.setObjects(
      *(("CISCO-GTP-MIB", "cGtpPathFailureOccurrences"),
        ("CISCO-GTP-MIB", "cGtpTotalDroppedPackets"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupRev1.setStatus("current")

cGtpConfigurationsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 8)
)
cGtpConfigurationsGroupRev2.setObjects(
      *(("CISCO-GTP-MIB", "cGtpGSNService"),
        ("CISCO-GTP-MIB", "cGtpVersion"),
        ("CISCO-GTP-MIB", "cGtpT3ResponseTimer"),
        ("CISCO-GTP-MIB", "cGtpN3Request"),
        ("CISCO-GTP-MIB", "cGtpN3BufferSize"),
        ("CISCO-GTP-MIB", "cGtpEchoRequestTimerEnable"),
        ("CISCO-GTP-MIB", "cGtpEchoRequestTimer"),
        ("CISCO-GTP-MIB", "cGtpMaximumPdps"),
        ("CISCO-GTP-MIB", "cGtpNotifEnable"),
        ("CISCO-GTP-MIB", "cGtpDynamicEchoTimerEnable"),
        ("CISCO-GTP-MIB", "cGtpDynamicEchoTimerMinTime"),
        ("CISCO-GTP-MIB", "cGtpDynamicEchoTimerSmoothFactor"))
)
if mibBuilder.loadTexts:
    cGtpConfigurationsGroupRev2.setStatus("current")

cGtpStatusGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 9)
)
cGtpStatusGroupRev2.setObjects(
      *(("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddrTyp"),
        ("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddr"),
        ("CISCO-GTP-MIB", "cGtpGSNAddress"),
        ("CISCO-GTP-MIB", "cGtpGSNVersion"))
)
if mibBuilder.loadTexts:
    cGtpStatusGroupRev2.setStatus("deprecated")

cGtpStatusGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 11)
)
cGtpStatusGroupRev3.setObjects(
      *(("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddrTyp"),
        ("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddr"),
        ("CISCO-GTP-MIB", "cGtpPathVersion"))
)
if mibBuilder.loadTexts:
    cGtpStatusGroupRev3.setStatus("current")

cGtpStatisticsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 12)
)
cGtpStatisticsGroupSup1.setObjects(
      *(("CISCO-GTP-MIB", "cGtpUnexpectedMsgs"),
        ("CISCO-GTP-MIB", "cGtpDroppedDataMsgs"),
        ("CISCO-GTP-MIB", "cGtpRcvdPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpSentPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpRcvdPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpSentPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpMsgTooShort"),
        ("CISCO-GTP-MIB", "cGtpUnknownMsgs"),
        ("CISCO-GTP-MIB", "cGtpUnexpectedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpRoamingPDUs"),
        ("CISCO-GTP-MIB", "cGtpSecurityViolations"),
        ("CISCO-GTP-MIB", "cGtpUnsupportedExtHdr"),
        ("CISCO-GTP-MIB", "cGtpPathFailures"),
        ("CISCO-GTP-MIB", "cGtpTotalDropped"),
        ("CISCO-GTP-MIB", "cGtpDroppedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpRcvdSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpSentSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpTotalCreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpTotalDeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpTotalCreatedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpTotalDeletedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpSinglePDPSessCleared"),
        ("CISCO-GTP-MIB", "cGtpPathFailLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpVerUpgradeLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpNoSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpVerFallbackLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpCreateCollideWithDel"),
        ("CISCO-GTP-MIB", "cGtpVersionChanges"),
        ("CISCO-GTP-MIB", "cGtpRetransCreatePDPReqs"),
        ("CISCO-GTP-MIB", "cGtpCreateAsUpdate"),
        ("CISCO-GTP-MIB", "cGtpIpv6PdpActRejects"),
        ("CISCO-GTP-MIB", "cGtpIpv6CreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpIpv6DeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpIpv6RcvdSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpIpv6SentSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpIpv6RcvdPDUs"),
        ("CISCO-GTP-MIB", "cGtpIpv6SentPDUs"),
        ("CISCO-GTP-MIB", "cGtpIpv6RcvdOctets"),
        ("CISCO-GTP-MIB", "cGtpIpv6SentOctets"),
        ("CISCO-GTP-MIB", "cGtpHistUnexpectedMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistDroppedDataMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistSentPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpHistSentPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpHistMsgTooShort"),
        ("CISCO-GTP-MIB", "cGtpHistUnknownMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistUnexpectedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRoamingPDUs"),
        ("CISCO-GTP-MIB", "cGtpHistSecurityViolations"),
        ("CISCO-GTP-MIB", "cGtpHistUnsupportedExtHdr"),
        ("CISCO-GTP-MIB", "cGtpHistPathFailures"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDropped"),
        ("CISCO-GTP-MIB", "cGtpHistDroppedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistSentSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalCreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalCreatedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDeletedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistSinglePDPSessCleared"),
        ("CISCO-GTP-MIB", "cGtpHistPathFailLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistVerUpgradeLocalDel"),
        ("CISCO-GTP-MIB", "cGtpHistNoSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistVerFallbackLocalDel"),
        ("CISCO-GTP-MIB", "cGtpHistCreateCollideWithDel"),
        ("CISCO-GTP-MIB", "cGtpHistVersionChanges"),
        ("CISCO-GTP-MIB", "cGtpHistRetransCreatePDPReqs"),
        ("CISCO-GTP-MIB", "cGtpHistCreateAsUpdate"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6PdpActRejects"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6CreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6DeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6RcvdSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6SentSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6RcvdPDUs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6SentPDUs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6RcvdOctets"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6SentOctets"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupSup1.setStatus("deprecated")

cGtpConfigurationsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 13)
)
cGtpConfigurationsGroupSup1.setObjects(
    ("CISCO-GTP-MIB", "cGtpPathHistoryLimit")
)
if mibBuilder.loadTexts:
    cGtpConfigurationsGroupSup1.setStatus("deprecated")

cGtpConfigurationsGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 14)
)
cGtpConfigurationsGroupSup2.setObjects(
      *(("CISCO-GTP-MIB", "cGtpPathHistoryLimit"),
        ("CISCO-GTP-MIB", "cGtpUpdateFailDelete"))
)
if mibBuilder.loadTexts:
    cGtpConfigurationsGroupSup2.setStatus("current")

cGtpStatisticsGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 15)
)
cGtpStatisticsGroupSup2.setObjects(
      *(("CISCO-GTP-MIB", "cGtpUnexpectedMsgs"),
        ("CISCO-GTP-MIB", "cGtpDroppedDataMsgs"),
        ("CISCO-GTP-MIB", "cGtpRcvdPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpSentPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpRcvdPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpSentPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpMsgTooShort"),
        ("CISCO-GTP-MIB", "cGtpUnknownMsgs"),
        ("CISCO-GTP-MIB", "cGtpUnexpectedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpSecurityViolations"),
        ("CISCO-GTP-MIB", "cGtpUnsupportedExtHdr"),
        ("CISCO-GTP-MIB", "cGtpPathFailures"),
        ("CISCO-GTP-MIB", "cGtpTotalDropped"),
        ("CISCO-GTP-MIB", "cGtpDroppedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpRcvdSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpSentSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpTotalCreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpTotalDeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpTotalCreatedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpTotalDeletedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpSinglePDPSessCleared"),
        ("CISCO-GTP-MIB", "cGtpPathFailLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpVerUpgradeLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpNoSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpVerFallbackLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpCreateCollideWithDel"),
        ("CISCO-GTP-MIB", "cGtpVersionChanges"),
        ("CISCO-GTP-MIB", "cGtpRetransCreatePDPReqs"),
        ("CISCO-GTP-MIB", "cGtpCreateAsUpdate"),
        ("CISCO-GTP-MIB", "cGtpIpv6PdpActRejects"),
        ("CISCO-GTP-MIB", "cGtpIpv6CreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpIpv6DeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpIpv6RcvdPDUs"),
        ("CISCO-GTP-MIB", "cGtpIpv6SentPDUs"),
        ("CISCO-GTP-MIB", "cGtpIpv6RcvdOctets"),
        ("CISCO-GTP-MIB", "cGtpIpv6SentOctets"),
        ("CISCO-GTP-MIB", "cGtpNoWaitSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpNoReqSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpRoamingTrustedPDPs"),
        ("CISCO-GTP-MIB", "cGtpRoamingNonTrustedPDPs"),
        ("CISCO-GTP-MIB", "cGtpNonRoamingPDPs"),
        ("CISCO-GTP-MIB", "cGtpSentPdpUpdateReqs"),
        ("CISCO-GTP-MIB", "cGtpRcvdPdpUpdateResponses"),
        ("CISCO-GTP-MIB", "cGtpTotalDtEnabled"),
        ("CISCO-GTP-MIB", "cGtpHistUnexpectedMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistDroppedDataMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistSentPDUMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpHistSentPDUOctets"),
        ("CISCO-GTP-MIB", "cGtpHistMsgTooShort"),
        ("CISCO-GTP-MIB", "cGtpHistUnknownMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistUnexpectedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistSecurityViolations"),
        ("CISCO-GTP-MIB", "cGtpHistUnsupportedExtHdr"),
        ("CISCO-GTP-MIB", "cGtpHistPathFailures"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDropped"),
        ("CISCO-GTP-MIB", "cGtpHistDroppedSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistSentSigMsgs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalCreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalCreatedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDeletedPppPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistSinglePDPSessCleared"),
        ("CISCO-GTP-MIB", "cGtpHistPathFailLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistVerUpgradeLocalDel"),
        ("CISCO-GTP-MIB", "cGtpHistNoSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistVerFallbackLocalDel"),
        ("CISCO-GTP-MIB", "cGtpHistCreateCollideWithDel"),
        ("CISCO-GTP-MIB", "cGtpHistVersionChanges"),
        ("CISCO-GTP-MIB", "cGtpHistRetransCreatePDPReqs"),
        ("CISCO-GTP-MIB", "cGtpHistCreateAsUpdate"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6PdpActRejects"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6CreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6DeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6RcvdPDUs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6SentPDUs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6RcvdOctets"),
        ("CISCO-GTP-MIB", "cGtpHistIpv6SentOctets"),
        ("CISCO-GTP-MIB", "cGtpHistNoWaitSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistNoReqSgsnLocalDelPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistRoamingTrustedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistRoamingNonTrustedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistNonRoamingPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistSentPdpUpdateReqs"),
        ("CISCO-GTP-MIB", "cGtpHistRcvdPdpUpdateResponses"),
        ("CISCO-GTP-MIB", "cGtpHistTotalDtEnabled"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupSup2.setStatus("current")

cGtpConfigurationsGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 16)
)
cGtpConfigurationsGroupSup3.setObjects(
      *(("CISCO-GTP-MIB", "cGtpSgsnProfileIpAddressType"),
        ("CISCO-GTP-MIB", "cGtpSgsnProfileStartIpAddress"),
        ("CISCO-GTP-MIB", "cGtpSgsnProfileEndIpAddress"),
        ("CISCO-GTP-MIB", "cGtpSgsnProfilePortNumber"),
        ("CISCO-GTP-MIB", "cGtpSgsnProfileEchoDisable"),
        ("CISCO-GTP-MIB", "cGtpSgsnProfileStorageType"),
        ("CISCO-GTP-MIB", "cGtpSgsnProfileRowStatus"))
)
if mibBuilder.loadTexts:
    cGtpConfigurationsGroupSup3.setStatus("current")

cGtpStatusGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 17)
)
cGtpStatusGroupSup1.setObjects(
      *(("CISCO-GTP-MIB", "cGtpPathRemoteNode"),
        ("CISCO-GTP-MIB", "cGtpPathVrfName"))
)
if mibBuilder.loadTexts:
    cGtpStatusGroupSup1.setStatus("current")

cGtpStatisticsGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 18)
)
cGtpStatisticsGroupSup3.setObjects(
      *(("CISCO-GTP-MIB", "cGtpHistRemoteNode"),
        ("CISCO-GTP-MIB", "cGtpIpv4v6CreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpIpv4v6DeletedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv4v6CreatedPDPs"),
        ("CISCO-GTP-MIB", "cGtpHistIpv4v6DeletedPDPs"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupSup3.setStatus("current")

cGtpStatisticsGroupSup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 19)
)
cGtpStatisticsGroupSup4.setObjects(
      *(("CISCO-GTP-MIB", "cGtpNetworkBehindMsApns"),
        ("CISCO-GTP-MIB", "cGtpTotalDownldFramedRout"),
        ("CISCO-GTP-MIB", "cGtpTotalDownldFramedRoutSavedFail"),
        ("CISCO-GTP-MIB", "cGtpTotalDownldFramedRoutInsFail"),
        ("CISCO-GTP-MIB", "cGtpTotalDownldFramedRoutIns"),
        ("CISCO-GTP-MIB", "cGtpTotalDownldFramedRoutDeleted"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupSup4.setStatus("current")

cGtpStatusGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 20)
)
cGtpStatusGroupSup2.setObjects(
      *(("CISCO-GTP-MIB", "cGtpTotalActivePaths"),
        ("CISCO-GTP-MIB", "cGtpTotalActiveGtpv1DataPaths"))
)
if mibBuilder.loadTexts:
    cGtpStatusGroupSup2.setStatus("current")

cGtpStatisticsGroupSup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 21)
)
cGtpStatisticsGroupSup5.setObjects(
      *(("CISCO-GTP-MIB", "cGtpTotalv0v1SigMsgDropped"),
        ("CISCO-GTP-MIB", "cGtpTotalDataMsgDropped"),
        ("CISCO-GTP-MIB", "cGtpv0PathCreated"),
        ("CISCO-GTP-MIB", "cGtpv0PathDeleted"),
        ("CISCO-GTP-MIB", "cGtpv0PathRestarted"),
        ("CISCO-GTP-MIB", "cGtpv1SigPathCreated"),
        ("CISCO-GTP-MIB", "cGtpv1SigPathDeleted"),
        ("CISCO-GTP-MIB", "cGtpv1SigPathRestarted"),
        ("CISCO-GTP-MIB", "cGtpv1DataPathCreated"),
        ("CISCO-GTP-MIB", "cGtpv1DataPathDeleted"),
        ("CISCO-GTP-MIB", "cGtpv1DataPathRestarted"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupSup5.setStatus("current")

cGtpStatisticsGroupSup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 22)
)
cGtpStatisticsGroupSup6.setObjects(
      *(("CISCO-GTP-MIB", "cGtpTotalDownlinkQosFailures"),
        ("CISCO-GTP-MIB", "cGtpTotalUplinkQosFailures"))
)
if mibBuilder.loadTexts:
    cGtpStatisticsGroupSup6.setStatus("current")


# Notification objects

cGtpPathFailedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 2, 0, 1)
)
cGtpPathFailedNotification.setObjects(
      *(("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddrTyp"),
        ("CISCO-GTP-MIB", "cGtpLastNoRespToEchoGSNIpAddr"))
)
if mibBuilder.loadTexts:
    cGtpPathFailedNotification.setStatus(
        "current"
    )


# Notifications groups

cGtpNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 2, 7)
)
cGtpNotifGroup.setObjects(
    ("CISCO-GTP-MIB", "cGtpPathFailedNotification")
)
if mibBuilder.loadTexts:
    cGtpNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cGtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cGtpMIBCompliance.setStatus(
        "obsolete"
    )

cGtpMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev1.setStatus(
        "obsolete"
    )

cGtpMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev2.setStatus(
        "obsolete"
    )

cGtpMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev3.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev4.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev5.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev6.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev7.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev8.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 10)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev9.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 11)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev10.setStatus(
        "deprecated"
    )

cGtpMIBComplianceRev11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 188, 3, 1, 12)
)
if mibBuilder.loadTexts:
    cGtpMIBComplianceRev11.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GTP-MIB",
    **{"CGtpMaxHistNumber": CGtpMaxHistNumber,
       "CGtpVersion": CGtpVersion,
       "CGtpEntities": CGtpEntities,
       "cGtpMIB": cGtpMIB,
       "cGtpMIBObjects": cGtpMIBObjects,
       "cGtpConfigurations": cGtpConfigurations,
       "cGtpGSNService": cGtpGSNService,
       "cGtpVersion": cGtpVersion,
       "cGtpT3TunnelTimer": cGtpT3TunnelTimer,
       "cGtpT3ResponseTimer": cGtpT3ResponseTimer,
       "cGtpN3Request": cGtpN3Request,
       "cGtpN3BufferSize": cGtpN3BufferSize,
       "cGtpEchoRequestTimerEnable": cGtpEchoRequestTimerEnable,
       "cGtpEchoRequestTimer": cGtpEchoRequestTimer,
       "cGtpGSNTotalBandwidthResrc": cGtpGSNTotalBandwidthResrc,
       "cGtpMaximumPdps": cGtpMaximumPdps,
       "cGtpNotifEnable": cGtpNotifEnable,
       "cGtpDynamicEchoTimerEnable": cGtpDynamicEchoTimerEnable,
       "cGtpDynamicEchoTimerMinTime": cGtpDynamicEchoTimerMinTime,
       "cGtpDynamicEchoTimerSmoothFactor": cGtpDynamicEchoTimerSmoothFactor,
       "cGtpPathHistoryLimit": cGtpPathHistoryLimit,
       "cGtpUpdateFailDelete": cGtpUpdateFailDelete,
       "cGtpSgsnProfileTable": cGtpSgsnProfileTable,
       "cGtpSgsnProfileEntry": cGtpSgsnProfileEntry,
       "cGtpSgsnProfileIndex": cGtpSgsnProfileIndex,
       "cGtpSgsnProfileIpAddressType": cGtpSgsnProfileIpAddressType,
       "cGtpSgsnProfileStartIpAddress": cGtpSgsnProfileStartIpAddress,
       "cGtpSgsnProfileEndIpAddress": cGtpSgsnProfileEndIpAddress,
       "cGtpSgsnProfilePortNumber": cGtpSgsnProfilePortNumber,
       "cGtpSgsnProfileEchoDisable": cGtpSgsnProfileEchoDisable,
       "cGtpSgsnProfileStorageType": cGtpSgsnProfileStorageType,
       "cGtpSgsnProfileRowStatus": cGtpSgsnProfileRowStatus,
       "cGtpStatus": cGtpStatus,
       "cGtpLastNoRespToEchoGSNIpAddrTyp": cGtpLastNoRespToEchoGSNIpAddrTyp,
       "cGtpLastNoRespToEchoGSNIpAddr": cGtpLastNoRespToEchoGSNIpAddr,
       "cGtpPremiumQosMeanThroughput": cGtpPremiumQosMeanThroughput,
       "cGtpNormalQosMeanThroughput": cGtpNormalQosMeanThroughput,
       "cGtpBestEffortQosMeanThroughput": cGtpBestEffortQosMeanThroughput,
       "cGtpGSNTable": cGtpGSNTable,
       "cGtpGSNEntry": cGtpGSNEntry,
       "cGtpGSNAddressType": cGtpGSNAddressType,
       "cGtpGSNAddress": cGtpGSNAddress,
       "cGtpGSNVersion": cGtpGSNVersion,
       "cGtpPathTable": cGtpPathTable,
       "cGtpPathEntry": cGtpPathEntry,
       "cGtpPathAddressType": cGtpPathAddressType,
       "cGtpPathAddress": cGtpPathAddress,
       "cGtpPathPort": cGtpPathPort,
       "cGtpPathVersion": cGtpPathVersion,
       "cGtpPathRemoteNode": cGtpPathRemoteNode,
       "cGtpPathVrfName": cGtpPathVrfName,
       "cGtpTotalActivePaths": cGtpTotalActivePaths,
       "cGtpTotalActiveGtpv1DataPaths": cGtpTotalActiveGtpv1DataPaths,
       "cGtpStatistics": cGtpStatistics,
       "cGtpPathFailureOccurrences": cGtpPathFailureOccurrences,
       "cGtpCurrentUsedBandwidth": cGtpCurrentUsedBandwidth,
       "cGtpTotalDroppedPackets": cGtpTotalDroppedPackets,
       "cGtpPathStatisticsTable": cGtpPathStatisticsTable,
       "cGtpPathStatisticsEntry": cGtpPathStatisticsEntry,
       "cGtpUnexpectedMsgs": cGtpUnexpectedMsgs,
       "cGtpDroppedDataMsgs": cGtpDroppedDataMsgs,
       "cGtpRcvdPDUMsgs": cGtpRcvdPDUMsgs,
       "cGtpSentPDUMsgs": cGtpSentPDUMsgs,
       "cGtpRcvdPDUOctets": cGtpRcvdPDUOctets,
       "cGtpSentPDUOctets": cGtpSentPDUOctets,
       "cGtpMsgTooShort": cGtpMsgTooShort,
       "cGtpUnknownMsgs": cGtpUnknownMsgs,
       "cGtpUnexpectedSigMsgs": cGtpUnexpectedSigMsgs,
       "cGtpRoamingPDUs": cGtpRoamingPDUs,
       "cGtpSecurityViolations": cGtpSecurityViolations,
       "cGtpUnsupportedExtHdr": cGtpUnsupportedExtHdr,
       "cGtpPathFailures": cGtpPathFailures,
       "cGtpTotalDropped": cGtpTotalDropped,
       "cGtpDroppedSigMsgs": cGtpDroppedSigMsgs,
       "cGtpRcvdSigMsgs": cGtpRcvdSigMsgs,
       "cGtpSentSigMsgs": cGtpSentSigMsgs,
       "cGtpTotalCreatedPDPs": cGtpTotalCreatedPDPs,
       "cGtpTotalDeletedPDPs": cGtpTotalDeletedPDPs,
       "cGtpTotalCreatedPppPDPs": cGtpTotalCreatedPppPDPs,
       "cGtpTotalDeletedPppPDPs": cGtpTotalDeletedPppPDPs,
       "cGtpSinglePDPSessCleared": cGtpSinglePDPSessCleared,
       "cGtpPathFailLocalDelPDPs": cGtpPathFailLocalDelPDPs,
       "cGtpVerUpgradeLocalDelPDPs": cGtpVerUpgradeLocalDelPDPs,
       "cGtpNoSgsnLocalDelPDPs": cGtpNoSgsnLocalDelPDPs,
       "cGtpVerFallbackLocalDelPDPs": cGtpVerFallbackLocalDelPDPs,
       "cGtpCreateCollideWithDel": cGtpCreateCollideWithDel,
       "cGtpVersionChanges": cGtpVersionChanges,
       "cGtpRetransCreatePDPReqs": cGtpRetransCreatePDPReqs,
       "cGtpCreateAsUpdate": cGtpCreateAsUpdate,
       "cGtpIpv6PdpActRejects": cGtpIpv6PdpActRejects,
       "cGtpIpv6CreatedPDPs": cGtpIpv6CreatedPDPs,
       "cGtpIpv6DeletedPDPs": cGtpIpv6DeletedPDPs,
       "cGtpIpv6RcvdSigMsgs": cGtpIpv6RcvdSigMsgs,
       "cGtpIpv6SentSigMsgs": cGtpIpv6SentSigMsgs,
       "cGtpIpv6RcvdPDUs": cGtpIpv6RcvdPDUs,
       "cGtpIpv6SentPDUs": cGtpIpv6SentPDUs,
       "cGtpIpv6RcvdOctets": cGtpIpv6RcvdOctets,
       "cGtpIpv6SentOctets": cGtpIpv6SentOctets,
       "cGtpNoWaitSgsnLocalDelPDPs": cGtpNoWaitSgsnLocalDelPDPs,
       "cGtpNoReqSgsnLocalDelPDPs": cGtpNoReqSgsnLocalDelPDPs,
       "cGtpRoamingTrustedPDPs": cGtpRoamingTrustedPDPs,
       "cGtpRoamingNonTrustedPDPs": cGtpRoamingNonTrustedPDPs,
       "cGtpNonRoamingPDPs": cGtpNonRoamingPDPs,
       "cGtpSentPdpUpdateReqs": cGtpSentPdpUpdateReqs,
       "cGtpRcvdPdpUpdateResponses": cGtpRcvdPdpUpdateResponses,
       "cGtpTotalDtEnabled": cGtpTotalDtEnabled,
       "cGtpIpv4v6CreatedPDPs": cGtpIpv4v6CreatedPDPs,
       "cGtpIpv4v6DeletedPDPs": cGtpIpv4v6DeletedPDPs,
       "cGtpPathStatisticsHistoryTable": cGtpPathStatisticsHistoryTable,
       "cGtpPathStatisticsHistEntry": cGtpPathStatisticsHistEntry,
       "cGtpHistIndex": cGtpHistIndex,
       "cGtpHistRemoteAddrType": cGtpHistRemoteAddrType,
       "cGtpHistRemoteAddress": cGtpHistRemoteAddress,
       "cGtpHistRemotePort": cGtpHistRemotePort,
       "cGtpHistUnexpectedMsgs": cGtpHistUnexpectedMsgs,
       "cGtpHistDroppedDataMsgs": cGtpHistDroppedDataMsgs,
       "cGtpHistRcvdPDUMsgs": cGtpHistRcvdPDUMsgs,
       "cGtpHistSentPDUMsgs": cGtpHistSentPDUMsgs,
       "cGtpHistRcvdPDUOctets": cGtpHistRcvdPDUOctets,
       "cGtpHistSentPDUOctets": cGtpHistSentPDUOctets,
       "cGtpHistMsgTooShort": cGtpHistMsgTooShort,
       "cGtpHistUnknownMsgs": cGtpHistUnknownMsgs,
       "cGtpHistUnexpectedSigMsgs": cGtpHistUnexpectedSigMsgs,
       "cGtpHistRoamingPDUs": cGtpHistRoamingPDUs,
       "cGtpHistSecurityViolations": cGtpHistSecurityViolations,
       "cGtpHistUnsupportedExtHdr": cGtpHistUnsupportedExtHdr,
       "cGtpHistPathFailures": cGtpHistPathFailures,
       "cGtpHistTotalDropped": cGtpHistTotalDropped,
       "cGtpHistDroppedSigMsgs": cGtpHistDroppedSigMsgs,
       "cGtpHistRcvdSigMsgs": cGtpHistRcvdSigMsgs,
       "cGtpHistSentSigMsgs": cGtpHistSentSigMsgs,
       "cGtpHistTotalCreatedPDPs": cGtpHistTotalCreatedPDPs,
       "cGtpHistTotalDeletedPDPs": cGtpHistTotalDeletedPDPs,
       "cGtpHistTotalCreatedPppPDPs": cGtpHistTotalCreatedPppPDPs,
       "cGtpHistTotalDeletedPppPDPs": cGtpHistTotalDeletedPppPDPs,
       "cGtpHistSinglePDPSessCleared": cGtpHistSinglePDPSessCleared,
       "cGtpHistPathFailLocalDelPDPs": cGtpHistPathFailLocalDelPDPs,
       "cGtpHistVerUpgradeLocalDel": cGtpHistVerUpgradeLocalDel,
       "cGtpHistNoSgsnLocalDelPDPs": cGtpHistNoSgsnLocalDelPDPs,
       "cGtpHistVerFallbackLocalDel": cGtpHistVerFallbackLocalDel,
       "cGtpHistCreateCollideWithDel": cGtpHistCreateCollideWithDel,
       "cGtpHistVersionChanges": cGtpHistVersionChanges,
       "cGtpHistRetransCreatePDPReqs": cGtpHistRetransCreatePDPReqs,
       "cGtpHistCreateAsUpdate": cGtpHistCreateAsUpdate,
       "cGtpHistIpv6PdpActRejects": cGtpHistIpv6PdpActRejects,
       "cGtpHistIpv6CreatedPDPs": cGtpHistIpv6CreatedPDPs,
       "cGtpHistIpv6DeletedPDPs": cGtpHistIpv6DeletedPDPs,
       "cGtpHistIpv6RcvdSigMsgs": cGtpHistIpv6RcvdSigMsgs,
       "cGtpHistIpv6SentSigMsgs": cGtpHistIpv6SentSigMsgs,
       "cGtpHistIpv6RcvdPDUs": cGtpHistIpv6RcvdPDUs,
       "cGtpHistIpv6SentPDUs": cGtpHistIpv6SentPDUs,
       "cGtpHistIpv6RcvdOctets": cGtpHistIpv6RcvdOctets,
       "cGtpHistIpv6SentOctets": cGtpHistIpv6SentOctets,
       "cGtpHistNoWaitSgsnLocalDelPDPs": cGtpHistNoWaitSgsnLocalDelPDPs,
       "cGtpHistNoReqSgsnLocalDelPDPs": cGtpHistNoReqSgsnLocalDelPDPs,
       "cGtpHistRoamingTrustedPDPs": cGtpHistRoamingTrustedPDPs,
       "cGtpHistRoamingNonTrustedPDPs": cGtpHistRoamingNonTrustedPDPs,
       "cGtpHistNonRoamingPDPs": cGtpHistNonRoamingPDPs,
       "cGtpHistSentPdpUpdateReqs": cGtpHistSentPdpUpdateReqs,
       "cGtpHistRcvdPdpUpdateResponses": cGtpHistRcvdPdpUpdateResponses,
       "cGtpHistTotalDtEnabled": cGtpHistTotalDtEnabled,
       "cGtpHistRemoteNode": cGtpHistRemoteNode,
       "cGtpHistIpv4v6CreatedPDPs": cGtpHistIpv4v6CreatedPDPs,
       "cGtpHistIpv4v6DeletedPDPs": cGtpHistIpv4v6DeletedPDPs,
       "cGtpNetworkBehindMsApns": cGtpNetworkBehindMsApns,
       "cGtpTotalDownldFramedRout": cGtpTotalDownldFramedRout,
       "cGtpTotalDownldFramedRoutSavedFail": cGtpTotalDownldFramedRoutSavedFail,
       "cGtpTotalDownldFramedRoutInsFail": cGtpTotalDownldFramedRoutInsFail,
       "cGtpTotalDownldFramedRoutIns": cGtpTotalDownldFramedRoutIns,
       "cGtpTotalDownldFramedRoutDeleted": cGtpTotalDownldFramedRoutDeleted,
       "cGtpTotalv0v1SigMsgDropped": cGtpTotalv0v1SigMsgDropped,
       "cGtpTotalDataMsgDropped": cGtpTotalDataMsgDropped,
       "cGtpv0PathCreated": cGtpv0PathCreated,
       "cGtpv0PathDeleted": cGtpv0PathDeleted,
       "cGtpv0PathRestarted": cGtpv0PathRestarted,
       "cGtpv1SigPathCreated": cGtpv1SigPathCreated,
       "cGtpv1SigPathDeleted": cGtpv1SigPathDeleted,
       "cGtpv1SigPathRestarted": cGtpv1SigPathRestarted,
       "cGtpv1DataPathCreated": cGtpv1DataPathCreated,
       "cGtpv1DataPathDeleted": cGtpv1DataPathDeleted,
       "cGtpv1DataPathRestarted": cGtpv1DataPathRestarted,
       "cGtpTotalDownlinkQosFailures": cGtpTotalDownlinkQosFailures,
       "cGtpTotalUplinkQosFailures": cGtpTotalUplinkQosFailures,
       "cGtpNotifPrefix": cGtpNotifPrefix,
       "cGtpNotifications": cGtpNotifications,
       "cGtpPathFailedNotification": cGtpPathFailedNotification,
       "cGtpMIBConformances": cGtpMIBConformances,
       "cGtpMIBCompliances": cGtpMIBCompliances,
       "cGtpMIBCompliance": cGtpMIBCompliance,
       "cGtpMIBComplianceRev1": cGtpMIBComplianceRev1,
       "cGtpMIBComplianceRev2": cGtpMIBComplianceRev2,
       "cGtpMIBComplianceRev3": cGtpMIBComplianceRev3,
       "cGtpMIBComplianceRev4": cGtpMIBComplianceRev4,
       "cGtpMIBComplianceRev5": cGtpMIBComplianceRev5,
       "cGtpMIBComplianceRev6": cGtpMIBComplianceRev6,
       "cGtpMIBComplianceRev7": cGtpMIBComplianceRev7,
       "cGtpMIBComplianceRev8": cGtpMIBComplianceRev8,
       "cGtpMIBComplianceRev9": cGtpMIBComplianceRev9,
       "cGtpMIBComplianceRev10": cGtpMIBComplianceRev10,
       "cGtpMIBComplianceRev11": cGtpMIBComplianceRev11,
       "cGtpMIBGroups": cGtpMIBGroups,
       "cGtpConfigurationsGroup": cGtpConfigurationsGroup,
       "cGtpStatusGroup": cGtpStatusGroup,
       "cGtpStatisticsGroup": cGtpStatisticsGroup,
       "cGtpConfigurationsGroupRev1": cGtpConfigurationsGroupRev1,
       "cGtpStatusGroupRev1": cGtpStatusGroupRev1,
       "cGtpStatisticsGroupRev1": cGtpStatisticsGroupRev1,
       "cGtpNotifGroup": cGtpNotifGroup,
       "cGtpConfigurationsGroupRev2": cGtpConfigurationsGroupRev2,
       "cGtpStatusGroupRev2": cGtpStatusGroupRev2,
       "cGtpStatusGroupRev3": cGtpStatusGroupRev3,
       "cGtpStatisticsGroupSup1": cGtpStatisticsGroupSup1,
       "cGtpConfigurationsGroupSup1": cGtpConfigurationsGroupSup1,
       "cGtpConfigurationsGroupSup2": cGtpConfigurationsGroupSup2,
       "cGtpStatisticsGroupSup2": cGtpStatisticsGroupSup2,
       "cGtpConfigurationsGroupSup3": cGtpConfigurationsGroupSup3,
       "cGtpStatusGroupSup1": cGtpStatusGroupSup1,
       "cGtpStatisticsGroupSup3": cGtpStatisticsGroupSup3,
       "cGtpStatisticsGroupSup4": cGtpStatisticsGroupSup4,
       "cGtpStatusGroupSup2": cGtpStatusGroupSup2,
       "cGtpStatisticsGroupSup5": cGtpStatisticsGroupSup5,
       "cGtpStatisticsGroupSup6": cGtpStatisticsGroupSup6}
)
