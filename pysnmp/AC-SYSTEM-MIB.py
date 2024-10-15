# SNMP MIB module (AC-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AC-SYSTEM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:39 2024
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

(acBoardMibs,
 acGeneric,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acSystem = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcSystemConfiguration_ObjectIdentity = ObjectIdentity
acSystemConfiguration = _AcSystemConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1)
)
_AcSysControl_ObjectIdentity = ObjectIdentity
acSysControl = _AcSysControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 1)
)


class _AcSysControlProtocolType_Type(Integer32):
    """Custom type acSysControlProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("controlProtocol-H323", 4),
          ("controlProtocol-MEGACO", 2),
          ("controlProtocol-MGCP", 1),
          ("controlProtocol-None", 0),
          ("controlProtocol-SIP", 8))
    )


_AcSysControlProtocolType_Type.__name__ = "Integer32"
_AcSysControlProtocolType_Object = MibScalar
acSysControlProtocolType = _AcSysControlProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 1, 1),
    _AcSysControlProtocolType_Type()
)
acSysControlProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysControlProtocolType.setStatus("current")


class _AcSysControlTrunkingToAnalogFunctionalityProfile_Type(Integer32):
    """Custom type acSysControlTrunkingToAnalogFunctionalityProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("cASAnalog", 1),
          ("disable", 0))
    )


_AcSysControlTrunkingToAnalogFunctionalityProfile_Type.__name__ = "Integer32"
_AcSysControlTrunkingToAnalogFunctionalityProfile_Object = MibScalar
acSysControlTrunkingToAnalogFunctionalityProfile = _AcSysControlTrunkingToAnalogFunctionalityProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 1, 2),
    _AcSysControlTrunkingToAnalogFunctionalityProfile_Type()
)
acSysControlTrunkingToAnalogFunctionalityProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysControlTrunkingToAnalogFunctionalityProfile.setStatus("current")
_AcSysTDM_ObjectIdentity = ObjectIdentity
acSysTDM = _AcSysTDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2)
)
_AcSysTDMClock_ObjectIdentity = ObjectIdentity
acSysTDMClock = _AcSysTDMClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1)
)


class _AcSysTDMClockSource_Type(Integer32):
    """Custom type acSysTDMClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("aTM-OC12", 19),
          ("aTM-OC3", 17),
          ("aTM-OC3-B", 18),
          ("bITS", 15),
          ("h110-A", 8),
          ("h110-B", 9),
          ("internal", 1),
          ("mVIP", 3),
          ("netReference1", 10),
          ("netReference2", 11),
          ("network", 4),
          ("network-DS3-1", 20),
          ("network-DS3-2", 21),
          ("network-DS3-3", 22),
          ("network-b", 16),
          ("sC-2M", 12),
          ("sC-4M", 13),
          ("sC-8M", 14))
    )


_AcSysTDMClockSource_Type.__name__ = "Integer32"
_AcSysTDMClockSource_Object = MibScalar
acSysTDMClockSource = _AcSysTDMClockSource_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 1),
    _AcSysTDMClockSource_Type()
)
acSysTDMClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockSource.setStatus("current")


class _AcSysTDMClockEnableFallBack_Type(Integer32):
    """Custom type acSysTDMClockEnableFallBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-Revertive", 2),
          ("autoNon-Revertive", 1),
          ("manual", 0))
    )


_AcSysTDMClockEnableFallBack_Type.__name__ = "Integer32"
_AcSysTDMClockEnableFallBack_Object = MibScalar
acSysTDMClockEnableFallBack = _AcSysTDMClockEnableFallBack_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 2),
    _AcSysTDMClockEnableFallBack_Type()
)
acSysTDMClockEnableFallBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockEnableFallBack.setStatus("current")


class _AcSysTDMClockLocalReference_Type(Unsigned32):
    """Custom type acSysTDMClockLocalReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AcSysTDMClockLocalReference_Type.__name__ = "Unsigned32"
_AcSysTDMClockLocalReference_Object = MibScalar
acSysTDMClockLocalReference = _AcSysTDMClockLocalReference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 3),
    _AcSysTDMClockLocalReference_Type()
)
acSysTDMClockLocalReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockLocalReference.setStatus("current")


class _AcSysTDMClockMasterSlaveSelection_Type(Integer32):
    """Custom type acSysTDMClockMasterSlaveSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acH110BusSecondaryMasterMode", 2),
          ("acTDMBusMasterMode", 1),
          ("acTDMBusSlaveMode", 0))
    )


_AcSysTDMClockMasterSlaveSelection_Type.__name__ = "Integer32"
_AcSysTDMClockMasterSlaveSelection_Object = MibScalar
acSysTDMClockMasterSlaveSelection = _AcSysTDMClockMasterSlaveSelection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 4),
    _AcSysTDMClockMasterSlaveSelection_Type()
)
acSysTDMClockMasterSlaveSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockMasterSlaveSelection.setStatus("current")


class _AcSysTDMClockNetRefSpeed_Type(Integer32):
    """Custom type acSysTDMClockNetRefSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acTH110BusNetRefSpeed-1544khz", 1),
          ("acTH110BusNetRefSpeed-20488khz", 2),
          ("acTH110BusNetRefSpeed-8khz", 0))
    )


_AcSysTDMClockNetRefSpeed_Type.__name__ = "Integer32"
_AcSysTDMClockNetRefSpeed_Object = MibScalar
acSysTDMClockNetRefSpeed = _AcSysTDMClockNetRefSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 5),
    _AcSysTDMClockNetRefSpeed_Type()
)
acSysTDMClockNetRefSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockNetRefSpeed.setStatus("current")


class _AcSysTDMClockAutoFallBackEnable_Type(Integer32):
    """Custom type acSysTDMClockAutoFallBackEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTDMClockAutoFallBackEnable_Type.__name__ = "Integer32"
_AcSysTDMClockAutoFallBackEnable_Object = MibScalar
acSysTDMClockAutoFallBackEnable = _AcSysTDMClockAutoFallBackEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 6),
    _AcSysTDMClockAutoFallBackEnable_Type()
)
acSysTDMClockAutoFallBackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockAutoFallBackEnable.setStatus("current")


class _AcSysTDMClockAutoFallBackRevertingEnable_Type(Integer32):
    """Custom type acSysTDMClockAutoFallBackRevertingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTDMClockAutoFallBackRevertingEnable_Type.__name__ = "Integer32"
_AcSysTDMClockAutoFallBackRevertingEnable_Object = MibScalar
acSysTDMClockAutoFallBackRevertingEnable = _AcSysTDMClockAutoFallBackRevertingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 7),
    _AcSysTDMClockAutoFallBackRevertingEnable_Type()
)
acSysTDMClockAutoFallBackRevertingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockAutoFallBackRevertingEnable.setStatus("current")


class _AcSysTDMClockBitsReference_Type(Unsigned32):
    """Custom type acSysTDMClockBitsReference based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysTDMClockBitsReference_Type.__name__ = "Unsigned32"
_AcSysTDMClockBitsReference_Object = MibScalar
acSysTDMClockBitsReference = _AcSysTDMClockBitsReference_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 8),
    _AcSysTDMClockBitsReference_Type()
)
acSysTDMClockBitsReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockBitsReference.setStatus("current")


class _AcSysTDMClockPLLOutOfRange_Type(Integer32):
    """Custom type acSysTDMClockPLLOutOfRange based on Integer32"""
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
        *(("oor-100to130ppm", 2),
          ("oor-13-8to18ppm", 4),
          ("oor-24-6to32ppm", 5),
          ("oor-36-6to47-5ppm", 6),
          ("oor-40to52ppm", 1),
          ("oor-52to67-5ppm", 7),
          ("oor-64to83ppm", 3),
          ("oor-9-2to12ppm", 0))
    )


_AcSysTDMClockPLLOutOfRange_Type.__name__ = "Integer32"
_AcSysTDMClockPLLOutOfRange_Object = MibScalar
acSysTDMClockPLLOutOfRange = _AcSysTDMClockPLLOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 9),
    _AcSysTDMClockPLLOutOfRange_Type()
)
acSysTDMClockPLLOutOfRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockPLLOutOfRange.setStatus("current")


class _AcSysTDMClockFallbackClock_Type(Integer32):
    """Custom type acSysTDMClockFallbackClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("h110-A", 8),
          ("h110-B", 9),
          ("netReference1", 10),
          ("netReference2", 11),
          ("network", 4))
    )


_AcSysTDMClockFallbackClock_Type.__name__ = "Integer32"
_AcSysTDMClockFallbackClock_Object = MibScalar
acSysTDMClockFallbackClock = _AcSysTDMClockFallbackClock_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 1, 10),
    _AcSysTDMClockFallbackClock_Type()
)
acSysTDMClockFallbackClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMClockFallbackClock.setStatus("current")
_AcSysTDMBus_ObjectIdentity = ObjectIdentity
acSysTDMBus = _AcSysTDMBus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2)
)


class _AcSysTDMBusType_Type(Integer32):
    """Custom type acSysTDMBusType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("aNALOG-BUS", 6),
          ("mVIP-BUS", 0),
          ("qSLAC-BUS", 3),
          ("sC-BUS", 1),
          ("uSE-EXT-BUS", 5),
          ("uSE-FRAMERS", 2),
          ("uSE-H110-BUS", 4),
          ("uSE-PSTN-SW-ONLY", 8))
    )


_AcSysTDMBusType_Type.__name__ = "Integer32"
_AcSysTDMBusType_Object = MibScalar
acSysTDMBusType = _AcSysTDMBusType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 1),
    _AcSysTDMBusType_Type()
)
acSysTDMBusType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusType.setStatus("current")


class _AcSysTDMBusSpeed_Type(Integer32):
    """Custom type acSysTDMBusSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("acTDMBusSpeed-16Mbps", 4),
          ("acTDMBusSpeed-2Mbps", 0),
          ("acTDMBusSpeed-4Mbps", 2),
          ("acTDMBusSpeed-8Mbps", 3))
    )


_AcSysTDMBusSpeed_Type.__name__ = "Integer32"
_AcSysTDMBusSpeed_Object = MibScalar
acSysTDMBusSpeed = _AcSysTDMBusSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 2),
    _AcSysTDMBusSpeed_Type()
)
acSysTDMBusSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusSpeed.setStatus("current")


class _AcSysTDMBusOutputPort_Type(Unsigned32):
    """Custom type acSysTDMBusOutputPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_AcSysTDMBusOutputPort_Type.__name__ = "Unsigned32"
_AcSysTDMBusOutputPort_Object = MibScalar
acSysTDMBusOutputPort = _AcSysTDMBusOutputPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 3),
    _AcSysTDMBusOutputPort_Type()
)
acSysTDMBusOutputPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusOutputPort.setStatus("current")


class _AcSysTDMBusOutputStartingChannel_Type(Unsigned32):
    """Custom type acSysTDMBusOutputStartingChannel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AcSysTDMBusOutputStartingChannel_Type.__name__ = "Unsigned32"
_AcSysTDMBusOutputStartingChannel_Object = MibScalar
acSysTDMBusOutputStartingChannel = _AcSysTDMBusOutputStartingChannel_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 2, 4),
    _AcSysTDMBusOutputStartingChannel_Type()
)
acSysTDMBusOutputStartingChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTDMBusOutputStartingChannel.setStatus("current")
_AcSysPCM_ObjectIdentity = ObjectIdentity
acSysPCM = _AcSysPCM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3)
)


class _AcSysPCMLawSelect_Type(Integer32):
    """Custom type acSysPCMLawSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aLaw", 1),
          ("automatic", 0),
          ("muLaw", 3))
    )


_AcSysPCMLawSelect_Type.__name__ = "Integer32"
_AcSysPCMLawSelect_Object = MibScalar
acSysPCMLawSelect = _AcSysPCMLawSelect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 1),
    _AcSysPCMLawSelect_Type()
)
acSysPCMLawSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMLawSelect.setStatus("current")


class _AcSysPCMIdlePattern_Type(Unsigned32):
    """Custom type acSysPCMIdlePattern based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysPCMIdlePattern_Type.__name__ = "Unsigned32"
_AcSysPCMIdlePattern_Object = MibScalar
acSysPCMIdlePattern = _AcSysPCMIdlePattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 2),
    _AcSysPCMIdlePattern_Type()
)
acSysPCMIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMIdlePattern.setStatus("current")


class _AcSysPCMIdleABCDPattern_Type(Unsigned32):
    """Custom type acSysPCMIdleABCDPattern based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysPCMIdleABCDPattern_Type.__name__ = "Unsigned32"
_AcSysPCMIdleABCDPattern_Object = MibScalar
acSysPCMIdleABCDPattern = _AcSysPCMIdleABCDPattern_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 3),
    _AcSysPCMIdleABCDPattern_Type()
)
acSysPCMIdleABCDPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMIdleABCDPattern.setStatus("current")


class _AcSysPCMSerialPortAuditIntervalMin_Type(Unsigned32):
    """Custom type acSysPCMSerialPortAuditIntervalMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AcSysPCMSerialPortAuditIntervalMin_Type.__name__ = "Unsigned32"
_AcSysPCMSerialPortAuditIntervalMin_Object = MibScalar
acSysPCMSerialPortAuditIntervalMin = _AcSysPCMSerialPortAuditIntervalMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 2, 3, 4),
    _AcSysPCMSerialPortAuditIntervalMin_Type()
)
acSysPCMSerialPortAuditIntervalMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysPCMSerialPortAuditIntervalMin.setStatus("current")
_AcSysNetworkConfig_ObjectIdentity = ObjectIdentity
acSysNetworkConfig = _AcSysNetworkConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3)
)
_AcSysIP_ObjectIdentity = ObjectIdentity
acSysIP = _AcSysIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1)
)
_AcSysIPAddress_Type = IpAddress
_AcSysIPAddress_Object = MibScalar
acSysIPAddress = _AcSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 1),
    _AcSysIPAddress_Type()
)
acSysIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPAddress.setStatus("current")
_AcSysIPSubNetAddress_Type = IpAddress
_AcSysIPSubNetAddress_Object = MibScalar
acSysIPSubNetAddress = _AcSysIPSubNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 2),
    _AcSysIPSubNetAddress_Type()
)
acSysIPSubNetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSubNetAddress.setStatus("current")
_AcSysIPDefaultGatewayAddress_Type = IpAddress
_AcSysIPDefaultGatewayAddress_Object = MibScalar
acSysIPDefaultGatewayAddress = _AcSysIPDefaultGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 3),
    _AcSysIPDefaultGatewayAddress_Type()
)
acSysIPDefaultGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDefaultGatewayAddress.setStatus("current")


class _AcSysIPDHCPEnable_Type(Integer32):
    """Custom type acSysIPDHCPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysIPDHCPEnable_Type.__name__ = "Integer32"
_AcSysIPDHCPEnable_Object = MibScalar
acSysIPDHCPEnable = _AcSysIPDHCPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 4),
    _AcSysIPDHCPEnable_Type()
)
acSysIPDHCPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDHCPEnable.setStatus("current")


class _AcSysIPDHCPSpeedFactor_Type(Unsigned32):
    """Custom type acSysIPDHCPSpeedFactor based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AcSysIPDHCPSpeedFactor_Type.__name__ = "Unsigned32"
_AcSysIPDHCPSpeedFactor_Object = MibScalar
acSysIPDHCPSpeedFactor = _AcSysIPDHCPSpeedFactor_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 5),
    _AcSysIPDHCPSpeedFactor_Type()
)
acSysIPDHCPSpeedFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDHCPSpeedFactor.setStatus("current")


class _AcSysIPDnsPrimaryServerType_Type(Integer32):
    """Custom type acSysIPDnsPrimaryServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AcSysIPDnsPrimaryServerType_Type.__name__ = "Integer32"
_AcSysIPDnsPrimaryServerType_Object = MibScalar
acSysIPDnsPrimaryServerType = _AcSysIPDnsPrimaryServerType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 6),
    _AcSysIPDnsPrimaryServerType_Type()
)
acSysIPDnsPrimaryServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsPrimaryServerType.setStatus("current")
_AcSysIPDnsPrimaryServer_Type = InetAddress
_AcSysIPDnsPrimaryServer_Object = MibScalar
acSysIPDnsPrimaryServer = _AcSysIPDnsPrimaryServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 7),
    _AcSysIPDnsPrimaryServer_Type()
)
acSysIPDnsPrimaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsPrimaryServer.setStatus("current")


class _AcSysIPDnsSecondaryServerType_Type(Integer32):
    """Custom type acSysIPDnsSecondaryServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ipv4", 1)
    )


_AcSysIPDnsSecondaryServerType_Type.__name__ = "Integer32"
_AcSysIPDnsSecondaryServerType_Object = MibScalar
acSysIPDnsSecondaryServerType = _AcSysIPDnsSecondaryServerType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 8),
    _AcSysIPDnsSecondaryServerType_Type()
)
acSysIPDnsSecondaryServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsSecondaryServerType.setStatus("current")
_AcSysIPDnsSecondaryServer_Type = InetAddress
_AcSysIPDnsSecondaryServer_Object = MibScalar
acSysIPDnsSecondaryServer = _AcSysIPDnsSecondaryServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 9),
    _AcSysIPDnsSecondaryServer_Type()
)
acSysIPDnsSecondaryServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDnsSecondaryServer.setStatus("current")


class _AcSysIPDHCPLeaseRenewalEnable_Type(Integer32):
    """Custom type acSysIPDHCPLeaseRenewalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysIPDHCPLeaseRenewalEnable_Type.__name__ = "Integer32"
_AcSysIPDHCPLeaseRenewalEnable_Object = MibScalar
acSysIPDHCPLeaseRenewalEnable = _AcSysIPDHCPLeaseRenewalEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 10),
    _AcSysIPDHCPLeaseRenewalEnable_Type()
)
acSysIPDHCPLeaseRenewalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPDHCPLeaseRenewalEnable.setStatus("current")
_AcMultipleIP_ObjectIdentity = ObjectIdentity
acMultipleIP = _AcMultipleIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30)
)


class _AcMultipleIPEnable_Type(Integer32):
    """Custom type acMultipleIPEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnable_Type.__name__ = "Integer32"
_AcMultipleIPEnable_Object = MibScalar
acMultipleIPEnable = _AcMultipleIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 1),
    _AcMultipleIPEnable_Type()
)
acMultipleIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnable.setStatus("obsolete")


class _AcMultipleIPEnableTPNCPasOAM_Type(Integer32):
    """Custom type acMultipleIPEnableTPNCPasOAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableTPNCPasOAM_Type.__name__ = "Integer32"
_AcMultipleIPEnableTPNCPasOAM_Object = MibScalar
acMultipleIPEnableTPNCPasOAM = _AcMultipleIPEnableTPNCPasOAM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 2),
    _AcMultipleIPEnableTPNCPasOAM_Type()
)
acMultipleIPEnableTPNCPasOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableTPNCPasOAM.setStatus("current")


class _AcMultipleIPEnableDNSasOAM_Type(Integer32):
    """Custom type acMultipleIPEnableDNSasOAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableDNSasOAM_Type.__name__ = "Integer32"
_AcMultipleIPEnableDNSasOAM_Object = MibScalar
acMultipleIPEnableDNSasOAM = _AcMultipleIPEnableDNSasOAM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 3),
    _AcMultipleIPEnableDNSasOAM_Type()
)
acMultipleIPEnableDNSasOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableDNSasOAM.setStatus("current")


class _AcMultipleIPEnableNTPasOAM_Type(Integer32):
    """Custom type acMultipleIPEnableNTPasOAM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableNTPasOAM_Type.__name__ = "Integer32"
_AcMultipleIPEnableNTPasOAM_Object = MibScalar
acMultipleIPEnableNTPasOAM = _AcMultipleIPEnableNTPasOAM_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 4),
    _AcMultipleIPEnableNTPasOAM_Type()
)
acMultipleIPEnableNTPasOAM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableNTPasOAM.setStatus("current")


class _AcMultipleIPEnableSCTPasControl_Type(Integer32):
    """Custom type acMultipleIPEnableSCTPasControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableSCTPasControl_Type.__name__ = "Integer32"
_AcMultipleIPEnableSCTPasControl_Object = MibScalar
acMultipleIPEnableSCTPasControl = _AcMultipleIPEnableSCTPasControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 5),
    _AcMultipleIPEnableSCTPasControl_Type()
)
acMultipleIPEnableSCTPasControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableSCTPasControl.setStatus("current")


class _AcMultipleIPEnableNetwotkSeparation_Type(Integer32):
    """Custom type acMultipleIPEnableNetwotkSeparation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcMultipleIPEnableNetwotkSeparation_Type.__name__ = "Integer32"
_AcMultipleIPEnableNetwotkSeparation_Object = MibScalar
acMultipleIPEnableNetwotkSeparation = _AcMultipleIPEnableNetwotkSeparation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 6),
    _AcMultipleIPEnableNetwotkSeparation_Type()
)
acMultipleIPEnableNetwotkSeparation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPEnableNetwotkSeparation.setStatus("current")


class _AcMultipleIPInterfaceTableAction_Type(Integer32):
    """Custom type acMultipleIPInterfaceTableAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("done", 1),
          ("validateConfiguration", 2))
    )


_AcMultipleIPInterfaceTableAction_Type.__name__ = "Integer32"
_AcMultipleIPInterfaceTableAction_Object = MibScalar
acMultipleIPInterfaceTableAction = _AcMultipleIPInterfaceTableAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 7),
    _AcMultipleIPInterfaceTableAction_Type()
)
acMultipleIPInterfaceTableAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acMultipleIPInterfaceTableAction.setStatus("current")
_AcNetworkIPTable_Object = MibTable
acNetworkIPTable = _AcNetworkIPTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21)
)
if mibBuilder.loadTexts:
    acNetworkIPTable.setStatus("obsolete")
_AcNetworkIPEntry_Object = MibTableRow
acNetworkIPEntry = _AcNetworkIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1)
)
acNetworkIPEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acNetworkIPIndex"),
)
if mibBuilder.loadTexts:
    acNetworkIPEntry.setStatus("obsolete")


class _AcNetworkIPIndex_Type(Integer32):
    """Custom type acNetworkIPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("control", 3),
          ("media", 2),
          ("oam", 1))
    )


_AcNetworkIPIndex_Type.__name__ = "Integer32"
_AcNetworkIPIndex_Object = MibTableColumn
acNetworkIPIndex = _AcNetworkIPIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 1),
    _AcNetworkIPIndex_Type()
)
acNetworkIPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acNetworkIPIndex.setStatus("obsolete")


class _AcNetworkIPIfIndex_Type(Unsigned32):
    """Custom type acNetworkIPIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcNetworkIPIfIndex_Type.__name__ = "Unsigned32"
_AcNetworkIPIfIndex_Object = MibTableColumn
acNetworkIPIfIndex = _AcNetworkIPIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 2),
    _AcNetworkIPIfIndex_Type()
)
acNetworkIPIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acNetworkIPIfIndex.setStatus("obsolete")
_AcNetworkIPLocalIPAddress_Type = IpAddress
_AcNetworkIPLocalIPAddress_Object = MibTableColumn
acNetworkIPLocalIPAddress = _AcNetworkIPLocalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 3),
    _AcNetworkIPLocalIPAddress_Type()
)
acNetworkIPLocalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPLocalIPAddress.setStatus("obsolete")
_AcNetworkIPLocalSubnetMask_Type = IpAddress
_AcNetworkIPLocalSubnetMask_Object = MibTableColumn
acNetworkIPLocalSubnetMask = _AcNetworkIPLocalSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 4),
    _AcNetworkIPLocalSubnetMask_Type()
)
acNetworkIPLocalSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPLocalSubnetMask.setStatus("obsolete")
_AcNetworkIPLocalDefGW_Type = IpAddress
_AcNetworkIPLocalDefGW_Object = MibTableColumn
acNetworkIPLocalDefGW = _AcNetworkIPLocalDefGW_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 5),
    _AcNetworkIPLocalDefGW_Type()
)
acNetworkIPLocalDefGW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPLocalDefGW.setStatus("obsolete")


class _AcNetworkIPAdminState_Type(Integer32):
    """Custom type acNetworkIPAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lock", 1),
          ("unLock", 2))
    )


_AcNetworkIPAdminState_Type.__name__ = "Integer32"
_AcNetworkIPAdminState_Object = MibTableColumn
acNetworkIPAdminState = _AcNetworkIPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 21, 1, 6),
    _AcNetworkIPAdminState_Type()
)
acNetworkIPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acNetworkIPAdminState.setStatus("obsolete")
_AcSysInterfaceTable_Object = MibTable
acSysInterfaceTable = _AcSysInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22)
)
if mibBuilder.loadTexts:
    acSysInterfaceTable.setStatus("current")
_AcSysInterfaceEntry_Object = MibTableRow
acSysInterfaceEntry = _AcSysInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1)
)
acSysInterfaceEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysInterfaceIndex"),
)
if mibBuilder.loadTexts:
    acSysInterfaceEntry.setStatus("current")


class _AcSysInterfaceIndex_Type(Unsigned32):
    """Custom type acSysInterfaceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcSysInterfaceIndex_Type.__name__ = "Unsigned32"
_AcSysInterfaceIndex_Object = MibTableColumn
acSysInterfaceIndex = _AcSysInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 1),
    _AcSysInterfaceIndex_Type()
)
acSysInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysInterfaceIndex.setStatus("current")
_AcSysInterfaceRowStatus_Type = RowStatus
_AcSysInterfaceRowStatus_Object = MibTableColumn
acSysInterfaceRowStatus = _AcSysInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 2),
    _AcSysInterfaceRowStatus_Type()
)
acSysInterfaceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceRowStatus.setStatus("current")


class _AcSysInterfaceAction_Type(Integer32):
    """Custom type acSysInterfaceAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysInterfaceAction_Type.__name__ = "Integer32"
_AcSysInterfaceAction_Object = MibTableColumn
acSysInterfaceAction = _AcSysInterfaceAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 3),
    _AcSysInterfaceAction_Type()
)
acSysInterfaceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceAction.setStatus("current")


class _AcSysInterfaceActionRes_Type(Integer32):
    """Custom type acSysInterfaceActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysInterfaceActionRes_Type.__name__ = "Integer32"
_AcSysInterfaceActionRes_Object = MibTableColumn
acSysInterfaceActionRes = _AcSysInterfaceActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 4),
    _AcSysInterfaceActionRes_Type()
)
acSysInterfaceActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceActionRes.setStatus("current")


class _AcSysInterfaceApplicationTypes_Type(Integer32):
    """Custom type acSysInterfaceApplicationTypes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("media", 1),
          ("mediaAndControl", 5),
          ("oam", 0),
          ("oamAndControl", 4),
          ("oamAndMedia", 3),
          ("oamAndMediaAndControl", 6))
    )


_AcSysInterfaceApplicationTypes_Type.__name__ = "Integer32"
_AcSysInterfaceApplicationTypes_Object = MibTableColumn
acSysInterfaceApplicationTypes = _AcSysInterfaceApplicationTypes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 5),
    _AcSysInterfaceApplicationTypes_Type()
)
acSysInterfaceApplicationTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceApplicationTypes.setStatus("current")


class _AcSysInterfaceMode_Type(Integer32):
    """Custom type acSysInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("iPv4Manual", 10),
          ("iPv6Manual", 4),
          ("iPv6PrefixManual", 3))
    )


_AcSysInterfaceMode_Type.__name__ = "Integer32"
_AcSysInterfaceMode_Object = MibTableColumn
acSysInterfaceMode = _AcSysInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 6),
    _AcSysInterfaceMode_Type()
)
acSysInterfaceMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceMode.setStatus("current")


class _AcSysInterfaceIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceIPAddress_Object = MibTableColumn
acSysInterfaceIPAddress = _AcSysInterfaceIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 7),
    _AcSysInterfaceIPAddress_Type()
)
acSysInterfaceIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceIPAddress.setStatus("current")


class _AcSysInterfacePrefixLength_Type(Unsigned32):
    """Custom type acSysInterfacePrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysInterfacePrefixLength_Type.__name__ = "Unsigned32"
_AcSysInterfacePrefixLength_Object = MibTableColumn
acSysInterfacePrefixLength = _AcSysInterfacePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 8),
    _AcSysInterfacePrefixLength_Type()
)
acSysInterfacePrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfacePrefixLength.setStatus("current")


class _AcSysInterfaceGateway_Type(SnmpAdminString):
    """Custom type acSysInterfaceGateway based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceGateway_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceGateway_Object = MibTableColumn
acSysInterfaceGateway = _AcSysInterfaceGateway_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 9),
    _AcSysInterfaceGateway_Type()
)
acSysInterfaceGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceGateway.setStatus("current")


class _AcSysInterfaceVlanID_Type(Unsigned32):
    """Custom type acSysInterfaceVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AcSysInterfaceVlanID_Type.__name__ = "Unsigned32"
_AcSysInterfaceVlanID_Object = MibTableColumn
acSysInterfaceVlanID = _AcSysInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 10),
    _AcSysInterfaceVlanID_Type()
)
acSysInterfaceVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceVlanID.setStatus("current")


class _AcSysInterfaceName_Type(SnmpAdminString):
    """Custom type acSysInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysInterfaceName_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceName_Object = MibTableColumn
acSysInterfaceName = _AcSysInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 1, 30, 22, 1, 11),
    _AcSysInterfaceName_Type()
)
acSysInterfaceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysInterfaceName.setStatus("current")
_AcSyslog_ObjectIdentity = ObjectIdentity
acSyslog = _AcSyslog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2)
)
_AcSyslogServerIPAddress_Type = IpAddress
_AcSyslogServerIPAddress_Object = MibScalar
acSyslogServerIPAddress = _AcSyslogServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 1),
    _AcSyslogServerIPAddress_Type()
)
acSyslogServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogServerIPAddress.setStatus("current")


class _AcSyslogEnable_Type(Integer32):
    """Custom type acSyslogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSyslogEnable_Type.__name__ = "Integer32"
_AcSyslogEnable_Object = MibScalar
acSyslogEnable = _AcSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 2),
    _AcSyslogEnable_Type()
)
acSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogEnable.setStatus("current")


class _AcSyslogAcSyslogServerPortNumber_Type(Unsigned32):
    """Custom type acSyslogAcSyslogServerPortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSyslogAcSyslogServerPortNumber_Type.__name__ = "Unsigned32"
_AcSyslogAcSyslogServerPortNumber_Object = MibScalar
acSyslogAcSyslogServerPortNumber = _AcSyslogAcSyslogServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 2, 3),
    _AcSyslogAcSyslogServerPortNumber_Type()
)
acSyslogAcSyslogServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSyslogAcSyslogServerPortNumber.setStatus("current")
_AcSysNTP_ObjectIdentity = ObjectIdentity
acSysNTP = _AcSysNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3)
)
_AcSysNTPServerIPAddress_Type = IpAddress
_AcSysNTPServerIPAddress_Object = MibScalar
acSysNTPServerIPAddress = _AcSysNTPServerIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 1),
    _AcSysNTPServerIPAddress_Type()
)
acSysNTPServerIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPServerIPAddress.setStatus("current")


class _AcSysNTPUtcOffset_Type(Integer32):
    """Custom type acSysNTPUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43200, 43200),
    )


_AcSysNTPUtcOffset_Type.__name__ = "Integer32"
_AcSysNTPUtcOffset_Object = MibScalar
acSysNTPUtcOffset = _AcSysNTPUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 2),
    _AcSysNTPUtcOffset_Type()
)
acSysNTPUtcOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPUtcOffset.setStatus("current")


class _AcSysNTPUpdateInterval_Type(Unsigned32):
    """Custom type acSysNTPUpdateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysNTPUpdateInterval_Type.__name__ = "Unsigned32"
_AcSysNTPUpdateInterval_Object = MibScalar
acSysNTPUpdateInterval = _AcSysNTPUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 3),
    _AcSysNTPUpdateInterval_Type()
)
acSysNTPUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysNTPUpdateInterval.setStatus("current")
_AcSysDayLightSavingTime_ObjectIdentity = ObjectIdentity
acSysDayLightSavingTime = _AcSysDayLightSavingTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21)
)


class _AcSysDayLightSavingTimeMode_Type(Integer32):
    """Custom type acSysDayLightSavingTimeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysDayLightSavingTimeMode_Type.__name__ = "Integer32"
_AcSysDayLightSavingTimeMode_Object = MibScalar
acSysDayLightSavingTimeMode = _AcSysDayLightSavingTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 1),
    _AcSysDayLightSavingTimeMode_Type()
)
acSysDayLightSavingTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeMode.setStatus("current")


class _AcSysDayLightSavingTimeOffset_Type(Unsigned32):
    """Custom type acSysDayLightSavingTimeOffset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_AcSysDayLightSavingTimeOffset_Type.__name__ = "Unsigned32"
_AcSysDayLightSavingTimeOffset_Object = MibScalar
acSysDayLightSavingTimeOffset = _AcSysDayLightSavingTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 2),
    _AcSysDayLightSavingTimeOffset_Type()
)
acSysDayLightSavingTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeOffset.setStatus("current")


class _AcSysDayLightSavingTimeStart_Type(SnmpAdminString):
    """Custom type acSysDayLightSavingTimeStart based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AcSysDayLightSavingTimeStart_Type.__name__ = "SnmpAdminString"
_AcSysDayLightSavingTimeStart_Object = MibScalar
acSysDayLightSavingTimeStart = _AcSysDayLightSavingTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 3),
    _AcSysDayLightSavingTimeStart_Type()
)
acSysDayLightSavingTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeStart.setStatus("current")


class _AcSysDayLightSavingTimeEnd_Type(SnmpAdminString):
    """Custom type acSysDayLightSavingTimeEnd based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AcSysDayLightSavingTimeEnd_Type.__name__ = "SnmpAdminString"
_AcSysDayLightSavingTimeEnd_Object = MibScalar
acSysDayLightSavingTimeEnd = _AcSysDayLightSavingTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 3, 21, 4),
    _AcSysDayLightSavingTimeEnd_Type()
)
acSysDayLightSavingTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDayLightSavingTimeEnd.setStatus("current")
_AcSysWEB_ObjectIdentity = ObjectIdentity
acSysWEB = _AcSysWEB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4)
)


class _AcSysWEBConfigDisable_Type(Integer32):
    """Custom type acSysWEBConfigDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 0))
    )


_AcSysWEBConfigDisable_Type.__name__ = "Integer32"
_AcSysWEBConfigDisable_Object = MibScalar
acSysWEBConfigDisable = _AcSysWEBConfigDisable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 1),
    _AcSysWEBConfigDisable_Type()
)
acSysWEBConfigDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBConfigDisable.setStatus("current")


class _AcSysWEBHTTPSOnly_Type(Integer32):
    """Custom type acSysWEBHTTPSOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBHTTPSOnly_Type.__name__ = "Integer32"
_AcSysWEBHTTPSOnly_Object = MibScalar
acSysWEBHTTPSOnly = _AcSysWEBHTTPSOnly_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 2),
    _AcSysWEBHTTPSOnly_Type()
)
acSysWEBHTTPSOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBHTTPSOnly.setStatus("current")


class _AcSysWEBHTTPSPort_Type(Unsigned32):
    """Custom type acSysWEBHTTPSPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysWEBHTTPSPort_Type.__name__ = "Unsigned32"
_AcSysWEBHTTPSPort_Object = MibScalar
acSysWEBHTTPSPort = _AcSysWEBHTTPSPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 3),
    _AcSysWEBHTTPSPort_Type()
)
acSysWEBHTTPSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBHTTPSPort.setStatus("current")


class _AcSysWEBWebUseRadiusLogin_Type(Integer32):
    """Custom type acSysWEBWebUseRadiusLogin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysWEBWebUseRadiusLogin_Type.__name__ = "Integer32"
_AcSysWEBWebUseRadiusLogin_Object = MibScalar
acSysWEBWebUseRadiusLogin = _AcSysWEBWebUseRadiusLogin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 4),
    _AcSysWEBWebUseRadiusLogin_Type()
)
acSysWEBWebUseRadiusLogin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBWebUseRadiusLogin.setStatus("current")


class _AcSysWEBHTTPSCipherString_Type(SnmpAdminString):
    """Custom type acSysWEBHTTPSCipherString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcSysWEBHTTPSCipherString_Type.__name__ = "SnmpAdminString"
_AcSysWEBHTTPSCipherString_Object = MibScalar
acSysWEBHTTPSCipherString = _AcSysWEBHTTPSCipherString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 5),
    _AcSysWEBHTTPSCipherString_Type()
)
acSysWEBHTTPSCipherString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBHTTPSCipherString.setStatus("current")


class _AcSysWEBDenyAuthenticationTimer_Type(Unsigned32):
    """Custom type acSysWEBDenyAuthenticationTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AcSysWEBDenyAuthenticationTimer_Type.__name__ = "Unsigned32"
_AcSysWEBDenyAuthenticationTimer_Object = MibScalar
acSysWEBDenyAuthenticationTimer = _AcSysWEBDenyAuthenticationTimer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 6),
    _AcSysWEBDenyAuthenticationTimer_Type()
)
acSysWEBDenyAuthenticationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBDenyAuthenticationTimer.setStatus("current")


class _AcSysWEBWanHttpPort_Type(Unsigned32):
    """Custom type acSysWEBWanHttpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysWEBWanHttpPort_Type.__name__ = "Unsigned32"
_AcSysWEBWanHttpPort_Object = MibScalar
acSysWEBWanHttpPort = _AcSysWEBWanHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 7),
    _AcSysWEBWanHttpPort_Type()
)
acSysWEBWanHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBWanHttpPort.setStatus("current")


class _AcSysWEBWanHttpsPort_Type(Unsigned32):
    """Custom type acSysWEBWanHttpsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysWEBWanHttpsPort_Type.__name__ = "Unsigned32"
_AcSysWEBWanHttpsPort_Object = MibScalar
acSysWEBWanHttpsPort = _AcSysWEBWanHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 8),
    _AcSysWEBWanHttpsPort_Type()
)
acSysWEBWanHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBWanHttpsPort.setStatus("current")
_AcSysWEBACLTable_Object = MibTable
acSysWEBACLTable = _AcSysWEBACLTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21)
)
if mibBuilder.loadTexts:
    acSysWEBACLTable.setStatus("current")
_AcSysWEBACLEntry_Object = MibTableRow
acSysWEBACLEntry = _AcSysWEBACLEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21, 1)
)
acSysWEBACLEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysWEBACLIndex"),
)
if mibBuilder.loadTexts:
    acSysWEBACLEntry.setStatus("current")


class _AcSysWEBACLIndex_Type(Unsigned32):
    """Custom type acSysWEBACLIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_AcSysWEBACLIndex_Type.__name__ = "Unsigned32"
_AcSysWEBACLIndex_Object = MibTableColumn
acSysWEBACLIndex = _AcSysWEBACLIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21, 1, 1),
    _AcSysWEBACLIndex_Type()
)
acSysWEBACLIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWEBACLIndex.setStatus("current")
_AcSysWEBACLIP_Type = IpAddress
_AcSysWEBACLIP_Object = MibTableColumn
acSysWEBACLIP = _AcSysWEBACLIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 4, 21, 1, 2),
    _AcSysWEBACLIP_Type()
)
acSysWEBACLIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBACLIP.setStatus("current")
_AcSysWEBAccess_ObjectIdentity = ObjectIdentity
acSysWEBAccess = _AcSysWEBAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5)
)
_AcSysWEBAccessTable_Object = MibTable
acSysWEBAccessTable = _AcSysWEBAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1)
)
if mibBuilder.loadTexts:
    acSysWEBAccessTable.setStatus("current")
_AcSysWEBAccessEntry_Object = MibTableRow
acSysWEBAccessEntry = _AcSysWEBAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1)
)
acSysWEBAccessEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysWEBAccessIndex"),
)
if mibBuilder.loadTexts:
    acSysWEBAccessEntry.setStatus("current")


class _AcSysWEBAccessRowStatus_Type(Unsigned32):
    """Custom type acSysWEBAccessRowStatus based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcSysWEBAccessRowStatus_Type.__name__ = "Unsigned32"
_AcSysWEBAccessRowStatus_Object = MibTableColumn
acSysWEBAccessRowStatus = _AcSysWEBAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 1),
    _AcSysWEBAccessRowStatus_Type()
)
acSysWEBAccessRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysWEBAccessRowStatus.setStatus("current")


class _AcSysWEBAccessAction_Type(Unsigned32):
    """Custom type acSysWEBAccessAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysWEBAccessAction_Type.__name__ = "Unsigned32"
_AcSysWEBAccessAction_Object = MibTableColumn
acSysWEBAccessAction = _AcSysWEBAccessAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 2),
    _AcSysWEBAccessAction_Type()
)
acSysWEBAccessAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessAction.setStatus("current")


class _AcSysWEBAccessActionResult_Type(Unsigned32):
    """Custom type acSysWEBAccessActionResult based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysWEBAccessActionResult_Type.__name__ = "Unsigned32"
_AcSysWEBAccessActionResult_Object = MibTableColumn
acSysWEBAccessActionResult = _AcSysWEBAccessActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 3),
    _AcSysWEBAccessActionResult_Type()
)
acSysWEBAccessActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWEBAccessActionResult.setStatus("current")


class _AcSysWEBAccessIndex_Type(Integer32):
    """Custom type acSysWEBAccessIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("administrator", 0),
          ("monitoringLevel", 1))
    )


_AcSysWEBAccessIndex_Type.__name__ = "Integer32"
_AcSysWEBAccessIndex_Object = MibTableColumn
acSysWEBAccessIndex = _AcSysWEBAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 4),
    _AcSysWEBAccessIndex_Type()
)
acSysWEBAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWEBAccessIndex.setStatus("current")


class _AcSysWEBAccessUserName_Type(SnmpAdminString):
    """Custom type acSysWEBAccessUserName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AcSysWEBAccessUserName_Type.__name__ = "SnmpAdminString"
_AcSysWEBAccessUserName_Object = MibTableColumn
acSysWEBAccessUserName = _AcSysWEBAccessUserName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 5),
    _AcSysWEBAccessUserName_Type()
)
acSysWEBAccessUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessUserName.setStatus("current")


class _AcSysWEBAccessUserCode_Type(SnmpAdminString):
    """Custom type acSysWEBAccessUserCode based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AcSysWEBAccessUserCode_Type.__name__ = "SnmpAdminString"
_AcSysWEBAccessUserCode_Object = MibTableColumn
acSysWEBAccessUserCode = _AcSysWEBAccessUserCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 6),
    _AcSysWEBAccessUserCode_Type()
)
acSysWEBAccessUserCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessUserCode.setStatus("current")


class _AcSysWEBAccessWebAuthMode_Type(Integer32):
    """Custom type acSysWEBAccessWebAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basicMode", 0),
          ("digestModeHTTPOnly", 2),
          ("digestModeWhenPossible", 1))
    )


_AcSysWEBAccessWebAuthMode_Type.__name__ = "Integer32"
_AcSysWEBAccessWebAuthMode_Object = MibTableColumn
acSysWEBAccessWebAuthMode = _AcSysWEBAccessWebAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 5, 1, 1, 7),
    _AcSysWEBAccessWebAuthMode_Type()
)
acSysWEBAccessWebAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysWEBAccessWebAuthMode.setStatus("current")
_AcSysNATTraversal_ObjectIdentity = ObjectIdentity
acSysNATTraversal = _AcSysNATTraversal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6)
)
_AcSysSTUN_ObjectIdentity = ObjectIdentity
acSysSTUN = _AcSysSTUN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21)
)


class _AcSysSTUNEnable_Type(Integer32):
    """Custom type acSysSTUNEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSTUNEnable_Type.__name__ = "Integer32"
_AcSysSTUNEnable_Object = MibScalar
acSysSTUNEnable = _AcSysSTUNEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 1),
    _AcSysSTUNEnable_Type()
)
acSysSTUNEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNEnable.setStatus("current")
_AcSysSTUNPrimaryServerIP_Type = IpAddress
_AcSysSTUNPrimaryServerIP_Object = MibScalar
acSysSTUNPrimaryServerIP = _AcSysSTUNPrimaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 2),
    _AcSysSTUNPrimaryServerIP_Type()
)
acSysSTUNPrimaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNPrimaryServerIP.setStatus("current")
_AcSysSTUNSecondaryServerIP_Type = IpAddress
_AcSysSTUNSecondaryServerIP_Object = MibScalar
acSysSTUNSecondaryServerIP = _AcSysSTUNSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 3),
    _AcSysSTUNSecondaryServerIP_Type()
)
acSysSTUNSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNSecondaryServerIP.setStatus("current")


class _AcSysSTUNBindingLifeTime_Type(Unsigned32):
    """Custom type acSysSTUNBindingLifeTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysSTUNBindingLifeTime_Type.__name__ = "Unsigned32"
_AcSysSTUNBindingLifeTime_Object = MibScalar
acSysSTUNBindingLifeTime = _AcSysSTUNBindingLifeTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 6, 21, 4),
    _AcSysSTUNBindingLifeTime_Type()
)
acSysSTUNBindingLifeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSTUNBindingLifeTime.setStatus("current")
_AcSysTelnet_ObjectIdentity = ObjectIdentity
acSysTelnet = _AcSysTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7)
)


class _AcSysTelnetServerEnable_Type(Integer32):
    """Custom type acSysTelnetServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("ssl", 2))
    )


_AcSysTelnetServerEnable_Type.__name__ = "Integer32"
_AcSysTelnetServerEnable_Object = MibScalar
acSysTelnetServerEnable = _AcSysTelnetServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 1),
    _AcSysTelnetServerEnable_Type()
)
acSysTelnetServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerEnable.setStatus("current")


class _AcSysTelnetServerPort_Type(Unsigned32):
    """Custom type acSysTelnetServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetServerPort_Type.__name__ = "Unsigned32"
_AcSysTelnetServerPort_Object = MibScalar
acSysTelnetServerPort = _AcSysTelnetServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 2),
    _AcSysTelnetServerPort_Type()
)
acSysTelnetServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerPort.setStatus("current")


class _AcSysTelnetServerIdleDisconnect_Type(Unsigned32):
    """Custom type acSysTelnetServerIdleDisconnect based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTelnetServerIdleDisconnect_Type.__name__ = "Unsigned32"
_AcSysTelnetServerIdleDisconnect_Object = MibScalar
acSysTelnetServerIdleDisconnect = _AcSysTelnetServerIdleDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 3),
    _AcSysTelnetServerIdleDisconnect_Type()
)
acSysTelnetServerIdleDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerIdleDisconnect.setStatus("current")


class _AcSysTelnetSSHServerPort_Type(Unsigned32):
    """Custom type acSysTelnetSSHServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetSSHServerPort_Type.__name__ = "Unsigned32"
_AcSysTelnetSSHServerPort_Object = MibScalar
acSysTelnetSSHServerPort = _AcSysTelnetSSHServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 4),
    _AcSysTelnetSSHServerPort_Type()
)
acSysTelnetSSHServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHServerPort.setStatus("current")


class _AcSysTelnetSSHServerEnable_Type(Integer32):
    """Custom type acSysTelnetSSHServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTelnetSSHServerEnable_Type.__name__ = "Integer32"
_AcSysTelnetSSHServerEnable_Object = MibScalar
acSysTelnetSSHServerEnable = _AcSysTelnetSSHServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 5),
    _AcSysTelnetSSHServerEnable_Type()
)
acSysTelnetSSHServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHServerEnable.setStatus("current")


class _AcSysTelnetSSHAdminKey_Type(SnmpAdminString):
    """Custom type acSysTelnetSSHAdminKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 510),
    )


_AcSysTelnetSSHAdminKey_Type.__name__ = "SnmpAdminString"
_AcSysTelnetSSHAdminKey_Object = MibScalar
acSysTelnetSSHAdminKey = _AcSysTelnetSSHAdminKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 6),
    _AcSysTelnetSSHAdminKey_Type()
)
acSysTelnetSSHAdminKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHAdminKey.setStatus("current")


class _AcSysTelnetSSHRequirePublicKey_Type(Integer32):
    """Custom type acSysTelnetSSHRequirePublicKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysTelnetSSHRequirePublicKey_Type.__name__ = "Integer32"
_AcSysTelnetSSHRequirePublicKey_Object = MibScalar
acSysTelnetSSHRequirePublicKey = _AcSysTelnetSSHRequirePublicKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 7),
    _AcSysTelnetSSHRequirePublicKey_Type()
)
acSysTelnetSSHRequirePublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetSSHRequirePublicKey.setStatus("current")


class _AcSysTelnetServerWanPort_Type(Unsigned32):
    """Custom type acSysTelnetServerWanPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetServerWanPort_Type.__name__ = "Unsigned32"
_AcSysTelnetServerWanPort_Object = MibScalar
acSysTelnetServerWanPort = _AcSysTelnetServerWanPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 8),
    _AcSysTelnetServerWanPort_Type()
)
acSysTelnetServerWanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetServerWanPort.setStatus("current")


class _AcSysTelnetWanSSHServerPort_Type(Unsigned32):
    """Custom type acSysTelnetWanSSHServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysTelnetWanSSHServerPort_Type.__name__ = "Unsigned32"
_AcSysTelnetWanSSHServerPort_Object = MibScalar
acSysTelnetWanSSHServerPort = _AcSysTelnetWanSSHServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 7, 9),
    _AcSysTelnetWanSSHServerPort_Type()
)
acSysTelnetWanSSHServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTelnetWanSSHServerPort.setStatus("current")
_AcSysHTTPClient_ObjectIdentity = ObjectIdentity
acSysHTTPClient = _AcSysHTTPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8)
)


class _AcSysHTTPClientAutoUpdatePredefinedTime_Type(SnmpAdminString):
    """Custom type acSysHTTPClientAutoUpdatePredefinedTime based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_AcSysHTTPClientAutoUpdatePredefinedTime_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientAutoUpdatePredefinedTime_Object = MibScalar
acSysHTTPClientAutoUpdatePredefinedTime = _AcSysHTTPClientAutoUpdatePredefinedTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 1),
    _AcSysHTTPClientAutoUpdatePredefinedTime_Type()
)
acSysHTTPClientAutoUpdatePredefinedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAutoUpdatePredefinedTime.setStatus("current")


class _AcSysHTTPClientAutoUpdateFrequency_Type(Unsigned32):
    """Custom type acSysHTTPClientAutoUpdateFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysHTTPClientAutoUpdateFrequency_Type.__name__ = "Unsigned32"
_AcSysHTTPClientAutoUpdateFrequency_Object = MibScalar
acSysHTTPClientAutoUpdateFrequency = _AcSysHTTPClientAutoUpdateFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 2),
    _AcSysHTTPClientAutoUpdateFrequency_Type()
)
acSysHTTPClientAutoUpdateFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAutoUpdateFrequency.setStatus("current")


class _AcSysHTTPClientAutoUpdateCmpFile_Type(Integer32):
    """Custom type acSysHTTPClientAutoUpdateCmpFile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysHTTPClientAutoUpdateCmpFile_Type.__name__ = "Integer32"
_AcSysHTTPClientAutoUpdateCmpFile_Object = MibScalar
acSysHTTPClientAutoUpdateCmpFile = _AcSysHTTPClientAutoUpdateCmpFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 3),
    _AcSysHTTPClientAutoUpdateCmpFile_Type()
)
acSysHTTPClientAutoUpdateCmpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientAutoUpdateCmpFile.setStatus("current")


class _AcSysHTTPClientCmpFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCmpFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCmpFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCmpFileURL_Object = MibScalar
acSysHTTPClientCmpFileURL = _AcSysHTTPClientCmpFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 4),
    _AcSysHTTPClientCmpFileURL_Type()
)
acSysHTTPClientCmpFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCmpFileURL.setStatus("current")


class _AcSysHTTPClientIniFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientIniFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientIniFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientIniFileURL_Object = MibScalar
acSysHTTPClientIniFileURL = _AcSysHTTPClientIniFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 5),
    _AcSysHTTPClientIniFileURL_Type()
)
acSysHTTPClientIniFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientIniFileURL.setStatus("current")


class _AcSysHTTPClientIniFileTemplateURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientIniFileTemplateURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientIniFileTemplateURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientIniFileTemplateURL_Object = MibScalar
acSysHTTPClientIniFileTemplateURL = _AcSysHTTPClientIniFileTemplateURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 6),
    _AcSysHTTPClientIniFileTemplateURL_Type()
)
acSysHTTPClientIniFileTemplateURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientIniFileTemplateURL.setStatus("current")


class _AcSysHTTPClientCPTFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCPTFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCPTFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCPTFileURL_Object = MibScalar
acSysHTTPClientCPTFileURL = _AcSysHTTPClientCPTFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 7),
    _AcSysHTTPClientCPTFileURL_Type()
)
acSysHTTPClientCPTFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCPTFileURL.setStatus("current")


class _AcSysHTTPClientVPFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientVPFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientVPFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientVPFileURL_Object = MibScalar
acSysHTTPClientVPFileURL = _AcSysHTTPClientVPFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 8),
    _AcSysHTTPClientVPFileURL_Type()
)
acSysHTTPClientVPFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientVPFileURL.setStatus("current")


class _AcSysHTTPClientPRTFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientPRTFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientPRTFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientPRTFileURL_Object = MibScalar
acSysHTTPClientPRTFileURL = _AcSysHTTPClientPRTFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 9),
    _AcSysHTTPClientPRTFileURL_Type()
)
acSysHTTPClientPRTFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientPRTFileURL.setStatus("current")


class _AcSysHTTPClientFXSCoeffFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientFXSCoeffFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientFXSCoeffFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientFXSCoeffFileURL_Object = MibScalar
acSysHTTPClientFXSCoeffFileURL = _AcSysHTTPClientFXSCoeffFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 10),
    _AcSysHTTPClientFXSCoeffFileURL_Type()
)
acSysHTTPClientFXSCoeffFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientFXSCoeffFileURL.setStatus("deprecated")


class _AcSysHTTPClientFXOCoeffFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientFXOCoeffFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientFXOCoeffFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientFXOCoeffFileURL_Object = MibScalar
acSysHTTPClientFXOCoeffFileURL = _AcSysHTTPClientFXOCoeffFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 11),
    _AcSysHTTPClientFXOCoeffFileURL_Type()
)
acSysHTTPClientFXOCoeffFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientFXOCoeffFileURL.setStatus("deprecated")


class _AcSysHTTPClientCASFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCASFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCASFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCASFileURL_Object = MibScalar
acSysHTTPClientCASFileURL = _AcSysHTTPClientCASFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 12),
    _AcSysHTTPClientCASFileURL_Type()
)
acSysHTTPClientCASFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCASFileURL.setStatus("current")


class _AcSysHTTPClientXMLFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientXMLFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientXMLFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientXMLFileUrl_Object = MibScalar
acSysHTTPClientXMLFileUrl = _AcSysHTTPClientXMLFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 13),
    _AcSysHTTPClientXMLFileUrl_Type()
)
acSysHTTPClientXMLFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientXMLFileUrl.setStatus("current")


class _AcSysHTTPClientCoderTableFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientCoderTableFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientCoderTableFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientCoderTableFileUrl_Object = MibScalar
acSysHTTPClientCoderTableFileUrl = _AcSysHTTPClientCoderTableFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 14),
    _AcSysHTTPClientCoderTableFileUrl_Type()
)
acSysHTTPClientCoderTableFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientCoderTableFileUrl.setStatus("current")


class _AcSysHTTPClientUserInfoFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientUserInfoFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientUserInfoFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientUserInfoFileURL_Object = MibScalar
acSysHTTPClientUserInfoFileURL = _AcSysHTTPClientUserInfoFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 15),
    _AcSysHTTPClientUserInfoFileURL_Type()
)
acSysHTTPClientUserInfoFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientUserInfoFileURL.setStatus("current")


class _AcSysHTTPClientDialPlanFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientDialPlanFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientDialPlanFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientDialPlanFileURL_Object = MibScalar
acSysHTTPClientDialPlanFileURL = _AcSysHTTPClientDialPlanFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 16),
    _AcSysHTTPClientDialPlanFileURL_Type()
)
acSysHTTPClientDialPlanFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientDialPlanFileURL.setStatus("current")


class _AcSysHTTPClientTLSPkeyFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSPkeyFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSPkeyFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSPkeyFileUrl_Object = MibScalar
acSysHTTPClientTLSPkeyFileUrl = _AcSysHTTPClientTLSPkeyFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 17),
    _AcSysHTTPClientTLSPkeyFileUrl_Type()
)
acSysHTTPClientTLSPkeyFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSPkeyFileUrl.setStatus("current")


class _AcSysHTTPClientTLSCertFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSCertFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSCertFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSCertFileUrl_Object = MibScalar
acSysHTTPClientTLSCertFileUrl = _AcSysHTTPClientTLSCertFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 18),
    _AcSysHTTPClientTLSCertFileUrl_Type()
)
acSysHTTPClientTLSCertFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSCertFileUrl.setStatus("current")


class _AcSysHTTPClientTLSRootFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientTLSRootFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientTLSRootFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientTLSRootFileUrl_Object = MibScalar
acSysHTTPClientTLSRootFileUrl = _AcSysHTTPClientTLSRootFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 19),
    _AcSysHTTPClientTLSRootFileUrl_Type()
)
acSysHTTPClientTLSRootFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientTLSRootFileUrl.setStatus("current")


class _AcSysHTTPClientWebLogoFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientWebLogoFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientWebLogoFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientWebLogoFileUrl_Object = MibScalar
acSysHTTPClientWebLogoFileUrl = _AcSysHTTPClientWebLogoFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 20),
    _AcSysHTTPClientWebLogoFileUrl_Type()
)
acSysHTTPClientWebLogoFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientWebLogoFileUrl.setStatus("current")


class _AcSysHTTPClientVideoFontFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientVideoFontFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientVideoFontFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientVideoFontFileURL_Object = MibScalar
acSysHTTPClientVideoFontFileURL = _AcSysHTTPClientVideoFontFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 21),
    _AcSysHTTPClientVideoFontFileURL_Type()
)
acSysHTTPClientVideoFontFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientVideoFontFileURL.setStatus("current")


class _AcSysHTTPClientV5PortConfFileURL_Type(SnmpAdminString):
    """Custom type acSysHTTPClientV5PortConfFileURL based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientV5PortConfFileURL_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientV5PortConfFileURL_Object = MibScalar
acSysHTTPClientV5PortConfFileURL = _AcSysHTTPClientV5PortConfFileURL_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 22),
    _AcSysHTTPClientV5PortConfFileURL_Type()
)
acSysHTTPClientV5PortConfFileURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientV5PortConfFileURL.setStatus("current")


class _AcSysHTTPClientDataConfigurationFileUrl_Type(SnmpAdminString):
    """Custom type acSysHTTPClientDataConfigurationFileUrl based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysHTTPClientDataConfigurationFileUrl_Type.__name__ = "SnmpAdminString"
_AcSysHTTPClientDataConfigurationFileUrl_Object = MibScalar
acSysHTTPClientDataConfigurationFileUrl = _AcSysHTTPClientDataConfigurationFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 8, 23),
    _AcSysHTTPClientDataConfigurationFileUrl_Type()
)
acSysHTTPClientDataConfigurationFileUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHTTPClientDataConfigurationFileUrl.setStatus("current")
_AcSysSNMP_ObjectIdentity = ObjectIdentity
acSysSNMP = _AcSysSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9)
)


class _AcSysSNMPKeepAliveTrapPort_Type(Unsigned32):
    """Custom type acSysSNMPKeepAliveTrapPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65334),
    )


_AcSysSNMPKeepAliveTrapPort_Type.__name__ = "Unsigned32"
_AcSysSNMPKeepAliveTrapPort_Object = MibScalar
acSysSNMPKeepAliveTrapPort = _AcSysSNMPKeepAliveTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 1),
    _AcSysSNMPKeepAliveTrapPort_Type()
)
acSysSNMPKeepAliveTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPKeepAliveTrapPort.setStatus("current")


class _AcSysSNMPEmsColdStrartIndication_Type(Unsigned32):
    """Custom type acSysSNMPEmsColdStrartIndication based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysSNMPEmsColdStrartIndication_Type.__name__ = "Unsigned32"
_AcSysSNMPEmsColdStrartIndication_Object = MibScalar
acSysSNMPEmsColdStrartIndication = _AcSysSNMPEmsColdStrartIndication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 2),
    _AcSysSNMPEmsColdStrartIndication_Type()
)
acSysSNMPEmsColdStrartIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPEmsColdStrartIndication.setStatus("current")


class _AcSysSNMPWanPort_Type(Unsigned32):
    """Custom type acSysSNMPWanPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65534),
    )


_AcSysSNMPWanPort_Type.__name__ = "Unsigned32"
_AcSysSNMPWanPort_Object = MibScalar
acSysSNMPWanPort = _AcSysSNMPWanPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 9, 3),
    _AcSysSNMPWanPort_Type()
)
acSysSNMPWanPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSNMPWanPort.setStatus("current")
_AcSysVLAN_ObjectIdentity = ObjectIdentity
acSysVLAN = _AcSysVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10)
)


class _AcSysVLANOamVlanId_Type(Unsigned32):
    """Custom type acSysVLANOamVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANOamVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANOamVlanId_Object = MibScalar
acSysVLANOamVlanId = _AcSysVLANOamVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 1),
    _AcSysVLANOamVlanId_Type()
)
acSysVLANOamVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANOamVlanId.setStatus("obsolete")


class _AcSysVLANControlVlanId_Type(Unsigned32):
    """Custom type acSysVLANControlVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANControlVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANControlVlanId_Object = MibScalar
acSysVLANControlVlanId = _AcSysVLANControlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 2),
    _AcSysVLANControlVlanId_Type()
)
acSysVLANControlVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANControlVlanId.setStatus("obsolete")


class _AcSysVLANMediaVlanId_Type(Unsigned32):
    """Custom type acSysVLANMediaVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANMediaVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANMediaVlanId_Object = MibScalar
acSysVLANMediaVlanId = _AcSysVLANMediaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 3),
    _AcSysVLANMediaVlanId_Type()
)
acSysVLANMediaVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANMediaVlanId.setStatus("obsolete")


class _AcSysVLANNetworkServiceClassPriority_Type(Unsigned32):
    """Custom type acSysVLANNetworkServiceClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANNetworkServiceClassPriority_Type.__name__ = "Unsigned32"
_AcSysVLANNetworkServiceClassPriority_Object = MibScalar
acSysVLANNetworkServiceClassPriority = _AcSysVLANNetworkServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 4),
    _AcSysVLANNetworkServiceClassPriority_Type()
)
acSysVLANNetworkServiceClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANNetworkServiceClassPriority.setStatus("deprecated")


class _AcSysVLANPremiumServiceClassMediaPriority_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassMediaPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANPremiumServiceClassMediaPriority_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassMediaPriority_Object = MibScalar
acSysVLANPremiumServiceClassMediaPriority = _AcSysVLANPremiumServiceClassMediaPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 5),
    _AcSysVLANPremiumServiceClassMediaPriority_Type()
)
acSysVLANPremiumServiceClassMediaPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassMediaPriority.setStatus("deprecated")


class _AcSysVLANGoldServiceClassPriority_Type(Unsigned32):
    """Custom type acSysVLANGoldServiceClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANGoldServiceClassPriority_Type.__name__ = "Unsigned32"
_AcSysVLANGoldServiceClassPriority_Object = MibScalar
acSysVLANGoldServiceClassPriority = _AcSysVLANGoldServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 6),
    _AcSysVLANGoldServiceClassPriority_Type()
)
acSysVLANGoldServiceClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANGoldServiceClassPriority.setStatus("deprecated")


class _AcSysVLANBronzeServiceClassPriority_Type(Unsigned32):
    """Custom type acSysVLANBronzeServiceClassPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANBronzeServiceClassPriority_Type.__name__ = "Unsigned32"
_AcSysVLANBronzeServiceClassPriority_Object = MibScalar
acSysVLANBronzeServiceClassPriority = _AcSysVLANBronzeServiceClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 7),
    _AcSysVLANBronzeServiceClassPriority_Type()
)
acSysVLANBronzeServiceClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANBronzeServiceClassPriority.setStatus("deprecated")


class _AcSysVLANPremiumServiceClassControlPriority_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassControlPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVLANPremiumServiceClassControlPriority_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassControlPriority_Object = MibScalar
acSysVLANPremiumServiceClassControlPriority = _AcSysVLANPremiumServiceClassControlPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 8),
    _AcSysVLANPremiumServiceClassControlPriority_Type()
)
acSysVLANPremiumServiceClassControlPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassControlPriority.setStatus("deprecated")


class _AcSysVLANNetworkServiceClassDiffServ_Type(Unsigned32):
    """Custom type acSysVLANNetworkServiceClassDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANNetworkServiceClassDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANNetworkServiceClassDiffServ_Object = MibScalar
acSysVLANNetworkServiceClassDiffServ = _AcSysVLANNetworkServiceClassDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 9),
    _AcSysVLANNetworkServiceClassDiffServ_Type()
)
acSysVLANNetworkServiceClassDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANNetworkServiceClassDiffServ.setStatus("current")


class _AcSysVLANPremiumServiceClassMediaDiffServ_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassMediaDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANPremiumServiceClassMediaDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassMediaDiffServ_Object = MibScalar
acSysVLANPremiumServiceClassMediaDiffServ = _AcSysVLANPremiumServiceClassMediaDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 10),
    _AcSysVLANPremiumServiceClassMediaDiffServ_Type()
)
acSysVLANPremiumServiceClassMediaDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassMediaDiffServ.setStatus("current")


class _AcSysVLANPremiumServiceClassControlDiffServ_Type(Unsigned32):
    """Custom type acSysVLANPremiumServiceClassControlDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANPremiumServiceClassControlDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANPremiumServiceClassControlDiffServ_Object = MibScalar
acSysVLANPremiumServiceClassControlDiffServ = _AcSysVLANPremiumServiceClassControlDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 11),
    _AcSysVLANPremiumServiceClassControlDiffServ_Type()
)
acSysVLANPremiumServiceClassControlDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANPremiumServiceClassControlDiffServ.setStatus("current")


class _AcSysVLANGoldServiceClassDiffServ_Type(Unsigned32):
    """Custom type acSysVLANGoldServiceClassDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANGoldServiceClassDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANGoldServiceClassDiffServ_Object = MibScalar
acSysVLANGoldServiceClassDiffServ = _AcSysVLANGoldServiceClassDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 12),
    _AcSysVLANGoldServiceClassDiffServ_Type()
)
acSysVLANGoldServiceClassDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANGoldServiceClassDiffServ.setStatus("current")


class _AcSysVLANBronzeServiceClassDiffServ_Type(Unsigned32):
    """Custom type acSysVLANBronzeServiceClassDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVLANBronzeServiceClassDiffServ_Type.__name__ = "Unsigned32"
_AcSysVLANBronzeServiceClassDiffServ_Object = MibScalar
acSysVLANBronzeServiceClassDiffServ = _AcSysVLANBronzeServiceClassDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 13),
    _AcSysVLANBronzeServiceClassDiffServ_Type()
)
acSysVLANBronzeServiceClassDiffServ.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANBronzeServiceClassDiffServ.setStatus("current")


class _AcSysVLANVlanNativeVlanId_Type(Unsigned32):
    """Custom type acSysVLANVlanNativeVlanId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AcSysVLANVlanNativeVlanId_Type.__name__ = "Unsigned32"
_AcSysVLANVlanNativeVlanId_Object = MibScalar
acSysVLANVlanNativeVlanId = _AcSysVLANVlanNativeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 14),
    _AcSysVLANVlanNativeVlanId_Type()
)
acSysVLANVlanNativeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANVlanNativeVlanId.setStatus("current")


class _AcSysVLANMode_Type(Unsigned32):
    """Custom type acSysVLANMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysVLANMode_Type.__name__ = "Unsigned32"
_AcSysVLANMode_Object = MibScalar
acSysVLANMode = _AcSysVLANMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 15),
    _AcSysVLANMode_Type()
)
acSysVLANMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysVLANMode.setStatus("current")
_AcSysVlanMapTable_Object = MibTable
acSysVlanMapTable = _AcSysVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21)
)
if mibBuilder.loadTexts:
    acSysVlanMapTable.setStatus("current")
_AcSysVlanMapEntry_Object = MibTableRow
acSysVlanMapEntry = _AcSysVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1)
)
acSysVlanMapEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysVlanMapIndex"),
)
if mibBuilder.loadTexts:
    acSysVlanMapEntry.setStatus("current")


class _AcSysVlanMapIndex_Type(Unsigned32):
    """Custom type acSysVlanMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVlanMapIndex_Type.__name__ = "Unsigned32"
_AcSysVlanMapIndex_Object = MibTableColumn
acSysVlanMapIndex = _AcSysVlanMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 1),
    _AcSysVlanMapIndex_Type()
)
acSysVlanMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysVlanMapIndex.setStatus("current")
_AcSysVlanMapRowStatus_Type = RowStatus
_AcSysVlanMapRowStatus_Object = MibTableColumn
acSysVlanMapRowStatus = _AcSysVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 2),
    _AcSysVlanMapRowStatus_Type()
)
acSysVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapRowStatus.setStatus("current")


class _AcSysVlanMapAction_Type(Integer32):
    """Custom type acSysVlanMapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysVlanMapAction_Type.__name__ = "Integer32"
_AcSysVlanMapAction_Object = MibTableColumn
acSysVlanMapAction = _AcSysVlanMapAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 3),
    _AcSysVlanMapAction_Type()
)
acSysVlanMapAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapAction.setStatus("current")


class _AcSysVlanMapActionRes_Type(Integer32):
    """Custom type acSysVlanMapActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysVlanMapActionRes_Type.__name__ = "Integer32"
_AcSysVlanMapActionRes_Object = MibTableColumn
acSysVlanMapActionRes = _AcSysVlanMapActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 4),
    _AcSysVlanMapActionRes_Type()
)
acSysVlanMapActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVlanMapActionRes.setStatus("current")


class _AcSysVlanMapDiffServ_Type(Unsigned32):
    """Custom type acSysVlanMapDiffServ based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcSysVlanMapDiffServ_Type.__name__ = "Unsigned32"
_AcSysVlanMapDiffServ_Object = MibTableColumn
acSysVlanMapDiffServ = _AcSysVlanMapDiffServ_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 5),
    _AcSysVlanMapDiffServ_Type()
)
acSysVlanMapDiffServ.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapDiffServ.setStatus("current")


class _AcSysVlanMapVlanPriority_Type(Unsigned32):
    """Custom type acSysVlanMapVlanPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysVlanMapVlanPriority_Type.__name__ = "Unsigned32"
_AcSysVlanMapVlanPriority_Object = MibTableColumn
acSysVlanMapVlanPriority = _AcSysVlanMapVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 10, 21, 1, 6),
    _AcSysVlanMapVlanPriority_Type()
)
acSysVlanMapVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysVlanMapVlanPriority.setStatus("current")
_AcSysSCTP_ObjectIdentity = ObjectIdentity
acSysSCTP = _AcSysSCTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11)
)


class _AcSysSCTPHeartBeatInterval_Type(Unsigned32):
    """Custom type acSysSCTPHeartBeatInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_AcSysSCTPHeartBeatInterval_Type.__name__ = "Unsigned32"
_AcSysSCTPHeartBeatInterval_Object = MibScalar
acSysSCTPHeartBeatInterval = _AcSysSCTPHeartBeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 1),
    _AcSysSCTPHeartBeatInterval_Type()
)
acSysSCTPHeartBeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPHeartBeatInterval.setStatus("current")


class _AcSysSCTPT4SACKTimer_Type(Unsigned32):
    """Custom type acSysSCTPT4SACKTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AcSysSCTPT4SACKTimer_Type.__name__ = "Unsigned32"
_AcSysSCTPT4SACKTimer_Object = MibScalar
acSysSCTPT4SACKTimer = _AcSysSCTPT4SACKTimer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 2),
    _AcSysSCTPT4SACKTimer_Type()
)
acSysSCTPT4SACKTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPT4SACKTimer.setStatus("current")


class _AcSysSCTPCheckSumMethod_Type(Integer32):
    """Custom type acSysSCTPCheckSumMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("adler", 0),
          ("crc", 1))
    )


_AcSysSCTPCheckSumMethod_Type.__name__ = "Integer32"
_AcSysSCTPCheckSumMethod_Object = MibScalar
acSysSCTPCheckSumMethod = _AcSysSCTPCheckSumMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 3),
    _AcSysSCTPCheckSumMethod_Type()
)
acSysSCTPCheckSumMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPCheckSumMethod.setStatus("current")


class _AcSysSCTPHostName_Type(SnmpAdminString):
    """Custom type acSysSCTPHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysSCTPHostName_Type.__name__ = "SnmpAdminString"
_AcSysSCTPHostName_Object = MibScalar
acSysSCTPHostName = _AcSysSCTPHostName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 4),
    _AcSysSCTPHostName_Type()
)
acSysSCTPHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPHostName.setStatus("current")


class _AcSysSCTPAssociationsNum_Type(Unsigned32):
    """Custom type acSysSCTPAssociationsNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_AcSysSCTPAssociationsNum_Type.__name__ = "Unsigned32"
_AcSysSCTPAssociationsNum_Object = MibScalar
acSysSCTPAssociationsNum = _AcSysSCTPAssociationsNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 11, 5),
    _AcSysSCTPAssociationsNum_Type()
)
acSysSCTPAssociationsNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSCTPAssociationsNum.setStatus("current")
_AcSysEthernetPort_ObjectIdentity = ObjectIdentity
acSysEthernetPort = _AcSysEthernetPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12)
)


class _AcSysEthernetPortPhyConfiguration_Type(Integer32):
    """Custom type acSysEthernetPortPhyConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 4),
          ("fullDuplex1000BaseT", 7),
          ("fullDuplex100BaseT", 3),
          ("fullDuplex10BaseT", 1),
          ("halfDuplex100BaseT", 2),
          ("halfDuplex10BaseT", 0))
    )


_AcSysEthernetPortPhyConfiguration_Type.__name__ = "Integer32"
_AcSysEthernetPortPhyConfiguration_Object = MibScalar
acSysEthernetPortPhyConfiguration = _AcSysEthernetPortPhyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 3, 12, 1),
    _AcSysEthernetPortPhyConfiguration_Type()
)
acSysEthernetPortPhyConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysEthernetPortPhyConfiguration.setStatus("current")
_AcSysMiscConfig_ObjectIdentity = ObjectIdentity
acSysMiscConfig = _AcSysMiscConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4)
)
_AcSysDiagnostics_ObjectIdentity = ObjectIdentity
acSysDiagnostics = _AcSysDiagnostics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1)
)


class _AcSysDiagnosticsEnable_Type(Integer32):
    """Custom type acSysDiagnosticsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              99)
        )
    )
    namedValues = NamedValues(
        *(("builtInTest", 1),
          ("builtInTestOnUtopiaVxb", 4),
          ("builtInTestWithSDRAM", 3),
          ("builtInTestwithPartialFlash", 2),
          ("disabled", 0),
          ("internalUse", 99))
    )


_AcSysDiagnosticsEnable_Type.__name__ = "Integer32"
_AcSysDiagnosticsEnable_Object = MibScalar
acSysDiagnosticsEnable = _AcSysDiagnosticsEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1, 1),
    _AcSysDiagnosticsEnable_Type()
)
acSysDiagnosticsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDiagnosticsEnable.setStatus("current")


class _AcSysDiagnosticsEnablePerformanceThresholdAlarms_Type(Integer32):
    """Custom type acSysDiagnosticsEnablePerformanceThresholdAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysDiagnosticsEnablePerformanceThresholdAlarms_Type.__name__ = "Integer32"
_AcSysDiagnosticsEnablePerformanceThresholdAlarms_Object = MibScalar
acSysDiagnosticsEnablePerformanceThresholdAlarms = _AcSysDiagnosticsEnablePerformanceThresholdAlarms_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1, 2),
    _AcSysDiagnosticsEnablePerformanceThresholdAlarms_Type()
)
acSysDiagnosticsEnablePerformanceThresholdAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDiagnosticsEnablePerformanceThresholdAlarms.setStatus("current")


class _AcSysDiagnosticsListOfActivitiesToLog_Type(SnmpAdminString):
    """Custom type acSysDiagnosticsListOfActivitiesToLog based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AcSysDiagnosticsListOfActivitiesToLog_Type.__name__ = "SnmpAdminString"
_AcSysDiagnosticsListOfActivitiesToLog_Object = MibScalar
acSysDiagnosticsListOfActivitiesToLog = _AcSysDiagnosticsListOfActivitiesToLog_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 1, 3),
    _AcSysDiagnosticsListOfActivitiesToLog_Type()
)
acSysDiagnosticsListOfActivitiesToLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysDiagnosticsListOfActivitiesToLog.setStatus("current")
_AcSysGenericINI_ObjectIdentity = ObjectIdentity
acSysGenericINI = _AcSysGenericINI_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 2)
)


class _AcSysGenericINILine_Type(SnmpAdminString):
    """Custom type acSysGenericINILine based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysGenericINILine_Type.__name__ = "SnmpAdminString"
_AcSysGenericINILine_Object = MibScalar
acSysGenericINILine = _AcSysGenericINILine_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 2, 1),
    _AcSysGenericINILine_Type()
)
acSysGenericINILine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysGenericINILine.setStatus("current")


class _AcSysGenericINISecureStartup_Type(Integer32):
    """Custom type acSysGenericINISecureStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysGenericINISecureStartup_Type.__name__ = "Integer32"
_AcSysGenericINISecureStartup_Object = MibScalar
acSysGenericINISecureStartup = _AcSysGenericINISecureStartup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 4, 2, 2),
    _AcSysGenericINISecureStartup_Type()
)
acSysGenericINISecureStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysGenericINISecureStartup.setStatus("current")
_AcSysLicenseKey_ObjectIdentity = ObjectIdentity
acSysLicenseKey = _AcSysLicenseKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5)
)


class _AcSysLicenseKeyString_Type(SnmpAdminString):
    """Custom type acSysLicenseKeyString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AcSysLicenseKeyString_Type.__name__ = "SnmpAdminString"
_AcSysLicenseKeyString_Object = MibScalar
acSysLicenseKeyString = _AcSysLicenseKeyString_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5, 1),
    _AcSysLicenseKeyString_Type()
)
acSysLicenseKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLicenseKeyString.setStatus("current")


class _AcSysLicenseKeyActiveList_Type(SnmpAdminString):
    """Custom type acSysLicenseKeyActiveList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 484),
    )


_AcSysLicenseKeyActiveList_Type.__name__ = "SnmpAdminString"
_AcSysLicenseKeyActiveList_Object = MibScalar
acSysLicenseKeyActiveList = _AcSysLicenseKeyActiveList_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 5, 2),
    _AcSysLicenseKeyActiveList_Type()
)
acSysLicenseKeyActiveList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLicenseKeyActiveList.setStatus("current")
_AcSysFile_ObjectIdentity = ObjectIdentity
acSysFile = _AcSysFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6)
)


class _AcSysFileCpt_Type(SnmpAdminString):
    """Custom type acSysFileCpt based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileCpt_Type.__name__ = "SnmpAdminString"
_AcSysFileCpt_Object = MibScalar
acSysFileCpt = _AcSysFileCpt_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 1),
    _AcSysFileCpt_Type()
)
acSysFileCpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileCpt.setStatus("current")


class _AcSysFileVp_Type(SnmpAdminString):
    """Custom type acSysFileVp based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileVp_Type.__name__ = "SnmpAdminString"
_AcSysFileVp_Object = MibScalar
acSysFileVp = _AcSysFileVp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 2),
    _AcSysFileVp_Type()
)
acSysFileVp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileVp.setStatus("current")


class _AcSysFilePrerecordedTones_Type(SnmpAdminString):
    """Custom type acSysFilePrerecordedTones based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFilePrerecordedTones_Type.__name__ = "SnmpAdminString"
_AcSysFilePrerecordedTones_Object = MibScalar
acSysFilePrerecordedTones = _AcSysFilePrerecordedTones_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 3),
    _AcSysFilePrerecordedTones_Type()
)
acSysFilePrerecordedTones.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFilePrerecordedTones.setStatus("current")


class _AcSysFileXml_Type(SnmpAdminString):
    """Custom type acSysFileXml based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileXml_Type.__name__ = "SnmpAdminString"
_AcSysFileXml_Object = MibScalar
acSysFileXml = _AcSysFileXml_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 4),
    _AcSysFileXml_Type()
)
acSysFileXml.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileXml.setStatus("current")


class _AcSysFileExternalCoder_Type(SnmpAdminString):
    """Custom type acSysFileExternalCoder based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileExternalCoder_Type.__name__ = "SnmpAdminString"
_AcSysFileExternalCoder_Object = MibScalar
acSysFileExternalCoder = _AcSysFileExternalCoder_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 5),
    _AcSysFileExternalCoder_Type()
)
acSysFileExternalCoder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileExternalCoder.setStatus("current")


class _AcSysFileUserInfo_Type(SnmpAdminString):
    """Custom type acSysFileUserInfo based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileUserInfo_Type.__name__ = "SnmpAdminString"
_AcSysFileUserInfo_Object = MibScalar
acSysFileUserInfo = _AcSysFileUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 6),
    _AcSysFileUserInfo_Type()
)
acSysFileUserInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileUserInfo.setStatus("current")


class _AcSysFileDialPlanFileName_Type(SnmpAdminString):
    """Custom type acSysFileDialPlanFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileDialPlanFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileDialPlanFileName_Object = MibScalar
acSysFileDialPlanFileName = _AcSysFileDialPlanFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 7),
    _AcSysFileDialPlanFileName_Type()
)
acSysFileDialPlanFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileDialPlanFileName.setStatus("current")


class _AcSysFileTLSPkeyFileName_Type(SnmpAdminString):
    """Custom type acSysFileTLSPkeyFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileTLSPkeyFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileTLSPkeyFileName_Object = MibScalar
acSysFileTLSPkeyFileName = _AcSysFileTLSPkeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 8),
    _AcSysFileTLSPkeyFileName_Type()
)
acSysFileTLSPkeyFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileTLSPkeyFileName.setStatus("current")


class _AcSysFileTLSCertFileName_Type(SnmpAdminString):
    """Custom type acSysFileTLSCertFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileTLSCertFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileTLSCertFileName_Object = MibScalar
acSysFileTLSCertFileName = _AcSysFileTLSCertFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 9),
    _AcSysFileTLSCertFileName_Type()
)
acSysFileTLSCertFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileTLSCertFileName.setStatus("current")


class _AcSysFileTLSRootFileName_Type(SnmpAdminString):
    """Custom type acSysFileTLSRootFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileTLSRootFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileTLSRootFileName_Object = MibScalar
acSysFileTLSRootFileName = _AcSysFileTLSRootFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 10),
    _AcSysFileTLSRootFileName_Type()
)
acSysFileTLSRootFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileTLSRootFileName.setStatus("current")


class _AcSysFileFirstVideoFontFileName_Type(SnmpAdminString):
    """Custom type acSysFileFirstVideoFontFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileFirstVideoFontFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileFirstVideoFontFileName_Object = MibScalar
acSysFileFirstVideoFontFileName = _AcSysFileFirstVideoFontFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 11),
    _AcSysFileFirstVideoFontFileName_Type()
)
acSysFileFirstVideoFontFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileFirstVideoFontFileName.setStatus("current")


class _AcSysFileSecondVideoFontFileName_Type(SnmpAdminString):
    """Custom type acSysFileSecondVideoFontFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileSecondVideoFontFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileSecondVideoFontFileName_Object = MibScalar
acSysFileSecondVideoFontFileName = _AcSysFileSecondVideoFontFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 12),
    _AcSysFileSecondVideoFontFileName_Type()
)
acSysFileSecondVideoFontFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileSecondVideoFontFileName.setStatus("current")


class _AcSysFileThirdVideoFontFileName_Type(SnmpAdminString):
    """Custom type acSysFileThirdVideoFontFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileThirdVideoFontFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileThirdVideoFontFileName_Object = MibScalar
acSysFileThirdVideoFontFileName = _AcSysFileThirdVideoFontFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 13),
    _AcSysFileThirdVideoFontFileName_Type()
)
acSysFileThirdVideoFontFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileThirdVideoFontFileName.setStatus("current")


class _AcSysFileV5PortConfFileName_Type(SnmpAdminString):
    """Custom type acSysFileV5PortConfFileName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 47),
    )


_AcSysFileV5PortConfFileName_Type.__name__ = "SnmpAdminString"
_AcSysFileV5PortConfFileName_Object = MibScalar
acSysFileV5PortConfFileName = _AcSysFileV5PortConfFileName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 6, 14),
    _AcSysFileV5PortConfFileName_Type()
)
acSysFileV5PortConfFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFileV5PortConfFileName.setStatus("current")
_AcSysSecurity_ObjectIdentity = ObjectIdentity
acSysSecurity = _AcSysSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7)
)


class _AcSysSecurityTLSVersion_Type(Unsigned32):
    """Custom type acSysSecurityTLSVersion based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysSecurityTLSVersion_Type.__name__ = "Unsigned32"
_AcSysSecurityTLSVersion_Object = MibScalar
acSysSecurityTLSVersion = _AcSysSecurityTLSVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 1),
    _AcSysSecurityTLSVersion_Type()
)
acSysSecurityTLSVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityTLSVersion.setStatus("current")


class _AcSysSecurityOcspEnable_Type(Integer32):
    """Custom type acSysSecurityOcspEnable based on Integer32"""
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


_AcSysSecurityOcspEnable_Type.__name__ = "Integer32"
_AcSysSecurityOcspEnable_Object = MibScalar
acSysSecurityOcspEnable = _AcSysSecurityOcspEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 2),
    _AcSysSecurityOcspEnable_Type()
)
acSysSecurityOcspEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspEnable.setStatus("current")
_AcSysSecurityOcspServerIPType_Type = InetAddressType
_AcSysSecurityOcspServerIPType_Object = MibScalar
acSysSecurityOcspServerIPType = _AcSysSecurityOcspServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 3),
    _AcSysSecurityOcspServerIPType_Type()
)
acSysSecurityOcspServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspServerIPType.setStatus("current")
_AcSysSecurityOcspServerIP_Type = InetAddress
_AcSysSecurityOcspServerIP_Object = MibScalar
acSysSecurityOcspServerIP = _AcSysSecurityOcspServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 4),
    _AcSysSecurityOcspServerIP_Type()
)
acSysSecurityOcspServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspServerIP.setStatus("current")


class _AcSysSecurityOcspServerPort_Type(Unsigned32):
    """Custom type acSysSecurityOcspServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_AcSysSecurityOcspServerPort_Type.__name__ = "Unsigned32"
_AcSysSecurityOcspServerPort_Object = MibScalar
acSysSecurityOcspServerPort = _AcSysSecurityOcspServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 5),
    _AcSysSecurityOcspServerPort_Type()
)
acSysSecurityOcspServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspServerPort.setStatus("current")


class _AcSysSecurityOcspDefaultResponse_Type(Integer32):
    """Custom type acSysSecurityOcspDefaultResponse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("allowPeerCertificate", 1),
          ("rejectPeerCertificate", 0))
    )


_AcSysSecurityOcspDefaultResponse_Type.__name__ = "Integer32"
_AcSysSecurityOcspDefaultResponse_Object = MibScalar
acSysSecurityOcspDefaultResponse = _AcSysSecurityOcspDefaultResponse_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 6),
    _AcSysSecurityOcspDefaultResponse_Type()
)
acSysSecurityOcspDefaultResponse.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspDefaultResponse.setStatus("current")


class _AcSysSecurityTLSFIPS140Mode_Type(Integer32):
    """Custom type acSysSecurityTLSFIPS140Mode based on Integer32"""
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


_AcSysSecurityTLSFIPS140Mode_Type.__name__ = "Integer32"
_AcSysSecurityTLSFIPS140Mode_Object = MibScalar
acSysSecurityTLSFIPS140Mode = _AcSysSecurityTLSFIPS140Mode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 7),
    _AcSysSecurityTLSFIPS140Mode_Type()
)
acSysSecurityTLSFIPS140Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityTLSFIPS140Mode.setStatus("current")


class _AcSysSecurityGenCsrSubjectName_Type(SnmpAdminString):
    """Custom type acSysSecurityGenCsrSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 600),
    )


_AcSysSecurityGenCsrSubjectName_Type.__name__ = "SnmpAdminString"
_AcSysSecurityGenCsrSubjectName_Object = MibScalar
acSysSecurityGenCsrSubjectName = _AcSysSecurityGenCsrSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 8),
    _AcSysSecurityGenCsrSubjectName_Type()
)
acSysSecurityGenCsrSubjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityGenCsrSubjectName.setStatus("current")


class _AcSysSecuritySelfSignedCertificateSubjectName_Type(SnmpAdminString):
    """Custom type acSysSecuritySelfSignedCertificateSubjectName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AcSysSecuritySelfSignedCertificateSubjectName_Type.__name__ = "SnmpAdminString"
_AcSysSecuritySelfSignedCertificateSubjectName_Object = MibScalar
acSysSecuritySelfSignedCertificateSubjectName = _AcSysSecuritySelfSignedCertificateSubjectName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 9),
    _AcSysSecuritySelfSignedCertificateSubjectName_Type()
)
acSysSecuritySelfSignedCertificateSubjectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecuritySelfSignedCertificateSubjectName.setStatus("current")
_AcSysSecurityOcspSecondaryServerIPType_Type = InetAddressType
_AcSysSecurityOcspSecondaryServerIPType_Object = MibScalar
acSysSecurityOcspSecondaryServerIPType = _AcSysSecurityOcspSecondaryServerIPType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 10),
    _AcSysSecurityOcspSecondaryServerIPType_Type()
)
acSysSecurityOcspSecondaryServerIPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspSecondaryServerIPType.setStatus("current")
_AcSysSecurityOcspSecondaryServerIP_Type = InetAddress
_AcSysSecurityOcspSecondaryServerIP_Object = MibScalar
acSysSecurityOcspSecondaryServerIP = _AcSysSecurityOcspSecondaryServerIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 11),
    _AcSysSecurityOcspSecondaryServerIP_Type()
)
acSysSecurityOcspSecondaryServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityOcspSecondaryServerIP.setStatus("current")


class _AcSysSecurityHTTPSRequireClientCertificate_Type(Integer32):
    """Custom type acSysSecurityHTTPSRequireClientCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSecurityHTTPSRequireClientCertificate_Type.__name__ = "Integer32"
_AcSysSecurityHTTPSRequireClientCertificate_Object = MibScalar
acSysSecurityHTTPSRequireClientCertificate = _AcSysSecurityHTTPSRequireClientCertificate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 12),
    _AcSysSecurityHTTPSRequireClientCertificate_Type()
)
acSysSecurityHTTPSRequireClientCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityHTTPSRequireClientCertificate.setStatus("current")


class _AcSysSecurityAUPDVerifyCertificates_Type(Integer32):
    """Custom type acSysSecurityAUPDVerifyCertificates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysSecurityAUPDVerifyCertificates_Type.__name__ = "Integer32"
_AcSysSecurityAUPDVerifyCertificates_Object = MibScalar
acSysSecurityAUPDVerifyCertificates = _AcSysSecurityAUPDVerifyCertificates_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 13),
    _AcSysSecurityAUPDVerifyCertificates_Type()
)
acSysSecurityAUPDVerifyCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSecurityAUPDVerifyCertificates.setStatus("current")
_AcSysIKE_ObjectIdentity = ObjectIdentity
acSysIKE = _AcSysIKE_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21)
)
_AcSysIKEPolicyTable_Object = MibTable
acSysIKEPolicyTable = _AcSysIKEPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1)
)
if mibBuilder.loadTexts:
    acSysIKEPolicyTable.setStatus("deprecated")
_AcSysIKEPolicyEntry_Object = MibTableRow
acSysIKEPolicyEntry = _AcSysIKEPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1)
)
acSysIKEPolicyEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIKEPolicyIndex"),
)
if mibBuilder.loadTexts:
    acSysIKEPolicyEntry.setStatus("deprecated")


class _AcSysIKEPolicyIndex_Type(Unsigned32):
    """Custom type acSysIKEPolicyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysIKEPolicyIndex_Type.__name__ = "Unsigned32"
_AcSysIKEPolicyIndex_Object = MibTableColumn
acSysIKEPolicyIndex = _AcSysIKEPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 1),
    _AcSysIKEPolicyIndex_Type()
)
acSysIKEPolicyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIKEPolicyIndex.setStatus("deprecated")
_AcSysIKEPolicyRowStatus_Type = RowStatus
_AcSysIKEPolicyRowStatus_Object = MibTableColumn
acSysIKEPolicyRowStatus = _AcSysIKEPolicyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 2),
    _AcSysIKEPolicyRowStatus_Type()
)
acSysIKEPolicyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyRowStatus.setStatus("deprecated")


class _AcSysIKEPolicyAction_Type(Integer32):
    """Custom type acSysIKEPolicyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysIKEPolicyAction_Type.__name__ = "Integer32"
_AcSysIKEPolicyAction_Object = MibTableColumn
acSysIKEPolicyAction = _AcSysIKEPolicyAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 3),
    _AcSysIKEPolicyAction_Type()
)
acSysIKEPolicyAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyAction.setStatus("deprecated")


class _AcSysIKEPolicyActionRes_Type(Integer32):
    """Custom type acSysIKEPolicyActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysIKEPolicyActionRes_Type.__name__ = "Integer32"
_AcSysIKEPolicyActionRes_Object = MibTableColumn
acSysIKEPolicyActionRes = _AcSysIKEPolicyActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 4),
    _AcSysIKEPolicyActionRes_Type()
)
acSysIKEPolicyActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIKEPolicyActionRes.setStatus("deprecated")


class _AcSysIKEPolicyShardKey_Type(SnmpAdminString):
    """Custom type acSysIKEPolicyShardKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AcSysIKEPolicyShardKey_Type.__name__ = "SnmpAdminString"
_AcSysIKEPolicyShardKey_Object = MibTableColumn
acSysIKEPolicyShardKey = _AcSysIKEPolicyShardKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 5),
    _AcSysIKEPolicyShardKey_Type()
)
acSysIKEPolicyShardKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyShardKey.setStatus("deprecated")


class _AcSysIKEPolicyLifeInSeconds_Type(Unsigned32):
    """Custom type acSysIKEPolicyLifeInSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIKEPolicyLifeInSeconds_Type.__name__ = "Unsigned32"
_AcSysIKEPolicyLifeInSeconds_Object = MibTableColumn
acSysIKEPolicyLifeInSeconds = _AcSysIKEPolicyLifeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 6),
    _AcSysIKEPolicyLifeInSeconds_Type()
)
acSysIKEPolicyLifeInSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyLifeInSeconds.setStatus("deprecated")


class _AcSysIKEPolicyLifeInKB_Type(Unsigned32):
    """Custom type acSysIKEPolicyLifeInKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIKEPolicyLifeInKB_Type.__name__ = "Unsigned32"
_AcSysIKEPolicyLifeInKB_Object = MibTableColumn
acSysIKEPolicyLifeInKB = _AcSysIKEPolicyLifeInKB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 7),
    _AcSysIKEPolicyLifeInKB_Type()
)
acSysIKEPolicyLifeInKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyLifeInKB.setStatus("deprecated")


class _AcSysIKEPolicyProposal0Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal0Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIKEPolicyProposal0Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal0Encryption_Object = MibTableColumn
acSysIKEPolicyProposal0Encryption = _AcSysIKEPolicyProposal0Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 8),
    _AcSysIKEPolicyProposal0Encryption_Type()
)
acSysIKEPolicyProposal0Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal0Encryption.setStatus("deprecated")


class _AcSysIKEPolicyProposal1Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal1Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIKEPolicyProposal1Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal1Encryption_Object = MibTableColumn
acSysIKEPolicyProposal1Encryption = _AcSysIKEPolicyProposal1Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 9),
    _AcSysIKEPolicyProposal1Encryption_Type()
)
acSysIKEPolicyProposal1Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal1Encryption.setStatus("deprecated")


class _AcSysIKEPolicyProposal2Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal2Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIKEPolicyProposal2Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal2Encryption_Object = MibTableColumn
acSysIKEPolicyProposal2Encryption = _AcSysIKEPolicyProposal2Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 10),
    _AcSysIKEPolicyProposal2Encryption_Type()
)
acSysIKEPolicyProposal2Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal2Encryption.setStatus("deprecated")


class _AcSysIKEPolicyProposal3Encryption_Type(Integer32):
    """Custom type acSysIKEPolicyProposal3Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIKEPolicyProposal3Encryption_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal3Encryption_Object = MibTableColumn
acSysIKEPolicyProposal3Encryption = _AcSysIKEPolicyProposal3Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 11),
    _AcSysIKEPolicyProposal3Encryption_Type()
)
acSysIKEPolicyProposal3Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal3Encryption.setStatus("deprecated")


class _AcSysIKEPolicyProposal0Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal0Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal0Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal0Authentication_Object = MibTableColumn
acSysIKEPolicyProposal0Authentication = _AcSysIKEPolicyProposal0Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 12),
    _AcSysIKEPolicyProposal0Authentication_Type()
)
acSysIKEPolicyProposal0Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal0Authentication.setStatus("deprecated")


class _AcSysIKEPolicyProposal1Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal1Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal1Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal1Authentication_Object = MibTableColumn
acSysIKEPolicyProposal1Authentication = _AcSysIKEPolicyProposal1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 13),
    _AcSysIKEPolicyProposal1Authentication_Type()
)
acSysIKEPolicyProposal1Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal1Authentication.setStatus("deprecated")


class _AcSysIKEPolicyProposal2Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal2Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal2Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal2Authentication_Object = MibTableColumn
acSysIKEPolicyProposal2Authentication = _AcSysIKEPolicyProposal2Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 14),
    _AcSysIKEPolicyProposal2Authentication_Type()
)
acSysIKEPolicyProposal2Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal2Authentication.setStatus("deprecated")


class _AcSysIKEPolicyProposal3Authentication_Type(Integer32):
    """Custom type acSysIKEPolicyProposal3Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal3Authentication_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal3Authentication_Object = MibTableColumn
acSysIKEPolicyProposal3Authentication = _AcSysIKEPolicyProposal3Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 15),
    _AcSysIKEPolicyProposal3Authentication_Type()
)
acSysIKEPolicyProposal3Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal3Authentication.setStatus("deprecated")


class _AcSysIKEPolicyProposal0DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal0DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-1024-BIT", 1),
          ("dH-786-BIT", 0),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal0DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal0DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal0DHGroup = _AcSysIKEPolicyProposal0DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 16),
    _AcSysIKEPolicyProposal0DHGroup_Type()
)
acSysIKEPolicyProposal0DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal0DHGroup.setStatus("deprecated")


class _AcSysIKEPolicyProposal1DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal1DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-1024-BIT", 1),
          ("dH-786-BIT", 0),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal1DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal1DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal1DHGroup = _AcSysIKEPolicyProposal1DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 17),
    _AcSysIKEPolicyProposal1DHGroup_Type()
)
acSysIKEPolicyProposal1DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal1DHGroup.setStatus("deprecated")


class _AcSysIKEPolicyProposal2DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal2DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-1024-BIT", 1),
          ("dH-786-BIT", 0),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal2DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal2DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal2DHGroup = _AcSysIKEPolicyProposal2DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 18),
    _AcSysIKEPolicyProposal2DHGroup_Type()
)
acSysIKEPolicyProposal2DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal2DHGroup.setStatus("deprecated")


class _AcSysIKEPolicyProposal3DHGroup_Type(Integer32):
    """Custom type acSysIKEPolicyProposal3DHGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dH-1024-BIT", 1),
          ("dH-786-BIT", 0),
          ("not-set", 10))
    )


_AcSysIKEPolicyProposal3DHGroup_Type.__name__ = "Integer32"
_AcSysIKEPolicyProposal3DHGroup_Object = MibTableColumn
acSysIKEPolicyProposal3DHGroup = _AcSysIKEPolicyProposal3DHGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 19),
    _AcSysIKEPolicyProposal3DHGroup_Type()
)
acSysIKEPolicyProposal3DHGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyProposal3DHGroup.setStatus("deprecated")


class _AcSysIKEPolicyAuthenticationMethod_Type(Integer32):
    """Custom type acSysIKEPolicyAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("presharedKey", 0),
          ("rsaSignature", 1))
    )


_AcSysIKEPolicyAuthenticationMethod_Type.__name__ = "Integer32"
_AcSysIKEPolicyAuthenticationMethod_Object = MibTableColumn
acSysIKEPolicyAuthenticationMethod = _AcSysIKEPolicyAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 21, 1, 1, 20),
    _AcSysIKEPolicyAuthenticationMethod_Type()
)
acSysIKEPolicyAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIKEPolicyAuthenticationMethod.setStatus("deprecated")
_AcSysIPSec_ObjectIdentity = ObjectIdentity
acSysIPSec = _AcSysIPSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22)
)


class _AcSysIPSecEnable_Type(Integer32):
    """Custom type acSysIPSecEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AcSysIPSecEnable_Type.__name__ = "Integer32"
_AcSysIPSecEnable_Object = MibScalar
acSysIPSecEnable = _AcSysIPSecEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 1),
    _AcSysIPSecEnable_Type()
)
acSysIPSecEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSecEnable.setStatus("current")


class _AcSysIPSecDpdMode_Type(Integer32):
    """Custom type acSysIPSecDpdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("ondemand", 2),
          ("periodic", 1))
    )


_AcSysIPSecDpdMode_Type.__name__ = "Integer32"
_AcSysIPSecDpdMode_Object = MibScalar
acSysIPSecDpdMode = _AcSysIPSecDpdMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 2),
    _AcSysIPSecDpdMode_Type()
)
acSysIPSecDpdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSecDpdMode.setStatus("current")


class _AcSysIPSecIKECertificateExtValidate_Type(Integer32):
    """Custom type acSysIPSecIKECertificateExtValidate based on Integer32"""
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


_AcSysIPSecIKECertificateExtValidate_Type.__name__ = "Integer32"
_AcSysIPSecIKECertificateExtValidate_Object = MibScalar
acSysIPSecIKECertificateExtValidate = _AcSysIPSecIKECertificateExtValidate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 3),
    _AcSysIPSecIKECertificateExtValidate_Type()
)
acSysIPSecIKECertificateExtValidate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysIPSecIKECertificateExtValidate.setStatus("current")
_AcSysIPSecSPDTable_Object = MibTable
acSysIPSecSPDTable = _AcSysIPSecSPDTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21)
)
if mibBuilder.loadTexts:
    acSysIPSecSPDTable.setStatus("deprecated")
_AcSysIPSecSPDEntry_Object = MibTableRow
acSysIPSecSPDEntry = _AcSysIPSecSPDEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1)
)
acSysIPSecSPDEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIPSecSPDIndex"),
)
if mibBuilder.loadTexts:
    acSysIPSecSPDEntry.setStatus("deprecated")


class _AcSysIPSecSPDIndex_Type(Unsigned32):
    """Custom type acSysIPSecSPDIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysIPSecSPDIndex_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDIndex_Object = MibTableColumn
acSysIPSecSPDIndex = _AcSysIPSecSPDIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 1),
    _AcSysIPSecSPDIndex_Type()
)
acSysIPSecSPDIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIPSecSPDIndex.setStatus("deprecated")
_AcSysIPSecSPDRowStatus_Type = RowStatus
_AcSysIPSecSPDRowStatus_Object = MibTableColumn
acSysIPSecSPDRowStatus = _AcSysIPSecSPDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 2),
    _AcSysIPSecSPDRowStatus_Type()
)
acSysIPSecSPDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDRowStatus.setStatus("deprecated")


class _AcSysIPSecSPDAction_Type(Integer32):
    """Custom type acSysIPSecSPDAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysIPSecSPDAction_Type.__name__ = "Integer32"
_AcSysIPSecSPDAction_Object = MibTableColumn
acSysIPSecSPDAction = _AcSysIPSecSPDAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 3),
    _AcSysIPSecSPDAction_Type()
)
acSysIPSecSPDAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDAction.setStatus("deprecated")


class _AcSysIPSecSPDActionRes_Type(Integer32):
    """Custom type acSysIPSecSPDActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysIPSecSPDActionRes_Type.__name__ = "Integer32"
_AcSysIPSecSPDActionRes_Object = MibTableColumn
acSysIPSecSPDActionRes = _AcSysIPSecSPDActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 4),
    _AcSysIPSecSPDActionRes_Type()
)
acSysIPSecSPDActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIPSecSPDActionRes.setStatus("deprecated")


class _AcSysIPSecSPDPolicyRemoteIPAddr_Type(SnmpAdminString):
    """Custom type acSysIPSecSPDPolicyRemoteIPAddr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_AcSysIPSecSPDPolicyRemoteIPAddr_Type.__name__ = "SnmpAdminString"
_AcSysIPSecSPDPolicyRemoteIPAddr_Object = MibTableColumn
acSysIPSecSPDPolicyRemoteIPAddr = _AcSysIPSecSPDPolicyRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 5),
    _AcSysIPSecSPDPolicyRemoteIPAddr_Type()
)
acSysIPSecSPDPolicyRemoteIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyRemoteIPAddr.setStatus("deprecated")


class _AcSysIPSecSPDPolicySrcPort_Type(Unsigned32):
    """Custom type acSysIPSecSPDPolicySrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysIPSecSPDPolicySrcPort_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDPolicySrcPort_Object = MibTableColumn
acSysIPSecSPDPolicySrcPort = _AcSysIPSecSPDPolicySrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 6),
    _AcSysIPSecSPDPolicySrcPort_Type()
)
acSysIPSecSPDPolicySrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicySrcPort.setStatus("deprecated")


class _AcSysIPSecSPDPolicyDestPort_Type(Unsigned32):
    """Custom type acSysIPSecSPDPolicyDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_AcSysIPSecSPDPolicyDestPort_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDPolicyDestPort_Object = MibTableColumn
acSysIPSecSPDPolicyDestPort = _AcSysIPSecSPDPolicyDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 7),
    _AcSysIPSecSPDPolicyDestPort_Type()
)
acSysIPSecSPDPolicyDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyDestPort.setStatus("deprecated")


class _AcSysIPSecSPDPolicyProtocol_Type(Unsigned32):
    """Custom type acSysIPSecSPDPolicyProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysIPSecSPDPolicyProtocol_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDPolicyProtocol_Object = MibTableColumn
acSysIPSecSPDPolicyProtocol = _AcSysIPSecSPDPolicyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 8),
    _AcSysIPSecSPDPolicyProtocol_Type()
)
acSysIPSecSPDPolicyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyProtocol.setStatus("deprecated")


class _AcSysIPSecSPDKeyExchangeMethodIndex_Type(Unsigned32):
    """Custom type acSysIPSecSPDKeyExchangeMethodIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPSecSPDKeyExchangeMethodIndex_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDKeyExchangeMethodIndex_Object = MibTableColumn
acSysIPSecSPDKeyExchangeMethodIndex = _AcSysIPSecSPDKeyExchangeMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 9),
    _AcSysIPSecSPDKeyExchangeMethodIndex_Type()
)
acSysIPSecSPDKeyExchangeMethodIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDKeyExchangeMethodIndex.setStatus("deprecated")


class _AcSysIPSecSPDLifeInSeconds_Type(Unsigned32):
    """Custom type acSysIPSecSPDLifeInSeconds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPSecSPDLifeInSeconds_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDLifeInSeconds_Object = MibTableColumn
acSysIPSecSPDLifeInSeconds = _AcSysIPSecSPDLifeInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 10),
    _AcSysIPSecSPDLifeInSeconds_Type()
)
acSysIPSecSPDLifeInSeconds.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDLifeInSeconds.setStatus("deprecated")


class _AcSysIPSecSPDLifeInKB_Type(Unsigned32):
    """Custom type acSysIPSecSPDLifeInKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPSecSPDLifeInKB_Type.__name__ = "Unsigned32"
_AcSysIPSecSPDLifeInKB_Object = MibTableColumn
acSysIPSecSPDLifeInKB = _AcSysIPSecSPDLifeInKB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 11),
    _AcSysIPSecSPDLifeInKB_Type()
)
acSysIPSecSPDLifeInKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDLifeInKB.setStatus("deprecated")


class _AcSysIPSecSPDProposal0Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal0Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("none", 0),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIPSecSPDProposal0Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal0Encryption_Object = MibTableColumn
acSysIPSecSPDProposal0Encryption = _AcSysIPSecSPDProposal0Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 12),
    _AcSysIPSecSPDProposal0Encryption_Type()
)
acSysIPSecSPDProposal0Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal0Encryption.setStatus("deprecated")


class _AcSysIPSecSPDProposal1Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal1Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("none", 0),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIPSecSPDProposal1Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal1Encryption_Object = MibTableColumn
acSysIPSecSPDProposal1Encryption = _AcSysIPSecSPDProposal1Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 13),
    _AcSysIPSecSPDProposal1Encryption_Type()
)
acSysIPSecSPDProposal1Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal1Encryption.setStatus("deprecated")


class _AcSysIPSecSPDProposal2Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal2Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("none", 0),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIPSecSPDProposal2Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal2Encryption_Object = MibTableColumn
acSysIPSecSPDProposal2Encryption = _AcSysIPSecSPDProposal2Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 14),
    _AcSysIPSecSPDProposal2Encryption_Type()
)
acSysIPSecSPDProposal2Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal2Encryption.setStatus("deprecated")


class _AcSysIPSecSPDProposal3Encryption_Type(Integer32):
    """Custom type acSysIPSecSPDProposal3Encryption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("aES", 3),
          ("dES-CBC", 1),
          ("none", 0),
          ("not-set", 10),
          ("triple-DES-CBC", 2))
    )


_AcSysIPSecSPDProposal3Encryption_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal3Encryption_Object = MibTableColumn
acSysIPSecSPDProposal3Encryption = _AcSysIPSecSPDProposal3Encryption_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 15),
    _AcSysIPSecSPDProposal3Encryption_Type()
)
acSysIPSecSPDProposal3Encryption.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal3Encryption.setStatus("deprecated")


class _AcSysIPSecSPDProposal0Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal0Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal0Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal0Authentication_Object = MibTableColumn
acSysIPSecSPDProposal0Authentication = _AcSysIPSecSPDProposal0Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 16),
    _AcSysIPSecSPDProposal0Authentication_Type()
)
acSysIPSecSPDProposal0Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal0Authentication.setStatus("deprecated")


class _AcSysIPSecSPDProposal1Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal1Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal1Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal1Authentication_Object = MibTableColumn
acSysIPSecSPDProposal1Authentication = _AcSysIPSecSPDProposal1Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 17),
    _AcSysIPSecSPDProposal1Authentication_Type()
)
acSysIPSecSPDProposal1Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal1Authentication.setStatus("deprecated")


class _AcSysIPSecSPDProposal2Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal2Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal2Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal2Authentication_Object = MibTableColumn
acSysIPSecSPDProposal2Authentication = _AcSysIPSecSPDProposal2Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 18),
    _AcSysIPSecSPDProposal2Authentication_Type()
)
acSysIPSecSPDProposal2Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal2Authentication.setStatus("deprecated")


class _AcSysIPSecSPDProposal3Authentication_Type(Integer32):
    """Custom type acSysIPSecSPDProposal3Authentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("hMAC-MD5-96", 4),
          ("hMAC-SHA-1-96", 2),
          ("not-set", 10))
    )


_AcSysIPSecSPDProposal3Authentication_Type.__name__ = "Integer32"
_AcSysIPSecSPDProposal3Authentication_Object = MibTableColumn
acSysIPSecSPDProposal3Authentication = _AcSysIPSecSPDProposal3Authentication_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 19),
    _AcSysIPSecSPDProposal3Authentication_Type()
)
acSysIPSecSPDProposal3Authentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDProposal3Authentication.setStatus("deprecated")


class _AcSysIPSecSPDPolicyLocalIPAddrType_Type(Integer32):
    """Custom type acSysIPSecSPDPolicyLocalIPAddrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("oam", 0))
    )


_AcSysIPSecSPDPolicyLocalIPAddrType_Type.__name__ = "Integer32"
_AcSysIPSecSPDPolicyLocalIPAddrType_Object = MibTableColumn
acSysIPSecSPDPolicyLocalIPAddrType = _AcSysIPSecSPDPolicyLocalIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 20),
    _AcSysIPSecSPDPolicyLocalIPAddrType_Type()
)
acSysIPSecSPDPolicyLocalIPAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyLocalIPAddrType.setStatus("deprecated")


class _AcSysIPSecSPDMode_Type(Integer32):
    """Custom type acSysIPSecSPDMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport", 0),
          ("tunneling", 1))
    )


_AcSysIPSecSPDMode_Type.__name__ = "Integer32"
_AcSysIPSecSPDMode_Object = MibTableColumn
acSysIPSecSPDMode = _AcSysIPSecSPDMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 21),
    _AcSysIPSecSPDMode_Type()
)
acSysIPSecSPDMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDMode.setStatus("deprecated")
_AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Type = IpAddress
_AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Object = MibTableColumn
acSysIPSecSPDPolicyRemoteTunnelIPAddress = _AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 22),
    _AcSysIPSecSPDPolicyRemoteTunnelIPAddress_Type()
)
acSysIPSecSPDPolicyRemoteTunnelIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyRemoteTunnelIPAddress.setStatus("deprecated")
_AcSysIPSecSPDPolicyLocalTunnelIPAddress_Type = IpAddress
_AcSysIPSecSPDPolicyLocalTunnelIPAddress_Object = MibTableColumn
acSysIPSecSPDPolicyLocalTunnelIPAddress = _AcSysIPSecSPDPolicyLocalTunnelIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 23),
    _AcSysIPSecSPDPolicyLocalTunnelIPAddress_Type()
)
acSysIPSecSPDPolicyLocalTunnelIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyLocalTunnelIPAddress.setStatus("deprecated")
_AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Type = IpAddress
_AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Object = MibTableColumn
acSysIPSecSPDPolicyRemoteTunnelSubnetMask = _AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 21, 1, 24),
    _AcSysIPSecSPDPolicyRemoteTunnelSubnetMask_Type()
)
acSysIPSecSPDPolicyRemoteTunnelSubnetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPSecSPDPolicyRemoteTunnelSubnetMask.setStatus("deprecated")
_AcSysIPsecProposalTable_Object = MibTable
acSysIPsecProposalTable = _AcSysIPsecProposalTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22)
)
if mibBuilder.loadTexts:
    acSysIPsecProposalTable.setStatus("current")
_AcSysIPsecProposalEntry_Object = MibTableRow
acSysIPsecProposalEntry = _AcSysIPsecProposalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1)
)
acSysIPsecProposalEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIPsecProposalIndex"),
)
if mibBuilder.loadTexts:
    acSysIPsecProposalEntry.setStatus("current")


class _AcSysIPsecProposalIndex_Type(Unsigned32):
    """Custom type acSysIPsecProposalIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcSysIPsecProposalIndex_Type.__name__ = "Unsigned32"
_AcSysIPsecProposalIndex_Object = MibTableColumn
acSysIPsecProposalIndex = _AcSysIPsecProposalIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 1),
    _AcSysIPsecProposalIndex_Type()
)
acSysIPsecProposalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIPsecProposalIndex.setStatus("current")
_AcSysIPsecProposalRowStatus_Type = RowStatus
_AcSysIPsecProposalRowStatus_Object = MibTableColumn
acSysIPsecProposalRowStatus = _AcSysIPsecProposalRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 2),
    _AcSysIPsecProposalRowStatus_Type()
)
acSysIPsecProposalRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalRowStatus.setStatus("current")


class _AcSysIPsecProposalAction_Type(Integer32):
    """Custom type acSysIPsecProposalAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysIPsecProposalAction_Type.__name__ = "Integer32"
_AcSysIPsecProposalAction_Object = MibTableColumn
acSysIPsecProposalAction = _AcSysIPsecProposalAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 3),
    _AcSysIPsecProposalAction_Type()
)
acSysIPsecProposalAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalAction.setStatus("current")


class _AcSysIPsecProposalActionRes_Type(Integer32):
    """Custom type acSysIPsecProposalActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysIPsecProposalActionRes_Type.__name__ = "Integer32"
_AcSysIPsecProposalActionRes_Object = MibTableColumn
acSysIPsecProposalActionRes = _AcSysIPsecProposalActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 4),
    _AcSysIPsecProposalActionRes_Type()
)
acSysIPsecProposalActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIPsecProposalActionRes.setStatus("current")


class _AcSysIPsecProposalEncryptionAlgorithm_Type(Integer32):
    """Custom type acSysIPsecProposalEncryptionAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("aes", 3),
          ("desCbc", 1),
          ("none", 0),
          ("tripleDesCbc", 2))
    )


_AcSysIPsecProposalEncryptionAlgorithm_Type.__name__ = "Integer32"
_AcSysIPsecProposalEncryptionAlgorithm_Object = MibTableColumn
acSysIPsecProposalEncryptionAlgorithm = _AcSysIPsecProposalEncryptionAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 5),
    _AcSysIPsecProposalEncryptionAlgorithm_Type()
)
acSysIPsecProposalEncryptionAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalEncryptionAlgorithm.setStatus("current")


class _AcSysIPsecProposalAuthenticationAlgorithm_Type(Integer32):
    """Custom type acSysIPsecProposalAuthenticationAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("hmacMd5-96", 4),
          ("hmacSha1-96", 2),
          ("none", 0))
    )


_AcSysIPsecProposalAuthenticationAlgorithm_Type.__name__ = "Integer32"
_AcSysIPsecProposalAuthenticationAlgorithm_Object = MibTableColumn
acSysIPsecProposalAuthenticationAlgorithm = _AcSysIPsecProposalAuthenticationAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 6),
    _AcSysIPsecProposalAuthenticationAlgorithm_Type()
)
acSysIPsecProposalAuthenticationAlgorithm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalAuthenticationAlgorithm.setStatus("current")


class _AcSysIPsecProposalDiffieHellmanGroup_Type(Integer32):
    """Custom type acSysIPsecProposalDiffieHellmanGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("group1-768Bits", 0),
          ("group2-1024Bits", 1))
    )


_AcSysIPsecProposalDiffieHellmanGroup_Type.__name__ = "Integer32"
_AcSysIPsecProposalDiffieHellmanGroup_Object = MibTableColumn
acSysIPsecProposalDiffieHellmanGroup = _AcSysIPsecProposalDiffieHellmanGroup_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 22, 1, 7),
    _AcSysIPsecProposalDiffieHellmanGroup_Type()
)
acSysIPsecProposalDiffieHellmanGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecProposalDiffieHellmanGroup.setStatus("current")
_AcSysIPsecSATable_Object = MibTable
acSysIPsecSATable = _AcSysIPsecSATable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23)
)
if mibBuilder.loadTexts:
    acSysIPsecSATable.setStatus("current")
_AcSysIPsecSAEntry_Object = MibTableRow
acSysIPsecSAEntry = _AcSysIPsecSAEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1)
)
acSysIPsecSAEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysIPsecSAIndex"),
)
if mibBuilder.loadTexts:
    acSysIPsecSAEntry.setStatus("current")


class _AcSysIPsecSAIndex_Type(Unsigned32):
    """Custom type acSysIPsecSAIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20),
    )


_AcSysIPsecSAIndex_Type.__name__ = "Unsigned32"
_AcSysIPsecSAIndex_Object = MibTableColumn
acSysIPsecSAIndex = _AcSysIPsecSAIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 1),
    _AcSysIPsecSAIndex_Type()
)
acSysIPsecSAIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysIPsecSAIndex.setStatus("current")
_AcSysIPsecSARowStatus_Type = RowStatus
_AcSysIPsecSARowStatus_Object = MibTableColumn
acSysIPsecSARowStatus = _AcSysIPsecSARowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 2),
    _AcSysIPsecSARowStatus_Type()
)
acSysIPsecSARowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARowStatus.setStatus("current")


class _AcSysIPsecSAAction_Type(Unsigned32):
    """Custom type acSysIPsecSAAction based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysIPsecSAAction_Type.__name__ = "Unsigned32"
_AcSysIPsecSAAction_Object = MibTableColumn
acSysIPsecSAAction = _AcSysIPsecSAAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 3),
    _AcSysIPsecSAAction_Type()
)
acSysIPsecSAAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAAction.setStatus("current")


class _AcSysIPsecSAActionRes_Type(Unsigned32):
    """Custom type acSysIPsecSAActionRes based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AcSysIPsecSAActionRes_Type.__name__ = "Unsigned32"
_AcSysIPsecSAActionRes_Object = MibTableColumn
acSysIPsecSAActionRes = _AcSysIPsecSAActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 4),
    _AcSysIPsecSAActionRes_Type()
)
acSysIPsecSAActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIPsecSAActionRes.setStatus("current")


class _AcSysIPsecSARemoteEndpointAddress_Type(SnmpAdminString):
    """Custom type acSysIPsecSARemoteEndpointAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 98),
    )


_AcSysIPsecSARemoteEndpointAddress_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSARemoteEndpointAddress_Object = MibTableColumn
acSysIPsecSARemoteEndpointAddress = _AcSysIPsecSARemoteEndpointAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 5),
    _AcSysIPsecSARemoteEndpointAddress_Type()
)
acSysIPsecSARemoteEndpointAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteEndpointAddress.setStatus("current")


class _AcSysIPsecSAAuthenticationMethod_Type(Integer32):
    """Custom type acSysIPsecSAAuthenticationMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("presharedKey", 0),
          ("rSASignature", 1))
    )


_AcSysIPsecSAAuthenticationMethod_Type.__name__ = "Integer32"
_AcSysIPsecSAAuthenticationMethod_Object = MibTableColumn
acSysIPsecSAAuthenticationMethod = _AcSysIPsecSAAuthenticationMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 6),
    _AcSysIPsecSAAuthenticationMethod_Type()
)
acSysIPsecSAAuthenticationMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAAuthenticationMethod.setStatus("current")


class _AcSysIPsecSASharedKey_Type(SnmpAdminString):
    """Custom type acSysIPsecSASharedKey based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_AcSysIPsecSASharedKey_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSASharedKey_Object = MibTableColumn
acSysIPsecSASharedKey = _AcSysIPsecSASharedKey_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 7),
    _AcSysIPsecSASharedKey_Type()
)
acSysIPsecSASharedKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSASharedKey.setStatus("current")


class _AcSysIPsecSASourcePort_Type(Unsigned32):
    """Custom type acSysIPsecSASourcePort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysIPsecSASourcePort_Type.__name__ = "Unsigned32"
_AcSysIPsecSASourcePort_Object = MibTableColumn
acSysIPsecSASourcePort = _AcSysIPsecSASourcePort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 8),
    _AcSysIPsecSASourcePort_Type()
)
acSysIPsecSASourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSASourcePort.setStatus("current")


class _AcSysIPsecSADestPort_Type(Unsigned32):
    """Custom type acSysIPsecSADestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysIPsecSADestPort_Type.__name__ = "Unsigned32"
_AcSysIPsecSADestPort_Object = MibTableColumn
acSysIPsecSADestPort = _AcSysIPsecSADestPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 9),
    _AcSysIPsecSADestPort_Type()
)
acSysIPsecSADestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSADestPort.setStatus("current")


class _AcSysIPsecSAProtocol_Type(Unsigned32):
    """Custom type acSysIPsecSAProtocol based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AcSysIPsecSAProtocol_Type.__name__ = "Unsigned32"
_AcSysIPsecSAProtocol_Object = MibTableColumn
acSysIPsecSAProtocol = _AcSysIPsecSAProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 10),
    _AcSysIPsecSAProtocol_Type()
)
acSysIPsecSAProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAProtocol.setStatus("current")


class _AcSysIPsecSAPhase1SaLifetimeInSec_Type(Unsigned32):
    """Custom type acSysIPsecSAPhase1SaLifetimeInSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPsecSAPhase1SaLifetimeInSec_Type.__name__ = "Unsigned32"
_AcSysIPsecSAPhase1SaLifetimeInSec_Object = MibTableColumn
acSysIPsecSAPhase1SaLifetimeInSec = _AcSysIPsecSAPhase1SaLifetimeInSec_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 11),
    _AcSysIPsecSAPhase1SaLifetimeInSec_Type()
)
acSysIPsecSAPhase1SaLifetimeInSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAPhase1SaLifetimeInSec.setStatus("current")


class _AcSysIPsecSAPhase2SaLifetimeInSec_Type(Unsigned32):
    """Custom type acSysIPsecSAPhase2SaLifetimeInSec based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPsecSAPhase2SaLifetimeInSec_Type.__name__ = "Unsigned32"
_AcSysIPsecSAPhase2SaLifetimeInSec_Object = MibTableColumn
acSysIPsecSAPhase2SaLifetimeInSec = _AcSysIPsecSAPhase2SaLifetimeInSec_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 12),
    _AcSysIPsecSAPhase2SaLifetimeInSec_Type()
)
acSysIPsecSAPhase2SaLifetimeInSec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAPhase2SaLifetimeInSec.setStatus("current")


class _AcSysIPsecSAPhase2SaLifetimeInKB_Type(Unsigned32):
    """Custom type acSysIPsecSAPhase2SaLifetimeInKB based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIPsecSAPhase2SaLifetimeInKB_Type.__name__ = "Unsigned32"
_AcSysIPsecSAPhase2SaLifetimeInKB_Object = MibTableColumn
acSysIPsecSAPhase2SaLifetimeInKB = _AcSysIPsecSAPhase2SaLifetimeInKB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 13),
    _AcSysIPsecSAPhase2SaLifetimeInKB_Type()
)
acSysIPsecSAPhase2SaLifetimeInKB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAPhase2SaLifetimeInKB.setStatus("current")


class _AcSysIPsecSADPDmode_Type(Integer32):
    """Custom type acSysIPsecSADPDmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dPDDisabled", 0),
          ("dPDOnDemand", 2),
          ("dPDPeriodic", 1))
    )


_AcSysIPsecSADPDmode_Type.__name__ = "Integer32"
_AcSysIPsecSADPDmode_Object = MibTableColumn
acSysIPsecSADPDmode = _AcSysIPsecSADPDmode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 14),
    _AcSysIPsecSADPDmode_Type()
)
acSysIPsecSADPDmode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSADPDmode.setStatus("current")


class _AcSysIPsecSAIPsecMode_Type(Integer32):
    """Custom type acSysIPsecSAIPsecMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("transport", 0),
          ("tunnel", 1))
    )


_AcSysIPsecSAIPsecMode_Type.__name__ = "Integer32"
_AcSysIPsecSAIPsecMode_Object = MibTableColumn
acSysIPsecSAIPsecMode = _AcSysIPsecSAIPsecMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 15),
    _AcSysIPsecSAIPsecMode_Type()
)
acSysIPsecSAIPsecMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSAIPsecMode.setStatus("current")


class _AcSysIPsecSARemoteTunnelAddress_Type(SnmpAdminString):
    """Custom type acSysIPsecSARemoteTunnelAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysIPsecSARemoteTunnelAddress_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSARemoteTunnelAddress_Object = MibTableColumn
acSysIPsecSARemoteTunnelAddress = _AcSysIPsecSARemoteTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 16),
    _AcSysIPsecSARemoteTunnelAddress_Type()
)
acSysIPsecSARemoteTunnelAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteTunnelAddress.setStatus("current")


class _AcSysIPsecSARemoteSubnetIPAddress_Type(SnmpAdminString):
    """Custom type acSysIPsecSARemoteSubnetIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysIPsecSARemoteSubnetIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysIPsecSARemoteSubnetIPAddress_Object = MibTableColumn
acSysIPsecSARemoteSubnetIPAddress = _AcSysIPsecSARemoteSubnetIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 17),
    _AcSysIPsecSARemoteSubnetIPAddress_Type()
)
acSysIPsecSARemoteSubnetIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteSubnetIPAddress.setStatus("current")


class _AcSysIPsecSARemoteSubnetPrefixLength_Type(Unsigned32):
    """Custom type acSysIPsecSARemoteSubnetPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysIPsecSARemoteSubnetPrefixLength_Type.__name__ = "Unsigned32"
_AcSysIPsecSARemoteSubnetPrefixLength_Object = MibTableColumn
acSysIPsecSARemoteSubnetPrefixLength = _AcSysIPsecSARemoteSubnetPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 22, 23, 1, 18),
    _AcSysIPsecSARemoteSubnetPrefixLength_Type()
)
acSysIPsecSARemoteSubnetPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysIPsecSARemoteSubnetPrefixLength.setStatus("current")
_AcFirewall_ObjectIdentity = ObjectIdentity
acFirewall = _AcFirewall_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23)
)
_AcSysAccessListTable_Object = MibTable
acSysAccessListTable = _AcSysAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1)
)
if mibBuilder.loadTexts:
    acSysAccessListTable.setStatus("current")
_AcSysAccessListEntry_Object = MibTableRow
acSysAccessListEntry = _AcSysAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1)
)
acSysAccessListEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysAccessListIndex"),
)
if mibBuilder.loadTexts:
    acSysAccessListEntry.setStatus("current")


class _AcSysAccessListIndex_Type(Unsigned32):
    """Custom type acSysAccessListIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AcSysAccessListIndex_Type.__name__ = "Unsigned32"
_AcSysAccessListIndex_Object = MibTableColumn
acSysAccessListIndex = _AcSysAccessListIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 1),
    _AcSysAccessListIndex_Type()
)
acSysAccessListIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysAccessListIndex.setStatus("current")
_AcSysAccessListRowStatus_Type = RowStatus
_AcSysAccessListRowStatus_Object = MibTableColumn
acSysAccessListRowStatus = _AcSysAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 2),
    _AcSysAccessListRowStatus_Type()
)
acSysAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListRowStatus.setStatus("current")


class _AcSysAccessListAction_Type(Integer32):
    """Custom type acSysAccessListAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysAccessListAction_Type.__name__ = "Integer32"
_AcSysAccessListAction_Object = MibTableColumn
acSysAccessListAction = _AcSysAccessListAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 3),
    _AcSysAccessListAction_Type()
)
acSysAccessListAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListAction.setStatus("current")


class _AcSysAccessListActionRes_Type(Integer32):
    """Custom type acSysAccessListActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysAccessListActionRes_Type.__name__ = "Integer32"
_AcSysAccessListActionRes_Object = MibTableColumn
acSysAccessListActionRes = _AcSysAccessListActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 4),
    _AcSysAccessListActionRes_Type()
)
acSysAccessListActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysAccessListActionRes.setStatus("current")


class _AcSysAccessListSourceIP_Type(SnmpAdminString):
    """Custom type acSysAccessListSourceIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 60),
    )


_AcSysAccessListSourceIP_Type.__name__ = "SnmpAdminString"
_AcSysAccessListSourceIP_Object = MibTableColumn
acSysAccessListSourceIP = _AcSysAccessListSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 5),
    _AcSysAccessListSourceIP_Type()
)
acSysAccessListSourceIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListSourceIP.setStatus("current")
_AcSysAccessListNetMask_Type = IpAddress
_AcSysAccessListNetMask_Object = MibTableColumn
acSysAccessListNetMask = _AcSysAccessListNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 6),
    _AcSysAccessListNetMask_Type()
)
acSysAccessListNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListNetMask.setStatus("current")


class _AcSysAccessListStartPort_Type(Unsigned32):
    """Custom type acSysAccessListStartPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListStartPort_Type.__name__ = "Unsigned32"
_AcSysAccessListStartPort_Object = MibTableColumn
acSysAccessListStartPort = _AcSysAccessListStartPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 7),
    _AcSysAccessListStartPort_Type()
)
acSysAccessListStartPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListStartPort.setStatus("current")


class _AcSysAccessListEndPort_Type(Unsigned32):
    """Custom type acSysAccessListEndPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListEndPort_Type.__name__ = "Unsigned32"
_AcSysAccessListEndPort_Object = MibTableColumn
acSysAccessListEndPort = _AcSysAccessListEndPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 8),
    _AcSysAccessListEndPort_Type()
)
acSysAccessListEndPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListEndPort.setStatus("current")


class _AcSysAccessListProtocol_Type(SnmpAdminString):
    """Custom type acSysAccessListProtocol based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AcSysAccessListProtocol_Type.__name__ = "SnmpAdminString"
_AcSysAccessListProtocol_Object = MibTableColumn
acSysAccessListProtocol = _AcSysAccessListProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 9),
    _AcSysAccessListProtocol_Type()
)
acSysAccessListProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListProtocol.setStatus("current")


class _AcSysAccessListPacketSize_Type(Unsigned32):
    """Custom type acSysAccessListPacketSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListPacketSize_Type.__name__ = "Unsigned32"
_AcSysAccessListPacketSize_Object = MibTableColumn
acSysAccessListPacketSize = _AcSysAccessListPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 10),
    _AcSysAccessListPacketSize_Type()
)
acSysAccessListPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListPacketSize.setStatus("current")


class _AcSysAccessListByteRate_Type(Unsigned32):
    """Custom type acSysAccessListByteRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysAccessListByteRate_Type.__name__ = "Unsigned32"
_AcSysAccessListByteRate_Object = MibTableColumn
acSysAccessListByteRate = _AcSysAccessListByteRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 11),
    _AcSysAccessListByteRate_Type()
)
acSysAccessListByteRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListByteRate.setStatus("current")


class _AcSysAccessListByteBurst_Type(Unsigned32):
    """Custom type acSysAccessListByteBurst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysAccessListByteBurst_Type.__name__ = "Unsigned32"
_AcSysAccessListByteBurst_Object = MibTableColumn
acSysAccessListByteBurst = _AcSysAccessListByteBurst_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 12),
    _AcSysAccessListByteBurst_Type()
)
acSysAccessListByteBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListByteBurst.setStatus("current")


class _AcSysAccessListAllowType_Type(Integer32):
    """Custom type acSysAccessListAllowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2),
          ("notSet", 0))
    )


_AcSysAccessListAllowType_Type.__name__ = "Integer32"
_AcSysAccessListAllowType_Object = MibTableColumn
acSysAccessListAllowType = _AcSysAccessListAllowType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 13),
    _AcSysAccessListAllowType_Type()
)
acSysAccessListAllowType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysAccessListAllowType.setStatus("current")


class _AcSysAccessListMatchCount_Type(Unsigned32):
    """Custom type acSysAccessListMatchCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysAccessListMatchCount_Type.__name__ = "Unsigned32"
_AcSysAccessListMatchCount_Object = MibTableColumn
acSysAccessListMatchCount = _AcSysAccessListMatchCount_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 23, 1, 1, 14),
    _AcSysAccessListMatchCount_Type()
)
acSysAccessListMatchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysAccessListMatchCount.setStatus("current")
_AcSysMediaEncription_ObjectIdentity = ObjectIdentity
acSysMediaEncription = _AcSysMediaEncription_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24)
)


class _AcSysMediaEncriptionRTPAuthenticationDisableTx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPAuthenticationDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AcSysMediaEncriptionRTPAuthenticationDisableTx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPAuthenticationDisableTx_Object = MibScalar
acSysMediaEncriptionRTPAuthenticationDisableTx = _AcSysMediaEncriptionRTPAuthenticationDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 1),
    _AcSysMediaEncriptionRTPAuthenticationDisableTx_Type()
)
acSysMediaEncriptionRTPAuthenticationDisableTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPAuthenticationDisableTx.setStatus("current")


class _AcSysMediaEncriptionRTPAuthenticationDisableRx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPAuthenticationDisableRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AcSysMediaEncriptionRTPAuthenticationDisableRx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPAuthenticationDisableRx_Object = MibScalar
acSysMediaEncriptionRTPAuthenticationDisableRx = _AcSysMediaEncriptionRTPAuthenticationDisableRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 2),
    _AcSysMediaEncriptionRTPAuthenticationDisableRx_Type()
)
acSysMediaEncriptionRTPAuthenticationDisableRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPAuthenticationDisableRx.setStatus("current")


class _AcSysMediaEncriptionRTPEncryptionDisableTx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPEncryptionDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AcSysMediaEncriptionRTPEncryptionDisableTx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPEncryptionDisableTx_Object = MibScalar
acSysMediaEncriptionRTPEncryptionDisableTx = _AcSysMediaEncriptionRTPEncryptionDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 3),
    _AcSysMediaEncriptionRTPEncryptionDisableTx_Type()
)
acSysMediaEncriptionRTPEncryptionDisableTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPEncryptionDisableTx.setStatus("current")


class _AcSysMediaEncriptionRTPEncryptionDisableRx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTPEncryptionDisableRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AcSysMediaEncriptionRTPEncryptionDisableRx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTPEncryptionDisableRx_Object = MibScalar
acSysMediaEncriptionRTPEncryptionDisableRx = _AcSysMediaEncriptionRTPEncryptionDisableRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 4),
    _AcSysMediaEncriptionRTPEncryptionDisableRx_Type()
)
acSysMediaEncriptionRTPEncryptionDisableRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTPEncryptionDisableRx.setStatus("current")


class _AcSysMediaEncriptionRTCPEncryptionDisableTx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTCPEncryptionDisableTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AcSysMediaEncriptionRTCPEncryptionDisableTx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTCPEncryptionDisableTx_Object = MibScalar
acSysMediaEncriptionRTCPEncryptionDisableTx = _AcSysMediaEncriptionRTCPEncryptionDisableTx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 5),
    _AcSysMediaEncriptionRTCPEncryptionDisableTx_Type()
)
acSysMediaEncriptionRTCPEncryptionDisableTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTCPEncryptionDisableTx.setStatus("current")


class _AcSysMediaEncriptionRTCPEncryptionDisableRx_Type(Integer32):
    """Custom type acSysMediaEncriptionRTCPEncryptionDisableRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_AcSysMediaEncriptionRTCPEncryptionDisableRx_Type.__name__ = "Integer32"
_AcSysMediaEncriptionRTCPEncryptionDisableRx_Object = MibScalar
acSysMediaEncriptionRTCPEncryptionDisableRx = _AcSysMediaEncriptionRTCPEncryptionDisableRx_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 6),
    _AcSysMediaEncriptionRTCPEncryptionDisableRx_Type()
)
acSysMediaEncriptionRTCPEncryptionDisableRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysMediaEncriptionRTCPEncryptionDisableRx.setStatus("current")
_AcSysSRTP_ObjectIdentity = ObjectIdentity
acSysSRTP = _AcSysSRTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 21)
)


class _AcSysSRTPPacketMKISize_Type(Unsigned32):
    """Custom type acSysSRTPPacketMKISize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcSysSRTPPacketMKISize_Type.__name__ = "Unsigned32"
_AcSysSRTPPacketMKISize_Object = MibScalar
acSysSRTPPacketMKISize = _AcSysSRTPPacketMKISize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 24, 21, 1),
    _AcSysSRTPPacketMKISize_Type()
)
acSysSRTPPacketMKISize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSRTPPacketMKISize.setStatus("current")
_AcSys802dot1x_ObjectIdentity = ObjectIdentity
acSys802dot1x = _AcSys802dot1x_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25)
)


class _AcSys802dot1xMode_Type(Integer32):
    """Custom type acSys802dot1xMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("eapMd5", 1),
          ("eapTls", 3),
          ("protectedEap", 2))
    )


_AcSys802dot1xMode_Type.__name__ = "Integer32"
_AcSys802dot1xMode_Object = MibScalar
acSys802dot1xMode = _AcSys802dot1xMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 1),
    _AcSys802dot1xMode_Type()
)
acSys802dot1xMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xMode.setStatus("current")


class _AcSys802dot1xUsername_Type(SnmpAdminString):
    """Custom type acSys802dot1xUsername based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AcSys802dot1xUsername_Type.__name__ = "SnmpAdminString"
_AcSys802dot1xUsername_Object = MibScalar
acSys802dot1xUsername = _AcSys802dot1xUsername_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 2),
    _AcSys802dot1xUsername_Type()
)
acSys802dot1xUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xUsername.setStatus("current")


class _AcSys802dot1xPassword_Type(SnmpAdminString):
    """Custom type acSys802dot1xPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AcSys802dot1xPassword_Type.__name__ = "SnmpAdminString"
_AcSys802dot1xPassword_Object = MibScalar
acSys802dot1xPassword = _AcSys802dot1xPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 3),
    _AcSys802dot1xPassword_Type()
)
acSys802dot1xPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xPassword.setStatus("current")


class _AcSys802dot1xVerifyPeerCertificate_Type(Integer32):
    """Custom type acSys802dot1xVerifyPeerCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSys802dot1xVerifyPeerCertificate_Type.__name__ = "Integer32"
_AcSys802dot1xVerifyPeerCertificate_Object = MibScalar
acSys802dot1xVerifyPeerCertificate = _AcSys802dot1xVerifyPeerCertificate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 7, 25, 4),
    _AcSys802dot1xVerifyPeerCertificate_Type()
)
acSys802dot1xVerifyPeerCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSys802dot1xVerifyPeerCertificate.setStatus("current")
_AcSysSerialIF_ObjectIdentity = ObjectIdentity
acSysSerialIF = _AcSysSerialIF_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8)
)


class _AcSysSerialIFBaudRate_Type(Unsigned32):
    """Custom type acSysSerialIFBaudRate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 115200),
    )


_AcSysSerialIFBaudRate_Type.__name__ = "Unsigned32"
_AcSysSerialIFBaudRate_Object = MibScalar
acSysSerialIFBaudRate = _AcSysSerialIFBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 1),
    _AcSysSerialIFBaudRate_Type()
)
acSysSerialIFBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFBaudRate.setStatus("current")


class _AcSysSerialIFData_Type(Unsigned32):
    """Custom type acSysSerialIFData based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_AcSysSerialIFData_Type.__name__ = "Unsigned32"
_AcSysSerialIFData_Object = MibScalar
acSysSerialIFData = _AcSysSerialIFData_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 2),
    _AcSysSerialIFData_Type()
)
acSysSerialIFData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFData.setStatus("current")


class _AcSysSerialIFParity_Type(Integer32):
    """Custom type acSysSerialIFParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("even", 2),
          ("none", 0),
          ("odd", 1))
    )


_AcSysSerialIFParity_Type.__name__ = "Integer32"
_AcSysSerialIFParity_Object = MibScalar
acSysSerialIFParity = _AcSysSerialIFParity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 3),
    _AcSysSerialIFParity_Type()
)
acSysSerialIFParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFParity.setStatus("current")


class _AcSysSerialIFStop_Type(Unsigned32):
    """Custom type acSysSerialIFStop based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSerialIFStop_Type.__name__ = "Unsigned32"
_AcSysSerialIFStop_Object = MibScalar
acSysSerialIFStop = _AcSysSerialIFStop_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 4),
    _AcSysSerialIFStop_Type()
)
acSysSerialIFStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFStop.setStatus("current")


class _AcSysSerialIFFlowControl_Type(Integer32):
    """Custom type acSysSerialIFFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hardware", 1),
          ("none", 0))
    )


_AcSysSerialIFFlowControl_Type.__name__ = "Integer32"
_AcSysSerialIFFlowControl_Object = MibScalar
acSysSerialIFFlowControl = _AcSysSerialIFFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 8, 5),
    _AcSysSerialIFFlowControl_Type()
)
acSysSerialIFFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysSerialIFFlowControl.setStatus("current")
_AcVoiceStream_ObjectIdentity = ObjectIdentity
acVoiceStream = _AcVoiceStream_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9)
)


class _AcVoiceStreamStatus_Type(Integer32):
    """Custom type acVoiceStreamStatus based on Integer32"""
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


_AcVoiceStreamStatus_Type.__name__ = "Integer32"
_AcVoiceStreamStatus_Object = MibScalar
acVoiceStreamStatus = _AcVoiceStreamStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9, 1),
    _AcVoiceStreamStatus_Type()
)
acVoiceStreamStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acVoiceStreamStatus.setStatus("current")


class _AcVoiceStreamUploadMethod_Type(Integer32):
    """Custom type acVoiceStreamUploadMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("httpPostMethod", 0),
          ("httpPutMethod", 1))
    )


_AcVoiceStreamUploadMethod_Type.__name__ = "Integer32"
_AcVoiceStreamUploadMethod_Object = MibScalar
acVoiceStreamUploadMethod = _AcVoiceStreamUploadMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9, 2),
    _AcVoiceStreamUploadMethod_Type()
)
acVoiceStreamUploadMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acVoiceStreamUploadMethod.setStatus("current")


class _AcVoiceStreamUploadPostUri_Type(SnmpAdminString):
    """Custom type acVoiceStreamUploadPostUri based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 59),
    )


_AcVoiceStreamUploadPostUri_Type.__name__ = "SnmpAdminString"
_AcVoiceStreamUploadPostUri_Object = MibScalar
acVoiceStreamUploadPostUri = _AcVoiceStreamUploadPostUri_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 9, 3),
    _AcVoiceStreamUploadPostUri_Type()
)
acVoiceStreamUploadPostUri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acVoiceStreamUploadPostUri.setStatus("current")
_AcSysAMS_ObjectIdentity = ObjectIdentity
acSysAMS = _AcSysAMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10)
)


class _AcSysAMSProfile_Type(Unsigned32):
    """Custom type acSysAMSProfile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AcSysAMSProfile_Type.__name__ = "Unsigned32"
_AcSysAMSProfile_Object = MibScalar
acSysAMSProfile = _AcSysAMSProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 1),
    _AcSysAMSProfile_Type()
)
acSysAMSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSProfile.setStatus("current")
_AcSysAMSApsIpAddress_Type = IpAddress
_AcSysAMSApsIpAddress_Object = MibScalar
acSysAMSApsIpAddress = _AcSysAMSApsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 2),
    _AcSysAMSApsIpAddress_Type()
)
acSysAMSApsIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSApsIpAddress.setStatus("current")


class _AcSysAMSApsPort_Type(Unsigned32):
    """Custom type acSysAMSApsPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64000),
    )


_AcSysAMSApsPort_Type.__name__ = "Unsigned32"
_AcSysAMSApsPort_Object = MibScalar
acSysAMSApsPort = _AcSysAMSApsPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 3),
    _AcSysAMSApsPort_Type()
)
acSysAMSApsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSApsPort.setStatus("current")


class _AcSysAMSPrimaryLanguage_Type(SnmpAdminString):
    """Custom type acSysAMSPrimaryLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AcSysAMSPrimaryLanguage_Type.__name__ = "SnmpAdminString"
_AcSysAMSPrimaryLanguage_Object = MibScalar
acSysAMSPrimaryLanguage = _AcSysAMSPrimaryLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 4),
    _AcSysAMSPrimaryLanguage_Type()
)
acSysAMSPrimaryLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSPrimaryLanguage.setStatus("current")


class _AcSysAMSSecondaryLanguage_Type(SnmpAdminString):
    """Custom type acSysAMSSecondaryLanguage based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AcSysAMSSecondaryLanguage_Type.__name__ = "SnmpAdminString"
_AcSysAMSSecondaryLanguage_Object = MibScalar
acSysAMSSecondaryLanguage = _AcSysAMSSecondaryLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 5),
    _AcSysAMSSecondaryLanguage_Type()
)
acSysAMSSecondaryLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSSecondaryLanguage.setStatus("current")


class _AcSysAMSAPSProfile_Type(Integer32):
    """Custom type acSysAMSAPSProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("apsProvidedAudio", 1),
          ("vpDatProvidedAudio", 0))
    )


_AcSysAMSAPSProfile_Type.__name__ = "Integer32"
_AcSysAMSAPSProfile_Object = MibScalar
acSysAMSAPSProfile = _AcSysAMSAPSProfile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 6),
    _AcSysAMSAPSProfile_Type()
)
acSysAMSAPSProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSAPSProfile.setStatus("current")


class _AcSysAMSForceRepositoryEnable_Type(Integer32):
    """Custom type acSysAMSForceRepositoryEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysAMSForceRepositoryEnable_Type.__name__ = "Integer32"
_AcSysAMSForceRepositoryEnable_Object = MibScalar
acSysAMSForceRepositoryEnable = _AcSysAMSForceRepositoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 10, 7),
    _AcSysAMSForceRepositoryEnable_Type()
)
acSysAMSForceRepositoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysAMSForceRepositoryEnable.setStatus("current")
_AcSysNetworkFileSystem_ObjectIdentity = ObjectIdentity
acSysNetworkFileSystem = _AcSysNetworkFileSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11)
)
_AcSysNFSTable_Object = MibTable
acSysNFSTable = _AcSysNFSTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21)
)
if mibBuilder.loadTexts:
    acSysNFSTable.setStatus("current")
_AcSysNFSEntry_Object = MibTableRow
acSysNFSEntry = _AcSysNFSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1)
)
acSysNFSEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysNFSIndex"),
)
if mibBuilder.loadTexts:
    acSysNFSEntry.setStatus("current")


class _AcSysNFSIndex_Type(Unsigned32):
    """Custom type acSysNFSIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcSysNFSIndex_Type.__name__ = "Unsigned32"
_AcSysNFSIndex_Object = MibTableColumn
acSysNFSIndex = _AcSysNFSIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 1),
    _AcSysNFSIndex_Type()
)
acSysNFSIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysNFSIndex.setStatus("current")
_AcSysNFSRowStatus_Type = RowStatus
_AcSysNFSRowStatus_Object = MibTableColumn
acSysNFSRowStatus = _AcSysNFSRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 2),
    _AcSysNFSRowStatus_Type()
)
acSysNFSRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSRowStatus.setStatus("current")


class _AcSysNFSAction_Type(Integer32):
    """Custom type acSysNFSAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("none", 0)
    )


_AcSysNFSAction_Type.__name__ = "Integer32"
_AcSysNFSAction_Object = MibTableColumn
acSysNFSAction = _AcSysNFSAction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 3),
    _AcSysNFSAction_Type()
)
acSysNFSAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSAction.setStatus("current")


class _AcSysNFSActionRes_Type(Integer32):
    """Custom type acSysNFSActionRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("succeeded", 0)
    )


_AcSysNFSActionRes_Type.__name__ = "Integer32"
_AcSysNFSActionRes_Object = MibTableColumn
acSysNFSActionRes = _AcSysNFSActionRes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 4),
    _AcSysNFSActionRes_Type()
)
acSysNFSActionRes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNFSActionRes.setStatus("current")


class _AcSysNFSHostOrIP_Type(SnmpAdminString):
    """Custom type acSysNFSHostOrIP based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysNFSHostOrIP_Type.__name__ = "SnmpAdminString"
_AcSysNFSHostOrIP_Object = MibTableColumn
acSysNFSHostOrIP = _AcSysNFSHostOrIP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 5),
    _AcSysNFSHostOrIP_Type()
)
acSysNFSHostOrIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSHostOrIP.setStatus("current")


class _AcSysNFSRootPath_Type(SnmpAdminString):
    """Custom type acSysNFSRootPath based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AcSysNFSRootPath_Type.__name__ = "SnmpAdminString"
_AcSysNFSRootPath_Object = MibTableColumn
acSysNFSRootPath = _AcSysNFSRootPath_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 6),
    _AcSysNFSRootPath_Type()
)
acSysNFSRootPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSRootPath.setStatus("current")


class _AcSysNFSNfsVersion_Type(Integer32):
    """Custom type acSysNFSNfsVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v2", 2),
          ("v3", 3))
    )


_AcSysNFSNfsVersion_Type.__name__ = "Integer32"
_AcSysNFSNfsVersion_Object = MibTableColumn
acSysNFSNfsVersion = _AcSysNFSNfsVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 7),
    _AcSysNFSNfsVersion_Type()
)
acSysNFSNfsVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSNfsVersion.setStatus("current")


class _AcSysNFSAuthType_Type(Integer32):
    """Custom type acSysNFSAuthType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("unix", 1))
    )


_AcSysNFSAuthType_Type.__name__ = "Integer32"
_AcSysNFSAuthType_Object = MibTableColumn
acSysNFSAuthType = _AcSysNFSAuthType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 8),
    _AcSysNFSAuthType_Type()
)
acSysNFSAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSAuthType.setStatus("current")


class _AcSysNFSUID_Type(Unsigned32):
    """Custom type acSysNFSUID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysNFSUID_Type.__name__ = "Unsigned32"
_AcSysNFSUID_Object = MibTableColumn
acSysNFSUID = _AcSysNFSUID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 9),
    _AcSysNFSUID_Type()
)
acSysNFSUID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSUID.setStatus("current")


class _AcSysNFSGID_Type(Unsigned32):
    """Custom type acSysNFSGID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysNFSGID_Type.__name__ = "Unsigned32"
_AcSysNFSGID_Object = MibTableColumn
acSysNFSGID = _AcSysNFSGID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 10),
    _AcSysNFSGID_Type()
)
acSysNFSGID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSGID.setStatus("current")


class _AcSysNFSVlanType_Type(Integer32):
    """Custom type acSysNFSVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("media", 1),
          ("oam", 0))
    )


_AcSysNFSVlanType_Type.__name__ = "Integer32"
_AcSysNFSVlanType_Object = MibTableColumn
acSysNFSVlanType = _AcSysNFSVlanType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 11, 21, 1, 11),
    _AcSysNFSVlanType_Type()
)
acSysNFSVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    acSysNFSVlanType.setStatus("current")
_AcSysHA_ObjectIdentity = ObjectIdentity
acSysHA = _AcSysHA_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12)
)
_AcSysHAGlobalIPAddress_Type = IpAddress
_AcSysHAGlobalIPAddress_Object = MibScalar
acSysHAGlobalIPAddress = _AcSysHAGlobalIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 12, 1),
    _AcSysHAGlobalIPAddress_Type()
)
acSysHAGlobalIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysHAGlobalIPAddress.setStatus("obsolete")
_AcSysTransmission_ObjectIdentity = ObjectIdentity
acSysTransmission = _AcSysTransmission_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 13)
)


class _AcSysTransmissionType_Type(Integer32):
    """Custom type acSysTransmissionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("copperDs3", 2),
          ("copperE1Ds1", 3),
          ("none", 0),
          ("opticalSonetSdh", 1))
    )


_AcSysTransmissionType_Type.__name__ = "Integer32"
_AcSysTransmissionType_Object = MibScalar
acSysTransmissionType = _AcSysTransmissionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 13, 1),
    _AcSysTransmissionType_Type()
)
acSysTransmissionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTransmissionType.setStatus("current")
_AcSysTiming_ObjectIdentity = ObjectIdentity
acSysTiming = _AcSysTiming_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14)
)


class _AcSysTimingMode_Type(Integer32):
    """Custom type acSysTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 1),
          ("lineSync", 2),
          ("standAlone", 0))
    )


_AcSysTimingMode_Type.__name__ = "Integer32"
_AcSysTimingMode_Object = MibScalar
acSysTimingMode = _AcSysTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 1),
    _AcSysTimingMode_Type()
)
acSysTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingMode.setStatus("current")


class _AcSysTimingValidationTime_Type(Unsigned32):
    """Custom type acSysTimingValidationTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcSysTimingValidationTime_Type.__name__ = "Unsigned32"
_AcSysTimingValidationTime_Object = MibScalar
acSysTimingValidationTime = _AcSysTimingValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 2),
    _AcSysTimingValidationTime_Type()
)
acSysTimingValidationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingValidationTime.setStatus("current")


class _AcSysTimingClockToDeriveA_Type(Integer32):
    """Custom type acSysTimingClockToDeriveA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clockFromReceiveSide", 7),
          ("deriveInternalClock", 4),
          ("deriveREFFromLineClock1", 0))
    )


_AcSysTimingClockToDeriveA_Type.__name__ = "Integer32"
_AcSysTimingClockToDeriveA_Object = MibScalar
acSysTimingClockToDeriveA = _AcSysTimingClockToDeriveA_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 3),
    _AcSysTimingClockToDeriveA_Type()
)
acSysTimingClockToDeriveA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingClockToDeriveA.setStatus("obsolete")


class _AcSysTimingClockToDeriveB_Type(Integer32):
    """Custom type acSysTimingClockToDeriveB based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("clockFromReceiveSide", 7),
          ("deriveInternalClock", 4),
          ("deriveREFFromLineClock1", 0))
    )


_AcSysTimingClockToDeriveB_Type.__name__ = "Integer32"
_AcSysTimingClockToDeriveB_Object = MibScalar
acSysTimingClockToDeriveB = _AcSysTimingClockToDeriveB_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 4),
    _AcSysTimingClockToDeriveB_Type()
)
acSysTimingClockToDeriveB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingClockToDeriveB.setStatus("obsolete")


class _AcSysTimingExternalIFType_Type(Integer32):
    """Custom type acSysTimingExternalIFType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1CAS", 1),
          ("e1CRC4", 0),
          ("e1FAS", 2),
          ("t12", 5),
          ("t1D4", 3),
          ("t1ESF", 4))
    )


_AcSysTimingExternalIFType_Type.__name__ = "Integer32"
_AcSysTimingExternalIFType_Object = MibScalar
acSysTimingExternalIFType = _AcSysTimingExternalIFType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 5),
    _AcSysTimingExternalIFType_Type()
)
acSysTimingExternalIFType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingExternalIFType.setStatus("current")


class _AcSysTimingLoopBackRef1_Type(Integer32):
    """Custom type acSysTimingLoopBackRef1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopDisable", 0),
          ("loopEnable", 1))
    )


_AcSysTimingLoopBackRef1_Type.__name__ = "Integer32"
_AcSysTimingLoopBackRef1_Object = MibScalar
acSysTimingLoopBackRef1 = _AcSysTimingLoopBackRef1_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 6),
    _AcSysTimingLoopBackRef1_Type()
)
acSysTimingLoopBackRef1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingLoopBackRef1.setStatus("current")


class _AcSysTimingLoopBackRef2_Type(Integer32):
    """Custom type acSysTimingLoopBackRef2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopDisable", 0),
          ("loopEnable", 1))
    )


_AcSysTimingLoopBackRef2_Type.__name__ = "Integer32"
_AcSysTimingLoopBackRef2_Object = MibScalar
acSysTimingLoopBackRef2 = _AcSysTimingLoopBackRef2_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 7),
    _AcSysTimingLoopBackRef2_Type()
)
acSysTimingLoopBackRef2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingLoopBackRef2.setStatus("current")


class _AcSysTimingTransmitControl_Type(Integer32):
    """Custom type acSysTimingTransmitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aIS", 1),
          ("disableTransmit", 2),
          ("systemClock", 0))
    )


_AcSysTimingTransmitControl_Type.__name__ = "Integer32"
_AcSysTimingTransmitControl_Object = MibScalar
acSysTimingTransmitControl = _AcSysTimingTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 8),
    _AcSysTimingTransmitControl_Type()
)
acSysTimingTransmitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingTransmitControl.setStatus("obsolete")


class _AcSysTimingE1LineBuildOut_Type(Integer32):
    """Custom type acSysTimingE1LineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("tm120OhmHighReturnLoss", 5),
          ("tm120OhmNormal", 1),
          ("tm120OhmNormalGappedClock", 7),
          ("tm75OhmHighReturnLoss", 4),
          ("tm75OhmNormal", 0),
          ("tm75OhmNormalGappedClock", 6))
    )


_AcSysTimingE1LineBuildOut_Type.__name__ = "Integer32"
_AcSysTimingE1LineBuildOut_Object = MibScalar
acSysTimingE1LineBuildOut = _AcSysTimingE1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 9),
    _AcSysTimingE1LineBuildOut_Type()
)
acSysTimingE1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingE1LineBuildOut.setStatus("obsolete")


class _AcSysTimingT1LineBuildOut_Type(Integer32):
    """Custom type acSysTimingT1LineBuildOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              7)
        )
    )
    namedValues = NamedValues(
        *(("dSX10to133feet0dBCSU", 0),
          ("dSX10to133ft0dBgappedclock", 7),
          ("dSX1133to266feet", 1),
          ("dSX1266to399feet", 2),
          ("dSX1399to533feet", 3),
          ("dSX1533to655feet", 4))
    )


_AcSysTimingT1LineBuildOut_Type.__name__ = "Integer32"
_AcSysTimingT1LineBuildOut_Object = MibScalar
acSysTimingT1LineBuildOut = _AcSysTimingT1LineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 14, 10),
    _AcSysTimingT1LineBuildOut_Type()
)
acSysTimingT1LineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysTimingT1LineBuildOut.setStatus("obsolete")
_AcSysLDAP_ObjectIdentity = ObjectIdentity
acSysLDAP = _AcSysLDAP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15)
)
_AcSysLDAPServerIp_Type = IpAddress
_AcSysLDAPServerIp_Object = MibScalar
acSysLDAPServerIp = _AcSysLDAPServerIp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 1),
    _AcSysLDAPServerIp_Type()
)
acSysLDAPServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerIp.setStatus("current")


class _AcSysLDAPServerPort_Type(Unsigned32):
    """Custom type acSysLDAPServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AcSysLDAPServerPort_Type.__name__ = "Unsigned32"
_AcSysLDAPServerPort_Object = MibScalar
acSysLDAPServerPort = _AcSysLDAPServerPort_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 2),
    _AcSysLDAPServerPort_Type()
)
acSysLDAPServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerPort.setStatus("current")


class _AcSysLDAPServerMaxRespondTime_Type(Unsigned32):
    """Custom type acSysLDAPServerMaxRespondTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_AcSysLDAPServerMaxRespondTime_Type.__name__ = "Unsigned32"
_AcSysLDAPServerMaxRespondTime_Object = MibScalar
acSysLDAPServerMaxRespondTime = _AcSysLDAPServerMaxRespondTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 3),
    _AcSysLDAPServerMaxRespondTime_Type()
)
acSysLDAPServerMaxRespondTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerMaxRespondTime.setStatus("current")


class _AcSysLDAPServerDomainName_Type(SnmpAdminString):
    """Custom type acSysLDAPServerDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPServerDomainName_Type.__name__ = "SnmpAdminString"
_AcSysLDAPServerDomainName_Object = MibScalar
acSysLDAPServerDomainName = _AcSysLDAPServerDomainName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 4),
    _AcSysLDAPServerDomainName_Type()
)
acSysLDAPServerDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServerDomainName.setStatus("current")


class _AcSysLDAPSearchDN_Type(SnmpAdminString):
    """Custom type acSysLDAPSearchDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPSearchDN_Type.__name__ = "SnmpAdminString"
_AcSysLDAPSearchDN_Object = MibScalar
acSysLDAPSearchDN = _AcSysLDAPSearchDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 5),
    _AcSysLDAPSearchDN_Type()
)
acSysLDAPSearchDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPSearchDN.setStatus("current")


class _AcSysLDAPPassword_Type(SnmpAdminString):
    """Custom type acSysLDAPPassword based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPPassword_Type.__name__ = "SnmpAdminString"
_AcSysLDAPPassword_Object = MibScalar
acSysLDAPPassword = _AcSysLDAPPassword_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 6),
    _AcSysLDAPPassword_Type()
)
acSysLDAPPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPPassword.setStatus("current")


class _AcSysLDAPBindDN_Type(SnmpAdminString):
    """Custom type acSysLDAPBindDN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AcSysLDAPBindDN_Type.__name__ = "SnmpAdminString"
_AcSysLDAPBindDN_Object = MibScalar
acSysLDAPBindDN = _AcSysLDAPBindDN_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 7),
    _AcSysLDAPBindDN_Type()
)
acSysLDAPBindDN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPBindDN.setStatus("current")


class _AcSysLDAPServiceEnable_Type(Integer32):
    """Custom type acSysLDAPServiceEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysLDAPServiceEnable_Type.__name__ = "Integer32"
_AcSysLDAPServiceEnable_Object = MibScalar
acSysLDAPServiceEnable = _AcSysLDAPServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 1, 15, 8),
    _AcSysLDAPServiceEnable_Type()
)
acSysLDAPServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysLDAPServiceEnable.setStatus("current")
_AcSystemStatus_ObjectIdentity = ObjectIdentity
acSystemStatus = _AcSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2)
)
_AcSysType_ObjectIdentity = ObjectIdentity
acSysType = _AcSysType_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1)
)


class _AcSysTypeProduct_Type(Integer32):
    """Custom type acSysTypeProduct based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              20,
              22,
              23,
              24,
              25,
              26,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69)
        )
    )
    namedValues = NamedValues(
        *(("acATP-1610", 53),
          ("acATP-260", 54),
          ("acATP-260-UN", 55),
          ("acIPMedia3000", 48),
          ("acIPmedia3000-T3", 61),
          ("acMediaPack-102", 26),
          ("acMediaPack-104", 25),
          ("acMediaPack-108", 2),
          ("acMediaPack-118", 56),
          ("acMediaPack-124", 3),
          ("acMediaPack-500-MSBG", 69),
          ("acMediaPack112", 58),
          ("acMediaPack114", 57),
          ("acMediant-600", 65),
          ("acMediant-600-MSBG", 68),
          ("acMediant1000", 47),
          ("acMediant1000-MSBG", 67),
          ("acMediant3000", 49),
          ("acMediant3000-T3", 60),
          ("acStretto3000", 50),
          ("acTPM1100", 22),
          ("acTPM1100-PCM", 44),
          ("acTPM6300", 46),
          ("acTrunkPack-08", 1),
          ("acTrunkPack-12610", 66),
          ("acTrunkPack-1600", 20),
          ("acTrunkPack-1610", 24),
          ("acTrunkPack-1610-IpMedia", 30),
          ("acTrunkPack-1610-SB", 29),
          ("acTrunkPack-260", 42),
          ("acTrunkPack-260-IpMedia", 23),
          ("acTrunkPack-260-IpMedia-120Ch", 38),
          ("acTrunkPack-260-IpMedia-30Ch", 36),
          ("acTrunkPack-260-IpMedia-60Ch", 37),
          ("acTrunkPack-260-UN", 43),
          ("acTrunkPack-260-UN-IpMedia", 35),
          ("acTrunkPack-260RT-IpMedia-120Ch", 41),
          ("acTrunkPack-260RT-IpMedia-30Ch", 39),
          ("acTrunkPack-260RT-IpMedia-60Ch", 40),
          ("acTrunkPack-2810", 34),
          ("acTrunkPack-6310", 45),
          ("acTrunkPack-6310-IpMedia", 51),
          ("acTrunkPack-6310-SB", 52),
          ("acTrunkPack-6310-T3", 59),
          ("acTrunkPack-6310-T3-IpMedia", 62),
          ("acTrunkPack-8410", 63),
          ("acTrunkPack-8410-IpMedia", 64),
          ("acTrunkPack-IPMServer2000", 33),
          ("acTrunkPack-MEDIANT2000", 31),
          ("acTrunkPack-STRETTO2000", 32),
          ("acUnknown", 0))
    )


_AcSysTypeProduct_Type.__name__ = "Integer32"
_AcSysTypeProduct_Object = MibScalar
acSysTypeProduct = _AcSysTypeProduct_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 1),
    _AcSysTypeProduct_Type()
)
acSysTypeProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeProduct.setStatus("current")


class _AcSysTypeDSP_Type(Unsigned32):
    """Custom type acSysTypeDSP based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTypeDSP_Type.__name__ = "Unsigned32"
_AcSysTypeDSP_Object = MibScalar
acSysTypeDSP = _AcSysTypeDSP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 2),
    _AcSysTypeDSP_Type()
)
acSysTypeDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeDSP.setStatus("current")


class _AcSysTypeModule_Type(Integer32):
    """Custom type acSysTypeModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("first", 2),
          ("second", 1),
          ("soloist", 0))
    )


_AcSysTypeModule_Type.__name__ = "Integer32"
_AcSysTypeModule_Object = MibScalar
acSysTypeModule = _AcSysTypeModule_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 3),
    _AcSysTypeModule_Type()
)
acSysTypeModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeModule.setStatus("current")


class _AcSysTypeCPUSpeed_Type(Unsigned32):
    """Custom type acSysTypeCPUSpeed based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTypeCPUSpeed_Type.__name__ = "Unsigned32"
_AcSysTypeCPUSpeed_Object = MibScalar
acSysTypeCPUSpeed = _AcSysTypeCPUSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 1, 4),
    _AcSysTypeCPUSpeed_Type()
)
acSysTypeCPUSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTypeCPUSpeed.setStatus("current")
_AcSysVersion_ObjectIdentity = ObjectIdentity
acSysVersion = _AcSysVersion_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2)
)


class _AcSysVersionSoftware_Type(SnmpAdminString):
    """Custom type acSysVersionSoftware based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysVersionSoftware_Type.__name__ = "SnmpAdminString"
_AcSysVersionSoftware_Object = MibScalar
acSysVersionSoftware = _AcSysVersionSoftware_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 1),
    _AcSysVersionSoftware_Type()
)
acSysVersionSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionSoftware.setStatus("current")


class _AcSysVersionFlash_Type(Unsigned32):
    """Custom type acSysVersionFlash based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVersionFlash_Type.__name__ = "Unsigned32"
_AcSysVersionFlash_Object = MibScalar
acSysVersionFlash = _AcSysVersionFlash_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 2),
    _AcSysVersionFlash_Type()
)
acSysVersionFlash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionFlash.setStatus("current")


class _AcSysVersionIniFile_Type(Unsigned32):
    """Custom type acSysVersionIniFile based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVersionIniFile_Type.__name__ = "Unsigned32"
_AcSysVersionIniFile_Object = MibScalar
acSysVersionIniFile = _AcSysVersionIniFile_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 3),
    _AcSysVersionIniFile_Type()
)
acSysVersionIniFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionIniFile.setStatus("current")


class _AcSysVersionSoftwareDate_Type(SnmpAdminString):
    """Custom type acSysVersionSoftwareDate based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysVersionSoftwareDate_Type.__name__ = "SnmpAdminString"
_AcSysVersionSoftwareDate_Object = MibScalar
acSysVersionSoftwareDate = _AcSysVersionSoftwareDate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 2, 4),
    _AcSysVersionSoftwareDate_Type()
)
acSysVersionSoftwareDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVersionSoftwareDate.setStatus("current")
_AcSysId_ObjectIdentity = ObjectIdentity
acSysId = _AcSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3)
)


class _AcSysIdName_Type(SnmpAdminString):
    """Custom type acSysIdName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysIdName_Type.__name__ = "SnmpAdminString"
_AcSysIdName_Object = MibScalar
acSysIdName = _AcSysIdName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 1),
    _AcSysIdName_Type()
)
acSysIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdName.setStatus("current")


class _AcSysIdSerialNumber_Type(Unsigned32):
    """Custom type acSysIdSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIdSerialNumber_Type.__name__ = "Unsigned32"
_AcSysIdSerialNumber_Object = MibScalar
acSysIdSerialNumber = _AcSysIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 2),
    _AcSysIdSerialNumber_Type()
)
acSysIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdSerialNumber.setStatus("current")


class _AcSysIdSlotNumber_Type(Unsigned32):
    """Custom type acSysIdSlotNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIdSlotNumber_Type.__name__ = "Unsigned32"
_AcSysIdSlotNumber_Object = MibScalar
acSysIdSlotNumber = _AcSysIdSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 3),
    _AcSysIdSlotNumber_Type()
)
acSysIdSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdSlotNumber.setStatus("current")


class _AcSysIdFirstSerialNumber_Type(Unsigned32):
    """Custom type acSysIdFirstSerialNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysIdFirstSerialNumber_Type.__name__ = "Unsigned32"
_AcSysIdFirstSerialNumber_Object = MibScalar
acSysIdFirstSerialNumber = _AcSysIdFirstSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 3, 4),
    _AcSysIdFirstSerialNumber_Type()
)
acSysIdFirstSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysIdFirstSerialNumber.setStatus("current")
_AcSysCount_ObjectIdentity = ObjectIdentity
acSysCount = _AcSysCount_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4)
)


class _AcSysCountDSPs_Type(Unsigned32):
    """Custom type acSysCountDSPs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysCountDSPs_Type.__name__ = "Unsigned32"
_AcSysCountDSPs_Object = MibScalar
acSysCountDSPs = _AcSysCountDSPs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4, 1),
    _AcSysCountDSPs_Type()
)
acSysCountDSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysCountDSPs.setStatus("current")


class _AcSysCountChannels_Type(Unsigned32):
    """Custom type acSysCountChannels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysCountChannels_Type.__name__ = "Unsigned32"
_AcSysCountChannels_Object = MibScalar
acSysCountChannels = _AcSysCountChannels_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4, 2),
    _AcSysCountChannels_Type()
)
acSysCountChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysCountChannels.setStatus("current")


class _AcSysCountTrunks_Type(Unsigned32):
    """Custom type acSysCountTrunks based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysCountTrunks_Type.__name__ = "Unsigned32"
_AcSysCountTrunks_Object = MibScalar
acSysCountTrunks = _AcSysCountTrunks_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 4, 3),
    _AcSysCountTrunks_Type()
)
acSysCountTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysCountTrunks.setStatus("current")
_AcSysState_ObjectIdentity = ObjectIdentity
acSysState = _AcSysState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5)
)


class _AcSysStateTemperature_Type(Unsigned32):
    """Custom type acSysStateTemperature based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcSysStateTemperature_Type.__name__ = "Unsigned32"
_AcSysStateTemperature_Object = MibScalar
acSysStateTemperature = _AcSysStateTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 1),
    _AcSysStateTemperature_Type()
)
acSysStateTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateTemperature.setStatus("current")


class _AcSysStateOperational_Type(Integer32):
    """Custom type acSysStateOperational based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AcSysStateOperational_Type.__name__ = "Integer32"
_AcSysStateOperational_Object = MibScalar
acSysStateOperational = _AcSysStateOperational_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 2),
    _AcSysStateOperational_Type()
)
acSysStateOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateOperational.setStatus("current")


class _AcSysStateHAupdateInProgress_Type(Integer32):
    """Custom type acSysStateHAupdateInProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("updateDone", 1),
          ("updateInProgress", 2))
    )


_AcSysStateHAupdateInProgress_Type.__name__ = "Integer32"
_AcSysStateHAupdateInProgress_Object = MibScalar
acSysStateHAupdateInProgress = _AcSysStateHAupdateInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 3),
    _AcSysStateHAupdateInProgress_Type()
)
acSysStateHAupdateInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateHAupdateInProgress.setStatus("current")


class _AcSysStateGWSeverity_Type(Integer32):
    """Custom type acSysStateGWSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("critical", 5),
          ("indeterminate", 1),
          ("major", 4),
          ("minor", 3),
          ("noAlarm", 0),
          ("warning", 2))
    )


_AcSysStateGWSeverity_Type.__name__ = "Integer32"
_AcSysStateGWSeverity_Object = MibScalar
acSysStateGWSeverity = _AcSysStateGWSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 4),
    _AcSysStateGWSeverity_Type()
)
acSysStateGWSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateGWSeverity.setStatus("current")


class _AcSysStateIsPstnManagementEnable_Type(Integer32):
    """Custom type acSysStateIsPstnManagementEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AcSysStateIsPstnManagementEnable_Type.__name__ = "Integer32"
_AcSysStateIsPstnManagementEnable_Object = MibScalar
acSysStateIsPstnManagementEnable = _AcSysStateIsPstnManagementEnable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 5, 5),
    _AcSysStateIsPstnManagementEnable_Type()
)
acSysStateIsPstnManagementEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysStateIsPstnManagementEnable.setStatus("current")
_AcSysNetwork_ObjectIdentity = ObjectIdentity
acSysNetwork = _AcSysNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6)
)
_AcSysEthernet_ObjectIdentity = ObjectIdentity
acSysEthernet = _AcSysEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1)
)


class _AcSysEthernetFirstPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetFirstPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("fullDuplex", 1),
          ("halfDuplex", 0),
          ("notAvailable", 3))
    )


_AcSysEthernetFirstPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetFirstPortDuplexMode_Object = MibScalar
acSysEthernetFirstPortDuplexMode = _AcSysEthernetFirstPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 1),
    _AcSysEthernetFirstPortDuplexMode_Type()
)
acSysEthernetFirstPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetFirstPortDuplexMode.setStatus("current")


class _AcSysEthernetFirstPortSpeed_Type(Integer32):
    """Custom type acSysEthernetFirstPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("ac1000Mbps", 1000),
          ("ac100Mbps", 100),
          ("ac10Mbps", 10),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetFirstPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetFirstPortSpeed_Object = MibScalar
acSysEthernetFirstPortSpeed = _AcSysEthernetFirstPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 2),
    _AcSysEthernetFirstPortSpeed_Type()
)
acSysEthernetFirstPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetFirstPortSpeed.setStatus("current")


class _AcSysEthernetSecondPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetSecondPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("fullDuplex", 1),
          ("halfDuplex", 0),
          ("notAvailable", 3))
    )


_AcSysEthernetSecondPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetSecondPortDuplexMode_Object = MibScalar
acSysEthernetSecondPortDuplexMode = _AcSysEthernetSecondPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 3),
    _AcSysEthernetSecondPortDuplexMode_Type()
)
acSysEthernetSecondPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetSecondPortDuplexMode.setStatus("current")


class _AcSysEthernetSecondPortSpeed_Type(Integer32):
    """Custom type acSysEthernetSecondPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("ac1000Mbps", 1000),
          ("ac100Mbps", 100),
          ("ac10Mbps", 10),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetSecondPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetSecondPortSpeed_Object = MibScalar
acSysEthernetSecondPortSpeed = _AcSysEthernetSecondPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 4),
    _AcSysEthernetSecondPortSpeed_Type()
)
acSysEthernetSecondPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetSecondPortSpeed.setStatus("current")


class _AcSysEthernetActivePortNumber_Type(Unsigned32):
    """Custom type acSysEthernetActivePortNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcSysEthernetActivePortNumber_Type.__name__ = "Unsigned32"
_AcSysEthernetActivePortNumber_Object = MibScalar
acSysEthernetActivePortNumber = _AcSysEthernetActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 5),
    _AcSysEthernetActivePortNumber_Type()
)
acSysEthernetActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetActivePortNumber.setStatus("current")
_AcSysEthernetStatusTable_Object = MibTable
acSysEthernetStatusTable = _AcSysEthernetStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21)
)
if mibBuilder.loadTexts:
    acSysEthernetStatusTable.setStatus("current")
_AcSysEthernetStatusEntry_Object = MibTableRow
acSysEthernetStatusEntry = _AcSysEthernetStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1)
)
acSysEthernetStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysEthernetStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysEthernetStatusEntry.setStatus("current")


class _AcSysEthernetStatusIndex_Type(Unsigned32):
    """Custom type acSysEthernetStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_AcSysEthernetStatusIndex_Type.__name__ = "Unsigned32"
_AcSysEthernetStatusIndex_Object = MibTableColumn
acSysEthernetStatusIndex = _AcSysEthernetStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 1),
    _AcSysEthernetStatusIndex_Type()
)
acSysEthernetStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysEthernetStatusIndex.setStatus("current")


class _AcSysEthernetStatusPortDuplexMode_Type(Integer32):
    """Custom type acSysEthernetStatusPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceModeValue", 2),
          ("fullDuplex", 1),
          ("halfDuplex", 0),
          ("notAvailable", 3))
    )


_AcSysEthernetStatusPortDuplexMode_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortDuplexMode_Object = MibTableColumn
acSysEthernetStatusPortDuplexMode = _AcSysEthernetStatusPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 2),
    _AcSysEthernetStatusPortDuplexMode_Type()
)
acSysEthernetStatusPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortDuplexMode.setStatus("current")


class _AcSysEthernetStatusPortSpeed_Type(Integer32):
    """Custom type acSysEthernetStatusPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              10,
              100,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("ac1000Mbps", 1000),
          ("ac100Mbps", 100),
          ("ac10Mbps", 10),
          ("forceModeValue", 2),
          ("notAvailable", 3))
    )


_AcSysEthernetStatusPortSpeed_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortSpeed_Object = MibTableColumn
acSysEthernetStatusPortSpeed = _AcSysEthernetStatusPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 3),
    _AcSysEthernetStatusPortSpeed_Type()
)
acSysEthernetStatusPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortSpeed.setStatus("current")


class _AcSysEthernetStatusActivePortNumber_Type(Integer32):
    """Custom type acSysEthernetStatusActivePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 0))
    )


_AcSysEthernetStatusActivePortNumber_Type.__name__ = "Integer32"
_AcSysEthernetStatusActivePortNumber_Object = MibTableColumn
acSysEthernetStatusActivePortNumber = _AcSysEthernetStatusActivePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 4),
    _AcSysEthernetStatusActivePortNumber_Type()
)
acSysEthernetStatusActivePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusActivePortNumber.setStatus("current")


class _AcSysEthernetStatusPortState_Type(Integer32):
    """Custom type acSysEthernetStatusPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("disabled", 0),
          ("forwarding", 3),
          ("learning", 2),
          ("notApplicable", 10))
    )


_AcSysEthernetStatusPortState_Type.__name__ = "Integer32"
_AcSysEthernetStatusPortState_Object = MibTableColumn
acSysEthernetStatusPortState = _AcSysEthernetStatusPortState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 5),
    _AcSysEthernetStatusPortState_Type()
)
acSysEthernetStatusPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPortState.setStatus("current")


class _AcSysEthernetStatusPowerOverEthernet_Type(Integer32):
    """Custom type acSysEthernetStatusPowerOverEthernet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notActive", 2),
          ("notApplicable", 0))
    )


_AcSysEthernetStatusPowerOverEthernet_Type.__name__ = "Integer32"
_AcSysEthernetStatusPowerOverEthernet_Object = MibTableColumn
acSysEthernetStatusPowerOverEthernet = _AcSysEthernetStatusPowerOverEthernet_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 1, 21, 1, 6),
    _AcSysEthernetStatusPowerOverEthernet_Type()
)
acSysEthernetStatusPowerOverEthernet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysEthernetStatusPowerOverEthernet.setStatus("current")
_AcSysNAT_ObjectIdentity = ObjectIdentity
acSysNAT = _AcSysNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 2)
)


class _AcSysNATType_Type(Integer32):
    """Custom type acSysNATType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              10)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 6),
          ("fullCone", 1),
          ("natIdentificationInProgress", 10),
          ("none", 0),
          ("portRestricted", 3),
          ("restricted", 2),
          ("stunDisabled", -1),
          ("symmetric", 4),
          ("symmetricFireWall", 5),
          ("unknown", 7))
    )


_AcSysNATType_Type.__name__ = "Integer32"
_AcSysNATType_Object = MibScalar
acSysNATType = _AcSysNATType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 2, 1),
    _AcSysNATType_Type()
)
acSysNATType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysNATType.setStatus("current")
_AcSysWebStat_ObjectIdentity = ObjectIdentity
acSysWebStat = _AcSysWebStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 3)
)


class _AcSysWebStatPasswordControlViaSNMP_Type(Integer32):
    """Custom type acSysWebStatPasswordControlViaSNMP based on Integer32"""
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


_AcSysWebStatPasswordControlViaSNMP_Type.__name__ = "Integer32"
_AcSysWebStatPasswordControlViaSNMP_Object = MibScalar
acSysWebStatPasswordControlViaSNMP = _AcSysWebStatPasswordControlViaSNMP_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 3, 1),
    _AcSysWebStatPasswordControlViaSNMP_Type()
)
acSysWebStatPasswordControlViaSNMP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysWebStatPasswordControlViaSNMP.setStatus("current")
_AcSysIPStatus_ObjectIdentity = ObjectIdentity
acSysIPStatus = _AcSysIPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4)
)
_AcSysInterfaceStatusTable_Object = MibTable
acSysInterfaceStatusTable = _AcSysInterfaceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21)
)
if mibBuilder.loadTexts:
    acSysInterfaceStatusTable.setStatus("current")
_AcSysInterfaceStatusEntry_Object = MibTableRow
acSysInterfaceStatusEntry = _AcSysInterfaceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1)
)
acSysInterfaceStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysInterfaceStatusEntryIndex"),
    (0, "AC-SYSTEM-MIB", "acSysInterfaceStatusTypeIndex"),
)
if mibBuilder.loadTexts:
    acSysInterfaceStatusEntry.setStatus("current")


class _AcSysInterfaceStatusEntryIndex_Type(Unsigned32):
    """Custom type acSysInterfaceStatusEntryIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AcSysInterfaceStatusEntryIndex_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusEntryIndex_Object = MibTableColumn
acSysInterfaceStatusEntryIndex = _AcSysInterfaceStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 1),
    _AcSysInterfaceStatusEntryIndex_Type()
)
acSysInterfaceStatusEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysInterfaceStatusEntryIndex.setStatus("current")


class _AcSysInterfaceStatusTypeIndex_Type(Unsigned32):
    """Custom type acSysInterfaceStatusTypeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysInterfaceStatusTypeIndex_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusTypeIndex_Object = MibTableColumn
acSysInterfaceStatusTypeIndex = _AcSysInterfaceStatusTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 2),
    _AcSysInterfaceStatusTypeIndex_Type()
)
acSysInterfaceStatusTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysInterfaceStatusTypeIndex.setStatus("current")


class _AcSysInterfaceStatusApplicationTypes_Type(Integer32):
    """Custom type acSysInterfaceStatusApplicationTypes based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("control", 2),
          ("data", 11),
          ("media", 1),
          ("mediaAndControl", 5),
          ("oam", 0),
          ("oamAndControl", 4),
          ("oamAndMedia", 3),
          ("oamAndMediaAndControl", 6))
    )


_AcSysInterfaceStatusApplicationTypes_Type.__name__ = "Integer32"
_AcSysInterfaceStatusApplicationTypes_Object = MibTableColumn
acSysInterfaceStatusApplicationTypes = _AcSysInterfaceStatusApplicationTypes_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 3),
    _AcSysInterfaceStatusApplicationTypes_Type()
)
acSysInterfaceStatusApplicationTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusApplicationTypes.setStatus("current")


class _AcSysInterfaceStatusMode_Type(Integer32):
    """Custom type acSysInterfaceStatusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              10)
        )
    )
    namedValues = NamedValues(
        *(("iPv4Manual", 10),
          ("iPv6Manual", 4),
          ("iPv6PrefixManual", 3))
    )


_AcSysInterfaceStatusMode_Type.__name__ = "Integer32"
_AcSysInterfaceStatusMode_Object = MibTableColumn
acSysInterfaceStatusMode = _AcSysInterfaceStatusMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 4),
    _AcSysInterfaceStatusMode_Type()
)
acSysInterfaceStatusMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusMode.setStatus("current")


class _AcSysInterfaceStatusIPAddress_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusIPAddress based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceStatusIPAddress_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusIPAddress_Object = MibTableColumn
acSysInterfaceStatusIPAddress = _AcSysInterfaceStatusIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 5),
    _AcSysInterfaceStatusIPAddress_Type()
)
acSysInterfaceStatusIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusIPAddress.setStatus("current")


class _AcSysInterfaceStatusPrefixLength_Type(Unsigned32):
    """Custom type acSysInterfaceStatusPrefixLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AcSysInterfaceStatusPrefixLength_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusPrefixLength_Object = MibTableColumn
acSysInterfaceStatusPrefixLength = _AcSysInterfaceStatusPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 6),
    _AcSysInterfaceStatusPrefixLength_Type()
)
acSysInterfaceStatusPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusPrefixLength.setStatus("current")


class _AcSysInterfaceStatusGateway_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusGateway based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 45),
    )


_AcSysInterfaceStatusGateway_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusGateway_Object = MibTableColumn
acSysInterfaceStatusGateway = _AcSysInterfaceStatusGateway_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 7),
    _AcSysInterfaceStatusGateway_Type()
)
acSysInterfaceStatusGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusGateway.setStatus("current")


class _AcSysInterfaceStatusVlanID_Type(Unsigned32):
    """Custom type acSysInterfaceStatusVlanID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AcSysInterfaceStatusVlanID_Type.__name__ = "Unsigned32"
_AcSysInterfaceStatusVlanID_Object = MibTableColumn
acSysInterfaceStatusVlanID = _AcSysInterfaceStatusVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 8),
    _AcSysInterfaceStatusVlanID_Type()
)
acSysInterfaceStatusVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusVlanID.setStatus("current")


class _AcSysInterfaceStatusName_Type(SnmpAdminString):
    """Custom type acSysInterfaceStatusName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AcSysInterfaceStatusName_Type.__name__ = "SnmpAdminString"
_AcSysInterfaceStatusName_Object = MibTableColumn
acSysInterfaceStatusName = _AcSysInterfaceStatusName_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 6, 4, 21, 1, 9),
    _AcSysInterfaceStatusName_Type()
)
acSysInterfaceStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysInterfaceStatusName.setStatus("current")
_AcSysTime_ObjectIdentity = ObjectIdentity
acSysTime = _AcSysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7)
)


class _AcSysTimeUp_Type(Unsigned32):
    """Custom type acSysTimeUp based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysTimeUp_Type.__name__ = "Unsigned32"
_AcSysTimeUp_Object = MibScalar
acSysTimeUp = _AcSysTimeUp_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 7, 1),
    _AcSysTimeUp_Type()
)
acSysTimeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysTimeUp.setStatus("current")
_AcSysVoicePrompt_ObjectIdentity = ObjectIdentity
acSysVoicePrompt = _AcSysVoicePrompt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 8)
)


class _AcSysVoicePromptTotalMemorySize_Type(Unsigned32):
    """Custom type acSysVoicePromptTotalMemorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVoicePromptTotalMemorySize_Type.__name__ = "Unsigned32"
_AcSysVoicePromptTotalMemorySize_Object = MibScalar
acSysVoicePromptTotalMemorySize = _AcSysVoicePromptTotalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 8, 1),
    _AcSysVoicePromptTotalMemorySize_Type()
)
acSysVoicePromptTotalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVoicePromptTotalMemorySize.setStatus("current")


class _AcSysVoicePromptMaxFreeMemorySize_Type(Unsigned32):
    """Custom type acSysVoicePromptMaxFreeMemorySize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysVoicePromptMaxFreeMemorySize_Type.__name__ = "Unsigned32"
_AcSysVoicePromptMaxFreeMemorySize_Object = MibScalar
acSysVoicePromptMaxFreeMemorySize = _AcSysVoicePromptMaxFreeMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 8, 2),
    _AcSysVoicePromptMaxFreeMemorySize_Type()
)
acSysVoicePromptMaxFreeMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysVoicePromptMaxFreeMemorySize.setStatus("current")
_AcSysRepositoryAMS_ObjectIdentity = ObjectIdentity
acSysRepositoryAMS = _AcSysRepositoryAMS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 9)
)


class _AcSysRepositoryAMSIsReadyForUpdate_Type(Integer32):
    """Custom type acSysRepositoryAMSIsReadyForUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AcSysRepositoryAMSIsReadyForUpdate_Type.__name__ = "Integer32"
_AcSysRepositoryAMSIsReadyForUpdate_Object = MibScalar
acSysRepositoryAMSIsReadyForUpdate = _AcSysRepositoryAMSIsReadyForUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 9, 1),
    _AcSysRepositoryAMSIsReadyForUpdate_Type()
)
acSysRepositoryAMSIsReadyForUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysRepositoryAMSIsReadyForUpdate.setStatus("current")
_AcSysHAStatus_ObjectIdentity = ObjectIdentity
acSysHAStatus = _AcSysHAStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 10)
)


class _AcSysHAStatusReady_Type(Integer32):
    """Custom type acSysHAStatusReady based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 3),
          ("notApplicable", 1),
          ("yes", 2))
    )


_AcSysHAStatusReady_Type.__name__ = "Integer32"
_AcSysHAStatusReady_Object = MibScalar
acSysHAStatusReady = _AcSysHAStatusReady_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 10, 1),
    _AcSysHAStatusReady_Type()
)
acSysHAStatusReady.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysHAStatusReady.setStatus("current")
_AcSysLDAPStatus_ObjectIdentity = ObjectIdentity
acSysLDAPStatus = _AcSysLDAPStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 11)
)


class _AcSysLDAPStatusServerMode_Type(Integer32):
    """Custom type acSysLDAPStatusServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 3),
          ("connecting", 2),
          ("connectionBroken", 1),
          ("notApplicable", 0))
    )


_AcSysLDAPStatusServerMode_Type.__name__ = "Integer32"
_AcSysLDAPStatusServerMode_Object = MibScalar
acSysLDAPStatusServerMode = _AcSysLDAPStatusServerMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 2, 11, 1),
    _AcSysLDAPStatusServerMode_Type()
)
acSysLDAPStatusServerMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysLDAPStatusServerMode.setStatus("current")
_AcSystemAction_ObjectIdentity = ObjectIdentity
acSystemAction = _AcSystemAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3)
)
_AcSysAction_ObjectIdentity = ObjectIdentity
acSysAction = _AcSysAction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1)
)
_AcSysActionSet_ObjectIdentity = ObjectIdentity
acSysActionSet = _AcSysActionSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1)
)


class _AcSysActionSetReset_Type(Unsigned32):
    """Custom type acSysActionSetReset based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetReset_Type.__name__ = "Unsigned32"
_AcSysActionSetReset_Object = MibScalar
acSysActionSetReset = _AcSysActionSetReset_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 1),
    _AcSysActionSetReset_Type()
)
acSysActionSetReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetReset.setStatus("current")


class _AcSysActionSetResetControl_Type(Integer32):
    """Custom type acSysActionSetResetControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("resetFromBootP", 3),
          ("resetFromFlashAfterBurn", 1),
          ("resetFromFlashNoBurn", 2))
    )


_AcSysActionSetResetControl_Type.__name__ = "Integer32"
_AcSysActionSetResetControl_Object = MibScalar
acSysActionSetResetControl = _AcSysActionSetResetControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 2),
    _AcSysActionSetResetControl_Type()
)
acSysActionSetResetControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetResetControl.setStatus("current")


class _AcSysActionSetDefaults_Type(Unsigned32):
    """Custom type acSysActionSetDefaults based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetDefaults_Type.__name__ = "Unsigned32"
_AcSysActionSetDefaults_Object = MibScalar
acSysActionSetDefaults = _AcSysActionSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 3),
    _AcSysActionSetDefaults_Type()
)
acSysActionSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetDefaults.setStatus("current")


class _AcSysActionSetSaveConfig_Type(Unsigned32):
    """Custom type acSysActionSetSaveConfig based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetSaveConfig_Type.__name__ = "Unsigned32"
_AcSysActionSetSaveConfig_Object = MibScalar
acSysActionSetSaveConfig = _AcSysActionSetSaveConfig_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 4),
    _AcSysActionSetSaveConfig_Type()
)
acSysActionSetSaveConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetSaveConfig.setStatus("current")


class _AcSysActionSetAutoUpdate_Type(Unsigned32):
    """Custom type acSysActionSetAutoUpdate based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetAutoUpdate_Type.__name__ = "Unsigned32"
_AcSysActionSetAutoUpdate_Object = MibScalar
acSysActionSetAutoUpdate = _AcSysActionSetAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 5),
    _AcSysActionSetAutoUpdate_Type()
)
acSysActionSetAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetAutoUpdate.setStatus("current")


class _AcSysActionSetGetTimeFromNTPServer_Type(Unsigned32):
    """Custom type acSysActionSetGetTimeFromNTPServer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysActionSetGetTimeFromNTPServer_Type.__name__ = "Unsigned32"
_AcSysActionSetGetTimeFromNTPServer_Object = MibScalar
acSysActionSetGetTimeFromNTPServer = _AcSysActionSetGetTimeFromNTPServer_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 6),
    _AcSysActionSetGetTimeFromNTPServer_Type()
)
acSysActionSetGetTimeFromNTPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetGetTimeFromNTPServer.setStatus("current")


class _AcSysActionSetSwUpgrade_Type(Integer32):
    """Custom type acSysActionSetSwUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hitLessUpGrade", 1),
          ("systemResetUpGrade", 2))
    )


_AcSysActionSetSwUpgrade_Type.__name__ = "Integer32"
_AcSysActionSetSwUpgrade_Object = MibScalar
acSysActionSetSwUpgrade = _AcSysActionSetSwUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 7),
    _AcSysActionSetSwUpgrade_Type()
)
acSysActionSetSwUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetSwUpgrade.setStatus("current")


class _AcSysActionSetOnLineChangesApply_Type(Integer32):
    """Custom type acSysActionSetOnLineChangesApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("applyChanges", 1),
          ("defaultValue", 0))
    )


_AcSysActionSetOnLineChangesApply_Type.__name__ = "Integer32"
_AcSysActionSetOnLineChangesApply_Object = MibScalar
acSysActionSetOnLineChangesApply = _AcSysActionSetOnLineChangesApply_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 8),
    _AcSysActionSetOnLineChangesApply_Type()
)
acSysActionSetOnLineChangesApply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetOnLineChangesApply.setStatus("current")


class _AcSysActionSetIPSecTLSUpgrade_Type(Integer32):
    """Custom type acSysActionSetIPSecTLSUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("defaultValue", 0),
          ("upDateChanges", 1))
    )


_AcSysActionSetIPSecTLSUpgrade_Type.__name__ = "Integer32"
_AcSysActionSetIPSecTLSUpgrade_Object = MibScalar
acSysActionSetIPSecTLSUpgrade = _AcSysActionSetIPSecTLSUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 9),
    _AcSysActionSetIPSecTLSUpgrade_Type()
)
acSysActionSetIPSecTLSUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetIPSecTLSUpgrade.setStatus("current")


class _AcSysActionSetGWAppTLSUpgrade_Type(Integer32):
    """Custom type acSysActionSetGWAppTLSUpgrade based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("defaultValue", 0),
          ("upDateChanges", 1))
    )


_AcSysActionSetGWAppTLSUpgrade_Type.__name__ = "Integer32"
_AcSysActionSetGWAppTLSUpgrade_Object = MibScalar
acSysActionSetGWAppTLSUpgrade = _AcSysActionSetGWAppTLSUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 10),
    _AcSysActionSetGWAppTLSUpgrade_Type()
)
acSysActionSetGWAppTLSUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetGWAppTLSUpgrade.setStatus("current")


class _AcSysActionSetConvertNetworkIFsConfiguration_Type(Integer32):
    """Custom type acSysActionSetConvertNetworkIFsConfiguration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("convertAction", 1),
          ("defaultValue", 0))
    )


_AcSysActionSetConvertNetworkIFsConfiguration_Type.__name__ = "Integer32"
_AcSysActionSetConvertNetworkIFsConfiguration_Object = MibScalar
acSysActionSetConvertNetworkIFsConfiguration = _AcSysActionSetConvertNetworkIFsConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 11),
    _AcSysActionSetConvertNetworkIFsConfiguration_Type()
)
acSysActionSetConvertNetworkIFsConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetConvertNetworkIFsConfiguration.setStatus("current")


class _AcSysActionSetActionId_Type(Unsigned32):
    """Custom type acSysActionSetActionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysActionSetActionId_Type.__name__ = "Unsigned32"
_AcSysActionSetActionId_Object = MibScalar
acSysActionSetActionId = _AcSysActionSetActionId_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 12),
    _AcSysActionSetActionId_Type()
)
acSysActionSetActionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionSetActionId.setStatus("current")


class _AcSysActionSetAutoUpdateActionResult_Type(SnmpAdminString):
    """Custom type acSysActionSetAutoUpdateActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AcSysActionSetAutoUpdateActionResult_Type.__name__ = "SnmpAdminString"
_AcSysActionSetAutoUpdateActionResult_Object = MibScalar
acSysActionSetAutoUpdateActionResult = _AcSysActionSetAutoUpdateActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 1, 13),
    _AcSysActionSetAutoUpdateActionResult_Type()
)
acSysActionSetAutoUpdateActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysActionSetAutoUpdateActionResult.setStatus("current")
_AcSysActionAdmin_ObjectIdentity = ObjectIdentity
acSysActionAdmin = _AcSysActionAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 2)
)


class _AcSysActionAdminState_Type(Integer32):
    """Custom type acSysActionAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 0),
          ("shuttingDown", 1),
          ("unlocked", 2))
    )


_AcSysActionAdminState_Type.__name__ = "Integer32"
_AcSysActionAdminState_Object = MibScalar
acSysActionAdminState = _AcSysActionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 2, 1),
    _AcSysActionAdminState_Type()
)
acSysActionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionAdminState.setStatus("current")


class _AcSysActionAdminStateLockTimeout_Type(Integer32):
    """Custom type acSysActionAdminStateLockTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32768),
    )


_AcSysActionAdminStateLockTimeout_Type.__name__ = "Integer32"
_AcSysActionAdminStateLockTimeout_Object = MibScalar
acSysActionAdminStateLockTimeout = _AcSysActionAdminStateLockTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 2, 2),
    _AcSysActionAdminStateLockTimeout_Type()
)
acSysActionAdminStateLockTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysActionAdminStateLockTimeout.setStatus("current")
_AcSysUpload_ObjectIdentity = ObjectIdentity
acSysUpload = _AcSysUpload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3)
)


class _AcSysUploadActionType_Type(Integer32):
    """Custom type acSysUploadActionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("actionDone", 10),
          ("none", 0),
          ("remove", 2),
          ("upload", 1))
    )


_AcSysUploadActionType_Type.__name__ = "Integer32"
_AcSysUploadActionType_Object = MibScalar
acSysUploadActionType = _AcSysUploadActionType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 1),
    _AcSysUploadActionType_Type()
)
acSysUploadActionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadActionType.setStatus("current")


class _AcSysUploadFileType_Type(Integer32):
    """Custom type acSysUploadFileType based on Integer32"""
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
        *(("casFile", 7),
          ("cptFile", 2),
          ("dataConfigurationFile", 17),
          ("dialPlanFile", 11),
          ("externalCoderFile", 9),
          ("fxoCoeffFile", 6),
          ("fxsCoeffFile", 5),
          ("iniFile", 1),
          ("prerecordedTonesFile", 4),
          ("tlsCertFile", 13),
          ("tlsPKeyFile", 12),
          ("tlsRootFile", 14),
          ("userInfoFile", 10),
          ("v5PortFile", 16),
          ("videoFontFile", 15),
          ("vpFile", 3),
          ("xmlFile", 8))
    )


_AcSysUploadFileType_Type.__name__ = "Integer32"
_AcSysUploadFileType_Object = MibScalar
acSysUploadFileType = _AcSysUploadFileType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 2),
    _AcSysUploadFileType_Type()
)
acSysUploadFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadFileType.setStatus("current")


class _AcSysUploadFileNumber_Type(Integer32):
    """Custom type acSysUploadFileNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AcSysUploadFileNumber_Type.__name__ = "Integer32"
_AcSysUploadFileNumber_Object = MibScalar
acSysUploadFileNumber = _AcSysUploadFileNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 3),
    _AcSysUploadFileNumber_Type()
)
acSysUploadFileNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadFileNumber.setStatus("current")


class _AcSysUploadFileURI_Type(SnmpAdminString):
    """Custom type acSysUploadFileURI based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 254),
    )


_AcSysUploadFileURI_Type.__name__ = "SnmpAdminString"
_AcSysUploadFileURI_Object = MibScalar
acSysUploadFileURI = _AcSysUploadFileURI_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 4),
    _AcSysUploadFileURI_Type()
)
acSysUploadFileURI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadFileURI.setStatus("current")


class _AcSysUploadActionID_Type(Unsigned32):
    """Custom type acSysUploadActionID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcSysUploadActionID_Type.__name__ = "Unsigned32"
_AcSysUploadActionID_Object = MibScalar
acSysUploadActionID = _AcSysUploadActionID_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 5),
    _AcSysUploadActionID_Type()
)
acSysUploadActionID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysUploadActionID.setStatus("current")


class _AcSysUploadActionResult_Type(SnmpAdminString):
    """Custom type acSysUploadActionResult based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AcSysUploadActionResult_Type.__name__ = "SnmpAdminString"
_AcSysUploadActionResult_Object = MibScalar
acSysUploadActionResult = _AcSysUploadActionResult_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 3, 1, 3, 6),
    _AcSysUploadActionResult_Type()
)
acSysUploadActionResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysUploadActionResult.setStatus("current")
_AcSystemChassis_ObjectIdentity = ObjectIdentity
acSystemChassis = _AcSystemChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4)
)


class _AcSystemChassisDryContactsOutStatus_Type(Bits):
    """Custom type acSystemChassisDryContactsOutStatus based on Bits"""
    namedValues = NamedValues(
        *(("criticalAlarm", 1),
          ("majorAlarm", 2),
          ("minorAlarm", 3),
          ("noAlarm", 0))
    )

_AcSystemChassisDryContactsOutStatus_Type.__name__ = "Bits"
_AcSystemChassisDryContactsOutStatus_Object = MibScalar
acSystemChassisDryContactsOutStatus = _AcSystemChassisDryContactsOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 1),
    _AcSystemChassisDryContactsOutStatus_Type()
)
acSystemChassisDryContactsOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisDryContactsOutStatus.setStatus("current")


class _AcSystemChassisDryContactsInStatus_Type(Bits):
    """Custom type acSystemChassisDryContactsInStatus based on Bits"""
    namedValues = NamedValues(
        *(("alarm1", 1),
          ("noAlarm", 0))
    )

_AcSystemChassisDryContactsInStatus_Type.__name__ = "Bits"
_AcSystemChassisDryContactsInStatus_Object = MibScalar
acSystemChassisDryContactsInStatus = _AcSystemChassisDryContactsInStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 2),
    _AcSystemChassisDryContactsInStatus_Type()
)
acSystemChassisDryContactsInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisDryContactsInStatus.setStatus("current")


class _AcSystemChassisLastChanged_Type(Unsigned32):
    """Custom type acSystemChassisLastChanged based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AcSystemChassisLastChanged_Type.__name__ = "Unsigned32"
_AcSystemChassisLastChanged_Object = MibScalar
acSystemChassisLastChanged = _AcSystemChassisLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 3),
    _AcSystemChassisLastChanged_Type()
)
acSystemChassisLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSystemChassisLastChanged.setStatus("current")
_AcSysModuleTable_Object = MibTable
acSysModuleTable = _AcSysModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21)
)
if mibBuilder.loadTexts:
    acSysModuleTable.setStatus("current")
_AcSysModuleEntry_Object = MibTableRow
acSysModuleEntry = _AcSysModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1)
)
acSysModuleEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysModuleIndex"),
)
if mibBuilder.loadTexts:
    acSysModuleEntry.setStatus("current")


class _AcSysModuleIndex_Type(Unsigned32):
    """Custom type acSysModuleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysModuleIndex_Type.__name__ = "Unsigned32"
_AcSysModuleIndex_Object = MibTableColumn
acSysModuleIndex = _AcSysModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 1),
    _AcSysModuleIndex_Type()
)
acSysModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysModuleIndex.setStatus("current")


class _AcSysModuleGeographicalPosition_Type(Unsigned32):
    """Custom type acSysModuleGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSysModuleGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysModuleGeographicalPosition_Object = MibTableColumn
acSysModuleGeographicalPosition = _AcSysModuleGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 2),
    _AcSysModuleGeographicalPosition_Type()
)
acSysModuleGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleGeographicalPosition.setStatus("current")


class _AcSysModuleType_Type(Integer32):
    """Custom type acSysModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              20,
              22,
              23,
              24,
              25,
              26,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              69,
              250,
              251,
              252,
              253,
              254,
              255,
              256,
              257,
              258,
              259,
              260,
              261,
              262,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279)
        )
    )
    namedValues = NamedValues(
        *(("acATP-1610", 53),
          ("acATP-260", 54),
          ("acATP-260-UN", 55),
          ("acIPMedia3000", 48),
          ("acIPmedia3000-T3", 61),
          ("acMediaPack-102", 26),
          ("acMediaPack-104", 25),
          ("acMediaPack-108", 2),
          ("acMediaPack-118", 56),
          ("acMediaPack-124", 3),
          ("acMediaPack-500-MSBG", 69),
          ("acMediaPack112", 58),
          ("acMediaPack114", 57),
          ("acMediaPack500CPUmodule", 265),
          ("acMediaPack500EthernetModule", 272),
          ("acMediaPack500IFADSLModule", 275),
          ("acMediaPack500IFAnalogModule", 267),
          ("acMediaPack500IFBRIModule", 268),
          ("acMediaPack500IFDigitalModule", 266),
          ("acMediaPack500IFSHDSLModule", 274),
          ("acMediaPack500IFT1WANModule", 273),
          ("acMediaPack500IFWANModule", 269),
          ("acMediaPack500IFWiFiModule", 270),
          ("acMediaPack500IPMediaModule", 271),
          ("acMediant1000", 47),
          ("acMediant1000CPUmodule", 253),
          ("acMediant1000IFADSLModule", 279),
          ("acMediant1000IFAnalogModule", 255),
          ("acMediant1000IFBRIModule", 256),
          ("acMediant1000IFDigitalModule", 254),
          ("acMediant1000IFSHDSLModule", 278),
          ("acMediant1000IFT1WANModule", 277),
          ("acMediant1000IFWANModule", 276),
          ("acMediant1000IPMediaModule", 257),
          ("acMediant3000", 49),
          ("acMediant3000-T3", 60),
          ("acMediant600CPUmodule", 258),
          ("acMediant600IFAnalogModule", 260),
          ("acMediant600IFBRIModule", 261),
          ("acMediant600IFDigitalModule", 259),
          ("acMediant600IPMediaModule", 262),
          ("acStretto3000", 50),
          ("acTPM1100", 22),
          ("acTPM1100-PCM", 44),
          ("acTPM6300", 46),
          ("acTrunkPack-08", 1),
          ("acTrunkPack-1600", 20),
          ("acTrunkPack-1610", 24),
          ("acTrunkPack-1610-IpMedia", 30),
          ("acTrunkPack-1610-SB", 29),
          ("acTrunkPack-260", 42),
          ("acTrunkPack-260-IpMedia", 23),
          ("acTrunkPack-260-IpMedia-120Ch", 38),
          ("acTrunkPack-260-IpMedia-30Ch", 36),
          ("acTrunkPack-260-IpMedia-60Ch", 37),
          ("acTrunkPack-260-UN", 43),
          ("acTrunkPack-260-UN-IpMedia", 35),
          ("acTrunkPack-260RT-IpMedia-120Ch", 41),
          ("acTrunkPack-260RT-IpMedia-30Ch", 39),
          ("acTrunkPack-260RT-IpMedia-60Ch", 40),
          ("acTrunkPack-2810", 34),
          ("acTrunkPack-6310", 45),
          ("acTrunkPack-6310-IpMedia", 51),
          ("acTrunkPack-6310-SB", 52),
          ("acTrunkPack-6310-T3", 59),
          ("acTrunkPack-6310-T3-IpMedia", 62),
          ("acTrunkPack-8410", 63),
          ("acTrunkPack-8410-IpMedia", 64),
          ("acTrunkPack-IPMServer2000", 33),
          ("acTrunkPack-MEDIANT2000", 31),
          ("acTrunkPack-STRETTO2000", 32),
          ("acUnknown", 0),
          ("sA1", 250),
          ("sA2", 251),
          ("sA3", 252))
    )


_AcSysModuleType_Type.__name__ = "Integer32"
_AcSysModuleType_Object = MibTableColumn
acSysModuleType = _AcSysModuleType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 3),
    _AcSysModuleType_Type()
)
acSysModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleType.setStatus("current")


class _AcSysModulePresence_Type(Integer32):
    """Custom type acSysModulePresence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("present", 1))
    )


_AcSysModulePresence_Type.__name__ = "Integer32"
_AcSysModulePresence_Object = MibTableColumn
acSysModulePresence = _AcSysModulePresence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 4),
    _AcSysModulePresence_Type()
)
acSysModulePresence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModulePresence.setStatus("current")


class _AcSysModuleLicenseKeyList_Type(SnmpAdminString):
    """Custom type acSysModuleLicenseKeyList based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1400),
    )


_AcSysModuleLicenseKeyList_Type.__name__ = "SnmpAdminString"
_AcSysModuleLicenseKeyList_Object = MibTableColumn
acSysModuleLicenseKeyList = _AcSysModuleLicenseKeyList_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 5),
    _AcSysModuleLicenseKeyList_Type()
)
acSysModuleLicenseKeyList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleLicenseKeyList.setStatus("current")


class _AcSysModuleSerialNumber_Type(Integer32):
    """Custom type acSysModuleSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcSysModuleSerialNumber_Type.__name__ = "Integer32"
_AcSysModuleSerialNumber_Object = MibTableColumn
acSysModuleSerialNumber = _AcSysModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 6),
    _AcSysModuleSerialNumber_Type()
)
acSysModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleSerialNumber.setStatus("current")


class _AcSysModuleSWVersion_Type(SnmpAdminString):
    """Custom type acSysModuleSWVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysModuleSWVersion_Type.__name__ = "SnmpAdminString"
_AcSysModuleSWVersion_Object = MibTableColumn
acSysModuleSWVersion = _AcSysModuleSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 7),
    _AcSysModuleSWVersion_Type()
)
acSysModuleSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleSWVersion.setStatus("current")


class _AcSysModuleOperationalState_Type(Integer32):
    """Custom type acSysModuleOperationalState based on Integer32"""
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


_AcSysModuleOperationalState_Type.__name__ = "Integer32"
_AcSysModuleOperationalState_Object = MibTableColumn
acSysModuleOperationalState = _AcSysModuleOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 8),
    _AcSysModuleOperationalState_Type()
)
acSysModuleOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleOperationalState.setStatus("current")


class _AcSysModuleHAStatus_Type(Integer32):
    """Custom type acSysModuleHAStatus based on Integer32"""
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
        *(("acitveNonHA", 1),
          ("active", 2),
          ("notApplicable", 6),
          ("redundant", 3),
          ("redundantNonHA", 5),
          ("standAlone", 4))
    )


_AcSysModuleHAStatus_Type.__name__ = "Integer32"
_AcSysModuleHAStatus_Object = MibTableColumn
acSysModuleHAStatus = _AcSysModuleHAStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 9),
    _AcSysModuleHAStatus_Type()
)
acSysModuleHAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleHAStatus.setStatus("current")


class _AcSysModuleLEDs_Type(OctetString):
    """Custom type acSysModuleLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysModuleLEDs_Type.__name__ = "OctetString"
_AcSysModuleLEDs_Object = MibTableColumn
acSysModuleLEDs = _AcSysModuleLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 10),
    _AcSysModuleLEDs_Type()
)
acSysModuleLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleLEDs.setStatus("current")


class _AcSysModuleTemperature_Type(Integer32):
    """Custom type acSysModuleTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcSysModuleTemperature_Type.__name__ = "Integer32"
_AcSysModuleTemperature_Object = MibTableColumn
acSysModuleTemperature = _AcSysModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 11),
    _AcSysModuleTemperature_Type()
)
acSysModuleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleTemperature.setStatus("current")


class _AcSysModuleActions_Type(Integer32):
    """Custom type acSysModuleActions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("actionDone", 3),
          ("reset", 1),
          ("switchOver", 2))
    )


_AcSysModuleActions_Type.__name__ = "Integer32"
_AcSysModuleActions_Object = MibTableColumn
acSysModuleActions = _AcSysModuleActions_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 12),
    _AcSysModuleActions_Type()
)
acSysModuleActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysModuleActions.setStatus("current")


class _AcSysModuleFRUaction_Type(Integer32):
    """Custom type acSysModuleFRUaction based on Integer32"""
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
        *(("fruActionDone", 1),
          ("fruBackToServiceAction", 3),
          ("fruNotApplicable", 4),
          ("fruOutOfServiceAction", 2))
    )


_AcSysModuleFRUaction_Type.__name__ = "Integer32"
_AcSysModuleFRUaction_Object = MibTableColumn
acSysModuleFRUaction = _AcSysModuleFRUaction_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 13),
    _AcSysModuleFRUaction_Type()
)
acSysModuleFRUaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acSysModuleFRUaction.setStatus("current")


class _AcSysModuleFRUstatus_Type(Integer32):
    """Custom type acSysModuleFRUstatus based on Integer32"""
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
        *(("moduleBackToServiceStart", 4),
          ("moduleExistOk", 2),
          ("moduleFaulty", 6),
          ("moduleMismatch", 5),
          ("moduleNotExist", 1),
          ("moduleOutOfService", 3),
          ("notApplicable", 7))
    )


_AcSysModuleFRUstatus_Type.__name__ = "Integer32"
_AcSysModuleFRUstatus_Object = MibTableColumn
acSysModuleFRUstatus = _AcSysModuleFRUstatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 14),
    _AcSysModuleFRUstatus_Type()
)
acSysModuleFRUstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleFRUstatus.setStatus("current")


class _AcSysModuleNumOfPorts_Type(Unsigned32):
    """Custom type acSysModuleNumOfPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AcSysModuleNumOfPorts_Type.__name__ = "Unsigned32"
_AcSysModuleNumOfPorts_Object = MibTableColumn
acSysModuleNumOfPorts = _AcSysModuleNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 15),
    _AcSysModuleNumOfPorts_Type()
)
acSysModuleNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleNumOfPorts.setStatus("current")


class _AcSysModuleFirstPortNum_Type(Unsigned32):
    """Custom type acSysModuleFirstPortNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 19),
    )


_AcSysModuleFirstPortNum_Type.__name__ = "Unsigned32"
_AcSysModuleFirstPortNum_Object = MibTableColumn
acSysModuleFirstPortNum = _AcSysModuleFirstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 21, 1, 16),
    _AcSysModuleFirstPortNum_Type()
)
acSysModuleFirstPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysModuleFirstPortNum.setStatus("current")
_AcSysFanTrayTable_Object = MibTable
acSysFanTrayTable = _AcSysFanTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22)
)
if mibBuilder.loadTexts:
    acSysFanTrayTable.setStatus("current")
_AcSysFanTrayEntry_Object = MibTableRow
acSysFanTrayEntry = _AcSysFanTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1)
)
acSysFanTrayEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysFanTrayIndex"),
)
if mibBuilder.loadTexts:
    acSysFanTrayEntry.setStatus("current")


class _AcSysFanTrayIndex_Type(Unsigned32):
    """Custom type acSysFanTrayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysFanTrayIndex_Type.__name__ = "Unsigned32"
_AcSysFanTrayIndex_Object = MibTableColumn
acSysFanTrayIndex = _AcSysFanTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 1),
    _AcSysFanTrayIndex_Type()
)
acSysFanTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysFanTrayIndex.setStatus("current")


class _AcSysFanTrayGeographicalPosition_Type(Unsigned32):
    """Custom type acSysFanTrayGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AcSysFanTrayGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysFanTrayGeographicalPosition_Object = MibTableColumn
acSysFanTrayGeographicalPosition = _AcSysFanTrayGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 2),
    _AcSysFanTrayGeographicalPosition_Type()
)
acSysFanTrayGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayGeographicalPosition.setStatus("current")


class _AcSysFanTrayExistence_Type(Integer32):
    """Custom type acSysFanTrayExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("present", 1))
    )


_AcSysFanTrayExistence_Type.__name__ = "Integer32"
_AcSysFanTrayExistence_Object = MibTableColumn
acSysFanTrayExistence = _AcSysFanTrayExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 3),
    _AcSysFanTrayExistence_Type()
)
acSysFanTrayExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayExistence.setStatus("current")


class _AcSysFanTrayType_Type(SnmpAdminString):
    """Custom type acSysFanTrayType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_AcSysFanTrayType_Type.__name__ = "SnmpAdminString"
_AcSysFanTrayType_Object = MibTableColumn
acSysFanTrayType = _AcSysFanTrayType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 4),
    _AcSysFanTrayType_Type()
)
acSysFanTrayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayType.setStatus("current")


class _AcSysFanTrayLEDs_Type(OctetString):
    """Custom type acSysFanTrayLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysFanTrayLEDs_Type.__name__ = "OctetString"
_AcSysFanTrayLEDs_Object = MibTableColumn
acSysFanTrayLEDs = _AcSysFanTrayLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 5),
    _AcSysFanTrayLEDs_Type()
)
acSysFanTrayLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayLEDs.setStatus("current")


class _AcSysFanTraySeverity_Type(Integer32):
    """Custom type acSysFanTraySeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 0),
          ("critical", 5),
          ("indeterminate", 1),
          ("major", 4),
          ("minor", 3),
          ("warning", 2))
    )


_AcSysFanTraySeverity_Type.__name__ = "Integer32"
_AcSysFanTraySeverity_Object = MibTableColumn
acSysFanTraySeverity = _AcSysFanTraySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 6),
    _AcSysFanTraySeverity_Type()
)
acSysFanTraySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTraySeverity.setStatus("current")


class _AcSysFanTrayFansConfiguredSpeed_Type(OctetString):
    """Custom type acSysFanTrayFansConfiguredSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcSysFanTrayFansConfiguredSpeed_Type.__name__ = "OctetString"
_AcSysFanTrayFansConfiguredSpeed_Object = MibTableColumn
acSysFanTrayFansConfiguredSpeed = _AcSysFanTrayFansConfiguredSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 7),
    _AcSysFanTrayFansConfiguredSpeed_Type()
)
acSysFanTrayFansConfiguredSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayFansConfiguredSpeed.setStatus("current")


class _AcSysFanTrayFansCurrentSpeed_Type(OctetString):
    """Custom type acSysFanTrayFansCurrentSpeed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AcSysFanTrayFansCurrentSpeed_Type.__name__ = "OctetString"
_AcSysFanTrayFansCurrentSpeed_Object = MibTableColumn
acSysFanTrayFansCurrentSpeed = _AcSysFanTrayFansCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 8),
    _AcSysFanTrayFansCurrentSpeed_Type()
)
acSysFanTrayFansCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayFansCurrentSpeed.setStatus("current")


class _AcSysFanTrayFansStatus_Type(OctetString):
    """Custom type acSysFanTrayFansStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_AcSysFanTrayFansStatus_Type.__name__ = "OctetString"
_AcSysFanTrayFansStatus_Object = MibTableColumn
acSysFanTrayFansStatus = _AcSysFanTrayFansStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 22, 1, 9),
    _AcSysFanTrayFansStatus_Type()
)
acSysFanTrayFansStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysFanTrayFansStatus.setStatus("current")
_AcSysPowerSupplyTable_Object = MibTable
acSysPowerSupplyTable = _AcSysPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23)
)
if mibBuilder.loadTexts:
    acSysPowerSupplyTable.setStatus("current")
_AcSysPowerSupplyEntry_Object = MibTableRow
acSysPowerSupplyEntry = _AcSysPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1)
)
acSysPowerSupplyEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPowerSupplyIndex"),
)
if mibBuilder.loadTexts:
    acSysPowerSupplyEntry.setStatus("current")


class _AcSysPowerSupplyIndex_Type(Unsigned32):
    """Custom type acSysPowerSupplyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysPowerSupplyIndex_Type.__name__ = "Unsigned32"
_AcSysPowerSupplyIndex_Object = MibTableColumn
acSysPowerSupplyIndex = _AcSysPowerSupplyIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 1),
    _AcSysPowerSupplyIndex_Type()
)
acSysPowerSupplyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPowerSupplyIndex.setStatus("current")


class _AcSysPowerSupplyGeographicalPosition_Type(Unsigned32):
    """Custom type acSysPowerSupplyGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysPowerSupplyGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysPowerSupplyGeographicalPosition_Object = MibTableColumn
acSysPowerSupplyGeographicalPosition = _AcSysPowerSupplyGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 2),
    _AcSysPowerSupplyGeographicalPosition_Type()
)
acSysPowerSupplyGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyGeographicalPosition.setStatus("current")


class _AcSysPowerSupplyExistence_Type(Integer32):
    """Custom type acSysPowerSupplyExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("present", 1))
    )


_AcSysPowerSupplyExistence_Type.__name__ = "Integer32"
_AcSysPowerSupplyExistence_Object = MibTableColumn
acSysPowerSupplyExistence = _AcSysPowerSupplyExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 3),
    _AcSysPowerSupplyExistence_Type()
)
acSysPowerSupplyExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyExistence.setStatus("current")


class _AcSysPowerSupplyHwversion_Type(SnmpAdminString):
    """Custom type acSysPowerSupplyHwversion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysPowerSupplyHwversion_Type.__name__ = "SnmpAdminString"
_AcSysPowerSupplyHwversion_Object = MibTableColumn
acSysPowerSupplyHwversion = _AcSysPowerSupplyHwversion_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 4),
    _AcSysPowerSupplyHwversion_Type()
)
acSysPowerSupplyHwversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyHwversion.setStatus("current")


class _AcSysPowerSupplyLEDs_Type(OctetString):
    """Custom type acSysPowerSupplyLEDs based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysPowerSupplyLEDs_Type.__name__ = "OctetString"
_AcSysPowerSupplyLEDs_Object = MibTableColumn
acSysPowerSupplyLEDs = _AcSysPowerSupplyLEDs_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 5),
    _AcSysPowerSupplyLEDs_Type()
)
acSysPowerSupplyLEDs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplyLEDs.setStatus("current")


class _AcSysPowerSupplySeverity_Type(Integer32):
    """Custom type acSysPowerSupplySeverity based on Integer32"""
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
        *(("cleared", 1),
          ("critical", 6),
          ("indeterminate", 2),
          ("major", 5),
          ("minor", 4),
          ("warning", 3))
    )


_AcSysPowerSupplySeverity_Type.__name__ = "Integer32"
_AcSysPowerSupplySeverity_Object = MibTableColumn
acSysPowerSupplySeverity = _AcSysPowerSupplySeverity_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 23, 1, 6),
    _AcSysPowerSupplySeverity_Type()
)
acSysPowerSupplySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPowerSupplySeverity.setStatus("current")
_AcSysPEMTable_Object = MibTable
acSysPEMTable = _AcSysPEMTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24)
)
if mibBuilder.loadTexts:
    acSysPEMTable.setStatus("current")
_AcSysPEMEntry_Object = MibTableRow
acSysPEMEntry = _AcSysPEMEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1)
)
acSysPEMEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPEMIndex"),
)
if mibBuilder.loadTexts:
    acSysPEMEntry.setStatus("current")


class _AcSysPEMIndex_Type(Unsigned32):
    """Custom type acSysPEMIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AcSysPEMIndex_Type.__name__ = "Unsigned32"
_AcSysPEMIndex_Object = MibTableColumn
acSysPEMIndex = _AcSysPEMIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 1),
    _AcSysPEMIndex_Type()
)
acSysPEMIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPEMIndex.setStatus("current")


class _AcSysPEMGeographicalPosition_Type(Unsigned32):
    """Custom type acSysPEMGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysPEMGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysPEMGeographicalPosition_Object = MibTableColumn
acSysPEMGeographicalPosition = _AcSysPEMGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 2),
    _AcSysPEMGeographicalPosition_Type()
)
acSysPEMGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMGeographicalPosition.setStatus("current")


class _AcSysPEMExistence_Type(Integer32):
    """Custom type acSysPEMExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("present", 1))
    )


_AcSysPEMExistence_Type.__name__ = "Integer32"
_AcSysPEMExistence_Object = MibTableColumn
acSysPEMExistence = _AcSysPEMExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 3),
    _AcSysPEMExistence_Type()
)
acSysPEMExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMExistence.setStatus("current")


class _AcSysPEMType_Type(SnmpAdminString):
    """Custom type acSysPEMType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysPEMType_Type.__name__ = "SnmpAdminString"
_AcSysPEMType_Object = MibTableColumn
acSysPEMType = _AcSysPEMType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 4),
    _AcSysPEMType_Type()
)
acSysPEMType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMType.setStatus("current")


class _AcSysPEMElectricWireConnection_Type(Integer32):
    """Custom type acSysPEMElectricWireConnection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("disconnected", 2))
    )


_AcSysPEMElectricWireConnection_Type.__name__ = "Integer32"
_AcSysPEMElectricWireConnection_Object = MibTableColumn
acSysPEMElectricWireConnection = _AcSysPEMElectricWireConnection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 24, 1, 5),
    _AcSysPEMElectricWireConnection_Type()
)
acSysPEMElectricWireConnection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPEMElectricWireConnection.setStatus("current")
_AcSysSATModule_ObjectIdentity = ObjectIdentity
acSysSATModule = _AcSysSATModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25)
)
_AcSysSATTable_Object = MibTable
acSysSATTable = _AcSysSATTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21)
)
if mibBuilder.loadTexts:
    acSysSATTable.setStatus("current")
_AcSysSATEntry_Object = MibTableRow
acSysSATEntry = _AcSysSATEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1)
)
acSysSATEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysSATSatIndex"),
)
if mibBuilder.loadTexts:
    acSysSATEntry.setStatus("current")


class _AcSysSATSatIndex_Type(Unsigned32):
    """Custom type acSysSATSatIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSATSatIndex_Type.__name__ = "Unsigned32"
_AcSysSATSatIndex_Object = MibTableColumn
acSysSATSatIndex = _AcSysSATSatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 1),
    _AcSysSATSatIndex_Type()
)
acSysSATSatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysSATSatIndex.setStatus("current")


class _AcSysSATGeographicalPosition_Type(Unsigned32):
    """Custom type acSysSATGeographicalPosition based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_AcSysSATGeographicalPosition_Type.__name__ = "Unsigned32"
_AcSysSATGeographicalPosition_Object = MibTableColumn
acSysSATGeographicalPosition = _AcSysSATGeographicalPosition_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 2),
    _AcSysSATGeographicalPosition_Type()
)
acSysSATGeographicalPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATGeographicalPosition.setStatus("current")


class _AcSysSATType_Type(SnmpAdminString):
    """Custom type acSysSATType based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AcSysSATType_Type.__name__ = "SnmpAdminString"
_AcSysSATType_Object = MibTableColumn
acSysSATType = _AcSysSATType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 3),
    _AcSysSATType_Type()
)
acSysSATType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATType.setStatus("current")


class _AcSysSATInitInformation_Type(Integer32):
    """Custom type acSysSATInitInformation based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("detected", 0),
          ("initComplete", 11),
          ("initFail", 7),
          ("initInProgress", 8),
          ("initIsMissing", 5),
          ("initUpdateREFTable", 9),
          ("initWasReset", 6),
          ("notInitialized", 4),
          ("reConfig", 1),
          ("reConfigTry2", 2),
          ("reConfigTry3", 3),
          ("remoteKeepAlive", 10))
    )


_AcSysSATInitInformation_Type.__name__ = "Integer32"
_AcSysSATInitInformation_Object = MibTableColumn
acSysSATInitInformation = _AcSysSATInitInformation_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 4),
    _AcSysSATInitInformation_Type()
)
acSysSATInitInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATInitInformation.setStatus("current")


class _AcSysSATTimingUnitExistence_Type(Integer32):
    """Custom type acSysSATTimingUnitExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notExist", 2))
    )


_AcSysSATTimingUnitExistence_Type.__name__ = "Integer32"
_AcSysSATTimingUnitExistence_Object = MibTableColumn
acSysSATTimingUnitExistence = _AcSysSATTimingUnitExistence_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 5),
    _AcSysSATTimingUnitExistence_Type()
)
acSysSATTimingUnitExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATTimingUnitExistence.setStatus("current")


class _AcSysSATTimingRefSelection_Type(Integer32):
    """Custom type acSysSATTimingRefSelection based on Integer32"""
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
        *(("bITSNOREF", 0),
          ("bITSNOREF1", 3),
          ("rEFFromBITSA", 1),
          ("rEFFromBITSB", 2),
          ("rEFFromLineClock1", 4),
          ("rEFFromLineClock2", 5),
          ("rEFFromLineClock3", 6),
          ("rEFFromLineClock7", 7))
    )


_AcSysSATTimingRefSelection_Type.__name__ = "Integer32"
_AcSysSATTimingRefSelection_Object = MibTableColumn
acSysSATTimingRefSelection = _AcSysSATTimingRefSelection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 21, 1, 6),
    _AcSysSATTimingRefSelection_Type()
)
acSysSATTimingRefSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATTimingRefSelection.setStatus("current")
_AcSysSATFramersTable_Object = MibTable
acSysSATFramersTable = _AcSysSATFramersTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22)
)
if mibBuilder.loadTexts:
    acSysSATFramersTable.setStatus("current")
_AcSysSATFramersEntry_Object = MibTableRow
acSysSATFramersEntry = _AcSysSATFramersEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1)
)
acSysSATFramersEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysSATFramersSatIndex"),
    (0, "AC-SYSTEM-MIB", "acSysSATFramersFramerIndex"),
)
if mibBuilder.loadTexts:
    acSysSATFramersEntry.setStatus("current")


class _AcSysSATFramersSatIndex_Type(Unsigned32):
    """Custom type acSysSATFramersSatIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSATFramersSatIndex_Type.__name__ = "Unsigned32"
_AcSysSATFramersSatIndex_Object = MibTableColumn
acSysSATFramersSatIndex = _AcSysSATFramersSatIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 1),
    _AcSysSATFramersSatIndex_Type()
)
acSysSATFramersSatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysSATFramersSatIndex.setStatus("current")


class _AcSysSATFramersFramerIndex_Type(Unsigned32):
    """Custom type acSysSATFramersFramerIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcSysSATFramersFramerIndex_Type.__name__ = "Unsigned32"
_AcSysSATFramersFramerIndex_Object = MibTableColumn
acSysSATFramersFramerIndex = _AcSysSATFramersFramerIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 2),
    _AcSysSATFramersFramerIndex_Type()
)
acSysSATFramersFramerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysSATFramersFramerIndex.setStatus("current")


class _AcSysSATFramersFramerInterfaceStatus_Type(Integer32):
    """Custom type acSysSATFramersFramerInterfaceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("framerInitialized", 0),
          ("framerNotInitialized", 1))
    )


_AcSysSATFramersFramerInterfaceStatus_Type.__name__ = "Integer32"
_AcSysSATFramersFramerInterfaceStatus_Object = MibTableColumn
acSysSATFramersFramerInterfaceStatus = _AcSysSATFramersFramerInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 3),
    _AcSysSATFramersFramerInterfaceStatus_Type()
)
acSysSATFramersFramerInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerInterfaceStatus.setStatus("current")


class _AcSysSATFramersFramerLoopBackRef_Type(Integer32):
    """Custom type acSysSATFramersFramerLoopBackRef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("loopdisable", 0),
          ("loopenable", 1))
    )


_AcSysSATFramersFramerLoopBackRef_Type.__name__ = "Integer32"
_AcSysSATFramersFramerLoopBackRef_Object = MibTableColumn
acSysSATFramersFramerLoopBackRef = _AcSysSATFramersFramerLoopBackRef_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 4),
    _AcSysSATFramersFramerLoopBackRef_Type()
)
acSysSATFramersFramerLoopBackRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerLoopBackRef.setStatus("current")


class _AcSysSATFramersFramerInterfaceType_Type(Integer32):
    """Custom type acSysSATFramersFramerInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("e1CAS", 1),
          ("e1CRC4", 0),
          ("e1FAS", 2),
          ("t12", 5),
          ("t1D4", 3),
          ("t1ESF", 4))
    )


_AcSysSATFramersFramerInterfaceType_Type.__name__ = "Integer32"
_AcSysSATFramersFramerInterfaceType_Object = MibTableColumn
acSysSATFramersFramerInterfaceType = _AcSysSATFramersFramerInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 5),
    _AcSysSATFramersFramerInterfaceType_Type()
)
acSysSATFramersFramerInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerInterfaceType.setStatus("current")


class _AcSysSATFramersFramerTransmitControl_Type(Integer32):
    """Custom type acSysSATFramersFramerTransmitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aIS", 1),
          ("disableTransmit", 2),
          ("systemClock", 0))
    )


_AcSysSATFramersFramerTransmitControl_Type.__name__ = "Integer32"
_AcSysSATFramersFramerTransmitControl_Object = MibTableColumn
acSysSATFramersFramerTransmitControl = _AcSysSATFramersFramerTransmitControl_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 6),
    _AcSysSATFramersFramerTransmitControl_Type()
)
acSysSATFramersFramerTransmitControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersFramerTransmitControl.setStatus("current")


class _AcSysSATFramersRxStatus_Type(Integer32):
    """Custom type acSysSATFramersRxStatus based on Integer32"""
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
        *(("aISAlarm", 3),
          ("aISInit", 4),
          ("alarmClear", 0),
          ("lOFAlarm", 1),
          ("lOSAlarm", 2))
    )


_AcSysSATFramersRxStatus_Type.__name__ = "Integer32"
_AcSysSATFramersRxStatus_Object = MibTableColumn
acSysSATFramersRxStatus = _AcSysSATFramersRxStatus_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 7),
    _AcSysSATFramersRxStatus_Type()
)
acSysSATFramersRxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersRxStatus.setStatus("current")


class _AcSysSATFramersIsUsedAsPLLClock_Type(Integer32):
    """Custom type acSysSATFramersIsUsedAsPLLClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1))
    )


_AcSysSATFramersIsUsedAsPLLClock_Type.__name__ = "Integer32"
_AcSysSATFramersIsUsedAsPLLClock_Object = MibTableColumn
acSysSATFramersIsUsedAsPLLClock = _AcSysSATFramersIsUsedAsPLLClock_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 25, 22, 1, 8),
    _AcSysSATFramersIsUsedAsPLLClock_Type()
)
acSysSATFramersIsUsedAsPLLClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysSATFramersIsUsedAsPLLClock.setStatus("current")
_AcSysTimingModule_ObjectIdentity = ObjectIdentity
acSysTimingModule = _AcSysTimingModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26)
)
_AcSysPLLStatusTable_Object = MibTable
acSysPLLStatusTable = _AcSysPLLStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21)
)
if mibBuilder.loadTexts:
    acSysPLLStatusTable.setStatus("current")
_AcSysPLLStatusEntry_Object = MibTableRow
acSysPLLStatusEntry = _AcSysPLLStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21, 1)
)
acSysPLLStatusEntry.setIndexNames(
    (0, "AC-SYSTEM-MIB", "acSysPLLStatusIndex"),
)
if mibBuilder.loadTexts:
    acSysPLLStatusEntry.setStatus("current")


class _AcSysPLLStatusIndex_Type(Unsigned32):
    """Custom type acSysPLLStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_AcSysPLLStatusIndex_Type.__name__ = "Unsigned32"
_AcSysPLLStatusIndex_Object = MibTableColumn
acSysPLLStatusIndex = _AcSysPLLStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21, 1, 1),
    _AcSysPLLStatusIndex_Type()
)
acSysPLLStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acSysPLLStatusIndex.setStatus("current")


class _AcSysPLLStatusOperatingMode_Type(Integer32):
    """Custom type acSysPLLStatusOperatingMode based on Integer32"""
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
        *(("freeRun", 0),
          ("holdOver", 4),
          ("lockToLocal", 3),
          ("lockToRef1", 1),
          ("lockToRef2", 2))
    )


_AcSysPLLStatusOperatingMode_Type.__name__ = "Integer32"
_AcSysPLLStatusOperatingMode_Object = MibTableColumn
acSysPLLStatusOperatingMode = _AcSysPLLStatusOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 9, 10, 10, 4, 26, 21, 1, 2),
    _AcSysPLLStatusOperatingMode_Type()
)
acSysPLLStatusOperatingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acSysPLLStatusOperatingMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-SYSTEM-MIB",
    **{"acSystem": acSystem,
       "acSystemConfiguration": acSystemConfiguration,
       "acSysControl": acSysControl,
       "acSysControlProtocolType": acSysControlProtocolType,
       "acSysControlTrunkingToAnalogFunctionalityProfile": acSysControlTrunkingToAnalogFunctionalityProfile,
       "acSysTDM": acSysTDM,
       "acSysTDMClock": acSysTDMClock,
       "acSysTDMClockSource": acSysTDMClockSource,
       "acSysTDMClockEnableFallBack": acSysTDMClockEnableFallBack,
       "acSysTDMClockLocalReference": acSysTDMClockLocalReference,
       "acSysTDMClockMasterSlaveSelection": acSysTDMClockMasterSlaveSelection,
       "acSysTDMClockNetRefSpeed": acSysTDMClockNetRefSpeed,
       "acSysTDMClockAutoFallBackEnable": acSysTDMClockAutoFallBackEnable,
       "acSysTDMClockAutoFallBackRevertingEnable": acSysTDMClockAutoFallBackRevertingEnable,
       "acSysTDMClockBitsReference": acSysTDMClockBitsReference,
       "acSysTDMClockPLLOutOfRange": acSysTDMClockPLLOutOfRange,
       "acSysTDMClockFallbackClock": acSysTDMClockFallbackClock,
       "acSysTDMBus": acSysTDMBus,
       "acSysTDMBusType": acSysTDMBusType,
       "acSysTDMBusSpeed": acSysTDMBusSpeed,
       "acSysTDMBusOutputPort": acSysTDMBusOutputPort,
       "acSysTDMBusOutputStartingChannel": acSysTDMBusOutputStartingChannel,
       "acSysPCM": acSysPCM,
       "acSysPCMLawSelect": acSysPCMLawSelect,
       "acSysPCMIdlePattern": acSysPCMIdlePattern,
       "acSysPCMIdleABCDPattern": acSysPCMIdleABCDPattern,
       "acSysPCMSerialPortAuditIntervalMin": acSysPCMSerialPortAuditIntervalMin,
       "acSysNetworkConfig": acSysNetworkConfig,
       "acSysIP": acSysIP,
       "acSysIPAddress": acSysIPAddress,
       "acSysIPSubNetAddress": acSysIPSubNetAddress,
       "acSysIPDefaultGatewayAddress": acSysIPDefaultGatewayAddress,
       "acSysIPDHCPEnable": acSysIPDHCPEnable,
       "acSysIPDHCPSpeedFactor": acSysIPDHCPSpeedFactor,
       "acSysIPDnsPrimaryServerType": acSysIPDnsPrimaryServerType,
       "acSysIPDnsPrimaryServer": acSysIPDnsPrimaryServer,
       "acSysIPDnsSecondaryServerType": acSysIPDnsSecondaryServerType,
       "acSysIPDnsSecondaryServer": acSysIPDnsSecondaryServer,
       "acSysIPDHCPLeaseRenewalEnable": acSysIPDHCPLeaseRenewalEnable,
       "acMultipleIP": acMultipleIP,
       "acMultipleIPEnable": acMultipleIPEnable,
       "acMultipleIPEnableTPNCPasOAM": acMultipleIPEnableTPNCPasOAM,
       "acMultipleIPEnableDNSasOAM": acMultipleIPEnableDNSasOAM,
       "acMultipleIPEnableNTPasOAM": acMultipleIPEnableNTPasOAM,
       "acMultipleIPEnableSCTPasControl": acMultipleIPEnableSCTPasControl,
       "acMultipleIPEnableNetwotkSeparation": acMultipleIPEnableNetwotkSeparation,
       "acMultipleIPInterfaceTableAction": acMultipleIPInterfaceTableAction,
       "acNetworkIPTable": acNetworkIPTable,
       "acNetworkIPEntry": acNetworkIPEntry,
       "acNetworkIPIndex": acNetworkIPIndex,
       "acNetworkIPIfIndex": acNetworkIPIfIndex,
       "acNetworkIPLocalIPAddress": acNetworkIPLocalIPAddress,
       "acNetworkIPLocalSubnetMask": acNetworkIPLocalSubnetMask,
       "acNetworkIPLocalDefGW": acNetworkIPLocalDefGW,
       "acNetworkIPAdminState": acNetworkIPAdminState,
       "acSysInterfaceTable": acSysInterfaceTable,
       "acSysInterfaceEntry": acSysInterfaceEntry,
       "acSysInterfaceIndex": acSysInterfaceIndex,
       "acSysInterfaceRowStatus": acSysInterfaceRowStatus,
       "acSysInterfaceAction": acSysInterfaceAction,
       "acSysInterfaceActionRes": acSysInterfaceActionRes,
       "acSysInterfaceApplicationTypes": acSysInterfaceApplicationTypes,
       "acSysInterfaceMode": acSysInterfaceMode,
       "acSysInterfaceIPAddress": acSysInterfaceIPAddress,
       "acSysInterfacePrefixLength": acSysInterfacePrefixLength,
       "acSysInterfaceGateway": acSysInterfaceGateway,
       "acSysInterfaceVlanID": acSysInterfaceVlanID,
       "acSysInterfaceName": acSysInterfaceName,
       "acSyslog": acSyslog,
       "acSyslogServerIPAddress": acSyslogServerIPAddress,
       "acSyslogEnable": acSyslogEnable,
       "acSyslogAcSyslogServerPortNumber": acSyslogAcSyslogServerPortNumber,
       "acSysNTP": acSysNTP,
       "acSysNTPServerIPAddress": acSysNTPServerIPAddress,
       "acSysNTPUtcOffset": acSysNTPUtcOffset,
       "acSysNTPUpdateInterval": acSysNTPUpdateInterval,
       "acSysDayLightSavingTime": acSysDayLightSavingTime,
       "acSysDayLightSavingTimeMode": acSysDayLightSavingTimeMode,
       "acSysDayLightSavingTimeOffset": acSysDayLightSavingTimeOffset,
       "acSysDayLightSavingTimeStart": acSysDayLightSavingTimeStart,
       "acSysDayLightSavingTimeEnd": acSysDayLightSavingTimeEnd,
       "acSysWEB": acSysWEB,
       "acSysWEBConfigDisable": acSysWEBConfigDisable,
       "acSysWEBHTTPSOnly": acSysWEBHTTPSOnly,
       "acSysWEBHTTPSPort": acSysWEBHTTPSPort,
       "acSysWEBWebUseRadiusLogin": acSysWEBWebUseRadiusLogin,
       "acSysWEBHTTPSCipherString": acSysWEBHTTPSCipherString,
       "acSysWEBDenyAuthenticationTimer": acSysWEBDenyAuthenticationTimer,
       "acSysWEBWanHttpPort": acSysWEBWanHttpPort,
       "acSysWEBWanHttpsPort": acSysWEBWanHttpsPort,
       "acSysWEBACLTable": acSysWEBACLTable,
       "acSysWEBACLEntry": acSysWEBACLEntry,
       "acSysWEBACLIndex": acSysWEBACLIndex,
       "acSysWEBACLIP": acSysWEBACLIP,
       "acSysWEBAccess": acSysWEBAccess,
       "acSysWEBAccessTable": acSysWEBAccessTable,
       "acSysWEBAccessEntry": acSysWEBAccessEntry,
       "acSysWEBAccessRowStatus": acSysWEBAccessRowStatus,
       "acSysWEBAccessAction": acSysWEBAccessAction,
       "acSysWEBAccessActionResult": acSysWEBAccessActionResult,
       "acSysWEBAccessIndex": acSysWEBAccessIndex,
       "acSysWEBAccessUserName": acSysWEBAccessUserName,
       "acSysWEBAccessUserCode": acSysWEBAccessUserCode,
       "acSysWEBAccessWebAuthMode": acSysWEBAccessWebAuthMode,
       "acSysNATTraversal": acSysNATTraversal,
       "acSysSTUN": acSysSTUN,
       "acSysSTUNEnable": acSysSTUNEnable,
       "acSysSTUNPrimaryServerIP": acSysSTUNPrimaryServerIP,
       "acSysSTUNSecondaryServerIP": acSysSTUNSecondaryServerIP,
       "acSysSTUNBindingLifeTime": acSysSTUNBindingLifeTime,
       "acSysTelnet": acSysTelnet,
       "acSysTelnetServerEnable": acSysTelnetServerEnable,
       "acSysTelnetServerPort": acSysTelnetServerPort,
       "acSysTelnetServerIdleDisconnect": acSysTelnetServerIdleDisconnect,
       "acSysTelnetSSHServerPort": acSysTelnetSSHServerPort,
       "acSysTelnetSSHServerEnable": acSysTelnetSSHServerEnable,
       "acSysTelnetSSHAdminKey": acSysTelnetSSHAdminKey,
       "acSysTelnetSSHRequirePublicKey": acSysTelnetSSHRequirePublicKey,
       "acSysTelnetServerWanPort": acSysTelnetServerWanPort,
       "acSysTelnetWanSSHServerPort": acSysTelnetWanSSHServerPort,
       "acSysHTTPClient": acSysHTTPClient,
       "acSysHTTPClientAutoUpdatePredefinedTime": acSysHTTPClientAutoUpdatePredefinedTime,
       "acSysHTTPClientAutoUpdateFrequency": acSysHTTPClientAutoUpdateFrequency,
       "acSysHTTPClientAutoUpdateCmpFile": acSysHTTPClientAutoUpdateCmpFile,
       "acSysHTTPClientCmpFileURL": acSysHTTPClientCmpFileURL,
       "acSysHTTPClientIniFileURL": acSysHTTPClientIniFileURL,
       "acSysHTTPClientIniFileTemplateURL": acSysHTTPClientIniFileTemplateURL,
       "acSysHTTPClientCPTFileURL": acSysHTTPClientCPTFileURL,
       "acSysHTTPClientVPFileURL": acSysHTTPClientVPFileURL,
       "acSysHTTPClientPRTFileURL": acSysHTTPClientPRTFileURL,
       "acSysHTTPClientFXSCoeffFileURL": acSysHTTPClientFXSCoeffFileURL,
       "acSysHTTPClientFXOCoeffFileURL": acSysHTTPClientFXOCoeffFileURL,
       "acSysHTTPClientCASFileURL": acSysHTTPClientCASFileURL,
       "acSysHTTPClientXMLFileUrl": acSysHTTPClientXMLFileUrl,
       "acSysHTTPClientCoderTableFileUrl": acSysHTTPClientCoderTableFileUrl,
       "acSysHTTPClientUserInfoFileURL": acSysHTTPClientUserInfoFileURL,
       "acSysHTTPClientDialPlanFileURL": acSysHTTPClientDialPlanFileURL,
       "acSysHTTPClientTLSPkeyFileUrl": acSysHTTPClientTLSPkeyFileUrl,
       "acSysHTTPClientTLSCertFileUrl": acSysHTTPClientTLSCertFileUrl,
       "acSysHTTPClientTLSRootFileUrl": acSysHTTPClientTLSRootFileUrl,
       "acSysHTTPClientWebLogoFileUrl": acSysHTTPClientWebLogoFileUrl,
       "acSysHTTPClientVideoFontFileURL": acSysHTTPClientVideoFontFileURL,
       "acSysHTTPClientV5PortConfFileURL": acSysHTTPClientV5PortConfFileURL,
       "acSysHTTPClientDataConfigurationFileUrl": acSysHTTPClientDataConfigurationFileUrl,
       "acSysSNMP": acSysSNMP,
       "acSysSNMPKeepAliveTrapPort": acSysSNMPKeepAliveTrapPort,
       "acSysSNMPEmsColdStrartIndication": acSysSNMPEmsColdStrartIndication,
       "acSysSNMPWanPort": acSysSNMPWanPort,
       "acSysVLAN": acSysVLAN,
       "acSysVLANOamVlanId": acSysVLANOamVlanId,
       "acSysVLANControlVlanId": acSysVLANControlVlanId,
       "acSysVLANMediaVlanId": acSysVLANMediaVlanId,
       "acSysVLANNetworkServiceClassPriority": acSysVLANNetworkServiceClassPriority,
       "acSysVLANPremiumServiceClassMediaPriority": acSysVLANPremiumServiceClassMediaPriority,
       "acSysVLANGoldServiceClassPriority": acSysVLANGoldServiceClassPriority,
       "acSysVLANBronzeServiceClassPriority": acSysVLANBronzeServiceClassPriority,
       "acSysVLANPremiumServiceClassControlPriority": acSysVLANPremiumServiceClassControlPriority,
       "acSysVLANNetworkServiceClassDiffServ": acSysVLANNetworkServiceClassDiffServ,
       "acSysVLANPremiumServiceClassMediaDiffServ": acSysVLANPremiumServiceClassMediaDiffServ,
       "acSysVLANPremiumServiceClassControlDiffServ": acSysVLANPremiumServiceClassControlDiffServ,
       "acSysVLANGoldServiceClassDiffServ": acSysVLANGoldServiceClassDiffServ,
       "acSysVLANBronzeServiceClassDiffServ": acSysVLANBronzeServiceClassDiffServ,
       "acSysVLANVlanNativeVlanId": acSysVLANVlanNativeVlanId,
       "acSysVLANMode": acSysVLANMode,
       "acSysVlanMapTable": acSysVlanMapTable,
       "acSysVlanMapEntry": acSysVlanMapEntry,
       "acSysVlanMapIndex": acSysVlanMapIndex,
       "acSysVlanMapRowStatus": acSysVlanMapRowStatus,
       "acSysVlanMapAction": acSysVlanMapAction,
       "acSysVlanMapActionRes": acSysVlanMapActionRes,
       "acSysVlanMapDiffServ": acSysVlanMapDiffServ,
       "acSysVlanMapVlanPriority": acSysVlanMapVlanPriority,
       "acSysSCTP": acSysSCTP,
       "acSysSCTPHeartBeatInterval": acSysSCTPHeartBeatInterval,
       "acSysSCTPT4SACKTimer": acSysSCTPT4SACKTimer,
       "acSysSCTPCheckSumMethod": acSysSCTPCheckSumMethod,
       "acSysSCTPHostName": acSysSCTPHostName,
       "acSysSCTPAssociationsNum": acSysSCTPAssociationsNum,
       "acSysEthernetPort": acSysEthernetPort,
       "acSysEthernetPortPhyConfiguration": acSysEthernetPortPhyConfiguration,
       "acSysMiscConfig": acSysMiscConfig,
       "acSysDiagnostics": acSysDiagnostics,
       "acSysDiagnosticsEnable": acSysDiagnosticsEnable,
       "acSysDiagnosticsEnablePerformanceThresholdAlarms": acSysDiagnosticsEnablePerformanceThresholdAlarms,
       "acSysDiagnosticsListOfActivitiesToLog": acSysDiagnosticsListOfActivitiesToLog,
       "acSysGenericINI": acSysGenericINI,
       "acSysGenericINILine": acSysGenericINILine,
       "acSysGenericINISecureStartup": acSysGenericINISecureStartup,
       "acSysLicenseKey": acSysLicenseKey,
       "acSysLicenseKeyString": acSysLicenseKeyString,
       "acSysLicenseKeyActiveList": acSysLicenseKeyActiveList,
       "acSysFile": acSysFile,
       "acSysFileCpt": acSysFileCpt,
       "acSysFileVp": acSysFileVp,
       "acSysFilePrerecordedTones": acSysFilePrerecordedTones,
       "acSysFileXml": acSysFileXml,
       "acSysFileExternalCoder": acSysFileExternalCoder,
       "acSysFileUserInfo": acSysFileUserInfo,
       "acSysFileDialPlanFileName": acSysFileDialPlanFileName,
       "acSysFileTLSPkeyFileName": acSysFileTLSPkeyFileName,
       "acSysFileTLSCertFileName": acSysFileTLSCertFileName,
       "acSysFileTLSRootFileName": acSysFileTLSRootFileName,
       "acSysFileFirstVideoFontFileName": acSysFileFirstVideoFontFileName,
       "acSysFileSecondVideoFontFileName": acSysFileSecondVideoFontFileName,
       "acSysFileThirdVideoFontFileName": acSysFileThirdVideoFontFileName,
       "acSysFileV5PortConfFileName": acSysFileV5PortConfFileName,
       "acSysSecurity": acSysSecurity,
       "acSysSecurityTLSVersion": acSysSecurityTLSVersion,
       "acSysSecurityOcspEnable": acSysSecurityOcspEnable,
       "acSysSecurityOcspServerIPType": acSysSecurityOcspServerIPType,
       "acSysSecurityOcspServerIP": acSysSecurityOcspServerIP,
       "acSysSecurityOcspServerPort": acSysSecurityOcspServerPort,
       "acSysSecurityOcspDefaultResponse": acSysSecurityOcspDefaultResponse,
       "acSysSecurityTLSFIPS140Mode": acSysSecurityTLSFIPS140Mode,
       "acSysSecurityGenCsrSubjectName": acSysSecurityGenCsrSubjectName,
       "acSysSecuritySelfSignedCertificateSubjectName": acSysSecuritySelfSignedCertificateSubjectName,
       "acSysSecurityOcspSecondaryServerIPType": acSysSecurityOcspSecondaryServerIPType,
       "acSysSecurityOcspSecondaryServerIP": acSysSecurityOcspSecondaryServerIP,
       "acSysSecurityHTTPSRequireClientCertificate": acSysSecurityHTTPSRequireClientCertificate,
       "acSysSecurityAUPDVerifyCertificates": acSysSecurityAUPDVerifyCertificates,
       "acSysIKE": acSysIKE,
       "acSysIKEPolicyTable": acSysIKEPolicyTable,
       "acSysIKEPolicyEntry": acSysIKEPolicyEntry,
       "acSysIKEPolicyIndex": acSysIKEPolicyIndex,
       "acSysIKEPolicyRowStatus": acSysIKEPolicyRowStatus,
       "acSysIKEPolicyAction": acSysIKEPolicyAction,
       "acSysIKEPolicyActionRes": acSysIKEPolicyActionRes,
       "acSysIKEPolicyShardKey": acSysIKEPolicyShardKey,
       "acSysIKEPolicyLifeInSeconds": acSysIKEPolicyLifeInSeconds,
       "acSysIKEPolicyLifeInKB": acSysIKEPolicyLifeInKB,
       "acSysIKEPolicyProposal0Encryption": acSysIKEPolicyProposal0Encryption,
       "acSysIKEPolicyProposal1Encryption": acSysIKEPolicyProposal1Encryption,
       "acSysIKEPolicyProposal2Encryption": acSysIKEPolicyProposal2Encryption,
       "acSysIKEPolicyProposal3Encryption": acSysIKEPolicyProposal3Encryption,
       "acSysIKEPolicyProposal0Authentication": acSysIKEPolicyProposal0Authentication,
       "acSysIKEPolicyProposal1Authentication": acSysIKEPolicyProposal1Authentication,
       "acSysIKEPolicyProposal2Authentication": acSysIKEPolicyProposal2Authentication,
       "acSysIKEPolicyProposal3Authentication": acSysIKEPolicyProposal3Authentication,
       "acSysIKEPolicyProposal0DHGroup": acSysIKEPolicyProposal0DHGroup,
       "acSysIKEPolicyProposal1DHGroup": acSysIKEPolicyProposal1DHGroup,
       "acSysIKEPolicyProposal2DHGroup": acSysIKEPolicyProposal2DHGroup,
       "acSysIKEPolicyProposal3DHGroup": acSysIKEPolicyProposal3DHGroup,
       "acSysIKEPolicyAuthenticationMethod": acSysIKEPolicyAuthenticationMethod,
       "acSysIPSec": acSysIPSec,
       "acSysIPSecEnable": acSysIPSecEnable,
       "acSysIPSecDpdMode": acSysIPSecDpdMode,
       "acSysIPSecIKECertificateExtValidate": acSysIPSecIKECertificateExtValidate,
       "acSysIPSecSPDTable": acSysIPSecSPDTable,
       "acSysIPSecSPDEntry": acSysIPSecSPDEntry,
       "acSysIPSecSPDIndex": acSysIPSecSPDIndex,
       "acSysIPSecSPDRowStatus": acSysIPSecSPDRowStatus,
       "acSysIPSecSPDAction": acSysIPSecSPDAction,
       "acSysIPSecSPDActionRes": acSysIPSecSPDActionRes,
       "acSysIPSecSPDPolicyRemoteIPAddr": acSysIPSecSPDPolicyRemoteIPAddr,
       "acSysIPSecSPDPolicySrcPort": acSysIPSecSPDPolicySrcPort,
       "acSysIPSecSPDPolicyDestPort": acSysIPSecSPDPolicyDestPort,
       "acSysIPSecSPDPolicyProtocol": acSysIPSecSPDPolicyProtocol,
       "acSysIPSecSPDKeyExchangeMethodIndex": acSysIPSecSPDKeyExchangeMethodIndex,
       "acSysIPSecSPDLifeInSeconds": acSysIPSecSPDLifeInSeconds,
       "acSysIPSecSPDLifeInKB": acSysIPSecSPDLifeInKB,
       "acSysIPSecSPDProposal0Encryption": acSysIPSecSPDProposal0Encryption,
       "acSysIPSecSPDProposal1Encryption": acSysIPSecSPDProposal1Encryption,
       "acSysIPSecSPDProposal2Encryption": acSysIPSecSPDProposal2Encryption,
       "acSysIPSecSPDProposal3Encryption": acSysIPSecSPDProposal3Encryption,
       "acSysIPSecSPDProposal0Authentication": acSysIPSecSPDProposal0Authentication,
       "acSysIPSecSPDProposal1Authentication": acSysIPSecSPDProposal1Authentication,
       "acSysIPSecSPDProposal2Authentication": acSysIPSecSPDProposal2Authentication,
       "acSysIPSecSPDProposal3Authentication": acSysIPSecSPDProposal3Authentication,
       "acSysIPSecSPDPolicyLocalIPAddrType": acSysIPSecSPDPolicyLocalIPAddrType,
       "acSysIPSecSPDMode": acSysIPSecSPDMode,
       "acSysIPSecSPDPolicyRemoteTunnelIPAddress": acSysIPSecSPDPolicyRemoteTunnelIPAddress,
       "acSysIPSecSPDPolicyLocalTunnelIPAddress": acSysIPSecSPDPolicyLocalTunnelIPAddress,
       "acSysIPSecSPDPolicyRemoteTunnelSubnetMask": acSysIPSecSPDPolicyRemoteTunnelSubnetMask,
       "acSysIPsecProposalTable": acSysIPsecProposalTable,
       "acSysIPsecProposalEntry": acSysIPsecProposalEntry,
       "acSysIPsecProposalIndex": acSysIPsecProposalIndex,
       "acSysIPsecProposalRowStatus": acSysIPsecProposalRowStatus,
       "acSysIPsecProposalAction": acSysIPsecProposalAction,
       "acSysIPsecProposalActionRes": acSysIPsecProposalActionRes,
       "acSysIPsecProposalEncryptionAlgorithm": acSysIPsecProposalEncryptionAlgorithm,
       "acSysIPsecProposalAuthenticationAlgorithm": acSysIPsecProposalAuthenticationAlgorithm,
       "acSysIPsecProposalDiffieHellmanGroup": acSysIPsecProposalDiffieHellmanGroup,
       "acSysIPsecSATable": acSysIPsecSATable,
       "acSysIPsecSAEntry": acSysIPsecSAEntry,
       "acSysIPsecSAIndex": acSysIPsecSAIndex,
       "acSysIPsecSARowStatus": acSysIPsecSARowStatus,
       "acSysIPsecSAAction": acSysIPsecSAAction,
       "acSysIPsecSAActionRes": acSysIPsecSAActionRes,
       "acSysIPsecSARemoteEndpointAddress": acSysIPsecSARemoteEndpointAddress,
       "acSysIPsecSAAuthenticationMethod": acSysIPsecSAAuthenticationMethod,
       "acSysIPsecSASharedKey": acSysIPsecSASharedKey,
       "acSysIPsecSASourcePort": acSysIPsecSASourcePort,
       "acSysIPsecSADestPort": acSysIPsecSADestPort,
       "acSysIPsecSAProtocol": acSysIPsecSAProtocol,
       "acSysIPsecSAPhase1SaLifetimeInSec": acSysIPsecSAPhase1SaLifetimeInSec,
       "acSysIPsecSAPhase2SaLifetimeInSec": acSysIPsecSAPhase2SaLifetimeInSec,
       "acSysIPsecSAPhase2SaLifetimeInKB": acSysIPsecSAPhase2SaLifetimeInKB,
       "acSysIPsecSADPDmode": acSysIPsecSADPDmode,
       "acSysIPsecSAIPsecMode": acSysIPsecSAIPsecMode,
       "acSysIPsecSARemoteTunnelAddress": acSysIPsecSARemoteTunnelAddress,
       "acSysIPsecSARemoteSubnetIPAddress": acSysIPsecSARemoteSubnetIPAddress,
       "acSysIPsecSARemoteSubnetPrefixLength": acSysIPsecSARemoteSubnetPrefixLength,
       "acFirewall": acFirewall,
       "acSysAccessListTable": acSysAccessListTable,
       "acSysAccessListEntry": acSysAccessListEntry,
       "acSysAccessListIndex": acSysAccessListIndex,
       "acSysAccessListRowStatus": acSysAccessListRowStatus,
       "acSysAccessListAction": acSysAccessListAction,
       "acSysAccessListActionRes": acSysAccessListActionRes,
       "acSysAccessListSourceIP": acSysAccessListSourceIP,
       "acSysAccessListNetMask": acSysAccessListNetMask,
       "acSysAccessListStartPort": acSysAccessListStartPort,
       "acSysAccessListEndPort": acSysAccessListEndPort,
       "acSysAccessListProtocol": acSysAccessListProtocol,
       "acSysAccessListPacketSize": acSysAccessListPacketSize,
       "acSysAccessListByteRate": acSysAccessListByteRate,
       "acSysAccessListByteBurst": acSysAccessListByteBurst,
       "acSysAccessListAllowType": acSysAccessListAllowType,
       "acSysAccessListMatchCount": acSysAccessListMatchCount,
       "acSysMediaEncription": acSysMediaEncription,
       "acSysMediaEncriptionRTPAuthenticationDisableTx": acSysMediaEncriptionRTPAuthenticationDisableTx,
       "acSysMediaEncriptionRTPAuthenticationDisableRx": acSysMediaEncriptionRTPAuthenticationDisableRx,
       "acSysMediaEncriptionRTPEncryptionDisableTx": acSysMediaEncriptionRTPEncryptionDisableTx,
       "acSysMediaEncriptionRTPEncryptionDisableRx": acSysMediaEncriptionRTPEncryptionDisableRx,
       "acSysMediaEncriptionRTCPEncryptionDisableTx": acSysMediaEncriptionRTCPEncryptionDisableTx,
       "acSysMediaEncriptionRTCPEncryptionDisableRx": acSysMediaEncriptionRTCPEncryptionDisableRx,
       "acSysSRTP": acSysSRTP,
       "acSysSRTPPacketMKISize": acSysSRTPPacketMKISize,
       "acSys802dot1x": acSys802dot1x,
       "acSys802dot1xMode": acSys802dot1xMode,
       "acSys802dot1xUsername": acSys802dot1xUsername,
       "acSys802dot1xPassword": acSys802dot1xPassword,
       "acSys802dot1xVerifyPeerCertificate": acSys802dot1xVerifyPeerCertificate,
       "acSysSerialIF": acSysSerialIF,
       "acSysSerialIFBaudRate": acSysSerialIFBaudRate,
       "acSysSerialIFData": acSysSerialIFData,
       "acSysSerialIFParity": acSysSerialIFParity,
       "acSysSerialIFStop": acSysSerialIFStop,
       "acSysSerialIFFlowControl": acSysSerialIFFlowControl,
       "acVoiceStream": acVoiceStream,
       "acVoiceStreamStatus": acVoiceStreamStatus,
       "acVoiceStreamUploadMethod": acVoiceStreamUploadMethod,
       "acVoiceStreamUploadPostUri": acVoiceStreamUploadPostUri,
       "acSysAMS": acSysAMS,
       "acSysAMSProfile": acSysAMSProfile,
       "acSysAMSApsIpAddress": acSysAMSApsIpAddress,
       "acSysAMSApsPort": acSysAMSApsPort,
       "acSysAMSPrimaryLanguage": acSysAMSPrimaryLanguage,
       "acSysAMSSecondaryLanguage": acSysAMSSecondaryLanguage,
       "acSysAMSAPSProfile": acSysAMSAPSProfile,
       "acSysAMSForceRepositoryEnable": acSysAMSForceRepositoryEnable,
       "acSysNetworkFileSystem": acSysNetworkFileSystem,
       "acSysNFSTable": acSysNFSTable,
       "acSysNFSEntry": acSysNFSEntry,
       "acSysNFSIndex": acSysNFSIndex,
       "acSysNFSRowStatus": acSysNFSRowStatus,
       "acSysNFSAction": acSysNFSAction,
       "acSysNFSActionRes": acSysNFSActionRes,
       "acSysNFSHostOrIP": acSysNFSHostOrIP,
       "acSysNFSRootPath": acSysNFSRootPath,
       "acSysNFSNfsVersion": acSysNFSNfsVersion,
       "acSysNFSAuthType": acSysNFSAuthType,
       "acSysNFSUID": acSysNFSUID,
       "acSysNFSGID": acSysNFSGID,
       "acSysNFSVlanType": acSysNFSVlanType,
       "acSysHA": acSysHA,
       "acSysHAGlobalIPAddress": acSysHAGlobalIPAddress,
       "acSysTransmission": acSysTransmission,
       "acSysTransmissionType": acSysTransmissionType,
       "acSysTiming": acSysTiming,
       "acSysTimingMode": acSysTimingMode,
       "acSysTimingValidationTime": acSysTimingValidationTime,
       "acSysTimingClockToDeriveA": acSysTimingClockToDeriveA,
       "acSysTimingClockToDeriveB": acSysTimingClockToDeriveB,
       "acSysTimingExternalIFType": acSysTimingExternalIFType,
       "acSysTimingLoopBackRef1": acSysTimingLoopBackRef1,
       "acSysTimingLoopBackRef2": acSysTimingLoopBackRef2,
       "acSysTimingTransmitControl": acSysTimingTransmitControl,
       "acSysTimingE1LineBuildOut": acSysTimingE1LineBuildOut,
       "acSysTimingT1LineBuildOut": acSysTimingT1LineBuildOut,
       "acSysLDAP": acSysLDAP,
       "acSysLDAPServerIp": acSysLDAPServerIp,
       "acSysLDAPServerPort": acSysLDAPServerPort,
       "acSysLDAPServerMaxRespondTime": acSysLDAPServerMaxRespondTime,
       "acSysLDAPServerDomainName": acSysLDAPServerDomainName,
       "acSysLDAPSearchDN": acSysLDAPSearchDN,
       "acSysLDAPPassword": acSysLDAPPassword,
       "acSysLDAPBindDN": acSysLDAPBindDN,
       "acSysLDAPServiceEnable": acSysLDAPServiceEnable,
       "acSystemStatus": acSystemStatus,
       "acSysType": acSysType,
       "acSysTypeProduct": acSysTypeProduct,
       "acSysTypeDSP": acSysTypeDSP,
       "acSysTypeModule": acSysTypeModule,
       "acSysTypeCPUSpeed": acSysTypeCPUSpeed,
       "acSysVersion": acSysVersion,
       "acSysVersionSoftware": acSysVersionSoftware,
       "acSysVersionFlash": acSysVersionFlash,
       "acSysVersionIniFile": acSysVersionIniFile,
       "acSysVersionSoftwareDate": acSysVersionSoftwareDate,
       "acSysId": acSysId,
       "acSysIdName": acSysIdName,
       "acSysIdSerialNumber": acSysIdSerialNumber,
       "acSysIdSlotNumber": acSysIdSlotNumber,
       "acSysIdFirstSerialNumber": acSysIdFirstSerialNumber,
       "acSysCount": acSysCount,
       "acSysCountDSPs": acSysCountDSPs,
       "acSysCountChannels": acSysCountChannels,
       "acSysCountTrunks": acSysCountTrunks,
       "acSysState": acSysState,
       "acSysStateTemperature": acSysStateTemperature,
       "acSysStateOperational": acSysStateOperational,
       "acSysStateHAupdateInProgress": acSysStateHAupdateInProgress,
       "acSysStateGWSeverity": acSysStateGWSeverity,
       "acSysStateIsPstnManagementEnable": acSysStateIsPstnManagementEnable,
       "acSysNetwork": acSysNetwork,
       "acSysEthernet": acSysEthernet,
       "acSysEthernetFirstPortDuplexMode": acSysEthernetFirstPortDuplexMode,
       "acSysEthernetFirstPortSpeed": acSysEthernetFirstPortSpeed,
       "acSysEthernetSecondPortDuplexMode": acSysEthernetSecondPortDuplexMode,
       "acSysEthernetSecondPortSpeed": acSysEthernetSecondPortSpeed,
       "acSysEthernetActivePortNumber": acSysEthernetActivePortNumber,
       "acSysEthernetStatusTable": acSysEthernetStatusTable,
       "acSysEthernetStatusEntry": acSysEthernetStatusEntry,
       "acSysEthernetStatusIndex": acSysEthernetStatusIndex,
       "acSysEthernetStatusPortDuplexMode": acSysEthernetStatusPortDuplexMode,
       "acSysEthernetStatusPortSpeed": acSysEthernetStatusPortSpeed,
       "acSysEthernetStatusActivePortNumber": acSysEthernetStatusActivePortNumber,
       "acSysEthernetStatusPortState": acSysEthernetStatusPortState,
       "acSysEthernetStatusPowerOverEthernet": acSysEthernetStatusPowerOverEthernet,
       "acSysNAT": acSysNAT,
       "acSysNATType": acSysNATType,
       "acSysWebStat": acSysWebStat,
       "acSysWebStatPasswordControlViaSNMP": acSysWebStatPasswordControlViaSNMP,
       "acSysIPStatus": acSysIPStatus,
       "acSysInterfaceStatusTable": acSysInterfaceStatusTable,
       "acSysInterfaceStatusEntry": acSysInterfaceStatusEntry,
       "acSysInterfaceStatusEntryIndex": acSysInterfaceStatusEntryIndex,
       "acSysInterfaceStatusTypeIndex": acSysInterfaceStatusTypeIndex,
       "acSysInterfaceStatusApplicationTypes": acSysInterfaceStatusApplicationTypes,
       "acSysInterfaceStatusMode": acSysInterfaceStatusMode,
       "acSysInterfaceStatusIPAddress": acSysInterfaceStatusIPAddress,
       "acSysInterfaceStatusPrefixLength": acSysInterfaceStatusPrefixLength,
       "acSysInterfaceStatusGateway": acSysInterfaceStatusGateway,
       "acSysInterfaceStatusVlanID": acSysInterfaceStatusVlanID,
       "acSysInterfaceStatusName": acSysInterfaceStatusName,
       "acSysTime": acSysTime,
       "acSysTimeUp": acSysTimeUp,
       "acSysVoicePrompt": acSysVoicePrompt,
       "acSysVoicePromptTotalMemorySize": acSysVoicePromptTotalMemorySize,
       "acSysVoicePromptMaxFreeMemorySize": acSysVoicePromptMaxFreeMemorySize,
       "acSysRepositoryAMS": acSysRepositoryAMS,
       "acSysRepositoryAMSIsReadyForUpdate": acSysRepositoryAMSIsReadyForUpdate,
       "acSysHAStatus": acSysHAStatus,
       "acSysHAStatusReady": acSysHAStatusReady,
       "acSysLDAPStatus": acSysLDAPStatus,
       "acSysLDAPStatusServerMode": acSysLDAPStatusServerMode,
       "acSystemAction": acSystemAction,
       "acSysAction": acSysAction,
       "acSysActionSet": acSysActionSet,
       "acSysActionSetReset": acSysActionSetReset,
       "acSysActionSetResetControl": acSysActionSetResetControl,
       "acSysActionSetDefaults": acSysActionSetDefaults,
       "acSysActionSetSaveConfig": acSysActionSetSaveConfig,
       "acSysActionSetAutoUpdate": acSysActionSetAutoUpdate,
       "acSysActionSetGetTimeFromNTPServer": acSysActionSetGetTimeFromNTPServer,
       "acSysActionSetSwUpgrade": acSysActionSetSwUpgrade,
       "acSysActionSetOnLineChangesApply": acSysActionSetOnLineChangesApply,
       "acSysActionSetIPSecTLSUpgrade": acSysActionSetIPSecTLSUpgrade,
       "acSysActionSetGWAppTLSUpgrade": acSysActionSetGWAppTLSUpgrade,
       "acSysActionSetConvertNetworkIFsConfiguration": acSysActionSetConvertNetworkIFsConfiguration,
       "acSysActionSetActionId": acSysActionSetActionId,
       "acSysActionSetAutoUpdateActionResult": acSysActionSetAutoUpdateActionResult,
       "acSysActionAdmin": acSysActionAdmin,
       "acSysActionAdminState": acSysActionAdminState,
       "acSysActionAdminStateLockTimeout": acSysActionAdminStateLockTimeout,
       "acSysUpload": acSysUpload,
       "acSysUploadActionType": acSysUploadActionType,
       "acSysUploadFileType": acSysUploadFileType,
       "acSysUploadFileNumber": acSysUploadFileNumber,
       "acSysUploadFileURI": acSysUploadFileURI,
       "acSysUploadActionID": acSysUploadActionID,
       "acSysUploadActionResult": acSysUploadActionResult,
       "acSystemChassis": acSystemChassis,
       "acSystemChassisDryContactsOutStatus": acSystemChassisDryContactsOutStatus,
       "acSystemChassisDryContactsInStatus": acSystemChassisDryContactsInStatus,
       "acSystemChassisLastChanged": acSystemChassisLastChanged,
       "acSysModuleTable": acSysModuleTable,
       "acSysModuleEntry": acSysModuleEntry,
       "acSysModuleIndex": acSysModuleIndex,
       "acSysModuleGeographicalPosition": acSysModuleGeographicalPosition,
       "acSysModuleType": acSysModuleType,
       "acSysModulePresence": acSysModulePresence,
       "acSysModuleLicenseKeyList": acSysModuleLicenseKeyList,
       "acSysModuleSerialNumber": acSysModuleSerialNumber,
       "acSysModuleSWVersion": acSysModuleSWVersion,
       "acSysModuleOperationalState": acSysModuleOperationalState,
       "acSysModuleHAStatus": acSysModuleHAStatus,
       "acSysModuleLEDs": acSysModuleLEDs,
       "acSysModuleTemperature": acSysModuleTemperature,
       "acSysModuleActions": acSysModuleActions,
       "acSysModuleFRUaction": acSysModuleFRUaction,
       "acSysModuleFRUstatus": acSysModuleFRUstatus,
       "acSysModuleNumOfPorts": acSysModuleNumOfPorts,
       "acSysModuleFirstPortNum": acSysModuleFirstPortNum,
       "acSysFanTrayTable": acSysFanTrayTable,
       "acSysFanTrayEntry": acSysFanTrayEntry,
       "acSysFanTrayIndex": acSysFanTrayIndex,
       "acSysFanTrayGeographicalPosition": acSysFanTrayGeographicalPosition,
       "acSysFanTrayExistence": acSysFanTrayExistence,
       "acSysFanTrayType": acSysFanTrayType,
       "acSysFanTrayLEDs": acSysFanTrayLEDs,
       "acSysFanTraySeverity": acSysFanTraySeverity,
       "acSysFanTrayFansConfiguredSpeed": acSysFanTrayFansConfiguredSpeed,
       "acSysFanTrayFansCurrentSpeed": acSysFanTrayFansCurrentSpeed,
       "acSysFanTrayFansStatus": acSysFanTrayFansStatus,
       "acSysPowerSupplyTable": acSysPowerSupplyTable,
       "acSysPowerSupplyEntry": acSysPowerSupplyEntry,
       "acSysPowerSupplyIndex": acSysPowerSupplyIndex,
       "acSysPowerSupplyGeographicalPosition": acSysPowerSupplyGeographicalPosition,
       "acSysPowerSupplyExistence": acSysPowerSupplyExistence,
       "acSysPowerSupplyHwversion": acSysPowerSupplyHwversion,
       "acSysPowerSupplyLEDs": acSysPowerSupplyLEDs,
       "acSysPowerSupplySeverity": acSysPowerSupplySeverity,
       "acSysPEMTable": acSysPEMTable,
       "acSysPEMEntry": acSysPEMEntry,
       "acSysPEMIndex": acSysPEMIndex,
       "acSysPEMGeographicalPosition": acSysPEMGeographicalPosition,
       "acSysPEMExistence": acSysPEMExistence,
       "acSysPEMType": acSysPEMType,
       "acSysPEMElectricWireConnection": acSysPEMElectricWireConnection,
       "acSysSATModule": acSysSATModule,
       "acSysSATTable": acSysSATTable,
       "acSysSATEntry": acSysSATEntry,
       "acSysSATSatIndex": acSysSATSatIndex,
       "acSysSATGeographicalPosition": acSysSATGeographicalPosition,
       "acSysSATType": acSysSATType,
       "acSysSATInitInformation": acSysSATInitInformation,
       "acSysSATTimingUnitExistence": acSysSATTimingUnitExistence,
       "acSysSATTimingRefSelection": acSysSATTimingRefSelection,
       "acSysSATFramersTable": acSysSATFramersTable,
       "acSysSATFramersEntry": acSysSATFramersEntry,
       "acSysSATFramersSatIndex": acSysSATFramersSatIndex,
       "acSysSATFramersFramerIndex": acSysSATFramersFramerIndex,
       "acSysSATFramersFramerInterfaceStatus": acSysSATFramersFramerInterfaceStatus,
       "acSysSATFramersFramerLoopBackRef": acSysSATFramersFramerLoopBackRef,
       "acSysSATFramersFramerInterfaceType": acSysSATFramersFramerInterfaceType,
       "acSysSATFramersFramerTransmitControl": acSysSATFramersFramerTransmitControl,
       "acSysSATFramersRxStatus": acSysSATFramersRxStatus,
       "acSysSATFramersIsUsedAsPLLClock": acSysSATFramersIsUsedAsPLLClock,
       "acSysTimingModule": acSysTimingModule,
       "acSysPLLStatusTable": acSysPLLStatusTable,
       "acSysPLLStatusEntry": acSysPLLStatusEntry,
       "acSysPLLStatusIndex": acSysPLLStatusIndex,
       "acSysPLLStatusOperatingMode": acSysPLLStatusOperatingMode}
)
