# SNMP MIB module (Wellfleet-RREDUND-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-RREDUND-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:01 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(wfRRedGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfRRedGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfRRedundGroup_ObjectIdentity = ObjectIdentity
wfRRedundGroup = _WfRRedundGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1)
)


class _WfRRedundDelete_Type(Integer32):
    """Custom type wfRRedundDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRRedundDelete_Type.__name__ = "Integer32"
_WfRRedundDelete_Object = MibScalar
wfRRedundDelete = _WfRRedundDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 1),
    _WfRRedundDelete_Type()
)
wfRRedundDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundDelete.setStatus("mandatory")


class _WfRRedundDisable_Type(Integer32):
    """Custom type wfRRedundDisable based on Integer32"""
    defaultValue = 1

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


_WfRRedundDisable_Type.__name__ = "Integer32"
_WfRRedundDisable_Object = MibScalar
wfRRedundDisable = _WfRRedundDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 2),
    _WfRRedundDisable_Type()
)
wfRRedundDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundDisable.setStatus("mandatory")


class _WfRRedundState_Type(Integer32):
    """Custom type wfRRedundState based on Integer32"""
    defaultValue = 7

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
        *(("bidding", 6),
          ("down", 8),
          ("init", 7),
          ("notpresent", 9),
          ("rcvdprigdby", 3),
          ("up", 1),
          ("waitnewpri", 2),
          ("waitprigdby", 4),
          ("waitsosrply", 5))
    )


_WfRRedundState_Type.__name__ = "Integer32"
_WfRRedundState_Object = MibScalar
wfRRedundState = _WfRRedundState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 3),
    _WfRRedundState_Type()
)
wfRRedundState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundState.setStatus("mandatory")


class _WfRRedundGroupId_Type(Integer32):
    """Custom type wfRRedundGroupId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfRRedundGroupId_Type.__name__ = "Integer32"
_WfRRedundGroupId_Object = MibScalar
wfRRedundGroupId = _WfRRedundGroupId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 4),
    _WfRRedundGroupId_Type()
)
wfRRedundGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundGroupId.setStatus("mandatory")


class _WfRRedundMemberId_Type(Integer32):
    """Custom type wfRRedundMemberId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfRRedundMemberId_Type.__name__ = "Integer32"
_WfRRedundMemberId_Object = MibScalar
wfRRedundMemberId = _WfRRedundMemberId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 5),
    _WfRRedundMemberId_Type()
)
wfRRedundMemberId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundMemberId.setStatus("mandatory")


class _WfRRedundRole_Type(Integer32):
    """Custom type wfRRedundRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WfRRedundRole_Type.__name__ = "Integer32"
_WfRRedundRole_Object = MibScalar
wfRRedundRole = _WfRRedundRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 6),
    _WfRRedundRole_Type()
)
wfRRedundRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundRole.setStatus("mandatory")
_WfRRedundRefNum_Type = Integer32
_WfRRedundRefNum_Object = MibScalar
wfRRedundRefNum = _WfRRedundRefNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 7),
    _WfRRedundRefNum_Type()
)
wfRRedundRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRefNum.setStatus("mandatory")
_WfRRedundGoodIFCount_Type = Integer32
_WfRRedundGoodIFCount_Object = MibScalar
wfRRedundGoodIFCount = _WfRRedundGoodIFCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 8),
    _WfRRedundGoodIFCount_Type()
)
wfRRedundGoodIFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundGoodIFCount.setStatus("mandatory")
_WfRRedundGoodRESCount_Type = Integer32
_WfRRedundGoodRESCount_Object = MibScalar
wfRRedundGoodRESCount = _WfRRedundGoodRESCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 9),
    _WfRRedundGoodRESCount_Type()
)
wfRRedundGoodRESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundGoodRESCount.setStatus("mandatory")


class _WfRRedundSwitch_Type(Integer32):
    """Custom type wfRRedundSwitch based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dontswitch", 1),
          ("switch", 2))
    )


_WfRRedundSwitch_Type.__name__ = "Integer32"
_WfRRedundSwitch_Object = MibScalar
wfRRedundSwitch = _WfRRedundSwitch_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 10),
    _WfRRedundSwitch_Type()
)
wfRRedundSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundSwitch.setStatus("mandatory")


class _WfRRedundAuto_Type(Integer32):
    """Custom type wfRRedundAuto based on Integer32"""
    defaultValue = 2

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
        *(("auto", 2),
          ("failureonlyauto", 4),
          ("manual", 1),
          ("oneshotauto", 3))
    )


_WfRRedundAuto_Type.__name__ = "Integer32"
_WfRRedundAuto_Object = MibScalar
wfRRedundAuto = _WfRRedundAuto_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 11),
    _WfRRedundAuto_Type()
)
wfRRedundAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundAuto.setStatus("mandatory")


class _WfRRedundGoodBidCount_Type(Integer32):
    """Custom type wfRRedundGoodBidCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfRRedundGoodBidCount_Type.__name__ = "Integer32"
_WfRRedundGoodBidCount_Object = MibScalar
wfRRedundGoodBidCount = _WfRRedundGoodBidCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 12),
    _WfRRedundGoodBidCount_Type()
)
wfRRedundGoodBidCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundGoodBidCount.setStatus("mandatory")


class _WfRRedundVersion_Type(Integer32):
    """Custom type wfRRedundVersion based on Integer32"""
    defaultValue = 1


_WfRRedundVersion_Object = MibScalar
wfRRedundVersion = _WfRRedundVersion_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 13),
    _WfRRedundVersion_Type()
)
wfRRedundVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundVersion.setStatus("mandatory")


class _WfRRedundPriority_Type(Integer32):
    """Custom type wfRRedundPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfRRedundPriority_Type.__name__ = "Integer32"
_WfRRedundPriority_Object = MibScalar
wfRRedundPriority = _WfRRedundPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 14),
    _WfRRedundPriority_Type()
)
wfRRedundPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundPriority.setStatus("mandatory")


class _WfRRedundHelloTimer_Type(Integer32):
    """Custom type wfRRedundHelloTimer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_WfRRedundHelloTimer_Type.__name__ = "Integer32"
_WfRRedundHelloTimer_Object = MibScalar
wfRRedundHelloTimer = _WfRRedundHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 15),
    _WfRRedundHelloTimer_Type()
)
wfRRedundHelloTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundHelloTimer.setStatus("mandatory")


class _WfRRedundBidDuration_Type(Integer32):
    """Custom type wfRRedundBidDuration based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfRRedundBidDuration_Type.__name__ = "Integer32"
_WfRRedundBidDuration_Object = MibScalar
wfRRedundBidDuration = _WfRRedundBidDuration_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 16),
    _WfRRedundBidDuration_Type()
)
wfRRedundBidDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundBidDuration.setStatus("mandatory")


class _WfRRedundTimeoutCounters_Type(Integer32):
    """Custom type wfRRedundTimeoutCounters based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_WfRRedundTimeoutCounters_Type.__name__ = "Integer32"
_WfRRedundTimeoutCounters_Object = MibScalar
wfRRedundTimeoutCounters = _WfRRedundTimeoutCounters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 17),
    _WfRRedundTimeoutCounters_Type()
)
wfRRedundTimeoutCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundTimeoutCounters.setStatus("mandatory")
_WfRRedundNPrimaryCounters_Type = Counter32
_WfRRedundNPrimaryCounters_Object = MibScalar
wfRRedundNPrimaryCounters = _WfRRedundNPrimaryCounters_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 18),
    _WfRRedundNPrimaryCounters_Type()
)
wfRRedundNPrimaryCounters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundNPrimaryCounters.setStatus("mandatory")


class _WfRRedundRoleSwitchDelayTimer_Type(Integer32):
    """Custom type wfRRedundRoleSwitchDelayTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_WfRRedundRoleSwitchDelayTimer_Type.__name__ = "Integer32"
_WfRRedundRoleSwitchDelayTimer_Object = MibScalar
wfRRedundRoleSwitchDelayTimer = _WfRRedundRoleSwitchDelayTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 19),
    _WfRRedundRoleSwitchDelayTimer_Type()
)
wfRRedundRoleSwitchDelayTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundRoleSwitchDelayTimer.setStatus("mandatory")
_WfRRedundPriConfigFilePath_Type = DisplayString
_WfRRedundPriConfigFilePath_Object = MibScalar
wfRRedundPriConfigFilePath = _WfRRedundPriConfigFilePath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 20),
    _WfRRedundPriConfigFilePath_Type()
)
wfRRedundPriConfigFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundPriConfigFilePath.setStatus("mandatory")


class _WfRRedundPriMemberID_Type(Integer32):
    """Custom type wfRRedundPriMemberID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfRRedundPriMemberID_Type.__name__ = "Integer32"
_WfRRedundPriMemberID_Object = MibScalar
wfRRedundPriMemberID = _WfRRedundPriMemberID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 21),
    _WfRRedundPriMemberID_Type()
)
wfRRedundPriMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundPriMemberID.setStatus("mandatory")


class _WfRRedundPriState_Type(Integer32):
    """Custom type wfRRedundPriState based on Integer32"""
    defaultValue = 7

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
        *(("bidding", 6),
          ("down", 8),
          ("init", 7),
          ("notpresent", 9),
          ("rcvdprigdby", 3),
          ("up", 1),
          ("waitnewpri", 2),
          ("waitprigdby", 4),
          ("waitsosrply", 5))
    )


_WfRRedundPriState_Type.__name__ = "Integer32"
_WfRRedundPriState_Object = MibScalar
wfRRedundPriState = _WfRRedundPriState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 22),
    _WfRRedundPriState_Type()
)
wfRRedundPriState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundPriState.setStatus("mandatory")
_WfRRedundPriRefNum_Type = Integer32
_WfRRedundPriRefNum_Object = MibScalar
wfRRedundPriRefNum = _WfRRedundPriRefNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 23),
    _WfRRedundPriRefNum_Type()
)
wfRRedundPriRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundPriRefNum.setStatus("mandatory")
_WfRRedundPriGoodIFCount_Type = Integer32
_WfRRedundPriGoodIFCount_Object = MibScalar
wfRRedundPriGoodIFCount = _WfRRedundPriGoodIFCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 24),
    _WfRRedundPriGoodIFCount_Type()
)
wfRRedundPriGoodIFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundPriGoodIFCount.setStatus("mandatory")
_WfRRedundPriGoodRESCount_Type = Integer32
_WfRRedundPriGoodRESCount_Object = MibScalar
wfRRedundPriGoodRESCount = _WfRRedundPriGoodRESCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 25),
    _WfRRedundPriGoodRESCount_Type()
)
wfRRedundPriGoodRESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundPriGoodRESCount.setStatus("mandatory")


class _WfRRedundBSecMemberID_Type(Integer32):
    """Custom type wfRRedundBSecMemberID based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfRRedundBSecMemberID_Type.__name__ = "Integer32"
_WfRRedundBSecMemberID_Object = MibScalar
wfRRedundBSecMemberID = _WfRRedundBSecMemberID_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 26),
    _WfRRedundBSecMemberID_Type()
)
wfRRedundBSecMemberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundBSecMemberID.setStatus("mandatory")


class _WfRRedundBSecState_Type(Integer32):
    """Custom type wfRRedundBSecState based on Integer32"""
    defaultValue = 7

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
        *(("bidding", 6),
          ("down", 8),
          ("init", 7),
          ("notpresent", 9),
          ("rcvdprigdby", 3),
          ("up", 1),
          ("waitnewpri", 2),
          ("waitprigdby", 4),
          ("waitsosrply", 5))
    )


_WfRRedundBSecState_Type.__name__ = "Integer32"
_WfRRedundBSecState_Object = MibScalar
wfRRedundBSecState = _WfRRedundBSecState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 27),
    _WfRRedundBSecState_Type()
)
wfRRedundBSecState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundBSecState.setStatus("mandatory")
_WfRRedundBSecRefNum_Type = Integer32
_WfRRedundBSecRefNum_Object = MibScalar
wfRRedundBSecRefNum = _WfRRedundBSecRefNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 28),
    _WfRRedundBSecRefNum_Type()
)
wfRRedundBSecRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundBSecRefNum.setStatus("mandatory")
_WfRRedundBSecGoodIFCount_Type = Integer32
_WfRRedundBSecGoodIFCount_Object = MibScalar
wfRRedundBSecGoodIFCount = _WfRRedundBSecGoodIFCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 29),
    _WfRRedundBSecGoodIFCount_Type()
)
wfRRedundBSecGoodIFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundBSecGoodIFCount.setStatus("mandatory")
_WfRRedundBSecGoodRESCount_Type = Integer32
_WfRRedundBSecGoodRESCount_Object = MibScalar
wfRRedundBSecGoodRESCount = _WfRRedundBSecGoodRESCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 30),
    _WfRRedundBSecGoodRESCount_Type()
)
wfRRedundBSecGoodRESCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundBSecGoodRESCount.setStatus("mandatory")


class _WfRRedundWarmBoot_Type(Integer32):
    """Custom type wfRRedundWarmBoot based on Integer32"""
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


_WfRRedundWarmBoot_Type.__name__ = "Integer32"
_WfRRedundWarmBoot_Object = MibScalar
wfRRedundWarmBoot = _WfRRedundWarmBoot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 31),
    _WfRRedundWarmBoot_Type()
)
wfRRedundWarmBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundWarmBoot.setStatus("mandatory")


class _WfRRedundSlot_Type(Integer32):
    """Custom type wfRRedundSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 14),
    )


_WfRRedundSlot_Type.__name__ = "Integer32"
_WfRRedundSlot_Object = MibScalar
wfRRedundSlot = _WfRRedundSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 32),
    _WfRRedundSlot_Type()
)
wfRRedundSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundSlot.setStatus("mandatory")


class _WfRRedundSlotMask_Type(Gauge32):
    """Custom type wfRRedundSlotMask based on Gauge32"""
    defaultValue = 4294705152


_WfRRedundSlotMask_Object = MibScalar
wfRRedundSlotMask = _WfRRedundSlotMask_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 33),
    _WfRRedundSlotMask_Type()
)
wfRRedundSlotMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundSlotMask.setStatus("mandatory")


class _WfRRedundAtmDeathTimer_Type(Integer32):
    """Custom type wfRRedundAtmDeathTimer based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WfRRedundAtmDeathTimer_Type.__name__ = "Integer32"
_WfRRedundAtmDeathTimer_Object = MibScalar
wfRRedundAtmDeathTimer = _WfRRedundAtmDeathTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 1, 34),
    _WfRRedundAtmDeathTimer_Type()
)
wfRRedundAtmDeathTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundAtmDeathTimer.setStatus("mandatory")
_WfRRedundCctTable_Object = MibTable
wfRRedundCctTable = _WfRRedundCctTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2)
)
if mibBuilder.loadTexts:
    wfRRedundCctTable.setStatus("mandatory")
_WfRRedundCctEntry_Object = MibTableRow
wfRRedundCctEntry = _WfRRedundCctEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1)
)
wfRRedundCctEntry.setIndexNames(
    (0, "Wellfleet-RREDUND-MIB", "wfRRedundCctCct"),
)
if mibBuilder.loadTexts:
    wfRRedundCctEntry.setStatus("mandatory")


class _WfRRedundCctDelete_Type(Integer32):
    """Custom type wfRRedundCctDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRRedundCctDelete_Type.__name__ = "Integer32"
_WfRRedundCctDelete_Object = MibTableColumn
wfRRedundCctDelete = _WfRRedundCctDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 1),
    _WfRRedundCctDelete_Type()
)
wfRRedundCctDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundCctDelete.setStatus("mandatory")


class _WfRRedundCctDisable_Type(Integer32):
    """Custom type wfRRedundCctDisable based on Integer32"""
    defaultValue = 1

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


_WfRRedundCctDisable_Type.__name__ = "Integer32"
_WfRRedundCctDisable_Object = MibTableColumn
wfRRedundCctDisable = _WfRRedundCctDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 2),
    _WfRRedundCctDisable_Type()
)
wfRRedundCctDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundCctDisable.setStatus("mandatory")
_WfRRedundCctCct_Type = Integer32
_WfRRedundCctCct_Object = MibTableColumn
wfRRedundCctCct = _WfRRedundCctCct_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 3),
    _WfRRedundCctCct_Type()
)
wfRRedundCctCct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundCctCct.setStatus("mandatory")
_WfRRedundCctPrimaryMACAddr_Type = OctetString
_WfRRedundCctPrimaryMACAddr_Object = MibTableColumn
wfRRedundCctPrimaryMACAddr = _WfRRedundCctPrimaryMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 4),
    _WfRRedundCctPrimaryMACAddr_Type()
)
wfRRedundCctPrimaryMACAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundCctPrimaryMACAddr.setStatus("mandatory")


class _WfRRedundCctMonitor_Type(Integer32):
    """Custom type wfRRedundCctMonitor based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circuit", 1),
          ("link", 2))
    )


_WfRRedundCctMonitor_Type.__name__ = "Integer32"
_WfRRedundCctMonitor_Object = MibTableColumn
wfRRedundCctMonitor = _WfRRedundCctMonitor_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 5),
    _WfRRedundCctMonitor_Type()
)
wfRRedundCctMonitor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundCctMonitor.setStatus("mandatory")


class _WfRRedundCctRSwitchOnFailure_Type(Integer32):
    """Custom type wfRRedundCctRSwitchOnFailure based on Integer32"""
    defaultValue = 1

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


_WfRRedundCctRSwitchOnFailure_Type.__name__ = "Integer32"
_WfRRedundCctRSwitchOnFailure_Object = MibTableColumn
wfRRedundCctRSwitchOnFailure = _WfRRedundCctRSwitchOnFailure_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 6),
    _WfRRedundCctRSwitchOnFailure_Type()
)
wfRRedundCctRSwitchOnFailure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundCctRSwitchOnFailure.setStatus("mandatory")


class _WfRRedundCctSendPduDisable_Type(Integer32):
    """Custom type wfRRedundCctSendPduDisable based on Integer32"""
    defaultValue = 1

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


_WfRRedundCctSendPduDisable_Type.__name__ = "Integer32"
_WfRRedundCctSendPduDisable_Object = MibTableColumn
wfRRedundCctSendPduDisable = _WfRRedundCctSendPduDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 7),
    _WfRRedundCctSendPduDisable_Type()
)
wfRRedundCctSendPduDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundCctSendPduDisable.setStatus("mandatory")


class _WfRRedundCctStatus_Type(Integer32):
    """Custom type wfRRedundCctStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_WfRRedundCctStatus_Type.__name__ = "Integer32"
_WfRRedundCctStatus_Object = MibTableColumn
wfRRedundCctStatus = _WfRRedundCctStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 8),
    _WfRRedundCctStatus_Type()
)
wfRRedundCctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundCctStatus.setStatus("mandatory")
_WfRRedundCctSONMPXmtCount_Type = Integer32
_WfRRedundCctSONMPXmtCount_Object = MibTableColumn
wfRRedundCctSONMPXmtCount = _WfRRedundCctSONMPXmtCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 9),
    _WfRRedundCctSONMPXmtCount_Type()
)
wfRRedundCctSONMPXmtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundCctSONMPXmtCount.setStatus("mandatory")
_WfRRedundCctSONMPRcvCount_Type = Integer32
_WfRRedundCctSONMPRcvCount_Object = MibTableColumn
wfRRedundCctSONMPRcvCount = _WfRRedundCctSONMPRcvCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 10),
    _WfRRedundCctSONMPRcvCount_Type()
)
wfRRedundCctSONMPRcvCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundCctSONMPRcvCount.setStatus("mandatory")
_WfRRedundCctSONMPRcvErrorCount_Type = Integer32
_WfRRedundCctSONMPRcvErrorCount_Object = MibTableColumn
wfRRedundCctSONMPRcvErrorCount = _WfRRedundCctSONMPRcvErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 2, 1, 11),
    _WfRRedundCctSONMPRcvErrorCount_Type()
)
wfRRedundCctSONMPRcvErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundCctSONMPRcvErrorCount.setStatus("mandatory")
_WfRRedundResourceTable_Object = MibTable
wfRRedundResourceTable = _WfRRedundResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3)
)
if mibBuilder.loadTexts:
    wfRRedundResourceTable.setStatus("mandatory")
_WfRRedundResourceEntry_Object = MibTableRow
wfRRedundResourceEntry = _WfRRedundResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1)
)
wfRRedundResourceEntry.setIndexNames(
    (0, "Wellfleet-RREDUND-MIB", "wfRRedundResourceCircuitNumber"),
    (0, "Wellfleet-RREDUND-MIB", "wfRRedundResourceNetAddr"),
)
if mibBuilder.loadTexts:
    wfRRedundResourceEntry.setStatus("mandatory")


class _WfRRedundResourceDelete_Type(Integer32):
    """Custom type wfRRedundResourceDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRRedundResourceDelete_Type.__name__ = "Integer32"
_WfRRedundResourceDelete_Object = MibTableColumn
wfRRedundResourceDelete = _WfRRedundResourceDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 1),
    _WfRRedundResourceDelete_Type()
)
wfRRedundResourceDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundResourceDelete.setStatus("mandatory")


class _WfRRedundResourceDisable_Type(Integer32):
    """Custom type wfRRedundResourceDisable based on Integer32"""
    defaultValue = 1

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


_WfRRedundResourceDisable_Type.__name__ = "Integer32"
_WfRRedundResourceDisable_Object = MibTableColumn
wfRRedundResourceDisable = _WfRRedundResourceDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 2),
    _WfRRedundResourceDisable_Type()
)
wfRRedundResourceDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundResourceDisable.setStatus("mandatory")
_WfRRedundResourceCircuitNumber_Type = Integer32
_WfRRedundResourceCircuitNumber_Object = MibTableColumn
wfRRedundResourceCircuitNumber = _WfRRedundResourceCircuitNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 3),
    _WfRRedundResourceCircuitNumber_Type()
)
wfRRedundResourceCircuitNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundResourceCircuitNumber.setStatus("mandatory")
_WfRRedundResourceNetAddr_Type = IpAddress
_WfRRedundResourceNetAddr_Object = MibTableColumn
wfRRedundResourceNetAddr = _WfRRedundResourceNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 4),
    _WfRRedundResourceNetAddr_Type()
)
wfRRedundResourceNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundResourceNetAddr.setStatus("mandatory")


class _WfRRedundResourceStatus_Type(Integer32):
    """Custom type wfRRedundResourceStatus based on Integer32"""
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
        *(("reachable", 1),
          ("unknown", 3),
          ("unreachable", 2))
    )


_WfRRedundResourceStatus_Type.__name__ = "Integer32"
_WfRRedundResourceStatus_Object = MibTableColumn
wfRRedundResourceStatus = _WfRRedundResourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 5),
    _WfRRedundResourceStatus_Type()
)
wfRRedundResourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundResourceStatus.setStatus("mandatory")


class _WfRRedundResourceStatusUpdateDisable_Type(Integer32):
    """Custom type wfRRedundResourceStatusUpdateDisable based on Integer32"""
    defaultValue = 1

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


_WfRRedundResourceStatusUpdateDisable_Type.__name__ = "Integer32"
_WfRRedundResourceStatusUpdateDisable_Object = MibTableColumn
wfRRedundResourceStatusUpdateDisable = _WfRRedundResourceStatusUpdateDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 6),
    _WfRRedundResourceStatusUpdateDisable_Type()
)
wfRRedundResourceStatusUpdateDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundResourceStatusUpdateDisable.setStatus("mandatory")


class _WfRRedundResourcePingIntervalTimer_Type(Integer32):
    """Custom type wfRRedundResourcePingIntervalTimer based on Integer32"""
    defaultValue = 600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86399),
    )


_WfRRedundResourcePingIntervalTimer_Type.__name__ = "Integer32"
_WfRRedundResourcePingIntervalTimer_Object = MibTableColumn
wfRRedundResourcePingIntervalTimer = _WfRRedundResourcePingIntervalTimer_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 7),
    _WfRRedundResourcePingIntervalTimer_Type()
)
wfRRedundResourcePingIntervalTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundResourcePingIntervalTimer.setStatus("mandatory")


class _WfRRedundResourcePingRetryCount_Type(Integer32):
    """Custom type wfRRedundResourcePingRetryCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_WfRRedundResourcePingRetryCount_Type.__name__ = "Integer32"
_WfRRedundResourcePingRetryCount_Object = MibTableColumn
wfRRedundResourcePingRetryCount = _WfRRedundResourcePingRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 8),
    _WfRRedundResourcePingRetryCount_Type()
)
wfRRedundResourcePingRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundResourcePingRetryCount.setStatus("mandatory")


class _WfRRedundResourcePingTimeOut_Type(Integer32):
    """Custom type wfRRedundResourcePingTimeOut based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_WfRRedundResourcePingTimeOut_Type.__name__ = "Integer32"
_WfRRedundResourcePingTimeOut_Object = MibTableColumn
wfRRedundResourcePingTimeOut = _WfRRedundResourcePingTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 3, 1, 9),
    _WfRRedundResourcePingTimeOut_Type()
)
wfRRedundResourcePingTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundResourcePingTimeOut.setStatus("mandatory")
_WfRRedundRemoteMemberTable_Object = MibTable
wfRRedundRemoteMemberTable = _WfRRedundRemoteMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4)
)
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberTable.setStatus("mandatory")
_WfRRedundRemoteMemberEntry_Object = MibTableRow
wfRRedundRemoteMemberEntry = _WfRRedundRemoteMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1)
)
wfRRedundRemoteMemberEntry.setIndexNames(
    (0, "Wellfleet-RREDUND-MIB", "wfRRedundRemoteMemberGroupId"),
    (0, "Wellfleet-RREDUND-MIB", "wfRRedundRemoteMemberId"),
)
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberEntry.setStatus("mandatory")


class _WfRRedundRemoteMemberDelete_Type(Integer32):
    """Custom type wfRRedundRemoteMemberDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfRRedundRemoteMemberDelete_Type.__name__ = "Integer32"
_WfRRedundRemoteMemberDelete_Object = MibTableColumn
wfRRedundRemoteMemberDelete = _WfRRedundRemoteMemberDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 1),
    _WfRRedundRemoteMemberDelete_Type()
)
wfRRedundRemoteMemberDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberDelete.setStatus("mandatory")
_WfRRedundRemoteMemberGroupId_Type = Integer32
_WfRRedundRemoteMemberGroupId_Object = MibTableColumn
wfRRedundRemoteMemberGroupId = _WfRRedundRemoteMemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 2),
    _WfRRedundRemoteMemberGroupId_Type()
)
wfRRedundRemoteMemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberGroupId.setStatus("mandatory")
_WfRRedundRemoteMemberId_Type = Integer32
_WfRRedundRemoteMemberId_Object = MibTableColumn
wfRRedundRemoteMemberId = _WfRRedundRemoteMemberId_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 3),
    _WfRRedundRemoteMemberId_Type()
)
wfRRedundRemoteMemberId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberId.setStatus("mandatory")
_WfRRedundRemoteMemberNetAddr_Type = IpAddress
_WfRRedundRemoteMemberNetAddr_Object = MibTableColumn
wfRRedundRemoteMemberNetAddr = _WfRRedundRemoteMemberNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 4),
    _WfRRedundRemoteMemberNetAddr_Type()
)
wfRRedundRemoteMemberNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberNetAddr.setStatus("mandatory")


class _WfRRedundRemoteMemberRole_Type(Integer32):
    """Custom type wfRRedundRemoteMemberRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_WfRRedundRemoteMemberRole_Type.__name__ = "Integer32"
_WfRRedundRemoteMemberRole_Object = MibTableColumn
wfRRedundRemoteMemberRole = _WfRRedundRemoteMemberRole_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 5),
    _WfRRedundRemoteMemberRole_Type()
)
wfRRedundRemoteMemberRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberRole.setStatus("mandatory")


class _WfRRedundRemoteMemberState_Type(Integer32):
    """Custom type wfRRedundRemoteMemberState based on Integer32"""
    defaultValue = 7

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
        *(("bidding", 6),
          ("down", 8),
          ("init", 7),
          ("notpresent", 9),
          ("rcvdprigdby", 3),
          ("up", 1),
          ("waitnewpri", 2),
          ("waitprigdby", 4),
          ("waitsosrply", 5))
    )


_WfRRedundRemoteMemberState_Type.__name__ = "Integer32"
_WfRRedundRemoteMemberState_Object = MibTableColumn
wfRRedundRemoteMemberState = _WfRRedundRemoteMemberState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 6),
    _WfRRedundRemoteMemberState_Type()
)
wfRRedundRemoteMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberState.setStatus("mandatory")
_WfRRedundRemoteMemberRefNum_Type = Integer32
_WfRRedundRemoteMemberRefNum_Object = MibTableColumn
wfRRedundRemoteMemberRefNum = _WfRRedundRemoteMemberRefNum_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 7),
    _WfRRedundRemoteMemberRefNum_Type()
)
wfRRedundRemoteMemberRefNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberRefNum.setStatus("mandatory")


class _WfRRedundRemoteMemberPriority_Type(Integer32):
    """Custom type wfRRedundRemoteMemberPriority based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_WfRRedundRemoteMemberPriority_Type.__name__ = "Integer32"
_WfRRedundRemoteMemberPriority_Object = MibTableColumn
wfRRedundRemoteMemberPriority = _WfRRedundRemoteMemberPriority_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 8),
    _WfRRedundRemoteMemberPriority_Type()
)
wfRRedundRemoteMemberPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberPriority.setStatus("mandatory")
_WfRRedundRemoteMemberGoodIfCnt_Type = Integer32
_WfRRedundRemoteMemberGoodIfCnt_Object = MibTableColumn
wfRRedundRemoteMemberGoodIfCnt = _WfRRedundRemoteMemberGoodIfCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 9),
    _WfRRedundRemoteMemberGoodIfCnt_Type()
)
wfRRedundRemoteMemberGoodIfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberGoodIfCnt.setStatus("mandatory")
_WfRRedundRemoteMemberGoodResCnt_Type = Integer32
_WfRRedundRemoteMemberGoodResCnt_Object = MibTableColumn
wfRRedundRemoteMemberGoodResCnt = _WfRRedundRemoteMemberGoodResCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 10),
    _WfRRedundRemoteMemberGoodResCnt_Type()
)
wfRRedundRemoteMemberGoodResCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberGoodResCnt.setStatus("mandatory")
_WfRRedundRemoteMemberIfCnt_Type = Integer32
_WfRRedundRemoteMemberIfCnt_Object = MibTableColumn
wfRRedundRemoteMemberIfCnt = _WfRRedundRemoteMemberIfCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 11),
    _WfRRedundRemoteMemberIfCnt_Type()
)
wfRRedundRemoteMemberIfCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberIfCnt.setStatus("mandatory")
_WfRRedundRemoteMemberLocalIfReachCnt_Type = Integer32
_WfRRedundRemoteMemberLocalIfReachCnt_Object = MibTableColumn
wfRRedundRemoteMemberLocalIfReachCnt = _WfRRedundRemoteMemberLocalIfReachCnt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 17, 4, 1, 12),
    _WfRRedundRemoteMemberLocalIfReachCnt_Type()
)
wfRRedundRemoteMemberLocalIfReachCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfRRedundRemoteMemberLocalIfReachCnt.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-RREDUND-MIB",
    **{"wfRRedundGroup": wfRRedundGroup,
       "wfRRedundDelete": wfRRedundDelete,
       "wfRRedundDisable": wfRRedundDisable,
       "wfRRedundState": wfRRedundState,
       "wfRRedundGroupId": wfRRedundGroupId,
       "wfRRedundMemberId": wfRRedundMemberId,
       "wfRRedundRole": wfRRedundRole,
       "wfRRedundRefNum": wfRRedundRefNum,
       "wfRRedundGoodIFCount": wfRRedundGoodIFCount,
       "wfRRedundGoodRESCount": wfRRedundGoodRESCount,
       "wfRRedundSwitch": wfRRedundSwitch,
       "wfRRedundAuto": wfRRedundAuto,
       "wfRRedundGoodBidCount": wfRRedundGoodBidCount,
       "wfRRedundVersion": wfRRedundVersion,
       "wfRRedundPriority": wfRRedundPriority,
       "wfRRedundHelloTimer": wfRRedundHelloTimer,
       "wfRRedundBidDuration": wfRRedundBidDuration,
       "wfRRedundTimeoutCounters": wfRRedundTimeoutCounters,
       "wfRRedundNPrimaryCounters": wfRRedundNPrimaryCounters,
       "wfRRedundRoleSwitchDelayTimer": wfRRedundRoleSwitchDelayTimer,
       "wfRRedundPriConfigFilePath": wfRRedundPriConfigFilePath,
       "wfRRedundPriMemberID": wfRRedundPriMemberID,
       "wfRRedundPriState": wfRRedundPriState,
       "wfRRedundPriRefNum": wfRRedundPriRefNum,
       "wfRRedundPriGoodIFCount": wfRRedundPriGoodIFCount,
       "wfRRedundPriGoodRESCount": wfRRedundPriGoodRESCount,
       "wfRRedundBSecMemberID": wfRRedundBSecMemberID,
       "wfRRedundBSecState": wfRRedundBSecState,
       "wfRRedundBSecRefNum": wfRRedundBSecRefNum,
       "wfRRedundBSecGoodIFCount": wfRRedundBSecGoodIFCount,
       "wfRRedundBSecGoodRESCount": wfRRedundBSecGoodRESCount,
       "wfRRedundWarmBoot": wfRRedundWarmBoot,
       "wfRRedundSlot": wfRRedundSlot,
       "wfRRedundSlotMask": wfRRedundSlotMask,
       "wfRRedundAtmDeathTimer": wfRRedundAtmDeathTimer,
       "wfRRedundCctTable": wfRRedundCctTable,
       "wfRRedundCctEntry": wfRRedundCctEntry,
       "wfRRedundCctDelete": wfRRedundCctDelete,
       "wfRRedundCctDisable": wfRRedundCctDisable,
       "wfRRedundCctCct": wfRRedundCctCct,
       "wfRRedundCctPrimaryMACAddr": wfRRedundCctPrimaryMACAddr,
       "wfRRedundCctMonitor": wfRRedundCctMonitor,
       "wfRRedundCctRSwitchOnFailure": wfRRedundCctRSwitchOnFailure,
       "wfRRedundCctSendPduDisable": wfRRedundCctSendPduDisable,
       "wfRRedundCctStatus": wfRRedundCctStatus,
       "wfRRedundCctSONMPXmtCount": wfRRedundCctSONMPXmtCount,
       "wfRRedundCctSONMPRcvCount": wfRRedundCctSONMPRcvCount,
       "wfRRedundCctSONMPRcvErrorCount": wfRRedundCctSONMPRcvErrorCount,
       "wfRRedundResourceTable": wfRRedundResourceTable,
       "wfRRedundResourceEntry": wfRRedundResourceEntry,
       "wfRRedundResourceDelete": wfRRedundResourceDelete,
       "wfRRedundResourceDisable": wfRRedundResourceDisable,
       "wfRRedundResourceCircuitNumber": wfRRedundResourceCircuitNumber,
       "wfRRedundResourceNetAddr": wfRRedundResourceNetAddr,
       "wfRRedundResourceStatus": wfRRedundResourceStatus,
       "wfRRedundResourceStatusUpdateDisable": wfRRedundResourceStatusUpdateDisable,
       "wfRRedundResourcePingIntervalTimer": wfRRedundResourcePingIntervalTimer,
       "wfRRedundResourcePingRetryCount": wfRRedundResourcePingRetryCount,
       "wfRRedundResourcePingTimeOut": wfRRedundResourcePingTimeOut,
       "wfRRedundRemoteMemberTable": wfRRedundRemoteMemberTable,
       "wfRRedundRemoteMemberEntry": wfRRedundRemoteMemberEntry,
       "wfRRedundRemoteMemberDelete": wfRRedundRemoteMemberDelete,
       "wfRRedundRemoteMemberGroupId": wfRRedundRemoteMemberGroupId,
       "wfRRedundRemoteMemberId": wfRRedundRemoteMemberId,
       "wfRRedundRemoteMemberNetAddr": wfRRedundRemoteMemberNetAddr,
       "wfRRedundRemoteMemberRole": wfRRedundRemoteMemberRole,
       "wfRRedundRemoteMemberState": wfRRedundRemoteMemberState,
       "wfRRedundRemoteMemberRefNum": wfRRedundRemoteMemberRefNum,
       "wfRRedundRemoteMemberPriority": wfRRedundRemoteMemberPriority,
       "wfRRedundRemoteMemberGoodIfCnt": wfRRedundRemoteMemberGoodIfCnt,
       "wfRRedundRemoteMemberGoodResCnt": wfRRedundRemoteMemberGoodResCnt,
       "wfRRedundRemoteMemberIfCnt": wfRRedundRemoteMemberIfCnt,
       "wfRRedundRemoteMemberLocalIfReachCnt": wfRRedundRemoteMemberLocalIfReachCnt}
)
