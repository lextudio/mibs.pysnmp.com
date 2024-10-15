# SNMP MIB module (SUN-HW-CTRL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SUN-HW-CTRL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:32 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sunHwCtrlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104)
)
sunHwCtrlMIB.setRevisions(
        ("2010-01-04 00:00",
         "2009-08-20 00:00",
         "2009-07-28 00:00",
         "2009-03-01 00:00",
         "2008-09-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SunHwCtrlPowerMgmtID(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class SunHwCtrlPowerMgmtPolicy(Integer32, TextualConvention):
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
        *(("elastic", 4),
          ("notsupported", 1),
          ("performance", 3),
          ("unknown", 2))
    )



class SunHwCtrlPowerMgmtBudgetTimelimitActions(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Sun_ObjectIdentity = ObjectIdentity
sun = _Sun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2)
)
_Ilom_ObjectIdentity = ObjectIdentity
ilom = _Ilom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175)
)
_SunHwCtrlMIBObjects_ObjectIdentity = ObjectIdentity
sunHwCtrlMIBObjects = _SunHwCtrlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1)
)
_SunHwCtrlPowerMgmt_ObjectIdentity = ObjectIdentity
sunHwCtrlPowerMgmt = _SunHwCtrlPowerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6)
)
_SunHwCtrlReservedPSU_Type = Integer32
_SunHwCtrlReservedPSU_Object = MibScalar
sunHwCtrlReservedPSU = _SunHwCtrlReservedPSU_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 1),
    _SunHwCtrlReservedPSU_Type()
)
sunHwCtrlReservedPSU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlReservedPSU.setStatus("current")
_SunHwCtrlTotalPSU_Type = Integer32
_SunHwCtrlTotalPSU_Object = MibScalar
sunHwCtrlTotalPSU = _SunHwCtrlTotalPSU_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 2),
    _SunHwCtrlTotalPSU_Type()
)
sunHwCtrlTotalPSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlTotalPSU.setStatus("current")
_SunHwCtrlPowerMgmtTable_Object = MibTable
sunHwCtrlPowerMgmtTable = _SunHwCtrlPowerMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3)
)
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtTable.setStatus("current")
_SunHwCtrlPowerMgmtEntry_Object = MibTableRow
sunHwCtrlPowerMgmtEntry = _SunHwCtrlPowerMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1)
)
sunHwCtrlPowerMgmtEntry.setIndexNames(
    (0, "SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtID"),
)
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtEntry.setStatus("current")
_SunHwCtrlPowerMgmtID_Type = SunHwCtrlPowerMgmtID
_SunHwCtrlPowerMgmtID_Object = MibTableColumn
sunHwCtrlPowerMgmtID = _SunHwCtrlPowerMgmtID_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 1),
    _SunHwCtrlPowerMgmtID_Type()
)
sunHwCtrlPowerMgmtID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtID.setStatus("current")
_SunHwCtrlPowerMgmtName_Type = SnmpAdminString
_SunHwCtrlPowerMgmtName_Object = MibTableColumn
sunHwCtrlPowerMgmtName = _SunHwCtrlPowerMgmtName_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 2),
    _SunHwCtrlPowerMgmtName_Type()
)
sunHwCtrlPowerMgmtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtName.setStatus("current")
_SunHwCtrlPowerMgmtUnits_Type = SnmpAdminString
_SunHwCtrlPowerMgmtUnits_Object = MibTableColumn
sunHwCtrlPowerMgmtUnits = _SunHwCtrlPowerMgmtUnits_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 3),
    _SunHwCtrlPowerMgmtUnits_Type()
)
sunHwCtrlPowerMgmtUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtUnits.setStatus("current")
_SunHwCtrlPowerMgmtValue_Type = SnmpAdminString
_SunHwCtrlPowerMgmtValue_Object = MibTableColumn
sunHwCtrlPowerMgmtValue = _SunHwCtrlPowerMgmtValue_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 3, 1, 4),
    _SunHwCtrlPowerMgmtValue_Type()
)
sunHwCtrlPowerMgmtValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtValue.setStatus("current")
_SunHwCtrlPowerMgmtActualPower_Type = Integer32
_SunHwCtrlPowerMgmtActualPower_Object = MibScalar
sunHwCtrlPowerMgmtActualPower = _SunHwCtrlPowerMgmtActualPower_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 4),
    _SunHwCtrlPowerMgmtActualPower_Type()
)
sunHwCtrlPowerMgmtActualPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtActualPower.setStatus("current")
_SunHwCtrlPowerMgmtPermittedPower_Type = Integer32
_SunHwCtrlPowerMgmtPermittedPower_Object = MibScalar
sunHwCtrlPowerMgmtPermittedPower = _SunHwCtrlPowerMgmtPermittedPower_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 5),
    _SunHwCtrlPowerMgmtPermittedPower_Type()
)
sunHwCtrlPowerMgmtPermittedPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtPermittedPower.setStatus("current")
_SunHwCtrlPowerMgmtAvailablePower_Type = Integer32
_SunHwCtrlPowerMgmtAvailablePower_Object = MibScalar
sunHwCtrlPowerMgmtAvailablePower = _SunHwCtrlPowerMgmtAvailablePower_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 6),
    _SunHwCtrlPowerMgmtAvailablePower_Type()
)
sunHwCtrlPowerMgmtAvailablePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtAvailablePower.setStatus("current")
_SunHwCtrlPowerMgmtPolicy_Type = SunHwCtrlPowerMgmtPolicy
_SunHwCtrlPowerMgmtPolicy_Object = MibScalar
sunHwCtrlPowerMgmtPolicy = _SunHwCtrlPowerMgmtPolicy_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 7),
    _SunHwCtrlPowerMgmtPolicy_Type()
)
sunHwCtrlPowerMgmtPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtPolicy.setStatus("current")
_SunHwCtrlPowerMgmtBudgetSettings_ObjectIdentity = ObjectIdentity
sunHwCtrlPowerMgmtBudgetSettings = _SunHwCtrlPowerMgmtBudgetSettings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9)
)


class _SunHwCtrlPowerMgmtBudget_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtBudget based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 3),
          ("enabledPostPoweron", 4),
          ("unknown", 1))
    )


_SunHwCtrlPowerMgmtBudget_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtBudget_Object = MibScalar
sunHwCtrlPowerMgmtBudget = _SunHwCtrlPowerMgmtBudget_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 1),
    _SunHwCtrlPowerMgmtBudget_Type()
)
sunHwCtrlPowerMgmtBudget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudget.setStatus("current")


class _SunHwCtrlPowerMgmtBudgetMinPowerlimit_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtBudgetMinPowerlimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtBudgetMinPowerlimit_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtBudgetMinPowerlimit_Object = MibScalar
sunHwCtrlPowerMgmtBudgetMinPowerlimit = _SunHwCtrlPowerMgmtBudgetMinPowerlimit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 2),
    _SunHwCtrlPowerMgmtBudgetMinPowerlimit_Type()
)
sunHwCtrlPowerMgmtBudgetMinPowerlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetMinPowerlimit.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetMinPowerlimit.setUnits("watts")


class _SunHwCtrlPowerMgmtBudgetPowerlimit_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtBudgetPowerlimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtBudgetPowerlimit_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtBudgetPowerlimit_Object = MibScalar
sunHwCtrlPowerMgmtBudgetPowerlimit = _SunHwCtrlPowerMgmtBudgetPowerlimit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 3),
    _SunHwCtrlPowerMgmtBudgetPowerlimit_Type()
)
sunHwCtrlPowerMgmtBudgetPowerlimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPowerlimit.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPowerlimit.setUnits("watts")


class _SunHwCtrlPowerMgmtBudgetTimelimit_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtBudgetTimelimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtBudgetTimelimit_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtBudgetTimelimit_Object = MibScalar
sunHwCtrlPowerMgmtBudgetTimelimit = _SunHwCtrlPowerMgmtBudgetTimelimit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 5),
    _SunHwCtrlPowerMgmtBudgetTimelimit_Type()
)
sunHwCtrlPowerMgmtBudgetTimelimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetTimelimit.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetTimelimit.setUnits("milliseconds")
_SunHwCtrlPowerMgmtBudgetTimelimitActions_Type = SunHwCtrlPowerMgmtBudgetTimelimitActions
_SunHwCtrlPowerMgmtBudgetTimelimitActions_Object = MibScalar
sunHwCtrlPowerMgmtBudgetTimelimitActions = _SunHwCtrlPowerMgmtBudgetTimelimitActions_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 6),
    _SunHwCtrlPowerMgmtBudgetTimelimitActions_Type()
)
sunHwCtrlPowerMgmtBudgetTimelimitActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetTimelimitActions.setStatus("current")
_SunHwCtrlPowerMgmtBudgetOK_Type = TruthValue
_SunHwCtrlPowerMgmtBudgetOK_Object = MibScalar
sunHwCtrlPowerMgmtBudgetOK = _SunHwCtrlPowerMgmtBudgetOK_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 7),
    _SunHwCtrlPowerMgmtBudgetOK_Type()
)
sunHwCtrlPowerMgmtBudgetOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetOK.setStatus("current")
_SunHwCtrlPowerMgmtBudgetCommitPending_Type = TruthValue
_SunHwCtrlPowerMgmtBudgetCommitPending_Object = MibScalar
sunHwCtrlPowerMgmtBudgetCommitPending = _SunHwCtrlPowerMgmtBudgetCommitPending_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 100),
    _SunHwCtrlPowerMgmtBudgetCommitPending_Type()
)
sunHwCtrlPowerMgmtBudgetCommitPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetCommitPending.setStatus("current")


class _SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtBudgetPendingPowerlimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Object = MibScalar
sunHwCtrlPowerMgmtBudgetPendingPowerlimit = _SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 103),
    _SunHwCtrlPowerMgmtBudgetPendingPowerlimit_Type()
)
sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPendingPowerlimit.setUnits("watts")


class _SunHwCtrlPowerMgmtBudgetPendingTimelimit_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtBudgetPendingTimelimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_SunHwCtrlPowerMgmtBudgetPendingTimelimit_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtBudgetPendingTimelimit_Object = MibScalar
sunHwCtrlPowerMgmtBudgetPendingTimelimit = _SunHwCtrlPowerMgmtBudgetPendingTimelimit_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 105),
    _SunHwCtrlPowerMgmtBudgetPendingTimelimit_Type()
)
sunHwCtrlPowerMgmtBudgetPendingTimelimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPendingTimelimit.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPendingTimelimit.setUnits("milliseconds")
_SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Type = SunHwCtrlPowerMgmtBudgetTimelimitActions
_SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Object = MibScalar
sunHwCtrlPowerMgmtBudgetPendingTimelimitActions = _SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 9, 106),
    _SunHwCtrlPowerMgmtBudgetPendingTimelimitActions_Type()
)
sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtBudgetPendingTimelimitActions.setStatus("current")
_SunHwCtrlPowerMgmtConsumptionThresholds_ObjectIdentity = ObjectIdentity
sunHwCtrlPowerMgmtConsumptionThresholds = _SunHwCtrlPowerMgmtConsumptionThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10)
)


class _SunHwCtrlPowerMgmtConsumptionThreshold1_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtConsumptionThreshold1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SunHwCtrlPowerMgmtConsumptionThreshold1_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtConsumptionThreshold1_Object = MibScalar
sunHwCtrlPowerMgmtConsumptionThreshold1 = _SunHwCtrlPowerMgmtConsumptionThreshold1_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10, 1),
    _SunHwCtrlPowerMgmtConsumptionThreshold1_Type()
)
sunHwCtrlPowerMgmtConsumptionThreshold1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtConsumptionThreshold1.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtConsumptionThreshold1.setUnits("watts")


class _SunHwCtrlPowerMgmtConsumptionThreshold2_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtConsumptionThreshold2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SunHwCtrlPowerMgmtConsumptionThreshold2_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtConsumptionThreshold2_Object = MibScalar
sunHwCtrlPowerMgmtConsumptionThreshold2 = _SunHwCtrlPowerMgmtConsumptionThreshold2_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 10, 2),
    _SunHwCtrlPowerMgmtConsumptionThreshold2_Type()
)
sunHwCtrlPowerMgmtConsumptionThreshold2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtConsumptionThreshold2.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtConsumptionThreshold2.setUnits("watts")
_SunHwCtrlPowerMgmtSampling_ObjectIdentity = ObjectIdentity
sunHwCtrlPowerMgmtSampling = _SunHwCtrlPowerMgmtSampling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11)
)


class _SunHwCtrlPowerMgmtSamplingPeriod_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtSamplingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtSamplingPeriod_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtSamplingPeriod_Object = MibScalar
sunHwCtrlPowerMgmtSamplingPeriod = _SunHwCtrlPowerMgmtSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 1),
    _SunHwCtrlPowerMgmtSamplingPeriod_Type()
)
sunHwCtrlPowerMgmtSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingPeriod.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingPeriod.setUnits("seconds")
_SunHwCtrlPowerMgmtSamplingTimestamp_Type = DateAndTime
_SunHwCtrlPowerMgmtSamplingTimestamp_Object = MibScalar
sunHwCtrlPowerMgmtSamplingTimestamp = _SunHwCtrlPowerMgmtSamplingTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 2),
    _SunHwCtrlPowerMgmtSamplingTimestamp_Type()
)
sunHwCtrlPowerMgmtSamplingTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingTimestamp.setStatus("current")


class _SunHwCtrlPowerMgmtSamplingMinimumPower_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtSamplingMinimumPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtSamplingMinimumPower_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtSamplingMinimumPower_Object = MibScalar
sunHwCtrlPowerMgmtSamplingMinimumPower = _SunHwCtrlPowerMgmtSamplingMinimumPower_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 3),
    _SunHwCtrlPowerMgmtSamplingMinimumPower_Type()
)
sunHwCtrlPowerMgmtSamplingMinimumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingMinimumPower.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingMinimumPower.setUnits("watts")


class _SunHwCtrlPowerMgmtSamplingMaximumPower_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtSamplingMaximumPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtSamplingMaximumPower_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtSamplingMaximumPower_Object = MibScalar
sunHwCtrlPowerMgmtSamplingMaximumPower = _SunHwCtrlPowerMgmtSamplingMaximumPower_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 4),
    _SunHwCtrlPowerMgmtSamplingMaximumPower_Type()
)
sunHwCtrlPowerMgmtSamplingMaximumPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingMaximumPower.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingMaximumPower.setUnits("watts")


class _SunHwCtrlPowerMgmtSamplingAveragePower_Type(Integer32):
    """Custom type sunHwCtrlPowerMgmtSamplingAveragePower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SunHwCtrlPowerMgmtSamplingAveragePower_Type.__name__ = "Integer32"
_SunHwCtrlPowerMgmtSamplingAveragePower_Object = MibScalar
sunHwCtrlPowerMgmtSamplingAveragePower = _SunHwCtrlPowerMgmtSamplingAveragePower_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 6, 11, 5),
    _SunHwCtrlPowerMgmtSamplingAveragePower_Type()
)
sunHwCtrlPowerMgmtSamplingAveragePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingAveragePower.setStatus("current")
if mibBuilder.loadTexts:
    sunHwCtrlPowerMgmtSamplingAveragePower.setUnits("watts")
_SunHwCtrlTPM_ObjectIdentity = ObjectIdentity
sunHwCtrlTPM = _SunHwCtrlTPM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7)
)
_SunHwCtrlTpmEnable_Type = TruthValue
_SunHwCtrlTpmEnable_Object = MibScalar
sunHwCtrlTpmEnable = _SunHwCtrlTpmEnable_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 1),
    _SunHwCtrlTpmEnable_Type()
)
sunHwCtrlTpmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlTpmEnable.setStatus("current")
_SunHwCtrlTpmActivate_Type = TruthValue
_SunHwCtrlTpmActivate_Object = MibScalar
sunHwCtrlTpmActivate = _SunHwCtrlTpmActivate_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 2),
    _SunHwCtrlTpmActivate_Type()
)
sunHwCtrlTpmActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlTpmActivate.setStatus("current")
_SunHwCtrlTpmForceClear_Type = TruthValue
_SunHwCtrlTpmForceClear_Object = MibScalar
sunHwCtrlTpmForceClear = _SunHwCtrlTpmForceClear_Object(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 1, 7, 3),
    _SunHwCtrlTpmForceClear_Type()
)
sunHwCtrlTpmForceClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sunHwCtrlTpmForceClear.setStatus("current")
_SunHwCtrlMIBConformances_ObjectIdentity = ObjectIdentity
sunHwCtrlMIBConformances = _SunHwCtrlMIBConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2)
)
_SunHwCtrlCompliances_ObjectIdentity = ObjectIdentity
sunHwCtrlCompliances = _SunHwCtrlCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 1)
)
_SunHwCtrlGroups_ObjectIdentity = ObjectIdentity
sunHwCtrlGroups = _SunHwCtrlGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 2)
)

# Managed Objects groups

sunHwCtrlObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 42, 2, 175, 104, 2, 2, 1)
)
sunHwCtrlObjectsGroup.setObjects(
      *(("SUN-HW-CTRL-MIB", "sunHwCtrlReservedPSU"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlTotalPSU"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtName"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtUnits"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtValue"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtActualPower"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtPermittedPower"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtAvailablePower"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtPolicy"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudget"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetMinPowerlimit"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPowerlimit"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetTimelimit"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetTimelimitActions"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetOK"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetCommitPending"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingPowerlimit"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingTimelimit"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtBudgetPendingTimelimitActions"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtConsumptionThreshold1"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtConsumptionThreshold2"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingPeriod"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingTimestamp"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingMinimumPower"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingMaximumPower"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlPowerMgmtSamplingAveragePower"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmEnable"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmActivate"),
        ("SUN-HW-CTRL-MIB", "sunHwCtrlTpmForceClear"))
)
if mibBuilder.loadTexts:
    sunHwCtrlObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUN-HW-CTRL-MIB",
    **{"SunHwCtrlPowerMgmtID": SunHwCtrlPowerMgmtID,
       "SunHwCtrlPowerMgmtPolicy": SunHwCtrlPowerMgmtPolicy,
       "SunHwCtrlPowerMgmtBudgetTimelimitActions": SunHwCtrlPowerMgmtBudgetTimelimitActions,
       "sun": sun,
       "products": products,
       "ilom": ilom,
       "sunHwCtrlMIB": sunHwCtrlMIB,
       "sunHwCtrlMIBObjects": sunHwCtrlMIBObjects,
       "sunHwCtrlPowerMgmt": sunHwCtrlPowerMgmt,
       "sunHwCtrlReservedPSU": sunHwCtrlReservedPSU,
       "sunHwCtrlTotalPSU": sunHwCtrlTotalPSU,
       "sunHwCtrlPowerMgmtTable": sunHwCtrlPowerMgmtTable,
       "sunHwCtrlPowerMgmtEntry": sunHwCtrlPowerMgmtEntry,
       "sunHwCtrlPowerMgmtID": sunHwCtrlPowerMgmtID,
       "sunHwCtrlPowerMgmtName": sunHwCtrlPowerMgmtName,
       "sunHwCtrlPowerMgmtUnits": sunHwCtrlPowerMgmtUnits,
       "sunHwCtrlPowerMgmtValue": sunHwCtrlPowerMgmtValue,
       "sunHwCtrlPowerMgmtActualPower": sunHwCtrlPowerMgmtActualPower,
       "sunHwCtrlPowerMgmtPermittedPower": sunHwCtrlPowerMgmtPermittedPower,
       "sunHwCtrlPowerMgmtAvailablePower": sunHwCtrlPowerMgmtAvailablePower,
       "sunHwCtrlPowerMgmtPolicy": sunHwCtrlPowerMgmtPolicy,
       "sunHwCtrlPowerMgmtBudgetSettings": sunHwCtrlPowerMgmtBudgetSettings,
       "sunHwCtrlPowerMgmtBudget": sunHwCtrlPowerMgmtBudget,
       "sunHwCtrlPowerMgmtBudgetMinPowerlimit": sunHwCtrlPowerMgmtBudgetMinPowerlimit,
       "sunHwCtrlPowerMgmtBudgetPowerlimit": sunHwCtrlPowerMgmtBudgetPowerlimit,
       "sunHwCtrlPowerMgmtBudgetTimelimit": sunHwCtrlPowerMgmtBudgetTimelimit,
       "sunHwCtrlPowerMgmtBudgetTimelimitActions": sunHwCtrlPowerMgmtBudgetTimelimitActions,
       "sunHwCtrlPowerMgmtBudgetOK": sunHwCtrlPowerMgmtBudgetOK,
       "sunHwCtrlPowerMgmtBudgetCommitPending": sunHwCtrlPowerMgmtBudgetCommitPending,
       "sunHwCtrlPowerMgmtBudgetPendingPowerlimit": sunHwCtrlPowerMgmtBudgetPendingPowerlimit,
       "sunHwCtrlPowerMgmtBudgetPendingTimelimit": sunHwCtrlPowerMgmtBudgetPendingTimelimit,
       "sunHwCtrlPowerMgmtBudgetPendingTimelimitActions": sunHwCtrlPowerMgmtBudgetPendingTimelimitActions,
       "sunHwCtrlPowerMgmtConsumptionThresholds": sunHwCtrlPowerMgmtConsumptionThresholds,
       "sunHwCtrlPowerMgmtConsumptionThreshold1": sunHwCtrlPowerMgmtConsumptionThreshold1,
       "sunHwCtrlPowerMgmtConsumptionThreshold2": sunHwCtrlPowerMgmtConsumptionThreshold2,
       "sunHwCtrlPowerMgmtSampling": sunHwCtrlPowerMgmtSampling,
       "sunHwCtrlPowerMgmtSamplingPeriod": sunHwCtrlPowerMgmtSamplingPeriod,
       "sunHwCtrlPowerMgmtSamplingTimestamp": sunHwCtrlPowerMgmtSamplingTimestamp,
       "sunHwCtrlPowerMgmtSamplingMinimumPower": sunHwCtrlPowerMgmtSamplingMinimumPower,
       "sunHwCtrlPowerMgmtSamplingMaximumPower": sunHwCtrlPowerMgmtSamplingMaximumPower,
       "sunHwCtrlPowerMgmtSamplingAveragePower": sunHwCtrlPowerMgmtSamplingAveragePower,
       "sunHwCtrlTPM": sunHwCtrlTPM,
       "sunHwCtrlTpmEnable": sunHwCtrlTpmEnable,
       "sunHwCtrlTpmActivate": sunHwCtrlTpmActivate,
       "sunHwCtrlTpmForceClear": sunHwCtrlTpmForceClear,
       "sunHwCtrlMIBConformances": sunHwCtrlMIBConformances,
       "sunHwCtrlCompliances": sunHwCtrlCompliances,
       "sunHwCtrlGroups": sunHwCtrlGroups,
       "sunHwCtrlObjectsGroup": sunHwCtrlObjectsGroup}
)
