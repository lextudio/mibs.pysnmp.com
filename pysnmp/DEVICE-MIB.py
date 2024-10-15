# SNMP MIB module (DEVICE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DEVICE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:26:09 2024
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

(coriolisMibs,
 device) = mibBuilder.importSymbols(
    "CORIOLIS-MIB",
    "coriolisMibs",
    "device")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

deviceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Chassis_ObjectIdentity = ObjectIdentity
chassis = _Chassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2)
)
_ChassisAutoConfig_Type = TruthValue
_ChassisAutoConfig_Object = MibScalar
chassisAutoConfig = _ChassisAutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 1),
    _ChassisAutoConfig_Type()
)
chassisAutoConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisAutoConfig.setStatus("current")
_ChassisIpAddr_Type = IpAddress
_ChassisIpAddr_Object = MibScalar
chassisIpAddr = _ChassisIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 2),
    _ChassisIpAddr_Type()
)
chassisIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisIpAddr.setStatus("current")


class _ChassisId_Type(Integer32):
    """Custom type chassisId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              21,
              25)
        )
    )
    namedValues = NamedValues(
        *(("optiFlow1010", 21),
          ("optiFlow1020", 25),
          ("optiFlow3000", 4),
          ("optiFlow3000thirteen", 6),
          ("optiFlow3500", 3),
          ("optiFlow3500thirteen", 5),
          ("optiFlow5000", 2),
          ("optiFlow5500", 1))
    )


_ChassisId_Type.__name__ = "Integer32"
_ChassisId_Object = MibScalar
chassisId = _ChassisId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 3),
    _ChassisId_Type()
)
chassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisId.setStatus("current")


class _ChassisCharacter_Type(Integer32):
    """Custom type chassisCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gne", 1),
          ("ne", 2),
          ("sne", 3))
    )


_ChassisCharacter_Type.__name__ = "Integer32"
_ChassisCharacter_Object = MibScalar
chassisCharacter = _ChassisCharacter_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 4),
    _ChassisCharacter_Type()
)
chassisCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisCharacter.setStatus("current")


class _ChassisElemReachStatus_Type(Integer32):
    """Custom type chassisElemReachStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reachable", 1),
          ("unreachable", 2))
    )


_ChassisElemReachStatus_Type.__name__ = "Integer32"
_ChassisElemReachStatus_Object = MibScalar
chassisElemReachStatus = _ChassisElemReachStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 5),
    _ChassisElemReachStatus_Type()
)
chassisElemReachStatus.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chassisElemReachStatus.setStatus("current")
_ChassisNumElemReachable_Type = Integer32
_ChassisNumElemReachable_Object = MibScalar
chassisNumElemReachable = _ChassisNumElemReachable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 6),
    _ChassisNumElemReachable_Type()
)
chassisNumElemReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNumElemReachable.setStatus("current")


class _ChassisCurrentCharacter_Type(Integer32):
    """Custom type chassisCurrentCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gne", 1),
          ("ne", 2),
          ("sne", 3))
    )


_ChassisCurrentCharacter_Type.__name__ = "Integer32"
_ChassisCurrentCharacter_Object = MibScalar
chassisCurrentCharacter = _ChassisCurrentCharacter_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 8),
    _ChassisCurrentCharacter_Type()
)
chassisCurrentCharacter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCurrentCharacter.setStatus("current")


class _ChassisFanStatus_Type(Integer32):
    """Custom type chassisFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("good", 2))
    )


_ChassisFanStatus_Type.__name__ = "Integer32"
_ChassisFanStatus_Object = MibScalar
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 9),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("current")
_ChassisPowerSupplyTable_Object = MibTable
chassisPowerSupplyTable = _ChassisPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 10)
)
if mibBuilder.loadTexts:
    chassisPowerSupplyTable.setStatus("current")
_ChassisPowerSupplyEntry_Object = MibTableRow
chassisPowerSupplyEntry = _ChassisPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 10, 1)
)
chassisPowerSupplyEntry.setIndexNames(
    (0, "DEVICE-MIB", "chassisPowerSupplyNumber"),
)
if mibBuilder.loadTexts:
    chassisPowerSupplyEntry.setStatus("current")
_ChassisPowerSupplyNumber_Type = Integer32
_ChassisPowerSupplyNumber_Object = MibTableColumn
chassisPowerSupplyNumber = _ChassisPowerSupplyNumber_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 10, 1, 1),
    _ChassisPowerSupplyNumber_Type()
)
chassisPowerSupplyNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    chassisPowerSupplyNumber.setStatus("current")


class _ChassisPowerSupplyStatus_Type(Integer32):
    """Custom type chassisPowerSupplyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("absent", 2),
          ("fail", 7),
          ("fault", 5),
          ("noFail", 8),
          ("noFault", 6),
          ("present", 1),
          ("tempHot", 3),
          ("tempNorm", 4))
    )


_ChassisPowerSupplyStatus_Type.__name__ = "Integer32"
_ChassisPowerSupplyStatus_Object = MibTableColumn
chassisPowerSupplyStatus = _ChassisPowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 10, 1, 2),
    _ChassisPowerSupplyStatus_Type()
)
chassisPowerSupplyStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chassisPowerSupplyStatus.setStatus("current")


class _ChassisFWStatus_Type(Integer32):
    """Custom type chassisFWStatus based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("abort", 27),
          ("bad-host", 1),
          ("bad-ip-addr", 13),
          ("bad-msg", 14),
          ("busy", 9),
          ("crc-mismatch", 22),
          ("fault", 18),
          ("file-not-found", 3),
          ("in-progress", 11),
          ("init-not-complete", 26),
          ("invalid-image-header", 21),
          ("last-instance", 25),
          ("lock-failure", 19),
          ("locked", 20),
          ("net-drv", 2),
          ("not-a-gne", 23),
          ("ok", 0),
          ("out-of-memory", 7),
          ("pending", 28),
          ("read-error", 5),
          ("reg-ipc", 17),
          ("retries-expired", 16),
          ("signature-mismatch", 24),
          ("spawn-failed", 10),
          ("state-error", 12),
          ("task-not-found", 4),
          ("unknown-image-type", 6),
          ("unknown-msg", 15),
          ("write-error", 8))
    )


_ChassisFWStatus_Type.__name__ = "Integer32"
_ChassisFWStatus_Object = MibScalar
chassisFWStatus = _ChassisFWStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 11),
    _ChassisFWStatus_Type()
)
chassisFWStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    chassisFWStatus.setStatus("current")


class _RingFWStatus_Type(Integer32):
    """Custom type ringFWStatus based on Integer32"""
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("abort", 27),
          ("bad-host", 1),
          ("bad-ip-addr", 13),
          ("bad-msg", 14),
          ("busy", 9),
          ("crc-mismatch", 22),
          ("fault", 18),
          ("file-not-found", 3),
          ("in-progress", 11),
          ("init-not-complete", 26),
          ("invalid-image-header", 21),
          ("last-instance", 25),
          ("lock-failure", 19),
          ("locked", 20),
          ("net-drv", 2),
          ("not-a-gne", 23),
          ("ok", 0),
          ("out-of-memory", 7),
          ("pending", 28),
          ("read-error", 5),
          ("reg-ipc", 17),
          ("retries-expired", 16),
          ("signature-mismatch", 24),
          ("spawn-failed", 10),
          ("state-error", 12),
          ("task-not-found", 4),
          ("unknown-image-type", 6),
          ("unknown-msg", 15),
          ("write-error", 8))
    )


_RingFWStatus_Type.__name__ = "Integer32"
_RingFWStatus_Object = MibScalar
ringFWStatus = _RingFWStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 12),
    _RingFWStatus_Type()
)
ringFWStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ringFWStatus.setStatus("current")
_FtpServerIP_Type = IpAddress
_FtpServerIP_Object = MibScalar
ftpServerIP = _FtpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 13),
    _FtpServerIP_Type()
)
ftpServerIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ftpServerIP.setStatus("current")
_ControlFilePath_Type = OctetString
_ControlFilePath_Object = MibScalar
controlFilePath = _ControlFilePath_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 14),
    _ControlFilePath_Type()
)
controlFilePath.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    controlFilePath.setStatus("current")
_VersionString_Type = OctetString
_VersionString_Object = MibScalar
versionString = _VersionString_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 15),
    _VersionString_Type()
)
versionString.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    versionString.setStatus("current")
_SyslogUnknownEvent_Type = Integer32
_SyslogUnknownEvent_Object = MibScalar
syslogUnknownEvent = _SyslogUnknownEvent_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 16),
    _SyslogUnknownEvent_Type()
)
syslogUnknownEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogUnknownEvent.setStatus("current")
_SyslogUnknownVersion_Type = Integer32
_SyslogUnknownVersion_Object = MibScalar
syslogUnknownVersion = _SyslogUnknownVersion_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 17),
    _SyslogUnknownVersion_Type()
)
syslogUnknownVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    syslogUnknownVersion.setStatus("current")


class _ChassisRoutingProt_Type(Integer32):
    """Custom type chassisRoutingProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("rip", 2))
    )


_ChassisRoutingProt_Type.__name__ = "Integer32"
_ChassisRoutingProt_Object = MibScalar
chassisRoutingProt = _ChassisRoutingProt_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 18),
    _ChassisRoutingProt_Type()
)
chassisRoutingProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisRoutingProt.setStatus("current")
_ChassisSubnetIp_Type = IpAddress
_ChassisSubnetIp_Object = MibScalar
chassisSubnetIp = _ChassisSubnetIp_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 19),
    _ChassisSubnetIp_Type()
)
chassisSubnetIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSubnetIp.setStatus("current")
_ChassisSubnetMask_Type = IpAddress
_ChassisSubnetMask_Object = MibScalar
chassisSubnetMask = _ChassisSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 20),
    _ChassisSubnetMask_Type()
)
chassisSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisSubnetMask.setStatus("current")
_ChassisRingsOnMaster_Type = OctetString
_ChassisRingsOnMaster_Object = MibScalar
chassisRingsOnMaster = _ChassisRingsOnMaster_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 21),
    _ChassisRingsOnMaster_Type()
)
chassisRingsOnMaster.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisRingsOnMaster.setStatus("current")
_ChassisCurrentRingsOnMaster_Type = OctetString
_ChassisCurrentRingsOnMaster_Object = MibScalar
chassisCurrentRingsOnMaster = _ChassisCurrentRingsOnMaster_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 22),
    _ChassisCurrentRingsOnMaster_Type()
)
chassisCurrentRingsOnMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisCurrentRingsOnMaster.setStatus("current")
_ChassisFailoverPreserveRings_Type = OctetString
_ChassisFailoverPreserveRings_Object = MibScalar
chassisFailoverPreserveRings = _ChassisFailoverPreserveRings_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 2, 23),
    _ChassisFailoverPreserveRings_Type()
)
chassisFailoverPreserveRings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chassisFailoverPreserveRings.setStatus("current")
_Systime_ObjectIdentity = ObjectIdentity
systime = _Systime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3)
)


class _SystimeTimingMode_Type(Integer32):
    """Custom type systimeTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tmExt", 1),
          ("tmFreerun", 3),
          ("tmLine", 2))
    )


_SystimeTimingMode_Type.__name__ = "Integer32"
_SystimeTimingMode_Object = MibScalar
systimeTimingMode = _SystimeTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 1),
    _SystimeTimingMode_Type()
)
systimeTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeTimingMode.setStatus("current")


class _SystimePriBITSFraming_Type(Integer32):
    """Custom type systimePriBITSFraming based on Integer32"""
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
        *(("e1", 6),
          ("t1ESF4K", 2),
          ("t1SF", 1),
          ("t1SLC96", 5),
          ("t1T1DM", 3),
          ("t1T1DMAlt", 4))
    )


_SystimePriBITSFraming_Type.__name__ = "Integer32"
_SystimePriBITSFraming_Object = MibScalar
systimePriBITSFraming = _SystimePriBITSFraming_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 2),
    _SystimePriBITSFraming_Type()
)
systimePriBITSFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriBITSFraming.setStatus("current")


class _SystimeSecBITSFraming_Type(Integer32):
    """Custom type systimeSecBITSFraming based on Integer32"""
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
        *(("e1", 6),
          ("t1ESF4K", 2),
          ("t1SF", 1),
          ("t1SLC96", 5),
          ("t1T1DM", 3),
          ("t1T1DMAlt", 4))
    )


_SystimeSecBITSFraming_Type.__name__ = "Integer32"
_SystimeSecBITSFraming_Object = MibScalar
systimeSecBITSFraming = _SystimeSecBITSFraming_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 3),
    _SystimeSecBITSFraming_Type()
)
systimeSecBITSFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecBITSFraming.setStatus("current")


class _SystimePriBITSCoding_Type(Integer32):
    """Custom type systimePriBITSCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_SystimePriBITSCoding_Type.__name__ = "Integer32"
_SystimePriBITSCoding_Object = MibScalar
systimePriBITSCoding = _SystimePriBITSCoding_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 4),
    _SystimePriBITSCoding_Type()
)
systimePriBITSCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriBITSCoding.setStatus("current")


class _SystimeSecBITSCoding_Type(Integer32):
    """Custom type systimeSecBITSCoding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ami", 1),
          ("b8zs", 2),
          ("hdb3", 3))
    )


_SystimeSecBITSCoding_Type.__name__ = "Integer32"
_SystimeSecBITSCoding_Object = MibScalar
systimeSecBITSCoding = _SystimeSecBITSCoding_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 5),
    _SystimeSecBITSCoding_Type()
)
systimeSecBITSCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecBITSCoding.setStatus("current")
_SystimePriClkSrcId_Type = OctetString
_SystimePriClkSrcId_Object = MibScalar
systimePriClkSrcId = _SystimePriClkSrcId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 6),
    _SystimePriClkSrcId_Type()
)
systimePriClkSrcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriClkSrcId.setStatus("current")
_SystimeSecClkSrcId_Type = OctetString
_SystimeSecClkSrcId_Object = MibScalar
systimeSecClkSrcId = _SystimeSecClkSrcId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 7),
    _SystimeSecClkSrcId_Type()
)
systimeSecClkSrcId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecClkSrcId.setStatus("current")


class _SystimeClkReference_Type(Integer32):
    """Custom type systimeClkReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("crAuto", 1),
          ("crFreerun", 8),
          ("crHoldover", 4),
          ("crPri", 2),
          ("crSec", 3),
          ("crStandby", 5),
          ("crStandbypri", 6),
          ("crStandbysec", 7))
    )


_SystimeClkReference_Type.__name__ = "Integer32"
_SystimeClkReference_Object = MibScalar
systimeClkReference = _SystimeClkReference_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 8),
    _SystimeClkReference_Type()
)
systimeClkReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeClkReference.setStatus("current")


class _SystimeClkRevertive_Type(Integer32):
    """Custom type systimeClkRevertive based on Integer32"""
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


_SystimeClkRevertive_Type.__name__ = "Integer32"
_SystimeClkRevertive_Object = MibScalar
systimeClkRevertive = _SystimeClkRevertive_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 9),
    _SystimeClkRevertive_Type()
)
systimeClkRevertive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeClkRevertive.setStatus("current")


class _SystimeStandbyClkEnable_Type(Integer32):
    """Custom type systimeStandbyClkEnable based on Integer32"""
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


_SystimeStandbyClkEnable_Type.__name__ = "Integer32"
_SystimeStandbyClkEnable_Object = MibScalar
systimeStandbyClkEnable = _SystimeStandbyClkEnable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 10),
    _SystimeStandbyClkEnable_Type()
)
systimeStandbyClkEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeStandbyClkEnable.setStatus("current")


class _SystimePriCSNVTime_Type(Integer32):
    """Custom type systimePriCSNVTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SystimePriCSNVTime_Type.__name__ = "Integer32"
_SystimePriCSNVTime_Object = MibScalar
systimePriCSNVTime = _SystimePriCSNVTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 11),
    _SystimePriCSNVTime_Type()
)
systimePriCSNVTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriCSNVTime.setStatus("current")


class _SystimeSecCSNVTime_Type(Integer32):
    """Custom type systimeSecCSNVTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_SystimeSecCSNVTime_Type.__name__ = "Integer32"
_SystimeSecCSNVTime_Object = MibScalar
systimeSecCSNVTime = _SystimeSecCSNVTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 12),
    _SystimeSecCSNVTime_Type()
)
systimeSecCSNVTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecCSNVTime.setStatus("current")


class _SystimePriCSHVTime_Type(Integer32):
    """Custom type systimePriCSHVTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SystimePriCSHVTime_Type.__name__ = "Integer32"
_SystimePriCSHVTime_Object = MibScalar
systimePriCSHVTime = _SystimePriCSHVTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 13),
    _SystimePriCSHVTime_Type()
)
systimePriCSHVTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriCSHVTime.setStatus("current")


class _SystimeSecCSHVTime_Type(Integer32):
    """Custom type systimeSecCSHVTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_SystimeSecCSHVTime_Type.__name__ = "Integer32"
_SystimeSecCSHVTime_Object = MibScalar
systimeSecCSHVTime = _SystimeSecCSHVTime_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 14),
    _SystimeSecCSHVTime_Type()
)
systimeSecCSHVTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecCSHVTime.setStatus("current")


class _SystimePriCSUseLimit_Type(Integer32):
    """Custom type systimePriCSUseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SystimePriCSUseLimit_Type.__name__ = "Integer32"
_SystimePriCSUseLimit_Object = MibScalar
systimePriCSUseLimit = _SystimePriCSUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 15),
    _SystimePriCSUseLimit_Type()
)
systimePriCSUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriCSUseLimit.setStatus("current")


class _SystimeSecCSUseLimit_Type(Integer32):
    """Custom type systimeSecCSUseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SystimeSecCSUseLimit_Type.__name__ = "Integer32"
_SystimeSecCSUseLimit_Object = MibScalar
systimeSecCSUseLimit = _SystimeSecCSUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 16),
    _SystimeSecCSUseLimit_Type()
)
systimeSecCSUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecCSUseLimit.setStatus("current")


class _SystimeStandbyCSUseLimit_Type(Integer32):
    """Custom type systimeStandbyCSUseLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_SystimeStandbyCSUseLimit_Type.__name__ = "Integer32"
_SystimeStandbyCSUseLimit_Object = MibScalar
systimeStandbyCSUseLimit = _SystimeStandbyCSUseLimit_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 17),
    _SystimeStandbyCSUseLimit_Type()
)
systimeStandbyCSUseLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeStandbyCSUseLimit.setStatus("current")


class _SystimePriCSUseInterval_Type(Integer32):
    """Custom type systimePriCSUseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SystimePriCSUseInterval_Type.__name__ = "Integer32"
_SystimePriCSUseInterval_Object = MibScalar
systimePriCSUseInterval = _SystimePriCSUseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 18),
    _SystimePriCSUseInterval_Type()
)
systimePriCSUseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimePriCSUseInterval.setStatus("current")


class _SystimeSecCSUseInterval_Type(Integer32):
    """Custom type systimeSecCSUseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SystimeSecCSUseInterval_Type.__name__ = "Integer32"
_SystimeSecCSUseInterval_Object = MibScalar
systimeSecCSUseInterval = _SystimeSecCSUseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 19),
    _SystimeSecCSUseInterval_Type()
)
systimeSecCSUseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeSecCSUseInterval.setStatus("current")


class _SystimeStandbyCSUseInterval_Type(Integer32):
    """Custom type systimeStandbyCSUseInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_SystimeStandbyCSUseInterval_Type.__name__ = "Integer32"
_SystimeStandbyCSUseInterval_Object = MibScalar
systimeStandbyCSUseInterval = _SystimeStandbyCSUseInterval_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 20),
    _SystimeStandbyCSUseInterval_Type()
)
systimeStandbyCSUseInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeStandbyCSUseInterval.setStatus("current")


class _SystimeCREventEnable_Type(Integer32):
    """Custom type systimeCREventEnable based on Integer32"""
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


_SystimeCREventEnable_Type.__name__ = "Integer32"
_SystimeCREventEnable_Object = MibScalar
systimeCREventEnable = _SystimeCREventEnable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 21),
    _SystimeCREventEnable_Type()
)
systimeCREventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    systimeCREventEnable.setStatus("current")


class _SystimeCRInUse_Type(Integer32):
    """Custom type systimeCRInUse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("crAuto", 1),
          ("crFreerun", 8),
          ("crHoldover", 4),
          ("crPri", 2),
          ("crSec", 3),
          ("crStandby", 5),
          ("crStandbypri", 6),
          ("crStandbysec", 7))
    )


_SystimeCRInUse_Type.__name__ = "Integer32"
_SystimeCRInUse_Object = MibScalar
systimeCRInUse = _SystimeCRInUse_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 22),
    _SystimeCRInUse_Type()
)
systimeCRInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systimeCRInUse.setStatus("current")
_SystimeCRUsedCount_Type = Counter32
_SystimeCRUsedCount_Object = MibScalar
systimeCRUsedCount = _SystimeCRUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 3, 23),
    _SystimeCRUsedCount_Type()
)
systimeCRUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systimeCRUsedCount.setStatus("current")
_DeviceNMSTable_Object = MibTable
deviceNMSTable = _DeviceNMSTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4)
)
if mibBuilder.loadTexts:
    deviceNMSTable.setStatus("current")
_DeviceNMSEntry_Object = MibTableRow
deviceNMSEntry = _DeviceNMSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1)
)
deviceNMSEntry.setIndexNames(
    (0, "DEVICE-MIB", "deviceNMSIndex"),
)
if mibBuilder.loadTexts:
    deviceNMSEntry.setStatus("current")
_DeviceNMSIndex_Type = Integer32
_DeviceNMSIndex_Object = MibTableColumn
deviceNMSIndex = _DeviceNMSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1, 1),
    _DeviceNMSIndex_Type()
)
deviceNMSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    deviceNMSIndex.setStatus("current")
_DeviceNMSIpAddress_Type = IpAddress
_DeviceNMSIpAddress_Object = MibTableColumn
deviceNMSIpAddress = _DeviceNMSIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1, 2),
    _DeviceNMSIpAddress_Type()
)
deviceNMSIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceNMSIpAddress.setStatus("current")


class _DeviceNMSAccessType_Type(Integer32):
    """Custom type deviceNMSAccessType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accessTypeTrapDisabled", 2),
          ("accessTypeTrapEnabled", 1))
    )


_DeviceNMSAccessType_Type.__name__ = "Integer32"
_DeviceNMSAccessType_Object = MibTableColumn
deviceNMSAccessType = _DeviceNMSAccessType_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1, 3),
    _DeviceNMSAccessType_Type()
)
deviceNMSAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceNMSAccessType.setStatus("current")


class _DeviceNMSMIBIITrapList_Type(OctetString):
    """Custom type deviceNMSMIBIITrapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_DeviceNMSMIBIITrapList_Type.__name__ = "OctetString"
_DeviceNMSMIBIITrapList_Object = MibTableColumn
deviceNMSMIBIITrapList = _DeviceNMSMIBIITrapList_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1, 4),
    _DeviceNMSMIBIITrapList_Type()
)
deviceNMSMIBIITrapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceNMSMIBIITrapList.setStatus("current")


class _DeviceNMSEnterpriseTrapList_Type(OctetString):
    """Custom type deviceNMSEnterpriseTrapList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )


_DeviceNMSEnterpriseTrapList_Type.__name__ = "OctetString"
_DeviceNMSEnterpriseTrapList_Object = MibTableColumn
deviceNMSEnterpriseTrapList = _DeviceNMSEnterpriseTrapList_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1, 5),
    _DeviceNMSEnterpriseTrapList_Type()
)
deviceNMSEnterpriseTrapList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceNMSEnterpriseTrapList.setStatus("current")


class _DeviceNMSTrapSevAllowed_Type(Integer32):
    """Custom type deviceNMSTrapSevAllowed based on Integer32"""
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
        *(("trapSevClear", 1),
          ("trapSevCritical", 6),
          ("trapSevInfo", 2),
          ("trapSevMajor", 5),
          ("trapSevMinor", 4),
          ("trapSevWarning", 3))
    )


_DeviceNMSTrapSevAllowed_Type.__name__ = "Integer32"
_DeviceNMSTrapSevAllowed_Object = MibTableColumn
deviceNMSTrapSevAllowed = _DeviceNMSTrapSevAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 4, 1, 6),
    _DeviceNMSTrapSevAllowed_Type()
)
deviceNMSTrapSevAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    deviceNMSTrapSevAllowed.setStatus("current")
_SysMemory_ObjectIdentity = ObjectIdentity
sysMemory = _SysMemory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5)
)
_NumBytesFree_Type = Integer32
_NumBytesFree_Object = MibScalar
numBytesFree = _NumBytesFree_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 1),
    _NumBytesFree_Type()
)
numBytesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesFree.setStatus("current")
_NumBlocksFree_Type = Integer32
_NumBlocksFree_Object = MibScalar
numBlocksFree = _NumBlocksFree_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 2),
    _NumBlocksFree_Type()
)
numBlocksFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksFree.setStatus("current")
_AvgBlockSizeFree_Type = Integer32
_AvgBlockSizeFree_Object = MibScalar
avgBlockSizeFree = _AvgBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 3),
    _AvgBlockSizeFree_Type()
)
avgBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBlockSizeFree.setStatus("current")
_MaxBlockSizeFree_Type = Integer32
_MaxBlockSizeFree_Object = MibScalar
maxBlockSizeFree = _MaxBlockSizeFree_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 4),
    _MaxBlockSizeFree_Type()
)
maxBlockSizeFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maxBlockSizeFree.setStatus("current")
_NumBytesAlloc_Type = Integer32
_NumBytesAlloc_Object = MibScalar
numBytesAlloc = _NumBytesAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 5),
    _NumBytesAlloc_Type()
)
numBytesAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBytesAlloc.setStatus("current")
_NumBlocksAlloc_Type = Integer32
_NumBlocksAlloc_Object = MibScalar
numBlocksAlloc = _NumBlocksAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 6),
    _NumBlocksAlloc_Type()
)
numBlocksAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numBlocksAlloc.setStatus("current")
_AvgBlockSizeAlloc_Type = Integer32
_AvgBlockSizeAlloc_Object = MibScalar
avgBlockSizeAlloc = _AvgBlockSizeAlloc_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 7),
    _AvgBlockSizeAlloc_Type()
)
avgBlockSizeAlloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avgBlockSizeAlloc.setStatus("current")
_MemUtilization_Type = Integer32
_MemUtilization_Object = MibScalar
memUtilization = _MemUtilization_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 5, 8),
    _MemUtilization_Type()
)
memUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memUtilization.setStatus("current")
_SysTask_ObjectIdentity = ObjectIdentity
sysTask = _SysTask_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6)
)
_TaskTable_Object = MibTable
taskTable = _TaskTable_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1)
)
if mibBuilder.loadTexts:
    taskTable.setStatus("current")
_TaskEntry_Object = MibTableRow
taskEntry = _TaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1)
)
taskEntry.setIndexNames(
    (0, "DEVICE-MIB", "taskId"),
)
if mibBuilder.loadTexts:
    taskEntry.setStatus("current")
_TaskId_Type = Integer32
_TaskId_Object = MibTableColumn
taskId = _TaskId_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 1),
    _TaskId_Type()
)
taskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskId.setStatus("current")
_TaskName_Type = DisplayString
_TaskName_Object = MibTableColumn
taskName = _TaskName_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 2),
    _TaskName_Type()
)
taskName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskName.setStatus("current")
_TaskPriority_Type = Integer32
_TaskPriority_Object = MibTableColumn
taskPriority = _TaskPriority_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 3),
    _TaskPriority_Type()
)
taskPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskPriority.setStatus("current")


class _TaskStatus_Type(Integer32):
    """Custom type taskStatus based on Integer32"""
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
        *(("task-delay", 3),
          ("task-deleted", 4),
          ("task-ready", 1),
          ("task-suspended", 2))
    )


_TaskStatus_Type.__name__ = "Integer32"
_TaskStatus_Object = MibTableColumn
taskStatus = _TaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 4),
    _TaskStatus_Type()
)
taskStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskStatus.setStatus("current")
_TaskOptions_Type = Integer32
_TaskOptions_Object = MibTableColumn
taskOptions = _TaskOptions_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 5),
    _TaskOptions_Type()
)
taskOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskOptions.setStatus("current")
_TaskMain_Type = DisplayString
_TaskMain_Object = MibTableColumn
taskMain = _TaskMain_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 6),
    _TaskMain_Type()
)
taskMain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskMain.setStatus("current")
_TaskStackPtr_Type = Unsigned32
_TaskStackPtr_Object = MibTableColumn
taskStackPtr = _TaskStackPtr_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 7),
    _TaskStackPtr_Type()
)
taskStackPtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackPtr.setStatus("current")
_TaskStackBase_Type = Unsigned32
_TaskStackBase_Object = MibTableColumn
taskStackBase = _TaskStackBase_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 8),
    _TaskStackBase_Type()
)
taskStackBase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackBase.setStatus("current")
_TaskStackPos_Type = Unsigned32
_TaskStackPos_Object = MibTableColumn
taskStackPos = _TaskStackPos_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 9),
    _TaskStackPos_Type()
)
taskStackPos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackPos.setStatus("current")
_TaskStackEnd_Type = Unsigned32
_TaskStackEnd_Object = MibTableColumn
taskStackEnd = _TaskStackEnd_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 10),
    _TaskStackEnd_Type()
)
taskStackEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackEnd.setStatus("current")
_TaskStackSize_Type = Unsigned32
_TaskStackSize_Object = MibTableColumn
taskStackSize = _TaskStackSize_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 11),
    _TaskStackSize_Type()
)
taskStackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    taskStackSize.setStatus("current")
_TaskStackSizeUsage_Type = Unsigned32
_TaskStackSizeUsage_Object = MibTableColumn
taskStackSizeUsage = _TaskStackSizeUsage_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 12),
    _TaskStackSizeUsage_Type()
)
taskStackSizeUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackSizeUsage.setStatus("current")
_TaskStackMaxUsed_Type = Unsigned32
_TaskStackMaxUsed_Object = MibTableColumn
taskStackMaxUsed = _TaskStackMaxUsed_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 13),
    _TaskStackMaxUsed_Type()
)
taskStackMaxUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackMaxUsed.setStatus("current")
_TaskStackFree_Type = Unsigned32
_TaskStackFree_Object = MibTableColumn
taskStackFree = _TaskStackFree_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 14),
    _TaskStackFree_Type()
)
taskStackFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskStackFree.setStatus("current")
_TaskErrorStatus_Type = Integer32
_TaskErrorStatus_Object = MibTableColumn
taskErrorStatus = _TaskErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 5812, 1, 6, 1, 1, 15),
    _TaskErrorStatus_Type()
)
taskErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    taskErrorStatus.setStatus("current")

# Managed Objects groups


# Notification objects

emSysLogCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 8)
)
if mibBuilder.loadTexts:
    emSysLogCorrupt.setStatus(
        ""
    )

emSysLogCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 9)
)
if mibBuilder.loadTexts:
    emSysLogCapacity.setStatus(
        ""
    )

emSysLogBackUpDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 10)
)
if mibBuilder.loadTexts:
    emSysLogBackUpDelete.setStatus(
        ""
    )

emSysLogEvIdWrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 11)
)
if mibBuilder.loadTexts:
    emSysLogEvIdWrap.setStatus(
        ""
    )

emErrLogCorrupt = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 14)
)
if mibBuilder.loadTexts:
    emErrLogCorrupt.setStatus(
        ""
    )

emErrLogCapacity = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 15)
)
if mibBuilder.loadTexts:
    emErrLogCapacity.setStatus(
        ""
    )

emErrLogBackUpDelete = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 16)
)
if mibBuilder.loadTexts:
    emErrLogBackUpDelete.setStatus(
        ""
    )

emErrLogEvIdWrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 17)
)
if mibBuilder.loadTexts:
    emErrLogEvIdWrap.setStatus(
        ""
    )

emSysLogsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 18)
)
if mibBuilder.loadTexts:
    emSysLogsCleared.setStatus(
        ""
    )

emErrLogsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 19)
)
if mibBuilder.loadTexts:
    emErrLogsCleared.setStatus(
        ""
    )

systimeClkReferenceChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 23)
)
systimeClkReferenceChange.setObjects(
    ("DEVICE-MIB", "systimeClkReference")
)
if mibBuilder.loadTexts:
    systimeClkReferenceChange.setStatus(
        ""
    )

powerSupplyStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 42)
)
powerSupplyStatusChange.setObjects(
      *(("DEVICE-MIB", "chassisPowerSupplyNumber"),
        ("DEVICE-MIB", "chassisPowerSupplyStatus"))
)
if mibBuilder.loadTexts:
    powerSupplyStatusChange.setStatus(
        ""
    )

fanStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 43)
)
fanStatusChange.setObjects(
    ("DEVICE-MIB", "chassisFanStatus")
)
if mibBuilder.loadTexts:
    fanStatusChange.setStatus(
        ""
    )

ringFWActivate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 51)
)
ringFWActivate.setObjects(
      *(("DEVICE-MIB", "ringFWStatus"),
        ("DEVICE-MIB", "chassisIpAddr"),
        ("DEVICE-MIB", "versionString"))
)
if mibBuilder.loadTexts:
    ringFWActivate.setStatus(
        ""
    )

chassisFWActivate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 52)
)
chassisFWActivate.setObjects(
      *(("DEVICE-MIB", "chassisFWStatus"),
        ("DEVICE-MIB", "chassisIpAddr"),
        ("DEVICE-MIB", "versionString"))
)
if mibBuilder.loadTexts:
    chassisFWActivate.setStatus(
        ""
    )

ringFWUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 53)
)
ringFWUpdate.setObjects(
      *(("DEVICE-MIB", "ringFWStatus"),
        ("DEVICE-MIB", "chassisIpAddr"),
        ("DEVICE-MIB", "ftpServerIP"),
        ("DEVICE-MIB", "controlFilePath"))
)
if mibBuilder.loadTexts:
    ringFWUpdate.setStatus(
        ""
    )

chassisFWUpdate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 54)
)
chassisFWUpdate.setObjects(
      *(("DEVICE-MIB", "chassisFWStatus"),
        ("DEVICE-MIB", "chassisIpAddr"),
        ("DEVICE-MIB", "ftpServerIP"),
        ("DEVICE-MIB", "controlFilePath"))
)
if mibBuilder.loadTexts:
    chassisFWUpdate.setStatus(
        ""
    )

sysLogUnknownEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 57)
)
sysLogUnknownEvent.setObjects(
    ("DEVICE-MIB", "syslogUnknownEvent")
)
if mibBuilder.loadTexts:
    sysLogUnknownEvent.setStatus(
        ""
    )

sysLogUnknownVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 5812, 0, 58)
)
sysLogUnknownVersion.setObjects(
    ("DEVICE-MIB", "syslogUnknownVersion")
)
if mibBuilder.loadTexts:
    sysLogUnknownVersion.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DEVICE-MIB",
    **{"emSysLogCorrupt": emSysLogCorrupt,
       "emSysLogCapacity": emSysLogCapacity,
       "emSysLogBackUpDelete": emSysLogBackUpDelete,
       "emSysLogEvIdWrap": emSysLogEvIdWrap,
       "emErrLogCorrupt": emErrLogCorrupt,
       "emErrLogCapacity": emErrLogCapacity,
       "emErrLogBackUpDelete": emErrLogBackUpDelete,
       "emErrLogEvIdWrap": emErrLogEvIdWrap,
       "emSysLogsCleared": emSysLogsCleared,
       "emErrLogsCleared": emErrLogsCleared,
       "systimeClkReferenceChange": systimeClkReferenceChange,
       "powerSupplyStatusChange": powerSupplyStatusChange,
       "fanStatusChange": fanStatusChange,
       "ringFWActivate": ringFWActivate,
       "chassisFWActivate": chassisFWActivate,
       "ringFWUpdate": ringFWUpdate,
       "chassisFWUpdate": chassisFWUpdate,
       "sysLogUnknownEvent": sysLogUnknownEvent,
       "sysLogUnknownVersion": sysLogUnknownVersion,
       "deviceMIB": deviceMIB,
       "chassis": chassis,
       "chassisAutoConfig": chassisAutoConfig,
       "chassisIpAddr": chassisIpAddr,
       "chassisId": chassisId,
       "chassisCharacter": chassisCharacter,
       "chassisElemReachStatus": chassisElemReachStatus,
       "chassisNumElemReachable": chassisNumElemReachable,
       "chassisCurrentCharacter": chassisCurrentCharacter,
       "chassisFanStatus": chassisFanStatus,
       "chassisPowerSupplyTable": chassisPowerSupplyTable,
       "chassisPowerSupplyEntry": chassisPowerSupplyEntry,
       "chassisPowerSupplyNumber": chassisPowerSupplyNumber,
       "chassisPowerSupplyStatus": chassisPowerSupplyStatus,
       "chassisFWStatus": chassisFWStatus,
       "ringFWStatus": ringFWStatus,
       "ftpServerIP": ftpServerIP,
       "controlFilePath": controlFilePath,
       "versionString": versionString,
       "syslogUnknownEvent": syslogUnknownEvent,
       "syslogUnknownVersion": syslogUnknownVersion,
       "chassisRoutingProt": chassisRoutingProt,
       "chassisSubnetIp": chassisSubnetIp,
       "chassisSubnetMask": chassisSubnetMask,
       "chassisRingsOnMaster": chassisRingsOnMaster,
       "chassisCurrentRingsOnMaster": chassisCurrentRingsOnMaster,
       "chassisFailoverPreserveRings": chassisFailoverPreserveRings,
       "systime": systime,
       "systimeTimingMode": systimeTimingMode,
       "systimePriBITSFraming": systimePriBITSFraming,
       "systimeSecBITSFraming": systimeSecBITSFraming,
       "systimePriBITSCoding": systimePriBITSCoding,
       "systimeSecBITSCoding": systimeSecBITSCoding,
       "systimePriClkSrcId": systimePriClkSrcId,
       "systimeSecClkSrcId": systimeSecClkSrcId,
       "systimeClkReference": systimeClkReference,
       "systimeClkRevertive": systimeClkRevertive,
       "systimeStandbyClkEnable": systimeStandbyClkEnable,
       "systimePriCSNVTime": systimePriCSNVTime,
       "systimeSecCSNVTime": systimeSecCSNVTime,
       "systimePriCSHVTime": systimePriCSHVTime,
       "systimeSecCSHVTime": systimeSecCSHVTime,
       "systimePriCSUseLimit": systimePriCSUseLimit,
       "systimeSecCSUseLimit": systimeSecCSUseLimit,
       "systimeStandbyCSUseLimit": systimeStandbyCSUseLimit,
       "systimePriCSUseInterval": systimePriCSUseInterval,
       "systimeSecCSUseInterval": systimeSecCSUseInterval,
       "systimeStandbyCSUseInterval": systimeStandbyCSUseInterval,
       "systimeCREventEnable": systimeCREventEnable,
       "systimeCRInUse": systimeCRInUse,
       "systimeCRUsedCount": systimeCRUsedCount,
       "deviceNMSTable": deviceNMSTable,
       "deviceNMSEntry": deviceNMSEntry,
       "deviceNMSIndex": deviceNMSIndex,
       "deviceNMSIpAddress": deviceNMSIpAddress,
       "deviceNMSAccessType": deviceNMSAccessType,
       "deviceNMSMIBIITrapList": deviceNMSMIBIITrapList,
       "deviceNMSEnterpriseTrapList": deviceNMSEnterpriseTrapList,
       "deviceNMSTrapSevAllowed": deviceNMSTrapSevAllowed,
       "sysMemory": sysMemory,
       "numBytesFree": numBytesFree,
       "numBlocksFree": numBlocksFree,
       "avgBlockSizeFree": avgBlockSizeFree,
       "maxBlockSizeFree": maxBlockSizeFree,
       "numBytesAlloc": numBytesAlloc,
       "numBlocksAlloc": numBlocksAlloc,
       "avgBlockSizeAlloc": avgBlockSizeAlloc,
       "memUtilization": memUtilization,
       "sysTask": sysTask,
       "taskTable": taskTable,
       "taskEntry": taskEntry,
       "taskId": taskId,
       "taskName": taskName,
       "taskPriority": taskPriority,
       "taskStatus": taskStatus,
       "taskOptions": taskOptions,
       "taskMain": taskMain,
       "taskStackPtr": taskStackPtr,
       "taskStackBase": taskStackBase,
       "taskStackPos": taskStackPos,
       "taskStackEnd": taskStackEnd,
       "taskStackSize": taskStackSize,
       "taskStackSizeUsage": taskStackSizeUsage,
       "taskStackMaxUsed": taskStackMaxUsed,
       "taskStackFree": taskStackFree,
       "taskErrorStatus": taskErrorStatus}
)
