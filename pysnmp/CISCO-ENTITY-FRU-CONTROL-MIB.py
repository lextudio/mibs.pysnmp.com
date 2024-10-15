# SNMP MIB module (CISCO-ENTITY-FRU-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-FRU-CONTROL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:49 2024
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

(entPhysicalClass,
 entPhysicalContainedIn,
 entPhysicalIndex,
 entPhysicalModelName,
 entPhysicalName,
 entPhysicalVendorType) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalClass",
    "entPhysicalContainedIn",
    "entPhysicalIndex",
    "entPhysicalModelName",
    "entPhysicalName",
    "entPhysicalVendorType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoEntityFRUControlMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117)
)
ciscoEntityFRUControlMIB.setRevisions(
        ("2013-08-19 00:00",
         "2011-12-22 00:00",
         "2011-03-18 00:00",
         "2010-12-10 00:00",
         "2008-10-08 00:00",
         "2007-06-21 00:00",
         "2007-03-14 00:00",
         "2006-06-23 00:00",
         "2005-09-06 00:00",
         "2004-12-09 00:00",
         "2004-10-19 00:00",
         "2003-11-24 00:00",
         "2003-10-27 00:00",
         "2003-10-23 00:00",
         "2003-07-22 00:00",
         "2002-10-16 00:00",
         "2002-10-03 00:00",
         "2002-09-15 00:00",
         "2002-07-12 00:00",
         "2001-05-22 00:00",
         "2000-01-13 00:00",
         "1999-04-05 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PowerRedundancyType(Integer32, TextualConvention):
    status = "current"
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
        *(("combined", 3),
          ("inPwrSrcRedundant", 6),
          ("nonRedundant", 4),
          ("notsupported", 1),
          ("psRedundant", 5),
          ("psRedundantSingleInput", 7),
          ("redundant", 2))
    )



class PowerAdminType(Integer32, TextualConvention):
    status = "current"
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
        *(("inlineAuto", 3),
          ("inlineOn", 4),
          ("off", 2),
          ("on", 1),
          ("powerCycle", 5))
    )



class PowerOperType(Integer32, TextualConvention):
    status = "current"
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("failed", 8),
          ("offAdmin", 3),
          ("offConnectorRating", 11),
          ("offCooling", 10),
          ("offDenied", 4),
          ("offEnvFan", 7),
          ("offEnvOther", 1),
          ("offEnvPower", 5),
          ("offEnvTemp", 6),
          ("on", 2),
          ("onButFanFail", 9),
          ("onButInlinePowerFail", 12))
    )



class FRUCurrentType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000000000, 1000000000),
    )



class ModuleAdminType(Integer32, TextualConvention):
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
        *(("disabled", 2),
          ("enabled", 1),
          ("outOfServiceAdmin", 4),
          ("reset", 3))
    )



class ModuleOperType(Integer32, TextualConvention):
    status = "current"
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("boot", 5),
          ("diagFailed", 11),
          ("disabled", 3),
          ("dormant", 12),
          ("failed", 7),
          ("fwDownloadFailure", 27),
          ("fwDownloadSuccess", 26),
          ("fwMismatchFound", 25),
          ("mdr", 24),
          ("mismatchConfig", 10),
          ("mismatchWithParent", 9),
          ("missing", 8),
          ("ok", 2),
          ("okButAuthFailed", 23),
          ("okButDiagFailed", 4),
          ("okButPowerOverCritical", 20),
          ("okButPowerOverWarning", 19),
          ("outOfServiceAdmin", 13),
          ("outOfServiceEnvTemp", 14),
          ("powerCycled", 18),
          ("powerDenied", 17),
          ("poweredDown", 15),
          ("poweredUp", 16),
          ("selfTest", 6),
          ("syncInProgress", 21),
          ("unknown", 1),
          ("upgrading", 22))
    )



class ModuleResetReasonType(Integer32, TextualConvention):
    status = "current"
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
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("abortRevReset", 19),
          ("burnBootReset", 20),
          ("cacheErrorReset", 15),
          ("clearConfigReset", 4),
          ("controllerReset", 10),
          ("deviceDriverReset", 16),
          ("downgradeReset", 14),
          ("lowVoltageReset", 9),
          ("manualReset", 5),
          ("memoryProtectionErrorReset", 23),
          ("missingTaskReset", 8),
          ("nonNativeConfigClearReset", 22),
          ("parityError", 3),
          ("powerUp", 2),
          ("resourceOverflowReset", 7),
          ("restoreConfigReset", 18),
          ("softwareExceptionReset", 17),
          ("standbyCdHealthierReset", 21),
          ("switchoverReset", 12),
          ("systemReset", 11),
          ("unknown", 1),
          ("upgradeReset", 13),
          ("watchDogTimeoutReset", 6))
    )



class FRUTimeSeconds(Unsigned32, TextualConvention):
    status = "current"


class FRUCoolingUnit(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cfm", 1),
          ("watts", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CefcMIBObjects_ObjectIdentity = ObjectIdentity
cefcMIBObjects = _CefcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1)
)
_CefcFRUPower_ObjectIdentity = ObjectIdentity
cefcFRUPower = _CefcFRUPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1)
)
_CefcFRUPowerSupplyGroupTable_Object = MibTable
cefcFRUPowerSupplyGroupTable = _CefcFRUPowerSupplyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cefcFRUPowerSupplyGroupTable.setStatus("current")
_CefcFRUPowerSupplyGroupEntry_Object = MibTableRow
cefcFRUPowerSupplyGroupEntry = _CefcFRUPowerSupplyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1)
)
cefcFRUPowerSupplyGroupEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcFRUPowerSupplyGroupEntry.setStatus("current")
_CefcPowerRedundancyMode_Type = PowerRedundancyType
_CefcPowerRedundancyMode_Object = MibTableColumn
cefcPowerRedundancyMode = _CefcPowerRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 1),
    _CefcPowerRedundancyMode_Type()
)
cefcPowerRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcPowerRedundancyMode.setStatus("current")
_CefcPowerUnits_Type = DisplayString
_CefcPowerUnits_Object = MibTableColumn
cefcPowerUnits = _CefcPowerUnits_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 2),
    _CefcPowerUnits_Type()
)
cefcPowerUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPowerUnits.setStatus("current")
_CefcTotalAvailableCurrent_Type = FRUCurrentType
_CefcTotalAvailableCurrent_Object = MibTableColumn
cefcTotalAvailableCurrent = _CefcTotalAvailableCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 3),
    _CefcTotalAvailableCurrent_Type()
)
cefcTotalAvailableCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcTotalAvailableCurrent.setStatus("current")
_CefcTotalDrawnCurrent_Type = FRUCurrentType
_CefcTotalDrawnCurrent_Object = MibTableColumn
cefcTotalDrawnCurrent = _CefcTotalDrawnCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 4),
    _CefcTotalDrawnCurrent_Type()
)
cefcTotalDrawnCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcTotalDrawnCurrent.setStatus("current")
_CefcPowerRedundancyOperMode_Type = PowerRedundancyType
_CefcPowerRedundancyOperMode_Object = MibTableColumn
cefcPowerRedundancyOperMode = _CefcPowerRedundancyOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 5),
    _CefcPowerRedundancyOperMode_Type()
)
cefcPowerRedundancyOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPowerRedundancyOperMode.setStatus("current")


class _CefcPowerNonRedundantReason_Type(Integer32):
    """Custom type cefcPowerNonRedundantReason based on Integer32"""
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
        *(("mismatchedSupplies", 4),
          ("notApplicable", 1),
          ("singleSupply", 3),
          ("supplyError", 5),
          ("unknown", 2))
    )


_CefcPowerNonRedundantReason_Type.__name__ = "Integer32"
_CefcPowerNonRedundantReason_Object = MibTableColumn
cefcPowerNonRedundantReason = _CefcPowerNonRedundantReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 6),
    _CefcPowerNonRedundantReason_Type()
)
cefcPowerNonRedundantReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPowerNonRedundantReason.setStatus("current")
_CefcTotalDrawnInlineCurrent_Type = FRUCurrentType
_CefcTotalDrawnInlineCurrent_Object = MibTableColumn
cefcTotalDrawnInlineCurrent = _CefcTotalDrawnInlineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 1, 1, 7),
    _CefcTotalDrawnInlineCurrent_Type()
)
cefcTotalDrawnInlineCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcTotalDrawnInlineCurrent.setStatus("current")
_CefcFRUPowerStatusTable_Object = MibTable
cefcFRUPowerStatusTable = _CefcFRUPowerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cefcFRUPowerStatusTable.setStatus("current")
_CefcFRUPowerStatusEntry_Object = MibTableRow
cefcFRUPowerStatusEntry = _CefcFRUPowerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1)
)
cefcFRUPowerStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcFRUPowerStatusEntry.setStatus("current")
_CefcFRUPowerAdminStatus_Type = PowerAdminType
_CefcFRUPowerAdminStatus_Object = MibTableColumn
cefcFRUPowerAdminStatus = _CefcFRUPowerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 1),
    _CefcFRUPowerAdminStatus_Type()
)
cefcFRUPowerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcFRUPowerAdminStatus.setStatus("current")
_CefcFRUPowerOperStatus_Type = PowerOperType
_CefcFRUPowerOperStatus_Object = MibTableColumn
cefcFRUPowerOperStatus = _CefcFRUPowerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 2),
    _CefcFRUPowerOperStatus_Type()
)
cefcFRUPowerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFRUPowerOperStatus.setStatus("current")
_CefcFRUCurrent_Type = FRUCurrentType
_CefcFRUCurrent_Object = MibTableColumn
cefcFRUCurrent = _CefcFRUCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 3),
    _CefcFRUCurrent_Type()
)
cefcFRUCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFRUCurrent.setStatus("current")


class _CefcFRUPowerCapability_Type(Bits):
    """Custom type cefcFRUPowerCapability based on Bits"""
    namedValues = NamedValues(
        ("realTimeCurrent", 0)
    )

_CefcFRUPowerCapability_Type.__name__ = "Bits"
_CefcFRUPowerCapability_Object = MibTableColumn
cefcFRUPowerCapability = _CefcFRUPowerCapability_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 4),
    _CefcFRUPowerCapability_Type()
)
cefcFRUPowerCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFRUPowerCapability.setStatus("current")
_CefcFRURealTimeCurrent_Type = FRUCurrentType
_CefcFRURealTimeCurrent_Object = MibTableColumn
cefcFRURealTimeCurrent = _CefcFRURealTimeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 2, 1, 5),
    _CefcFRURealTimeCurrent_Type()
)
cefcFRURealTimeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFRURealTimeCurrent.setStatus("current")


class _CefcMaxDefaultInLinePower_Type(Integer32):
    """Custom type cefcMaxDefaultInLinePower based on Integer32"""
    defaultValue = 12500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12500),
    )


_CefcMaxDefaultInLinePower_Type.__name__ = "Integer32"
_CefcMaxDefaultInLinePower_Object = MibScalar
cefcMaxDefaultInLinePower = _CefcMaxDefaultInLinePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 3),
    _CefcMaxDefaultInLinePower_Type()
)
cefcMaxDefaultInLinePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcMaxDefaultInLinePower.setStatus("deprecated")
if mibBuilder.loadTexts:
    cefcMaxDefaultInLinePower.setUnits("miliwatts")
_CefcFRUPowerSupplyValueTable_Object = MibTable
cefcFRUPowerSupplyValueTable = _CefcFRUPowerSupplyValueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cefcFRUPowerSupplyValueTable.setStatus("current")
_CefcFRUPowerSupplyValueEntry_Object = MibTableRow
cefcFRUPowerSupplyValueEntry = _CefcFRUPowerSupplyValueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1)
)
cefcFRUPowerSupplyValueEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcFRUPowerSupplyValueEntry.setStatus("current")
_CefcFRUTotalSystemCurrent_Type = FRUCurrentType
_CefcFRUTotalSystemCurrent_Object = MibTableColumn
cefcFRUTotalSystemCurrent = _CefcFRUTotalSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 1),
    _CefcFRUTotalSystemCurrent_Type()
)
cefcFRUTotalSystemCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcFRUTotalSystemCurrent.setStatus("current")
_CefcFRUDrawnSystemCurrent_Type = FRUCurrentType
_CefcFRUDrawnSystemCurrent_Object = MibTableColumn
cefcFRUDrawnSystemCurrent = _CefcFRUDrawnSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 2),
    _CefcFRUDrawnSystemCurrent_Type()
)
cefcFRUDrawnSystemCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcFRUDrawnSystemCurrent.setStatus("current")
_CefcFRUTotalInlineCurrent_Type = FRUCurrentType
_CefcFRUTotalInlineCurrent_Object = MibTableColumn
cefcFRUTotalInlineCurrent = _CefcFRUTotalInlineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 3),
    _CefcFRUTotalInlineCurrent_Type()
)
cefcFRUTotalInlineCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcFRUTotalInlineCurrent.setStatus("current")
_CefcFRUDrawnInlineCurrent_Type = FRUCurrentType
_CefcFRUDrawnInlineCurrent_Object = MibTableColumn
cefcFRUDrawnInlineCurrent = _CefcFRUDrawnInlineCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 4, 1, 4),
    _CefcFRUDrawnInlineCurrent_Type()
)
cefcFRUDrawnInlineCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcFRUDrawnInlineCurrent.setStatus("current")
_CefcMaxDefaultHighInLinePower_Type = Unsigned32
_CefcMaxDefaultHighInLinePower_Object = MibScalar
cefcMaxDefaultHighInLinePower = _CefcMaxDefaultHighInLinePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 1, 5),
    _CefcMaxDefaultHighInLinePower_Type()
)
cefcMaxDefaultHighInLinePower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcMaxDefaultHighInLinePower.setStatus("current")
if mibBuilder.loadTexts:
    cefcMaxDefaultHighInLinePower.setUnits("miliwatts")
_CefcModule_ObjectIdentity = ObjectIdentity
cefcModule = _CefcModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2)
)
_CefcModuleTable_Object = MibTable
cefcModuleTable = _CefcModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cefcModuleTable.setStatus("current")
_CefcModuleEntry_Object = MibTableRow
cefcModuleEntry = _CefcModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1)
)
cefcModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcModuleEntry.setStatus("current")
_CefcModuleAdminStatus_Type = ModuleAdminType
_CefcModuleAdminStatus_Object = MibTableColumn
cefcModuleAdminStatus = _CefcModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 1),
    _CefcModuleAdminStatus_Type()
)
cefcModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcModuleAdminStatus.setStatus("current")
_CefcModuleOperStatus_Type = ModuleOperType
_CefcModuleOperStatus_Object = MibTableColumn
cefcModuleOperStatus = _CefcModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 2),
    _CefcModuleOperStatus_Type()
)
cefcModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleOperStatus.setStatus("current")
_CefcModuleResetReason_Type = ModuleResetReasonType
_CefcModuleResetReason_Object = MibTableColumn
cefcModuleResetReason = _CefcModuleResetReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 3),
    _CefcModuleResetReason_Type()
)
cefcModuleResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleResetReason.setStatus("current")
_CefcModuleStatusLastChangeTime_Type = TimeStamp
_CefcModuleStatusLastChangeTime_Object = MibTableColumn
cefcModuleStatusLastChangeTime = _CefcModuleStatusLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 4),
    _CefcModuleStatusLastChangeTime_Type()
)
cefcModuleStatusLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleStatusLastChangeTime.setStatus("current")
_CefcModuleLastClearConfigTime_Type = TimeStamp
_CefcModuleLastClearConfigTime_Object = MibTableColumn
cefcModuleLastClearConfigTime = _CefcModuleLastClearConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 5),
    _CefcModuleLastClearConfigTime_Type()
)
cefcModuleLastClearConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleLastClearConfigTime.setStatus("current")
_CefcModuleResetReasonDescription_Type = DisplayString
_CefcModuleResetReasonDescription_Object = MibTableColumn
cefcModuleResetReasonDescription = _CefcModuleResetReasonDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 6),
    _CefcModuleResetReasonDescription_Type()
)
cefcModuleResetReasonDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleResetReasonDescription.setStatus("current")
_CefcModuleStateChangeReasonDescr_Type = DisplayString
_CefcModuleStateChangeReasonDescr_Object = MibTableColumn
cefcModuleStateChangeReasonDescr = _CefcModuleStateChangeReasonDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 7),
    _CefcModuleStateChangeReasonDescr_Type()
)
cefcModuleStateChangeReasonDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleStateChangeReasonDescr.setStatus("current")
_CefcModuleUpTime_Type = FRUTimeSeconds
_CefcModuleUpTime_Object = MibTableColumn
cefcModuleUpTime = _CefcModuleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 1, 1, 8),
    _CefcModuleUpTime_Type()
)
cefcModuleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleUpTime.setStatus("current")
_CefcIntelliModuleTable_Object = MibTable
cefcIntelliModuleTable = _CefcIntelliModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cefcIntelliModuleTable.setStatus("current")
_CefcIntelliModuleEntry_Object = MibTableRow
cefcIntelliModuleEntry = _CefcIntelliModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1)
)
cefcIntelliModuleEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcIntelliModuleEntry.setStatus("current")
_CefcIntelliModuleIPAddrType_Type = InetAddressType
_CefcIntelliModuleIPAddrType_Object = MibTableColumn
cefcIntelliModuleIPAddrType = _CefcIntelliModuleIPAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1, 1),
    _CefcIntelliModuleIPAddrType_Type()
)
cefcIntelliModuleIPAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcIntelliModuleIPAddrType.setStatus("current")
_CefcIntelliModuleIPAddr_Type = InetAddress
_CefcIntelliModuleIPAddr_Object = MibTableColumn
cefcIntelliModuleIPAddr = _CefcIntelliModuleIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 2, 1, 2),
    _CefcIntelliModuleIPAddr_Type()
)
cefcIntelliModuleIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcIntelliModuleIPAddr.setStatus("current")
_CefcModuleLocalSwitchingTable_Object = MibTable
cefcModuleLocalSwitchingTable = _CefcModuleLocalSwitchingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cefcModuleLocalSwitchingTable.setStatus("current")
_CefcModuleLocalSwitchingEntry_Object = MibTableRow
cefcModuleLocalSwitchingEntry = _CefcModuleLocalSwitchingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3, 1)
)
cefcModuleLocalSwitchingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcModuleLocalSwitchingEntry.setStatus("current")


class _CefcModuleLocalSwitchingMode_Type(Integer32):
    """Custom type cefcModuleLocalSwitchingMode based on Integer32"""
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


_CefcModuleLocalSwitchingMode_Type.__name__ = "Integer32"
_CefcModuleLocalSwitchingMode_Object = MibTableColumn
cefcModuleLocalSwitchingMode = _CefcModuleLocalSwitchingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 2, 3, 1, 1),
    _CefcModuleLocalSwitchingMode_Type()
)
cefcModuleLocalSwitchingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcModuleLocalSwitchingMode.setStatus("current")
_CefcMIBNotificationEnables_ObjectIdentity = ObjectIdentity
cefcMIBNotificationEnables = _CefcMIBNotificationEnables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3)
)


class _CefcMIBEnableStatusNotification_Type(TruthValue):
    """Custom type cefcMIBEnableStatusNotification based on TruthValue"""


_CefcMIBEnableStatusNotification_Object = MibScalar
cefcMIBEnableStatusNotification = _CefcMIBEnableStatusNotification_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3, 1),
    _CefcMIBEnableStatusNotification_Type()
)
cefcMIBEnableStatusNotification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcMIBEnableStatusNotification.setStatus("current")


class _CefcEnablePSOutputChangeNotif_Type(TruthValue):
    """Custom type cefcEnablePSOutputChangeNotif based on TruthValue"""


_CefcEnablePSOutputChangeNotif_Object = MibScalar
cefcEnablePSOutputChangeNotif = _CefcEnablePSOutputChangeNotif_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 3, 2),
    _CefcEnablePSOutputChangeNotif_Type()
)
cefcEnablePSOutputChangeNotif.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cefcEnablePSOutputChangeNotif.setStatus("current")
_CefcFRUFan_ObjectIdentity = ObjectIdentity
cefcFRUFan = _CefcFRUFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4)
)
_CefcFanTrayStatusTable_Object = MibTable
cefcFanTrayStatusTable = _CefcFanTrayStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cefcFanTrayStatusTable.setStatus("current")
_CefcFanTrayStatusEntry_Object = MibTableRow
cefcFanTrayStatusEntry = _CefcFanTrayStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1)
)
cefcFanTrayStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcFanTrayStatusEntry.setStatus("current")


class _CefcFanTrayOperStatus_Type(Integer32):
    """Custom type cefcFanTrayOperStatus based on Integer32"""
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
        *(("down", 3),
          ("unknown", 1),
          ("up", 2),
          ("warning", 4))
    )


_CefcFanTrayOperStatus_Type.__name__ = "Integer32"
_CefcFanTrayOperStatus_Object = MibTableColumn
cefcFanTrayOperStatus = _CefcFanTrayOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 4, 1, 1, 1),
    _CefcFanTrayOperStatus_Type()
)
cefcFanTrayOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanTrayOperStatus.setStatus("current")
_CefcPhysical_ObjectIdentity = ObjectIdentity
cefcPhysical = _CefcPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5)
)
_CefcPhysicalTable_Object = MibTable
cefcPhysicalTable = _CefcPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cefcPhysicalTable.setStatus("current")
_CefcPhysicalEntry_Object = MibTableRow
cefcPhysicalEntry = _CefcPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1, 1)
)
cefcPhysicalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcPhysicalEntry.setStatus("current")


class _CefcPhysicalStatus_Type(Integer32):
    """Custom type cefcPhysicalStatus based on Integer32"""
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
        *(("incompatible", 4),
          ("other", 1),
          ("supported", 2),
          ("unsupported", 3))
    )


_CefcPhysicalStatus_Type.__name__ = "Integer32"
_CefcPhysicalStatus_Object = MibTableColumn
cefcPhysicalStatus = _CefcPhysicalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 5, 1, 1, 1),
    _CefcPhysicalStatus_Type()
)
cefcPhysicalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPhysicalStatus.setStatus("current")
_CefcPowerCapacity_ObjectIdentity = ObjectIdentity
cefcPowerCapacity = _CefcPowerCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6)
)
_CefcPowerSupplyInputTable_Object = MibTable
cefcPowerSupplyInputTable = _CefcPowerSupplyInputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cefcPowerSupplyInputTable.setStatus("current")
_CefcPowerSupplyInputEntry_Object = MibTableRow
cefcPowerSupplyInputEntry = _CefcPowerSupplyInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1)
)
cefcPowerSupplyInputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyInputIndex"),
)
if mibBuilder.loadTexts:
    cefcPowerSupplyInputEntry.setStatus("current")
_CefcPowerSupplyInputIndex_Type = Unsigned32
_CefcPowerSupplyInputIndex_Object = MibTableColumn
cefcPowerSupplyInputIndex = _CefcPowerSupplyInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1, 1),
    _CefcPowerSupplyInputIndex_Type()
)
cefcPowerSupplyInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefcPowerSupplyInputIndex.setStatus("current")


class _CefcPowerSupplyInputType_Type(Integer32):
    """Custom type cefcPowerSupplyInputType based on Integer32"""
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
        *(("acHigh", 3),
          ("acLow", 2),
          ("dcHigh", 5),
          ("dcLow", 4),
          ("unknown", 1))
    )


_CefcPowerSupplyInputType_Type.__name__ = "Integer32"
_CefcPowerSupplyInputType_Object = MibTableColumn
cefcPowerSupplyInputType = _CefcPowerSupplyInputType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 1, 1, 2),
    _CefcPowerSupplyInputType_Type()
)
cefcPowerSupplyInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPowerSupplyInputType.setStatus("current")
_CefcPowerSupplyOutputTable_Object = MibTable
cefcPowerSupplyOutputTable = _CefcPowerSupplyOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2)
)
if mibBuilder.loadTexts:
    cefcPowerSupplyOutputTable.setStatus("current")
_CefcPowerSupplyOutputEntry_Object = MibTableRow
cefcPowerSupplyOutputEntry = _CefcPowerSupplyOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1)
)
cefcPowerSupplyOutputEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeIndex"),
)
if mibBuilder.loadTexts:
    cefcPowerSupplyOutputEntry.setStatus("current")
_CefcPSOutputModeIndex_Type = Unsigned32
_CefcPSOutputModeIndex_Object = MibTableColumn
cefcPSOutputModeIndex = _CefcPSOutputModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 1),
    _CefcPSOutputModeIndex_Type()
)
cefcPSOutputModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefcPSOutputModeIndex.setStatus("current")
_CefcPSOutputModeCurrent_Type = FRUCurrentType
_CefcPSOutputModeCurrent_Object = MibTableColumn
cefcPSOutputModeCurrent = _CefcPSOutputModeCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 2),
    _CefcPSOutputModeCurrent_Type()
)
cefcPSOutputModeCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPSOutputModeCurrent.setStatus("current")
_CefcPSOutputModeInOperation_Type = TruthValue
_CefcPSOutputModeInOperation_Object = MibTableColumn
cefcPSOutputModeInOperation = _CefcPSOutputModeInOperation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 6, 2, 1, 3),
    _CefcPSOutputModeInOperation_Type()
)
cefcPSOutputModeInOperation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcPSOutputModeInOperation.setStatus("current")
_CefcCooling_ObjectIdentity = ObjectIdentity
cefcCooling = _CefcCooling_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7)
)
_CefcChassisCoolingTable_Object = MibTable
cefcChassisCoolingTable = _CefcChassisCoolingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cefcChassisCoolingTable.setStatus("current")
_CefcChassisCoolingEntry_Object = MibTableRow
cefcChassisCoolingEntry = _CefcChassisCoolingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1)
)
cefcChassisCoolingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcChassisCoolingEntry.setStatus("current")
_CefcChassisPerSlotCoolingCap_Type = Unsigned32
_CefcChassisPerSlotCoolingCap_Object = MibTableColumn
cefcChassisPerSlotCoolingCap = _CefcChassisPerSlotCoolingCap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1, 1),
    _CefcChassisPerSlotCoolingCap_Type()
)
cefcChassisPerSlotCoolingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcChassisPerSlotCoolingCap.setStatus("current")
_CefcChassisPerSlotCoolingUnit_Type = FRUCoolingUnit
_CefcChassisPerSlotCoolingUnit_Object = MibTableColumn
cefcChassisPerSlotCoolingUnit = _CefcChassisPerSlotCoolingUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 1, 1, 2),
    _CefcChassisPerSlotCoolingUnit_Type()
)
cefcChassisPerSlotCoolingUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcChassisPerSlotCoolingUnit.setStatus("current")
_CefcFanCoolingTable_Object = MibTable
cefcFanCoolingTable = _CefcFanCoolingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2)
)
if mibBuilder.loadTexts:
    cefcFanCoolingTable.setStatus("current")
_CefcFanCoolingEntry_Object = MibTableRow
cefcFanCoolingEntry = _CefcFanCoolingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1)
)
cefcFanCoolingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcFanCoolingEntry.setStatus("current")
_CefcFanCoolingCapacity_Type = Unsigned32
_CefcFanCoolingCapacity_Object = MibTableColumn
cefcFanCoolingCapacity = _CefcFanCoolingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1, 1),
    _CefcFanCoolingCapacity_Type()
)
cefcFanCoolingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanCoolingCapacity.setStatus("current")
_CefcFanCoolingCapacityUnit_Type = FRUCoolingUnit
_CefcFanCoolingCapacityUnit_Object = MibTableColumn
cefcFanCoolingCapacityUnit = _CefcFanCoolingCapacityUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 2, 1, 2),
    _CefcFanCoolingCapacityUnit_Type()
)
cefcFanCoolingCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanCoolingCapacityUnit.setStatus("current")
_CefcModuleCoolingTable_Object = MibTable
cefcModuleCoolingTable = _CefcModuleCoolingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3)
)
if mibBuilder.loadTexts:
    cefcModuleCoolingTable.setStatus("current")
_CefcModuleCoolingEntry_Object = MibTableRow
cefcModuleCoolingEntry = _CefcModuleCoolingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1)
)
cefcModuleCoolingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcModuleCoolingEntry.setStatus("current")
_CefcModuleCooling_Type = Unsigned32
_CefcModuleCooling_Object = MibTableColumn
cefcModuleCooling = _CefcModuleCooling_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1, 1),
    _CefcModuleCooling_Type()
)
cefcModuleCooling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleCooling.setStatus("current")
_CefcModuleCoolingUnit_Type = FRUCoolingUnit
_CefcModuleCoolingUnit_Object = MibTableColumn
cefcModuleCoolingUnit = _CefcModuleCoolingUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 3, 1, 2),
    _CefcModuleCoolingUnit_Type()
)
cefcModuleCoolingUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModuleCoolingUnit.setStatus("current")
_CefcFanCoolingCapTable_Object = MibTable
cefcFanCoolingCapTable = _CefcFanCoolingCapTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4)
)
if mibBuilder.loadTexts:
    cefcFanCoolingCapTable.setStatus("current")
_CefcFanCoolingCapEntry_Object = MibTableRow
cefcFanCoolingCapEntry = _CefcFanCoolingCapEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1)
)
cefcFanCoolingCapEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapIndex"),
)
if mibBuilder.loadTexts:
    cefcFanCoolingCapEntry.setStatus("current")


class _CefcFanCoolingCapIndex_Type(Unsigned32):
    """Custom type cefcFanCoolingCapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_CefcFanCoolingCapIndex_Type.__name__ = "Unsigned32"
_CefcFanCoolingCapIndex_Object = MibTableColumn
cefcFanCoolingCapIndex = _CefcFanCoolingCapIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 1),
    _CefcFanCoolingCapIndex_Type()
)
cefcFanCoolingCapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cefcFanCoolingCapIndex.setStatus("current")
_CefcFanCoolingCapModeDescr_Type = SnmpAdminString
_CefcFanCoolingCapModeDescr_Object = MibTableColumn
cefcFanCoolingCapModeDescr = _CefcFanCoolingCapModeDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 2),
    _CefcFanCoolingCapModeDescr_Type()
)
cefcFanCoolingCapModeDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanCoolingCapModeDescr.setStatus("current")
_CefcFanCoolingCapCapacity_Type = Unsigned32
_CefcFanCoolingCapCapacity_Object = MibTableColumn
cefcFanCoolingCapCapacity = _CefcFanCoolingCapCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 3),
    _CefcFanCoolingCapCapacity_Type()
)
cefcFanCoolingCapCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanCoolingCapCapacity.setStatus("current")
_CefcFanCoolingCapCurrent_Type = FRUCurrentType
_CefcFanCoolingCapCurrent_Object = MibTableColumn
cefcFanCoolingCapCurrent = _CefcFanCoolingCapCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 4),
    _CefcFanCoolingCapCurrent_Type()
)
cefcFanCoolingCapCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanCoolingCapCurrent.setStatus("current")
_CefcFanCoolingCapCapacityUnit_Type = FRUCoolingUnit
_CefcFanCoolingCapCapacityUnit_Object = MibTableColumn
cefcFanCoolingCapCapacityUnit = _CefcFanCoolingCapCapacityUnit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 7, 4, 1, 5),
    _CefcFanCoolingCapCapacityUnit_Type()
)
cefcFanCoolingCapCapacityUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcFanCoolingCapCapacityUnit.setStatus("current")
_CefcConnector_ObjectIdentity = ObjectIdentity
cefcConnector = _CefcConnector_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8)
)
_CefcConnectorRatingTable_Object = MibTable
cefcConnectorRatingTable = _CefcConnectorRatingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cefcConnectorRatingTable.setStatus("current")
_CefcConnectorRatingEntry_Object = MibTableRow
cefcConnectorRatingEntry = _CefcConnectorRatingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1, 1)
)
cefcConnectorRatingEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcConnectorRatingEntry.setStatus("current")
_CefcConnectorRating_Type = FRUCurrentType
_CefcConnectorRating_Object = MibTableColumn
cefcConnectorRating = _CefcConnectorRating_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 1, 1, 1),
    _CefcConnectorRating_Type()
)
cefcConnectorRating.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcConnectorRating.setStatus("current")
_CefcModulePowerConsumptionTable_Object = MibTable
cefcModulePowerConsumptionTable = _CefcModulePowerConsumptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2)
)
if mibBuilder.loadTexts:
    cefcModulePowerConsumptionTable.setStatus("current")
_CefcModulePowerConsumptionEntry_Object = MibTableRow
cefcModulePowerConsumptionEntry = _CefcModulePowerConsumptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2, 1)
)
cefcModulePowerConsumptionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    cefcModulePowerConsumptionEntry.setStatus("current")
_CefcModulePowerConsumption_Type = FRUCurrentType
_CefcModulePowerConsumption_Object = MibTableColumn
cefcModulePowerConsumption = _CefcModulePowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 1, 8, 2, 1, 1),
    _CefcModulePowerConsumption_Type()
)
cefcModulePowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cefcModulePowerConsumption.setStatus("current")
_CefcFRUMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
cefcFRUMIBNotificationPrefix = _CefcFRUMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2)
)
_CefcMIBNotifications_ObjectIdentity = ObjectIdentity
cefcMIBNotifications = _CefcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0)
)
_CefcMIBConformance_ObjectIdentity = ObjectIdentity
cefcMIBConformance = _CefcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3)
)
_CefcMIBCompliances_ObjectIdentity = ObjectIdentity
cefcMIBCompliances = _CefcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1)
)
_CefcMIBGroups_ObjectIdentity = ObjectIdentity
cefcMIBGroups = _CefcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2)
)

# Managed Objects groups

cefcMIBPowerModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 1)
)
cefcMIBPowerModeGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerRedundancyMode"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerUnits"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalAvailableCurrent"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalDrawnCurrent"))
)
if mibBuilder.loadTexts:
    cefcMIBPowerModeGroup.setStatus("current")

cefcMIBPowerFRUControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 2)
)
cefcMIBPowerFRUControlGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerAdminStatus"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerOperStatus"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUCurrent"))
)
if mibBuilder.loadTexts:
    cefcMIBPowerFRUControlGroup.setStatus("current")

cefcMIBModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 3)
)
cefcMIBModuleGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleAdminStatus"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleOperStatus"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleResetReason"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusLastChangeTime"))
)
if mibBuilder.loadTexts:
    cefcMIBModuleGroup.setStatus("current")

cefcMIBInLinePowerControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 4)
)
cefcMIBInLinePowerControlGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMaxDefaultInLinePower")
)
if mibBuilder.loadTexts:
    cefcMIBInLinePowerControlGroup.setStatus("deprecated")

cefcMIBNotificationEnablesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 5)
)
cefcMIBNotificationEnablesGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMIBEnableStatusNotification")
)
if mibBuilder.loadTexts:
    cefcMIBNotificationEnablesGroup.setStatus("current")

cefcModuleGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 7)
)
cefcModuleGroupRev1.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleLastClearConfigTime"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleResetReasonDescription"))
)
if mibBuilder.loadTexts:
    cefcModuleGroupRev1.setStatus("current")

cefcMIBPowerFRUValueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 8)
)
cefcMIBPowerFRUValueGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUTotalSystemCurrent"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUDrawnSystemCurrent"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUTotalInlineCurrent"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUDrawnInlineCurrent"))
)
if mibBuilder.loadTexts:
    cefcMIBPowerFRUValueGroup.setStatus("current")

cefcMIBFanTrayStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 9)
)
cefcMIBFanTrayStatusGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayOperStatus")
)
if mibBuilder.loadTexts:
    cefcMIBFanTrayStatusGroup.setStatus("current")

cefcMIBPhysicalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 10)
)
cefcMIBPhysicalGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPhysicalStatus")
)
if mibBuilder.loadTexts:
    cefcMIBPhysicalGroup.setStatus("current")

cefcMIBPowerOperModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 12)
)
cefcMIBPowerOperModeGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerRedundancyOperMode")
)
if mibBuilder.loadTexts:
    cefcMIBPowerOperModeGroup.setStatus("current")

cefcMIBInLinePowerControlGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 13)
)
cefcMIBInLinePowerControlGroupRev1.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcMaxDefaultHighInLinePower")
)
if mibBuilder.loadTexts:
    cefcMIBInLinePowerControlGroupRev1.setStatus("current")

cefcModuleExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 14)
)
cefcModuleExtGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStateChangeReasonDescr"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleUpTime"))
)
if mibBuilder.loadTexts:
    cefcModuleExtGroup.setStatus("current")

cefcIntelliModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 15)
)
cefcIntelliModuleGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleIPAddrType"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcIntelliModuleIPAddr"))
)
if mibBuilder.loadTexts:
    cefcIntelliModuleGroup.setStatus("current")

cefcPowerCapacityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 16)
)
cefcPowerCapacityGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyInputType"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeCurrent"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeInOperation"))
)
if mibBuilder.loadTexts:
    cefcPowerCapacityGroup.setStatus("current")

cefcCoolingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 17)
)
cefcCoolingGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingCap"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacity"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCooling"))
)
if mibBuilder.loadTexts:
    cefcCoolingGroup.setStatus("deprecated")

cefcConnectorRatingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 18)
)
cefcConnectorRatingGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcConnectorRating"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModulePowerConsumption"))
)
if mibBuilder.loadTexts:
    cefcConnectorRatingGroup.setStatus("current")

cefcMIBNotificationEnablesGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 19)
)
cefcMIBNotificationEnablesGroup2.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcEnablePSOutputChangeNotif")
)
if mibBuilder.loadTexts:
    cefcMIBNotificationEnablesGroup2.setStatus("current")

cefcMIBInLinePowerCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 21)
)
cefcMIBInLinePowerCurrentGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcTotalDrawnInlineCurrent")
)
if mibBuilder.loadTexts:
    cefcMIBInLinePowerCurrentGroup.setStatus("current")

cefcMIBPowerRedundancyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 22)
)
cefcMIBPowerRedundancyInfoGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerNonRedundantReason")
)
if mibBuilder.loadTexts:
    cefcMIBPowerRedundancyInfoGroup.setStatus("current")

cefcFanCoolingCapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 23)
)
cefcFanCoolingCapGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapModeDescr"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCapacity"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCurrent"))
)
if mibBuilder.loadTexts:
    cefcFanCoolingCapGroup.setStatus("current")

cefcMIBModuleLocalSwitchingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 24)
)
cefcMIBModuleLocalSwitchingGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleLocalSwitchingMode")
)
if mibBuilder.loadTexts:
    cefcMIBModuleLocalSwitchingGroup.setStatus("current")

cefcFRUPowerRealTimeStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 25)
)
cefcFRUPowerRealTimeStatusGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRURealTimeCurrent")
)
if mibBuilder.loadTexts:
    cefcFRUPowerRealTimeStatusGroup.setStatus("current")

cefcFRUPowerCapabilityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 26)
)
cefcFRUPowerCapabilityGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerCapability")
)
if mibBuilder.loadTexts:
    cefcFRUPowerCapabilityGroup.setStatus("current")

cefcFRUCoolingUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 27)
)
cefcFRUCoolingUnitGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingUnit"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCoolingUnit"))
)
if mibBuilder.loadTexts:
    cefcFRUCoolingUnitGroup.setStatus("current")

cefcFRUFanCoolingUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 28)
)
cefcFRUFanCoolingUnitGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacityUnit"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapCapacityUnit"))
)
if mibBuilder.loadTexts:
    cefcFRUFanCoolingUnitGroup.setStatus("current")

cefcCoolingGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 29)
)
cefcCoolingGroup2.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcChassisPerSlotCoolingCap"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleCooling"))
)
if mibBuilder.loadTexts:
    cefcCoolingGroup2.setStatus("current")

cefcFanCoolingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 30)
)
cefcFanCoolingGroup.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanCoolingCapacity")
)
if mibBuilder.loadTexts:
    cefcFanCoolingGroup.setStatus("current")


# Notification objects

cefcModuleStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 1)
)
cefcModuleStatusChange.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleOperStatus"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusLastChangeTime"))
)
if mibBuilder.loadTexts:
    cefcModuleStatusChange.setStatus(
        "current"
    )

cefcPowerStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 2)
)
cefcPowerStatusChange.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerOperStatus"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUPowerAdminStatus"))
)
if mibBuilder.loadTexts:
    cefcPowerStatusChange.setStatus(
        "current"
    )

cefcFRUInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 3)
)
cefcFRUInserted.setObjects(
    ("ENTITY-MIB", "entPhysicalContainedIn")
)
if mibBuilder.loadTexts:
    cefcFRUInserted.setStatus(
        "current"
    )

cefcFRURemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 4)
)
cefcFRURemoved.setObjects(
    ("ENTITY-MIB", "entPhysicalContainedIn")
)
if mibBuilder.loadTexts:
    cefcFRURemoved.setStatus(
        "current"
    )

cefcUnrecognizedFRU = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 5)
)
cefcUnrecognizedFRU.setObjects(
      *(("ENTITY-MIB", "entPhysicalClass"),
        ("ENTITY-MIB", "entPhysicalVendorType"),
        ("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalModelName"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPhysicalStatus"))
)
if mibBuilder.loadTexts:
    cefcUnrecognizedFRU.setStatus(
        "current"
    )

cefcFanTrayStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 6)
)
cefcFanTrayStatusChange.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayOperStatus")
)
if mibBuilder.loadTexts:
    cefcFanTrayStatusChange.setStatus(
        "current"
    )

cefcPowerSupplyOutputChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 2, 0, 7)
)
cefcPowerSupplyOutputChange.setObjects(
      *(("ENTITY-MIB", "entPhysicalName"),
        ("ENTITY-MIB", "entPhysicalModelName"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPSOutputModeCurrent"))
)
if mibBuilder.loadTexts:
    cefcPowerSupplyOutputChange.setStatus(
        "current"
    )


# Notifications groups

cefcMgmtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 6)
)
cefcMgmtNotificationsGroup.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcModuleStatusChange"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerStatusChange"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRUInserted"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFRURemoved"))
)
if mibBuilder.loadTexts:
    cefcMgmtNotificationsGroup.setStatus(
        "current"
    )

cefcMgmtNotificationsGroup2 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 11)
)
cefcMgmtNotificationsGroup2.setObjects(
      *(("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcUnrecognizedFRU"),
        ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcFanTrayStatusChange"))
)
if mibBuilder.loadTexts:
    cefcMgmtNotificationsGroup2.setStatus(
        "current"
    )

cefcMgmtNotificationsGroup3 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 2, 20)
)
cefcMgmtNotificationsGroup3.setObjects(
    ("CISCO-ENTITY-FRU-CONTROL-MIB", "cefcPowerSupplyOutputChange")
)
if mibBuilder.loadTexts:
    cefcMgmtNotificationsGroup3.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cefcMIBPowerCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance.setStatus(
        "obsolete"
    )

cefcMIBPowerCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 2)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance2.setStatus(
        "deprecated"
    )

cefcMIBPowerCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 3)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance3.setStatus(
        "deprecated"
    )

cefcMIBPowerCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 4)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance4.setStatus(
        "deprecated"
    )

cefcMIBPowerCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 5)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance5.setStatus(
        "deprecated"
    )

cefcMIBPowerCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 6)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance6.setStatus(
        "current"
    )

cefcMIBPowerCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 7)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance7.setStatus(
        "deprecated"
    )

cefcMIBPowerCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 8)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance8.setStatus(
        "deprecated"
    )

cefcMIBPowerCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 117, 3, 1, 9)
)
if mibBuilder.loadTexts:
    cefcMIBPowerCompliance9.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-FRU-CONTROL-MIB",
    **{"PowerRedundancyType": PowerRedundancyType,
       "PowerAdminType": PowerAdminType,
       "PowerOperType": PowerOperType,
       "FRUCurrentType": FRUCurrentType,
       "ModuleAdminType": ModuleAdminType,
       "ModuleOperType": ModuleOperType,
       "ModuleResetReasonType": ModuleResetReasonType,
       "FRUTimeSeconds": FRUTimeSeconds,
       "FRUCoolingUnit": FRUCoolingUnit,
       "ciscoEntityFRUControlMIB": ciscoEntityFRUControlMIB,
       "cefcMIBObjects": cefcMIBObjects,
       "cefcFRUPower": cefcFRUPower,
       "cefcFRUPowerSupplyGroupTable": cefcFRUPowerSupplyGroupTable,
       "cefcFRUPowerSupplyGroupEntry": cefcFRUPowerSupplyGroupEntry,
       "cefcPowerRedundancyMode": cefcPowerRedundancyMode,
       "cefcPowerUnits": cefcPowerUnits,
       "cefcTotalAvailableCurrent": cefcTotalAvailableCurrent,
       "cefcTotalDrawnCurrent": cefcTotalDrawnCurrent,
       "cefcPowerRedundancyOperMode": cefcPowerRedundancyOperMode,
       "cefcPowerNonRedundantReason": cefcPowerNonRedundantReason,
       "cefcTotalDrawnInlineCurrent": cefcTotalDrawnInlineCurrent,
       "cefcFRUPowerStatusTable": cefcFRUPowerStatusTable,
       "cefcFRUPowerStatusEntry": cefcFRUPowerStatusEntry,
       "cefcFRUPowerAdminStatus": cefcFRUPowerAdminStatus,
       "cefcFRUPowerOperStatus": cefcFRUPowerOperStatus,
       "cefcFRUCurrent": cefcFRUCurrent,
       "cefcFRUPowerCapability": cefcFRUPowerCapability,
       "cefcFRURealTimeCurrent": cefcFRURealTimeCurrent,
       "cefcMaxDefaultInLinePower": cefcMaxDefaultInLinePower,
       "cefcFRUPowerSupplyValueTable": cefcFRUPowerSupplyValueTable,
       "cefcFRUPowerSupplyValueEntry": cefcFRUPowerSupplyValueEntry,
       "cefcFRUTotalSystemCurrent": cefcFRUTotalSystemCurrent,
       "cefcFRUDrawnSystemCurrent": cefcFRUDrawnSystemCurrent,
       "cefcFRUTotalInlineCurrent": cefcFRUTotalInlineCurrent,
       "cefcFRUDrawnInlineCurrent": cefcFRUDrawnInlineCurrent,
       "cefcMaxDefaultHighInLinePower": cefcMaxDefaultHighInLinePower,
       "cefcModule": cefcModule,
       "cefcModuleTable": cefcModuleTable,
       "cefcModuleEntry": cefcModuleEntry,
       "cefcModuleAdminStatus": cefcModuleAdminStatus,
       "cefcModuleOperStatus": cefcModuleOperStatus,
       "cefcModuleResetReason": cefcModuleResetReason,
       "cefcModuleStatusLastChangeTime": cefcModuleStatusLastChangeTime,
       "cefcModuleLastClearConfigTime": cefcModuleLastClearConfigTime,
       "cefcModuleResetReasonDescription": cefcModuleResetReasonDescription,
       "cefcModuleStateChangeReasonDescr": cefcModuleStateChangeReasonDescr,
       "cefcModuleUpTime": cefcModuleUpTime,
       "cefcIntelliModuleTable": cefcIntelliModuleTable,
       "cefcIntelliModuleEntry": cefcIntelliModuleEntry,
       "cefcIntelliModuleIPAddrType": cefcIntelliModuleIPAddrType,
       "cefcIntelliModuleIPAddr": cefcIntelliModuleIPAddr,
       "cefcModuleLocalSwitchingTable": cefcModuleLocalSwitchingTable,
       "cefcModuleLocalSwitchingEntry": cefcModuleLocalSwitchingEntry,
       "cefcModuleLocalSwitchingMode": cefcModuleLocalSwitchingMode,
       "cefcMIBNotificationEnables": cefcMIBNotificationEnables,
       "cefcMIBEnableStatusNotification": cefcMIBEnableStatusNotification,
       "cefcEnablePSOutputChangeNotif": cefcEnablePSOutputChangeNotif,
       "cefcFRUFan": cefcFRUFan,
       "cefcFanTrayStatusTable": cefcFanTrayStatusTable,
       "cefcFanTrayStatusEntry": cefcFanTrayStatusEntry,
       "cefcFanTrayOperStatus": cefcFanTrayOperStatus,
       "cefcPhysical": cefcPhysical,
       "cefcPhysicalTable": cefcPhysicalTable,
       "cefcPhysicalEntry": cefcPhysicalEntry,
       "cefcPhysicalStatus": cefcPhysicalStatus,
       "cefcPowerCapacity": cefcPowerCapacity,
       "cefcPowerSupplyInputTable": cefcPowerSupplyInputTable,
       "cefcPowerSupplyInputEntry": cefcPowerSupplyInputEntry,
       "cefcPowerSupplyInputIndex": cefcPowerSupplyInputIndex,
       "cefcPowerSupplyInputType": cefcPowerSupplyInputType,
       "cefcPowerSupplyOutputTable": cefcPowerSupplyOutputTable,
       "cefcPowerSupplyOutputEntry": cefcPowerSupplyOutputEntry,
       "cefcPSOutputModeIndex": cefcPSOutputModeIndex,
       "cefcPSOutputModeCurrent": cefcPSOutputModeCurrent,
       "cefcPSOutputModeInOperation": cefcPSOutputModeInOperation,
       "cefcCooling": cefcCooling,
       "cefcChassisCoolingTable": cefcChassisCoolingTable,
       "cefcChassisCoolingEntry": cefcChassisCoolingEntry,
       "cefcChassisPerSlotCoolingCap": cefcChassisPerSlotCoolingCap,
       "cefcChassisPerSlotCoolingUnit": cefcChassisPerSlotCoolingUnit,
       "cefcFanCoolingTable": cefcFanCoolingTable,
       "cefcFanCoolingEntry": cefcFanCoolingEntry,
       "cefcFanCoolingCapacity": cefcFanCoolingCapacity,
       "cefcFanCoolingCapacityUnit": cefcFanCoolingCapacityUnit,
       "cefcModuleCoolingTable": cefcModuleCoolingTable,
       "cefcModuleCoolingEntry": cefcModuleCoolingEntry,
       "cefcModuleCooling": cefcModuleCooling,
       "cefcModuleCoolingUnit": cefcModuleCoolingUnit,
       "cefcFanCoolingCapTable": cefcFanCoolingCapTable,
       "cefcFanCoolingCapEntry": cefcFanCoolingCapEntry,
       "cefcFanCoolingCapIndex": cefcFanCoolingCapIndex,
       "cefcFanCoolingCapModeDescr": cefcFanCoolingCapModeDescr,
       "cefcFanCoolingCapCapacity": cefcFanCoolingCapCapacity,
       "cefcFanCoolingCapCurrent": cefcFanCoolingCapCurrent,
       "cefcFanCoolingCapCapacityUnit": cefcFanCoolingCapCapacityUnit,
       "cefcConnector": cefcConnector,
       "cefcConnectorRatingTable": cefcConnectorRatingTable,
       "cefcConnectorRatingEntry": cefcConnectorRatingEntry,
       "cefcConnectorRating": cefcConnectorRating,
       "cefcModulePowerConsumptionTable": cefcModulePowerConsumptionTable,
       "cefcModulePowerConsumptionEntry": cefcModulePowerConsumptionEntry,
       "cefcModulePowerConsumption": cefcModulePowerConsumption,
       "cefcFRUMIBNotificationPrefix": cefcFRUMIBNotificationPrefix,
       "cefcMIBNotifications": cefcMIBNotifications,
       "cefcModuleStatusChange": cefcModuleStatusChange,
       "cefcPowerStatusChange": cefcPowerStatusChange,
       "cefcFRUInserted": cefcFRUInserted,
       "cefcFRURemoved": cefcFRURemoved,
       "cefcUnrecognizedFRU": cefcUnrecognizedFRU,
       "cefcFanTrayStatusChange": cefcFanTrayStatusChange,
       "cefcPowerSupplyOutputChange": cefcPowerSupplyOutputChange,
       "cefcMIBConformance": cefcMIBConformance,
       "cefcMIBCompliances": cefcMIBCompliances,
       "cefcMIBPowerCompliance": cefcMIBPowerCompliance,
       "cefcMIBPowerCompliance2": cefcMIBPowerCompliance2,
       "cefcMIBPowerCompliance3": cefcMIBPowerCompliance3,
       "cefcMIBPowerCompliance4": cefcMIBPowerCompliance4,
       "cefcMIBPowerCompliance5": cefcMIBPowerCompliance5,
       "cefcMIBPowerCompliance6": cefcMIBPowerCompliance6,
       "cefcMIBPowerCompliance7": cefcMIBPowerCompliance7,
       "cefcMIBPowerCompliance8": cefcMIBPowerCompliance8,
       "cefcMIBPowerCompliance9": cefcMIBPowerCompliance9,
       "cefcMIBGroups": cefcMIBGroups,
       "cefcMIBPowerModeGroup": cefcMIBPowerModeGroup,
       "cefcMIBPowerFRUControlGroup": cefcMIBPowerFRUControlGroup,
       "cefcMIBModuleGroup": cefcMIBModuleGroup,
       "cefcMIBInLinePowerControlGroup": cefcMIBInLinePowerControlGroup,
       "cefcMIBNotificationEnablesGroup": cefcMIBNotificationEnablesGroup,
       "cefcMgmtNotificationsGroup": cefcMgmtNotificationsGroup,
       "cefcModuleGroupRev1": cefcModuleGroupRev1,
       "cefcMIBPowerFRUValueGroup": cefcMIBPowerFRUValueGroup,
       "cefcMIBFanTrayStatusGroup": cefcMIBFanTrayStatusGroup,
       "cefcMIBPhysicalGroup": cefcMIBPhysicalGroup,
       "cefcMgmtNotificationsGroup2": cefcMgmtNotificationsGroup2,
       "cefcMIBPowerOperModeGroup": cefcMIBPowerOperModeGroup,
       "cefcMIBInLinePowerControlGroupRev1": cefcMIBInLinePowerControlGroupRev1,
       "cefcModuleExtGroup": cefcModuleExtGroup,
       "cefcIntelliModuleGroup": cefcIntelliModuleGroup,
       "cefcPowerCapacityGroup": cefcPowerCapacityGroup,
       "cefcCoolingGroup": cefcCoolingGroup,
       "cefcConnectorRatingGroup": cefcConnectorRatingGroup,
       "cefcMIBNotificationEnablesGroup2": cefcMIBNotificationEnablesGroup2,
       "cefcMgmtNotificationsGroup3": cefcMgmtNotificationsGroup3,
       "cefcMIBInLinePowerCurrentGroup": cefcMIBInLinePowerCurrentGroup,
       "cefcMIBPowerRedundancyInfoGroup": cefcMIBPowerRedundancyInfoGroup,
       "cefcFanCoolingCapGroup": cefcFanCoolingCapGroup,
       "cefcMIBModuleLocalSwitchingGroup": cefcMIBModuleLocalSwitchingGroup,
       "cefcFRUPowerRealTimeStatusGroup": cefcFRUPowerRealTimeStatusGroup,
       "cefcFRUPowerCapabilityGroup": cefcFRUPowerCapabilityGroup,
       "cefcFRUCoolingUnitGroup": cefcFRUCoolingUnitGroup,
       "cefcFRUFanCoolingUnitGroup": cefcFRUFanCoolingUnitGroup,
       "cefcCoolingGroup2": cefcCoolingGroup2,
       "cefcFanCoolingGroup": cefcFanCoolingGroup}
)
