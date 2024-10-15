# SNMP MIB module (DIAL-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DIAL-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:29:24 2024
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

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex",
    "ifOperStatus")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

dialControlMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AbsoluteCounter32(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_DialControlMibObjects_ObjectIdentity = ObjectIdentity
dialControlMibObjects = _DialControlMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 1)
)
_DialCtlConfiguration_ObjectIdentity = ObjectIdentity
dialCtlConfiguration = _DialCtlConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 1)
)


class _DialCtlAcceptMode_Type(Integer32):
    """Custom type dialCtlAcceptMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acceptAll", 2),
          ("acceptKnown", 3),
          ("acceptNone", 1))
    )


_DialCtlAcceptMode_Type.__name__ = "Integer32"
_DialCtlAcceptMode_Object = MibScalar
dialCtlAcceptMode = _DialCtlAcceptMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 1, 1),
    _DialCtlAcceptMode_Type()
)
dialCtlAcceptMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialCtlAcceptMode.setStatus("current")


class _DialCtlTrapEnable_Type(Integer32):
    """Custom type dialCtlTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DialCtlTrapEnable_Type.__name__ = "Integer32"
_DialCtlTrapEnable_Object = MibScalar
dialCtlTrapEnable = _DialCtlTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 1, 2),
    _DialCtlTrapEnable_Type()
)
dialCtlTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dialCtlTrapEnable.setStatus("current")
_DialCtlPeer_ObjectIdentity = ObjectIdentity
dialCtlPeer = _DialCtlPeer_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2)
)
_DialCtlPeerCfgTable_Object = MibTable
dialCtlPeerCfgTable = _DialCtlPeerCfgTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dialCtlPeerCfgTable.setStatus("current")
_DialCtlPeerCfgEntry_Object = MibTableRow
dialCtlPeerCfgEntry = _DialCtlPeerCfgEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1)
)
dialCtlPeerCfgEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "dialCtlPeerCfgId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dialCtlPeerCfgEntry.setStatus("current")


class _DialCtlPeerCfgId_Type(Integer32):
    """Custom type dialCtlPeerCfgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DialCtlPeerCfgId_Type.__name__ = "Integer32"
_DialCtlPeerCfgId_Object = MibTableColumn
dialCtlPeerCfgId = _DialCtlPeerCfgId_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 1),
    _DialCtlPeerCfgId_Type()
)
dialCtlPeerCfgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dialCtlPeerCfgId.setStatus("current")


class _DialCtlPeerCfgIfType_Type(IANAifType):
    """Custom type dialCtlPeerCfgIfType based on IANAifType"""


_DialCtlPeerCfgIfType_Object = MibTableColumn
dialCtlPeerCfgIfType = _DialCtlPeerCfgIfType_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 2),
    _DialCtlPeerCfgIfType_Type()
)
dialCtlPeerCfgIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgIfType.setStatus("current")


class _DialCtlPeerCfgLowerIf_Type(InterfaceIndexOrZero):
    """Custom type dialCtlPeerCfgLowerIf based on InterfaceIndexOrZero"""
    defaultValue = 0


_DialCtlPeerCfgLowerIf_Object = MibTableColumn
dialCtlPeerCfgLowerIf = _DialCtlPeerCfgLowerIf_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 3),
    _DialCtlPeerCfgLowerIf_Type()
)
dialCtlPeerCfgLowerIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgLowerIf.setStatus("current")
_DialCtlPeerCfgOriginateAddress_Type = DisplayString
_DialCtlPeerCfgOriginateAddress_Object = MibTableColumn
dialCtlPeerCfgOriginateAddress = _DialCtlPeerCfgOriginateAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 4),
    _DialCtlPeerCfgOriginateAddress_Type()
)
dialCtlPeerCfgOriginateAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgOriginateAddress.setStatus("current")
_DialCtlPeerCfgAnswerAddress_Type = DisplayString
_DialCtlPeerCfgAnswerAddress_Object = MibTableColumn
dialCtlPeerCfgAnswerAddress = _DialCtlPeerCfgAnswerAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 5),
    _DialCtlPeerCfgAnswerAddress_Type()
)
dialCtlPeerCfgAnswerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgAnswerAddress.setStatus("current")
_DialCtlPeerCfgSubAddress_Type = DisplayString
_DialCtlPeerCfgSubAddress_Object = MibTableColumn
dialCtlPeerCfgSubAddress = _DialCtlPeerCfgSubAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 6),
    _DialCtlPeerCfgSubAddress_Type()
)
dialCtlPeerCfgSubAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgSubAddress.setStatus("current")
_DialCtlPeerCfgClosedUserGroup_Type = DisplayString
_DialCtlPeerCfgClosedUserGroup_Object = MibTableColumn
dialCtlPeerCfgClosedUserGroup = _DialCtlPeerCfgClosedUserGroup_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 7),
    _DialCtlPeerCfgClosedUserGroup_Type()
)
dialCtlPeerCfgClosedUserGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgClosedUserGroup.setStatus("current")


class _DialCtlPeerCfgSpeed_Type(Integer32):
    """Custom type dialCtlPeerCfgSpeed based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgSpeed_Type.__name__ = "Integer32"
_DialCtlPeerCfgSpeed_Object = MibTableColumn
dialCtlPeerCfgSpeed = _DialCtlPeerCfgSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 8),
    _DialCtlPeerCfgSpeed_Type()
)
dialCtlPeerCfgSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgSpeed.setStatus("current")


class _DialCtlPeerCfgInfoType_Type(Integer32):
    """Custom type dialCtlPeerCfgInfoType based on Integer32"""
    defaultValue = 1

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_DialCtlPeerCfgInfoType_Type.__name__ = "Integer32"
_DialCtlPeerCfgInfoType_Object = MibTableColumn
dialCtlPeerCfgInfoType = _DialCtlPeerCfgInfoType_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 9),
    _DialCtlPeerCfgInfoType_Type()
)
dialCtlPeerCfgInfoType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgInfoType.setStatus("current")


class _DialCtlPeerCfgPermission_Type(Integer32):
    """Custom type dialCtlPeerCfgPermission based on Integer32"""
    defaultValue = 3

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
        *(("answer", 2),
          ("both", 3),
          ("callback", 4),
          ("none", 5),
          ("originate", 1))
    )


_DialCtlPeerCfgPermission_Type.__name__ = "Integer32"
_DialCtlPeerCfgPermission_Object = MibTableColumn
dialCtlPeerCfgPermission = _DialCtlPeerCfgPermission_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 10),
    _DialCtlPeerCfgPermission_Type()
)
dialCtlPeerCfgPermission.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgPermission.setStatus("current")


class _DialCtlPeerCfgInactivityTimer_Type(Integer32):
    """Custom type dialCtlPeerCfgInactivityTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgInactivityTimer_Type.__name__ = "Integer32"
_DialCtlPeerCfgInactivityTimer_Object = MibTableColumn
dialCtlPeerCfgInactivityTimer = _DialCtlPeerCfgInactivityTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 11),
    _DialCtlPeerCfgInactivityTimer_Type()
)
dialCtlPeerCfgInactivityTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgInactivityTimer.setStatus("current")
if mibBuilder.loadTexts:
    dialCtlPeerCfgInactivityTimer.setUnits("seconds")


class _DialCtlPeerCfgMinDuration_Type(Integer32):
    """Custom type dialCtlPeerCfgMinDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgMinDuration_Type.__name__ = "Integer32"
_DialCtlPeerCfgMinDuration_Object = MibTableColumn
dialCtlPeerCfgMinDuration = _DialCtlPeerCfgMinDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 12),
    _DialCtlPeerCfgMinDuration_Type()
)
dialCtlPeerCfgMinDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgMinDuration.setStatus("current")


class _DialCtlPeerCfgMaxDuration_Type(Integer32):
    """Custom type dialCtlPeerCfgMaxDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgMaxDuration_Type.__name__ = "Integer32"
_DialCtlPeerCfgMaxDuration_Object = MibTableColumn
dialCtlPeerCfgMaxDuration = _DialCtlPeerCfgMaxDuration_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 13),
    _DialCtlPeerCfgMaxDuration_Type()
)
dialCtlPeerCfgMaxDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgMaxDuration.setStatus("current")


class _DialCtlPeerCfgCarrierDelay_Type(Integer32):
    """Custom type dialCtlPeerCfgCarrierDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgCarrierDelay_Type.__name__ = "Integer32"
_DialCtlPeerCfgCarrierDelay_Object = MibTableColumn
dialCtlPeerCfgCarrierDelay = _DialCtlPeerCfgCarrierDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 14),
    _DialCtlPeerCfgCarrierDelay_Type()
)
dialCtlPeerCfgCarrierDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgCarrierDelay.setStatus("current")
if mibBuilder.loadTexts:
    dialCtlPeerCfgCarrierDelay.setUnits("seconds")


class _DialCtlPeerCfgCallRetries_Type(Integer32):
    """Custom type dialCtlPeerCfgCallRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgCallRetries_Type.__name__ = "Integer32"
_DialCtlPeerCfgCallRetries_Object = MibTableColumn
dialCtlPeerCfgCallRetries = _DialCtlPeerCfgCallRetries_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 15),
    _DialCtlPeerCfgCallRetries_Type()
)
dialCtlPeerCfgCallRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgCallRetries.setStatus("current")


class _DialCtlPeerCfgRetryDelay_Type(Integer32):
    """Custom type dialCtlPeerCfgRetryDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgRetryDelay_Type.__name__ = "Integer32"
_DialCtlPeerCfgRetryDelay_Object = MibTableColumn
dialCtlPeerCfgRetryDelay = _DialCtlPeerCfgRetryDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 16),
    _DialCtlPeerCfgRetryDelay_Type()
)
dialCtlPeerCfgRetryDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgRetryDelay.setStatus("current")
if mibBuilder.loadTexts:
    dialCtlPeerCfgRetryDelay.setUnits("seconds")


class _DialCtlPeerCfgFailureDelay_Type(Integer32):
    """Custom type dialCtlPeerCfgFailureDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DialCtlPeerCfgFailureDelay_Type.__name__ = "Integer32"
_DialCtlPeerCfgFailureDelay_Object = MibTableColumn
dialCtlPeerCfgFailureDelay = _DialCtlPeerCfgFailureDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 17),
    _DialCtlPeerCfgFailureDelay_Type()
)
dialCtlPeerCfgFailureDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgFailureDelay.setStatus("current")
if mibBuilder.loadTexts:
    dialCtlPeerCfgFailureDelay.setUnits("seconds")


class _DialCtlPeerCfgTrapEnable_Type(Integer32):
    """Custom type dialCtlPeerCfgTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_DialCtlPeerCfgTrapEnable_Type.__name__ = "Integer32"
_DialCtlPeerCfgTrapEnable_Object = MibTableColumn
dialCtlPeerCfgTrapEnable = _DialCtlPeerCfgTrapEnable_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 18),
    _DialCtlPeerCfgTrapEnable_Type()
)
dialCtlPeerCfgTrapEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgTrapEnable.setStatus("current")
_DialCtlPeerCfgStatus_Type = RowStatus
_DialCtlPeerCfgStatus_Object = MibTableColumn
dialCtlPeerCfgStatus = _DialCtlPeerCfgStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 1, 1, 19),
    _DialCtlPeerCfgStatus_Type()
)
dialCtlPeerCfgStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dialCtlPeerCfgStatus.setStatus("current")
_DialCtlPeerStatsTable_Object = MibTable
dialCtlPeerStatsTable = _DialCtlPeerStatsTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dialCtlPeerStatsTable.setStatus("current")
_DialCtlPeerStatsEntry_Object = MibTableRow
dialCtlPeerStatsEntry = _DialCtlPeerStatsEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dialCtlPeerStatsEntry.setStatus("current")
_DialCtlPeerStatsConnectTime_Type = AbsoluteCounter32
_DialCtlPeerStatsConnectTime_Object = MibTableColumn
dialCtlPeerStatsConnectTime = _DialCtlPeerStatsConnectTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 1),
    _DialCtlPeerStatsConnectTime_Type()
)
dialCtlPeerStatsConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsConnectTime.setStatus("current")
if mibBuilder.loadTexts:
    dialCtlPeerStatsConnectTime.setUnits("seconds")
_DialCtlPeerStatsChargedUnits_Type = AbsoluteCounter32
_DialCtlPeerStatsChargedUnits_Object = MibTableColumn
dialCtlPeerStatsChargedUnits = _DialCtlPeerStatsChargedUnits_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 2),
    _DialCtlPeerStatsChargedUnits_Type()
)
dialCtlPeerStatsChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsChargedUnits.setStatus("current")
_DialCtlPeerStatsSuccessCalls_Type = AbsoluteCounter32
_DialCtlPeerStatsSuccessCalls_Object = MibTableColumn
dialCtlPeerStatsSuccessCalls = _DialCtlPeerStatsSuccessCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 3),
    _DialCtlPeerStatsSuccessCalls_Type()
)
dialCtlPeerStatsSuccessCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsSuccessCalls.setStatus("current")
_DialCtlPeerStatsFailCalls_Type = AbsoluteCounter32
_DialCtlPeerStatsFailCalls_Object = MibTableColumn
dialCtlPeerStatsFailCalls = _DialCtlPeerStatsFailCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 4),
    _DialCtlPeerStatsFailCalls_Type()
)
dialCtlPeerStatsFailCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsFailCalls.setStatus("current")
_DialCtlPeerStatsAcceptCalls_Type = AbsoluteCounter32
_DialCtlPeerStatsAcceptCalls_Object = MibTableColumn
dialCtlPeerStatsAcceptCalls = _DialCtlPeerStatsAcceptCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 5),
    _DialCtlPeerStatsAcceptCalls_Type()
)
dialCtlPeerStatsAcceptCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsAcceptCalls.setStatus("current")
_DialCtlPeerStatsRefuseCalls_Type = AbsoluteCounter32
_DialCtlPeerStatsRefuseCalls_Object = MibTableColumn
dialCtlPeerStatsRefuseCalls = _DialCtlPeerStatsRefuseCalls_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 6),
    _DialCtlPeerStatsRefuseCalls_Type()
)
dialCtlPeerStatsRefuseCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsRefuseCalls.setStatus("current")


class _DialCtlPeerStatsLastDisconnectCause_Type(OctetString):
    """Custom type dialCtlPeerStatsLastDisconnectCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_DialCtlPeerStatsLastDisconnectCause_Type.__name__ = "OctetString"
_DialCtlPeerStatsLastDisconnectCause_Object = MibTableColumn
dialCtlPeerStatsLastDisconnectCause = _DialCtlPeerStatsLastDisconnectCause_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 7),
    _DialCtlPeerStatsLastDisconnectCause_Type()
)
dialCtlPeerStatsLastDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsLastDisconnectCause.setStatus("current")
_DialCtlPeerStatsLastDisconnectText_Type = DisplayString
_DialCtlPeerStatsLastDisconnectText_Object = MibTableColumn
dialCtlPeerStatsLastDisconnectText = _DialCtlPeerStatsLastDisconnectText_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 8),
    _DialCtlPeerStatsLastDisconnectText_Type()
)
dialCtlPeerStatsLastDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsLastDisconnectText.setStatus("current")
_DialCtlPeerStatsLastSetupTime_Type = TimeStamp
_DialCtlPeerStatsLastSetupTime_Object = MibTableColumn
dialCtlPeerStatsLastSetupTime = _DialCtlPeerStatsLastSetupTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 2, 2, 1, 9),
    _DialCtlPeerStatsLastSetupTime_Type()
)
dialCtlPeerStatsLastSetupTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dialCtlPeerStatsLastSetupTime.setStatus("current")
_CallActive_ObjectIdentity = ObjectIdentity
callActive = _CallActive_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3)
)
_CallActiveTable_Object = MibTable
callActiveTable = _CallActiveTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1)
)
if mibBuilder.loadTexts:
    callActiveTable.setStatus("current")
_CallActiveEntry_Object = MibTableRow
callActiveEntry = _CallActiveEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1)
)
callActiveEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    callActiveEntry.setStatus("current")
_CallActiveSetupTime_Type = TimeStamp
_CallActiveSetupTime_Object = MibTableColumn
callActiveSetupTime = _CallActiveSetupTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 1),
    _CallActiveSetupTime_Type()
)
callActiveSetupTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callActiveSetupTime.setStatus("current")


class _CallActiveIndex_Type(Integer32):
    """Custom type callActiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CallActiveIndex_Type.__name__ = "Integer32"
_CallActiveIndex_Object = MibTableColumn
callActiveIndex = _CallActiveIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 2),
    _CallActiveIndex_Type()
)
callActiveIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    callActiveIndex.setStatus("current")
_CallActivePeerAddress_Type = DisplayString
_CallActivePeerAddress_Object = MibTableColumn
callActivePeerAddress = _CallActivePeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 3),
    _CallActivePeerAddress_Type()
)
callActivePeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActivePeerAddress.setStatus("current")
_CallActivePeerSubAddress_Type = DisplayString
_CallActivePeerSubAddress_Object = MibTableColumn
callActivePeerSubAddress = _CallActivePeerSubAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 4),
    _CallActivePeerSubAddress_Type()
)
callActivePeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActivePeerSubAddress.setStatus("current")


class _CallActivePeerId_Type(Integer32):
    """Custom type callActivePeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallActivePeerId_Type.__name__ = "Integer32"
_CallActivePeerId_Object = MibTableColumn
callActivePeerId = _CallActivePeerId_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 5),
    _CallActivePeerId_Type()
)
callActivePeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActivePeerId.setStatus("current")


class _CallActivePeerIfIndex_Type(Integer32):
    """Custom type callActivePeerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallActivePeerIfIndex_Type.__name__ = "Integer32"
_CallActivePeerIfIndex_Object = MibTableColumn
callActivePeerIfIndex = _CallActivePeerIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 6),
    _CallActivePeerIfIndex_Type()
)
callActivePeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActivePeerIfIndex.setStatus("current")
_CallActiveLogicalIfIndex_Type = InterfaceIndexOrZero
_CallActiveLogicalIfIndex_Object = MibTableColumn
callActiveLogicalIfIndex = _CallActiveLogicalIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 7),
    _CallActiveLogicalIfIndex_Type()
)
callActiveLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveLogicalIfIndex.setStatus("current")
_CallActiveConnectTime_Type = TimeStamp
_CallActiveConnectTime_Object = MibTableColumn
callActiveConnectTime = _CallActiveConnectTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 8),
    _CallActiveConnectTime_Type()
)
callActiveConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveConnectTime.setStatus("current")


class _CallActiveCallState_Type(Integer32):
    """Custom type callActiveCallState based on Integer32"""
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
        *(("active", 4),
          ("connected", 3),
          ("connecting", 2),
          ("unknown", 1))
    )


_CallActiveCallState_Type.__name__ = "Integer32"
_CallActiveCallState_Object = MibTableColumn
callActiveCallState = _CallActiveCallState_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 9),
    _CallActiveCallState_Type()
)
callActiveCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallState.setStatus("current")


class _CallActiveCallOrigin_Type(Integer32):
    """Custom type callActiveCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("callback", 3),
          ("originate", 1))
    )


_CallActiveCallOrigin_Type.__name__ = "Integer32"
_CallActiveCallOrigin_Object = MibTableColumn
callActiveCallOrigin = _CallActiveCallOrigin_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 10),
    _CallActiveCallOrigin_Type()
)
callActiveCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveCallOrigin.setStatus("current")
_CallActiveChargedUnits_Type = AbsoluteCounter32
_CallActiveChargedUnits_Object = MibTableColumn
callActiveChargedUnits = _CallActiveChargedUnits_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 11),
    _CallActiveChargedUnits_Type()
)
callActiveChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveChargedUnits.setStatus("current")


class _CallActiveInfoType_Type(Integer32):
    """Custom type callActiveInfoType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_CallActiveInfoType_Type.__name__ = "Integer32"
_CallActiveInfoType_Object = MibTableColumn
callActiveInfoType = _CallActiveInfoType_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 12),
    _CallActiveInfoType_Type()
)
callActiveInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveInfoType.setStatus("current")
_CallActiveTransmitPackets_Type = AbsoluteCounter32
_CallActiveTransmitPackets_Object = MibTableColumn
callActiveTransmitPackets = _CallActiveTransmitPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 13),
    _CallActiveTransmitPackets_Type()
)
callActiveTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveTransmitPackets.setStatus("current")
_CallActiveTransmitBytes_Type = AbsoluteCounter32
_CallActiveTransmitBytes_Object = MibTableColumn
callActiveTransmitBytes = _CallActiveTransmitBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 14),
    _CallActiveTransmitBytes_Type()
)
callActiveTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveTransmitBytes.setStatus("current")
_CallActiveReceivePackets_Type = AbsoluteCounter32
_CallActiveReceivePackets_Object = MibTableColumn
callActiveReceivePackets = _CallActiveReceivePackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 15),
    _CallActiveReceivePackets_Type()
)
callActiveReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveReceivePackets.setStatus("current")
_CallActiveReceiveBytes_Type = AbsoluteCounter32
_CallActiveReceiveBytes_Object = MibTableColumn
callActiveReceiveBytes = _CallActiveReceiveBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 3, 1, 1, 16),
    _CallActiveReceiveBytes_Type()
)
callActiveReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callActiveReceiveBytes.setStatus("current")
_CallHistory_ObjectIdentity = ObjectIdentity
callHistory = _CallHistory_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4)
)


class _CallHistoryTableMaxLength_Type(Integer32):
    """Custom type callHistoryTableMaxLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallHistoryTableMaxLength_Type.__name__ = "Integer32"
_CallHistoryTableMaxLength_Object = MibScalar
callHistoryTableMaxLength = _CallHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 1),
    _CallHistoryTableMaxLength_Type()
)
callHistoryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHistoryTableMaxLength.setStatus("current")


class _CallHistoryRetainTimer_Type(Integer32):
    """Custom type callHistoryRetainTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallHistoryRetainTimer_Type.__name__ = "Integer32"
_CallHistoryRetainTimer_Object = MibScalar
callHistoryRetainTimer = _CallHistoryRetainTimer_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 2),
    _CallHistoryRetainTimer_Type()
)
callHistoryRetainTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    callHistoryRetainTimer.setStatus("current")
if mibBuilder.loadTexts:
    callHistoryRetainTimer.setUnits("minutes")
_CallHistoryTable_Object = MibTable
callHistoryTable = _CallHistoryTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3)
)
if mibBuilder.loadTexts:
    callHistoryTable.setStatus("current")
_CallHistoryEntry_Object = MibTableRow
callHistoryEntry = _CallHistoryEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1)
)
callHistoryEntry.setIndexNames(
    (0, "DIAL-CONTROL-MIB", "callActiveSetupTime"),
    (0, "DIAL-CONTROL-MIB", "callActiveIndex"),
)
if mibBuilder.loadTexts:
    callHistoryEntry.setStatus("current")
_CallHistoryPeerAddress_Type = DisplayString
_CallHistoryPeerAddress_Object = MibTableColumn
callHistoryPeerAddress = _CallHistoryPeerAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 1),
    _CallHistoryPeerAddress_Type()
)
callHistoryPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryPeerAddress.setStatus("current")
_CallHistoryPeerSubAddress_Type = DisplayString
_CallHistoryPeerSubAddress_Object = MibTableColumn
callHistoryPeerSubAddress = _CallHistoryPeerSubAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 2),
    _CallHistoryPeerSubAddress_Type()
)
callHistoryPeerSubAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryPeerSubAddress.setStatus("current")


class _CallHistoryPeerId_Type(Integer32):
    """Custom type callHistoryPeerId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallHistoryPeerId_Type.__name__ = "Integer32"
_CallHistoryPeerId_Object = MibTableColumn
callHistoryPeerId = _CallHistoryPeerId_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 3),
    _CallHistoryPeerId_Type()
)
callHistoryPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryPeerId.setStatus("current")


class _CallHistoryPeerIfIndex_Type(Integer32):
    """Custom type callHistoryPeerIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CallHistoryPeerIfIndex_Type.__name__ = "Integer32"
_CallHistoryPeerIfIndex_Object = MibTableColumn
callHistoryPeerIfIndex = _CallHistoryPeerIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 4),
    _CallHistoryPeerIfIndex_Type()
)
callHistoryPeerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryPeerIfIndex.setStatus("current")
_CallHistoryLogicalIfIndex_Type = InterfaceIndex
_CallHistoryLogicalIfIndex_Object = MibTableColumn
callHistoryLogicalIfIndex = _CallHistoryLogicalIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 5),
    _CallHistoryLogicalIfIndex_Type()
)
callHistoryLogicalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryLogicalIfIndex.setStatus("current")


class _CallHistoryDisconnectCause_Type(OctetString):
    """Custom type callHistoryDisconnectCause based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_CallHistoryDisconnectCause_Type.__name__ = "OctetString"
_CallHistoryDisconnectCause_Object = MibTableColumn
callHistoryDisconnectCause = _CallHistoryDisconnectCause_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 6),
    _CallHistoryDisconnectCause_Type()
)
callHistoryDisconnectCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryDisconnectCause.setStatus("current")
_CallHistoryDisconnectText_Type = DisplayString
_CallHistoryDisconnectText_Object = MibTableColumn
callHistoryDisconnectText = _CallHistoryDisconnectText_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 7),
    _CallHistoryDisconnectText_Type()
)
callHistoryDisconnectText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryDisconnectText.setStatus("current")
_CallHistoryConnectTime_Type = TimeStamp
_CallHistoryConnectTime_Object = MibTableColumn
callHistoryConnectTime = _CallHistoryConnectTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 8),
    _CallHistoryConnectTime_Type()
)
callHistoryConnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryConnectTime.setStatus("current")
_CallHistoryDisconnectTime_Type = TimeStamp
_CallHistoryDisconnectTime_Object = MibTableColumn
callHistoryDisconnectTime = _CallHistoryDisconnectTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 9),
    _CallHistoryDisconnectTime_Type()
)
callHistoryDisconnectTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryDisconnectTime.setStatus("current")


class _CallHistoryCallOrigin_Type(Integer32):
    """Custom type callHistoryCallOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("answer", 2),
          ("callback", 3),
          ("originate", 1))
    )


_CallHistoryCallOrigin_Type.__name__ = "Integer32"
_CallHistoryCallOrigin_Object = MibTableColumn
callHistoryCallOrigin = _CallHistoryCallOrigin_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 10),
    _CallHistoryCallOrigin_Type()
)
callHistoryCallOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryCallOrigin.setStatus("current")
_CallHistoryChargedUnits_Type = AbsoluteCounter32
_CallHistoryChargedUnits_Object = MibTableColumn
callHistoryChargedUnits = _CallHistoryChargedUnits_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 11),
    _CallHistoryChargedUnits_Type()
)
callHistoryChargedUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryChargedUnits.setStatus("current")


class _CallHistoryInfoType_Type(Integer32):
    """Custom type callHistoryInfoType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("audio31", 6),
          ("audio7", 7),
          ("fax", 10),
          ("other", 1),
          ("packetSwitched", 9),
          ("restrictedDigital", 5),
          ("speech", 2),
          ("unrestrictedDigital", 3),
          ("unrestrictedDigital56", 4),
          ("video", 8))
    )


_CallHistoryInfoType_Type.__name__ = "Integer32"
_CallHistoryInfoType_Object = MibTableColumn
callHistoryInfoType = _CallHistoryInfoType_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 12),
    _CallHistoryInfoType_Type()
)
callHistoryInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryInfoType.setStatus("current")
_CallHistoryTransmitPackets_Type = AbsoluteCounter32
_CallHistoryTransmitPackets_Object = MibTableColumn
callHistoryTransmitPackets = _CallHistoryTransmitPackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 13),
    _CallHistoryTransmitPackets_Type()
)
callHistoryTransmitPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryTransmitPackets.setStatus("current")
_CallHistoryTransmitBytes_Type = AbsoluteCounter32
_CallHistoryTransmitBytes_Object = MibTableColumn
callHistoryTransmitBytes = _CallHistoryTransmitBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 14),
    _CallHistoryTransmitBytes_Type()
)
callHistoryTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryTransmitBytes.setStatus("current")
_CallHistoryReceivePackets_Type = AbsoluteCounter32
_CallHistoryReceivePackets_Object = MibTableColumn
callHistoryReceivePackets = _CallHistoryReceivePackets_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 15),
    _CallHistoryReceivePackets_Type()
)
callHistoryReceivePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryReceivePackets.setStatus("current")
_CallHistoryReceiveBytes_Type = AbsoluteCounter32
_CallHistoryReceiveBytes_Object = MibTableColumn
callHistoryReceiveBytes = _CallHistoryReceiveBytes_Object(
    (1, 3, 6, 1, 2, 1, 10, 21, 1, 4, 3, 1, 16),
    _CallHistoryReceiveBytes_Type()
)
callHistoryReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    callHistoryReceiveBytes.setStatus("current")
_DialControlMibTrapPrefix_ObjectIdentity = ObjectIdentity
dialControlMibTrapPrefix = _DialControlMibTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 2)
)
_DialControlMibTraps_ObjectIdentity = ObjectIdentity
dialControlMibTraps = _DialControlMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 2, 0)
)
_DialControlMibConformance_ObjectIdentity = ObjectIdentity
dialControlMibConformance = _DialControlMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 3)
)
_DialControlMibCompliances_ObjectIdentity = ObjectIdentity
dialControlMibCompliances = _DialControlMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 1)
)
_DialControlMibGroups_ObjectIdentity = ObjectIdentity
dialControlMibGroups = _DialControlMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 2)
)
dialCtlPeerCfgEntry.registerAugmentions(
    ("DIAL-CONTROL-MIB",
     "dialCtlPeerStatsEntry")
)
dialCtlPeerStatsEntry.setIndexNames(*dialCtlPeerCfgEntry.getIndexNames())

# Managed Objects groups

dialControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 1)
)
dialControlGroup.setObjects(
      *(("DIAL-CONTROL-MIB", "dialCtlAcceptMode"),
        ("DIAL-CONTROL-MIB", "dialCtlTrapEnable"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgIfType"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgLowerIf"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgOriginateAddress"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgAnswerAddress"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgSubAddress"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgClosedUserGroup"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgSpeed"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgInfoType"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgPermission"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgInactivityTimer"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgMinDuration"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgMaxDuration"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgCarrierDelay"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgCallRetries"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgRetryDelay"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgFailureDelay"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgTrapEnable"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCfgStatus"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsConnectTime"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsChargedUnits"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsSuccessCalls"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsFailCalls"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsAcceptCalls"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsRefuseCalls"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastDisconnectCause"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastDisconnectText"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerStatsLastSetupTime"))
)
if mibBuilder.loadTexts:
    dialControlGroup.setStatus("current")

callActiveGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 2)
)
callActiveGroup.setObjects(
      *(("DIAL-CONTROL-MIB", "callActivePeerAddress"),
        ("DIAL-CONTROL-MIB", "callActivePeerSubAddress"),
        ("DIAL-CONTROL-MIB", "callActivePeerId"),
        ("DIAL-CONTROL-MIB", "callActivePeerIfIndex"),
        ("DIAL-CONTROL-MIB", "callActiveLogicalIfIndex"),
        ("DIAL-CONTROL-MIB", "callActiveConnectTime"),
        ("DIAL-CONTROL-MIB", "callActiveCallState"),
        ("DIAL-CONTROL-MIB", "callActiveCallOrigin"),
        ("DIAL-CONTROL-MIB", "callActiveChargedUnits"),
        ("DIAL-CONTROL-MIB", "callActiveInfoType"),
        ("DIAL-CONTROL-MIB", "callActiveTransmitPackets"),
        ("DIAL-CONTROL-MIB", "callActiveTransmitBytes"),
        ("DIAL-CONTROL-MIB", "callActiveReceivePackets"),
        ("DIAL-CONTROL-MIB", "callActiveReceiveBytes"))
)
if mibBuilder.loadTexts:
    callActiveGroup.setStatus("current")

callHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 3)
)
callHistoryGroup.setObjects(
      *(("DIAL-CONTROL-MIB", "callHistoryTableMaxLength"),
        ("DIAL-CONTROL-MIB", "callHistoryRetainTimer"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerAddress"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerSubAddress"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerId"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerIfIndex"),
        ("DIAL-CONTROL-MIB", "callHistoryLogicalIfIndex"),
        ("DIAL-CONTROL-MIB", "callHistoryDisconnectCause"),
        ("DIAL-CONTROL-MIB", "callHistoryDisconnectText"),
        ("DIAL-CONTROL-MIB", "callHistoryConnectTime"),
        ("DIAL-CONTROL-MIB", "callHistoryDisconnectTime"),
        ("DIAL-CONTROL-MIB", "callHistoryCallOrigin"),
        ("DIAL-CONTROL-MIB", "callHistoryChargedUnits"),
        ("DIAL-CONTROL-MIB", "callHistoryInfoType"),
        ("DIAL-CONTROL-MIB", "callHistoryTransmitPackets"),
        ("DIAL-CONTROL-MIB", "callHistoryTransmitBytes"),
        ("DIAL-CONTROL-MIB", "callHistoryReceivePackets"),
        ("DIAL-CONTROL-MIB", "callHistoryReceiveBytes"))
)
if mibBuilder.loadTexts:
    callHistoryGroup.setStatus("current")


# Notification objects

dialCtlPeerCallInformation = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 21, 2, 0, 1)
)
dialCtlPeerCallInformation.setObjects(
      *(("DIAL-CONTROL-MIB", "callHistoryPeerId"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerIfIndex"),
        ("DIAL-CONTROL-MIB", "callHistoryLogicalIfIndex"),
        ("IF-MIB", "ifOperStatus"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerAddress"),
        ("DIAL-CONTROL-MIB", "callHistoryPeerSubAddress"),
        ("DIAL-CONTROL-MIB", "callHistoryDisconnectCause"),
        ("DIAL-CONTROL-MIB", "callHistoryConnectTime"),
        ("DIAL-CONTROL-MIB", "callHistoryDisconnectTime"),
        ("DIAL-CONTROL-MIB", "callHistoryInfoType"),
        ("DIAL-CONTROL-MIB", "callHistoryCallOrigin"))
)
if mibBuilder.loadTexts:
    dialCtlPeerCallInformation.setStatus(
        "current"
    )

dialCtlPeerCallSetup = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 21, 2, 0, 2)
)
dialCtlPeerCallSetup.setObjects(
      *(("DIAL-CONTROL-MIB", "callActivePeerId"),
        ("DIAL-CONTROL-MIB", "callActivePeerIfIndex"),
        ("DIAL-CONTROL-MIB", "callActiveLogicalIfIndex"),
        ("IF-MIB", "ifOperStatus"),
        ("DIAL-CONTROL-MIB", "callActivePeerAddress"),
        ("DIAL-CONTROL-MIB", "callActivePeerSubAddress"),
        ("DIAL-CONTROL-MIB", "callActiveInfoType"),
        ("DIAL-CONTROL-MIB", "callActiveCallOrigin"))
)
if mibBuilder.loadTexts:
    dialCtlPeerCallSetup.setStatus(
        "current"
    )


# Notifications groups

callNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 2, 4)
)
callNotificationsGroup.setObjects(
      *(("DIAL-CONTROL-MIB", "dialCtlPeerCallInformation"),
        ("DIAL-CONTROL-MIB", "dialCtlPeerCallSetup"))
)
if mibBuilder.loadTexts:
    callNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

dialControlMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 21, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dialControlMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DIAL-CONTROL-MIB",
    **{"AbsoluteCounter32": AbsoluteCounter32,
       "dialControlMib": dialControlMib,
       "dialControlMibObjects": dialControlMibObjects,
       "dialCtlConfiguration": dialCtlConfiguration,
       "dialCtlAcceptMode": dialCtlAcceptMode,
       "dialCtlTrapEnable": dialCtlTrapEnable,
       "dialCtlPeer": dialCtlPeer,
       "dialCtlPeerCfgTable": dialCtlPeerCfgTable,
       "dialCtlPeerCfgEntry": dialCtlPeerCfgEntry,
       "dialCtlPeerCfgId": dialCtlPeerCfgId,
       "dialCtlPeerCfgIfType": dialCtlPeerCfgIfType,
       "dialCtlPeerCfgLowerIf": dialCtlPeerCfgLowerIf,
       "dialCtlPeerCfgOriginateAddress": dialCtlPeerCfgOriginateAddress,
       "dialCtlPeerCfgAnswerAddress": dialCtlPeerCfgAnswerAddress,
       "dialCtlPeerCfgSubAddress": dialCtlPeerCfgSubAddress,
       "dialCtlPeerCfgClosedUserGroup": dialCtlPeerCfgClosedUserGroup,
       "dialCtlPeerCfgSpeed": dialCtlPeerCfgSpeed,
       "dialCtlPeerCfgInfoType": dialCtlPeerCfgInfoType,
       "dialCtlPeerCfgPermission": dialCtlPeerCfgPermission,
       "dialCtlPeerCfgInactivityTimer": dialCtlPeerCfgInactivityTimer,
       "dialCtlPeerCfgMinDuration": dialCtlPeerCfgMinDuration,
       "dialCtlPeerCfgMaxDuration": dialCtlPeerCfgMaxDuration,
       "dialCtlPeerCfgCarrierDelay": dialCtlPeerCfgCarrierDelay,
       "dialCtlPeerCfgCallRetries": dialCtlPeerCfgCallRetries,
       "dialCtlPeerCfgRetryDelay": dialCtlPeerCfgRetryDelay,
       "dialCtlPeerCfgFailureDelay": dialCtlPeerCfgFailureDelay,
       "dialCtlPeerCfgTrapEnable": dialCtlPeerCfgTrapEnable,
       "dialCtlPeerCfgStatus": dialCtlPeerCfgStatus,
       "dialCtlPeerStatsTable": dialCtlPeerStatsTable,
       "dialCtlPeerStatsEntry": dialCtlPeerStatsEntry,
       "dialCtlPeerStatsConnectTime": dialCtlPeerStatsConnectTime,
       "dialCtlPeerStatsChargedUnits": dialCtlPeerStatsChargedUnits,
       "dialCtlPeerStatsSuccessCalls": dialCtlPeerStatsSuccessCalls,
       "dialCtlPeerStatsFailCalls": dialCtlPeerStatsFailCalls,
       "dialCtlPeerStatsAcceptCalls": dialCtlPeerStatsAcceptCalls,
       "dialCtlPeerStatsRefuseCalls": dialCtlPeerStatsRefuseCalls,
       "dialCtlPeerStatsLastDisconnectCause": dialCtlPeerStatsLastDisconnectCause,
       "dialCtlPeerStatsLastDisconnectText": dialCtlPeerStatsLastDisconnectText,
       "dialCtlPeerStatsLastSetupTime": dialCtlPeerStatsLastSetupTime,
       "callActive": callActive,
       "callActiveTable": callActiveTable,
       "callActiveEntry": callActiveEntry,
       "callActiveSetupTime": callActiveSetupTime,
       "callActiveIndex": callActiveIndex,
       "callActivePeerAddress": callActivePeerAddress,
       "callActivePeerSubAddress": callActivePeerSubAddress,
       "callActivePeerId": callActivePeerId,
       "callActivePeerIfIndex": callActivePeerIfIndex,
       "callActiveLogicalIfIndex": callActiveLogicalIfIndex,
       "callActiveConnectTime": callActiveConnectTime,
       "callActiveCallState": callActiveCallState,
       "callActiveCallOrigin": callActiveCallOrigin,
       "callActiveChargedUnits": callActiveChargedUnits,
       "callActiveInfoType": callActiveInfoType,
       "callActiveTransmitPackets": callActiveTransmitPackets,
       "callActiveTransmitBytes": callActiveTransmitBytes,
       "callActiveReceivePackets": callActiveReceivePackets,
       "callActiveReceiveBytes": callActiveReceiveBytes,
       "callHistory": callHistory,
       "callHistoryTableMaxLength": callHistoryTableMaxLength,
       "callHistoryRetainTimer": callHistoryRetainTimer,
       "callHistoryTable": callHistoryTable,
       "callHistoryEntry": callHistoryEntry,
       "callHistoryPeerAddress": callHistoryPeerAddress,
       "callHistoryPeerSubAddress": callHistoryPeerSubAddress,
       "callHistoryPeerId": callHistoryPeerId,
       "callHistoryPeerIfIndex": callHistoryPeerIfIndex,
       "callHistoryLogicalIfIndex": callHistoryLogicalIfIndex,
       "callHistoryDisconnectCause": callHistoryDisconnectCause,
       "callHistoryDisconnectText": callHistoryDisconnectText,
       "callHistoryConnectTime": callHistoryConnectTime,
       "callHistoryDisconnectTime": callHistoryDisconnectTime,
       "callHistoryCallOrigin": callHistoryCallOrigin,
       "callHistoryChargedUnits": callHistoryChargedUnits,
       "callHistoryInfoType": callHistoryInfoType,
       "callHistoryTransmitPackets": callHistoryTransmitPackets,
       "callHistoryTransmitBytes": callHistoryTransmitBytes,
       "callHistoryReceivePackets": callHistoryReceivePackets,
       "callHistoryReceiveBytes": callHistoryReceiveBytes,
       "dialControlMibTrapPrefix": dialControlMibTrapPrefix,
       "dialControlMibTraps": dialControlMibTraps,
       "dialCtlPeerCallInformation": dialCtlPeerCallInformation,
       "dialCtlPeerCallSetup": dialCtlPeerCallSetup,
       "dialControlMibConformance": dialControlMibConformance,
       "dialControlMibCompliances": dialControlMibCompliances,
       "dialControlMibCompliance": dialControlMibCompliance,
       "dialControlMibGroups": dialControlMibGroups,
       "dialControlGroup": dialControlGroup,
       "callActiveGroup": callActiveGroup,
       "callHistoryGroup": callHistoryGroup,
       "callNotificationsGroup": callNotificationsGroup}
)
