# SNMP MIB module (ALCATEL-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ALCATEL-ISIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:37:40 2024
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

(routingIND1ISIS,) = mibBuilder.importSymbols(
    "ALCATEL-IND1-BASE",
    "routingIND1ISIS")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(SNPAAddress,
 SystemID,
 isisISAdjEntry,
 isisISAdjState,
 isisManAreaAddrExistState,
 isisSysInstance,
 isisSysL1State,
 isisSysL2State) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "SNPAAddress",
    "SystemID",
    "isisISAdjEntry",
    "isisISAdjState",
    "isisManAreaAddrExistState",
    "isisSysInstance",
    "isisSysL1State",
    "isisSysL2State")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

timetraIsisMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1)
)
timetraIsisMIBModule.setRevisions(
        ("2007-07-02 00:00",
         "1906-03-16 00:00",
         "1905-08-31 00:00",
         "1905-01-24 00:00",
         "1904-06-02 00:00",
         "1904-01-15 00:00",
         "1903-08-15 00:00",
         "1903-01-20 00:00",
         "1901-09-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxAdminState(Integer32, TextualConvention):
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
        *(("inService", 2),
          ("noop", 1),
          ("outOfService", 3))
    )



class TmnxOperState(Integer32, TextualConvention):
    status = "current"
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
        *(("inService", 2),
          ("outOfService", 3),
          ("transition", 4),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_VRtrIsisObjs_ObjectIdentity = ObjectIdentity
vRtrIsisObjs = _VRtrIsisObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10)
)
_VRtrIsisScalarObjs_ObjectIdentity = ObjectIdentity
vRtrIsisScalarObjs = _VRtrIsisScalarObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 1)
)


class _VRtrIsisStatisticsClear_Type(Integer32):
    """Custom type vRtrIsisStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VRtrIsisStatisticsClear_Type.__name__ = "Integer32"
_VRtrIsisStatisticsClear_Object = MibScalar
vRtrIsisStatisticsClear = _VRtrIsisStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 1, 1),
    _VRtrIsisStatisticsClear_Type()
)
vRtrIsisStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisStatisticsClear.setStatus("current")


class _VRtrIsisLSPClear_Type(Integer32):
    """Custom type vRtrIsisLSPClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VRtrIsisLSPClear_Type.__name__ = "Integer32"
_VRtrIsisLSPClear_Object = MibScalar
vRtrIsisLSPClear = _VRtrIsisLSPClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 1, 2),
    _VRtrIsisLSPClear_Type()
)
vRtrIsisLSPClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLSPClear.setStatus("current")


class _VRtrIsisISAdjClear_Type(Integer32):
    """Custom type vRtrIsisISAdjClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VRtrIsisISAdjClear_Type.__name__ = "Integer32"
_VRtrIsisISAdjClear_Object = MibScalar
vRtrIsisISAdjClear = _VRtrIsisISAdjClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 1, 3),
    _VRtrIsisISAdjClear_Type()
)
vRtrIsisISAdjClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisISAdjClear.setStatus("current")


class _VRtrIsisSpfClear_Type(Integer32):
    """Custom type vRtrIsisSpfClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VRtrIsisSpfClear_Type.__name__ = "Integer32"
_VRtrIsisSpfClear_Object = MibScalar
vRtrIsisSpfClear = _VRtrIsisSpfClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 1, 4),
    _VRtrIsisSpfClear_Type()
)
vRtrIsisSpfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisSpfClear.setStatus("current")
_VRtrIsisSystemObjs_ObjectIdentity = ObjectIdentity
vRtrIsisSystemObjs = _VRtrIsisSystemObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2)
)
_VRtrIsisTable_Object = MibTable
vRtrIsisTable = _VRtrIsisTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisTable.setStatus("current")
_VRtrIsisEntry_Object = MibTableRow
vRtrIsisEntry = _VRtrIsisEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1)
)
vRtrIsisEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    vRtrIsisEntry.setStatus("current")


class _VRtrIsisLastEnabledTime_Type(DisplayString):
    """Custom type vRtrIsisLastEnabledTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VRtrIsisLastEnabledTime_Type.__name__ = "DisplayString"
_VRtrIsisLastEnabledTime_Object = MibTableColumn
vRtrIsisLastEnabledTime = _VRtrIsisLastEnabledTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 1),
    _VRtrIsisLastEnabledTime_Type()
)
vRtrIsisLastEnabledTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLastEnabledTime.setStatus("current")


class _VRtrIsisAuthKey_Type(OctetString):
    """Custom type vRtrIsisAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 118),
    )


_VRtrIsisAuthKey_Type.__name__ = "OctetString"
_VRtrIsisAuthKey_Object = MibTableColumn
vRtrIsisAuthKey = _VRtrIsisAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 2),
    _VRtrIsisAuthKey_Type()
)
vRtrIsisAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisAuthKey.setStatus("current")


class _VRtrIsisAuthType_Type(Integer32):
    """Custom type vRtrIsisAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_VRtrIsisAuthType_Type.__name__ = "Integer32"
_VRtrIsisAuthType_Object = MibTableColumn
vRtrIsisAuthType = _VRtrIsisAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 3),
    _VRtrIsisAuthType_Type()
)
vRtrIsisAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisAuthType.setStatus("current")


class _VRtrIsisAuthCheck_Type(TruthValue):
    """Custom type vRtrIsisAuthCheck based on TruthValue"""


_VRtrIsisAuthCheck_Object = MibTableColumn
vRtrIsisAuthCheck = _VRtrIsisAuthCheck_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 4),
    _VRtrIsisAuthCheck_Type()
)
vRtrIsisAuthCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisAuthCheck.setStatus("current")


class _VRtrIsisLspLifetime_Type(Unsigned32):
    """Custom type vRtrIsisLspLifetime based on Unsigned32"""
    defaultValue = 1200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_VRtrIsisLspLifetime_Type.__name__ = "Unsigned32"
_VRtrIsisLspLifetime_Object = MibTableColumn
vRtrIsisLspLifetime = _VRtrIsisLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 10),
    _VRtrIsisLspLifetime_Type()
)
vRtrIsisLspLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLspLifetime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisLspLifetime.setUnits("seconds")


class _VRtrIsisOverloadTimeout_Type(Unsigned32):
    """Custom type vRtrIsisOverloadTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_VRtrIsisOverloadTimeout_Type.__name__ = "Unsigned32"
_VRtrIsisOverloadTimeout_Object = MibTableColumn
vRtrIsisOverloadTimeout = _VRtrIsisOverloadTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 11),
    _VRtrIsisOverloadTimeout_Type()
)
vRtrIsisOverloadTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisOverloadTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisOverloadTimeout.setUnits("seconds")
_VRtrIsisOperState_Type = TmnxOperState
_VRtrIsisOperState_Object = MibTableColumn
vRtrIsisOperState = _VRtrIsisOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 12),
    _VRtrIsisOperState_Type()
)
vRtrIsisOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisOperState.setStatus("current")


class _VRtrIsisShortCuts_Type(TruthValue):
    """Custom type vRtrIsisShortCuts based on TruthValue"""


_VRtrIsisShortCuts_Object = MibTableColumn
vRtrIsisShortCuts = _VRtrIsisShortCuts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 13),
    _VRtrIsisShortCuts_Type()
)
vRtrIsisShortCuts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisShortCuts.setStatus("current")


class _VRtrIsisSpfHoldTime_Type(Integer32):
    """Custom type vRtrIsisSpfHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisSpfHoldTime_Type.__name__ = "Integer32"
_VRtrIsisSpfHoldTime_Object = MibTableColumn
vRtrIsisSpfHoldTime = _VRtrIsisSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 14),
    _VRtrIsisSpfHoldTime_Type()
)
vRtrIsisSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisSpfHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisSpfHoldTime.setUnits("seconds")


class _VRtrIsisLastSpfRun_Type(DisplayString):
    """Custom type vRtrIsisLastSpfRun based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_VRtrIsisLastSpfRun_Type.__name__ = "DisplayString"
_VRtrIsisLastSpfRun_Object = MibTableColumn
vRtrIsisLastSpfRun = _VRtrIsisLastSpfRun_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 15),
    _VRtrIsisLastSpfRun_Type()
)
vRtrIsisLastSpfRun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLastSpfRun.setStatus("current")


class _VRtrIsisGracefulRestart_Type(TruthValue):
    """Custom type vRtrIsisGracefulRestart based on TruthValue"""


_VRtrIsisGracefulRestart_Object = MibTableColumn
vRtrIsisGracefulRestart = _VRtrIsisGracefulRestart_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 16),
    _VRtrIsisGracefulRestart_Type()
)
vRtrIsisGracefulRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisGracefulRestart.setStatus("current")


class _VRtrIsisOverloadOnBoot_Type(Integer32):
    """Custom type vRtrIsisOverloadOnBoot based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("enabledWaitForBgp", 3))
    )


_VRtrIsisOverloadOnBoot_Type.__name__ = "Integer32"
_VRtrIsisOverloadOnBoot_Object = MibTableColumn
vRtrIsisOverloadOnBoot = _VRtrIsisOverloadOnBoot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 17),
    _VRtrIsisOverloadOnBoot_Type()
)
vRtrIsisOverloadOnBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBoot.setStatus("current")


class _VRtrIsisOverloadOnBootTimeout_Type(Unsigned32):
    """Custom type vRtrIsisOverloadOnBootTimeout based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1800),
    )


_VRtrIsisOverloadOnBootTimeout_Type.__name__ = "Unsigned32"
_VRtrIsisOverloadOnBootTimeout_Object = MibTableColumn
vRtrIsisOverloadOnBootTimeout = _VRtrIsisOverloadOnBootTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 18),
    _VRtrIsisOverloadOnBootTimeout_Type()
)
vRtrIsisOverloadOnBootTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBootTimeout.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisOverloadOnBootTimeout.setUnits("seconds")


class _VRtrIsisSpfWait_Type(Unsigned32):
    """Custom type vRtrIsisSpfWait based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_VRtrIsisSpfWait_Type.__name__ = "Unsigned32"
_VRtrIsisSpfWait_Object = MibTableColumn
vRtrIsisSpfWait = _VRtrIsisSpfWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 19),
    _VRtrIsisSpfWait_Type()
)
vRtrIsisSpfWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisSpfWait.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisSpfWait.setUnits("seconds")


class _VRtrIsisSpfInitialWait_Type(Unsigned32):
    """Custom type vRtrIsisSpfInitialWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 100000),
    )


_VRtrIsisSpfInitialWait_Type.__name__ = "Unsigned32"
_VRtrIsisSpfInitialWait_Object = MibTableColumn
vRtrIsisSpfInitialWait = _VRtrIsisSpfInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 20),
    _VRtrIsisSpfInitialWait_Type()
)
vRtrIsisSpfInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisSpfInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisSpfInitialWait.setUnits("milliseconds")


class _VRtrIsisSpfSecondWait_Type(Unsigned32):
    """Custom type vRtrIsisSpfSecondWait based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_VRtrIsisSpfSecondWait_Type.__name__ = "Unsigned32"
_VRtrIsisSpfSecondWait_Object = MibTableColumn
vRtrIsisSpfSecondWait = _VRtrIsisSpfSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 21),
    _VRtrIsisSpfSecondWait_Type()
)
vRtrIsisSpfSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisSpfSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisSpfSecondWait.setUnits("milliseconds")


class _VRtrIsisLspMaxWait_Type(Unsigned32):
    """Custom type vRtrIsisLspMaxWait based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_VRtrIsisLspMaxWait_Type.__name__ = "Unsigned32"
_VRtrIsisLspMaxWait_Object = MibTableColumn
vRtrIsisLspMaxWait = _VRtrIsisLspMaxWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 22),
    _VRtrIsisLspMaxWait_Type()
)
vRtrIsisLspMaxWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLspMaxWait.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisLspMaxWait.setUnits("seconds")


class _VRtrIsisLspInitialWait_Type(Unsigned32):
    """Custom type vRtrIsisLspInitialWait based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VRtrIsisLspInitialWait_Type.__name__ = "Unsigned32"
_VRtrIsisLspInitialWait_Object = MibTableColumn
vRtrIsisLspInitialWait = _VRtrIsisLspInitialWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 23),
    _VRtrIsisLspInitialWait_Type()
)
vRtrIsisLspInitialWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLspInitialWait.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisLspInitialWait.setUnits("seconds")


class _VRtrIsisLspSecondWait_Type(Unsigned32):
    """Custom type vRtrIsisLspSecondWait based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VRtrIsisLspSecondWait_Type.__name__ = "Unsigned32"
_VRtrIsisLspSecondWait_Object = MibTableColumn
vRtrIsisLspSecondWait = _VRtrIsisLspSecondWait_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 24),
    _VRtrIsisLspSecondWait_Type()
)
vRtrIsisLspSecondWait.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLspSecondWait.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisLspSecondWait.setUnits("seconds")


class _VRtrIsisCsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisCsnpAuthentication based on TruthValue"""


_VRtrIsisCsnpAuthentication_Object = MibTableColumn
vRtrIsisCsnpAuthentication = _VRtrIsisCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 25),
    _VRtrIsisCsnpAuthentication_Type()
)
vRtrIsisCsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisCsnpAuthentication.setStatus("current")


class _VRtrIsisHelloAuthentication_Type(TruthValue):
    """Custom type vRtrIsisHelloAuthentication based on TruthValue"""


_VRtrIsisHelloAuthentication_Object = MibTableColumn
vRtrIsisHelloAuthentication = _VRtrIsisHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 26),
    _VRtrIsisHelloAuthentication_Type()
)
vRtrIsisHelloAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisHelloAuthentication.setStatus("current")


class _VRtrIsisPsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisPsnpAuthentication based on TruthValue"""


_VRtrIsisPsnpAuthentication_Object = MibTableColumn
vRtrIsisPsnpAuthentication = _VRtrIsisPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 27),
    _VRtrIsisPsnpAuthentication_Type()
)
vRtrIsisPsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisPsnpAuthentication.setStatus("current")


class _VRtrIsisGRRestartDuration_Type(Unsigned32):
    """Custom type vRtrIsisGRRestartDuration based on Unsigned32"""
    defaultValue = 180

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_VRtrIsisGRRestartDuration_Type.__name__ = "Unsigned32"
_VRtrIsisGRRestartDuration_Object = MibTableColumn
vRtrIsisGRRestartDuration = _VRtrIsisGRRestartDuration_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 28),
    _VRtrIsisGRRestartDuration_Type()
)
vRtrIsisGRRestartDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisGRRestartDuration.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisGRRestartDuration.setUnits("seconds")


class _VRtrIsisGRHelperMode_Type(TruthValue):
    """Custom type vRtrIsisGRHelperMode based on TruthValue"""


_VRtrIsisGRHelperMode_Object = MibTableColumn
vRtrIsisGRHelperMode = _VRtrIsisGRHelperMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 29),
    _VRtrIsisGRHelperMode_Type()
)
vRtrIsisGRHelperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisGRHelperMode.setStatus("current")


class _VRtrIsisStrictAdjacencyCheck_Type(TruthValue):
    """Custom type vRtrIsisStrictAdjacencyCheck based on TruthValue"""


_VRtrIsisStrictAdjacencyCheck_Object = MibTableColumn
vRtrIsisStrictAdjacencyCheck = _VRtrIsisStrictAdjacencyCheck_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 1, 1, 30),
    _VRtrIsisStrictAdjacencyCheck_Type()
)
vRtrIsisStrictAdjacencyCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisStrictAdjacencyCheck.setStatus("current")
_VRtrIsisLevelTable_Object = MibTable
vRtrIsisLevelTable = _VRtrIsisLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2)
)
if mibBuilder.loadTexts:
    vRtrIsisLevelTable.setStatus("current")
_VRtrIsisLevelEntry_Object = MibTableRow
vRtrIsisLevelEntry = _VRtrIsisLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1)
)
vRtrIsisLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisLevel"),
)
if mibBuilder.loadTexts:
    vRtrIsisLevelEntry.setStatus("current")


class _VRtrIsisLevel_Type(Integer32):
    """Custom type vRtrIsisLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_VRtrIsisLevel_Type.__name__ = "Integer32"
_VRtrIsisLevel_Object = MibTableColumn
vRtrIsisLevel = _VRtrIsisLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 1),
    _VRtrIsisLevel_Type()
)
vRtrIsisLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisLevel.setStatus("current")


class _VRtrIsisLevelAuthKey_Type(OctetString):
    """Custom type vRtrIsisLevelAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 118),
    )


_VRtrIsisLevelAuthKey_Type.__name__ = "OctetString"
_VRtrIsisLevelAuthKey_Object = MibTableColumn
vRtrIsisLevelAuthKey = _VRtrIsisLevelAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 2),
    _VRtrIsisLevelAuthKey_Type()
)
vRtrIsisLevelAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLevelAuthKey.setStatus("current")


class _VRtrIsisLevelAuthType_Type(Integer32):
    """Custom type vRtrIsisLevelAuthType based on Integer32"""
    defaultValue = 0

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
        *(("md5", 3),
          ("none", 1),
          ("password", 2),
          ("useGlobal", 0))
    )


_VRtrIsisLevelAuthType_Type.__name__ = "Integer32"
_VRtrIsisLevelAuthType_Object = MibTableColumn
vRtrIsisLevelAuthType = _VRtrIsisLevelAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 3),
    _VRtrIsisLevelAuthType_Type()
)
vRtrIsisLevelAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLevelAuthType.setStatus("current")


class _VRtrIsisLevelWideMetricsOnly_Type(TruthValue):
    """Custom type vRtrIsisLevelWideMetricsOnly based on TruthValue"""


_VRtrIsisLevelWideMetricsOnly_Object = MibTableColumn
vRtrIsisLevelWideMetricsOnly = _VRtrIsisLevelWideMetricsOnly_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 4),
    _VRtrIsisLevelWideMetricsOnly_Type()
)
vRtrIsisLevelWideMetricsOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLevelWideMetricsOnly.setStatus("current")


class _VRtrIsisLevelOverloadStatus_Type(Integer32):
    """Custom type vRtrIsisLevelOverloadStatus based on Integer32"""
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
        *(("dynamic", 2),
          ("manual", 3),
          ("manualOnBoot", 4),
          ("notInOverload", 1))
    )


_VRtrIsisLevelOverloadStatus_Type.__name__ = "Integer32"
_VRtrIsisLevelOverloadStatus_Object = MibTableColumn
vRtrIsisLevelOverloadStatus = _VRtrIsisLevelOverloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 5),
    _VRtrIsisLevelOverloadStatus_Type()
)
vRtrIsisLevelOverloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelOverloadStatus.setStatus("current")
_VRtrIsisLevelOverloadTimeLeft_Type = TimeInterval
_VRtrIsisLevelOverloadTimeLeft_Object = MibTableColumn
vRtrIsisLevelOverloadTimeLeft = _VRtrIsisLevelOverloadTimeLeft_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 6),
    _VRtrIsisLevelOverloadTimeLeft_Type()
)
vRtrIsisLevelOverloadTimeLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelOverloadTimeLeft.setStatus("current")
_VRtrIsisLevelNumLSPs_Type = Unsigned32
_VRtrIsisLevelNumLSPs_Object = MibTableColumn
vRtrIsisLevelNumLSPs = _VRtrIsisLevelNumLSPs_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 7),
    _VRtrIsisLevelNumLSPs_Type()
)
vRtrIsisLevelNumLSPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLevelNumLSPs.setStatus("current")


class _VRtrIsisLevelCsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisLevelCsnpAuthentication based on TruthValue"""


_VRtrIsisLevelCsnpAuthentication_Object = MibTableColumn
vRtrIsisLevelCsnpAuthentication = _VRtrIsisLevelCsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 8),
    _VRtrIsisLevelCsnpAuthentication_Type()
)
vRtrIsisLevelCsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLevelCsnpAuthentication.setStatus("current")


class _VRtrIsisLevelHelloAuthentication_Type(TruthValue):
    """Custom type vRtrIsisLevelHelloAuthentication based on TruthValue"""


_VRtrIsisLevelHelloAuthentication_Object = MibTableColumn
vRtrIsisLevelHelloAuthentication = _VRtrIsisLevelHelloAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 9),
    _VRtrIsisLevelHelloAuthentication_Type()
)
vRtrIsisLevelHelloAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLevelHelloAuthentication.setStatus("current")


class _VRtrIsisLevelPsnpAuthentication_Type(TruthValue):
    """Custom type vRtrIsisLevelPsnpAuthentication based on TruthValue"""


_VRtrIsisLevelPsnpAuthentication_Object = MibTableColumn
vRtrIsisLevelPsnpAuthentication = _VRtrIsisLevelPsnpAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 2, 1, 10),
    _VRtrIsisLevelPsnpAuthentication_Type()
)
vRtrIsisLevelPsnpAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLevelPsnpAuthentication.setStatus("current")
_VRtrIsisStatsTable_Object = MibTable
vRtrIsisStatsTable = _VRtrIsisStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3)
)
if mibBuilder.loadTexts:
    vRtrIsisStatsTable.setStatus("current")
_VRtrIsisStatsEntry_Object = MibTableRow
vRtrIsisStatsEntry = _VRtrIsisStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1)
)
vRtrIsisStatsEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    vRtrIsisStatsEntry.setStatus("current")
_VRtrIsisSpfRuns_Type = Counter32
_VRtrIsisSpfRuns_Object = MibTableColumn
vRtrIsisSpfRuns = _VRtrIsisSpfRuns_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 1),
    _VRtrIsisSpfRuns_Type()
)
vRtrIsisSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfRuns.setStatus("current")
_VRtrIsisLSPRegenerations_Type = Counter32
_VRtrIsisLSPRegenerations_Object = MibTableColumn
vRtrIsisLSPRegenerations = _VRtrIsisLSPRegenerations_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 2),
    _VRtrIsisLSPRegenerations_Type()
)
vRtrIsisLSPRegenerations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPRegenerations.setStatus("current")
_VRtrIsisInitiatedPurges_Type = Counter32
_VRtrIsisInitiatedPurges_Object = MibTableColumn
vRtrIsisInitiatedPurges = _VRtrIsisInitiatedPurges_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 3),
    _VRtrIsisInitiatedPurges_Type()
)
vRtrIsisInitiatedPurges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInitiatedPurges.setStatus("current")
_VRtrIsisLSPRecd_Type = Counter32
_VRtrIsisLSPRecd_Object = MibTableColumn
vRtrIsisLSPRecd = _VRtrIsisLSPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 4),
    _VRtrIsisLSPRecd_Type()
)
vRtrIsisLSPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPRecd.setStatus("current")
_VRtrIsisLSPDrop_Type = Counter32
_VRtrIsisLSPDrop_Object = MibTableColumn
vRtrIsisLSPDrop = _VRtrIsisLSPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 5),
    _VRtrIsisLSPDrop_Type()
)
vRtrIsisLSPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPDrop.setStatus("current")
_VRtrIsisLSPSent_Type = Counter32
_VRtrIsisLSPSent_Object = MibTableColumn
vRtrIsisLSPSent = _VRtrIsisLSPSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 6),
    _VRtrIsisLSPSent_Type()
)
vRtrIsisLSPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPSent.setStatus("current")
_VRtrIsisLSPRetrans_Type = Counter32
_VRtrIsisLSPRetrans_Object = MibTableColumn
vRtrIsisLSPRetrans = _VRtrIsisLSPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 7),
    _VRtrIsisLSPRetrans_Type()
)
vRtrIsisLSPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPRetrans.setStatus("current")
_VRtrIsisIIHRecd_Type = Counter32
_VRtrIsisIIHRecd_Object = MibTableColumn
vRtrIsisIIHRecd = _VRtrIsisIIHRecd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 8),
    _VRtrIsisIIHRecd_Type()
)
vRtrIsisIIHRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHRecd.setStatus("current")
_VRtrIsisIIHDrop_Type = Counter32
_VRtrIsisIIHDrop_Object = MibTableColumn
vRtrIsisIIHDrop = _VRtrIsisIIHDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 9),
    _VRtrIsisIIHDrop_Type()
)
vRtrIsisIIHDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHDrop.setStatus("current")
_VRtrIsisIIHSent_Type = Counter32
_VRtrIsisIIHSent_Object = MibTableColumn
vRtrIsisIIHSent = _VRtrIsisIIHSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 10),
    _VRtrIsisIIHSent_Type()
)
vRtrIsisIIHSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHSent.setStatus("current")
_VRtrIsisIIHRetrans_Type = Counter32
_VRtrIsisIIHRetrans_Object = MibTableColumn
vRtrIsisIIHRetrans = _VRtrIsisIIHRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 11),
    _VRtrIsisIIHRetrans_Type()
)
vRtrIsisIIHRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIIHRetrans.setStatus("current")
_VRtrIsisCSNPRecd_Type = Counter32
_VRtrIsisCSNPRecd_Object = MibTableColumn
vRtrIsisCSNPRecd = _VRtrIsisCSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 12),
    _VRtrIsisCSNPRecd_Type()
)
vRtrIsisCSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPRecd.setStatus("current")
_VRtrIsisCSNPDrop_Type = Counter32
_VRtrIsisCSNPDrop_Object = MibTableColumn
vRtrIsisCSNPDrop = _VRtrIsisCSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 13),
    _VRtrIsisCSNPDrop_Type()
)
vRtrIsisCSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPDrop.setStatus("current")
_VRtrIsisCSNPSent_Type = Counter32
_VRtrIsisCSNPSent_Object = MibTableColumn
vRtrIsisCSNPSent = _VRtrIsisCSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 14),
    _VRtrIsisCSNPSent_Type()
)
vRtrIsisCSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPSent.setStatus("current")
_VRtrIsisCSNPRetrans_Type = Counter32
_VRtrIsisCSNPRetrans_Object = MibTableColumn
vRtrIsisCSNPRetrans = _VRtrIsisCSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 15),
    _VRtrIsisCSNPRetrans_Type()
)
vRtrIsisCSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSNPRetrans.setStatus("current")
_VRtrIsisPSNPRecd_Type = Counter32
_VRtrIsisPSNPRecd_Object = MibTableColumn
vRtrIsisPSNPRecd = _VRtrIsisPSNPRecd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 16),
    _VRtrIsisPSNPRecd_Type()
)
vRtrIsisPSNPRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPRecd.setStatus("current")
_VRtrIsisPSNPDrop_Type = Counter32
_VRtrIsisPSNPDrop_Object = MibTableColumn
vRtrIsisPSNPDrop = _VRtrIsisPSNPDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 17),
    _VRtrIsisPSNPDrop_Type()
)
vRtrIsisPSNPDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPDrop.setStatus("current")
_VRtrIsisPSNPSent_Type = Counter32
_VRtrIsisPSNPSent_Object = MibTableColumn
vRtrIsisPSNPSent = _VRtrIsisPSNPSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 18),
    _VRtrIsisPSNPSent_Type()
)
vRtrIsisPSNPSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPSent.setStatus("current")
_VRtrIsisPSNPRetrans_Type = Counter32
_VRtrIsisPSNPRetrans_Object = MibTableColumn
vRtrIsisPSNPRetrans = _VRtrIsisPSNPRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 19),
    _VRtrIsisPSNPRetrans_Type()
)
vRtrIsisPSNPRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPSNPRetrans.setStatus("current")
_VRtrIsisUnknownRecd_Type = Counter32
_VRtrIsisUnknownRecd_Object = MibTableColumn
vRtrIsisUnknownRecd = _VRtrIsisUnknownRecd_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 20),
    _VRtrIsisUnknownRecd_Type()
)
vRtrIsisUnknownRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownRecd.setStatus("current")
_VRtrIsisUnknownDrop_Type = Counter32
_VRtrIsisUnknownDrop_Object = MibTableColumn
vRtrIsisUnknownDrop = _VRtrIsisUnknownDrop_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 21),
    _VRtrIsisUnknownDrop_Type()
)
vRtrIsisUnknownDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownDrop.setStatus("current")
_VRtrIsisUnknownSent_Type = Counter32
_VRtrIsisUnknownSent_Object = MibTableColumn
vRtrIsisUnknownSent = _VRtrIsisUnknownSent_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 22),
    _VRtrIsisUnknownSent_Type()
)
vRtrIsisUnknownSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownSent.setStatus("current")
_VRtrIsisUnknownRetrans_Type = Counter32
_VRtrIsisUnknownRetrans_Object = MibTableColumn
vRtrIsisUnknownRetrans = _VRtrIsisUnknownRetrans_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 23),
    _VRtrIsisUnknownRetrans_Type()
)
vRtrIsisUnknownRetrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisUnknownRetrans.setStatus("current")
_VRtrIsisCSPFRequests_Type = Counter32
_VRtrIsisCSPFRequests_Object = MibTableColumn
vRtrIsisCSPFRequests = _VRtrIsisCSPFRequests_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 24),
    _VRtrIsisCSPFRequests_Type()
)
vRtrIsisCSPFRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFRequests.setStatus("current")
_VRtrIsisCSPFDroppedRequests_Type = Counter32
_VRtrIsisCSPFDroppedRequests_Object = MibTableColumn
vRtrIsisCSPFDroppedRequests = _VRtrIsisCSPFDroppedRequests_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 25),
    _VRtrIsisCSPFDroppedRequests_Type()
)
vRtrIsisCSPFDroppedRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFDroppedRequests.setStatus("current")
_VRtrIsisCSPFPathsFound_Type = Counter32
_VRtrIsisCSPFPathsFound_Object = MibTableColumn
vRtrIsisCSPFPathsFound = _VRtrIsisCSPFPathsFound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 26),
    _VRtrIsisCSPFPathsFound_Type()
)
vRtrIsisCSPFPathsFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFPathsFound.setStatus("current")
_VRtrIsisCSPFPathsNotFound_Type = Counter32
_VRtrIsisCSPFPathsNotFound_Object = MibTableColumn
vRtrIsisCSPFPathsNotFound = _VRtrIsisCSPFPathsNotFound_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 3, 1, 27),
    _VRtrIsisCSPFPathsNotFound_Type()
)
vRtrIsisCSPFPathsNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisCSPFPathsNotFound.setStatus("current")
_VRtrIsisHostnameTable_Object = MibTable
vRtrIsisHostnameTable = _VRtrIsisHostnameTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 4)
)
if mibBuilder.loadTexts:
    vRtrIsisHostnameTable.setStatus("current")
_VRtrIsisHostnameEntry_Object = MibTableRow
vRtrIsisHostnameEntry = _VRtrIsisHostnameEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 4, 1)
)
vRtrIsisHostnameEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisSysID"),
)
if mibBuilder.loadTexts:
    vRtrIsisHostnameEntry.setStatus("current")
_VRtrIsisSysID_Type = SystemID
_VRtrIsisSysID_Object = MibTableColumn
vRtrIsisSysID = _VRtrIsisSysID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 4, 1, 1),
    _VRtrIsisSysID_Type()
)
vRtrIsisSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSysID.setStatus("current")
_VRtrIsisHostname_Type = DisplayString
_VRtrIsisHostname_Object = MibTableColumn
vRtrIsisHostname = _VRtrIsisHostname_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 4, 1, 2),
    _VRtrIsisHostname_Type()
)
vRtrIsisHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisHostname.setStatus("current")
_VRtrIsisRouteTable_Object = MibTable
vRtrIsisRouteTable = _VRtrIsisRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5)
)
if mibBuilder.loadTexts:
    vRtrIsisRouteTable.setStatus("current")
_VRtrIsisRouteEntry_Object = MibTableRow
vRtrIsisRouteEntry = _VRtrIsisRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1)
)
vRtrIsisRouteEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisRouteDest"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisRouteMask"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    vRtrIsisRouteEntry.setStatus("current")
_VRtrIsisRouteDest_Type = IpAddress
_VRtrIsisRouteDest_Object = MibTableColumn
vRtrIsisRouteDest = _VRtrIsisRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 1),
    _VRtrIsisRouteDest_Type()
)
vRtrIsisRouteDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteDest.setStatus("current")
_VRtrIsisRouteMask_Type = IpAddress
_VRtrIsisRouteMask_Object = MibTableColumn
vRtrIsisRouteMask = _VRtrIsisRouteMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 2),
    _VRtrIsisRouteMask_Type()
)
vRtrIsisRouteMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteMask.setStatus("current")
_VRtrIsisRouteNexthopIP_Type = IpAddress
_VRtrIsisRouteNexthopIP_Object = MibTableColumn
vRtrIsisRouteNexthopIP = _VRtrIsisRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 3),
    _VRtrIsisRouteNexthopIP_Type()
)
vRtrIsisRouteNexthopIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteNexthopIP.setStatus("current")


class _VRtrIsisRouteLevel_Type(Integer32):
    """Custom type vRtrIsisRouteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_VRtrIsisRouteLevel_Type.__name__ = "Integer32"
_VRtrIsisRouteLevel_Object = MibTableColumn
vRtrIsisRouteLevel = _VRtrIsisRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 4),
    _VRtrIsisRouteLevel_Type()
)
vRtrIsisRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteLevel.setStatus("current")
_VRtrIsisRouteSpfVersion_Type = Counter32
_VRtrIsisRouteSpfVersion_Object = MibTableColumn
vRtrIsisRouteSpfVersion = _VRtrIsisRouteSpfVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 5),
    _VRtrIsisRouteSpfVersion_Type()
)
vRtrIsisRouteSpfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteSpfVersion.setStatus("current")
_VRtrIsisRouteMetric_Type = Unsigned32
_VRtrIsisRouteMetric_Object = MibTableColumn
vRtrIsisRouteMetric = _VRtrIsisRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 6),
    _VRtrIsisRouteMetric_Type()
)
vRtrIsisRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteMetric.setStatus("current")


class _VRtrIsisRouteType_Type(Integer32):
    """Custom type vRtrIsisRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_VRtrIsisRouteType_Type.__name__ = "Integer32"
_VRtrIsisRouteType_Object = MibTableColumn
vRtrIsisRouteType = _VRtrIsisRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 7),
    _VRtrIsisRouteType_Type()
)
vRtrIsisRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteType.setStatus("current")
_VRtrIsisRouteNHopSysID_Type = SystemID
_VRtrIsisRouteNHopSysID_Object = MibTableColumn
vRtrIsisRouteNHopSysID = _VRtrIsisRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 5, 1, 8),
    _VRtrIsisRouteNHopSysID_Type()
)
vRtrIsisRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisRouteNHopSysID.setStatus("current")
_VRtrIsisPathTable_Object = MibTable
vRtrIsisPathTable = _VRtrIsisPathTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6)
)
if mibBuilder.loadTexts:
    vRtrIsisPathTable.setStatus("current")
_VRtrIsisPathEntry_Object = MibTableRow
vRtrIsisPathEntry = _VRtrIsisPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6, 1)
)
vRtrIsisPathEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisLevel"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisPathID"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisPathIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIsisPathEntry.setStatus("current")


class _VRtrIsisPathID_Type(OctetString):
    """Custom type vRtrIsisPathID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_VRtrIsisPathID_Type.__name__ = "OctetString"
_VRtrIsisPathID_Object = MibTableColumn
vRtrIsisPathID = _VRtrIsisPathID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6, 1, 1),
    _VRtrIsisPathID_Type()
)
vRtrIsisPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathID.setStatus("current")
_VRtrIsisPathIfIndex_Type = InterfaceIndex
_VRtrIsisPathIfIndex_Object = MibTableColumn
vRtrIsisPathIfIndex = _VRtrIsisPathIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6, 1, 2),
    _VRtrIsisPathIfIndex_Type()
)
vRtrIsisPathIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathIfIndex.setStatus("current")
_VRtrIsisPathNHopSysID_Type = SystemID
_VRtrIsisPathNHopSysID_Object = MibTableColumn
vRtrIsisPathNHopSysID = _VRtrIsisPathNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6, 1, 3),
    _VRtrIsisPathNHopSysID_Type()
)
vRtrIsisPathNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathNHopSysID.setStatus("current")
_VRtrIsisPathMetric_Type = Unsigned32
_VRtrIsisPathMetric_Object = MibTableColumn
vRtrIsisPathMetric = _VRtrIsisPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6, 1, 4),
    _VRtrIsisPathMetric_Type()
)
vRtrIsisPathMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathMetric.setStatus("current")
_VRtrIsisPathSNPA_Type = SNPAAddress
_VRtrIsisPathSNPA_Object = MibTableColumn
vRtrIsisPathSNPA = _VRtrIsisPathSNPA_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 6, 1, 5),
    _VRtrIsisPathSNPA_Type()
)
vRtrIsisPathSNPA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisPathSNPA.setStatus("current")
_VRtrIsisLSPTable_Object = MibTable
vRtrIsisLSPTable = _VRtrIsisLSPTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7)
)
if mibBuilder.loadTexts:
    vRtrIsisLSPTable.setStatus("current")
_VRtrIsisLSPEntry_Object = MibTableRow
vRtrIsisLSPEntry = _VRtrIsisLSPEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1)
)
vRtrIsisLSPEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisLevel"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisLSPId"),
)
if mibBuilder.loadTexts:
    vRtrIsisLSPEntry.setStatus("current")


class _VRtrIsisLSPId_Type(OctetString):
    """Custom type vRtrIsisLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VRtrIsisLSPId_Type.__name__ = "OctetString"
_VRtrIsisLSPId_Object = MibTableColumn
vRtrIsisLSPId = _VRtrIsisLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 1),
    _VRtrIsisLSPId_Type()
)
vRtrIsisLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPId.setStatus("current")
_VRtrIsisLSPSeq_Type = Counter32
_VRtrIsisLSPSeq_Object = MibTableColumn
vRtrIsisLSPSeq = _VRtrIsisLSPSeq_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 2),
    _VRtrIsisLSPSeq_Type()
)
vRtrIsisLSPSeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPSeq.setStatus("current")


class _VRtrIsisLSPChecksum_Type(Integer32):
    """Custom type vRtrIsisLSPChecksum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisLSPChecksum_Type.__name__ = "Integer32"
_VRtrIsisLSPChecksum_Object = MibTableColumn
vRtrIsisLSPChecksum = _VRtrIsisLSPChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 3),
    _VRtrIsisLSPChecksum_Type()
)
vRtrIsisLSPChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPChecksum.setStatus("current")


class _VRtrIsisLSPLifetimeRemain_Type(Integer32):
    """Custom type vRtrIsisLSPLifetimeRemain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisLSPLifetimeRemain_Type.__name__ = "Integer32"
_VRtrIsisLSPLifetimeRemain_Object = MibTableColumn
vRtrIsisLSPLifetimeRemain = _VRtrIsisLSPLifetimeRemain_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 4),
    _VRtrIsisLSPLifetimeRemain_Type()
)
vRtrIsisLSPLifetimeRemain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPLifetimeRemain.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisLSPLifetimeRemain.setUnits("seconds")
_VRtrIsisLSPVersion_Type = Integer32
_VRtrIsisLSPVersion_Object = MibTableColumn
vRtrIsisLSPVersion = _VRtrIsisLSPVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 5),
    _VRtrIsisLSPVersion_Type()
)
vRtrIsisLSPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPVersion.setStatus("current")
_VRtrIsisLSPPktType_Type = Integer32
_VRtrIsisLSPPktType_Object = MibTableColumn
vRtrIsisLSPPktType = _VRtrIsisLSPPktType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 6),
    _VRtrIsisLSPPktType_Type()
)
vRtrIsisLSPPktType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPPktType.setStatus("current")
_VRtrIsisLSPPktVersion_Type = Integer32
_VRtrIsisLSPPktVersion_Object = MibTableColumn
vRtrIsisLSPPktVersion = _VRtrIsisLSPPktVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 7),
    _VRtrIsisLSPPktVersion_Type()
)
vRtrIsisLSPPktVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPPktVersion.setStatus("current")
_VRtrIsisLSPMaxArea_Type = Integer32
_VRtrIsisLSPMaxArea_Object = MibTableColumn
vRtrIsisLSPMaxArea = _VRtrIsisLSPMaxArea_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 8),
    _VRtrIsisLSPMaxArea_Type()
)
vRtrIsisLSPMaxArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPMaxArea.setStatus("current")
_VRtrIsisLSPSysIdLen_Type = Integer32
_VRtrIsisLSPSysIdLen_Object = MibTableColumn
vRtrIsisLSPSysIdLen = _VRtrIsisLSPSysIdLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 9),
    _VRtrIsisLSPSysIdLen_Type()
)
vRtrIsisLSPSysIdLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPSysIdLen.setStatus("current")
_VRtrIsisLSPAttributes_Type = Integer32
_VRtrIsisLSPAttributes_Object = MibTableColumn
vRtrIsisLSPAttributes = _VRtrIsisLSPAttributes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 10),
    _VRtrIsisLSPAttributes_Type()
)
vRtrIsisLSPAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPAttributes.setStatus("current")
_VRtrIsisLSPUsedLen_Type = Integer32
_VRtrIsisLSPUsedLen_Object = MibTableColumn
vRtrIsisLSPUsedLen = _VRtrIsisLSPUsedLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 11),
    _VRtrIsisLSPUsedLen_Type()
)
vRtrIsisLSPUsedLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPUsedLen.setStatus("current")
_VRtrIsisLSPAllocLen_Type = Integer32
_VRtrIsisLSPAllocLen_Object = MibTableColumn
vRtrIsisLSPAllocLen = _VRtrIsisLSPAllocLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 12),
    _VRtrIsisLSPAllocLen_Type()
)
vRtrIsisLSPAllocLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPAllocLen.setStatus("current")


class _VRtrIsisLSPBuff_Type(OctetString):
    """Custom type vRtrIsisLSPBuff based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(27, 1492),
    )


_VRtrIsisLSPBuff_Type.__name__ = "OctetString"
_VRtrIsisLSPBuff_Object = MibTableColumn
vRtrIsisLSPBuff = _VRtrIsisLSPBuff_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 13),
    _VRtrIsisLSPBuff_Type()
)
vRtrIsisLSPBuff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPBuff.setStatus("current")
_VRtrIsisLSPZeroRLT_Type = TruthValue
_VRtrIsisLSPZeroRLT_Object = MibTableColumn
vRtrIsisLSPZeroRLT = _VRtrIsisLSPZeroRLT_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 7, 1, 14),
    _VRtrIsisLSPZeroRLT_Type()
)
vRtrIsisLSPZeroRLT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisLSPZeroRLT.setStatus("current")
_VRtrIsisSpfLogTable_Object = MibTable
vRtrIsisSpfLogTable = _VRtrIsisSpfLogTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8)
)
if mibBuilder.loadTexts:
    vRtrIsisSpfLogTable.setStatus("current")
_VRtrIsisSpfLogEntry_Object = MibTableRow
vRtrIsisSpfLogEntry = _VRtrIsisSpfLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1)
)
vRtrIsisSpfLogEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisSpfTimeStamp"),
)
if mibBuilder.loadTexts:
    vRtrIsisSpfLogEntry.setStatus("current")
_VRtrIsisSpfTimeStamp_Type = TimeStamp
_VRtrIsisSpfTimeStamp_Object = MibTableColumn
vRtrIsisSpfTimeStamp = _VRtrIsisSpfTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 1),
    _VRtrIsisSpfTimeStamp_Type()
)
vRtrIsisSpfTimeStamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSpfTimeStamp.setStatus("current")
_VRtrIsisSpfRunTime_Type = TimeTicks
_VRtrIsisSpfRunTime_Object = MibTableColumn
vRtrIsisSpfRunTime = _VRtrIsisSpfRunTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 2),
    _VRtrIsisSpfRunTime_Type()
)
vRtrIsisSpfRunTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfRunTime.setStatus("current")
_VRtrIsisSpfL1Nodes_Type = Unsigned32
_VRtrIsisSpfL1Nodes_Object = MibTableColumn
vRtrIsisSpfL1Nodes = _VRtrIsisSpfL1Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 3),
    _VRtrIsisSpfL1Nodes_Type()
)
vRtrIsisSpfL1Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfL1Nodes.setStatus("current")
_VRtrIsisSpfL2Nodes_Type = Unsigned32
_VRtrIsisSpfL2Nodes_Object = MibTableColumn
vRtrIsisSpfL2Nodes = _VRtrIsisSpfL2Nodes_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 4),
    _VRtrIsisSpfL2Nodes_Type()
)
vRtrIsisSpfL2Nodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfL2Nodes.setStatus("current")
_VRtrIsisSpfEventCount_Type = Unsigned32
_VRtrIsisSpfEventCount_Object = MibTableColumn
vRtrIsisSpfEventCount = _VRtrIsisSpfEventCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 5),
    _VRtrIsisSpfEventCount_Type()
)
vRtrIsisSpfEventCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfEventCount.setStatus("current")


class _VRtrIsisSpfLastTriggerLSPId_Type(OctetString):
    """Custom type vRtrIsisSpfLastTriggerLSPId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_VRtrIsisSpfLastTriggerLSPId_Type.__name__ = "OctetString"
_VRtrIsisSpfLastTriggerLSPId_Object = MibTableColumn
vRtrIsisSpfLastTriggerLSPId = _VRtrIsisSpfLastTriggerLSPId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 6),
    _VRtrIsisSpfLastTriggerLSPId_Type()
)
vRtrIsisSpfLastTriggerLSPId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfLastTriggerLSPId.setStatus("current")


class _VRtrIsisSpfTriggerReason_Type(Bits):
    """Custom type vRtrIsisSpfTriggerReason based on Bits"""
    namedValues = NamedValues(
        *(("ecmpChanged", 4),
          ("lspChanged", 10),
          ("lspDbChanged", 9),
          ("lspExpired", 8),
          ("newAdjacency", 0),
          ("newArea", 2),
          ("newLSP", 1),
          ("newMetric", 5),
          ("newNLPID", 12),
          ("newPreference", 11),
          ("reach", 3),
          ("restart", 7),
          ("teChanged", 6))
    )

_VRtrIsisSpfTriggerReason_Type.__name__ = "Bits"
_VRtrIsisSpfTriggerReason_Object = MibTableColumn
vRtrIsisSpfTriggerReason = _VRtrIsisSpfTriggerReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 8, 1, 7),
    _VRtrIsisSpfTriggerReason_Type()
)
vRtrIsisSpfTriggerReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisSpfTriggerReason.setStatus("current")
_VRtrIsisSummaryTable_Object = MibTable
vRtrIsisSummaryTable = _VRtrIsisSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 9)
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryTable.setStatus("current")
_VRtrIsisSummaryEntry_Object = MibTableRow
vRtrIsisSummaryEntry = _VRtrIsisSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 9, 1)
)
vRtrIsisSummaryEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisSummPrefix"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisSummMask"),
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryEntry.setStatus("current")
_VRtrIsisSummPrefix_Type = IpAddress
_VRtrIsisSummPrefix_Object = MibTableColumn
vRtrIsisSummPrefix = _VRtrIsisSummPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 9, 1, 1),
    _VRtrIsisSummPrefix_Type()
)
vRtrIsisSummPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSummPrefix.setStatus("current")
_VRtrIsisSummMask_Type = IpAddress
_VRtrIsisSummMask_Object = MibTableColumn
vRtrIsisSummMask = _VRtrIsisSummMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 9, 1, 2),
    _VRtrIsisSummMask_Type()
)
vRtrIsisSummMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisSummMask.setStatus("current")
_VRtrIsisSummRowStatus_Type = RowStatus
_VRtrIsisSummRowStatus_Object = MibTableColumn
vRtrIsisSummRowStatus = _VRtrIsisSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 9, 1, 3),
    _VRtrIsisSummRowStatus_Type()
)
vRtrIsisSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisSummRowStatus.setStatus("current")


class _VRtrIsisSummLevel_Type(Integer32):
    """Custom type vRtrIsisSummLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level1L2", 3),
          ("level2", 2))
    )


_VRtrIsisSummLevel_Type.__name__ = "Integer32"
_VRtrIsisSummLevel_Object = MibTableColumn
vRtrIsisSummLevel = _VRtrIsisSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 9, 1, 4),
    _VRtrIsisSummLevel_Type()
)
vRtrIsisSummLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisSummLevel.setStatus("current")
_VRtrIsisInetRouteTable_Object = MibTable
vRtrIsisInetRouteTable = _VRtrIsisInetRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10)
)
if mibBuilder.loadTexts:
    vRtrIsisInetRouteTable.setStatus("current")
_VRtrIsisInetRouteEntry_Object = MibTableRow
vRtrIsisInetRouteEntry = _VRtrIsisInetRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1)
)
vRtrIsisInetRouteEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetRouteDestType"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetRouteDest"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetRoutePrefixLength"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetRouteNexthopIPType"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetRouteNexthopIP"),
)
if mibBuilder.loadTexts:
    vRtrIsisInetRouteEntry.setStatus("current")
_VRtrIsisInetRouteDestType_Type = InetAddressType
_VRtrIsisInetRouteDestType_Object = MibTableColumn
vRtrIsisInetRouteDestType = _VRtrIsisInetRouteDestType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 1),
    _VRtrIsisInetRouteDestType_Type()
)
vRtrIsisInetRouteDestType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteDestType.setStatus("current")
_VRtrIsisInetRouteDest_Type = InetAddress
_VRtrIsisInetRouteDest_Object = MibTableColumn
vRtrIsisInetRouteDest = _VRtrIsisInetRouteDest_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 2),
    _VRtrIsisInetRouteDest_Type()
)
vRtrIsisInetRouteDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteDest.setStatus("current")
_VRtrIsisInetRoutePrefixLength_Type = InetAddressPrefixLength
_VRtrIsisInetRoutePrefixLength_Object = MibTableColumn
vRtrIsisInetRoutePrefixLength = _VRtrIsisInetRoutePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 3),
    _VRtrIsisInetRoutePrefixLength_Type()
)
vRtrIsisInetRoutePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRoutePrefixLength.setStatus("current")
_VRtrIsisInetRouteNexthopIPType_Type = InetAddressType
_VRtrIsisInetRouteNexthopIPType_Object = MibTableColumn
vRtrIsisInetRouteNexthopIPType = _VRtrIsisInetRouteNexthopIPType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 4),
    _VRtrIsisInetRouteNexthopIPType_Type()
)
vRtrIsisInetRouteNexthopIPType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteNexthopIPType.setStatus("current")
_VRtrIsisInetRouteNexthopIP_Type = InetAddress
_VRtrIsisInetRouteNexthopIP_Object = MibTableColumn
vRtrIsisInetRouteNexthopIP = _VRtrIsisInetRouteNexthopIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 5),
    _VRtrIsisInetRouteNexthopIP_Type()
)
vRtrIsisInetRouteNexthopIP.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteNexthopIP.setStatus("current")


class _VRtrIsisInetRouteLevel_Type(Integer32):
    """Custom type vRtrIsisInetRouteLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1IS", 1),
          ("level2IS", 2))
    )


_VRtrIsisInetRouteLevel_Type.__name__ = "Integer32"
_VRtrIsisInetRouteLevel_Object = MibTableColumn
vRtrIsisInetRouteLevel = _VRtrIsisInetRouteLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 6),
    _VRtrIsisInetRouteLevel_Type()
)
vRtrIsisInetRouteLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteLevel.setStatus("current")
_VRtrIsisInetRouteSpfRunNumber_Type = Counter32
_VRtrIsisInetRouteSpfRunNumber_Object = MibTableColumn
vRtrIsisInetRouteSpfRunNumber = _VRtrIsisInetRouteSpfRunNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 7),
    _VRtrIsisInetRouteSpfRunNumber_Type()
)
vRtrIsisInetRouteSpfRunNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteSpfRunNumber.setStatus("current")
_VRtrIsisInetRouteMetric_Type = Unsigned32
_VRtrIsisInetRouteMetric_Object = MibTableColumn
vRtrIsisInetRouteMetric = _VRtrIsisInetRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 8),
    _VRtrIsisInetRouteMetric_Type()
)
vRtrIsisInetRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteMetric.setStatus("current")


class _VRtrIsisInetRouteType_Type(Integer32):
    """Custom type vRtrIsisInetRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1))
    )


_VRtrIsisInetRouteType_Type.__name__ = "Integer32"
_VRtrIsisInetRouteType_Object = MibTableColumn
vRtrIsisInetRouteType = _VRtrIsisInetRouteType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 9),
    _VRtrIsisInetRouteType_Type()
)
vRtrIsisInetRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteType.setStatus("current")
_VRtrIsisInetRouteNHopSysID_Type = SystemID
_VRtrIsisInetRouteNHopSysID_Object = MibTableColumn
vRtrIsisInetRouteNHopSysID = _VRtrIsisInetRouteNHopSysID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 10, 1, 10),
    _VRtrIsisInetRouteNHopSysID_Type()
)
vRtrIsisInetRouteNHopSysID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisInetRouteNHopSysID.setStatus("current")
_VRtrIsisInetSummaryTable_Object = MibTable
vRtrIsisInetSummaryTable = _VRtrIsisInetSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11)
)
if mibBuilder.loadTexts:
    vRtrIsisInetSummaryTable.setStatus("current")
_VRtrIsisInetSummaryEntry_Object = MibTableRow
vRtrIsisInetSummaryEntry = _VRtrIsisInetSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11, 1)
)
vRtrIsisInetSummaryEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetSummPrefixType"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetSummPrefix"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisInetSummPrefixLength"),
)
if mibBuilder.loadTexts:
    vRtrIsisInetSummaryEntry.setStatus("current")
_VRtrIsisInetSummPrefixType_Type = InetAddressType
_VRtrIsisInetSummPrefixType_Object = MibTableColumn
vRtrIsisInetSummPrefixType = _VRtrIsisInetSummPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11, 1, 1),
    _VRtrIsisInetSummPrefixType_Type()
)
vRtrIsisInetSummPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetSummPrefixType.setStatus("current")
_VRtrIsisInetSummPrefix_Type = InetAddress
_VRtrIsisInetSummPrefix_Object = MibTableColumn
vRtrIsisInetSummPrefix = _VRtrIsisInetSummPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11, 1, 2),
    _VRtrIsisInetSummPrefix_Type()
)
vRtrIsisInetSummPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetSummPrefix.setStatus("current")
_VRtrIsisInetSummPrefixLength_Type = InetAddressPrefixLength
_VRtrIsisInetSummPrefixLength_Object = MibTableColumn
vRtrIsisInetSummPrefixLength = _VRtrIsisInetSummPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11, 1, 3),
    _VRtrIsisInetSummPrefixLength_Type()
)
vRtrIsisInetSummPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisInetSummPrefixLength.setStatus("current")
_VRtrIsisInetSummRowStatus_Type = RowStatus
_VRtrIsisInetSummRowStatus_Object = MibTableColumn
vRtrIsisInetSummRowStatus = _VRtrIsisInetSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11, 1, 4),
    _VRtrIsisInetSummRowStatus_Type()
)
vRtrIsisInetSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisInetSummRowStatus.setStatus("current")


class _VRtrIsisInetSummLevel_Type(Integer32):
    """Custom type vRtrIsisInetSummLevel based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level1L2", 3),
          ("level2", 2))
    )


_VRtrIsisInetSummLevel_Type.__name__ = "Integer32"
_VRtrIsisInetSummLevel_Object = MibTableColumn
vRtrIsisInetSummLevel = _VRtrIsisInetSummLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 2, 11, 1, 5),
    _VRtrIsisInetSummLevel_Type()
)
vRtrIsisInetSummLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisInetSummLevel.setStatus("current")
_VRtrIsisIfObjs_ObjectIdentity = ObjectIdentity
vRtrIsisIfObjs = _VRtrIsisIfObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3)
)
_VRtrIsisIfTable_Object = MibTable
vRtrIsisIfTable = _VRtrIsisIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisIfTable.setStatus("current")
_VRtrIsisIfEntry_Object = MibTableRow
vRtrIsisIfEntry = _VRtrIsisIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1)
)
vRtrIsisIfEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrIsisIfEntry.setStatus("current")
_VRtrIsisIfIndex_Type = InterfaceIndex
_VRtrIsisIfIndex_Object = MibTableColumn
vRtrIsisIfIndex = _VRtrIsisIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 1),
    _VRtrIsisIfIndex_Type()
)
vRtrIsisIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisIfIndex.setStatus("current")
_VRtrIsisIfRowStatus_Type = RowStatus
_VRtrIsisIfRowStatus_Object = MibTableColumn
vRtrIsisIfRowStatus = _VRtrIsisIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 2),
    _VRtrIsisIfRowStatus_Type()
)
vRtrIsisIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfRowStatus.setStatus("current")
_VRtrIsisIfLastChangeTime_Type = TimeStamp
_VRtrIsisIfLastChangeTime_Object = MibTableColumn
vRtrIsisIfLastChangeTime = _VRtrIsisIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 3),
    _VRtrIsisIfLastChangeTime_Type()
)
vRtrIsisIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLastChangeTime.setStatus("current")


class _VRtrIsisIfAdminState_Type(TmnxAdminState):
    """Custom type vRtrIsisIfAdminState based on TmnxAdminState"""


_VRtrIsisIfAdminState_Object = MibTableColumn
vRtrIsisIfAdminState = _VRtrIsisIfAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 4),
    _VRtrIsisIfAdminState_Type()
)
vRtrIsisIfAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfAdminState.setStatus("current")
_VRtrIsisIfOperState_Type = TmnxOperState
_VRtrIsisIfOperState_Object = MibTableColumn
vRtrIsisIfOperState = _VRtrIsisIfOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 5),
    _VRtrIsisIfOperState_Type()
)
vRtrIsisIfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfOperState.setStatus("current")


class _VRtrIsisIfCsnpInterval_Type(Unsigned32):
    """Custom type vRtrIsisIfCsnpInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrIsisIfCsnpInterval_Type.__name__ = "Unsigned32"
_VRtrIsisIfCsnpInterval_Object = MibTableColumn
vRtrIsisIfCsnpInterval = _VRtrIsisIfCsnpInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 6),
    _VRtrIsisIfCsnpInterval_Type()
)
vRtrIsisIfCsnpInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfCsnpInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisIfCsnpInterval.setUnits("seconds")


class _VRtrIsisIfHelloAuthKey_Type(OctetString):
    """Custom type vRtrIsisIfHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 118),
    )


_VRtrIsisIfHelloAuthKey_Type.__name__ = "OctetString"
_VRtrIsisIfHelloAuthKey_Object = MibTableColumn
vRtrIsisIfHelloAuthKey = _VRtrIsisIfHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 7),
    _VRtrIsisIfHelloAuthKey_Type()
)
vRtrIsisIfHelloAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfHelloAuthKey.setStatus("current")


class _VRtrIsisIfHelloAuthType_Type(Integer32):
    """Custom type vRtrIsisIfHelloAuthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("md5", 3),
          ("none", 1),
          ("password", 2))
    )


_VRtrIsisIfHelloAuthType_Type.__name__ = "Integer32"
_VRtrIsisIfHelloAuthType_Object = MibTableColumn
vRtrIsisIfHelloAuthType = _VRtrIsisIfHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 8),
    _VRtrIsisIfHelloAuthType_Type()
)
vRtrIsisIfHelloAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfHelloAuthType.setStatus("current")


class _VRtrIsisIfLspPacingInterval_Type(Unsigned32):
    """Custom type vRtrIsisIfLspPacingInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VRtrIsisIfLspPacingInterval_Type.__name__ = "Unsigned32"
_VRtrIsisIfLspPacingInterval_Object = MibTableColumn
vRtrIsisIfLspPacingInterval = _VRtrIsisIfLspPacingInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 9),
    _VRtrIsisIfLspPacingInterval_Type()
)
vRtrIsisIfLspPacingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLspPacingInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisIfLspPacingInterval.setUnits("milliseconds")


class _VRtrIsisIfCircIndex_Type(Integer32):
    """Custom type vRtrIsisIfCircIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000000000),
    )


_VRtrIsisIfCircIndex_Type.__name__ = "Integer32"
_VRtrIsisIfCircIndex_Object = MibTableColumn
vRtrIsisIfCircIndex = _VRtrIsisIfCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 10),
    _VRtrIsisIfCircIndex_Type()
)
vRtrIsisIfCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfCircIndex.setStatus("current")


class _VRtrIsisIfRetransmitInterval_Type(Unsigned32):
    """Custom type vRtrIsisIfRetransmitInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrIsisIfRetransmitInterval_Type.__name__ = "Unsigned32"
_VRtrIsisIfRetransmitInterval_Object = MibTableColumn
vRtrIsisIfRetransmitInterval = _VRtrIsisIfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 11),
    _VRtrIsisIfRetransmitInterval_Type()
)
vRtrIsisIfRetransmitInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfRetransmitInterval.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisIfRetransmitInterval.setUnits("seconds")


class _VRtrIsisIfTypeDefault_Type(TruthValue):
    """Custom type vRtrIsisIfTypeDefault based on TruthValue"""


_VRtrIsisIfTypeDefault_Object = MibTableColumn
vRtrIsisIfTypeDefault = _VRtrIsisIfTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 1, 1, 12),
    _VRtrIsisIfTypeDefault_Type()
)
vRtrIsisIfTypeDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfTypeDefault.setStatus("current")
_VRtrIsisIfLevelTable_Object = MibTable
vRtrIsisIfLevelTable = _VRtrIsisIfLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2)
)
if mibBuilder.loadTexts:
    vRtrIsisIfLevelTable.setStatus("current")
_VRtrIsisIfLevelEntry_Object = MibTableRow
vRtrIsisIfLevelEntry = _VRtrIsisIfLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1)
)
vRtrIsisIfLevelEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisIfLevel"),
)
if mibBuilder.loadTexts:
    vRtrIsisIfLevelEntry.setStatus("current")


class _VRtrIsisIfLevel_Type(Integer32):
    """Custom type vRtrIsisIfLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2))
    )


_VRtrIsisIfLevel_Type.__name__ = "Integer32"
_VRtrIsisIfLevel_Object = MibTableColumn
vRtrIsisIfLevel = _VRtrIsisIfLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 1),
    _VRtrIsisIfLevel_Type()
)
vRtrIsisIfLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrIsisIfLevel.setStatus("current")
_VRtrIsisIfLevelLastChangeTime_Type = TimeStamp
_VRtrIsisIfLevelLastChangeTime_Object = MibTableColumn
vRtrIsisIfLevelLastChangeTime = _VRtrIsisIfLevelLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 2),
    _VRtrIsisIfLevelLastChangeTime_Type()
)
vRtrIsisIfLevelLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelLastChangeTime.setStatus("current")


class _VRtrIsisIfLevelHelloAuthKey_Type(OctetString):
    """Custom type vRtrIsisIfLevelHelloAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 118),
    )


_VRtrIsisIfLevelHelloAuthKey_Type.__name__ = "OctetString"
_VRtrIsisIfLevelHelloAuthKey_Object = MibTableColumn
vRtrIsisIfLevelHelloAuthKey = _VRtrIsisIfLevelHelloAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 3),
    _VRtrIsisIfLevelHelloAuthKey_Type()
)
vRtrIsisIfLevelHelloAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelHelloAuthKey.setStatus("current")


class _VRtrIsisIfLevelHelloAuthType_Type(Integer32):
    """Custom type vRtrIsisIfLevelHelloAuthType based on Integer32"""
    defaultValue = 0

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
        *(("md5", 3),
          ("none", 1),
          ("password", 2),
          ("useGlobal", 0))
    )


_VRtrIsisIfLevelHelloAuthType_Type.__name__ = "Integer32"
_VRtrIsisIfLevelHelloAuthType_Object = MibTableColumn
vRtrIsisIfLevelHelloAuthType = _VRtrIsisIfLevelHelloAuthType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 4),
    _VRtrIsisIfLevelHelloAuthType_Type()
)
vRtrIsisIfLevelHelloAuthType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelHelloAuthType.setStatus("current")


class _VRtrIsisIfLevelPassive_Type(TruthValue):
    """Custom type vRtrIsisIfLevelPassive based on TruthValue"""


_VRtrIsisIfLevelPassive_Object = MibTableColumn
vRtrIsisIfLevelPassive = _VRtrIsisIfLevelPassive_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 5),
    _VRtrIsisIfLevelPassive_Type()
)
vRtrIsisIfLevelPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelPassive.setStatus("current")


class _VRtrIsisIfLevelTeMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelTeMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4261412864),
    )


_VRtrIsisIfLevelTeMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelTeMetric_Object = MibTableColumn
vRtrIsisIfLevelTeMetric = _VRtrIsisIfLevelTeMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 6),
    _VRtrIsisIfLevelTeMetric_Type()
)
vRtrIsisIfLevelTeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelTeMetric.setStatus("current")
_VRtrIsisIfLevelNumAdjacencies_Type = Unsigned32
_VRtrIsisIfLevelNumAdjacencies_Object = MibTableColumn
vRtrIsisIfLevelNumAdjacencies = _VRtrIsisIfLevelNumAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 7),
    _VRtrIsisIfLevelNumAdjacencies_Type()
)
vRtrIsisIfLevelNumAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelNumAdjacencies.setStatus("current")


class _VRtrIsisIfLevelISPriority_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelISPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_VRtrIsisIfLevelISPriority_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelISPriority_Object = MibTableColumn
vRtrIsisIfLevelISPriority = _VRtrIsisIfLevelISPriority_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 8),
    _VRtrIsisIfLevelISPriority_Type()
)
vRtrIsisIfLevelISPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelISPriority.setStatus("current")


class _VRtrIsisIfLevelHelloTimer_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelHelloTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20000),
    )


_VRtrIsisIfLevelHelloTimer_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelHelloTimer_Object = MibTableColumn
vRtrIsisIfLevelHelloTimer = _VRtrIsisIfLevelHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 9),
    _VRtrIsisIfLevelHelloTimer_Type()
)
vRtrIsisIfLevelHelloTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelHelloTimer.setStatus("current")


class _VRtrIsisIfLevelAdminMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelAdminMetric based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_VRtrIsisIfLevelAdminMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelAdminMetric_Object = MibTableColumn
vRtrIsisIfLevelAdminMetric = _VRtrIsisIfLevelAdminMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 10),
    _VRtrIsisIfLevelAdminMetric_Type()
)
vRtrIsisIfLevelAdminMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelAdminMetric.setStatus("current")


class _VRtrIsisIfLevelOperMetric_Type(Unsigned32):
    """Custom type vRtrIsisIfLevelOperMetric based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )


_VRtrIsisIfLevelOperMetric_Type.__name__ = "Unsigned32"
_VRtrIsisIfLevelOperMetric_Object = MibTableColumn
vRtrIsisIfLevelOperMetric = _VRtrIsisIfLevelOperMetric_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 3, 2, 1, 11),
    _VRtrIsisIfLevelOperMetric_Type()
)
vRtrIsisIfLevelOperMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisIfLevelOperMetric.setStatus("current")
_VRtrIsisAdjObjs_ObjectIdentity = ObjectIdentity
vRtrIsisAdjObjs = _VRtrIsisAdjObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4)
)
_VRtrIsisISAdjTable_Object = MibTable
vRtrIsisISAdjTable = _VRtrIsisISAdjTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisISAdjTable.setStatus("current")
_VRtrIsisISAdjEntry_Object = MibTableRow
vRtrIsisISAdjEntry = _VRtrIsisISAdjEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisISAdjEntry.setStatus("current")


class _VRtrIsisISAdjExpiresIn_Type(Integer32):
    """Custom type vRtrIsisISAdjExpiresIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_VRtrIsisISAdjExpiresIn_Type.__name__ = "Integer32"
_VRtrIsisISAdjExpiresIn_Object = MibTableColumn
vRtrIsisISAdjExpiresIn = _VRtrIsisISAdjExpiresIn_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 1),
    _VRtrIsisISAdjExpiresIn_Type()
)
vRtrIsisISAdjExpiresIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjExpiresIn.setStatus("current")
if mibBuilder.loadTexts:
    vRtrIsisISAdjExpiresIn.setUnits("seconds")


class _VRtrIsisISAdjCircLevel_Type(Integer32):
    """Custom type vRtrIsisISAdjCircLevel based on Integer32"""
    defaultValue = 4

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
        *(("level1", 1),
          ("level1L2", 3),
          ("level2", 2),
          ("unknown", 4))
    )


_VRtrIsisISAdjCircLevel_Type.__name__ = "Integer32"
_VRtrIsisISAdjCircLevel_Object = MibTableColumn
vRtrIsisISAdjCircLevel = _VRtrIsisISAdjCircLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 2),
    _VRtrIsisISAdjCircLevel_Type()
)
vRtrIsisISAdjCircLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjCircLevel.setStatus("current")
_VRtrIsisISAdjNeighborIP_Type = IpAddress
_VRtrIsisISAdjNeighborIP_Object = MibTableColumn
vRtrIsisISAdjNeighborIP = _VRtrIsisISAdjNeighborIP_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 3),
    _VRtrIsisISAdjNeighborIP_Type()
)
vRtrIsisISAdjNeighborIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNeighborIP.setStatus("current")
_VRtrIsisISAdjRestartSupport_Type = TruthValue
_VRtrIsisISAdjRestartSupport_Object = MibTableColumn
vRtrIsisISAdjRestartSupport = _VRtrIsisISAdjRestartSupport_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 4),
    _VRtrIsisISAdjRestartSupport_Type()
)
vRtrIsisISAdjRestartSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjRestartSupport.setStatus("current")


class _VRtrIsisISAdjRestartStatus_Type(Integer32):
    """Custom type vRtrIsisISAdjRestartStatus based on Integer32"""
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
        *(("helping", 4),
          ("notHelping", 1),
          ("restart-complete", 3),
          ("restarting", 2))
    )


_VRtrIsisISAdjRestartStatus_Type.__name__ = "Integer32"
_VRtrIsisISAdjRestartStatus_Object = MibTableColumn
vRtrIsisISAdjRestartStatus = _VRtrIsisISAdjRestartStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 5),
    _VRtrIsisISAdjRestartStatus_Type()
)
vRtrIsisISAdjRestartStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjRestartStatus.setStatus("current")
_VRtrIsisISAdjRestartSupressed_Type = TruthValue
_VRtrIsisISAdjRestartSupressed_Object = MibTableColumn
vRtrIsisISAdjRestartSupressed = _VRtrIsisISAdjRestartSupressed_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 6),
    _VRtrIsisISAdjRestartSupressed_Type()
)
vRtrIsisISAdjRestartSupressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjRestartSupressed.setStatus("current")
_VRtrIsisISAdjNumRestarts_Type = Unsigned32
_VRtrIsisISAdjNumRestarts_Object = MibTableColumn
vRtrIsisISAdjNumRestarts = _VRtrIsisISAdjNumRestarts_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 7),
    _VRtrIsisISAdjNumRestarts_Type()
)
vRtrIsisISAdjNumRestarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNumRestarts.setStatus("current")
_VRtrIsisISAdjLastRestartTime_Type = TimeStamp
_VRtrIsisISAdjLastRestartTime_Object = MibTableColumn
vRtrIsisISAdjLastRestartTime = _VRtrIsisISAdjLastRestartTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 8),
    _VRtrIsisISAdjLastRestartTime_Type()
)
vRtrIsisISAdjLastRestartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjLastRestartTime.setStatus("current")
_VRtrIsisISAdjNeighborIPv6Type_Type = InetAddressType
_VRtrIsisISAdjNeighborIPv6Type_Object = MibTableColumn
vRtrIsisISAdjNeighborIPv6Type = _VRtrIsisISAdjNeighborIPv6Type_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 9),
    _VRtrIsisISAdjNeighborIPv6Type_Type()
)
vRtrIsisISAdjNeighborIPv6Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNeighborIPv6Type.setStatus("current")
_VRtrIsisISAdjNeighborIpv6_Type = InetAddress
_VRtrIsisISAdjNeighborIpv6_Object = MibTableColumn
vRtrIsisISAdjNeighborIpv6 = _VRtrIsisISAdjNeighborIpv6_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 4, 1, 1, 10),
    _VRtrIsisISAdjNeighborIpv6_Type()
)
vRtrIsisISAdjNeighborIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrIsisISAdjNeighborIpv6.setStatus("current")
_VRtrIsisNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrIsisNotificationObjs = _VRtrIsisNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5)
)
_VRtrIsisNotificationTable_Object = MibTable
vRtrIsisNotificationTable = _VRtrIsisNotificationTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationTable.setStatus("current")
_VRtrIsisNotificationEntry_Object = MibTableRow
vRtrIsisNotificationEntry = _VRtrIsisNotificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1)
)
vRtrIsisNotificationEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationEntry.setStatus("current")


class _VRtrIsisTrapLSPID_Type(OctetString):
    """Custom type vRtrIsisTrapLSPID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(8, 8),
    )


_VRtrIsisTrapLSPID_Type.__name__ = "OctetString"
_VRtrIsisTrapLSPID_Object = MibTableColumn
vRtrIsisTrapLSPID = _VRtrIsisTrapLSPID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 1),
    _VRtrIsisTrapLSPID_Type()
)
vRtrIsisTrapLSPID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisTrapLSPID.setStatus("current")


class _VRtrIsisSystemLevel_Type(Integer32):
    """Custom type vRtrIsisSystemLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("l1", 1),
          ("l1l2", 3),
          ("l2", 2))
    )


_VRtrIsisSystemLevel_Type.__name__ = "Integer32"
_VRtrIsisSystemLevel_Object = MibTableColumn
vRtrIsisSystemLevel = _VRtrIsisSystemLevel_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 2),
    _VRtrIsisSystemLevel_Type()
)
vRtrIsisSystemLevel.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisSystemLevel.setStatus("current")


class _VRtrIsisPDUFragment_Type(OctetString):
    """Custom type vRtrIsisPDUFragment based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_VRtrIsisPDUFragment_Type.__name__ = "OctetString"
_VRtrIsisPDUFragment_Object = MibTableColumn
vRtrIsisPDUFragment = _VRtrIsisPDUFragment_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 3),
    _VRtrIsisPDUFragment_Type()
)
vRtrIsisPDUFragment.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisPDUFragment.setStatus("current")


class _VRtrIsisFieldLen_Type(Integer32):
    """Custom type vRtrIsisFieldLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIsisFieldLen_Type.__name__ = "Integer32"
_VRtrIsisFieldLen_Object = MibTableColumn
vRtrIsisFieldLen = _VRtrIsisFieldLen_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 4),
    _VRtrIsisFieldLen_Type()
)
vRtrIsisFieldLen.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisFieldLen.setStatus("current")


class _VRtrIsisMaxAreaAddress_Type(Integer32):
    """Custom type vRtrIsisMaxAreaAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIsisMaxAreaAddress_Type.__name__ = "Integer32"
_VRtrIsisMaxAreaAddress_Object = MibTableColumn
vRtrIsisMaxAreaAddress = _VRtrIsisMaxAreaAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 5),
    _VRtrIsisMaxAreaAddress_Type()
)
vRtrIsisMaxAreaAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisMaxAreaAddress.setStatus("current")


class _VRtrIsisProtocolVersion_Type(Integer32):
    """Custom type vRtrIsisProtocolVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrIsisProtocolVersion_Type.__name__ = "Integer32"
_VRtrIsisProtocolVersion_Object = MibTableColumn
vRtrIsisProtocolVersion = _VRtrIsisProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 6),
    _VRtrIsisProtocolVersion_Type()
)
vRtrIsisProtocolVersion.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisProtocolVersion.setStatus("current")


class _VRtrIsisLSPSize_Type(Integer32):
    """Custom type vRtrIsisLSPSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIsisLSPSize_Type.__name__ = "Integer32"
_VRtrIsisLSPSize_Object = MibTableColumn
vRtrIsisLSPSize = _VRtrIsisLSPSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 7),
    _VRtrIsisLSPSize_Type()
)
vRtrIsisLSPSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisLSPSize.setStatus("current")


class _VRtrIsisOriginatingBufferSize_Type(Integer32):
    """Custom type vRtrIsisOriginatingBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_VRtrIsisOriginatingBufferSize_Type.__name__ = "Integer32"
_VRtrIsisOriginatingBufferSize_Object = MibTableColumn
vRtrIsisOriginatingBufferSize = _VRtrIsisOriginatingBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 8),
    _VRtrIsisOriginatingBufferSize_Type()
)
vRtrIsisOriginatingBufferSize.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisOriginatingBufferSize.setStatus("current")


class _VRtrIsisProtocolsSupported_Type(OctetString):
    """Custom type vRtrIsisProtocolsSupported based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VRtrIsisProtocolsSupported_Type.__name__ = "OctetString"
_VRtrIsisProtocolsSupported_Object = MibTableColumn
vRtrIsisProtocolsSupported = _VRtrIsisProtocolsSupported_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 5, 1, 1, 9),
    _VRtrIsisProtocolsSupported_Type()
)
vRtrIsisProtocolsSupported.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrIsisProtocolsSupported.setStatus("current")
_VRtrIsisDatabaseClearObjs_ObjectIdentity = ObjectIdentity
vRtrIsisDatabaseClearObjs = _VRtrIsisDatabaseClearObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 6)
)
_VRtrIsisDatabaseClearTable_Object = MibTable
vRtrIsisDatabaseClearTable = _VRtrIsisDatabaseClearTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 6, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisDatabaseClearTable.setStatus("current")
_VRtrIsisDatabaseClearEntry_Object = MibTableRow
vRtrIsisDatabaseClearEntry = _VRtrIsisDatabaseClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 6, 1, 1)
)
vRtrIsisDatabaseClearEntry.setIndexNames(
    (0, "ISIS-MIB", "isisSysInstance"),
    (0, "ALCATEL-ISIS-MIB", "vRtrIsisSysID"),
)
if mibBuilder.loadTexts:
    vRtrIsisDatabaseClearEntry.setStatus("current")


class _VRtrIsisAdjDatabaseClear_Type(Integer32):
    """Custom type vRtrIsisAdjDatabaseClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VRtrIsisAdjDatabaseClear_Type.__name__ = "Integer32"
_VRtrIsisAdjDatabaseClear_Object = MibTableColumn
vRtrIsisAdjDatabaseClear = _VRtrIsisAdjDatabaseClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 6, 1, 1, 1),
    _VRtrIsisAdjDatabaseClear_Type()
)
vRtrIsisAdjDatabaseClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisAdjDatabaseClear.setStatus("current")


class _VRtrIsisLSPDatabaseClear_Type(Integer32):
    """Custom type vRtrIsisLSPDatabaseClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("reset", 1))
    )


_VRtrIsisLSPDatabaseClear_Type.__name__ = "Integer32"
_VRtrIsisLSPDatabaseClear_Object = MibTableColumn
vRtrIsisLSPDatabaseClear = _VRtrIsisLSPDatabaseClear_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 10, 6, 1, 1, 2),
    _VRtrIsisLSPDatabaseClear_Type()
)
vRtrIsisLSPDatabaseClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vRtrIsisLSPDatabaseClear.setStatus("current")
_VRtrIsisNotifications_ObjectIdentity = ObjectIdentity
vRtrIsisNotifications = _VRtrIsisNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11)
)
_VRtrIsisMIBConformance_ObjectIdentity = ObjectIdentity
vRtrIsisMIBConformance = _VRtrIsisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12)
)
_VRtrIsisMIBConformances_ObjectIdentity = ObjectIdentity
vRtrIsisMIBConformances = _VRtrIsisMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 1)
)
_VRtrIsisMIBGroups_ObjectIdentity = ObjectIdentity
vRtrIsisMIBGroups = _VRtrIsisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2)
)
isisISAdjEntry.registerAugmentions(
    ("ALCATEL-ISIS-MIB",
     "vRtrIsisISAdjEntry")
)
vRtrIsisISAdjEntry.setIndexNames(*isisISAdjEntry.getIndexNames())

# Managed Objects groups

vRtrIsisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 1)
)
vRtrIsisGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOperState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisShortCuts"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"))
)
if mibBuilder.loadTexts:
    vRtrIsisGroup.setStatus("obsolete")

vRtrIsisHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 2)
)
vRtrIsisHostGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSysID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisHostname"))
)
if mibBuilder.loadTexts:
    vRtrIsisHostGroup.setStatus("current")

vRtrIsisRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 3)
)
vRtrIsisRouteGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisRouteDest"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteMask"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteNexthopIP"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteSpfVersion"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteNHopSysID"))
)
if mibBuilder.loadTexts:
    vRtrIsisRouteGroup.setStatus("obsolete")

vRtrIsisPathGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 4)
)
vRtrIsisPathGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisPathID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPathIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPathNHopSysID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPathMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPathSNPA"))
)
if mibBuilder.loadTexts:
    vRtrIsisPathGroup.setStatus("current")

vRtrIsisLSPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 5)
)
vRtrIsisLSPGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLSPId"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSeq"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPChecksum"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPLifetimeRemain"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPVersion"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPPktType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPPktVersion"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPMaxArea"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSysIdLen"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPAttributes"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPUsedLen"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPAllocLen"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPBuff"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPZeroRLT"))
)
if mibBuilder.loadTexts:
    vRtrIsisLSPGroup.setStatus("current")

vRtrIsisIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 6)
)
vRtrIsisIfGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisIfRowStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLastChangeTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfAdminState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfOperState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfCsnpInterval"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfHelloAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfHelloAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLspPacingInterval"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfCircIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfRetransmitInterval"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfTypeDefault"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelLastChangeTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelHelloAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelHelloAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelPassive"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelTeMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelNumAdjacencies"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelISPriority"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelHelloTimer"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelAdminMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelOperMetric"))
)
if mibBuilder.loadTexts:
    vRtrIsisIfGroup.setStatus("obsolete")

vRtrIsisAdjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 7)
)
vRtrIsisAdjGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisISAdjExpiresIn"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjCircLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNeighborIP"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjGroup.setStatus("obsolete")

vRtrIsisNotificationObjGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 8)
)
vRtrIsisNotificationObjGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisFieldLen"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisMaxAreaAddress"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisProtocolVersion"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSize"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOriginatingBufferSize"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisProtocolsSupported"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationObjGroup.setStatus("current")

vRtrIsisSpfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 10)
)
vRtrIsisSpfGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSpfRunTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfL1Nodes"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfL2Nodes"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfEventCount"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfLastTriggerLSPId"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfTriggerReason"))
)
if mibBuilder.loadTexts:
    vRtrIsisSpfGroup.setStatus("current")

vRtrIsisSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 11)
)
vRtrIsisSummaryGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSummRowStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSummLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryGroup.setStatus("obsolete")

vRtrIsisR2r1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 12)
)
vRtrIsisR2r1Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOperState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisShortCuts"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisHelloAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelCsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelHelloAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelPsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"))
)
if mibBuilder.loadTexts:
    vRtrIsisR2r1Group.setStatus("obsolete")

vRtrIsisV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 13)
)
vRtrIsisV3v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOperState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisShortCuts"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisHelloAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGRRestartDuration"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGRHelperMode"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelCsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelHelloAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelPsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"))
)
if mibBuilder.loadTexts:
    vRtrIsisV3v0Group.setStatus("obsolete")

vRtrIsisAdjV3v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 14)
)
vRtrIsisAdjV3v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisISAdjExpiresIn"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjCircLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNeighborIP"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartSupport"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartSupressed"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNumRestarts"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjLastRestartTime"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjV3v0Group.setStatus("obsolete")

vRtrIsisV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 16)
)
vRtrIsisV4v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLastEnabledTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthCheck"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspLifetime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOperState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisShortCuts"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfHoldTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLastSpfRun"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGracefulRestart"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBoot"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOverloadOnBootTimeout"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspMaxWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspInitialWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLspSecondWait"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisHelloAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGRRestartDuration"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisGRHelperMode"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisStrictAdjacencyCheck"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelWideMetricsOnly"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelOverloadTimeLeft"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelNumLSPs"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelCsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelHelloAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLevelPsnpAuthentication"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfRuns"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRegenerations"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInitiatedPurges"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIIHRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPSNPRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRecd"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownDrop"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownSent"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisUnknownRetrans"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFDroppedRequests"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsFound"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCSPFPathsNotFound"))
)
if mibBuilder.loadTexts:
    vRtrIsisV4v0Group.setStatus("current")

vRtrIsisRouteV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 17)
)
vRtrIsisRouteV4v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisRouteDest"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteMask"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteNexthopIP"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteSpfVersion"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRouteNHopSysID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetRouteLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetRouteSpfRunNumber"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetRouteMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetRouteType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetRouteNHopSysID"))
)
if mibBuilder.loadTexts:
    vRtrIsisRouteV4v0Group.setStatus("current")

vRtrIsisSummaryV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 18)
)
vRtrIsisSummaryV4v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSummRowStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSummLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetSummRowStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisInetSummLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisSummaryV4v0Group.setStatus("current")

vRtrIsisAdjV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 19)
)
vRtrIsisAdjV4v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisISAdjExpiresIn"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjCircLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNeighborIP"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartSupport"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartSupressed"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNumRestarts"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjLastRestartTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNeighborIPv6Type"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjNeighborIpv6"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjV4v0Group.setStatus("current")

vRtrIsisIfV4v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 20)
)
vRtrIsisIfV4v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisIfRowStatus"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLastChangeTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfAdminState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfOperState"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfCsnpInterval"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfHelloAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfHelloAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLspPacingInterval"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfCircIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfRetransmitInterval"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfTypeDefault"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelLastChangeTime"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelHelloAuthKey"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelHelloAuthType"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelPassive"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelTeMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelNumAdjacencies"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelISPriority"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelHelloTimer"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelAdminMetric"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfLevelOperMetric"))
)
if mibBuilder.loadTexts:
    vRtrIsisIfV4v0Group.setStatus("current")

vRtrIsisScalarObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 21)
)
vRtrIsisScalarObjsGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisStatisticsClear"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPClear"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjClear"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSpfClear"))
)
if mibBuilder.loadTexts:
    vRtrIsisScalarObjsGroup.setStatus("current")

vRtrIsisDBClearObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 22)
)
vRtrIsisDBClearObjsGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisAdjDatabaseClear"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPDatabaseClear"))
)
if mibBuilder.loadTexts:
    vRtrIsisDBClearObjsGroup.setStatus("current")


# Notification objects

vRtrIsisDatabaseOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 1)
)
vRtrIsisDatabaseOverload.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ISIS-MIB", "isisSysL1State"),
        ("ISIS-MIB", "isisSysL2State"))
)
if mibBuilder.loadTexts:
    vRtrIsisDatabaseOverload.setStatus(
        "current"
    )

vRtrIsisManualAddressDrops = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 2)
)
vRtrIsisManualAddressDrops.setObjects(
    ("ISIS-MIB", "isisManAreaAddrExistState")
)
if mibBuilder.loadTexts:
    vRtrIsisManualAddressDrops.setStatus(
        "current"
    )

vRtrIsisCorruptedLSPDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 3)
)
vRtrIsisCorruptedLSPDetected.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"))
)
if mibBuilder.loadTexts:
    vRtrIsisCorruptedLSPDetected.setStatus(
        "current"
    )

vRtrIsisMaxSeqExceedAttempt = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 4)
)
vRtrIsisMaxSeqExceedAttempt.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"))
)
if mibBuilder.loadTexts:
    vRtrIsisMaxSeqExceedAttempt.setStatus(
        "current"
    )

vRtrIsisIDLenMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 5)
)
vRtrIsisIDLenMismatch.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisFieldLen"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"))
)
if mibBuilder.loadTexts:
    vRtrIsisIDLenMismatch.setStatus(
        "current"
    )

vRtrIsisMaxAreaAddrsMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 6)
)
vRtrIsisMaxAreaAddrsMismatch.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisMaxAreaAddress"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"))
)
if mibBuilder.loadTexts:
    vRtrIsisMaxAreaAddrsMismatch.setStatus(
        "current"
    )

vRtrIsisOwnLSPPurge = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 7)
)
vRtrIsisOwnLSPPurge.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisOwnLSPPurge.setStatus(
        "current"
    )

vRtrIsisSequenceNumberSkip = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 8)
)
vRtrIsisSequenceNumberSkip.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"))
)
if mibBuilder.loadTexts:
    vRtrIsisSequenceNumberSkip.setStatus(
        "current"
    )

vRtrIsisAutTypeFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 9)
)
vRtrIsisAutTypeFail.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisAutTypeFail.setStatus(
        "current"
    )

vRtrIsisAuthFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 10)
)
vRtrIsisAuthFail.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisAuthFail.setStatus(
        "current"
    )

vRtrIsisVersionSkew = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 11)
)
vRtrIsisVersionSkew.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisProtocolVersion"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisVersionSkew.setStatus(
        "current"
    )

vRtrIsisAreaMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 12)
)
vRtrIsisAreaMismatch.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLSPSize"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisPDUFragment"))
)
if mibBuilder.loadTexts:
    vRtrIsisAreaMismatch.setStatus(
        "current"
    )

vRtrIsisRejectedAdjacency = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 13)
)
vRtrIsisRejectedAdjacency.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisRejectedAdjacency.setStatus(
        "current"
    )

vRtrIsisLSPTooLargeToPropagate = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 14)
)
vRtrIsisLSPTooLargeToPropagate.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisLSPSize"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisLSPTooLargeToPropagate.setStatus(
        "current"
    )

vRtrIsisOrigLSPBufSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 15)
)
vRtrIsisOrigLSPBufSizeMismatch.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisOriginatingBufferSize"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisOrigLSPBufSizeMismatch.setStatus(
        "current"
    )

vRtrIsisProtoSuppMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 16)
)
vRtrIsisProtoSuppMismatch.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisProtocolsSupported"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrIsisProtoSuppMismatch.setStatus(
        "current"
    )

vRtrIsisAdjacencyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 17)
)
vRtrIsisAdjacencyChange.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisTrapLSPID"),
        ("ISIS-MIB", "isisISAdjState"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjacencyChange.setStatus(
        "current"
    )

vRtrIsisCircIdExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 18)
)
vRtrIsisCircIdExhausted.setObjects(
    ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex")
)
if mibBuilder.loadTexts:
    vRtrIsisCircIdExhausted.setStatus(
        "current"
    )

vRtrIsisAdjRestartStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 11, 0, 19)
)
vRtrIsisAdjRestartStatusChange.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisSystemLevel"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIfIndex"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisISAdjRestartStatus"))
)
if mibBuilder.loadTexts:
    vRtrIsisAdjRestartStatusChange.setStatus(
        "current"
    )


# Notifications groups

vRtrIsisNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 9)
)
vRtrIsisNotificationsGroup.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisDatabaseOverload"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisManualAddressDrops"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCorruptedLSPDetected"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisMaxSeqExceedAttempt"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIDLenMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisMaxAreaAddrsMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOwnLSPPurge"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSequenceNumberSkip"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAutTypeFail"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthFail"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisVersionSkew"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAreaMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRejectedAdjacency"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPTooLargeToPropagate"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOrigLSPBufSizeMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisProtoSuppMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAdjacencyChange"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCircIdExhausted"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationsGroup.setStatus(
        "obsolete"
    )

vRtrIsisNotificationV3v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 2, 15)
)
vRtrIsisNotificationV3v0Group.setObjects(
      *(("ALCATEL-ISIS-MIB", "vRtrIsisDatabaseOverload"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisManualAddressDrops"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCorruptedLSPDetected"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisMaxSeqExceedAttempt"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisIDLenMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisMaxAreaAddrsMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOwnLSPPurge"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisSequenceNumberSkip"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAutTypeFail"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAuthFail"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisVersionSkew"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAreaMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisRejectedAdjacency"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisLSPTooLargeToPropagate"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisOrigLSPBufSizeMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisProtoSuppMismatch"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAdjacencyChange"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisCircIdExhausted"),
        ("ALCATEL-ISIS-MIB", "vRtrIsisAdjRestartStatusChange"))
)
if mibBuilder.loadTexts:
    vRtrIsisNotificationV3v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

vRtrIsisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 1, 1)
)
if mibBuilder.loadTexts:
    vRtrIsisMIBCompliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBR2r1Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    vRtrIsisMIBR2r1Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV3v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 1, 3)
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV3v0Compliance.setStatus(
        "obsolete"
    )

vRtrIsisMIBV4v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 10, 14, 1, 12, 1, 4)
)
if mibBuilder.loadTexts:
    vRtrIsisMIBV4v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ISIS-MIB",
    **{"TmnxAdminState": TmnxAdminState,
       "TmnxOperState": TmnxOperState,
       "timetraIsisMIBModule": timetraIsisMIBModule,
       "vRtrIsisObjs": vRtrIsisObjs,
       "vRtrIsisScalarObjs": vRtrIsisScalarObjs,
       "vRtrIsisStatisticsClear": vRtrIsisStatisticsClear,
       "vRtrIsisLSPClear": vRtrIsisLSPClear,
       "vRtrIsisISAdjClear": vRtrIsisISAdjClear,
       "vRtrIsisSpfClear": vRtrIsisSpfClear,
       "vRtrIsisSystemObjs": vRtrIsisSystemObjs,
       "vRtrIsisTable": vRtrIsisTable,
       "vRtrIsisEntry": vRtrIsisEntry,
       "vRtrIsisLastEnabledTime": vRtrIsisLastEnabledTime,
       "vRtrIsisAuthKey": vRtrIsisAuthKey,
       "vRtrIsisAuthType": vRtrIsisAuthType,
       "vRtrIsisAuthCheck": vRtrIsisAuthCheck,
       "vRtrIsisLspLifetime": vRtrIsisLspLifetime,
       "vRtrIsisOverloadTimeout": vRtrIsisOverloadTimeout,
       "vRtrIsisOperState": vRtrIsisOperState,
       "vRtrIsisShortCuts": vRtrIsisShortCuts,
       "vRtrIsisSpfHoldTime": vRtrIsisSpfHoldTime,
       "vRtrIsisLastSpfRun": vRtrIsisLastSpfRun,
       "vRtrIsisGracefulRestart": vRtrIsisGracefulRestart,
       "vRtrIsisOverloadOnBoot": vRtrIsisOverloadOnBoot,
       "vRtrIsisOverloadOnBootTimeout": vRtrIsisOverloadOnBootTimeout,
       "vRtrIsisSpfWait": vRtrIsisSpfWait,
       "vRtrIsisSpfInitialWait": vRtrIsisSpfInitialWait,
       "vRtrIsisSpfSecondWait": vRtrIsisSpfSecondWait,
       "vRtrIsisLspMaxWait": vRtrIsisLspMaxWait,
       "vRtrIsisLspInitialWait": vRtrIsisLspInitialWait,
       "vRtrIsisLspSecondWait": vRtrIsisLspSecondWait,
       "vRtrIsisCsnpAuthentication": vRtrIsisCsnpAuthentication,
       "vRtrIsisHelloAuthentication": vRtrIsisHelloAuthentication,
       "vRtrIsisPsnpAuthentication": vRtrIsisPsnpAuthentication,
       "vRtrIsisGRRestartDuration": vRtrIsisGRRestartDuration,
       "vRtrIsisGRHelperMode": vRtrIsisGRHelperMode,
       "vRtrIsisStrictAdjacencyCheck": vRtrIsisStrictAdjacencyCheck,
       "vRtrIsisLevelTable": vRtrIsisLevelTable,
       "vRtrIsisLevelEntry": vRtrIsisLevelEntry,
       "vRtrIsisLevel": vRtrIsisLevel,
       "vRtrIsisLevelAuthKey": vRtrIsisLevelAuthKey,
       "vRtrIsisLevelAuthType": vRtrIsisLevelAuthType,
       "vRtrIsisLevelWideMetricsOnly": vRtrIsisLevelWideMetricsOnly,
       "vRtrIsisLevelOverloadStatus": vRtrIsisLevelOverloadStatus,
       "vRtrIsisLevelOverloadTimeLeft": vRtrIsisLevelOverloadTimeLeft,
       "vRtrIsisLevelNumLSPs": vRtrIsisLevelNumLSPs,
       "vRtrIsisLevelCsnpAuthentication": vRtrIsisLevelCsnpAuthentication,
       "vRtrIsisLevelHelloAuthentication": vRtrIsisLevelHelloAuthentication,
       "vRtrIsisLevelPsnpAuthentication": vRtrIsisLevelPsnpAuthentication,
       "vRtrIsisStatsTable": vRtrIsisStatsTable,
       "vRtrIsisStatsEntry": vRtrIsisStatsEntry,
       "vRtrIsisSpfRuns": vRtrIsisSpfRuns,
       "vRtrIsisLSPRegenerations": vRtrIsisLSPRegenerations,
       "vRtrIsisInitiatedPurges": vRtrIsisInitiatedPurges,
       "vRtrIsisLSPRecd": vRtrIsisLSPRecd,
       "vRtrIsisLSPDrop": vRtrIsisLSPDrop,
       "vRtrIsisLSPSent": vRtrIsisLSPSent,
       "vRtrIsisLSPRetrans": vRtrIsisLSPRetrans,
       "vRtrIsisIIHRecd": vRtrIsisIIHRecd,
       "vRtrIsisIIHDrop": vRtrIsisIIHDrop,
       "vRtrIsisIIHSent": vRtrIsisIIHSent,
       "vRtrIsisIIHRetrans": vRtrIsisIIHRetrans,
       "vRtrIsisCSNPRecd": vRtrIsisCSNPRecd,
       "vRtrIsisCSNPDrop": vRtrIsisCSNPDrop,
       "vRtrIsisCSNPSent": vRtrIsisCSNPSent,
       "vRtrIsisCSNPRetrans": vRtrIsisCSNPRetrans,
       "vRtrIsisPSNPRecd": vRtrIsisPSNPRecd,
       "vRtrIsisPSNPDrop": vRtrIsisPSNPDrop,
       "vRtrIsisPSNPSent": vRtrIsisPSNPSent,
       "vRtrIsisPSNPRetrans": vRtrIsisPSNPRetrans,
       "vRtrIsisUnknownRecd": vRtrIsisUnknownRecd,
       "vRtrIsisUnknownDrop": vRtrIsisUnknownDrop,
       "vRtrIsisUnknownSent": vRtrIsisUnknownSent,
       "vRtrIsisUnknownRetrans": vRtrIsisUnknownRetrans,
       "vRtrIsisCSPFRequests": vRtrIsisCSPFRequests,
       "vRtrIsisCSPFDroppedRequests": vRtrIsisCSPFDroppedRequests,
       "vRtrIsisCSPFPathsFound": vRtrIsisCSPFPathsFound,
       "vRtrIsisCSPFPathsNotFound": vRtrIsisCSPFPathsNotFound,
       "vRtrIsisHostnameTable": vRtrIsisHostnameTable,
       "vRtrIsisHostnameEntry": vRtrIsisHostnameEntry,
       "vRtrIsisSysID": vRtrIsisSysID,
       "vRtrIsisHostname": vRtrIsisHostname,
       "vRtrIsisRouteTable": vRtrIsisRouteTable,
       "vRtrIsisRouteEntry": vRtrIsisRouteEntry,
       "vRtrIsisRouteDest": vRtrIsisRouteDest,
       "vRtrIsisRouteMask": vRtrIsisRouteMask,
       "vRtrIsisRouteNexthopIP": vRtrIsisRouteNexthopIP,
       "vRtrIsisRouteLevel": vRtrIsisRouteLevel,
       "vRtrIsisRouteSpfVersion": vRtrIsisRouteSpfVersion,
       "vRtrIsisRouteMetric": vRtrIsisRouteMetric,
       "vRtrIsisRouteType": vRtrIsisRouteType,
       "vRtrIsisRouteNHopSysID": vRtrIsisRouteNHopSysID,
       "vRtrIsisPathTable": vRtrIsisPathTable,
       "vRtrIsisPathEntry": vRtrIsisPathEntry,
       "vRtrIsisPathID": vRtrIsisPathID,
       "vRtrIsisPathIfIndex": vRtrIsisPathIfIndex,
       "vRtrIsisPathNHopSysID": vRtrIsisPathNHopSysID,
       "vRtrIsisPathMetric": vRtrIsisPathMetric,
       "vRtrIsisPathSNPA": vRtrIsisPathSNPA,
       "vRtrIsisLSPTable": vRtrIsisLSPTable,
       "vRtrIsisLSPEntry": vRtrIsisLSPEntry,
       "vRtrIsisLSPId": vRtrIsisLSPId,
       "vRtrIsisLSPSeq": vRtrIsisLSPSeq,
       "vRtrIsisLSPChecksum": vRtrIsisLSPChecksum,
       "vRtrIsisLSPLifetimeRemain": vRtrIsisLSPLifetimeRemain,
       "vRtrIsisLSPVersion": vRtrIsisLSPVersion,
       "vRtrIsisLSPPktType": vRtrIsisLSPPktType,
       "vRtrIsisLSPPktVersion": vRtrIsisLSPPktVersion,
       "vRtrIsisLSPMaxArea": vRtrIsisLSPMaxArea,
       "vRtrIsisLSPSysIdLen": vRtrIsisLSPSysIdLen,
       "vRtrIsisLSPAttributes": vRtrIsisLSPAttributes,
       "vRtrIsisLSPUsedLen": vRtrIsisLSPUsedLen,
       "vRtrIsisLSPAllocLen": vRtrIsisLSPAllocLen,
       "vRtrIsisLSPBuff": vRtrIsisLSPBuff,
       "vRtrIsisLSPZeroRLT": vRtrIsisLSPZeroRLT,
       "vRtrIsisSpfLogTable": vRtrIsisSpfLogTable,
       "vRtrIsisSpfLogEntry": vRtrIsisSpfLogEntry,
       "vRtrIsisSpfTimeStamp": vRtrIsisSpfTimeStamp,
       "vRtrIsisSpfRunTime": vRtrIsisSpfRunTime,
       "vRtrIsisSpfL1Nodes": vRtrIsisSpfL1Nodes,
       "vRtrIsisSpfL2Nodes": vRtrIsisSpfL2Nodes,
       "vRtrIsisSpfEventCount": vRtrIsisSpfEventCount,
       "vRtrIsisSpfLastTriggerLSPId": vRtrIsisSpfLastTriggerLSPId,
       "vRtrIsisSpfTriggerReason": vRtrIsisSpfTriggerReason,
       "vRtrIsisSummaryTable": vRtrIsisSummaryTable,
       "vRtrIsisSummaryEntry": vRtrIsisSummaryEntry,
       "vRtrIsisSummPrefix": vRtrIsisSummPrefix,
       "vRtrIsisSummMask": vRtrIsisSummMask,
       "vRtrIsisSummRowStatus": vRtrIsisSummRowStatus,
       "vRtrIsisSummLevel": vRtrIsisSummLevel,
       "vRtrIsisInetRouteTable": vRtrIsisInetRouteTable,
       "vRtrIsisInetRouteEntry": vRtrIsisInetRouteEntry,
       "vRtrIsisInetRouteDestType": vRtrIsisInetRouteDestType,
       "vRtrIsisInetRouteDest": vRtrIsisInetRouteDest,
       "vRtrIsisInetRoutePrefixLength": vRtrIsisInetRoutePrefixLength,
       "vRtrIsisInetRouteNexthopIPType": vRtrIsisInetRouteNexthopIPType,
       "vRtrIsisInetRouteNexthopIP": vRtrIsisInetRouteNexthopIP,
       "vRtrIsisInetRouteLevel": vRtrIsisInetRouteLevel,
       "vRtrIsisInetRouteSpfRunNumber": vRtrIsisInetRouteSpfRunNumber,
       "vRtrIsisInetRouteMetric": vRtrIsisInetRouteMetric,
       "vRtrIsisInetRouteType": vRtrIsisInetRouteType,
       "vRtrIsisInetRouteNHopSysID": vRtrIsisInetRouteNHopSysID,
       "vRtrIsisInetSummaryTable": vRtrIsisInetSummaryTable,
       "vRtrIsisInetSummaryEntry": vRtrIsisInetSummaryEntry,
       "vRtrIsisInetSummPrefixType": vRtrIsisInetSummPrefixType,
       "vRtrIsisInetSummPrefix": vRtrIsisInetSummPrefix,
       "vRtrIsisInetSummPrefixLength": vRtrIsisInetSummPrefixLength,
       "vRtrIsisInetSummRowStatus": vRtrIsisInetSummRowStatus,
       "vRtrIsisInetSummLevel": vRtrIsisInetSummLevel,
       "vRtrIsisIfObjs": vRtrIsisIfObjs,
       "vRtrIsisIfTable": vRtrIsisIfTable,
       "vRtrIsisIfEntry": vRtrIsisIfEntry,
       "vRtrIsisIfIndex": vRtrIsisIfIndex,
       "vRtrIsisIfRowStatus": vRtrIsisIfRowStatus,
       "vRtrIsisIfLastChangeTime": vRtrIsisIfLastChangeTime,
       "vRtrIsisIfAdminState": vRtrIsisIfAdminState,
       "vRtrIsisIfOperState": vRtrIsisIfOperState,
       "vRtrIsisIfCsnpInterval": vRtrIsisIfCsnpInterval,
       "vRtrIsisIfHelloAuthKey": vRtrIsisIfHelloAuthKey,
       "vRtrIsisIfHelloAuthType": vRtrIsisIfHelloAuthType,
       "vRtrIsisIfLspPacingInterval": vRtrIsisIfLspPacingInterval,
       "vRtrIsisIfCircIndex": vRtrIsisIfCircIndex,
       "vRtrIsisIfRetransmitInterval": vRtrIsisIfRetransmitInterval,
       "vRtrIsisIfTypeDefault": vRtrIsisIfTypeDefault,
       "vRtrIsisIfLevelTable": vRtrIsisIfLevelTable,
       "vRtrIsisIfLevelEntry": vRtrIsisIfLevelEntry,
       "vRtrIsisIfLevel": vRtrIsisIfLevel,
       "vRtrIsisIfLevelLastChangeTime": vRtrIsisIfLevelLastChangeTime,
       "vRtrIsisIfLevelHelloAuthKey": vRtrIsisIfLevelHelloAuthKey,
       "vRtrIsisIfLevelHelloAuthType": vRtrIsisIfLevelHelloAuthType,
       "vRtrIsisIfLevelPassive": vRtrIsisIfLevelPassive,
       "vRtrIsisIfLevelTeMetric": vRtrIsisIfLevelTeMetric,
       "vRtrIsisIfLevelNumAdjacencies": vRtrIsisIfLevelNumAdjacencies,
       "vRtrIsisIfLevelISPriority": vRtrIsisIfLevelISPriority,
       "vRtrIsisIfLevelHelloTimer": vRtrIsisIfLevelHelloTimer,
       "vRtrIsisIfLevelAdminMetric": vRtrIsisIfLevelAdminMetric,
       "vRtrIsisIfLevelOperMetric": vRtrIsisIfLevelOperMetric,
       "vRtrIsisAdjObjs": vRtrIsisAdjObjs,
       "vRtrIsisISAdjTable": vRtrIsisISAdjTable,
       "vRtrIsisISAdjEntry": vRtrIsisISAdjEntry,
       "vRtrIsisISAdjExpiresIn": vRtrIsisISAdjExpiresIn,
       "vRtrIsisISAdjCircLevel": vRtrIsisISAdjCircLevel,
       "vRtrIsisISAdjNeighborIP": vRtrIsisISAdjNeighborIP,
       "vRtrIsisISAdjRestartSupport": vRtrIsisISAdjRestartSupport,
       "vRtrIsisISAdjRestartStatus": vRtrIsisISAdjRestartStatus,
       "vRtrIsisISAdjRestartSupressed": vRtrIsisISAdjRestartSupressed,
       "vRtrIsisISAdjNumRestarts": vRtrIsisISAdjNumRestarts,
       "vRtrIsisISAdjLastRestartTime": vRtrIsisISAdjLastRestartTime,
       "vRtrIsisISAdjNeighborIPv6Type": vRtrIsisISAdjNeighborIPv6Type,
       "vRtrIsisISAdjNeighborIpv6": vRtrIsisISAdjNeighborIpv6,
       "vRtrIsisNotificationObjs": vRtrIsisNotificationObjs,
       "vRtrIsisNotificationTable": vRtrIsisNotificationTable,
       "vRtrIsisNotificationEntry": vRtrIsisNotificationEntry,
       "vRtrIsisTrapLSPID": vRtrIsisTrapLSPID,
       "vRtrIsisSystemLevel": vRtrIsisSystemLevel,
       "vRtrIsisPDUFragment": vRtrIsisPDUFragment,
       "vRtrIsisFieldLen": vRtrIsisFieldLen,
       "vRtrIsisMaxAreaAddress": vRtrIsisMaxAreaAddress,
       "vRtrIsisProtocolVersion": vRtrIsisProtocolVersion,
       "vRtrIsisLSPSize": vRtrIsisLSPSize,
       "vRtrIsisOriginatingBufferSize": vRtrIsisOriginatingBufferSize,
       "vRtrIsisProtocolsSupported": vRtrIsisProtocolsSupported,
       "vRtrIsisDatabaseClearObjs": vRtrIsisDatabaseClearObjs,
       "vRtrIsisDatabaseClearTable": vRtrIsisDatabaseClearTable,
       "vRtrIsisDatabaseClearEntry": vRtrIsisDatabaseClearEntry,
       "vRtrIsisAdjDatabaseClear": vRtrIsisAdjDatabaseClear,
       "vRtrIsisLSPDatabaseClear": vRtrIsisLSPDatabaseClear,
       "vRtrIsisNotifications": vRtrIsisNotifications,
       "vRtrIsisDatabaseOverload": vRtrIsisDatabaseOverload,
       "vRtrIsisManualAddressDrops": vRtrIsisManualAddressDrops,
       "vRtrIsisCorruptedLSPDetected": vRtrIsisCorruptedLSPDetected,
       "vRtrIsisMaxSeqExceedAttempt": vRtrIsisMaxSeqExceedAttempt,
       "vRtrIsisIDLenMismatch": vRtrIsisIDLenMismatch,
       "vRtrIsisMaxAreaAddrsMismatch": vRtrIsisMaxAreaAddrsMismatch,
       "vRtrIsisOwnLSPPurge": vRtrIsisOwnLSPPurge,
       "vRtrIsisSequenceNumberSkip": vRtrIsisSequenceNumberSkip,
       "vRtrIsisAutTypeFail": vRtrIsisAutTypeFail,
       "vRtrIsisAuthFail": vRtrIsisAuthFail,
       "vRtrIsisVersionSkew": vRtrIsisVersionSkew,
       "vRtrIsisAreaMismatch": vRtrIsisAreaMismatch,
       "vRtrIsisRejectedAdjacency": vRtrIsisRejectedAdjacency,
       "vRtrIsisLSPTooLargeToPropagate": vRtrIsisLSPTooLargeToPropagate,
       "vRtrIsisOrigLSPBufSizeMismatch": vRtrIsisOrigLSPBufSizeMismatch,
       "vRtrIsisProtoSuppMismatch": vRtrIsisProtoSuppMismatch,
       "vRtrIsisAdjacencyChange": vRtrIsisAdjacencyChange,
       "vRtrIsisCircIdExhausted": vRtrIsisCircIdExhausted,
       "vRtrIsisAdjRestartStatusChange": vRtrIsisAdjRestartStatusChange,
       "vRtrIsisMIBConformance": vRtrIsisMIBConformance,
       "vRtrIsisMIBConformances": vRtrIsisMIBConformances,
       "vRtrIsisMIBCompliance": vRtrIsisMIBCompliance,
       "vRtrIsisMIBR2r1Compliance": vRtrIsisMIBR2r1Compliance,
       "vRtrIsisMIBV3v0Compliance": vRtrIsisMIBV3v0Compliance,
       "vRtrIsisMIBV4v0Compliance": vRtrIsisMIBV4v0Compliance,
       "vRtrIsisMIBGroups": vRtrIsisMIBGroups,
       "vRtrIsisGroup": vRtrIsisGroup,
       "vRtrIsisHostGroup": vRtrIsisHostGroup,
       "vRtrIsisRouteGroup": vRtrIsisRouteGroup,
       "vRtrIsisPathGroup": vRtrIsisPathGroup,
       "vRtrIsisLSPGroup": vRtrIsisLSPGroup,
       "vRtrIsisIfGroup": vRtrIsisIfGroup,
       "vRtrIsisAdjGroup": vRtrIsisAdjGroup,
       "vRtrIsisNotificationObjGroup": vRtrIsisNotificationObjGroup,
       "vRtrIsisNotificationsGroup": vRtrIsisNotificationsGroup,
       "vRtrIsisSpfGroup": vRtrIsisSpfGroup,
       "vRtrIsisSummaryGroup": vRtrIsisSummaryGroup,
       "vRtrIsisR2r1Group": vRtrIsisR2r1Group,
       "vRtrIsisV3v0Group": vRtrIsisV3v0Group,
       "vRtrIsisAdjV3v0Group": vRtrIsisAdjV3v0Group,
       "vRtrIsisNotificationV3v0Group": vRtrIsisNotificationV3v0Group,
       "vRtrIsisV4v0Group": vRtrIsisV4v0Group,
       "vRtrIsisRouteV4v0Group": vRtrIsisRouteV4v0Group,
       "vRtrIsisSummaryV4v0Group": vRtrIsisSummaryV4v0Group,
       "vRtrIsisAdjV4v0Group": vRtrIsisAdjV4v0Group,
       "vRtrIsisIfV4v0Group": vRtrIsisIfV4v0Group,
       "vRtrIsisScalarObjsGroup": vRtrIsisScalarObjsGroup,
       "vRtrIsisDBClearObjsGroup": vRtrIsisDBClearObjsGroup}
)
