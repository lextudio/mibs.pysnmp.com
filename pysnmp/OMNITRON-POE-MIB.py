# SNMP MIB module (OMNITRON-POE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OMNITRON-POE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:34:43 2024
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

(OstFloatValue,
 OstPortSingleIndex,
 omnitron) = mibBuilder.importSymbols(
    "OMNITRON-TC-MIB",
    "OstFloatValue",
    "OstPortSingleIndex",
    "omnitron")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

omnitronPoeMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 15)
)
omnitronPoeMib.setRevisions(
        ("2015-01-19 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OstPoeGlobalCfgTable_ObjectIdentity = ObjectIdentity
ostPoeGlobalCfgTable = _OstPoeGlobalCfgTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 15, 1)
)


class _OstPoeGlobalCfgPwrLimitationEnable_Type(TruthValue):
    """Custom type ostPoeGlobalCfgPwrLimitationEnable based on TruthValue"""


_OstPoeGlobalCfgPwrLimitationEnable_Object = MibScalar
ostPoeGlobalCfgPwrLimitationEnable = _OstPoeGlobalCfgPwrLimitationEnable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 1, 1),
    _OstPoeGlobalCfgPwrLimitationEnable_Type()
)
ostPoeGlobalCfgPwrLimitationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoeGlobalCfgPwrLimitationEnable.setStatus("current")


class _OstPoeGlobalCfgTotalPwr_Type(OstFloatValue):
    """Custom type ostPoeGlobalCfgTotalPwr based on OstFloatValue"""
    defaultValue = OctetString("0.0")


_OstPoeGlobalCfgTotalPwr_Object = MibScalar
ostPoeGlobalCfgTotalPwr = _OstPoeGlobalCfgTotalPwr_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 1, 2),
    _OstPoeGlobalCfgTotalPwr_Type()
)
ostPoeGlobalCfgTotalPwr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostPoeGlobalCfgTotalPwr.setStatus("current")
_OstPoePortCfgTable_Object = MibTable
ostPoePortCfgTable = _OstPoePortCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2)
)
if mibBuilder.loadTexts:
    ostPoePortCfgTable.setStatus("current")
_OstPoePortCfgEntry_Object = MibTableRow
ostPoePortCfgEntry = _OstPoePortCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1)
)
ostPoePortCfgEntry.setIndexNames(
    (0, "OMNITRON-POE-MIB", "ostPoePortCfgIndex"),
)
if mibBuilder.loadTexts:
    ostPoePortCfgEntry.setStatus("current")
_OstPoePortCfgIndex_Type = OstPortSingleIndex
_OstPoePortCfgIndex_Object = MibTableColumn
ostPoePortCfgIndex = _OstPoePortCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 1),
    _OstPoePortCfgIndex_Type()
)
ostPoePortCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ostPoePortCfgIndex.setStatus("current")


class _OstPoePortPseEnable_Type(Integer32):
    """Custom type ostPoePortPseEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pseDisabled", 1),
          ("pseEnabled", 2))
    )


_OstPoePortPseEnable_Type.__name__ = "Integer32"
_OstPoePortPseEnable_Object = MibTableColumn
ostPoePortPseEnable = _OstPoePortPseEnable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 2),
    _OstPoePortPseEnable_Type()
)
ostPoePortPseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortPseEnable.setStatus("current")


class _OstPoePortPse60wMode_Type(Integer32):
    """Custom type ostPoePortPse60wMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pse60wAuto", 1),
          ("pse60wForce", 2),
          ("pse60wNotAvail", 0))
    )


_OstPoePortPse60wMode_Type.__name__ = "Integer32"
_OstPoePortPse60wMode_Object = MibTableColumn
ostPoePortPse60wMode = _OstPoePortPse60wMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 3),
    _OstPoePortPse60wMode_Type()
)
ostPoePortPse60wMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortPse60wMode.setStatus("current")


class _OstPoePortPdMode_Type(Integer32):
    """Custom type ostPoePortPdMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("pdMode60W", 9),
          ("pdModeClass0", 4),
          ("pdModeClass1", 5),
          ("pdModeClass2", 6),
          ("pdModeClass3", 7),
          ("pdModeClass4", 8),
          ("pdModeFailure", 3),
          ("pdModeNotClassified", 2),
          ("pdModeNotDetected", 1))
    )


_OstPoePortPdMode_Type.__name__ = "Integer32"
_OstPoePortPdMode_Object = MibTableColumn
ostPoePortPdMode = _OstPoePortPdMode_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 4),
    _OstPoePortPdMode_Type()
)
ostPoePortPdMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostPoePortPdMode.setStatus("current")


class _OstPoePortPseVoltageSupplied_Type(OstFloatValue):
    """Custom type ostPoePortPseVoltageSupplied based on OstFloatValue"""
    defaultValue = OctetString("0.0")


_OstPoePortPseVoltageSupplied_Object = MibTableColumn
ostPoePortPseVoltageSupplied = _OstPoePortPseVoltageSupplied_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 5),
    _OstPoePortPseVoltageSupplied_Type()
)
ostPoePortPseVoltageSupplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostPoePortPseVoltageSupplied.setStatus("current")


class _OstPoePortPseCurrentSupplied_Type(OstFloatValue):
    """Custom type ostPoePortPseCurrentSupplied based on OstFloatValue"""
    defaultValue = OctetString("0.0")


_OstPoePortPseCurrentSupplied_Object = MibTableColumn
ostPoePortPseCurrentSupplied = _OstPoePortPseCurrentSupplied_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 6),
    _OstPoePortPseCurrentSupplied_Type()
)
ostPoePortPseCurrentSupplied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostPoePortPseCurrentSupplied.setStatus("current")


class _OstPoePortPseStatus_Type(Integer32):
    """Custom type ostPoePortPseStatus based on Integer32"""
    defaultValue = 1

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
        *(("notApplicable", 1),
          ("pdBrownOut", 4),
          ("pdInsufficientPower", 5),
          ("pdNormal", 2),
          ("pdOverCurrent", 3))
    )


_OstPoePortPseStatus_Type.__name__ = "Integer32"
_OstPoePortPseStatus_Object = MibTableColumn
ostPoePortPseStatus = _OstPoePortPseStatus_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 7),
    _OstPoePortPseStatus_Type()
)
ostPoePortPseStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortPseStatus.setStatus("current")


class _OstPoePortHeartbeatEnable_Type(Integer32):
    """Custom type ostPoePortHeartbeatEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("heartbeatDisabled", 1),
          ("heartbeatEnabled", 2))
    )


_OstPoePortHeartbeatEnable_Type.__name__ = "Integer32"
_OstPoePortHeartbeatEnable_Object = MibTableColumn
ostPoePortHeartbeatEnable = _OstPoePortHeartbeatEnable_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 8),
    _OstPoePortHeartbeatEnable_Type()
)
ostPoePortHeartbeatEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortHeartbeatEnable.setStatus("current")


class _OstPoePortHeartbeatIpAddress_Type(IpAddress):
    """Custom type ostPoePortHeartbeatIpAddress based on IpAddress"""
    defaultHexValue = "00000000"


_OstPoePortHeartbeatIpAddress_Object = MibTableColumn
ostPoePortHeartbeatIpAddress = _OstPoePortHeartbeatIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 9),
    _OstPoePortHeartbeatIpAddress_Type()
)
ostPoePortHeartbeatIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortHeartbeatIpAddress.setStatus("current")


class _OstPoePortHeartbeatInterval_Type(Unsigned32):
    """Custom type ostPoePortHeartbeatInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OstPoePortHeartbeatInterval_Type.__name__ = "Unsigned32"
_OstPoePortHeartbeatInterval_Object = MibTableColumn
ostPoePortHeartbeatInterval = _OstPoePortHeartbeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 10),
    _OstPoePortHeartbeatInterval_Type()
)
ostPoePortHeartbeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortHeartbeatInterval.setStatus("current")


class _OstPoePortHeartbeatErrorDetection_Type(Unsigned32):
    """Custom type ostPoePortHeartbeatErrorDetection based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_OstPoePortHeartbeatErrorDetection_Type.__name__ = "Unsigned32"
_OstPoePortHeartbeatErrorDetection_Object = MibTableColumn
ostPoePortHeartbeatErrorDetection = _OstPoePortHeartbeatErrorDetection_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 11),
    _OstPoePortHeartbeatErrorDetection_Type()
)
ostPoePortHeartbeatErrorDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortHeartbeatErrorDetection.setStatus("current")


class _OstPoePortHeartbeatErrorAction_Type(Integer32):
    """Custom type ostPoePortHeartbeatErrorAction based on Integer32"""
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
        *(("errorLostIgnored", 1),
          ("errorRestart", 2),
          ("errorShutdown", 3))
    )


_OstPoePortHeartbeatErrorAction_Type.__name__ = "Integer32"
_OstPoePortHeartbeatErrorAction_Object = MibTableColumn
ostPoePortHeartbeatErrorAction = _OstPoePortHeartbeatErrorAction_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 12),
    _OstPoePortHeartbeatErrorAction_Type()
)
ostPoePortHeartbeatErrorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortHeartbeatErrorAction.setStatus("current")


class _OstPoePortHeartbeatNumberRestarts_Type(Unsigned32):
    """Custom type ostPoePortHeartbeatNumberRestarts based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16384),
    )


_OstPoePortHeartbeatNumberRestarts_Type.__name__ = "Unsigned32"
_OstPoePortHeartbeatNumberRestarts_Object = MibTableColumn
ostPoePortHeartbeatNumberRestarts = _OstPoePortHeartbeatNumberRestarts_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 13),
    _OstPoePortHeartbeatNumberRestarts_Type()
)
ostPoePortHeartbeatNumberRestarts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoePortHeartbeatNumberRestarts.setStatus("current")


class _OstPoEPortHeartbeatStatus_Type(Integer32):
    """Custom type ostPoEPortHeartbeatStatus based on Integer32"""
    defaultValue = 1

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
        *(("heartbeatAvailable", 2),
          ("heartbeatDisabled", 1),
          ("heartbeatErrored", 3),
          ("heartbeatRestart", 4),
          ("heartbeatShutdown", 5))
    )


_OstPoEPortHeartbeatStatus_Type.__name__ = "Integer32"
_OstPoEPortHeartbeatStatus_Object = MibTableColumn
ostPoEPortHeartbeatStatus = _OstPoEPortHeartbeatStatus_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 14),
    _OstPoEPortHeartbeatStatus_Type()
)
ostPoEPortHeartbeatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ostPoEPortHeartbeatStatus.setStatus("current")


class _OstPoEPortHeartbeatDeferTime_Type(Unsigned32):
    """Custom type ostPoEPortHeartbeatDeferTime based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_OstPoEPortHeartbeatDeferTime_Type.__name__ = "Unsigned32"
_OstPoEPortHeartbeatDeferTime_Object = MibTableColumn
ostPoEPortHeartbeatDeferTime = _OstPoEPortHeartbeatDeferTime_Object(
    (1, 3, 6, 1, 4, 1, 7342, 15, 2, 1, 15),
    _OstPoEPortHeartbeatDeferTime_Type()
)
ostPoEPortHeartbeatDeferTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ostPoEPortHeartbeatDeferTime.setStatus("current")
_OstPoeCompliances_ObjectIdentity = ObjectIdentity
ostPoeCompliances = _OstPoeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 15, 3)
)
_OstPoeGroups_ObjectIdentity = ObjectIdentity
ostPoeGroups = _OstPoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7342, 15, 4)
)

# Managed Objects groups

ostPoeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7342, 15, 4, 1)
)
ostPoeGroup.setObjects(
      *(("OMNITRON-POE-MIB", "ostPoeGlobalCfgPwrLimitationEnable"),
        ("OMNITRON-POE-MIB", "ostPoeGlobalCfgTotalPwr"),
        ("OMNITRON-POE-MIB", "ostPoePortPseEnable"),
        ("OMNITRON-POE-MIB", "ostPoePortPse60wMode"),
        ("OMNITRON-POE-MIB", "ostPoePortPdMode"),
        ("OMNITRON-POE-MIB", "ostPoePortPseVoltageSupplied"),
        ("OMNITRON-POE-MIB", "ostPoePortPseCurrentSupplied"),
        ("OMNITRON-POE-MIB", "ostPoePortPseStatus"),
        ("OMNITRON-POE-MIB", "ostPoePortHeartbeatEnable"),
        ("OMNITRON-POE-MIB", "ostPoePortHeartbeatIpAddress"),
        ("OMNITRON-POE-MIB", "ostPoePortHeartbeatInterval"),
        ("OMNITRON-POE-MIB", "ostPoePortHeartbeatErrorDetection"),
        ("OMNITRON-POE-MIB", "ostPoePortHeartbeatErrorAction"),
        ("OMNITRON-POE-MIB", "ostPoePortHeartbeatNumberRestarts"),
        ("OMNITRON-POE-MIB", "ostPoEPortHeartbeatStatus"),
        ("OMNITRON-POE-MIB", "ostPoEPortHeartbeatDeferTime"))
)
if mibBuilder.loadTexts:
    ostPoeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ostPoeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7342, 15, 3, 2)
)
if mibBuilder.loadTexts:
    ostPoeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OMNITRON-POE-MIB",
    **{"omnitronPoeMib": omnitronPoeMib,
       "ostPoeGlobalCfgTable": ostPoeGlobalCfgTable,
       "ostPoeGlobalCfgPwrLimitationEnable": ostPoeGlobalCfgPwrLimitationEnable,
       "ostPoeGlobalCfgTotalPwr": ostPoeGlobalCfgTotalPwr,
       "ostPoePortCfgTable": ostPoePortCfgTable,
       "ostPoePortCfgEntry": ostPoePortCfgEntry,
       "ostPoePortCfgIndex": ostPoePortCfgIndex,
       "ostPoePortPseEnable": ostPoePortPseEnable,
       "ostPoePortPse60wMode": ostPoePortPse60wMode,
       "ostPoePortPdMode": ostPoePortPdMode,
       "ostPoePortPseVoltageSupplied": ostPoePortPseVoltageSupplied,
       "ostPoePortPseCurrentSupplied": ostPoePortPseCurrentSupplied,
       "ostPoePortPseStatus": ostPoePortPseStatus,
       "ostPoePortHeartbeatEnable": ostPoePortHeartbeatEnable,
       "ostPoePortHeartbeatIpAddress": ostPoePortHeartbeatIpAddress,
       "ostPoePortHeartbeatInterval": ostPoePortHeartbeatInterval,
       "ostPoePortHeartbeatErrorDetection": ostPoePortHeartbeatErrorDetection,
       "ostPoePortHeartbeatErrorAction": ostPoePortHeartbeatErrorAction,
       "ostPoePortHeartbeatNumberRestarts": ostPoePortHeartbeatNumberRestarts,
       "ostPoEPortHeartbeatStatus": ostPoEPortHeartbeatStatus,
       "ostPoEPortHeartbeatDeferTime": ostPoEPortHeartbeatDeferTime,
       "ostPoeCompliances": ostPoeCompliances,
       "ostPoeCompliance": ostPoeCompliance,
       "ostPoeGroups": ostPoeGroups,
       "ostPoeGroup": ostPoeGroup}
)
