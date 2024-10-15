# SNMP MIB module (PWG-IMAGING-COUNTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PWG-IMAGING-COUNTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:40:24 2024
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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

imagingCounterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3)
)
imagingCounterMIB.setRevisions(
        ("2008-03-18 00:00",
         "2005-12-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IcCounter32(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class IcCounterEventTypeTC(Integer32, TextualConvention):
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("counterCreated", 3),
          ("counterForErrors", 4),
          ("counterForWarnings", 5),
          ("counterInterval", 13),
          ("counterReset", 6),
          ("counterThreshold", 14),
          ("counterWrap", 7),
          ("mediaUsedCreated", 10),
          ("other", 1),
          ("serviceCreated", 8),
          ("serviceStateChanged", 11),
          ("subunitCreated", 9),
          ("subunitStatusChanged", 12),
          ("unknown", 2))
    )



class IcPersistenceTC(Integer32, TextualConvention):
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
        *(("lifetime", 3),
          ("other", 1),
          ("powerOn", 4),
          ("reset", 5),
          ("unknown", 2))
    )



class IcServiceStateTC(Integer32, TextualConvention):
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
        *(("down", 7),
          ("idle", 3),
          ("other", 1),
          ("processing", 4),
          ("stopped", 5),
          ("testing", 6),
          ("unknown", 2))
    )



class IcServiceTypeTC(Integer32, TextualConvention):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("copy", 4),
          ("emailIn", 5),
          ("emailOut", 6),
          ("faxIn", 7),
          ("faxOut", 8),
          ("networkFaxIn", 9),
          ("networkFaxOut", 10),
          ("other", 1),
          ("print", 11),
          ("scan", 12),
          ("systemTotals", 3),
          ("transform", 13),
          ("unknown", 2))
    )



class IcSubunitStatusTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )



class IcSubunitTypeTC(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              6,
              8,
              9,
              10,
              13,
              14,
              15,
              30,
              40,
              50,
              302,
              303,
              304,
              305,
              306,
              307,
              308,
              309,
              310,
              311,
              312,
              313,
              314,
              315,
              316,
              317,
              318,
              503,
              504)
        )
    )
    namedValues = NamedValues(
        *(("bander", 314),
          ("binder", 305),
          ("channel", 14),
          ("console", 4),
          ("cover", 6),
          ("dieCutter", 307),
          ("finisher", 30),
          ("folder", 304),
          ("imprinter", 312),
          ("inputTray", 8),
          ("inserter", 318),
          ("interface", 40),
          ("interpreter", 15),
          ("makeEnvelope", 315),
          ("marker", 10),
          ("mediaPath", 13),
          ("other", 1),
          ("outputTray", 9),
          ("perforater", 309),
          ("puncher", 308),
          ("scanner", 50),
          ("scannerADF", 503),
          ("scannerPlaten", 504),
          ("separationCutter", 311),
          ("sheetRotator", 317),
          ("slitter", 310),
          ("stacker", 316),
          ("stapler", 302),
          ("stitcher", 303),
          ("trimmer", 306),
          ("unknown", 2),
          ("wrapper", 313))
    )



class IcWorkTypeTC(Integer32, TextualConvention):
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
        *(("auxiliary", 5),
          ("datastream", 4),
          ("maintenance", 7),
          ("other", 1),
          ("unknown", 2),
          ("waste", 6),
          ("workTotals", 3))
    )



# MIB Managed Objects in the order of their OIDs

_IcMIBNotifications_ObjectIdentity = ObjectIdentity
icMIBNotifications = _IcMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 0)
)
_IcMIBObjects_ObjectIdentity = ObjectIdentity
icMIBObjects = _IcMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1)
)
_IcGeneral_ObjectIdentity = ObjectIdentity
icGeneral = _IcGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 1)
)


class _IcGeneralNaturalLanguage_Type(DisplayString):
    """Custom type icGeneralNaturalLanguage based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IcGeneralNaturalLanguage_Type.__name__ = "DisplayString"
_IcGeneralNaturalLanguage_Object = MibScalar
icGeneralNaturalLanguage = _IcGeneralNaturalLanguage_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 1, 1),
    _IcGeneralNaturalLanguage_Type()
)
icGeneralNaturalLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icGeneralNaturalLanguage.setStatus("current")


class _IcGeneralTotalServiceRecords_Type(IcCounter32):
    """Custom type icGeneralTotalServiceRecords based on IcCounter32"""
    defaultValue = 0


_IcGeneralTotalServiceRecords_Object = MibScalar
icGeneralTotalServiceRecords = _IcGeneralTotalServiceRecords_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 1, 2),
    _IcGeneralTotalServiceRecords_Type()
)
icGeneralTotalServiceRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icGeneralTotalServiceRecords.setStatus("current")
if mibBuilder.loadTexts:
    icGeneralTotalServiceRecords.setUnits("records")


class _IcGeneralTotalSubunitRecords_Type(IcCounter32):
    """Custom type icGeneralTotalSubunitRecords based on IcCounter32"""
    defaultValue = 0


_IcGeneralTotalSubunitRecords_Object = MibScalar
icGeneralTotalSubunitRecords = _IcGeneralTotalSubunitRecords_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 1, 3),
    _IcGeneralTotalSubunitRecords_Type()
)
icGeneralTotalSubunitRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icGeneralTotalSubunitRecords.setStatus("current")
if mibBuilder.loadTexts:
    icGeneralTotalSubunitRecords.setUnits("records")


class _IcGeneralTotalMediaUsedRecords_Type(IcCounter32):
    """Custom type icGeneralTotalMediaUsedRecords based on IcCounter32"""
    defaultValue = 0


_IcGeneralTotalMediaUsedRecords_Object = MibScalar
icGeneralTotalMediaUsedRecords = _IcGeneralTotalMediaUsedRecords_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 1, 4),
    _IcGeneralTotalMediaUsedRecords_Type()
)
icGeneralTotalMediaUsedRecords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icGeneralTotalMediaUsedRecords.setStatus("current")
if mibBuilder.loadTexts:
    icGeneralTotalMediaUsedRecords.setUnits("records")
_IcKey_ObjectIdentity = ObjectIdentity
icKey = _IcKey_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2)
)
_IcKeyTable_Object = MibTable
icKeyTable = _IcKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    icKeyTable.setStatus("current")
_IcKeyEntry_Object = MibTableRow
icKeyEntry = _IcKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1, 1)
)
icKeyEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icKeyIndex"),
)
if mibBuilder.loadTexts:
    icKeyEntry.setStatus("current")


class _IcKeyIndex_Type(Integer32):
    """Custom type icKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcKeyIndex_Type.__name__ = "Integer32"
_IcKeyIndex_Object = MibTableColumn
icKeyIndex = _IcKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1, 1, 1),
    _IcKeyIndex_Type()
)
icKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icKeyIndex.setStatus("current")


class _IcKeyServiceType_Type(IcServiceTypeTC):
    """Custom type icKeyServiceType based on IcServiceTypeTC"""


_IcKeyServiceType_Object = MibTableColumn
icKeyServiceType = _IcKeyServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1, 1, 2),
    _IcKeyServiceType_Type()
)
icKeyServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icKeyServiceType.setStatus("current")


class _IcKeyServiceIndex_Type(Integer32):
    """Custom type icKeyServiceIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IcKeyServiceIndex_Type.__name__ = "Integer32"
_IcKeyServiceIndex_Object = MibTableColumn
icKeyServiceIndex = _IcKeyServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1, 1, 3),
    _IcKeyServiceIndex_Type()
)
icKeyServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icKeyServiceIndex.setStatus("current")


class _IcKeySubunitType_Type(IcSubunitTypeTC):
    """Custom type icKeySubunitType based on IcSubunitTypeTC"""


_IcKeySubunitType_Object = MibTableColumn
icKeySubunitType = _IcKeySubunitType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1, 1, 4),
    _IcKeySubunitType_Type()
)
icKeySubunitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icKeySubunitType.setStatus("current")


class _IcKeySubunitIndex_Type(Integer32):
    """Custom type icKeySubunitIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IcKeySubunitIndex_Type.__name__ = "Integer32"
_IcKeySubunitIndex_Object = MibTableColumn
icKeySubunitIndex = _IcKeySubunitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 2, 1, 1, 5),
    _IcKeySubunitIndex_Type()
)
icKeySubunitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icKeySubunitIndex.setStatus("current")
_IcService_ObjectIdentity = ObjectIdentity
icService = _IcService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3)
)
_IcServiceTable_Object = MibTable
icServiceTable = _IcServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1)
)
if mibBuilder.loadTexts:
    icServiceTable.setStatus("current")
_IcServiceEntry_Object = MibTableRow
icServiceEntry = _IcServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1)
)
icServiceEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icServiceType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icServiceIndex"),
)
if mibBuilder.loadTexts:
    icServiceEntry.setStatus("current")
_IcServiceType_Type = IcServiceTypeTC
_IcServiceType_Object = MibTableColumn
icServiceType = _IcServiceType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 1),
    _IcServiceType_Type()
)
icServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icServiceType.setStatus("current")


class _IcServiceIndex_Type(Integer32):
    """Custom type icServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcServiceIndex_Type.__name__ = "Integer32"
_IcServiceIndex_Object = MibTableColumn
icServiceIndex = _IcServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 2),
    _IcServiceIndex_Type()
)
icServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icServiceIndex.setStatus("current")


class _IcServiceKey_Type(Integer32):
    """Custom type icServiceKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcServiceKey_Type.__name__ = "Integer32"
_IcServiceKey_Object = MibTableColumn
icServiceKey = _IcServiceKey_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 3),
    _IcServiceKey_Type()
)
icServiceKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icServiceKey.setStatus("current")


class _IcServiceInfo_Type(SnmpAdminString):
    """Custom type icServiceInfo based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcServiceInfo_Type.__name__ = "SnmpAdminString"
_IcServiceInfo_Object = MibTableColumn
icServiceInfo = _IcServiceInfo_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 4),
    _IcServiceInfo_Type()
)
icServiceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icServiceInfo.setStatus("current")


class _IcServiceJobSetIndex_Type(Integer32):
    """Custom type icServiceJobSetIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_IcServiceJobSetIndex_Type.__name__ = "Integer32"
_IcServiceJobSetIndex_Object = MibTableColumn
icServiceJobSetIndex = _IcServiceJobSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 5),
    _IcServiceJobSetIndex_Type()
)
icServiceJobSetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icServiceJobSetIndex.setStatus("current")


class _IcServiceState_Type(IcServiceStateTC):
    """Custom type icServiceState based on IcServiceStateTC"""


_IcServiceState_Object = MibTableColumn
icServiceState = _IcServiceState_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 6),
    _IcServiceState_Type()
)
icServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icServiceState.setStatus("current")


class _IcServiceStateMessage_Type(SnmpAdminString):
    """Custom type icServiceStateMessage based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcServiceStateMessage_Type.__name__ = "SnmpAdminString"
_IcServiceStateMessage_Object = MibTableColumn
icServiceStateMessage = _IcServiceStateMessage_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 7),
    _IcServiceStateMessage_Type()
)
icServiceStateMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icServiceStateMessage.setStatus("current")


class _IcServicePrtAlertIndex_Type(Integer32):
    """Custom type icServicePrtAlertIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IcServicePrtAlertIndex_Type.__name__ = "Integer32"
_IcServicePrtAlertIndex_Object = MibTableColumn
icServicePrtAlertIndex = _IcServicePrtAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 3, 1, 1, 8),
    _IcServicePrtAlertIndex_Type()
)
icServicePrtAlertIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icServicePrtAlertIndex.setStatus("current")
_IcSubunit_ObjectIdentity = ObjectIdentity
icSubunit = _IcSubunit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4)
)
_IcSubunitTable_Object = MibTable
icSubunitTable = _IcSubunitTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    icSubunitTable.setStatus("current")
_IcSubunitEntry_Object = MibTableRow
icSubunitEntry = _IcSubunitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1)
)
icSubunitEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icSubunitType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icSubunitIndex"),
)
if mibBuilder.loadTexts:
    icSubunitEntry.setStatus("current")
_IcSubunitType_Type = IcSubunitTypeTC
_IcSubunitType_Object = MibTableColumn
icSubunitType = _IcSubunitType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1, 1),
    _IcSubunitType_Type()
)
icSubunitType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSubunitType.setStatus("current")


class _IcSubunitIndex_Type(Integer32):
    """Custom type icSubunitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcSubunitIndex_Type.__name__ = "Integer32"
_IcSubunitIndex_Object = MibTableColumn
icSubunitIndex = _IcSubunitIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1, 2),
    _IcSubunitIndex_Type()
)
icSubunitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSubunitIndex.setStatus("current")


class _IcSubunitKey_Type(Integer32):
    """Custom type icSubunitKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcSubunitKey_Type.__name__ = "Integer32"
_IcSubunitKey_Object = MibTableColumn
icSubunitKey = _IcSubunitKey_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1, 3),
    _IcSubunitKey_Type()
)
icSubunitKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSubunitKey.setStatus("current")


class _IcSubunitInfo_Type(SnmpAdminString):
    """Custom type icSubunitInfo based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcSubunitInfo_Type.__name__ = "SnmpAdminString"
_IcSubunitInfo_Object = MibTableColumn
icSubunitInfo = _IcSubunitInfo_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1, 4),
    _IcSubunitInfo_Type()
)
icSubunitInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSubunitInfo.setStatus("current")


class _IcSubunitStatus_Type(IcSubunitStatusTC):
    """Custom type icSubunitStatus based on IcSubunitStatusTC"""
    defaultValue = 5


_IcSubunitStatus_Object = MibTableColumn
icSubunitStatus = _IcSubunitStatus_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1, 5),
    _IcSubunitStatus_Type()
)
icSubunitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSubunitStatus.setStatus("current")


class _IcSubunitStatusMessage_Type(SnmpAdminString):
    """Custom type icSubunitStatusMessage based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcSubunitStatusMessage_Type.__name__ = "SnmpAdminString"
_IcSubunitStatusMessage_Object = MibTableColumn
icSubunitStatusMessage = _IcSubunitStatusMessage_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 4, 1, 1, 6),
    _IcSubunitStatusMessage_Type()
)
icSubunitStatusMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSubunitStatusMessage.setStatus("current")
_IcTime_ObjectIdentity = ObjectIdentity
icTime = _IcTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5)
)
_IcTimeTable_Object = MibTable
icTimeTable = _IcTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1)
)
if mibBuilder.loadTexts:
    icTimeTable.setStatus("current")
_IcTimeEntry_Object = MibTableRow
icTimeEntry = _IcTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1)
)
icTimeEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icTimeKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icTimePersistence"),
)
if mibBuilder.loadTexts:
    icTimeEntry.setStatus("current")


class _IcTimeKeyIndex_Type(Integer32):
    """Custom type icTimeKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcTimeKeyIndex_Type.__name__ = "Integer32"
_IcTimeKeyIndex_Object = MibTableColumn
icTimeKeyIndex = _IcTimeKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1, 1),
    _IcTimeKeyIndex_Type()
)
icTimeKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTimeKeyIndex.setStatus("current")
_IcTimePersistence_Type = IcPersistenceTC
_IcTimePersistence_Object = MibTableColumn
icTimePersistence = _IcTimePersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1, 2),
    _IcTimePersistence_Type()
)
icTimePersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTimePersistence.setStatus("current")


class _IcTimeTotalSeconds_Type(IcCounter32):
    """Custom type icTimeTotalSeconds based on IcCounter32"""
    defaultValue = 0


_IcTimeTotalSeconds_Object = MibTableColumn
icTimeTotalSeconds = _IcTimeTotalSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1, 3),
    _IcTimeTotalSeconds_Type()
)
icTimeTotalSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTimeTotalSeconds.setStatus("current")
if mibBuilder.loadTexts:
    icTimeTotalSeconds.setUnits("seconds")


class _IcTimeDownSeconds_Type(IcCounter32):
    """Custom type icTimeDownSeconds based on IcCounter32"""
    defaultValue = 0


_IcTimeDownSeconds_Object = MibTableColumn
icTimeDownSeconds = _IcTimeDownSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1, 4),
    _IcTimeDownSeconds_Type()
)
icTimeDownSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTimeDownSeconds.setStatus("current")
if mibBuilder.loadTexts:
    icTimeDownSeconds.setUnits("seconds")


class _IcTimeMaintenanceSeconds_Type(IcCounter32):
    """Custom type icTimeMaintenanceSeconds based on IcCounter32"""
    defaultValue = 0


_IcTimeMaintenanceSeconds_Object = MibTableColumn
icTimeMaintenanceSeconds = _IcTimeMaintenanceSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1, 5),
    _IcTimeMaintenanceSeconds_Type()
)
icTimeMaintenanceSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTimeMaintenanceSeconds.setStatus("current")
if mibBuilder.loadTexts:
    icTimeMaintenanceSeconds.setUnits("seconds")


class _IcTimeProcessingSeconds_Type(IcCounter32):
    """Custom type icTimeProcessingSeconds based on IcCounter32"""
    defaultValue = 0


_IcTimeProcessingSeconds_Object = MibTableColumn
icTimeProcessingSeconds = _IcTimeProcessingSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 5, 1, 1, 6),
    _IcTimeProcessingSeconds_Type()
)
icTimeProcessingSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTimeProcessingSeconds.setStatus("current")
if mibBuilder.loadTexts:
    icTimeProcessingSeconds.setUnits("seconds")
_IcMonitor_ObjectIdentity = ObjectIdentity
icMonitor = _IcMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6)
)
_IcMonitorTable_Object = MibTable
icMonitorTable = _IcMonitorTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1)
)
if mibBuilder.loadTexts:
    icMonitorTable.setStatus("current")
_IcMonitorEntry_Object = MibTableRow
icMonitorEntry = _IcMonitorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1)
)
icMonitorEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icMonitorKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icMonitorPersistence"),
)
if mibBuilder.loadTexts:
    icMonitorEntry.setStatus("current")


class _IcMonitorKeyIndex_Type(Integer32):
    """Custom type icMonitorKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcMonitorKeyIndex_Type.__name__ = "Integer32"
_IcMonitorKeyIndex_Object = MibTableColumn
icMonitorKeyIndex = _IcMonitorKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 1),
    _IcMonitorKeyIndex_Type()
)
icMonitorKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icMonitorKeyIndex.setStatus("current")
_IcMonitorPersistence_Type = IcPersistenceTC
_IcMonitorPersistence_Object = MibTableColumn
icMonitorPersistence = _IcMonitorPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 2),
    _IcMonitorPersistence_Type()
)
icMonitorPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icMonitorPersistence.setStatus("current")


class _IcMonitorConfigChanges_Type(IcCounter32):
    """Custom type icMonitorConfigChanges based on IcCounter32"""
    defaultValue = 0


_IcMonitorConfigChanges_Object = MibTableColumn
icMonitorConfigChanges = _IcMonitorConfigChanges_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 3),
    _IcMonitorConfigChanges_Type()
)
icMonitorConfigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorConfigChanges.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorConfigChanges.setUnits("changes")


class _IcMonitorTotalAlerts_Type(IcCounter32):
    """Custom type icMonitorTotalAlerts based on IcCounter32"""
    defaultValue = 0


_IcMonitorTotalAlerts_Object = MibTableColumn
icMonitorTotalAlerts = _IcMonitorTotalAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 4),
    _IcMonitorTotalAlerts_Type()
)
icMonitorTotalAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorTotalAlerts.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorTotalAlerts.setUnits("alerts")


class _IcMonitorCriticalAlerts_Type(IcCounter32):
    """Custom type icMonitorCriticalAlerts based on IcCounter32"""
    defaultValue = 0


_IcMonitorCriticalAlerts_Object = MibTableColumn
icMonitorCriticalAlerts = _IcMonitorCriticalAlerts_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 5),
    _IcMonitorCriticalAlerts_Type()
)
icMonitorCriticalAlerts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorCriticalAlerts.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorCriticalAlerts.setUnits("alerts")


class _IcMonitorAbortedJobs_Type(IcCounter32):
    """Custom type icMonitorAbortedJobs based on IcCounter32"""
    defaultValue = 0


_IcMonitorAbortedJobs_Object = MibTableColumn
icMonitorAbortedJobs = _IcMonitorAbortedJobs_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 6),
    _IcMonitorAbortedJobs_Type()
)
icMonitorAbortedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorAbortedJobs.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorAbortedJobs.setUnits("jobs")


class _IcMonitorCanceledJobs_Type(IcCounter32):
    """Custom type icMonitorCanceledJobs based on IcCounter32"""
    defaultValue = 0


_IcMonitorCanceledJobs_Object = MibTableColumn
icMonitorCanceledJobs = _IcMonitorCanceledJobs_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 7),
    _IcMonitorCanceledJobs_Type()
)
icMonitorCanceledJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorCanceledJobs.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorCanceledJobs.setUnits("jobs")


class _IcMonitorCompletedJobs_Type(IcCounter32):
    """Custom type icMonitorCompletedJobs based on IcCounter32"""
    defaultValue = 0


_IcMonitorCompletedJobs_Object = MibTableColumn
icMonitorCompletedJobs = _IcMonitorCompletedJobs_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 8),
    _IcMonitorCompletedJobs_Type()
)
icMonitorCompletedJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorCompletedJobs.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorCompletedJobs.setUnits("jobs")


class _IcMonitorCompletedFinisherJobs_Type(IcCounter32):
    """Custom type icMonitorCompletedFinisherJobs based on IcCounter32"""
    defaultValue = 0


_IcMonitorCompletedFinisherJobs_Object = MibTableColumn
icMonitorCompletedFinisherJobs = _IcMonitorCompletedFinisherJobs_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 9),
    _IcMonitorCompletedFinisherJobs_Type()
)
icMonitorCompletedFinisherJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorCompletedFinisherJobs.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorCompletedFinisherJobs.setUnits("jobs")


class _IcMonitorMemoryAllocErrors_Type(IcCounter32):
    """Custom type icMonitorMemoryAllocErrors based on IcCounter32"""
    defaultValue = 0


_IcMonitorMemoryAllocErrors_Object = MibTableColumn
icMonitorMemoryAllocErrors = _IcMonitorMemoryAllocErrors_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 10),
    _IcMonitorMemoryAllocErrors_Type()
)
icMonitorMemoryAllocErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorMemoryAllocErrors.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorMemoryAllocErrors.setUnits("errors")


class _IcMonitorMemoryAllocWarnings_Type(IcCounter32):
    """Custom type icMonitorMemoryAllocWarnings based on IcCounter32"""
    defaultValue = 0


_IcMonitorMemoryAllocWarnings_Object = MibTableColumn
icMonitorMemoryAllocWarnings = _IcMonitorMemoryAllocWarnings_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 11),
    _IcMonitorMemoryAllocWarnings_Type()
)
icMonitorMemoryAllocWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorMemoryAllocWarnings.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorMemoryAllocWarnings.setUnits("warnings")


class _IcMonitorStorageAllocErrors_Type(IcCounter32):
    """Custom type icMonitorStorageAllocErrors based on IcCounter32"""
    defaultValue = 0


_IcMonitorStorageAllocErrors_Object = MibTableColumn
icMonitorStorageAllocErrors = _IcMonitorStorageAllocErrors_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 12),
    _IcMonitorStorageAllocErrors_Type()
)
icMonitorStorageAllocErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorStorageAllocErrors.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorStorageAllocErrors.setUnits("errors")


class _IcMonitorStorageAllocWarnings_Type(IcCounter32):
    """Custom type icMonitorStorageAllocWarnings based on IcCounter32"""
    defaultValue = 0


_IcMonitorStorageAllocWarnings_Object = MibTableColumn
icMonitorStorageAllocWarnings = _IcMonitorStorageAllocWarnings_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 13),
    _IcMonitorStorageAllocWarnings_Type()
)
icMonitorStorageAllocWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorStorageAllocWarnings.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorStorageAllocWarnings.setUnits("warnings")


class _IcMonitorLocalStorageKOctets_Type(IcCounter32):
    """Custom type icMonitorLocalStorageKOctets based on IcCounter32"""
    defaultValue = 0


_IcMonitorLocalStorageKOctets_Object = MibTableColumn
icMonitorLocalStorageKOctets = _IcMonitorLocalStorageKOctets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 14),
    _IcMonitorLocalStorageKOctets_Type()
)
icMonitorLocalStorageKOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorLocalStorageKOctets.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorLocalStorageKOctets.setUnits("koctets")


class _IcMonitorRemoteStorageKOctets_Type(IcCounter32):
    """Custom type icMonitorRemoteStorageKOctets based on IcCounter32"""
    defaultValue = 0


_IcMonitorRemoteStorageKOctets_Object = MibTableColumn
icMonitorRemoteStorageKOctets = _IcMonitorRemoteStorageKOctets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 6, 1, 1, 15),
    _IcMonitorRemoteStorageKOctets_Type()
)
icMonitorRemoteStorageKOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMonitorRemoteStorageKOctets.setStatus("current")
if mibBuilder.loadTexts:
    icMonitorRemoteStorageKOctets.setUnits("koctets")
_IcImage_ObjectIdentity = ObjectIdentity
icImage = _IcImage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7)
)
_IcImageTable_Object = MibTable
icImageTable = _IcImageTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1)
)
if mibBuilder.loadTexts:
    icImageTable.setStatus("current")
_IcImageEntry_Object = MibTableRow
icImageEntry = _IcImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1)
)
icImageEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icImageKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icImageWorkType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icImagePersistence"),
)
if mibBuilder.loadTexts:
    icImageEntry.setStatus("current")


class _IcImageKeyIndex_Type(Integer32):
    """Custom type icImageKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcImageKeyIndex_Type.__name__ = "Integer32"
_IcImageKeyIndex_Object = MibTableColumn
icImageKeyIndex = _IcImageKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1, 1),
    _IcImageKeyIndex_Type()
)
icImageKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icImageKeyIndex.setStatus("current")
_IcImageWorkType_Type = IcWorkTypeTC
_IcImageWorkType_Object = MibTableColumn
icImageWorkType = _IcImageWorkType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1, 2),
    _IcImageWorkType_Type()
)
icImageWorkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icImageWorkType.setStatus("current")
_IcImagePersistence_Type = IcPersistenceTC
_IcImagePersistence_Object = MibTableColumn
icImagePersistence = _IcImagePersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1, 3),
    _IcImagePersistence_Type()
)
icImagePersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icImagePersistence.setStatus("current")


class _IcImageTotalImages_Type(IcCounter32):
    """Custom type icImageTotalImages based on IcCounter32"""
    defaultValue = 0


_IcImageTotalImages_Object = MibTableColumn
icImageTotalImages = _IcImageTotalImages_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1, 4),
    _IcImageTotalImages_Type()
)
icImageTotalImages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImageTotalImages.setStatus("current")
if mibBuilder.loadTexts:
    icImageTotalImages.setUnits("images")


class _IcImageMonochromeImages_Type(IcCounter32):
    """Custom type icImageMonochromeImages based on IcCounter32"""
    defaultValue = 0


_IcImageMonochromeImages_Object = MibTableColumn
icImageMonochromeImages = _IcImageMonochromeImages_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1, 5),
    _IcImageMonochromeImages_Type()
)
icImageMonochromeImages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImageMonochromeImages.setStatus("current")
if mibBuilder.loadTexts:
    icImageMonochromeImages.setUnits("images")


class _IcImageFullColorImages_Type(IcCounter32):
    """Custom type icImageFullColorImages based on IcCounter32"""
    defaultValue = 0


_IcImageFullColorImages_Object = MibTableColumn
icImageFullColorImages = _IcImageFullColorImages_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 7, 1, 1, 6),
    _IcImageFullColorImages_Type()
)
icImageFullColorImages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImageFullColorImages.setStatus("current")
if mibBuilder.loadTexts:
    icImageFullColorImages.setUnits("images")
_IcImpression_ObjectIdentity = ObjectIdentity
icImpression = _IcImpression_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8)
)
_IcImpressionTable_Object = MibTable
icImpressionTable = _IcImpressionTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1)
)
if mibBuilder.loadTexts:
    icImpressionTable.setStatus("current")
_IcImpressionEntry_Object = MibTableRow
icImpressionEntry = _IcImpressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1)
)
icImpressionEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icImpressionKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icImpressionWorkType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icImpressionPersistence"),
)
if mibBuilder.loadTexts:
    icImpressionEntry.setStatus("current")


class _IcImpressionKeyIndex_Type(Integer32):
    """Custom type icImpressionKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcImpressionKeyIndex_Type.__name__ = "Integer32"
_IcImpressionKeyIndex_Object = MibTableColumn
icImpressionKeyIndex = _IcImpressionKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 1),
    _IcImpressionKeyIndex_Type()
)
icImpressionKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icImpressionKeyIndex.setStatus("current")
_IcImpressionWorkType_Type = IcWorkTypeTC
_IcImpressionWorkType_Object = MibTableColumn
icImpressionWorkType = _IcImpressionWorkType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 2),
    _IcImpressionWorkType_Type()
)
icImpressionWorkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icImpressionWorkType.setStatus("current")
_IcImpressionPersistence_Type = IcPersistenceTC
_IcImpressionPersistence_Object = MibTableColumn
icImpressionPersistence = _IcImpressionPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 3),
    _IcImpressionPersistence_Type()
)
icImpressionPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icImpressionPersistence.setStatus("current")


class _IcImpressionTotalImps_Type(IcCounter32):
    """Custom type icImpressionTotalImps based on IcCounter32"""
    defaultValue = 0


_IcImpressionTotalImps_Object = MibTableColumn
icImpressionTotalImps = _IcImpressionTotalImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 4),
    _IcImpressionTotalImps_Type()
)
icImpressionTotalImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImpressionTotalImps.setStatus("current")
if mibBuilder.loadTexts:
    icImpressionTotalImps.setUnits("impressions")


class _IcImpressionMonochromeImps_Type(IcCounter32):
    """Custom type icImpressionMonochromeImps based on IcCounter32"""
    defaultValue = 0


_IcImpressionMonochromeImps_Object = MibTableColumn
icImpressionMonochromeImps = _IcImpressionMonochromeImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 5),
    _IcImpressionMonochromeImps_Type()
)
icImpressionMonochromeImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImpressionMonochromeImps.setStatus("current")
if mibBuilder.loadTexts:
    icImpressionMonochromeImps.setUnits("impressions")


class _IcImpressionBlankImps_Type(IcCounter32):
    """Custom type icImpressionBlankImps based on IcCounter32"""
    defaultValue = 0


_IcImpressionBlankImps_Object = MibTableColumn
icImpressionBlankImps = _IcImpressionBlankImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 6),
    _IcImpressionBlankImps_Type()
)
icImpressionBlankImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImpressionBlankImps.setStatus("current")
if mibBuilder.loadTexts:
    icImpressionBlankImps.setUnits("impressions")


class _IcImpressionFullColorImps_Type(IcCounter32):
    """Custom type icImpressionFullColorImps based on IcCounter32"""
    defaultValue = 0


_IcImpressionFullColorImps_Object = MibTableColumn
icImpressionFullColorImps = _IcImpressionFullColorImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 7),
    _IcImpressionFullColorImps_Type()
)
icImpressionFullColorImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImpressionFullColorImps.setStatus("current")
if mibBuilder.loadTexts:
    icImpressionFullColorImps.setUnits("impressions")


class _IcImpressionHighlightColorImps_Type(IcCounter32):
    """Custom type icImpressionHighlightColorImps based on IcCounter32"""
    defaultValue = 0


_IcImpressionHighlightColorImps_Object = MibTableColumn
icImpressionHighlightColorImps = _IcImpressionHighlightColorImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 8, 1, 1, 8),
    _IcImpressionHighlightColorImps_Type()
)
icImpressionHighlightColorImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icImpressionHighlightColorImps.setStatus("current")
if mibBuilder.loadTexts:
    icImpressionHighlightColorImps.setUnits("impressions")
_IcTwoSided_ObjectIdentity = ObjectIdentity
icTwoSided = _IcTwoSided_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9)
)
_IcTwoSidedTable_Object = MibTable
icTwoSidedTable = _IcTwoSidedTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1)
)
if mibBuilder.loadTexts:
    icTwoSidedTable.setStatus("current")
_IcTwoSidedEntry_Object = MibTableRow
icTwoSidedEntry = _IcTwoSidedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1)
)
icTwoSidedEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icTwoSidedKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icTwoSidedWorkType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icTwoSidedPersistence"),
)
if mibBuilder.loadTexts:
    icTwoSidedEntry.setStatus("current")


class _IcTwoSidedKeyIndex_Type(Integer32):
    """Custom type icTwoSidedKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcTwoSidedKeyIndex_Type.__name__ = "Integer32"
_IcTwoSidedKeyIndex_Object = MibTableColumn
icTwoSidedKeyIndex = _IcTwoSidedKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 1),
    _IcTwoSidedKeyIndex_Type()
)
icTwoSidedKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTwoSidedKeyIndex.setStatus("current")
_IcTwoSidedWorkType_Type = IcWorkTypeTC
_IcTwoSidedWorkType_Object = MibTableColumn
icTwoSidedWorkType = _IcTwoSidedWorkType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 2),
    _IcTwoSidedWorkType_Type()
)
icTwoSidedWorkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTwoSidedWorkType.setStatus("current")
_IcTwoSidedPersistence_Type = IcPersistenceTC
_IcTwoSidedPersistence_Object = MibTableColumn
icTwoSidedPersistence = _IcTwoSidedPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 3),
    _IcTwoSidedPersistence_Type()
)
icTwoSidedPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTwoSidedPersistence.setStatus("current")


class _IcTwoSidedTotalImps_Type(IcCounter32):
    """Custom type icTwoSidedTotalImps based on IcCounter32"""
    defaultValue = 0


_IcTwoSidedTotalImps_Object = MibTableColumn
icTwoSidedTotalImps = _IcTwoSidedTotalImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 4),
    _IcTwoSidedTotalImps_Type()
)
icTwoSidedTotalImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTwoSidedTotalImps.setStatus("current")
if mibBuilder.loadTexts:
    icTwoSidedTotalImps.setUnits("impressions")


class _IcTwoSidedMonochromeImps_Type(IcCounter32):
    """Custom type icTwoSidedMonochromeImps based on IcCounter32"""
    defaultValue = 0


_IcTwoSidedMonochromeImps_Object = MibTableColumn
icTwoSidedMonochromeImps = _IcTwoSidedMonochromeImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 5),
    _IcTwoSidedMonochromeImps_Type()
)
icTwoSidedMonochromeImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTwoSidedMonochromeImps.setStatus("current")
if mibBuilder.loadTexts:
    icTwoSidedMonochromeImps.setUnits("impressions")


class _IcTwoSidedBlankImps_Type(IcCounter32):
    """Custom type icTwoSidedBlankImps based on IcCounter32"""
    defaultValue = 0


_IcTwoSidedBlankImps_Object = MibTableColumn
icTwoSidedBlankImps = _IcTwoSidedBlankImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 6),
    _IcTwoSidedBlankImps_Type()
)
icTwoSidedBlankImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTwoSidedBlankImps.setStatus("current")
if mibBuilder.loadTexts:
    icTwoSidedBlankImps.setUnits("impressions")


class _IcTwoSidedFullColorImps_Type(IcCounter32):
    """Custom type icTwoSidedFullColorImps based on IcCounter32"""
    defaultValue = 0


_IcTwoSidedFullColorImps_Object = MibTableColumn
icTwoSidedFullColorImps = _IcTwoSidedFullColorImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 7),
    _IcTwoSidedFullColorImps_Type()
)
icTwoSidedFullColorImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTwoSidedFullColorImps.setStatus("current")
if mibBuilder.loadTexts:
    icTwoSidedFullColorImps.setUnits("impressions")


class _IcTwoSidedHighlightColorImps_Type(IcCounter32):
    """Custom type icTwoSidedHighlightColorImps based on IcCounter32"""
    defaultValue = 0


_IcTwoSidedHighlightColorImps_Object = MibTableColumn
icTwoSidedHighlightColorImps = _IcTwoSidedHighlightColorImps_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 9, 1, 1, 8),
    _IcTwoSidedHighlightColorImps_Type()
)
icTwoSidedHighlightColorImps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTwoSidedHighlightColorImps.setStatus("current")
if mibBuilder.loadTexts:
    icTwoSidedHighlightColorImps.setUnits("impressions")
_IcSheet_ObjectIdentity = ObjectIdentity
icSheet = _IcSheet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10)
)
_IcSheetTable_Object = MibTable
icSheetTable = _IcSheetTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1)
)
if mibBuilder.loadTexts:
    icSheetTable.setStatus("current")
_IcSheetEntry_Object = MibTableRow
icSheetEntry = _IcSheetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1)
)
icSheetEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icSheetKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icSheetWorkType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icSheetPersistence"),
)
if mibBuilder.loadTexts:
    icSheetEntry.setStatus("current")


class _IcSheetKeyIndex_Type(Integer32):
    """Custom type icSheetKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcSheetKeyIndex_Type.__name__ = "Integer32"
_IcSheetKeyIndex_Object = MibTableColumn
icSheetKeyIndex = _IcSheetKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 1),
    _IcSheetKeyIndex_Type()
)
icSheetKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSheetKeyIndex.setStatus("current")
_IcSheetWorkType_Type = IcWorkTypeTC
_IcSheetWorkType_Object = MibTableColumn
icSheetWorkType = _IcSheetWorkType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 2),
    _IcSheetWorkType_Type()
)
icSheetWorkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSheetWorkType.setStatus("current")
_IcSheetPersistence_Type = IcPersistenceTC
_IcSheetPersistence_Object = MibTableColumn
icSheetPersistence = _IcSheetPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 3),
    _IcSheetPersistence_Type()
)
icSheetPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSheetPersistence.setStatus("current")


class _IcSheetTotalSheets_Type(IcCounter32):
    """Custom type icSheetTotalSheets based on IcCounter32"""
    defaultValue = 0


_IcSheetTotalSheets_Object = MibTableColumn
icSheetTotalSheets = _IcSheetTotalSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 4),
    _IcSheetTotalSheets_Type()
)
icSheetTotalSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSheetTotalSheets.setStatus("current")
if mibBuilder.loadTexts:
    icSheetTotalSheets.setUnits("sheets")


class _IcSheetMonochromeSheets_Type(IcCounter32):
    """Custom type icSheetMonochromeSheets based on IcCounter32"""
    defaultValue = 0


_IcSheetMonochromeSheets_Object = MibTableColumn
icSheetMonochromeSheets = _IcSheetMonochromeSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 5),
    _IcSheetMonochromeSheets_Type()
)
icSheetMonochromeSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSheetMonochromeSheets.setStatus("current")
if mibBuilder.loadTexts:
    icSheetMonochromeSheets.setUnits("sheets")


class _IcSheetBlankSheets_Type(IcCounter32):
    """Custom type icSheetBlankSheets based on IcCounter32"""
    defaultValue = 0


_IcSheetBlankSheets_Object = MibTableColumn
icSheetBlankSheets = _IcSheetBlankSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 6),
    _IcSheetBlankSheets_Type()
)
icSheetBlankSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSheetBlankSheets.setStatus("current")
if mibBuilder.loadTexts:
    icSheetBlankSheets.setUnits("sheets")


class _IcSheetFullColorSheets_Type(IcCounter32):
    """Custom type icSheetFullColorSheets based on IcCounter32"""
    defaultValue = 0


_IcSheetFullColorSheets_Object = MibTableColumn
icSheetFullColorSheets = _IcSheetFullColorSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 7),
    _IcSheetFullColorSheets_Type()
)
icSheetFullColorSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSheetFullColorSheets.setStatus("current")
if mibBuilder.loadTexts:
    icSheetFullColorSheets.setUnits("sheets")


class _IcSheetHighlightColorSheets_Type(IcCounter32):
    """Custom type icSheetHighlightColorSheets based on IcCounter32"""
    defaultValue = 0


_IcSheetHighlightColorSheets_Object = MibTableColumn
icSheetHighlightColorSheets = _IcSheetHighlightColorSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 10, 1, 1, 8),
    _IcSheetHighlightColorSheets_Type()
)
icSheetHighlightColorSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSheetHighlightColorSheets.setStatus("current")
if mibBuilder.loadTexts:
    icSheetHighlightColorSheets.setUnits("sheets")
_IcTraffic_ObjectIdentity = ObjectIdentity
icTraffic = _IcTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11)
)
_IcTrafficTable_Object = MibTable
icTrafficTable = _IcTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1)
)
if mibBuilder.loadTexts:
    icTrafficTable.setStatus("current")
_IcTrafficEntry_Object = MibTableRow
icTrafficEntry = _IcTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1)
)
icTrafficEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icTrafficKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icTrafficWorkType"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icTrafficPersistence"),
)
if mibBuilder.loadTexts:
    icTrafficEntry.setStatus("current")


class _IcTrafficKeyIndex_Type(Integer32):
    """Custom type icTrafficKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcTrafficKeyIndex_Type.__name__ = "Integer32"
_IcTrafficKeyIndex_Object = MibTableColumn
icTrafficKeyIndex = _IcTrafficKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 1),
    _IcTrafficKeyIndex_Type()
)
icTrafficKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTrafficKeyIndex.setStatus("current")
_IcTrafficWorkType_Type = IcWorkTypeTC
_IcTrafficWorkType_Object = MibTableColumn
icTrafficWorkType = _IcTrafficWorkType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 2),
    _IcTrafficWorkType_Type()
)
icTrafficWorkType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTrafficWorkType.setStatus("current")
_IcTrafficPersistence_Type = IcPersistenceTC
_IcTrafficPersistence_Object = MibTableColumn
icTrafficPersistence = _IcTrafficPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 3),
    _IcTrafficPersistence_Type()
)
icTrafficPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icTrafficPersistence.setStatus("current")


class _IcTrafficInputKOctets_Type(IcCounter32):
    """Custom type icTrafficInputKOctets based on IcCounter32"""
    defaultValue = 0


_IcTrafficInputKOctets_Object = MibTableColumn
icTrafficInputKOctets = _IcTrafficInputKOctets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 4),
    _IcTrafficInputKOctets_Type()
)
icTrafficInputKOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTrafficInputKOctets.setStatus("current")
if mibBuilder.loadTexts:
    icTrafficInputKOctets.setUnits("koctets")


class _IcTrafficOutputKOctets_Type(IcCounter32):
    """Custom type icTrafficOutputKOctets based on IcCounter32"""
    defaultValue = 0


_IcTrafficOutputKOctets_Object = MibTableColumn
icTrafficOutputKOctets = _IcTrafficOutputKOctets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 5),
    _IcTrafficOutputKOctets_Type()
)
icTrafficOutputKOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTrafficOutputKOctets.setStatus("current")
if mibBuilder.loadTexts:
    icTrafficOutputKOctets.setUnits("koctets")


class _IcTrafficInputMessages_Type(IcCounter32):
    """Custom type icTrafficInputMessages based on IcCounter32"""
    defaultValue = 0


_IcTrafficInputMessages_Object = MibTableColumn
icTrafficInputMessages = _IcTrafficInputMessages_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 6),
    _IcTrafficInputMessages_Type()
)
icTrafficInputMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTrafficInputMessages.setStatus("current")
if mibBuilder.loadTexts:
    icTrafficInputMessages.setUnits("messages")


class _IcTrafficOutputMessages_Type(IcCounter32):
    """Custom type icTrafficOutputMessages based on IcCounter32"""
    defaultValue = 0


_IcTrafficOutputMessages_Object = MibTableColumn
icTrafficOutputMessages = _IcTrafficOutputMessages_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 11, 1, 1, 7),
    _IcTrafficOutputMessages_Type()
)
icTrafficOutputMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icTrafficOutputMessages.setStatus("current")
if mibBuilder.loadTexts:
    icTrafficOutputMessages.setUnits("messages")
_IcMediaUsed_ObjectIdentity = ObjectIdentity
icMediaUsed = _IcMediaUsed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12)
)
_IcMediaUsedTable_Object = MibTable
icMediaUsedTable = _IcMediaUsedTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1)
)
if mibBuilder.loadTexts:
    icMediaUsedTable.setStatus("current")
_IcMediaUsedEntry_Object = MibTableRow
icMediaUsedEntry = _IcMediaUsedEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1)
)
icMediaUsedEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icMediaUsedKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icMediaUsedIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icMediaUsedPersistence"),
)
if mibBuilder.loadTexts:
    icMediaUsedEntry.setStatus("current")


class _IcMediaUsedKeyIndex_Type(Integer32):
    """Custom type icMediaUsedKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcMediaUsedKeyIndex_Type.__name__ = "Integer32"
_IcMediaUsedKeyIndex_Object = MibTableColumn
icMediaUsedKeyIndex = _IcMediaUsedKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 1),
    _IcMediaUsedKeyIndex_Type()
)
icMediaUsedKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icMediaUsedKeyIndex.setStatus("current")


class _IcMediaUsedIndex_Type(Integer32):
    """Custom type icMediaUsedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcMediaUsedIndex_Type.__name__ = "Integer32"
_IcMediaUsedIndex_Object = MibTableColumn
icMediaUsedIndex = _IcMediaUsedIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 2),
    _IcMediaUsedIndex_Type()
)
icMediaUsedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icMediaUsedIndex.setStatus("current")
_IcMediaUsedPersistence_Type = IcPersistenceTC
_IcMediaUsedPersistence_Object = MibTableColumn
icMediaUsedPersistence = _IcMediaUsedPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 3),
    _IcMediaUsedPersistence_Type()
)
icMediaUsedPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icMediaUsedPersistence.setStatus("current")


class _IcMediaUsedTotalSheets_Type(IcCounter32):
    """Custom type icMediaUsedTotalSheets based on IcCounter32"""
    defaultValue = 0


_IcMediaUsedTotalSheets_Object = MibTableColumn
icMediaUsedTotalSheets = _IcMediaUsedTotalSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 4),
    _IcMediaUsedTotalSheets_Type()
)
icMediaUsedTotalSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedTotalSheets.setStatus("current")
if mibBuilder.loadTexts:
    icMediaUsedTotalSheets.setUnits("sheets")


class _IcMediaUsedMonochromeSheets_Type(IcCounter32):
    """Custom type icMediaUsedMonochromeSheets based on IcCounter32"""
    defaultValue = 0


_IcMediaUsedMonochromeSheets_Object = MibTableColumn
icMediaUsedMonochromeSheets = _IcMediaUsedMonochromeSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 5),
    _IcMediaUsedMonochromeSheets_Type()
)
icMediaUsedMonochromeSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedMonochromeSheets.setStatus("current")
if mibBuilder.loadTexts:
    icMediaUsedMonochromeSheets.setUnits("sheets")


class _IcMediaUsedBlankSheets_Type(IcCounter32):
    """Custom type icMediaUsedBlankSheets based on IcCounter32"""
    defaultValue = 0


_IcMediaUsedBlankSheets_Object = MibTableColumn
icMediaUsedBlankSheets = _IcMediaUsedBlankSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 6),
    _IcMediaUsedBlankSheets_Type()
)
icMediaUsedBlankSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedBlankSheets.setStatus("current")
if mibBuilder.loadTexts:
    icMediaUsedBlankSheets.setUnits("sheets")


class _IcMediaUsedFullColorSheets_Type(IcCounter32):
    """Custom type icMediaUsedFullColorSheets based on IcCounter32"""
    defaultValue = 0


_IcMediaUsedFullColorSheets_Object = MibTableColumn
icMediaUsedFullColorSheets = _IcMediaUsedFullColorSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 7),
    _IcMediaUsedFullColorSheets_Type()
)
icMediaUsedFullColorSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedFullColorSheets.setStatus("current")
if mibBuilder.loadTexts:
    icMediaUsedFullColorSheets.setUnits("sheets")


class _IcMediaUsedHighlightColorSheets_Type(IcCounter32):
    """Custom type icMediaUsedHighlightColorSheets based on IcCounter32"""
    defaultValue = 0


_IcMediaUsedHighlightColorSheets_Object = MibTableColumn
icMediaUsedHighlightColorSheets = _IcMediaUsedHighlightColorSheets_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 8),
    _IcMediaUsedHighlightColorSheets_Type()
)
icMediaUsedHighlightColorSheets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedHighlightColorSheets.setStatus("current")
if mibBuilder.loadTexts:
    icMediaUsedHighlightColorSheets.setUnits("sheets")


class _IcMediaUsedMediaSizeName_Type(DisplayString):
    """Custom type icMediaUsedMediaSizeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcMediaUsedMediaSizeName_Type.__name__ = "DisplayString"
_IcMediaUsedMediaSizeName_Object = MibTableColumn
icMediaUsedMediaSizeName = _IcMediaUsedMediaSizeName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 9),
    _IcMediaUsedMediaSizeName_Type()
)
icMediaUsedMediaSizeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedMediaSizeName.setStatus("current")


class _IcMediaUsedMediaInfo_Type(SnmpAdminString):
    """Custom type icMediaUsedMediaInfo based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcMediaUsedMediaInfo_Type.__name__ = "SnmpAdminString"
_IcMediaUsedMediaInfo_Object = MibTableColumn
icMediaUsedMediaInfo = _IcMediaUsedMediaInfo_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 10),
    _IcMediaUsedMediaInfo_Type()
)
icMediaUsedMediaInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedMediaInfo.setStatus("current")


class _IcMediaUsedMediaName_Type(SnmpAdminString):
    """Custom type icMediaUsedMediaName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcMediaUsedMediaName_Type.__name__ = "SnmpAdminString"
_IcMediaUsedMediaName_Object = MibTableColumn
icMediaUsedMediaName = _IcMediaUsedMediaName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 11),
    _IcMediaUsedMediaName_Type()
)
icMediaUsedMediaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedMediaName.setStatus("current")


class _IcMediaUsedMediaAccountingKey_Type(DisplayString):
    """Custom type icMediaUsedMediaAccountingKey based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IcMediaUsedMediaAccountingKey_Type.__name__ = "DisplayString"
_IcMediaUsedMediaAccountingKey_Object = MibTableColumn
icMediaUsedMediaAccountingKey = _IcMediaUsedMediaAccountingKey_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 12, 1, 1, 12),
    _IcMediaUsedMediaAccountingKey_Type()
)
icMediaUsedMediaAccountingKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icMediaUsedMediaAccountingKey.setStatus("current")
_IcAlert_ObjectIdentity = ObjectIdentity
icAlert = _IcAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13)
)
_IcAlertTable_Object = MibTable
icAlertTable = _IcAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1)
)
if mibBuilder.loadTexts:
    icAlertTable.setStatus("current")
_IcAlertEntry_Object = MibTableRow
icAlertEntry = _IcAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1)
)
icAlertEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icAlertKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icAlertIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icAlertPersistence"),
)
if mibBuilder.loadTexts:
    icAlertEntry.setStatus("current")


class _IcAlertKeyIndex_Type(Integer32):
    """Custom type icAlertKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcAlertKeyIndex_Type.__name__ = "Integer32"
_IcAlertKeyIndex_Object = MibTableColumn
icAlertKeyIndex = _IcAlertKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 1),
    _IcAlertKeyIndex_Type()
)
icAlertKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icAlertKeyIndex.setStatus("current")


class _IcAlertIndex_Type(Integer32):
    """Custom type icAlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcAlertIndex_Type.__name__ = "Integer32"
_IcAlertIndex_Object = MibTableColumn
icAlertIndex = _IcAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 2),
    _IcAlertIndex_Type()
)
icAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icAlertIndex.setStatus("current")
_IcAlertPersistence_Type = IcPersistenceTC
_IcAlertPersistence_Object = MibTableColumn
icAlertPersistence = _IcAlertPersistence_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 3),
    _IcAlertPersistence_Type()
)
icAlertPersistence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icAlertPersistence.setStatus("current")
_IcAlertCounterEventType_Type = IcCounterEventTypeTC
_IcAlertCounterEventType_Object = MibTableColumn
icAlertCounterEventType = _IcAlertCounterEventType_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 4),
    _IcAlertCounterEventType_Type()
)
icAlertCounterEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icAlertCounterEventType.setStatus("current")


class _IcAlertCounterName_Type(DisplayString):
    """Custom type icAlertCounterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_IcAlertCounterName_Type.__name__ = "DisplayString"
_IcAlertCounterName_Object = MibTableColumn
icAlertCounterName = _IcAlertCounterName_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 5),
    _IcAlertCounterName_Type()
)
icAlertCounterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icAlertCounterName.setStatus("current")
_IcAlertCounterValue_Type = IcCounter32
_IcAlertCounterValue_Object = MibTableColumn
icAlertCounterValue = _IcAlertCounterValue_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 6),
    _IcAlertCounterValue_Type()
)
icAlertCounterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icAlertCounterValue.setStatus("current")
_IcAlertDateAndTime_Type = DateAndTime
_IcAlertDateAndTime_Object = MibTableColumn
icAlertDateAndTime = _IcAlertDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 7),
    _IcAlertDateAndTime_Type()
)
icAlertDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icAlertDateAndTime.setStatus("current")
_IcAlertTimeStamp_Type = TimeStamp
_IcAlertTimeStamp_Object = MibTableColumn
icAlertTimeStamp = _IcAlertTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 13, 1, 1, 8),
    _IcAlertTimeStamp_Type()
)
icAlertTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icAlertTimeStamp.setStatus("current")
_IcSubunitMap_ObjectIdentity = ObjectIdentity
icSubunitMap = _IcSubunitMap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 14)
)
_IcSubunitMapTable_Object = MibTable
icSubunitMapTable = _IcSubunitMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 14, 1)
)
if mibBuilder.loadTexts:
    icSubunitMapTable.setStatus("current")
_IcSubunitMapEntry_Object = MibTableRow
icSubunitMapEntry = _IcSubunitMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 14, 1, 1)
)
icSubunitMapEntry.setIndexNames(
    (0, "PWG-IMAGING-COUNTER-MIB", "icSubunitMapServiceKeyIndex"),
    (0, "PWG-IMAGING-COUNTER-MIB", "icSubunitMapSubunitKeyIndex"),
)
if mibBuilder.loadTexts:
    icSubunitMapEntry.setStatus("current")


class _IcSubunitMapServiceKeyIndex_Type(Integer32):
    """Custom type icSubunitMapServiceKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcSubunitMapServiceKeyIndex_Type.__name__ = "Integer32"
_IcSubunitMapServiceKeyIndex_Object = MibTableColumn
icSubunitMapServiceKeyIndex = _IcSubunitMapServiceKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 14, 1, 1, 1),
    _IcSubunitMapServiceKeyIndex_Type()
)
icSubunitMapServiceKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSubunitMapServiceKeyIndex.setStatus("current")


class _IcSubunitMapSubunitKeyIndex_Type(Integer32):
    """Custom type icSubunitMapSubunitKeyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IcSubunitMapSubunitKeyIndex_Type.__name__ = "Integer32"
_IcSubunitMapSubunitKeyIndex_Object = MibTableColumn
icSubunitMapSubunitKeyIndex = _IcSubunitMapSubunitKeyIndex_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 14, 1, 1, 2),
    _IcSubunitMapSubunitKeyIndex_Type()
)
icSubunitMapSubunitKeyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    icSubunitMapSubunitKeyIndex.setStatus("current")


class _IcSubunitMapSubunitEnabled_Type(TruthValue):
    """Custom type icSubunitMapSubunitEnabled based on TruthValue"""


_IcSubunitMapSubunitEnabled_Object = MibTableColumn
icSubunitMapSubunitEnabled = _IcSubunitMapSubunitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 1, 14, 1, 1, 3),
    _IcSubunitMapSubunitEnabled_Type()
)
icSubunitMapSubunitEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    icSubunitMapSubunitEnabled.setStatus("current")
_IcMIBConformance_ObjectIdentity = ObjectIdentity
icMIBConformance = _IcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2)
)
_IcMIBObjectGroups_ObjectIdentity = ObjectIdentity
icMIBObjectGroups = _IcMIBObjectGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2)
)
_IcMIBNotificationGroups_ObjectIdentity = ObjectIdentity
icMIBNotificationGroups = _IcMIBNotificationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 3)
)

# Managed Objects groups

icGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 1)
)
icGeneralGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icGeneralNaturalLanguage"),
        ("PWG-IMAGING-COUNTER-MIB", "icGeneralTotalServiceRecords"),
        ("PWG-IMAGING-COUNTER-MIB", "icGeneralTotalSubunitRecords"),
        ("PWG-IMAGING-COUNTER-MIB", "icGeneralTotalMediaUsedRecords"))
)
if mibBuilder.loadTexts:
    icGeneralGroup.setStatus("current")

icKeyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 2)
)
icKeyGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icKeyServiceType"),
        ("PWG-IMAGING-COUNTER-MIB", "icKeyServiceIndex"),
        ("PWG-IMAGING-COUNTER-MIB", "icKeySubunitType"),
        ("PWG-IMAGING-COUNTER-MIB", "icKeySubunitIndex"))
)
if mibBuilder.loadTexts:
    icKeyGroup.setStatus("current")

icServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 3)
)
icServiceGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icServiceKey"),
        ("PWG-IMAGING-COUNTER-MIB", "icServiceInfo"),
        ("PWG-IMAGING-COUNTER-MIB", "icServiceJobSetIndex"))
)
if mibBuilder.loadTexts:
    icServiceGroup.setStatus("current")

icSubunitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 4)
)
icSubunitGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icSubunitKey"),
        ("PWG-IMAGING-COUNTER-MIB", "icSubunitInfo"))
)
if mibBuilder.loadTexts:
    icSubunitGroup.setStatus("current")

icTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 5)
)
icTimeGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icTimeTotalSeconds"),
        ("PWG-IMAGING-COUNTER-MIB", "icTimeDownSeconds"),
        ("PWG-IMAGING-COUNTER-MIB", "icTimeMaintenanceSeconds"),
        ("PWG-IMAGING-COUNTER-MIB", "icTimeProcessingSeconds"))
)
if mibBuilder.loadTexts:
    icTimeGroup.setStatus("current")

icMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 6)
)
icMonitorGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icMonitorConfigChanges"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorTotalAlerts"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorCriticalAlerts"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorAbortedJobs"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorCanceledJobs"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorCompletedJobs"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorCompletedFinisherJobs"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorMemoryAllocErrors"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorMemoryAllocWarnings"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorStorageAllocErrors"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorStorageAllocWarnings"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorLocalStorageKOctets"),
        ("PWG-IMAGING-COUNTER-MIB", "icMonitorRemoteStorageKOctets"))
)
if mibBuilder.loadTexts:
    icMonitorGroup.setStatus("current")

icImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 7)
)
icImageGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icImageTotalImages"),
        ("PWG-IMAGING-COUNTER-MIB", "icImageMonochromeImages"),
        ("PWG-IMAGING-COUNTER-MIB", "icImageFullColorImages"))
)
if mibBuilder.loadTexts:
    icImageGroup.setStatus("current")

icImpressionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 8)
)
icImpressionGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icImpressionTotalImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icImpressionMonochromeImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icImpressionBlankImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icImpressionFullColorImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icImpressionHighlightColorImps"))
)
if mibBuilder.loadTexts:
    icImpressionGroup.setStatus("current")

icTwoSidedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 9)
)
icTwoSidedGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icTwoSidedTotalImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icTwoSidedMonochromeImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icTwoSidedBlankImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icTwoSidedFullColorImps"),
        ("PWG-IMAGING-COUNTER-MIB", "icTwoSidedHighlightColorImps"))
)
if mibBuilder.loadTexts:
    icTwoSidedGroup.setStatus("current")

icSheetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 10)
)
icSheetGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icSheetTotalSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icSheetMonochromeSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icSheetBlankSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icSheetFullColorSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icSheetHighlightColorSheets"))
)
if mibBuilder.loadTexts:
    icSheetGroup.setStatus("current")

icTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 11)
)
icTrafficGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icTrafficInputKOctets"),
        ("PWG-IMAGING-COUNTER-MIB", "icTrafficOutputKOctets"),
        ("PWG-IMAGING-COUNTER-MIB", "icTrafficInputMessages"),
        ("PWG-IMAGING-COUNTER-MIB", "icTrafficOutputMessages"))
)
if mibBuilder.loadTexts:
    icTrafficGroup.setStatus("current")

icMediaUsedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 12)
)
icMediaUsedGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icMediaUsedTotalSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedMonochromeSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedBlankSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedFullColorSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedHighlightColorSheets"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedMediaSizeName"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedMediaInfo"),
        ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedMediaName"))
)
if mibBuilder.loadTexts:
    icMediaUsedGroup.setStatus("current")

icAlertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 13)
)
icAlertGroup.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icAlertCounterEventType"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertCounterName"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertCounterValue"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertDateAndTime"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertTimeStamp"))
)
if mibBuilder.loadTexts:
    icAlertGroup.setStatus("current")

icSubunitMapV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 14)
)
icSubunitMapV2Group.setObjects(
    ("PWG-IMAGING-COUNTER-MIB", "icSubunitMapSubunitEnabled")
)
if mibBuilder.loadTexts:
    icSubunitMapV2Group.setStatus("current")

icServiceV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 15)
)
icServiceV2Group.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icServiceState"),
        ("PWG-IMAGING-COUNTER-MIB", "icServiceStateMessage"),
        ("PWG-IMAGING-COUNTER-MIB", "icServicePrtAlertIndex"))
)
if mibBuilder.loadTexts:
    icServiceV2Group.setStatus("current")

icSubunitV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 16)
)
icSubunitV2Group.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icSubunitStatus"),
        ("PWG-IMAGING-COUNTER-MIB", "icSubunitStatusMessage"))
)
if mibBuilder.loadTexts:
    icSubunitV2Group.setStatus("current")

icMediaUsedV2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 2, 17)
)
icMediaUsedV2Group.setObjects(
    ("PWG-IMAGING-COUNTER-MIB", "icMediaUsedMediaAccountingKey")
)
if mibBuilder.loadTexts:
    icMediaUsedV2Group.setStatus("current")


# Notification objects

icAlertV2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 0, 1)
)
icAlertV2Trap.setObjects(
      *(("PWG-IMAGING-COUNTER-MIB", "icAlertCounterEventType"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertCounterName"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertCounterValue"),
        ("PWG-IMAGING-COUNTER-MIB", "icAlertDateAndTime"))
)
if mibBuilder.loadTexts:
    icAlertV2Trap.setStatus(
        "current"
    )


# Notifications groups

icAlertTrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 3, 1)
)
icAlertTrapGroup.setObjects(
    ("PWG-IMAGING-COUNTER-MIB", "icAlertV2Trap")
)
if mibBuilder.loadTexts:
    icAlertTrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

icMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    icMIBCompliance.setStatus(
        "current"
    )

icMIBStateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2699, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    icMIBStateCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PWG-IMAGING-COUNTER-MIB",
    **{"IcCounter32": IcCounter32,
       "IcCounterEventTypeTC": IcCounterEventTypeTC,
       "IcPersistenceTC": IcPersistenceTC,
       "IcServiceStateTC": IcServiceStateTC,
       "IcServiceTypeTC": IcServiceTypeTC,
       "IcSubunitStatusTC": IcSubunitStatusTC,
       "IcSubunitTypeTC": IcSubunitTypeTC,
       "IcWorkTypeTC": IcWorkTypeTC,
       "imagingCounterMIB": imagingCounterMIB,
       "icMIBNotifications": icMIBNotifications,
       "icAlertV2Trap": icAlertV2Trap,
       "icMIBObjects": icMIBObjects,
       "icGeneral": icGeneral,
       "icGeneralNaturalLanguage": icGeneralNaturalLanguage,
       "icGeneralTotalServiceRecords": icGeneralTotalServiceRecords,
       "icGeneralTotalSubunitRecords": icGeneralTotalSubunitRecords,
       "icGeneralTotalMediaUsedRecords": icGeneralTotalMediaUsedRecords,
       "icKey": icKey,
       "icKeyTable": icKeyTable,
       "icKeyEntry": icKeyEntry,
       "icKeyIndex": icKeyIndex,
       "icKeyServiceType": icKeyServiceType,
       "icKeyServiceIndex": icKeyServiceIndex,
       "icKeySubunitType": icKeySubunitType,
       "icKeySubunitIndex": icKeySubunitIndex,
       "icService": icService,
       "icServiceTable": icServiceTable,
       "icServiceEntry": icServiceEntry,
       "icServiceType": icServiceType,
       "icServiceIndex": icServiceIndex,
       "icServiceKey": icServiceKey,
       "icServiceInfo": icServiceInfo,
       "icServiceJobSetIndex": icServiceJobSetIndex,
       "icServiceState": icServiceState,
       "icServiceStateMessage": icServiceStateMessage,
       "icServicePrtAlertIndex": icServicePrtAlertIndex,
       "icSubunit": icSubunit,
       "icSubunitTable": icSubunitTable,
       "icSubunitEntry": icSubunitEntry,
       "icSubunitType": icSubunitType,
       "icSubunitIndex": icSubunitIndex,
       "icSubunitKey": icSubunitKey,
       "icSubunitInfo": icSubunitInfo,
       "icSubunitStatus": icSubunitStatus,
       "icSubunitStatusMessage": icSubunitStatusMessage,
       "icTime": icTime,
       "icTimeTable": icTimeTable,
       "icTimeEntry": icTimeEntry,
       "icTimeKeyIndex": icTimeKeyIndex,
       "icTimePersistence": icTimePersistence,
       "icTimeTotalSeconds": icTimeTotalSeconds,
       "icTimeDownSeconds": icTimeDownSeconds,
       "icTimeMaintenanceSeconds": icTimeMaintenanceSeconds,
       "icTimeProcessingSeconds": icTimeProcessingSeconds,
       "icMonitor": icMonitor,
       "icMonitorTable": icMonitorTable,
       "icMonitorEntry": icMonitorEntry,
       "icMonitorKeyIndex": icMonitorKeyIndex,
       "icMonitorPersistence": icMonitorPersistence,
       "icMonitorConfigChanges": icMonitorConfigChanges,
       "icMonitorTotalAlerts": icMonitorTotalAlerts,
       "icMonitorCriticalAlerts": icMonitorCriticalAlerts,
       "icMonitorAbortedJobs": icMonitorAbortedJobs,
       "icMonitorCanceledJobs": icMonitorCanceledJobs,
       "icMonitorCompletedJobs": icMonitorCompletedJobs,
       "icMonitorCompletedFinisherJobs": icMonitorCompletedFinisherJobs,
       "icMonitorMemoryAllocErrors": icMonitorMemoryAllocErrors,
       "icMonitorMemoryAllocWarnings": icMonitorMemoryAllocWarnings,
       "icMonitorStorageAllocErrors": icMonitorStorageAllocErrors,
       "icMonitorStorageAllocWarnings": icMonitorStorageAllocWarnings,
       "icMonitorLocalStorageKOctets": icMonitorLocalStorageKOctets,
       "icMonitorRemoteStorageKOctets": icMonitorRemoteStorageKOctets,
       "icImage": icImage,
       "icImageTable": icImageTable,
       "icImageEntry": icImageEntry,
       "icImageKeyIndex": icImageKeyIndex,
       "icImageWorkType": icImageWorkType,
       "icImagePersistence": icImagePersistence,
       "icImageTotalImages": icImageTotalImages,
       "icImageMonochromeImages": icImageMonochromeImages,
       "icImageFullColorImages": icImageFullColorImages,
       "icImpression": icImpression,
       "icImpressionTable": icImpressionTable,
       "icImpressionEntry": icImpressionEntry,
       "icImpressionKeyIndex": icImpressionKeyIndex,
       "icImpressionWorkType": icImpressionWorkType,
       "icImpressionPersistence": icImpressionPersistence,
       "icImpressionTotalImps": icImpressionTotalImps,
       "icImpressionMonochromeImps": icImpressionMonochromeImps,
       "icImpressionBlankImps": icImpressionBlankImps,
       "icImpressionFullColorImps": icImpressionFullColorImps,
       "icImpressionHighlightColorImps": icImpressionHighlightColorImps,
       "icTwoSided": icTwoSided,
       "icTwoSidedTable": icTwoSidedTable,
       "icTwoSidedEntry": icTwoSidedEntry,
       "icTwoSidedKeyIndex": icTwoSidedKeyIndex,
       "icTwoSidedWorkType": icTwoSidedWorkType,
       "icTwoSidedPersistence": icTwoSidedPersistence,
       "icTwoSidedTotalImps": icTwoSidedTotalImps,
       "icTwoSidedMonochromeImps": icTwoSidedMonochromeImps,
       "icTwoSidedBlankImps": icTwoSidedBlankImps,
       "icTwoSidedFullColorImps": icTwoSidedFullColorImps,
       "icTwoSidedHighlightColorImps": icTwoSidedHighlightColorImps,
       "icSheet": icSheet,
       "icSheetTable": icSheetTable,
       "icSheetEntry": icSheetEntry,
       "icSheetKeyIndex": icSheetKeyIndex,
       "icSheetWorkType": icSheetWorkType,
       "icSheetPersistence": icSheetPersistence,
       "icSheetTotalSheets": icSheetTotalSheets,
       "icSheetMonochromeSheets": icSheetMonochromeSheets,
       "icSheetBlankSheets": icSheetBlankSheets,
       "icSheetFullColorSheets": icSheetFullColorSheets,
       "icSheetHighlightColorSheets": icSheetHighlightColorSheets,
       "icTraffic": icTraffic,
       "icTrafficTable": icTrafficTable,
       "icTrafficEntry": icTrafficEntry,
       "icTrafficKeyIndex": icTrafficKeyIndex,
       "icTrafficWorkType": icTrafficWorkType,
       "icTrafficPersistence": icTrafficPersistence,
       "icTrafficInputKOctets": icTrafficInputKOctets,
       "icTrafficOutputKOctets": icTrafficOutputKOctets,
       "icTrafficInputMessages": icTrafficInputMessages,
       "icTrafficOutputMessages": icTrafficOutputMessages,
       "icMediaUsed": icMediaUsed,
       "icMediaUsedTable": icMediaUsedTable,
       "icMediaUsedEntry": icMediaUsedEntry,
       "icMediaUsedKeyIndex": icMediaUsedKeyIndex,
       "icMediaUsedIndex": icMediaUsedIndex,
       "icMediaUsedPersistence": icMediaUsedPersistence,
       "icMediaUsedTotalSheets": icMediaUsedTotalSheets,
       "icMediaUsedMonochromeSheets": icMediaUsedMonochromeSheets,
       "icMediaUsedBlankSheets": icMediaUsedBlankSheets,
       "icMediaUsedFullColorSheets": icMediaUsedFullColorSheets,
       "icMediaUsedHighlightColorSheets": icMediaUsedHighlightColorSheets,
       "icMediaUsedMediaSizeName": icMediaUsedMediaSizeName,
       "icMediaUsedMediaInfo": icMediaUsedMediaInfo,
       "icMediaUsedMediaName": icMediaUsedMediaName,
       "icMediaUsedMediaAccountingKey": icMediaUsedMediaAccountingKey,
       "icAlert": icAlert,
       "icAlertTable": icAlertTable,
       "icAlertEntry": icAlertEntry,
       "icAlertKeyIndex": icAlertKeyIndex,
       "icAlertIndex": icAlertIndex,
       "icAlertPersistence": icAlertPersistence,
       "icAlertCounterEventType": icAlertCounterEventType,
       "icAlertCounterName": icAlertCounterName,
       "icAlertCounterValue": icAlertCounterValue,
       "icAlertDateAndTime": icAlertDateAndTime,
       "icAlertTimeStamp": icAlertTimeStamp,
       "icSubunitMap": icSubunitMap,
       "icSubunitMapTable": icSubunitMapTable,
       "icSubunitMapEntry": icSubunitMapEntry,
       "icSubunitMapServiceKeyIndex": icSubunitMapServiceKeyIndex,
       "icSubunitMapSubunitKeyIndex": icSubunitMapSubunitKeyIndex,
       "icSubunitMapSubunitEnabled": icSubunitMapSubunitEnabled,
       "icMIBConformance": icMIBConformance,
       "icMIBCompliance": icMIBCompliance,
       "icMIBObjectGroups": icMIBObjectGroups,
       "icGeneralGroup": icGeneralGroup,
       "icKeyGroup": icKeyGroup,
       "icServiceGroup": icServiceGroup,
       "icSubunitGroup": icSubunitGroup,
       "icTimeGroup": icTimeGroup,
       "icMonitorGroup": icMonitorGroup,
       "icImageGroup": icImageGroup,
       "icImpressionGroup": icImpressionGroup,
       "icTwoSidedGroup": icTwoSidedGroup,
       "icSheetGroup": icSheetGroup,
       "icTrafficGroup": icTrafficGroup,
       "icMediaUsedGroup": icMediaUsedGroup,
       "icAlertGroup": icAlertGroup,
       "icSubunitMapV2Group": icSubunitMapV2Group,
       "icServiceV2Group": icServiceV2Group,
       "icSubunitV2Group": icSubunitV2Group,
       "icMediaUsedV2Group": icMediaUsedV2Group,
       "icMIBNotificationGroups": icMIBNotificationGroups,
       "icAlertTrapGroup": icAlertTrapGroup,
       "icMIBStateCompliance": icMIBStateCompliance}
)
