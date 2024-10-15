# SNMP MIB module (COM21-HCXTOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXTOP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:38 2024
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

(com21,
 com21Hcx,
 com21Reg,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Reg",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxCtrl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 1)
)


# Types definitions



class UpstrmFreqKhz(Integer32):
    """Custom type UpstrmFreqKhz based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 40000),
    )





class StuGain(Integer32):
    """Custom type StuGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18, 58),
    )





class EpochTime(Integer32):
    """Custom type EpochTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )





class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )





class Com21RowStatus(Integer32):
    """Custom type Com21RowStatus based on Integer32"""
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
        *(("active", 1),
          ("create", 2),
          ("deactive", 4),
          ("destroy", 3))
    )





class HcxCardType(Integer32):
    """Custom type HcxCardType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("atm25", 9),
          ("atmlSw", 16),
          ("cc", 7),
          ("compactSw", 17),
          ("empty", 10),
          ("eth100bT", 5),
          ("eth10bT8k", 13),
          ("ethDual10bT", 3),
          ("ethQuad10bT", 4),
          ("intConn", 14),
          ("oc3", 8),
          ("rx", 1),
          ("rxm", 15),
          ("tele", 6),
          ("tx", 2),
          ("txDig", 12),
          ("txRf", 11))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxControlGroup_ObjectIdentity = ObjectIdentity
com21HcxControlGroup = _Com21HcxControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2)
)
_HcxMacAddress_Type = MacAddress
_HcxMacAddress_Object = MibScalar
hcxMacAddress = _HcxMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 1),
    _HcxMacAddress_Type()
)
hcxMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxMacAddress.setStatus("current")


class _HcxEncryptionEnable_Type(Integer32):
    """Custom type hcxEncryptionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxEncryptionEnable_Type.__name__ = "Integer32"
_HcxEncryptionEnable_Object = MibScalar
hcxEncryptionEnable = _HcxEncryptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 2),
    _HcxEncryptionEnable_Type()
)
hcxEncryptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEncryptionEnable.setStatus("current")


class _HcxPartNumber_Type(DisplayString):
    """Custom type hcxPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxPartNumber_Type.__name__ = "DisplayString"
_HcxPartNumber_Object = MibScalar
hcxPartNumber = _HcxPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 3),
    _HcxPartNumber_Type()
)
hcxPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPartNumber.setStatus("current")
_HcxEpochTime_Type = EpochTime
_HcxEpochTime_Object = MibScalar
hcxEpochTime = _HcxEpochTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 4),
    _HcxEpochTime_Type()
)
hcxEpochTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEpochTime.setStatus("current")


class _HcxUserText_Type(DisplayString):
    """Custom type hcxUserText based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxUserText_Type.__name__ = "DisplayString"
_HcxUserText_Object = MibScalar
hcxUserText = _HcxUserText_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 5),
    _HcxUserText_Type()
)
hcxUserText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUserText.setStatus("current")


class _HcxSerialNumber_Type(DisplayString):
    """Custom type hcxSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxSerialNumber_Type.__name__ = "DisplayString"
_HcxSerialNumber_Object = MibScalar
hcxSerialNumber = _HcxSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 6),
    _HcxSerialNumber_Type()
)
hcxSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSerialNumber.setStatus("current")
_HcxIpAddress_Type = IpAddress
_HcxIpAddress_Object = MibScalar
hcxIpAddress = _HcxIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 7),
    _HcxIpAddress_Type()
)
hcxIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxIpAddress.setStatus("current")
_HcxGatewayAddress_Type = IpAddress
_HcxGatewayAddress_Object = MibScalar
hcxGatewayAddress = _HcxGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 8),
    _HcxGatewayAddress_Type()
)
hcxGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxGatewayAddress.setStatus("current")


class _HcxRestartAction_Type(Integer32):
    """Custom type hcxRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 3),
          ("nil", 1),
          ("warmStart", 2))
    )


_HcxRestartAction_Type.__name__ = "Integer32"
_HcxRestartAction_Object = MibScalar
hcxRestartAction = _HcxRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 9),
    _HcxRestartAction_Type()
)
hcxRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxRestartAction.setStatus("current")


class _HcxMajorAlarmStatusLed_Type(Integer32):
    """Custom type hcxMajorAlarmStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxMajorAlarmStatusLed_Type.__name__ = "Integer32"
_HcxMajorAlarmStatusLed_Object = MibScalar
hcxMajorAlarmStatusLed = _HcxMajorAlarmStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 10),
    _HcxMajorAlarmStatusLed_Type()
)
hcxMajorAlarmStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxMajorAlarmStatusLed.setStatus("current")


class _HcxMinorAlarmStatusLed_Type(Integer32):
    """Custom type hcxMinorAlarmStatusLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxMinorAlarmStatusLed_Type.__name__ = "Integer32"
_HcxMinorAlarmStatusLed_Object = MibScalar
hcxMinorAlarmStatusLed = _HcxMinorAlarmStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 11),
    _HcxMinorAlarmStatusLed_Type()
)
hcxMinorAlarmStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxMinorAlarmStatusLed.setStatus("current")


class _HcxAutoLoadBalancing_Type(Integer32):
    """Custom type hcxAutoLoadBalancing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxAutoLoadBalancing_Type.__name__ = "Integer32"
_HcxAutoLoadBalancing_Object = MibScalar
hcxAutoLoadBalancing = _HcxAutoLoadBalancing_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 12),
    _HcxAutoLoadBalancing_Type()
)
hcxAutoLoadBalancing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAutoLoadBalancing.setStatus("current")


class _HcxAutoFreqHopping_Type(Integer32):
    """Custom type hcxAutoFreqHopping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_HcxAutoFreqHopping_Type.__name__ = "Integer32"
_HcxAutoFreqHopping_Object = MibScalar
hcxAutoFreqHopping = _HcxAutoFreqHopping_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 13),
    _HcxAutoFreqHopping_Type()
)
hcxAutoFreqHopping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAutoFreqHopping.setStatus("current")


class _HcxKeyRenewalPeriod_Type(Integer32):
    """Custom type hcxKeyRenewalPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8784),
    )


_HcxKeyRenewalPeriod_Type.__name__ = "Integer32"
_HcxKeyRenewalPeriod_Object = MibScalar
hcxKeyRenewalPeriod = _HcxKeyRenewalPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 14),
    _HcxKeyRenewalPeriod_Type()
)
hcxKeyRenewalPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxKeyRenewalPeriod.setStatus("current")


class _HcxHcxSwRelease_Type(DisplayString):
    """Custom type hcxHcxSwRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxHcxSwRelease_Type.__name__ = "DisplayString"
_HcxHcxSwRelease_Object = MibScalar
hcxHcxSwRelease = _HcxHcxSwRelease_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 16),
    _HcxHcxSwRelease_Type()
)
hcxHcxSwRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxHcxSwRelease.setStatus("current")


class _HcxHcxSwDnldResult_Type(Integer32):
    """Custom type hcxHcxSwDnldResult based on Integer32"""
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
        *(("imageNotFound", 4),
          ("inprogress", 1),
          ("serverConnectionLost", 6),
          ("serverNoResponse", 3),
          ("success", 2),
          ("uninitiated", 7),
          ("versionMismatch", 5))
    )


_HcxHcxSwDnldResult_Type.__name__ = "Integer32"
_HcxHcxSwDnldResult_Object = MibScalar
hcxHcxSwDnldResult = _HcxHcxSwDnldResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 18),
    _HcxHcxSwDnldResult_Type()
)
hcxHcxSwDnldResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxHcxSwDnldResult.setStatus("current")


class _HcxCnfgBackupAction_Type(Integer32):
    """Custom type hcxCnfgBackupAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("backupToSaved", 2),
          ("nil", 1),
          ("revertToSaved", 3))
    )


_HcxCnfgBackupAction_Type.__name__ = "Integer32"
_HcxCnfgBackupAction_Object = MibScalar
hcxCnfgBackupAction = _HcxCnfgBackupAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 21),
    _HcxCnfgBackupAction_Type()
)
hcxCnfgBackupAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxCnfgBackupAction.setStatus("current")


class _HcxCnfgBackupResult_Type(Integer32):
    """Custom type hcxCnfgBackupResult based on Integer32"""
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
        *(("inprogress", 1),
          ("serverNoResponse", 3),
          ("success", 2),
          ("uninitiated", 5),
          ("writeFailed", 4))
    )


_HcxCnfgBackupResult_Type.__name__ = "Integer32"
_HcxCnfgBackupResult_Object = MibScalar
hcxCnfgBackupResult = _HcxCnfgBackupResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 22),
    _HcxCnfgBackupResult_Type()
)
hcxCnfgBackupResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxCnfgBackupResult.setStatus("current")


class _HcxPhyConfigType_Type(Integer32):
    """Custom type hcxPhyConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("compactShelf", 3),
          ("fullConfig", 2),
          ("singleShelf", 1))
    )


_HcxPhyConfigType_Type.__name__ = "Integer32"
_HcxPhyConfigType_Object = MibScalar
hcxPhyConfigType = _HcxPhyConfigType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 23),
    _HcxPhyConfigType_Type()
)
hcxPhyConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxPhyConfigType.setStatus("current")


class _HcxNumOfShelves_Type(Integer32):
    """Custom type hcxNumOfShelves based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxNumOfShelves_Type.__name__ = "Integer32"
_HcxNumOfShelves_Object = MibScalar
hcxNumOfShelves = _HcxNumOfShelves_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 24),
    _HcxNumOfShelves_Type()
)
hcxNumOfShelves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxNumOfShelves.setStatus("current")


class _HcxBootpServer_Type(DisplayString):
    """Custom type hcxBootpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxBootpServer_Type.__name__ = "DisplayString"
_HcxBootpServer_Object = MibScalar
hcxBootpServer = _HcxBootpServer_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 25),
    _HcxBootpServer_Type()
)
hcxBootpServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxBootpServer.setStatus("current")


class _HcxBootpResult_Type(Integer32):
    """Custom type hcxBootpResult based on Integer32"""
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
        *(("imageNotFound", 5),
          ("inprogress", 1),
          ("serverConnectionLost", 7),
          ("serverNoResponse", 3),
          ("serverUnknown", 4),
          ("success", 2),
          ("versionMismatch", 6))
    )


_HcxBootpResult_Type.__name__ = "Integer32"
_HcxBootpResult_Object = MibScalar
hcxBootpResult = _HcxBootpResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 26),
    _HcxBootpResult_Type()
)
hcxBootpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxBootpResult.setStatus("current")
_HcxIpMask_Type = IpAddress
_HcxIpMask_Object = MibScalar
hcxIpMask = _HcxIpMask_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 27),
    _HcxIpMask_Type()
)
hcxIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxIpMask.setStatus("current")


class _HcxFreqHopPause_Type(Integer32):
    """Custom type hcxFreqHopPause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_HcxFreqHopPause_Type.__name__ = "Integer32"
_HcxFreqHopPause_Object = MibScalar
hcxFreqHopPause = _HcxFreqHopPause_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 28),
    _HcxFreqHopPause_Type()
)
hcxFreqHopPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxFreqHopPause.setStatus("current")


class _HcxMaxDnstrmCBRAlloc_Type(Integer32):
    """Custom type hcxMaxDnstrmCBRAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxMaxDnstrmCBRAlloc_Type.__name__ = "Integer32"
_HcxMaxDnstrmCBRAlloc_Object = MibScalar
hcxMaxDnstrmCBRAlloc = _HcxMaxDnstrmCBRAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 29),
    _HcxMaxDnstrmCBRAlloc_Type()
)
hcxMaxDnstrmCBRAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxMaxDnstrmCBRAlloc.setStatus("current")


class _HcxMaxUpstrmCBRAlloc_Type(Integer32):
    """Custom type hcxMaxUpstrmCBRAlloc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HcxMaxUpstrmCBRAlloc_Type.__name__ = "Integer32"
_HcxMaxUpstrmCBRAlloc_Object = MibScalar
hcxMaxUpstrmCBRAlloc = _HcxMaxUpstrmCBRAlloc_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 30),
    _HcxMaxUpstrmCBRAlloc_Type()
)
hcxMaxUpstrmCBRAlloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxMaxUpstrmCBRAlloc.setStatus("current")


class _HcxHcxAlternateSwRel_Type(DisplayString):
    """Custom type hcxHcxAlternateSwRel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxHcxAlternateSwRel_Type.__name__ = "DisplayString"
_HcxHcxAlternateSwRel_Object = MibScalar
hcxHcxAlternateSwRel = _HcxHcxAlternateSwRel_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 31),
    _HcxHcxAlternateSwRel_Type()
)
hcxHcxAlternateSwRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxHcxAlternateSwRel.setStatus("current")


class _HcxHcxImageControl_Type(DisplayString):
    """Custom type hcxHcxImageControl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxHcxImageControl_Type.__name__ = "DisplayString"
_HcxHcxImageControl_Object = MibScalar
hcxHcxImageControl = _HcxHcxImageControl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 32),
    _HcxHcxImageControl_Type()
)
hcxHcxImageControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxHcxImageControl.setStatus("current")


class _HcxStatsControl_Type(Integer32):
    """Custom type hcxStatsControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("previousCounts", 1),
          ("wrapCurr", 2))
    )


_HcxStatsControl_Type.__name__ = "Integer32"
_HcxStatsControl_Object = MibScalar
hcxStatsControl = _HcxStatsControl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 33),
    _HcxStatsControl_Type()
)
hcxStatsControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStatsControl.setStatus("current")


class _HcxImageTransfer_Type(DisplayString):
    """Custom type hcxImageTransfer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxImageTransfer_Type.__name__ = "DisplayString"
_HcxImageTransfer_Object = MibScalar
hcxImageTransfer = _HcxImageTransfer_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 34),
    _HcxImageTransfer_Type()
)
hcxImageTransfer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxImageTransfer.setStatus("current")


class _HcxTrapFormat_Type(Integer32):
    """Custom type hcxTrapFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1", 1),
          ("snmpv2", 2))
    )


_HcxTrapFormat_Type.__name__ = "Integer32"
_HcxTrapFormat_Object = MibScalar
hcxTrapFormat = _HcxTrapFormat_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 35),
    _HcxTrapFormat_Type()
)
hcxTrapFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxTrapFormat.setStatus("current")


class _HcxSyncClkConfigure_Type(Integer32):
    """Custom type hcxSyncClkConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalClk", 1),
          ("networkClk", 2))
    )


_HcxSyncClkConfigure_Type.__name__ = "Integer32"
_HcxSyncClkConfigure_Object = MibScalar
hcxSyncClkConfigure = _HcxSyncClkConfigure_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 36),
    _HcxSyncClkConfigure_Type()
)
hcxSyncClkConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxSyncClkConfigure.setStatus("current")


class _HcxSyncClkSelect_Type(Integer32):
    """Custom type hcxSyncClkSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalClk", 1),
          ("priNetworkClk", 2),
          ("secNetworkClk", 3))
    )


_HcxSyncClkSelect_Type.__name__ = "Integer32"
_HcxSyncClkSelect_Object = MibScalar
hcxSyncClkSelect = _HcxSyncClkSelect_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 2, 37),
    _HcxSyncClkSelect_Type()
)
hcxSyncClkSelect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSyncClkSelect.setStatus("current")
_Com21HcxAcqCnfgGroup_ObjectIdentity = ObjectIdentity
com21HcxAcqCnfgGroup = _Com21HcxAcqCnfgGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3)
)
_HcxAcquisitionFreq_Type = UpstrmFreqKhz
_HcxAcquisitionFreq_Object = MibScalar
hcxAcquisitionFreq = _HcxAcquisitionFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3, 1),
    _HcxAcquisitionFreq_Type()
)
hcxAcquisitionFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAcquisitionFreq.setStatus("deprecated")
_HcxAcqMinPower_Type = StuGain
_HcxAcqMinPower_Object = MibScalar
hcxAcqMinPower = _HcxAcqMinPower_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3, 6),
    _HcxAcqMinPower_Type()
)
hcxAcqMinPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAcqMinPower.setStatus("current")
_HcxAcqMaxPower_Type = StuGain
_HcxAcqMaxPower_Object = MibScalar
hcxAcqMaxPower = _HcxAcqMaxPower_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3, 7),
    _HcxAcqMaxPower_Type()
)
hcxAcqMaxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAcqMaxPower.setStatus("current")


class _HcxAcqPowerStepSize_Type(Integer32):
    """Custom type hcxAcqPowerStepSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_HcxAcqPowerStepSize_Type.__name__ = "Integer32"
_HcxAcqPowerStepSize_Object = MibScalar
hcxAcqPowerStepSize = _HcxAcqPowerStepSize_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3, 8),
    _HcxAcqPowerStepSize_Type()
)
hcxAcqPowerStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAcqPowerStepSize.setStatus("current")


class _HcxAltAcqFreq_Type(Integer32):
    """Custom type hcxAltAcqFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40000),
    )


_HcxAltAcqFreq_Type.__name__ = "Integer32"
_HcxAltAcqFreq_Object = MibScalar
hcxAltAcqFreq = _HcxAltAcqFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3, 9),
    _HcxAltAcqFreq_Type()
)
hcxAltAcqFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxAltAcqFreq.setStatus("deprecated")
_HcxActiveAcqFreq_Type = UpstrmFreqKhz
_HcxActiveAcqFreq_Object = MibScalar
hcxActiveAcqFreq = _HcxActiveAcqFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 3, 10),
    _HcxActiveAcqFreq_Type()
)
hcxActiveAcqFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxActiveAcqFreq.setStatus("deprecated")
_Com21HcxAlmOverGroup_ObjectIdentity = ObjectIdentity
com21HcxAlmOverGroup = _Com21HcxAlmOverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 4)
)


class _HcxNoCurrAlarms_Type(Integer32):
    """Custom type hcxNoCurrAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HcxNoCurrAlarms_Type.__name__ = "Integer32"
_HcxNoCurrAlarms_Object = MibScalar
hcxNoCurrAlarms = _HcxNoCurrAlarms_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 4, 1),
    _HcxNoCurrAlarms_Type()
)
hcxNoCurrAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxNoCurrAlarms.setStatus("current")


class _HcxEventLogSize_Type(Integer32):
    """Custom type hcxEventLogSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_HcxEventLogSize_Type.__name__ = "Integer32"
_HcxEventLogSize_Object = MibScalar
hcxEventLogSize = _HcxEventLogSize_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 4, 2),
    _HcxEventLogSize_Type()
)
hcxEventLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxEventLogSize.setStatus("current")
_Com21HcxStuOverGroup_ObjectIdentity = ObjectIdentity
com21HcxStuOverGroup = _Com21HcxStuOverGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5)
)


class _HcxNumConfiguredStus_Type(Integer32):
    """Custom type hcxNumConfiguredStus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_HcxNumConfiguredStus_Type.__name__ = "Integer32"
_HcxNumConfiguredStus_Object = MibScalar
hcxNumConfiguredStus = _HcxNumConfiguredStus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 1),
    _HcxNumConfiguredStus_Type()
)
hcxNumConfiguredStus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxNumConfiguredStus.setStatus("current")


class _HcxNumAcquiredStus_Type(Integer32):
    """Custom type hcxNumAcquiredStus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_HcxNumAcquiredStus_Type.__name__ = "Integer32"
_HcxNumAcquiredStus_Object = MibScalar
hcxNumAcquiredStus = _HcxNumAcquiredStus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 2),
    _HcxNumAcquiredStus_Type()
)
hcxNumAcquiredStus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxNumAcquiredStus.setStatus("current")
_HcxLastStuTopolgyChng_Type = EpochTime
_HcxLastStuTopolgyChng_Object = MibScalar
hcxLastStuTopolgyChng = _HcxLastStuTopolgyChng_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 3),
    _HcxLastStuTopolgyChng_Type()
)
hcxLastStuTopolgyChng.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxLastStuTopolgyChng.setStatus("current")


class _HcxNumEnabledStus_Type(Integer32):
    """Custom type hcxNumEnabledStus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_HcxNumEnabledStus_Type.__name__ = "Integer32"
_HcxNumEnabledStus_Object = MibScalar
hcxNumEnabledStus = _HcxNumEnabledStus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 4),
    _HcxNumEnabledStus_Type()
)
hcxNumEnabledStus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxNumEnabledStus.setStatus("current")
_HcxStuAggrUpStrmCbrRate_Type = Integer32
_HcxStuAggrUpStrmCbrRate_Object = MibScalar
hcxStuAggrUpStrmCbrRate = _HcxStuAggrUpStrmCbrRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 5),
    _HcxStuAggrUpStrmCbrRate_Type()
)
hcxStuAggrUpStrmCbrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuAggrUpStrmCbrRate.setStatus("current")
_HcxStuAggrUpStrmMinRate_Type = Integer32
_HcxStuAggrUpStrmMinRate_Object = MibScalar
hcxStuAggrUpStrmMinRate = _HcxStuAggrUpStrmMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 6),
    _HcxStuAggrUpStrmMinRate_Type()
)
hcxStuAggrUpStrmMinRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuAggrUpStrmMinRate.setStatus("current")
_HcxStuAggrUpStrmMaxRate_Type = Integer32
_HcxStuAggrUpStrmMaxRate_Object = MibScalar
hcxStuAggrUpStrmMaxRate = _HcxStuAggrUpStrmMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 7),
    _HcxStuAggrUpStrmMaxRate_Type()
)
hcxStuAggrUpStrmMaxRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuAggrUpStrmMaxRate.setStatus("current")


class _HcxStuAltDownFreq_Type(Integer32):
    """Custom type hcxStuAltDownFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(88000, 800000),
    )


_HcxStuAltDownFreq_Type.__name__ = "Integer32"
_HcxStuAltDownFreq_Object = MibScalar
hcxStuAltDownFreq = _HcxStuAltDownFreq_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 9),
    _HcxStuAltDownFreq_Type()
)
hcxStuAltDownFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAltDownFreq.setStatus("current")


class _HcxStuAcqTrapEnable_Type(Integer32):
    """Custom type hcxStuAcqTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acqTrapOnly", 2),
          ("bothTopoAndAcqTrap", 3),
          ("topoChgTrapOnly", 1))
    )


_HcxStuAcqTrapEnable_Type.__name__ = "Integer32"
_HcxStuAcqTrapEnable_Object = MibScalar
hcxStuAcqTrapEnable = _HcxStuAcqTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 11),
    _HcxStuAcqTrapEnable_Type()
)
hcxStuAcqTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAcqTrapEnable.setStatus("current")


class _HcxStuRpcEnable_Type(Integer32):
    """Custom type hcxStuRpcEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuRpcEnable_Type.__name__ = "Integer32"
_HcxStuRpcEnable_Object = MibScalar
hcxStuRpcEnable = _HcxStuRpcEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 12),
    _HcxStuRpcEnable_Type()
)
hcxStuRpcEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuRpcEnable.setStatus("current")


class _HcxStuAutoDiscEnable_Type(Integer32):
    """Custom type hcxStuAutoDiscEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuAutoDiscEnable_Type.__name__ = "Integer32"
_HcxStuAutoDiscEnable_Object = MibScalar
hcxStuAutoDiscEnable = _HcxStuAutoDiscEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 13),
    _HcxStuAutoDiscEnable_Type()
)
hcxStuAutoDiscEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAutoDiscEnable.setStatus("current")
_HcxStuAutoDiscIpAddr_Type = IpAddress
_HcxStuAutoDiscIpAddr_Object = MibScalar
hcxStuAutoDiscIpAddr = _HcxStuAutoDiscIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 14),
    _HcxStuAutoDiscIpAddr_Type()
)
hcxStuAutoDiscIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAutoDiscIpAddr.setStatus("current")


class _HcxStuAutoGainAdjust_Type(Integer32):
    """Custom type hcxStuAutoGainAdjust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxStuAutoGainAdjust_Type.__name__ = "Integer32"
_HcxStuAutoGainAdjust_Object = MibScalar
hcxStuAutoGainAdjust = _HcxStuAutoGainAdjust_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 15),
    _HcxStuAutoGainAdjust_Type()
)
hcxStuAutoGainAdjust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAutoGainAdjust.setStatus("current")


class _HcxStuAltDownFreqEnable_Type(Integer32):
    """Custom type hcxStuAltDownFreqEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_HcxStuAltDownFreqEnable_Type.__name__ = "Integer32"
_HcxStuAltDownFreqEnable_Object = MibScalar
hcxStuAltDownFreqEnable = _HcxStuAltDownFreqEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 16),
    _HcxStuAltDownFreqEnable_Type()
)
hcxStuAltDownFreqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuAltDownFreqEnable.setStatus("current")
_HcxStuPcMacAddress_Type = MacAddress
_HcxStuPcMacAddress_Object = MibScalar
hcxStuPcMacAddress = _HcxStuPcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 17),
    _HcxStuPcMacAddress_Type()
)
hcxStuPcMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuPcMacAddress.setStatus("current")


class _HcxStuPcToStuMacAddressResult_Type(Integer32):
    """Custom type hcxStuPcToStuMacAddressResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 3),
          ("inprogress", 1),
          ("success", 2))
    )


_HcxStuPcToStuMacAddressResult_Type.__name__ = "Integer32"
_HcxStuPcToStuMacAddressResult_Object = MibScalar
hcxStuPcToStuMacAddressResult = _HcxStuPcToStuMacAddressResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 18),
    _HcxStuPcToStuMacAddressResult_Type()
)
hcxStuPcToStuMacAddressResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuPcToStuMacAddressResult.setStatus("current")
_HcxStuOverMacAddress_Type = MacAddress
_HcxStuOverMacAddress_Object = MibScalar
hcxStuOverMacAddress = _HcxStuOverMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 19),
    _HcxStuOverMacAddress_Type()
)
hcxStuOverMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStuOverMacAddress.setStatus("current")


class _HcxStuGlobalSwImage_Type(DisplayString):
    """Custom type hcxStuGlobalSwImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxStuGlobalSwImage_Type.__name__ = "DisplayString"
_HcxStuGlobalSwImage_Object = MibScalar
hcxStuGlobalSwImage = _HcxStuGlobalSwImage_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 5, 20),
    _HcxStuGlobalSwImage_Type()
)
hcxStuGlobalSwImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuGlobalSwImage.setStatus("current")
_Com21HcxTrapRcvrGroup_ObjectIdentity = ObjectIdentity
com21HcxTrapRcvrGroup = _Com21HcxTrapRcvrGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6)
)
_HcxTrapReceiverTable_Object = MibTable
hcxTrapReceiverTable = _HcxTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6, 1)
)
if mibBuilder.loadTexts:
    hcxTrapReceiverTable.setStatus("current")
_HcxTrapReceiverEntry_Object = MibTableRow
hcxTrapReceiverEntry = _HcxTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6, 1, 1)
)
hcxTrapReceiverEntry.setIndexNames(
    (0, "COM21-HCXTOP-MIB", "hcxTrapRcvrNetAddress"),
)
if mibBuilder.loadTexts:
    hcxTrapReceiverEntry.setStatus("current")


class _HcxTrapRcvrStatus_Type(Integer32):
    """Custom type hcxTrapRcvrStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("delete", 3),
          ("invalid", 2),
          ("valid", 1))
    )


_HcxTrapRcvrStatus_Type.__name__ = "Integer32"
_HcxTrapRcvrStatus_Object = MibTableColumn
hcxTrapRcvrStatus = _HcxTrapRcvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6, 1, 1, 1),
    _HcxTrapRcvrStatus_Type()
)
hcxTrapRcvrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxTrapRcvrStatus.setStatus("current")
_HcxTrapRcvrNetAddress_Type = IpAddress
_HcxTrapRcvrNetAddress_Object = MibTableColumn
hcxTrapRcvrNetAddress = _HcxTrapRcvrNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6, 1, 1, 2),
    _HcxTrapRcvrNetAddress_Type()
)
hcxTrapRcvrNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxTrapRcvrNetAddress.setStatus("current")


class _HcxTrapRcvrComm_Type(OctetString):
    """Custom type hcxTrapRcvrComm based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HcxTrapRcvrComm_Type.__name__ = "OctetString"
_HcxTrapRcvrComm_Object = MibTableColumn
hcxTrapRcvrComm = _HcxTrapRcvrComm_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6, 1, 1, 3),
    _HcxTrapRcvrComm_Type()
)
hcxTrapRcvrComm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxTrapRcvrComm.setStatus("current")
_HcxTrapRcvrAgeTime_Type = TimeTicks
_HcxTrapRcvrAgeTime_Object = MibTableColumn
hcxTrapRcvrAgeTime = _HcxTrapRcvrAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 6, 1, 1, 4),
    _HcxTrapRcvrAgeTime_Type()
)
hcxTrapRcvrAgeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxTrapRcvrAgeTime.setStatus("current")
_Com21HcxShelfGroup_ObjectIdentity = ObjectIdentity
com21HcxShelfGroup = _Com21HcxShelfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 7)
)
_Com21HcxShelfTable_Object = MibTable
com21HcxShelfTable = _Com21HcxShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 7, 1)
)
if mibBuilder.loadTexts:
    com21HcxShelfTable.setStatus("current")
_Com21HcxShelfEntry_Object = MibTableRow
com21HcxShelfEntry = _Com21HcxShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 7, 1, 1)
)
com21HcxShelfEntry.setIndexNames(
    (0, "COM21-HCXTOP-MIB", "hcxShelfId"),
)
if mibBuilder.loadTexts:
    com21HcxShelfEntry.setStatus("current")


class _HcxShelfId_Type(Integer32):
    """Custom type hcxShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxShelfId_Type.__name__ = "Integer32"
_HcxShelfId_Object = MibTableColumn
hcxShelfId = _HcxShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 7, 1, 1, 1),
    _HcxShelfId_Type()
)
hcxShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxShelfId.setStatus("current")
_HcxShelfNoSlots_Type = Integer32
_HcxShelfNoSlots_Object = MibTableColumn
hcxShelfNoSlots = _HcxShelfNoSlots_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 7, 1, 1, 2),
    _HcxShelfNoSlots_Type()
)
hcxShelfNoSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxShelfNoSlots.setStatus("current")
_Com21HcxSlotGroup_ObjectIdentity = ObjectIdentity
com21HcxSlotGroup = _Com21HcxSlotGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8)
)
_Com21HcxSlotTable_Object = MibTable
com21HcxSlotTable = _Com21HcxSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1)
)
if mibBuilder.loadTexts:
    com21HcxSlotTable.setStatus("current")
_Com21HcxSlotEntry_Object = MibTableRow
com21HcxSlotEntry = _Com21HcxSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1, 1)
)
com21HcxSlotEntry.setIndexNames(
    (0, "COM21-HCXTOP-MIB", "hcxShelfNo"),
    (0, "COM21-HCXTOP-MIB", "hcxSlotId"),
)
if mibBuilder.loadTexts:
    com21HcxSlotEntry.setStatus("current")


class _HcxShelfNo_Type(Integer32):
    """Custom type hcxShelfNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxShelfNo_Type.__name__ = "Integer32"
_HcxShelfNo_Object = MibTableColumn
hcxShelfNo = _HcxShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1, 1, 1),
    _HcxShelfNo_Type()
)
hcxShelfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxShelfNo.setStatus("current")


class _HcxSlotId_Type(Integer32):
    """Custom type hcxSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_HcxSlotId_Type.__name__ = "Integer32"
_HcxSlotId_Object = MibTableColumn
hcxSlotId = _HcxSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1, 1, 2),
    _HcxSlotId_Type()
)
hcxSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSlotId.setStatus("current")


class _HcxSlotSupportedTypes_Type(Integer32):
    """Custom type hcxSlotSupportedTypes based on Integer32"""
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("cc", 3),
          ("com21Exp", 4),
          ("intConn", 6),
          ("noCard", 8),
          ("rx", 1),
          ("rxCom21Exp", 9),
          ("rxIntConn", 7),
          ("tx", 2),
          ("txDig", 5))
    )


_HcxSlotSupportedTypes_Type.__name__ = "Integer32"
_HcxSlotSupportedTypes_Object = MibTableColumn
hcxSlotSupportedTypes = _HcxSlotSupportedTypes_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1, 1, 3),
    _HcxSlotSupportedTypes_Type()
)
hcxSlotSupportedTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSlotSupportedTypes.setStatus("current")
_HcxSlotConfigCardType_Type = HcxCardType
_HcxSlotConfigCardType_Object = MibTableColumn
hcxSlotConfigCardType = _HcxSlotConfigCardType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1, 1, 4),
    _HcxSlotConfigCardType_Type()
)
hcxSlotConfigCardType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxSlotConfigCardType.setStatus("current")
_HcxSlotInsertCardType_Type = HcxCardType
_HcxSlotInsertCardType_Object = MibTableColumn
hcxSlotInsertCardType = _HcxSlotInsertCardType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 8, 1, 1, 5),
    _HcxSlotInsertCardType_Type()
)
hcxSlotInsertCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSlotInsertCardType.setStatus("current")
_Com21HcxImageListGroup_ObjectIdentity = ObjectIdentity
com21HcxImageListGroup = _Com21HcxImageListGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9)
)
_Com21HcxImageListTable_Object = MibTable
com21HcxImageListTable = _Com21HcxImageListTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1)
)
if mibBuilder.loadTexts:
    com21HcxImageListTable.setStatus("current")
_Com21HcxImageListEntry_Object = MibTableRow
com21HcxImageListEntry = _Com21HcxImageListEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1)
)
com21HcxImageListEntry.setIndexNames(
    (0, "COM21-HCXTOP-MIB", "hcxImageId"),
)
if mibBuilder.loadTexts:
    com21HcxImageListEntry.setStatus("current")


class _HcxImageId_Type(Integer32):
    """Custom type hcxImageId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_HcxImageId_Type.__name__ = "Integer32"
_HcxImageId_Object = MibTableColumn
hcxImageId = _HcxImageId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 1),
    _HcxImageId_Type()
)
hcxImageId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxImageId.setStatus("current")


class _HcxImageType_Type(Integer32):
    """Custom type hcxImageType based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("atmlSwitch", 10),
          ("compCfg", 11),
          ("compSwitch", 12),
          ("hcxCC", 1),
          ("hcxEth100baseT", 5),
          ("hcxEth10baseT", 4),
          ("hcxOc3", 13),
          ("hcxRx", 3),
          ("hcxRxm", 9),
          ("hcxTele", 6),
          ("hcxTx", 2),
          ("stu", 7),
          ("stu3com", 8))
    )


_HcxImageType_Type.__name__ = "Integer32"
_HcxImageType_Object = MibTableColumn
hcxImageType = _HcxImageType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 2),
    _HcxImageType_Type()
)
hcxImageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxImageType.setStatus("current")


class _HcxImageFilename_Type(DisplayString):
    """Custom type hcxImageFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )


_HcxImageFilename_Type.__name__ = "DisplayString"
_HcxImageFilename_Object = MibTableColumn
hcxImageFilename = _HcxImageFilename_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 3),
    _HcxImageFilename_Type()
)
hcxImageFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxImageFilename.setStatus("current")


class _HcxSwRevision_Type(DisplayString):
    """Custom type hcxSwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxSwRevision_Type.__name__ = "DisplayString"
_HcxSwRevision_Object = MibTableColumn
hcxSwRevision = _HcxSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 4),
    _HcxSwRevision_Type()
)
hcxSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxSwRevision.setStatus("current")


class _HcxHwRevision_Type(DisplayString):
    """Custom type hcxHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxHwRevision_Type.__name__ = "DisplayString"
_HcxHwRevision_Object = MibTableColumn
hcxHwRevision = _HcxHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 5),
    _HcxHwRevision_Type()
)
hcxHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxHwRevision.setStatus("current")


class _HcxFwRevision_Type(DisplayString):
    """Custom type hcxFwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxFwRevision_Type.__name__ = "DisplayString"
_HcxFwRevision_Object = MibTableColumn
hcxFwRevision = _HcxFwRevision_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 6),
    _HcxFwRevision_Type()
)
hcxFwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxFwRevision.setStatus("current")


class _HcxImageState_Type(Integer32):
    """Custom type hcxImageState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("alternate", 2))
    )


_HcxImageState_Type.__name__ = "Integer32"
_HcxImageState_Object = MibTableColumn
hcxImageState = _HcxImageState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 9, 1, 1, 7),
    _HcxImageState_Type()
)
hcxImageState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxImageState.setStatus("current")
_Com21HcxServTypeGroup_ObjectIdentity = ObjectIdentity
com21HcxServTypeGroup = _Com21HcxServTypeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10)
)
_Com21HcxServTypeTable_Object = MibTable
com21HcxServTypeTable = _Com21HcxServTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1)
)
if mibBuilder.loadTexts:
    com21HcxServTypeTable.setStatus("current")
_Com21HcxServTypeEntry_Object = MibTableRow
com21HcxServTypeEntry = _Com21HcxServTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1)
)
com21HcxServTypeEntry.setIndexNames(
    (0, "COM21-HCXTOP-MIB", "hcxServiceTypeId"),
)
if mibBuilder.loadTexts:
    com21HcxServTypeEntry.setStatus("current")
_HcxServiceTypeId_Type = Integer32
_HcxServiceTypeId_Object = MibTableColumn
hcxServiceTypeId = _HcxServiceTypeId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 1),
    _HcxServiceTypeId_Type()
)
hcxServiceTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxServiceTypeId.setStatus("current")


class _HcxServTypeDesc_Type(DisplayString):
    """Custom type hcxServTypeDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxServTypeDesc_Type.__name__ = "DisplayString"
_HcxServTypeDesc_Object = MibTableColumn
hcxServTypeDesc = _HcxServTypeDesc_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 2),
    _HcxServTypeDesc_Type()
)
hcxServTypeDesc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxServTypeDesc.setStatus("current")


class _HcxDnStrmType_Type(Integer32):
    """Custom type hcxDnStrmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ondemand", 2))
    )


_HcxDnStrmType_Type.__name__ = "Integer32"
_HcxDnStrmType_Object = MibTableColumn
hcxDnStrmType = _HcxDnStrmType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 3),
    _HcxDnStrmType_Type()
)
hcxDnStrmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDnStrmType.setStatus("current")


class _HcxDnStrmRate_Type(Integer32):
    """Custom type hcxDnStrmRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 11560000),
    )


_HcxDnStrmRate_Type.__name__ = "Integer32"
_HcxDnStrmRate_Object = MibTableColumn
hcxDnStrmRate = _HcxDnStrmRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 4),
    _HcxDnStrmRate_Type()
)
hcxDnStrmRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDnStrmRate.setStatus("current")


class _HcxUpStrmType_Type(Integer32):
    """Custom type hcxUpStrmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("ondemand", 2))
    )


_HcxUpStrmType_Type.__name__ = "Integer32"
_HcxUpStrmType_Object = MibTableColumn
hcxUpStrmType = _HcxUpStrmType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 5),
    _HcxUpStrmType_Type()
)
hcxUpStrmType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpStrmType.setStatus("current")


class _HcxUpStrmMinRate_Type(Integer32):
    """Custom type hcxUpStrmMinRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1650000),
    )


_HcxUpStrmMinRate_Type.__name__ = "Integer32"
_HcxUpStrmMinRate_Object = MibTableColumn
hcxUpStrmMinRate = _HcxUpStrmMinRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 6),
    _HcxUpStrmMinRate_Type()
)
hcxUpStrmMinRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpStrmMinRate.setStatus("current")


class _HcxUpStrmMaxRate_Type(Integer32):
    """Custom type hcxUpStrmMaxRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1650000),
    )


_HcxUpStrmMaxRate_Type.__name__ = "Integer32"
_HcxUpStrmMaxRate_Object = MibTableColumn
hcxUpStrmMaxRate = _HcxUpStrmMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 7),
    _HcxUpStrmMaxRate_Type()
)
hcxUpStrmMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxUpStrmMaxRate.setStatus("current")


class _HcxServTypeDelete_Type(Integer32):
    """Custom type hcxServTypeDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxServTypeDelete_Type.__name__ = "Integer32"
_HcxServTypeDelete_Object = MibTableColumn
hcxServTypeDelete = _HcxServTypeDelete_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 10, 1, 1, 8),
    _HcxServTypeDelete_Type()
)
hcxServTypeDelete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hcxServTypeDelete.setStatus("current")
_Com21HcxArpFiltTrapGroup_ObjectIdentity = ObjectIdentity
com21HcxArpFiltTrapGroup = _Com21HcxArpFiltTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 12)
)


class _HcxArpServerTrapEnable_Type(Integer32):
    """Custom type hcxArpServerTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxArpServerTrapEnable_Type.__name__ = "Integer32"
_HcxArpServerTrapEnable_Object = MibScalar
hcxArpServerTrapEnable = _HcxArpServerTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 12, 1),
    _HcxArpServerTrapEnable_Type()
)
hcxArpServerTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxArpServerTrapEnable.setStatus("current")


class _HcxArpUserTrapEnable_Type(Integer32):
    """Custom type hcxArpUserTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxArpUserTrapEnable_Type.__name__ = "Integer32"
_HcxArpUserTrapEnable_Object = MibScalar
hcxArpUserTrapEnable = _HcxArpUserTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 12, 2),
    _HcxArpUserTrapEnable_Type()
)
hcxArpUserTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxArpUserTrapEnable.setStatus("current")
_Com21HcxStuDefaultGroup_ObjectIdentity = ObjectIdentity
com21HcxStuDefaultGroup = _Com21HcxStuDefaultGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 13)
)


class _HcxStuDefaultAuth_Type(Integer32):
    """Custom type hcxStuDefaultAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_HcxStuDefaultAuth_Type.__name__ = "Integer32"
_HcxStuDefaultAuth_Object = MibScalar
hcxStuDefaultAuth = _HcxStuDefaultAuth_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 13, 1),
    _HcxStuDefaultAuth_Type()
)
hcxStuDefaultAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDefaultAuth.setStatus("current")


class _HcxStuDefaultServType_Type(Integer32):
    """Custom type hcxStuDefaultServType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_HcxStuDefaultServType_Type.__name__ = "Integer32"
_HcxStuDefaultServType_Object = MibScalar
hcxStuDefaultServType = _HcxStuDefaultServType_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 13, 2),
    _HcxStuDefaultServType_Type()
)
hcxStuDefaultServType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDefaultServType.setStatus("current")


class _HcxStuDefaultVlan_Type(Integer32):
    """Custom type hcxStuDefaultVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HcxStuDefaultVlan_Type.__name__ = "Integer32"
_HcxStuDefaultVlan_Object = MibScalar
hcxStuDefaultVlan = _HcxStuDefaultVlan_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 13, 3),
    _HcxStuDefaultVlan_Type()
)
hcxStuDefaultVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDefaultVlan.setStatus("current")


class _HcxStuDefCom21SwImage_Type(DisplayString):
    """Custom type hcxStuDefCom21SwImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxStuDefCom21SwImage_Type.__name__ = "DisplayString"
_HcxStuDefCom21SwImage_Object = MibScalar
hcxStuDefCom21SwImage = _HcxStuDefCom21SwImage_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 13, 4),
    _HcxStuDefCom21SwImage_Type()
)
hcxStuDefCom21SwImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDefCom21SwImage.setStatus("current")


class _HcxStuDef3ComSwImage_Type(DisplayString):
    """Custom type hcxStuDef3ComSwImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxStuDef3ComSwImage_Type.__name__ = "DisplayString"
_HcxStuDef3ComSwImage_Object = MibScalar
hcxStuDef3ComSwImage = _HcxStuDef3ComSwImage_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 13, 5),
    _HcxStuDef3ComSwImage_Type()
)
hcxStuDef3ComSwImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStuDef3ComSwImage.setStatus("current")
_Com21HcxDbControlGroup_ObjectIdentity = ObjectIdentity
com21HcxDbControlGroup = _Com21HcxDbControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 14)
)


class _HcxDbAction_Type(Integer32):
    """Custom type hcxDbAction based on Integer32"""
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
        *(("deletePeriodicDb", 4),
          ("deleteSavedDb", 3),
          ("nil", 1),
          ("revertToPeriodicDb", 5),
          ("revertToSavedDb", 6),
          ("saveDb", 2))
    )


_HcxDbAction_Type.__name__ = "Integer32"
_HcxDbAction_Object = MibScalar
hcxDbAction = _HcxDbAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 14, 1),
    _HcxDbAction_Type()
)
hcxDbAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDbAction.setStatus("current")


class _HcxDbActionResult_Type(Integer32):
    """Custom type hcxDbActionResult based on Integer32"""
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
        *(("diskFailure", 3),
          ("inprogress", 1),
          ("invalidDatabase", 5),
          ("noDatabaseFound", 4),
          ("success", 2))
    )


_HcxDbActionResult_Type.__name__ = "Integer32"
_HcxDbActionResult_Object = MibScalar
hcxDbActionResult = _HcxDbActionResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 14, 2),
    _HcxDbActionResult_Type()
)
hcxDbActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDbActionResult.setStatus("current")


class _HcxDbBackupPeriod_Type(Integer32):
    """Custom type hcxDbBackupPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_HcxDbBackupPeriod_Type.__name__ = "Integer32"
_HcxDbBackupPeriod_Object = MibScalar
hcxDbBackupPeriod = _HcxDbBackupPeriod_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 14, 3),
    _HcxDbBackupPeriod_Type()
)
hcxDbBackupPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDbBackupPeriod.setStatus("current")
_Com21HcxBootControlGroup_ObjectIdentity = ObjectIdentity
com21HcxBootControlGroup = _Com21HcxBootControlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18)
)


class _HcxFileTransProt_Type(Integer32):
    """Custom type hcxFileTransProt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("tftp", 2))
    )


_HcxFileTransProt_Type.__name__ = "Integer32"
_HcxFileTransProt_Object = MibScalar
hcxFileTransProt = _HcxFileTransProt_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 1),
    _HcxFileTransProt_Type()
)
hcxFileTransProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxFileTransProt.setStatus("current")


class _HcxFileServerCntrl_Type(Integer32):
    """Custom type hcxFileServerCntrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 1),
          ("mibSpecified", 2))
    )


_HcxFileServerCntrl_Type.__name__ = "Integer32"
_HcxFileServerCntrl_Object = MibScalar
hcxFileServerCntrl = _HcxFileServerCntrl_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 2),
    _HcxFileServerCntrl_Type()
)
hcxFileServerCntrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxFileServerCntrl.setStatus("current")
_HcxImageServerIpAddr_Type = IpAddress
_HcxImageServerIpAddr_Object = MibScalar
hcxImageServerIpAddr = _HcxImageServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 3),
    _HcxImageServerIpAddr_Type()
)
hcxImageServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxImageServerIpAddr.setStatus("current")


class _HcxImageServerPath_Type(DisplayString):
    """Custom type hcxImageServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxImageServerPath_Type.__name__ = "DisplayString"
_HcxImageServerPath_Object = MibScalar
hcxImageServerPath = _HcxImageServerPath_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 4),
    _HcxImageServerPath_Type()
)
hcxImageServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxImageServerPath.setStatus("current")


class _HcxImageServerLogin_Type(DisplayString):
    """Custom type hcxImageServerLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxImageServerLogin_Type.__name__ = "DisplayString"
_HcxImageServerLogin_Object = MibScalar
hcxImageServerLogin = _HcxImageServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 5),
    _HcxImageServerLogin_Type()
)
hcxImageServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxImageServerLogin.setStatus("current")


class _HcxImageServerPassword_Type(DisplayString):
    """Custom type hcxImageServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxImageServerPassword_Type.__name__ = "DisplayString"
_HcxImageServerPassword_Object = MibScalar
hcxImageServerPassword = _HcxImageServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 6),
    _HcxImageServerPassword_Type()
)
hcxImageServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxImageServerPassword.setStatus("current")
_HcxDatabaseServerIpAddr_Type = IpAddress
_HcxDatabaseServerIpAddr_Object = MibScalar
hcxDatabaseServerIpAddr = _HcxDatabaseServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 7),
    _HcxDatabaseServerIpAddr_Type()
)
hcxDatabaseServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDatabaseServerIpAddr.setStatus("current")


class _HcxDatabaseServerPath_Type(DisplayString):
    """Custom type hcxDatabaseServerPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )


_HcxDatabaseServerPath_Type.__name__ = "DisplayString"
_HcxDatabaseServerPath_Object = MibScalar
hcxDatabaseServerPath = _HcxDatabaseServerPath_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 8),
    _HcxDatabaseServerPath_Type()
)
hcxDatabaseServerPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDatabaseServerPath.setStatus("current")


class _HcxDatabaseServerLogin_Type(DisplayString):
    """Custom type hcxDatabaseServerLogin based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxDatabaseServerLogin_Type.__name__ = "DisplayString"
_HcxDatabaseServerLogin_Object = MibScalar
hcxDatabaseServerLogin = _HcxDatabaseServerLogin_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 9),
    _HcxDatabaseServerLogin_Type()
)
hcxDatabaseServerLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDatabaseServerLogin.setStatus("current")


class _HcxDatabaseServerPassword_Type(DisplayString):
    """Custom type hcxDatabaseServerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxDatabaseServerPassword_Type.__name__ = "DisplayString"
_HcxDatabaseServerPassword_Object = MibScalar
hcxDatabaseServerPassword = _HcxDatabaseServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 18, 10),
    _HcxDatabaseServerPassword_Type()
)
hcxDatabaseServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDatabaseServerPassword.setStatus("current")
_Com21HcxPhase30_ObjectIdentity = ObjectIdentity
com21HcxPhase30 = _Com21HcxPhase30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 6, 1)
)
_Com21HcxCompact_ObjectIdentity = ObjectIdentity
com21HcxCompact = _Com21HcxCompact_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 6, 2)
)

# Managed Objects groups


# Notification objects

hcxDbActionComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 19)
)
hcxDbActionComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxDbActionResult"))
)
if mibBuilder.loadTexts:
    hcxDbActionComplete.setStatus(
        "current"
    )

hcxMajorStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 40)
)
hcxMajorStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxMajorAlarmStatusLed"))
)
if mibBuilder.loadTexts:
    hcxMajorStatusLedChange.setStatus(
        "current"
    )

hcxMinorStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 41)
)
hcxMinorStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxMinorAlarmStatusLed"))
)
if mibBuilder.loadTexts:
    hcxMinorStatusLedChange.setStatus(
        "current"
    )

hcxHcxSwDnldComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 42)
)
hcxHcxSwDnldComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxHcxSwDnldResult"))
)
if mibBuilder.loadTexts:
    hcxHcxSwDnldComplete.setStatus(
        "current"
    )

hcxCnfgBackupComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 44)
)
hcxCnfgBackupComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxCnfgBackupResult"))
)
if mibBuilder.loadTexts:
    hcxCnfgBackupComplete.setStatus(
        "current"
    )

hcxBootpFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 45)
)
hcxBootpFailed.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxBootpResult"))
)
if mibBuilder.loadTexts:
    hcxBootpFailed.setStatus(
        "current"
    )

hcxPowerFailDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 46)
)
hcxPowerFailDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxShelfId"))
)
if mibBuilder.loadTexts:
    hcxPowerFailDetected.setStatus(
        "current"
    )

hcxPowerFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 47)
)
hcxPowerFailClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxShelfId"))
)
if mibBuilder.loadTexts:
    hcxPowerFailClear.setStatus(
        "current"
    )

hcxFanFailDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 48)
)
hcxFanFailDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxShelfId"))
)
if mibBuilder.loadTexts:
    hcxFanFailDetected.setStatus(
        "current"
    )

hcxFanFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 49)
)
hcxFanFailClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxShelfId"))
)
if mibBuilder.loadTexts:
    hcxFanFailClear.setStatus(
        "current"
    )

stuTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 50)
)
stuTopologyChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxNumAcquiredStus"))
)
if mibBuilder.loadTexts:
    stuTopologyChange.setStatus(
        "current"
    )

hcxStuResourceExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 51)
)
hcxStuResourceExhausted.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"))
)
if mibBuilder.loadTexts:
    hcxStuResourceExhausted.setStatus(
        "current"
    )

hcxInsertChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 52)
)
hcxInsertChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxInsertChange.setStatus(
        "current"
    )

hcxMismatchDetect = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 53)
)
hcxMismatchDetect.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxMismatchDetect.setStatus(
        "current"
    )

hcxMismatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 54)
)
hcxMismatchClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxMismatchClear.setStatus(
        "current"
    )

hcxCardNoRespond = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 55)
)
hcxCardNoRespond.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxCardNoRespond.setStatus(
        "current"
    )

hcxCardPollFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 56)
)
hcxCardPollFail.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxCardPollFail.setStatus(
        "current"
    )

hcxCardPollFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 57)
)
hcxCardPollFailClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxCardPollFailClear.setStatus(
        "current"
    )

hcxCardDnldFailNoImage = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 58)
)
hcxCardDnldFailNoImage.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSlotInsertCardType"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxCardDnldFailNoImage.setStatus(
        "current"
    )

hcxRestartNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 59)
)
hcxRestartNotify.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"))
)
if mibBuilder.loadTexts:
    hcxRestartNotify.setStatus(
        "current"
    )

hcxCardRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 120)
)
hcxCardRemoved.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxCardRemoved.setStatus(
        "current"
    )

hcxCardRemClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 121)
)
hcxCardRemClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxShelfNo"),
        ("COM21-HCXTOP-MIB", "hcxSlotId"))
)
if mibBuilder.loadTexts:
    hcxCardRemClear.setStatus(
        "current"
    )

hcxSyncClkChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 181)
)
hcxSyncClkChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTOP-MIB", "hcxSyncClkSelect"))
)
if mibBuilder.loadTexts:
    hcxSyncClkChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXTOP-MIB",
    **{"UpstrmFreqKhz": UpstrmFreqKhz,
       "StuGain": StuGain,
       "EpochTime": EpochTime,
       "PrimServiceState": PrimServiceState,
       "Com21RowStatus": Com21RowStatus,
       "HcxCardType": HcxCardType,
       "com21HcxCtrl": com21HcxCtrl,
       "com21HcxControlGroup": com21HcxControlGroup,
       "hcxMacAddress": hcxMacAddress,
       "hcxEncryptionEnable": hcxEncryptionEnable,
       "hcxPartNumber": hcxPartNumber,
       "hcxEpochTime": hcxEpochTime,
       "hcxUserText": hcxUserText,
       "hcxSerialNumber": hcxSerialNumber,
       "hcxIpAddress": hcxIpAddress,
       "hcxGatewayAddress": hcxGatewayAddress,
       "hcxRestartAction": hcxRestartAction,
       "hcxMajorAlarmStatusLed": hcxMajorAlarmStatusLed,
       "hcxMinorAlarmStatusLed": hcxMinorAlarmStatusLed,
       "hcxAutoLoadBalancing": hcxAutoLoadBalancing,
       "hcxAutoFreqHopping": hcxAutoFreqHopping,
       "hcxKeyRenewalPeriod": hcxKeyRenewalPeriod,
       "hcxHcxSwRelease": hcxHcxSwRelease,
       "hcxHcxSwDnldResult": hcxHcxSwDnldResult,
       "hcxCnfgBackupAction": hcxCnfgBackupAction,
       "hcxCnfgBackupResult": hcxCnfgBackupResult,
       "hcxPhyConfigType": hcxPhyConfigType,
       "hcxNumOfShelves": hcxNumOfShelves,
       "hcxBootpServer": hcxBootpServer,
       "hcxBootpResult": hcxBootpResult,
       "hcxIpMask": hcxIpMask,
       "hcxFreqHopPause": hcxFreqHopPause,
       "hcxMaxDnstrmCBRAlloc": hcxMaxDnstrmCBRAlloc,
       "hcxMaxUpstrmCBRAlloc": hcxMaxUpstrmCBRAlloc,
       "hcxHcxAlternateSwRel": hcxHcxAlternateSwRel,
       "hcxHcxImageControl": hcxHcxImageControl,
       "hcxStatsControl": hcxStatsControl,
       "hcxImageTransfer": hcxImageTransfer,
       "hcxTrapFormat": hcxTrapFormat,
       "hcxSyncClkConfigure": hcxSyncClkConfigure,
       "hcxSyncClkSelect": hcxSyncClkSelect,
       "com21HcxAcqCnfgGroup": com21HcxAcqCnfgGroup,
       "hcxAcquisitionFreq": hcxAcquisitionFreq,
       "hcxAcqMinPower": hcxAcqMinPower,
       "hcxAcqMaxPower": hcxAcqMaxPower,
       "hcxAcqPowerStepSize": hcxAcqPowerStepSize,
       "hcxAltAcqFreq": hcxAltAcqFreq,
       "hcxActiveAcqFreq": hcxActiveAcqFreq,
       "com21HcxAlmOverGroup": com21HcxAlmOverGroup,
       "hcxNoCurrAlarms": hcxNoCurrAlarms,
       "hcxEventLogSize": hcxEventLogSize,
       "com21HcxStuOverGroup": com21HcxStuOverGroup,
       "hcxNumConfiguredStus": hcxNumConfiguredStus,
       "hcxNumAcquiredStus": hcxNumAcquiredStus,
       "hcxLastStuTopolgyChng": hcxLastStuTopolgyChng,
       "hcxNumEnabledStus": hcxNumEnabledStus,
       "hcxStuAggrUpStrmCbrRate": hcxStuAggrUpStrmCbrRate,
       "hcxStuAggrUpStrmMinRate": hcxStuAggrUpStrmMinRate,
       "hcxStuAggrUpStrmMaxRate": hcxStuAggrUpStrmMaxRate,
       "hcxStuAltDownFreq": hcxStuAltDownFreq,
       "hcxStuAcqTrapEnable": hcxStuAcqTrapEnable,
       "hcxStuRpcEnable": hcxStuRpcEnable,
       "hcxStuAutoDiscEnable": hcxStuAutoDiscEnable,
       "hcxStuAutoDiscIpAddr": hcxStuAutoDiscIpAddr,
       "hcxStuAutoGainAdjust": hcxStuAutoGainAdjust,
       "hcxStuAltDownFreqEnable": hcxStuAltDownFreqEnable,
       "hcxStuPcMacAddress": hcxStuPcMacAddress,
       "hcxStuPcToStuMacAddressResult": hcxStuPcToStuMacAddressResult,
       "hcxStuOverMacAddress": hcxStuOverMacAddress,
       "hcxStuGlobalSwImage": hcxStuGlobalSwImage,
       "com21HcxTrapRcvrGroup": com21HcxTrapRcvrGroup,
       "hcxTrapReceiverTable": hcxTrapReceiverTable,
       "hcxTrapReceiverEntry": hcxTrapReceiverEntry,
       "hcxTrapRcvrStatus": hcxTrapRcvrStatus,
       "hcxTrapRcvrNetAddress": hcxTrapRcvrNetAddress,
       "hcxTrapRcvrComm": hcxTrapRcvrComm,
       "hcxTrapRcvrAgeTime": hcxTrapRcvrAgeTime,
       "com21HcxShelfGroup": com21HcxShelfGroup,
       "com21HcxShelfTable": com21HcxShelfTable,
       "com21HcxShelfEntry": com21HcxShelfEntry,
       "hcxShelfId": hcxShelfId,
       "hcxShelfNoSlots": hcxShelfNoSlots,
       "com21HcxSlotGroup": com21HcxSlotGroup,
       "com21HcxSlotTable": com21HcxSlotTable,
       "com21HcxSlotEntry": com21HcxSlotEntry,
       "hcxShelfNo": hcxShelfNo,
       "hcxSlotId": hcxSlotId,
       "hcxSlotSupportedTypes": hcxSlotSupportedTypes,
       "hcxSlotConfigCardType": hcxSlotConfigCardType,
       "hcxSlotInsertCardType": hcxSlotInsertCardType,
       "com21HcxImageListGroup": com21HcxImageListGroup,
       "com21HcxImageListTable": com21HcxImageListTable,
       "com21HcxImageListEntry": com21HcxImageListEntry,
       "hcxImageId": hcxImageId,
       "hcxImageType": hcxImageType,
       "hcxImageFilename": hcxImageFilename,
       "hcxSwRevision": hcxSwRevision,
       "hcxHwRevision": hcxHwRevision,
       "hcxFwRevision": hcxFwRevision,
       "hcxImageState": hcxImageState,
       "com21HcxServTypeGroup": com21HcxServTypeGroup,
       "com21HcxServTypeTable": com21HcxServTypeTable,
       "com21HcxServTypeEntry": com21HcxServTypeEntry,
       "hcxServiceTypeId": hcxServiceTypeId,
       "hcxServTypeDesc": hcxServTypeDesc,
       "hcxDnStrmType": hcxDnStrmType,
       "hcxDnStrmRate": hcxDnStrmRate,
       "hcxUpStrmType": hcxUpStrmType,
       "hcxUpStrmMinRate": hcxUpStrmMinRate,
       "hcxUpStrmMaxRate": hcxUpStrmMaxRate,
       "hcxServTypeDelete": hcxServTypeDelete,
       "com21HcxArpFiltTrapGroup": com21HcxArpFiltTrapGroup,
       "hcxArpServerTrapEnable": hcxArpServerTrapEnable,
       "hcxArpUserTrapEnable": hcxArpUserTrapEnable,
       "com21HcxStuDefaultGroup": com21HcxStuDefaultGroup,
       "hcxStuDefaultAuth": hcxStuDefaultAuth,
       "hcxStuDefaultServType": hcxStuDefaultServType,
       "hcxStuDefaultVlan": hcxStuDefaultVlan,
       "hcxStuDefCom21SwImage": hcxStuDefCom21SwImage,
       "hcxStuDef3ComSwImage": hcxStuDef3ComSwImage,
       "com21HcxDbControlGroup": com21HcxDbControlGroup,
       "hcxDbAction": hcxDbAction,
       "hcxDbActionResult": hcxDbActionResult,
       "hcxDbBackupPeriod": hcxDbBackupPeriod,
       "com21HcxBootControlGroup": com21HcxBootControlGroup,
       "hcxFileTransProt": hcxFileTransProt,
       "hcxFileServerCntrl": hcxFileServerCntrl,
       "hcxImageServerIpAddr": hcxImageServerIpAddr,
       "hcxImageServerPath": hcxImageServerPath,
       "hcxImageServerLogin": hcxImageServerLogin,
       "hcxImageServerPassword": hcxImageServerPassword,
       "hcxDatabaseServerIpAddr": hcxDatabaseServerIpAddr,
       "hcxDatabaseServerPath": hcxDatabaseServerPath,
       "hcxDatabaseServerLogin": hcxDatabaseServerLogin,
       "hcxDatabaseServerPassword": hcxDatabaseServerPassword,
       "hcxDbActionComplete": hcxDbActionComplete,
       "hcxMajorStatusLedChange": hcxMajorStatusLedChange,
       "hcxMinorStatusLedChange": hcxMinorStatusLedChange,
       "hcxHcxSwDnldComplete": hcxHcxSwDnldComplete,
       "hcxCnfgBackupComplete": hcxCnfgBackupComplete,
       "hcxBootpFailed": hcxBootpFailed,
       "hcxPowerFailDetected": hcxPowerFailDetected,
       "hcxPowerFailClear": hcxPowerFailClear,
       "hcxFanFailDetected": hcxFanFailDetected,
       "hcxFanFailClear": hcxFanFailClear,
       "stuTopologyChange": stuTopologyChange,
       "hcxStuResourceExhausted": hcxStuResourceExhausted,
       "hcxInsertChange": hcxInsertChange,
       "hcxMismatchDetect": hcxMismatchDetect,
       "hcxMismatchClear": hcxMismatchClear,
       "hcxCardNoRespond": hcxCardNoRespond,
       "hcxCardPollFail": hcxCardPollFail,
       "hcxCardPollFailClear": hcxCardPollFailClear,
       "hcxCardDnldFailNoImage": hcxCardDnldFailNoImage,
       "hcxRestartNotify": hcxRestartNotify,
       "hcxCardRemoved": hcxCardRemoved,
       "hcxCardRemClear": hcxCardRemClear,
       "hcxSyncClkChange": hcxSyncClkChange,
       "com21HcxPhase30": com21HcxPhase30,
       "com21HcxCompact": com21HcxCompact}
)
