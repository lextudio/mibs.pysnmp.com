# SNMP MIB module (CISCO-RHINO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-RHINO-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:07:36 2024
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

(workgroup,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "workgroup")

(Unsigned32,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Unsigned32")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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

ciscoLS1010ChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11)
)
ciscoLS1010ChassisMIB.setRevisions(
        ("2001-03-29 00:00",
         "2001-02-15 00:00",
         "2000-07-20 00:00",
         "2000-04-11 00:00",
         "2000-02-07 00:00",
         "1999-11-30 00:00",
         "1999-10-04 00:00",
         "1999-06-29 00:00",
         "1999-06-17 00:00",
         "1999-03-12 00:00",
         "1998-12-02 00:00",
         "1998-10-26 00:00",
         "1998-07-13 00:00",
         "1997-11-20 00:00",
         "1997-07-22 00:00",
         "1997-02-04 00:00",
         "1996-10-02 00:00",
         "1995-10-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PsType(Integer32, TextualConvention):
    status = "current"
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("ac1100W", 4),
          ("ac1200W", 5),
          ("ac1360W", 8),
          ("ac175W", 13),
          ("ac2000W", 10),
          ("acpem", 12),
          ("astec", 1),
          ("dc1200W", 6),
          ("dc1360W", 9),
          ("dc2000W", 11),
          ("empty", 3),
          ("minus48VDC", 2),
          ("pem", 7),
          ("powerone", 0))
    )



class OperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("empty", 6),
          ("fanAlarm", 4),
          ("fault", 3),
          ("ok", 2),
          ("partialFault", 5),
          ("unknown", 1))
    )



class AdminStatus(Integer32, TextualConvention):
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
        *(("disable", 2),
          ("enable", 1),
          ("reset", 3))
    )



class Led(Integer32, TextualConvention):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("blinkgreen", 5),
          ("blinkred", 7),
          ("blinkyellow", 6),
          ("green", 2),
          ("off", 1),
          ("red", 3),
          ("unknown", 8),
          ("yellow", 4))
    )



class PcmciaType(Integer32, TextualConvention):
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
        *(("disk", 4),
          ("empty", 2),
          ("flash", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoLS1010ChassisMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisMIBObjects = _CiscoLS1010ChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1)
)
_CiscoLS1010ChassisGroup_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisGroup = _CiscoLS1010ChassisGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1)
)


class _CiscoLS1010ChassisSysType_Type(Integer32):
    """Custom type ciscoLS1010ChassisSysType based on Integer32"""
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
        *(("c2948g", 8),
          ("c4908g", 9),
          ("c8510", 3),
          ("c8540", 5),
          ("cisco6400", 4),
          ("ls1010", 2),
          ("other", 1),
          ("tgx8750", 6),
          ("wsx6302", 7))
    )


_CiscoLS1010ChassisSysType_Type.__name__ = "Integer32"
_CiscoLS1010ChassisSysType_Object = MibScalar
ciscoLS1010ChassisSysType = _CiscoLS1010ChassisSysType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 1),
    _CiscoLS1010ChassisSysType_Type()
)
ciscoLS1010ChassisSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisSysType.setStatus("current")


class _CiscoLS1010ChassisBkplType_Type(Integer32):
    """Custom type ciscoLS1010ChassisBkplType based on Integer32"""
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
        *(("atm", 2),
          ("c2948g", 9),
          ("c4908g", 10),
          ("c5500", 3),
          ("c8510", 5),
          ("c8540", 6),
          ("cat6000", 8),
          ("cisco6400", 4),
          ("other", 1),
          ("tgx8750", 7))
    )


_CiscoLS1010ChassisBkplType_Type.__name__ = "Integer32"
_CiscoLS1010ChassisBkplType_Object = MibScalar
ciscoLS1010ChassisBkplType = _CiscoLS1010ChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 2),
    _CiscoLS1010ChassisBkplType_Type()
)
ciscoLS1010ChassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisBkplType.setStatus("current")
_CiscoLS1010ChassisPs0Type_Type = PsType
_CiscoLS1010ChassisPs0Type_Object = MibScalar
ciscoLS1010ChassisPs0Type = _CiscoLS1010ChassisPs0Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 3),
    _CiscoLS1010ChassisPs0Type_Type()
)
ciscoLS1010ChassisPs0Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs0Type.setStatus("current")
_CiscoLS1010ChassisPs0AdminStatus_Type = AdminStatus
_CiscoLS1010ChassisPs0AdminStatus_Object = MibScalar
ciscoLS1010ChassisPs0AdminStatus = _CiscoLS1010ChassisPs0AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 4),
    _CiscoLS1010ChassisPs0AdminStatus_Type()
)
ciscoLS1010ChassisPs0AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs0AdminStatus.setStatus("current")
_CiscoLS1010ChassisPs0Status_Type = OperStatus
_CiscoLS1010ChassisPs0Status_Object = MibScalar
ciscoLS1010ChassisPs0Status = _CiscoLS1010ChassisPs0Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 5),
    _CiscoLS1010ChassisPs0Status_Type()
)
ciscoLS1010ChassisPs0Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs0Status.setStatus("current")
_CiscoLS1010ChassisPs0Led_Type = Led
_CiscoLS1010ChassisPs0Led_Object = MibScalar
ciscoLS1010ChassisPs0Led = _CiscoLS1010ChassisPs0Led_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 6),
    _CiscoLS1010ChassisPs0Led_Type()
)
ciscoLS1010ChassisPs0Led.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs0Led.setStatus("current")
_CiscoLS1010ChassisPs1Type_Type = PsType
_CiscoLS1010ChassisPs1Type_Object = MibScalar
ciscoLS1010ChassisPs1Type = _CiscoLS1010ChassisPs1Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 7),
    _CiscoLS1010ChassisPs1Type_Type()
)
ciscoLS1010ChassisPs1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs1Type.setStatus("current")
_CiscoLS1010ChassisPs1AdminStatus_Type = AdminStatus
_CiscoLS1010ChassisPs1AdminStatus_Object = MibScalar
ciscoLS1010ChassisPs1AdminStatus = _CiscoLS1010ChassisPs1AdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 8),
    _CiscoLS1010ChassisPs1AdminStatus_Type()
)
ciscoLS1010ChassisPs1AdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs1AdminStatus.setStatus("current")
_CiscoLS1010ChassisPs1Status_Type = OperStatus
_CiscoLS1010ChassisPs1Status_Object = MibScalar
ciscoLS1010ChassisPs1Status = _CiscoLS1010ChassisPs1Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 9),
    _CiscoLS1010ChassisPs1Status_Type()
)
ciscoLS1010ChassisPs1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs1Status.setStatus("current")
_CiscoLS1010ChassisPs1Led_Type = Led
_CiscoLS1010ChassisPs1Led_Object = MibScalar
ciscoLS1010ChassisPs1Led = _CiscoLS1010ChassisPs1Led_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 10),
    _CiscoLS1010ChassisPs1Led_Type()
)
ciscoLS1010ChassisPs1Led.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPs1Led.setStatus("current")
_CiscoLS1010ChassisFanStatus_Type = OperStatus
_CiscoLS1010ChassisFanStatus_Object = MibScalar
ciscoLS1010ChassisFanStatus = _CiscoLS1010ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 11),
    _CiscoLS1010ChassisFanStatus_Type()
)
ciscoLS1010ChassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisFanStatus.setStatus("current")
_CiscoLS1010ChassisFanLed_Type = Led
_CiscoLS1010ChassisFanLed_Object = MibScalar
ciscoLS1010ChassisFanLed = _CiscoLS1010ChassisFanLed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 12),
    _CiscoLS1010ChassisFanLed_Type()
)
ciscoLS1010ChassisFanLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisFanLed.setStatus("current")
_CiscoLS1010ChassisCardStatusLed_Type = Led
_CiscoLS1010ChassisCardStatusLed_Object = MibScalar
ciscoLS1010ChassisCardStatusLed = _CiscoLS1010ChassisCardStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 13),
    _CiscoLS1010ChassisCardStatusLed_Type()
)
ciscoLS1010ChassisCardStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisCardStatusLed.setStatus("current")
_CiscoLS1010ChassisEnetLinkLed_Type = Led
_CiscoLS1010ChassisEnetLinkLed_Object = MibScalar
ciscoLS1010ChassisEnetLinkLed = _CiscoLS1010ChassisEnetLinkLed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 14),
    _CiscoLS1010ChassisEnetLinkLed_Type()
)
ciscoLS1010ChassisEnetLinkLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisEnetLinkLed.setStatus("current")


class _CiscoLS1010Chassis12VoltStatus_Type(Integer32):
    """Custom type ciscoLS1010Chassis12VoltStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("outOfTolerance", 2),
          ("unknown", 3))
    )


_CiscoLS1010Chassis12VoltStatus_Type.__name__ = "Integer32"
_CiscoLS1010Chassis12VoltStatus_Object = MibScalar
ciscoLS1010Chassis12VoltStatus = _CiscoLS1010Chassis12VoltStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 15),
    _CiscoLS1010Chassis12VoltStatus_Type()
)
ciscoLS1010Chassis12VoltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010Chassis12VoltStatus.setStatus("current")


class _CiscoLS1010ChassisTempStatus_Type(Integer32):
    """Custom type ciscoLS1010ChassisTempStatus based on Integer32"""
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
        *(("criticalWarning", 5),
          ("majorWarning", 4),
          ("minorWarning", 3),
          ("ok", 1),
          ("overTemperature", 2))
    )


_CiscoLS1010ChassisTempStatus_Type.__name__ = "Integer32"
_CiscoLS1010ChassisTempStatus_Object = MibScalar
ciscoLS1010ChassisTempStatus = _CiscoLS1010ChassisTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 16),
    _CiscoLS1010ChassisTempStatus_Type()
)
ciscoLS1010ChassisTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisTempStatus.setStatus("current")
_CiscoLS1010ChassisPcmciaSlot0Type_Type = PcmciaType
_CiscoLS1010ChassisPcmciaSlot0Type_Object = MibScalar
ciscoLS1010ChassisPcmciaSlot0Type = _CiscoLS1010ChassisPcmciaSlot0Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 17),
    _CiscoLS1010ChassisPcmciaSlot0Type_Type()
)
ciscoLS1010ChassisPcmciaSlot0Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPcmciaSlot0Type.setStatus("current")
_CiscoLS1010ChassisPcmciaSlot1Type_Type = PcmciaType
_CiscoLS1010ChassisPcmciaSlot1Type_Object = MibScalar
ciscoLS1010ChassisPcmciaSlot1Type = _CiscoLS1010ChassisPcmciaSlot1Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 18),
    _CiscoLS1010ChassisPcmciaSlot1Type_Type()
)
ciscoLS1010ChassisPcmciaSlot1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisPcmciaSlot1Type.setStatus("current")


class _CiscoLS1010ChassisNumSlots_Type(Integer32):
    """Custom type ciscoLS1010ChassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CiscoLS1010ChassisNumSlots_Type.__name__ = "Integer32"
_CiscoLS1010ChassisNumSlots_Object = MibScalar
ciscoLS1010ChassisNumSlots = _CiscoLS1010ChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 19),
    _CiscoLS1010ChassisNumSlots_Type()
)
ciscoLS1010ChassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisNumSlots.setStatus("current")
_CiscoLS1010ChassisLastChange_Type = TimeStamp
_CiscoLS1010ChassisLastChange_Object = MibScalar
ciscoLS1010ChassisLastChange = _CiscoLS1010ChassisLastChange_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 20),
    _CiscoLS1010ChassisLastChange_Type()
)
ciscoLS1010ChassisLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisLastChange.setStatus("current")


class _CiscoLS1010ChassisFailureAction_Type(Integer32):
    """Custom type ciscoLS1010ChassisFailureAction based on Integer32"""
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
        *(("nothing", 1),
          ("sendTrap", 2),
          ("sendTrapAndShutdown", 4),
          ("shutdown", 3))
    )


_CiscoLS1010ChassisFailureAction_Type.__name__ = "Integer32"
_CiscoLS1010ChassisFailureAction_Object = MibScalar
ciscoLS1010ChassisFailureAction = _CiscoLS1010ChassisFailureAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 21),
    _CiscoLS1010ChassisFailureAction_Type()
)
ciscoLS1010ChassisFailureAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisFailureAction.setStatus("current")


class _CiscoLS1010ChassisChangeAction_Type(Integer32):
    """Custom type ciscoLS1010ChassisChangeAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 1),
          ("sendTrap", 2))
    )


_CiscoLS1010ChassisChangeAction_Type.__name__ = "Integer32"
_CiscoLS1010ChassisChangeAction_Object = MibScalar
ciscoLS1010ChassisChangeAction = _CiscoLS1010ChassisChangeAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 22),
    _CiscoLS1010ChassisChangeAction_Type()
)
ciscoLS1010ChassisChangeAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisChangeAction.setStatus("current")


class _CiscoLS1010ChassisClockingMode_Type(Integer32):
    """Custom type ciscoLS1010ChassisClockingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 2),
          ("revertive", 1))
    )


_CiscoLS1010ChassisClockingMode_Type.__name__ = "Integer32"
_CiscoLS1010ChassisClockingMode_Object = MibScalar
ciscoLS1010ChassisClockingMode = _CiscoLS1010ChassisClockingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 23),
    _CiscoLS1010ChassisClockingMode_Type()
)
ciscoLS1010ChassisClockingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisClockingMode.setStatus("current")


class _Ciscols1010SystemClockSourceStatus_Type(Integer32):
    """Custom type ciscols1010SystemClockSourceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSelected", 1),
          ("selected", 2))
    )


_Ciscols1010SystemClockSourceStatus_Type.__name__ = "Integer32"
_Ciscols1010SystemClockSourceStatus_Object = MibScalar
ciscols1010SystemClockSourceStatus = _Ciscols1010SystemClockSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 24),
    _Ciscols1010SystemClockSourceStatus_Type()
)
ciscols1010SystemClockSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscols1010SystemClockSourceStatus.setStatus("current")


class _Ciscols1010SystemClockSourcePriority_Type(Integer32):
    """Custom type ciscols1010SystemClockSourcePriority based on Integer32"""
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
        *(("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5))
    )


_Ciscols1010SystemClockSourcePriority_Type.__name__ = "Integer32"
_Ciscols1010SystemClockSourcePriority_Object = MibScalar
ciscols1010SystemClockSourcePriority = _Ciscols1010SystemClockSourcePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 25),
    _Ciscols1010SystemClockSourcePriority_Type()
)
ciscols1010SystemClockSourcePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscols1010SystemClockSourcePriority.setStatus("current")


class _CiscoLS1010ChassisInletTempStatus_Type(Integer32):
    """Custom type ciscoLS1010ChassisInletTempStatus based on Integer32"""
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
        *(("criticalWarning", 5),
          ("majorWarning", 4),
          ("minorWarning", 3),
          ("ok", 1),
          ("overTemperature", 2),
          ("unknown", 6))
    )


_CiscoLS1010ChassisInletTempStatus_Type.__name__ = "Integer32"
_CiscoLS1010ChassisInletTempStatus_Object = MibScalar
ciscoLS1010ChassisInletTempStatus = _CiscoLS1010ChassisInletTempStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 1, 26),
    _CiscoLS1010ChassisInletTempStatus_Type()
)
ciscoLS1010ChassisInletTempStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ChassisInletTempStatus.setStatus("current")
_CiscoLS1010ModuleGroup_ObjectIdentity = ObjectIdentity
ciscoLS1010ModuleGroup = _CiscoLS1010ModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2)
)
_CiscoLS1010ModuleTable_Object = MibTable
ciscoLS1010ModuleTable = _CiscoLS1010ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ciscoLS1010ModuleTable.setStatus("current")
_CiscoLS1010ModuleEntry_Object = MibTableRow
ciscoLS1010ModuleEntry = _CiscoLS1010ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1)
)
ciscoLS1010ModuleEntry.setIndexNames(
    (0, "CISCO-RHINO-MIB", "ciscoLS1010ModuleIndex"),
)
if mibBuilder.loadTexts:
    ciscoLS1010ModuleEntry.setStatus("current")


class _CiscoLS1010ModuleIndex_Type(Integer32):
    """Custom type ciscoLS1010ModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CiscoLS1010ModuleIndex_Type.__name__ = "Integer32"
_CiscoLS1010ModuleIndex_Object = MibTableColumn
ciscoLS1010ModuleIndex = _CiscoLS1010ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 1),
    _CiscoLS1010ModuleIndex_Type()
)
ciscoLS1010ModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleIndex.setStatus("current")


class _CiscoLS1010ModuleType_Type(Integer32):
    """Custom type ciscoLS1010ModuleType based on Integer32"""
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
        *(("atmFabricIntegration", 9),
          ("carrier", 2),
          ("cmpmCarrier", 11),
          ("cpuRoute", 6),
          ("cpuSwitchAndFeature", 3),
          ("cpuSwitchAndFeaturePFQ", 4),
          ("dualSlot", 10),
          ("nodeSwitchProcessor2ndGeneration", 13),
          ("other", 1),
          ("superCarrier", 5),
          ("switch10GAndFC", 7),
          ("switch10GNoFC", 8),
          ("tsCarrier", 12))
    )


_CiscoLS1010ModuleType_Type.__name__ = "Integer32"
_CiscoLS1010ModuleType_Object = MibTableColumn
ciscoLS1010ModuleType = _CiscoLS1010ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 2),
    _CiscoLS1010ModuleType_Type()
)
ciscoLS1010ModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleType.setStatus("current")
_CiscoLS1010ModuleSerialNumber_Type = Integer32
_CiscoLS1010ModuleSerialNumber_Object = MibTableColumn
ciscoLS1010ModuleSerialNumber = _CiscoLS1010ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 3),
    _CiscoLS1010ModuleSerialNumber_Type()
)
ciscoLS1010ModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleSerialNumber.setStatus("deprecated")
_CiscoLS1010ModuleHwVersion_Type = Integer32
_CiscoLS1010ModuleHwVersion_Object = MibTableColumn
ciscoLS1010ModuleHwVersion = _CiscoLS1010ModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 4),
    _CiscoLS1010ModuleHwVersion_Type()
)
ciscoLS1010ModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleHwVersion.setStatus("current")
_CiscoLS1010ModuleSwVersion_Type = Integer32
_CiscoLS1010ModuleSwVersion_Object = MibTableColumn
ciscoLS1010ModuleSwVersion = _CiscoLS1010ModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 5),
    _CiscoLS1010ModuleSwVersion_Type()
)
ciscoLS1010ModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleSwVersion.setStatus("current")
_CiscoLS1010ModuleDescr_Type = DisplayString
_CiscoLS1010ModuleDescr_Object = MibTableColumn
ciscoLS1010ModuleDescr = _CiscoLS1010ModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 6),
    _CiscoLS1010ModuleDescr_Type()
)
ciscoLS1010ModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleDescr.setStatus("current")


class _CiscoLS1010ModuleNumSubModules_Type(Integer32):
    """Custom type ciscoLS1010ModuleNumSubModules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoLS1010ModuleNumSubModules_Type.__name__ = "Integer32"
_CiscoLS1010ModuleNumSubModules_Object = MibTableColumn
ciscoLS1010ModuleNumSubModules = _CiscoLS1010ModuleNumSubModules_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 7),
    _CiscoLS1010ModuleNumSubModules_Type()
)
ciscoLS1010ModuleNumSubModules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleNumSubModules.setStatus("current")
_CiscoLS1010ModuleAdminStatus_Type = AdminStatus
_CiscoLS1010ModuleAdminStatus_Object = MibTableColumn
ciscoLS1010ModuleAdminStatus = _CiscoLS1010ModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 8),
    _CiscoLS1010ModuleAdminStatus_Type()
)
ciscoLS1010ModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleAdminStatus.setStatus("current")
_CiscoLS1010ModuleOperStatus_Type = OperStatus
_CiscoLS1010ModuleOperStatus_Object = MibTableColumn
ciscoLS1010ModuleOperStatus = _CiscoLS1010ModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 9),
    _CiscoLS1010ModuleOperStatus_Type()
)
ciscoLS1010ModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleOperStatus.setStatus("current")
_CiscoLS1010ModuleHwVersionMinor_Type = Unsigned32
_CiscoLS1010ModuleHwVersionMinor_Object = MibTableColumn
ciscoLS1010ModuleHwVersionMinor = _CiscoLS1010ModuleHwVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 10),
    _CiscoLS1010ModuleHwVersionMinor_Type()
)
ciscoLS1010ModuleHwVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleHwVersionMinor.setStatus("current")
_CiscoLS1010ModuleSerialNumberString_Type = DisplayString
_CiscoLS1010ModuleSerialNumberString_Object = MibTableColumn
ciscoLS1010ModuleSerialNumberString = _CiscoLS1010ModuleSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 2, 1, 1, 11),
    _CiscoLS1010ModuleSerialNumberString_Type()
)
ciscoLS1010ModuleSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010ModuleSerialNumberString.setStatus("current")
_CiscoLS1010SubModuleGroup_ObjectIdentity = ObjectIdentity
ciscoLS1010SubModuleGroup = _CiscoLS1010SubModuleGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3)
)
_CiscoLS1010SubModuleTable_Object = MibTable
ciscoLS1010SubModuleTable = _CiscoLS1010SubModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleTable.setStatus("current")
_CiscoLS1010SubModuleEntry_Object = MibTableRow
ciscoLS1010SubModuleEntry = _CiscoLS1010SubModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1)
)
ciscoLS1010SubModuleEntry.setIndexNames(
    (0, "CISCO-RHINO-MIB", "ciscoLS1010ModuleIndex"),
    (0, "CISCO-RHINO-MIB", "ciscoLS1010SubModuleIndex"),
)
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleEntry.setStatus("current")


class _CiscoLS1010SubModuleIndex_Type(Integer32):
    """Custom type ciscoLS1010SubModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_CiscoLS1010SubModuleIndex_Type.__name__ = "Integer32"
_CiscoLS1010SubModuleIndex_Object = MibTableColumn
ciscoLS1010SubModuleIndex = _CiscoLS1010SubModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 1),
    _CiscoLS1010SubModuleIndex_Type()
)
ciscoLS1010SubModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleIndex.setStatus("current")


class _CiscoLS1010SubModuleType_Type(Integer32):
    """Custom type ciscoLS1010SubModuleType based on Integer32"""
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
              27,
              28,
              29,
              30,
              31,
              35,
              36,
              37,
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
              69,
              70,
              71,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98)
        )
    )
    namedValues = NamedValues(
        *(("aclDaughter", 98),
          ("arm1p64k", 80),
          ("arm2p64k", 81),
          ("atm25", 24),
          ("atm25m4p", 67),
          ("atmFIMBridge", 70),
          ("atmFIMoc12MM", 71),
          ("atmIma8pE1", 66),
          ("atmIma8pT1", 65),
          ("cbr120e1", 17),
          ("cbr75e1", 18),
          ("cbrt1", 16),
          ("cpuSwitch", 9),
          ("ds3", 7),
          ("dualDs3", 21),
          ("dualE3", 22),
          ("dualOC3MultiModeIRFiber", 28),
          ("dualOC3SingleModeIRFiber", 27),
          ("e1", 13),
          ("e1bnc", 14),
          ("e3", 8),
          ("feBridge4p", 52),
          ("feMMF16p16k", 46),
          ("feMMF16p64k", 47),
          ("feMMF8p16k", 42),
          ("feMMF8p64k", 43),
          ("feUTP16p16k", 44),
          ("feUTP16p64k", 45),
          ("feUTP8p16k", 40),
          ("feUTP8p16kFullDup", 53),
          ("feUTP8p64k", 41),
          ("feUTP8p64kFullDup", 54),
          ("featureABR", 58),
          ("featureAsic", 11),
          ("featureFpga", 10),
          ("featureLite", 60),
          ("featureNetClock", 57),
          ("featurePVC", 25),
          ("fratm1CT3", 30),
          ("fratm4CE1", 31),
          ("geF1p16k", 48),
          ("geF1p64k", 49),
          ("geF2p16k", 50),
          ("geF2p64k", 51),
          ("geF8p64k", 59),
          ("oc12Mixed", 23),
          ("oc12MultiModeFiber", 6),
          ("oc12SingleModeFiber", 5),
          ("oc12SingleModeLRFiber", 36),
          ("oc3Mixed", 15),
          ("oc3MultiModeFiber", 4),
          ("oc3SingleModeFiber", 3),
          ("oc3SingleModeLRFiber", 35),
          ("oc3Utp5", 2),
          ("other", 1),
          ("quadDs3", 19),
          ("quadE3", 20),
          ("routeProc", 55),
          ("routerProcessorAlpha", 26),
          ("routerProcessorBeta", 29),
          ("s16pOC3MM", 61),
          ("s16pOC3SM", 62),
          ("s1pOC48cSM", 68),
          ("s1pOC48cSMLR", 69),
          ("s4pOC12MM", 63),
          ("s4pOC12SM", 64),
          ("sixPortDS3", 37),
          ("switch10GProc", 56),
          ("t1", 12),
          ("xpif1pGE16k", 82),
          ("xpif1pGE256k", 84),
          ("xpif1pGE64k", 83),
          ("xpifArm2p256k", 97),
          ("xpifAtm1pOC12MM256k", 88),
          ("xpifAtm1pOC12MM64k", 87),
          ("xpifAtm1pOC12SMIR256k", 86),
          ("xpifAtm1pOC12SMIR64k", 85),
          ("xpifAtm1pOC3MM256k", 92),
          ("xpifAtm1pOC3MM64k", 91),
          ("xpifAtm1pOC3SMIR256k", 90),
          ("xpifAtm1pOC3SMIR64k", 89),
          ("xpifPos1pOC12SMIR256k", 94),
          ("xpifPos1pOC12SMIR64k", 93),
          ("xpifPos1pOC12SMLR256k", 96),
          ("xpifPos1pOC12SMLR64k", 95))
    )


_CiscoLS1010SubModuleType_Type.__name__ = "Integer32"
_CiscoLS1010SubModuleType_Object = MibTableColumn
ciscoLS1010SubModuleType = _CiscoLS1010SubModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 2),
    _CiscoLS1010SubModuleType_Type()
)
ciscoLS1010SubModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleType.setStatus("current")
_CiscoLS1010SubModuleSerialNumber_Type = Integer32
_CiscoLS1010SubModuleSerialNumber_Object = MibTableColumn
ciscoLS1010SubModuleSerialNumber = _CiscoLS1010SubModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 3),
    _CiscoLS1010SubModuleSerialNumber_Type()
)
ciscoLS1010SubModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleSerialNumber.setStatus("deprecated")
_CiscoLS1010SubModuleHwVersion_Type = Integer32
_CiscoLS1010SubModuleHwVersion_Object = MibTableColumn
ciscoLS1010SubModuleHwVersion = _CiscoLS1010SubModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 4),
    _CiscoLS1010SubModuleHwVersion_Type()
)
ciscoLS1010SubModuleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleHwVersion.setStatus("current")
_CiscoLS1010SubModuleSwVersion_Type = Integer32
_CiscoLS1010SubModuleSwVersion_Object = MibTableColumn
ciscoLS1010SubModuleSwVersion = _CiscoLS1010SubModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 5),
    _CiscoLS1010SubModuleSwVersion_Type()
)
ciscoLS1010SubModuleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleSwVersion.setStatus("current")
_CiscoLS1010SubModuleDescr_Type = DisplayString
_CiscoLS1010SubModuleDescr_Object = MibTableColumn
ciscoLS1010SubModuleDescr = _CiscoLS1010SubModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 6),
    _CiscoLS1010SubModuleDescr_Type()
)
ciscoLS1010SubModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleDescr.setStatus("current")


class _CiscoLS1010SubModuleNumPorts_Type(Integer32):
    """Custom type ciscoLS1010SubModuleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoLS1010SubModuleNumPorts_Type.__name__ = "Integer32"
_CiscoLS1010SubModuleNumPorts_Object = MibTableColumn
ciscoLS1010SubModuleNumPorts = _CiscoLS1010SubModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 7),
    _CiscoLS1010SubModuleNumPorts_Type()
)
ciscoLS1010SubModuleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleNumPorts.setStatus("current")


class _CiscoLS1010SubModuleAdminStatus_Type(Integer32):
    """Custom type ciscoLS1010SubModuleAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("reset", 1))
    )


_CiscoLS1010SubModuleAdminStatus_Type.__name__ = "Integer32"
_CiscoLS1010SubModuleAdminStatus_Object = MibTableColumn
ciscoLS1010SubModuleAdminStatus = _CiscoLS1010SubModuleAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 8),
    _CiscoLS1010SubModuleAdminStatus_Type()
)
ciscoLS1010SubModuleAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleAdminStatus.setStatus("current")
_CiscoLS1010SubModuleHwVersionMinor_Type = Integer32
_CiscoLS1010SubModuleHwVersionMinor_Object = MibTableColumn
ciscoLS1010SubModuleHwVersionMinor = _CiscoLS1010SubModuleHwVersionMinor_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 9),
    _CiscoLS1010SubModuleHwVersionMinor_Type()
)
ciscoLS1010SubModuleHwVersionMinor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleHwVersionMinor.setStatus("current")
_CiscoLS1010SubModuleOperStatus_Type = OperStatus
_CiscoLS1010SubModuleOperStatus_Object = MibTableColumn
ciscoLS1010SubModuleOperStatus = _CiscoLS1010SubModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 10),
    _CiscoLS1010SubModuleOperStatus_Type()
)
ciscoLS1010SubModuleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleOperStatus.setStatus("current")
_CiscoLS1010SubModuleSerialNumberString_Type = DisplayString
_CiscoLS1010SubModuleSerialNumberString_Object = MibTableColumn
ciscoLS1010SubModuleSerialNumberString = _CiscoLS1010SubModuleSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 3, 1, 1, 11),
    _CiscoLS1010SubModuleSerialNumberString_Type()
)
ciscoLS1010SubModuleSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010SubModuleSerialNumberString.setStatus("current")
_CiscoLS1010PortGroup_ObjectIdentity = ObjectIdentity
ciscoLS1010PortGroup = _CiscoLS1010PortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 4)
)
_CiscoLS1010PortTable_Object = MibTable
ciscoLS1010PortTable = _CiscoLS1010PortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ciscoLS1010PortTable.setStatus("current")
_CiscoLS1010PortEntry_Object = MibTableRow
ciscoLS1010PortEntry = _CiscoLS1010PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 4, 1, 1)
)
ciscoLS1010PortEntry.setIndexNames(
    (0, "CISCO-RHINO-MIB", "ciscoLS1010ModuleIndex"),
    (0, "CISCO-RHINO-MIB", "ciscoLS1010SubModuleIndex"),
    (0, "CISCO-RHINO-MIB", "ciscoLS1010PortIndex"),
)
if mibBuilder.loadTexts:
    ciscoLS1010PortEntry.setStatus("current")


class _CiscoLS1010PortIndex_Type(Integer32):
    """Custom type ciscoLS1010PortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CiscoLS1010PortIndex_Type.__name__ = "Integer32"
_CiscoLS1010PortIndex_Object = MibTableColumn
ciscoLS1010PortIndex = _CiscoLS1010PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 4, 1, 1, 1),
    _CiscoLS1010PortIndex_Type()
)
ciscoLS1010PortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoLS1010PortIndex.setStatus("current")
_CiscoLS1010PortIfIndex_Type = InterfaceIndex
_CiscoLS1010PortIfIndex_Object = MibTableColumn
ciscoLS1010PortIfIndex = _CiscoLS1010PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 4, 1, 1, 2),
    _CiscoLS1010PortIfIndex_Type()
)
ciscoLS1010PortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoLS1010PortIfIndex.setStatus("current")
_CiscoLS1010CpuSwitchGroup_ObjectIdentity = ObjectIdentity
ciscoLS1010CpuSwitchGroup = _CiscoLS1010CpuSwitchGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5)
)


class _CiscoAtmCpuAdminStatus_Type(Integer32):
    """Custom type ciscoAtmCpuAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 2),
          ("reset", 1))
    )


_CiscoAtmCpuAdminStatus_Type.__name__ = "Integer32"
_CiscoAtmCpuAdminStatus_Object = MibScalar
ciscoAtmCpuAdminStatus = _CiscoAtmCpuAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 1),
    _CiscoAtmCpuAdminStatus_Type()
)
ciscoAtmCpuAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmCpuAdminStatus.setStatus("current")
_CiscoAtmSwitchTotalBuffer_Type = Integer32
_CiscoAtmSwitchTotalBuffer_Object = MibScalar
ciscoAtmSwitchTotalBuffer = _CiscoAtmSwitchTotalBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 2),
    _CiscoAtmSwitchTotalBuffer_Type()
)
ciscoAtmSwitchTotalBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSwitchTotalBuffer.setStatus("current")
_CiscoAtmSwitchFreeBuffer_Type = Gauge32
_CiscoAtmSwitchFreeBuffer_Object = MibScalar
ciscoAtmSwitchFreeBuffer = _CiscoAtmSwitchFreeBuffer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 3),
    _CiscoAtmSwitchFreeBuffer_Type()
)
ciscoAtmSwitchFreeBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSwitchFreeBuffer.setStatus("current")
_CiscoAtmSwitchDiscardCells_Type = Counter32
_CiscoAtmSwitchDiscardCells_Object = MibScalar
ciscoAtmSwitchDiscardCells = _CiscoAtmSwitchDiscardCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 4),
    _CiscoAtmSwitchDiscardCells_Type()
)
ciscoAtmSwitchDiscardCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSwitchDiscardCells.setStatus("current")
_CiscoAtmSwitchInvalidCells_Type = Counter32
_CiscoAtmSwitchInvalidCells_Object = MibScalar
ciscoAtmSwitchInvalidCells = _CiscoAtmSwitchInvalidCells_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 5),
    _CiscoAtmSwitchInvalidCells_Type()
)
ciscoAtmSwitchInvalidCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSwitchInvalidCells.setStatus("current")
_CiscoAtmSwitchInvalidCellHeaderTable_Object = MibTable
ciscoAtmSwitchInvalidCellHeaderTable = _CiscoAtmSwitchInvalidCellHeaderTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 6)
)
if mibBuilder.loadTexts:
    ciscoAtmSwitchInvalidCellHeaderTable.setStatus("current")
_CiscoAtmSwitchInvalidCellHeaderEntry_Object = MibTableRow
ciscoAtmSwitchInvalidCellHeaderEntry = _CiscoAtmSwitchInvalidCellHeaderEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 6, 1)
)
ciscoAtmSwitchInvalidCellHeaderEntry.setIndexNames(
    (0, "CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCellHeaderIndex"),
)
if mibBuilder.loadTexts:
    ciscoAtmSwitchInvalidCellHeaderEntry.setStatus("current")


class _CiscoAtmSwitchInvalidCellHeaderIndex_Type(Integer32):
    """Custom type ciscoAtmSwitchInvalidCellHeaderIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_CiscoAtmSwitchInvalidCellHeaderIndex_Type.__name__ = "Integer32"
_CiscoAtmSwitchInvalidCellHeaderIndex_Object = MibTableColumn
ciscoAtmSwitchInvalidCellHeaderIndex = _CiscoAtmSwitchInvalidCellHeaderIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 6, 1, 1),
    _CiscoAtmSwitchInvalidCellHeaderIndex_Type()
)
ciscoAtmSwitchInvalidCellHeaderIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ciscoAtmSwitchInvalidCellHeaderIndex.setStatus("current")


class _CiscoAtmSwitchInvalidCellHeader_Type(OctetString):
    """Custom type ciscoAtmSwitchInvalidCellHeader based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )


_CiscoAtmSwitchInvalidCellHeader_Type.__name__ = "OctetString"
_CiscoAtmSwitchInvalidCellHeader_Object = MibTableColumn
ciscoAtmSwitchInvalidCellHeader = _CiscoAtmSwitchInvalidCellHeader_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 6, 1, 2),
    _CiscoAtmSwitchInvalidCellHeader_Type()
)
ciscoAtmSwitchInvalidCellHeader.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ciscoAtmSwitchInvalidCellHeader.setStatus("current")


class _CiscoAtmCpuTerminateOamFlow_Type(TruthValue):
    """Custom type ciscoAtmCpuTerminateOamFlow based on TruthValue"""


_CiscoAtmCpuTerminateOamFlow_Object = MibScalar
ciscoAtmCpuTerminateOamFlow = _CiscoAtmCpuTerminateOamFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 7),
    _CiscoAtmCpuTerminateOamFlow_Type()
)
ciscoAtmCpuTerminateOamFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmCpuTerminateOamFlow.setStatus("obsolete")


class _CiscoAtmInterceptEndToEndOamFlow_Type(TruthValue):
    """Custom type ciscoAtmInterceptEndToEndOamFlow based on TruthValue"""


_CiscoAtmInterceptEndToEndOamFlow_Object = MibScalar
ciscoAtmInterceptEndToEndOamFlow = _CiscoAtmInterceptEndToEndOamFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 5, 8),
    _CiscoAtmInterceptEndToEndOamFlow_Type()
)
ciscoAtmInterceptEndToEndOamFlow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ciscoAtmInterceptEndToEndOamFlow.setStatus("current")
_ClsEnetPortGroup_ObjectIdentity = ObjectIdentity
clsEnetPortGroup = _ClsEnetPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6)
)
_ClsEnetPortTable_Object = MibTable
clsEnetPortTable = _ClsEnetPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    clsEnetPortTable.setStatus("current")
_ClsEnetPortEntry_Object = MibTableRow
clsEnetPortEntry = _ClsEnetPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6, 1, 1)
)
clsEnetPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    clsEnetPortEntry.setStatus("current")


class _ClsEnetPortDuplex_Type(Integer32):
    """Custom type clsEnetPortDuplex based on Integer32"""
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
          ("full", 4),
          ("half", 3),
          ("unknown", 1))
    )


_ClsEnetPortDuplex_Type.__name__ = "Integer32"
_ClsEnetPortDuplex_Object = MibTableColumn
clsEnetPortDuplex = _ClsEnetPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6, 1, 1, 1),
    _ClsEnetPortDuplex_Type()
)
clsEnetPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsEnetPortDuplex.setStatus("current")


class _ClsEnetPortAdminSpeed_Type(Integer32):
    """Custom type clsEnetPortAdminSpeed based on Integer32"""
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
        *(("auto", 2),
          ("e1000Mbps", 5),
          ("e100Mbps", 4),
          ("e10Mbps", 3),
          ("unknown", 1))
    )


_ClsEnetPortAdminSpeed_Type.__name__ = "Integer32"
_ClsEnetPortAdminSpeed_Object = MibTableColumn
clsEnetPortAdminSpeed = _ClsEnetPortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6, 1, 1, 2),
    _ClsEnetPortAdminSpeed_Type()
)
clsEnetPortAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsEnetPortAdminSpeed.setStatus("current")


class _ClsEnetPortType_Type(Integer32):
    """Custom type clsEnetPortType based on Integer32"""
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
        *(("e1000BaseLX", 4),
          ("e1000BaseSX", 5),
          ("e100BaseFX", 3),
          ("e100BaseTX", 2),
          ("empty", 6),
          ("unknown", 1))
    )


_ClsEnetPortType_Type.__name__ = "Integer32"
_ClsEnetPortType_Object = MibTableColumn
clsEnetPortType = _ClsEnetPortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6, 1, 1, 3),
    _ClsEnetPortType_Type()
)
clsEnetPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsEnetPortType.setStatus("current")


class _ClsEnetPortLinkStatus_Type(Integer32):
    """Custom type clsEnetPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoNegotiate", 2),
          ("forceUp", 3),
          ("unknown", 1))
    )


_ClsEnetPortLinkStatus_Type.__name__ = "Integer32"
_ClsEnetPortLinkStatus_Object = MibTableColumn
clsEnetPortLinkStatus = _ClsEnetPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 6, 1, 1, 4),
    _ClsEnetPortLinkStatus_Type()
)
clsEnetPortLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clsEnetPortLinkStatus.setStatus("current")
_ClsPortLedGroup_ObjectIdentity = ObjectIdentity
clsPortLedGroup = _ClsPortLedGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 7)
)
_ClsPortLedTable_Object = MibTable
clsPortLedTable = _ClsPortLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 7, 1)
)
if mibBuilder.loadTexts:
    clsPortLedTable.setStatus("current")
_ClsPortLedEntry_Object = MibTableRow
clsPortLedEntry = _ClsPortLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 7, 1, 1)
)
clsPortLedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-RHINO-MIB", "clsPortLedIndex"),
)
if mibBuilder.loadTexts:
    clsPortLedEntry.setStatus("current")


class _ClsPortLedIndex_Type(Integer32):
    """Custom type clsPortLedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ClsPortLedIndex_Type.__name__ = "Integer32"
_ClsPortLedIndex_Object = MibTableColumn
clsPortLedIndex = _ClsPortLedIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 7, 1, 1, 1),
    _ClsPortLedIndex_Type()
)
clsPortLedIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clsPortLedIndex.setStatus("current")


class _ClsPortLedType_Type(Integer32):
    """Custom type clsPortLedType based on Integer32"""
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
        *(("led100Mbps", 4),
          ("ledFullDuplex", 8),
          ("ledLink", 3),
          ("ledOptDetect", 9),
          ("ledRx", 2),
          ("ledRxFullOut", 6),
          ("ledRxLoss", 5),
          ("ledRxSync", 7),
          ("ledTx", 1))
    )


_ClsPortLedType_Type.__name__ = "Integer32"
_ClsPortLedType_Object = MibTableColumn
clsPortLedType = _ClsPortLedType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 7, 1, 1, 2),
    _ClsPortLedType_Type()
)
clsPortLedType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortLedType.setStatus("current")


class _ClsPortLedStatus_Type(Integer32):
    """Custom type clsPortLedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 3),
          ("on", 2),
          ("unknown", 1))
    )


_ClsPortLedStatus_Type.__name__ = "Integer32"
_ClsPortLedStatus_Object = MibTableColumn
clsPortLedStatus = _ClsPortLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 1, 7, 1, 1, 3),
    _ClsPortLedStatus_Type()
)
clsPortLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clsPortLedStatus.setStatus("current")
_CiscoLS1010ChassisMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisMIBNotificationPrefix = _CiscoLS1010ChassisMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 2)
)
_CiscoLS1010ChassisMIBNotifications_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisMIBNotifications = _CiscoLS1010ChassisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 2, 0)
)
_CiscoLS1010ChassisMIBConformance_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisMIBConformance = _CiscoLS1010ChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3)
)
_CiscoLS1010ChassisMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisMIBCompliances = _CiscoLS1010ChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1)
)
_CiscoLS1010ChassisMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLS1010ChassisMIBGroups = _CiscoLS1010ChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2)
)

# Managed Objects groups

ciscoLS1010ChassisMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 1)
)
ciscoLS1010ChassisMIBGroup.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ChassisSysType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisBkplType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0AdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Led"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1AdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Led"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisCardStatusLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisEnetLinkLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010Chassis12VoltStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisTempStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPcmciaSlot0Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPcmciaSlot1Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisNumSlots"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisLastChange"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFailureAction"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisChangeAction"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisInletTempStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleSerialNumber"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleHwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleSwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleDescr"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleNumSubModules"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleOperStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSerialNumber"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleHwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleDescr"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleNumPorts"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010PortIfIndex"),
        ("CISCO-RHINO-MIB", "ciscoAtmCpuAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchTotalBuffer"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchFreeBuffer"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchDiscardCells"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCells"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCellHeader"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBGroup.setStatus("obsolete")

ciscoLS1010ChassisMIBObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 2)
)
ciscoLS1010ChassisMIBObsoleteGroup.setObjects(
    ("CISCO-RHINO-MIB", "ciscoAtmCpuTerminateOamFlow")
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBObsoleteGroup.setStatus("obsolete")

ciscoLS1010ChassisMIBRev1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 3)
)
ciscoLS1010ChassisMIBRev1Group.setObjects(
    ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleHwVersionMinor")
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBRev1Group.setStatus("current")

ciscoLS1010ChassisMIBClockingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 4)
)
ciscoLS1010ChassisMIBClockingGroup.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ChassisClockingMode"),
        ("CISCO-RHINO-MIB", "ciscols1010SystemClockSourceStatus"),
        ("CISCO-RHINO-MIB", "ciscols1010SystemClockSourcePriority"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBClockingGroup.setStatus("current")

ciscoLS1010ChassisMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 5)
)
ciscoLS1010ChassisMIBGroup1.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ChassisSysType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisBkplType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0AdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Led"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1AdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Led"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisCardStatusLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisEnetLinkLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010Chassis12VoltStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisTempStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPcmciaSlot0Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPcmciaSlot1Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisNumSlots"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisLastChange"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFailureAction"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisChangeAction"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleSerialNumber"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleHwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleSwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleDescr"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleNumSubModules"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSerialNumber"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleHwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleDescr"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleNumPorts"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleOperStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleHwVersionMinor"),
        ("CISCO-RHINO-MIB", "ciscoLS1010PortIfIndex"),
        ("CISCO-RHINO-MIB", "ciscoAtmCpuAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchTotalBuffer"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchFreeBuffer"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchDiscardCells"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCells"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCellHeader"),
        ("CISCO-RHINO-MIB", "ciscoAtmInterceptEndToEndOamFlow"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBGroup1.setStatus("obsolete")

clsEnetPortGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 6)
)
clsEnetPortGroup1.setObjects(
      *(("CISCO-RHINO-MIB", "clsEnetPortDuplex"),
        ("CISCO-RHINO-MIB", "clsEnetPortAdminSpeed"),
        ("CISCO-RHINO-MIB", "clsEnetPortType"),
        ("CISCO-RHINO-MIB", "clsEnetPortLinkStatus"))
)
if mibBuilder.loadTexts:
    clsEnetPortGroup1.setStatus("current")

clsPortLedGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 7)
)
clsPortLedGroup1.setObjects(
      *(("CISCO-RHINO-MIB", "clsPortLedType"),
        ("CISCO-RHINO-MIB", "clsPortLedStatus"))
)
if mibBuilder.loadTexts:
    clsPortLedGroup1.setStatus("current")

clsOperStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 8)
)
clsOperStatusGroup.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ModuleOperStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleOperStatus"))
)
if mibBuilder.loadTexts:
    clsOperStatusGroup.setStatus("current")

clsInletTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 9)
)
clsInletTempGroup.setObjects(
    ("CISCO-RHINO-MIB", "ciscoLS1010ChassisInletTempStatus")
)
if mibBuilder.loadTexts:
    clsInletTempGroup.setStatus("current")

ciscoLS1010ChassisMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 10)
)
ciscoLS1010ChassisMIBGroup2.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ChassisSysType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisBkplType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0AdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Led"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1AdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Led"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisCardStatusLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisEnetLinkLed"),
        ("CISCO-RHINO-MIB", "ciscoLS1010Chassis12VoltStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisTempStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPcmciaSlot0Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPcmciaSlot1Type"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisNumSlots"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisLastChange"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFailureAction"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisChangeAction"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleHwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleSwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleDescr"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleNumSubModules"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleType"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleHwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSwVersion"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleDescr"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleNumPorts"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleOperStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleHwVersionMinor"),
        ("CISCO-RHINO-MIB", "ciscoLS1010PortIfIndex"),
        ("CISCO-RHINO-MIB", "ciscoAtmCpuAdminStatus"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchTotalBuffer"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchFreeBuffer"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchDiscardCells"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCells"),
        ("CISCO-RHINO-MIB", "ciscoAtmSwitchInvalidCellHeader"),
        ("CISCO-RHINO-MIB", "ciscoAtmInterceptEndToEndOamFlow"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleHwVersionMinor"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ModuleSerialNumberString"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSerialNumberString"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBGroup2.setStatus("current")

ciscoLS1010ChassisMIBDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 11)
)
ciscoLS1010ChassisMIBDeprecatedGroup.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ModuleSerialNumber"),
        ("CISCO-RHINO-MIB", "ciscoLS1010SubModuleSerialNumber"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBDeprecatedGroup.setStatus("deprecated")


# Notification objects

ciscoLS1010ChassisFailureNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 2, 0, 1)
)
ciscoLS1010ChassisFailureNotification.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs0Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisPs1Status"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisFanStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010Chassis12VoltStatus"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisTempStatus"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisFailureNotification.setStatus(
        "current"
    )

ciscoLS1010ChassisChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 2, 0, 2)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisChangeNotification.setStatus(
        "current"
    )


# Notifications groups

ciscoLS1010ChassisMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 2, 12)
)
ciscoLS1010ChassisMIBNotificationGroup.setObjects(
      *(("CISCO-RHINO-MIB", "ciscoLS1010ChassisFailureNotification"),
        ("CISCO-RHINO-MIB", "ciscoLS1010ChassisChangeNotification"))
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLS1010ChassisMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBCompliance.setStatus(
        "obsolete"
    )

ciscoLS1010ChassisMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBComplianceRev1.setStatus(
        "obsolete"
    )

ciscoLS1010ChassisMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBComplianceRev2.setStatus(
        "obsolete"
    )

ciscoLS1010ChassisMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBComplianceRev3.setStatus(
        "obsolete"
    )

ciscoLS1010ChassisMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBComplianceRev4.setStatus(
        "obsolete"
    )

ciscoLS1010ChassisMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBComplianceRev5.setStatus(
        "obsolete"
    )

ciscoLS1010ChassisMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 11, 3, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoLS1010ChassisMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-RHINO-MIB",
    **{"PsType": PsType,
       "OperStatus": OperStatus,
       "AdminStatus": AdminStatus,
       "Led": Led,
       "PcmciaType": PcmciaType,
       "ciscoLS1010ChassisMIB": ciscoLS1010ChassisMIB,
       "ciscoLS1010ChassisMIBObjects": ciscoLS1010ChassisMIBObjects,
       "ciscoLS1010ChassisGroup": ciscoLS1010ChassisGroup,
       "ciscoLS1010ChassisSysType": ciscoLS1010ChassisSysType,
       "ciscoLS1010ChassisBkplType": ciscoLS1010ChassisBkplType,
       "ciscoLS1010ChassisPs0Type": ciscoLS1010ChassisPs0Type,
       "ciscoLS1010ChassisPs0AdminStatus": ciscoLS1010ChassisPs0AdminStatus,
       "ciscoLS1010ChassisPs0Status": ciscoLS1010ChassisPs0Status,
       "ciscoLS1010ChassisPs0Led": ciscoLS1010ChassisPs0Led,
       "ciscoLS1010ChassisPs1Type": ciscoLS1010ChassisPs1Type,
       "ciscoLS1010ChassisPs1AdminStatus": ciscoLS1010ChassisPs1AdminStatus,
       "ciscoLS1010ChassisPs1Status": ciscoLS1010ChassisPs1Status,
       "ciscoLS1010ChassisPs1Led": ciscoLS1010ChassisPs1Led,
       "ciscoLS1010ChassisFanStatus": ciscoLS1010ChassisFanStatus,
       "ciscoLS1010ChassisFanLed": ciscoLS1010ChassisFanLed,
       "ciscoLS1010ChassisCardStatusLed": ciscoLS1010ChassisCardStatusLed,
       "ciscoLS1010ChassisEnetLinkLed": ciscoLS1010ChassisEnetLinkLed,
       "ciscoLS1010Chassis12VoltStatus": ciscoLS1010Chassis12VoltStatus,
       "ciscoLS1010ChassisTempStatus": ciscoLS1010ChassisTempStatus,
       "ciscoLS1010ChassisPcmciaSlot0Type": ciscoLS1010ChassisPcmciaSlot0Type,
       "ciscoLS1010ChassisPcmciaSlot1Type": ciscoLS1010ChassisPcmciaSlot1Type,
       "ciscoLS1010ChassisNumSlots": ciscoLS1010ChassisNumSlots,
       "ciscoLS1010ChassisLastChange": ciscoLS1010ChassisLastChange,
       "ciscoLS1010ChassisFailureAction": ciscoLS1010ChassisFailureAction,
       "ciscoLS1010ChassisChangeAction": ciscoLS1010ChassisChangeAction,
       "ciscoLS1010ChassisClockingMode": ciscoLS1010ChassisClockingMode,
       "ciscols1010SystemClockSourceStatus": ciscols1010SystemClockSourceStatus,
       "ciscols1010SystemClockSourcePriority": ciscols1010SystemClockSourcePriority,
       "ciscoLS1010ChassisInletTempStatus": ciscoLS1010ChassisInletTempStatus,
       "ciscoLS1010ModuleGroup": ciscoLS1010ModuleGroup,
       "ciscoLS1010ModuleTable": ciscoLS1010ModuleTable,
       "ciscoLS1010ModuleEntry": ciscoLS1010ModuleEntry,
       "ciscoLS1010ModuleIndex": ciscoLS1010ModuleIndex,
       "ciscoLS1010ModuleType": ciscoLS1010ModuleType,
       "ciscoLS1010ModuleSerialNumber": ciscoLS1010ModuleSerialNumber,
       "ciscoLS1010ModuleHwVersion": ciscoLS1010ModuleHwVersion,
       "ciscoLS1010ModuleSwVersion": ciscoLS1010ModuleSwVersion,
       "ciscoLS1010ModuleDescr": ciscoLS1010ModuleDescr,
       "ciscoLS1010ModuleNumSubModules": ciscoLS1010ModuleNumSubModules,
       "ciscoLS1010ModuleAdminStatus": ciscoLS1010ModuleAdminStatus,
       "ciscoLS1010ModuleOperStatus": ciscoLS1010ModuleOperStatus,
       "ciscoLS1010ModuleHwVersionMinor": ciscoLS1010ModuleHwVersionMinor,
       "ciscoLS1010ModuleSerialNumberString": ciscoLS1010ModuleSerialNumberString,
       "ciscoLS1010SubModuleGroup": ciscoLS1010SubModuleGroup,
       "ciscoLS1010SubModuleTable": ciscoLS1010SubModuleTable,
       "ciscoLS1010SubModuleEntry": ciscoLS1010SubModuleEntry,
       "ciscoLS1010SubModuleIndex": ciscoLS1010SubModuleIndex,
       "ciscoLS1010SubModuleType": ciscoLS1010SubModuleType,
       "ciscoLS1010SubModuleSerialNumber": ciscoLS1010SubModuleSerialNumber,
       "ciscoLS1010SubModuleHwVersion": ciscoLS1010SubModuleHwVersion,
       "ciscoLS1010SubModuleSwVersion": ciscoLS1010SubModuleSwVersion,
       "ciscoLS1010SubModuleDescr": ciscoLS1010SubModuleDescr,
       "ciscoLS1010SubModuleNumPorts": ciscoLS1010SubModuleNumPorts,
       "ciscoLS1010SubModuleAdminStatus": ciscoLS1010SubModuleAdminStatus,
       "ciscoLS1010SubModuleHwVersionMinor": ciscoLS1010SubModuleHwVersionMinor,
       "ciscoLS1010SubModuleOperStatus": ciscoLS1010SubModuleOperStatus,
       "ciscoLS1010SubModuleSerialNumberString": ciscoLS1010SubModuleSerialNumberString,
       "ciscoLS1010PortGroup": ciscoLS1010PortGroup,
       "ciscoLS1010PortTable": ciscoLS1010PortTable,
       "ciscoLS1010PortEntry": ciscoLS1010PortEntry,
       "ciscoLS1010PortIndex": ciscoLS1010PortIndex,
       "ciscoLS1010PortIfIndex": ciscoLS1010PortIfIndex,
       "ciscoLS1010CpuSwitchGroup": ciscoLS1010CpuSwitchGroup,
       "ciscoAtmCpuAdminStatus": ciscoAtmCpuAdminStatus,
       "ciscoAtmSwitchTotalBuffer": ciscoAtmSwitchTotalBuffer,
       "ciscoAtmSwitchFreeBuffer": ciscoAtmSwitchFreeBuffer,
       "ciscoAtmSwitchDiscardCells": ciscoAtmSwitchDiscardCells,
       "ciscoAtmSwitchInvalidCells": ciscoAtmSwitchInvalidCells,
       "ciscoAtmSwitchInvalidCellHeaderTable": ciscoAtmSwitchInvalidCellHeaderTable,
       "ciscoAtmSwitchInvalidCellHeaderEntry": ciscoAtmSwitchInvalidCellHeaderEntry,
       "ciscoAtmSwitchInvalidCellHeaderIndex": ciscoAtmSwitchInvalidCellHeaderIndex,
       "ciscoAtmSwitchInvalidCellHeader": ciscoAtmSwitchInvalidCellHeader,
       "ciscoAtmCpuTerminateOamFlow": ciscoAtmCpuTerminateOamFlow,
       "ciscoAtmInterceptEndToEndOamFlow": ciscoAtmInterceptEndToEndOamFlow,
       "clsEnetPortGroup": clsEnetPortGroup,
       "clsEnetPortTable": clsEnetPortTable,
       "clsEnetPortEntry": clsEnetPortEntry,
       "clsEnetPortDuplex": clsEnetPortDuplex,
       "clsEnetPortAdminSpeed": clsEnetPortAdminSpeed,
       "clsEnetPortType": clsEnetPortType,
       "clsEnetPortLinkStatus": clsEnetPortLinkStatus,
       "clsPortLedGroup": clsPortLedGroup,
       "clsPortLedTable": clsPortLedTable,
       "clsPortLedEntry": clsPortLedEntry,
       "clsPortLedIndex": clsPortLedIndex,
       "clsPortLedType": clsPortLedType,
       "clsPortLedStatus": clsPortLedStatus,
       "ciscoLS1010ChassisMIBNotificationPrefix": ciscoLS1010ChassisMIBNotificationPrefix,
       "ciscoLS1010ChassisMIBNotifications": ciscoLS1010ChassisMIBNotifications,
       "ciscoLS1010ChassisFailureNotification": ciscoLS1010ChassisFailureNotification,
       "ciscoLS1010ChassisChangeNotification": ciscoLS1010ChassisChangeNotification,
       "ciscoLS1010ChassisMIBConformance": ciscoLS1010ChassisMIBConformance,
       "ciscoLS1010ChassisMIBCompliances": ciscoLS1010ChassisMIBCompliances,
       "ciscoLS1010ChassisMIBCompliance": ciscoLS1010ChassisMIBCompliance,
       "ciscoLS1010ChassisMIBComplianceRev1": ciscoLS1010ChassisMIBComplianceRev1,
       "ciscoLS1010ChassisMIBComplianceRev2": ciscoLS1010ChassisMIBComplianceRev2,
       "ciscoLS1010ChassisMIBComplianceRev3": ciscoLS1010ChassisMIBComplianceRev3,
       "ciscoLS1010ChassisMIBComplianceRev4": ciscoLS1010ChassisMIBComplianceRev4,
       "ciscoLS1010ChassisMIBComplianceRev5": ciscoLS1010ChassisMIBComplianceRev5,
       "ciscoLS1010ChassisMIBComplianceRev6": ciscoLS1010ChassisMIBComplianceRev6,
       "ciscoLS1010ChassisMIBGroups": ciscoLS1010ChassisMIBGroups,
       "ciscoLS1010ChassisMIBGroup": ciscoLS1010ChassisMIBGroup,
       "ciscoLS1010ChassisMIBObsoleteGroup": ciscoLS1010ChassisMIBObsoleteGroup,
       "ciscoLS1010ChassisMIBRev1Group": ciscoLS1010ChassisMIBRev1Group,
       "ciscoLS1010ChassisMIBClockingGroup": ciscoLS1010ChassisMIBClockingGroup,
       "ciscoLS1010ChassisMIBGroup1": ciscoLS1010ChassisMIBGroup1,
       "clsEnetPortGroup1": clsEnetPortGroup1,
       "clsPortLedGroup1": clsPortLedGroup1,
       "clsOperStatusGroup": clsOperStatusGroup,
       "clsInletTempGroup": clsInletTempGroup,
       "ciscoLS1010ChassisMIBGroup2": ciscoLS1010ChassisMIBGroup2,
       "ciscoLS1010ChassisMIBDeprecatedGroup": ciscoLS1010ChassisMIBDeprecatedGroup,
       "ciscoLS1010ChassisMIBNotificationGroup": ciscoLS1010ChassisMIBNotificationGroup}
)
