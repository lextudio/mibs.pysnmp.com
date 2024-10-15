# SNMP MIB module (WWP-LEOS-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-CHASSIS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:14:48 2024
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

(DateAndTime,
 DisplayString,
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosChassisMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11)
)
wwpLeosChassisMIB.setRevisions(
        ("2012-09-27 00:00",
         "2011-11-14 00:00",
         "2011-03-22 00:00",
         "2010-01-27 00:00",
         "2009-11-09 00:00",
         "2008-10-06 00:00",
         "2008-06-14 00:00",
         "2007-05-06 00:48",
         "2003-04-28 00:00",
         "2003-03-11 00:00",
         "2001-04-03 17:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class PortList(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class FileName(OctetString, TextualConvention):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosChassisMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosChassisMIBObjects = _WwpLeosChassisMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1)
)
_WwpLeosChassis_ObjectIdentity = ObjectIdentity
wwpLeosChassis = _WwpLeosChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1)
)
_WwpLeosChassisModule_ObjectIdentity = ObjectIdentity
wwpLeosChassisModule = _WwpLeosChassisModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1)
)


class _WwpLeosChassisRebootState_Type(TruthValue):
    """Custom type wwpLeosChassisRebootState based on TruthValue"""


_WwpLeosChassisRebootState_Object = MibScalar
wwpLeosChassisRebootState = _WwpLeosChassisRebootState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 1),
    _WwpLeosChassisRebootState_Type()
)
wwpLeosChassisRebootState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisRebootState.setStatus("current")


class _WwpLeosChassisSystemTimeOffsetScope_Type(Integer32):
    """Custom type wwpLeosChassisSystemTimeOffsetScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("dhcp", 1),
          ("user", 2))
    )


_WwpLeosChassisSystemTimeOffsetScope_Type.__name__ = "Integer32"
_WwpLeosChassisSystemTimeOffsetScope_Object = MibScalar
wwpLeosChassisSystemTimeOffsetScope = _WwpLeosChassisSystemTimeOffsetScope_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 2),
    _WwpLeosChassisSystemTimeOffsetScope_Type()
)
wwpLeosChassisSystemTimeOffsetScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisSystemTimeOffsetScope.setStatus("current")


class _WwpLeosChassisSystemTimeOffset_Type(Integer32):
    """Custom type wwpLeosChassisSystemTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-43200, 50400),
    )


_WwpLeosChassisSystemTimeOffset_Type.__name__ = "Integer32"
_WwpLeosChassisSystemTimeOffset_Object = MibScalar
wwpLeosChassisSystemTimeOffset = _WwpLeosChassisSystemTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 3),
    _WwpLeosChassisSystemTimeOffset_Type()
)
wwpLeosChassisSystemTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisSystemTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisSystemTimeOffset.setUnits("seconds")


class _WwpLeosChassisSerialConsoleState_Type(Integer32):
    """Custom type wwpLeosChassisSerialConsoleState based on Integer32"""
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


_WwpLeosChassisSerialConsoleState_Type.__name__ = "Integer32"
_WwpLeosChassisSerialConsoleState_Object = MibScalar
wwpLeosChassisSerialConsoleState = _WwpLeosChassisSerialConsoleState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 4),
    _WwpLeosChassisSerialConsoleState_Type()
)
wwpLeosChassisSerialConsoleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisSerialConsoleState.setStatus("current")


class _WwpLeosChassisShellInactivityTimerState_Type(Integer32):
    """Custom type wwpLeosChassisShellInactivityTimerState based on Integer32"""
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


_WwpLeosChassisShellInactivityTimerState_Type.__name__ = "Integer32"
_WwpLeosChassisShellInactivityTimerState_Object = MibScalar
wwpLeosChassisShellInactivityTimerState = _WwpLeosChassisShellInactivityTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 5),
    _WwpLeosChassisShellInactivityTimerState_Type()
)
wwpLeosChassisShellInactivityTimerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisShellInactivityTimerState.setStatus("current")


class _WwpLeosChassisShellInactivityTimeout_Type(Integer32):
    """Custom type wwpLeosChassisShellInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1500),
    )


_WwpLeosChassisShellInactivityTimeout_Type.__name__ = "Integer32"
_WwpLeosChassisShellInactivityTimeout_Object = MibScalar
wwpLeosChassisShellInactivityTimeout = _WwpLeosChassisShellInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 6),
    _WwpLeosChassisShellInactivityTimeout_Type()
)
wwpLeosChassisShellInactivityTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisShellInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisShellInactivityTimeout.setUnits("minutes")


class _WwpLeosChassisSerialConsoleDataBits_Type(Integer32):
    """Custom type wwpLeosChassisSerialConsoleDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_WwpLeosChassisSerialConsoleDataBits_Type.__name__ = "Integer32"
_WwpLeosChassisSerialConsoleDataBits_Object = MibScalar
wwpLeosChassisSerialConsoleDataBits = _WwpLeosChassisSerialConsoleDataBits_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 8),
    _WwpLeosChassisSerialConsoleDataBits_Type()
)
wwpLeosChassisSerialConsoleDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisSerialConsoleDataBits.setStatus("current")


class _WwpLeosChassisSerialConsoleParity_Type(Integer32):
    """Custom type wwpLeosChassisSerialConsoleParity based on Integer32"""
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
        *(("even", 1),
          ("mark", 2),
          ("none", 3),
          ("odd", 4),
          ("space", 5))
    )


_WwpLeosChassisSerialConsoleParity_Type.__name__ = "Integer32"
_WwpLeosChassisSerialConsoleParity_Object = MibScalar
wwpLeosChassisSerialConsoleParity = _WwpLeosChassisSerialConsoleParity_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 12),
    _WwpLeosChassisSerialConsoleParity_Type()
)
wwpLeosChassisSerialConsoleParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisSerialConsoleParity.setStatus("current")


class _WwpLeosChassisSerialConsoleStopBits_Type(Integer32):
    """Custom type wwpLeosChassisSerialConsoleStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WwpLeosChassisSerialConsoleStopBits_Type.__name__ = "Integer32"
_WwpLeosChassisSerialConsoleStopBits_Object = MibScalar
wwpLeosChassisSerialConsoleStopBits = _WwpLeosChassisSerialConsoleStopBits_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 13),
    _WwpLeosChassisSerialConsoleStopBits_Type()
)
wwpLeosChassisSerialConsoleStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisSerialConsoleStopBits.setStatus("current")


class _WwpLeosChassisRebootNow_Type(TruthValue):
    """Custom type wwpLeosChassisRebootNow based on TruthValue"""


_WwpLeosChassisRebootNow_Object = MibScalar
wwpLeosChassisRebootNow = _WwpLeosChassisRebootNow_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 14),
    _WwpLeosChassisRebootNow_Type()
)
wwpLeosChassisRebootNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisRebootNow.setStatus("current")


class _WwpLeosChassisShellLoginTimerState_Type(Integer32):
    """Custom type wwpLeosChassisShellLoginTimerState based on Integer32"""
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


_WwpLeosChassisShellLoginTimerState_Type.__name__ = "Integer32"
_WwpLeosChassisShellLoginTimerState_Object = MibScalar
wwpLeosChassisShellLoginTimerState = _WwpLeosChassisShellLoginTimerState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 15),
    _WwpLeosChassisShellLoginTimerState_Type()
)
wwpLeosChassisShellLoginTimerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisShellLoginTimerState.setStatus("current")


class _WwpLeosChassisShellLoginTimeout_Type(Integer32):
    """Custom type wwpLeosChassisShellLoginTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_WwpLeosChassisShellLoginTimeout_Type.__name__ = "Integer32"
_WwpLeosChassisShellLoginTimeout_Object = MibScalar
wwpLeosChassisShellLoginTimeout = _WwpLeosChassisShellLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 16),
    _WwpLeosChassisShellLoginTimeout_Type()
)
wwpLeosChassisShellLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisShellLoginTimeout.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisShellLoginTimeout.setUnits("seconds")
_WwpLeosChassisScheduledRebootTable_Object = MibTable
wwpLeosChassisScheduledRebootTable = _WwpLeosChassisScheduledRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootTable.setStatus("current")
_WwpLeosChassisScheduledRebootEntry_Object = MibTableRow
wwpLeosChassisScheduledRebootEntry = _WwpLeosChassisScheduledRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17, 1)
)
wwpLeosChassisScheduledRebootEntry.setIndexNames(
    (0, "WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisScheduledRebootIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootEntry.setStatus("current")


class _WwpLeosChassisScheduledRebootIndex_Type(Integer32):
    """Custom type wwpLeosChassisScheduledRebootIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_WwpLeosChassisScheduledRebootIndex_Type.__name__ = "Integer32"
_WwpLeosChassisScheduledRebootIndex_Object = MibTableColumn
wwpLeosChassisScheduledRebootIndex = _WwpLeosChassisScheduledRebootIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17, 1, 1),
    _WwpLeosChassisScheduledRebootIndex_Type()
)
wwpLeosChassisScheduledRebootIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootIndex.setStatus("current")
_WwpLeosChassisScheduledRebootTimestamp_Type = DateAndTime
_WwpLeosChassisScheduledRebootTimestamp_Object = MibTableColumn
wwpLeosChassisScheduledRebootTimestamp = _WwpLeosChassisScheduledRebootTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17, 1, 2),
    _WwpLeosChassisScheduledRebootTimestamp_Type()
)
wwpLeosChassisScheduledRebootTimestamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootTimestamp.setStatus("current")


class _WwpLeosChassisScheduledRebootActive_Type(TruthValue):
    """Custom type wwpLeosChassisScheduledRebootActive based on TruthValue"""


_WwpLeosChassisScheduledRebootActive_Object = MibTableColumn
wwpLeosChassisScheduledRebootActive = _WwpLeosChassisScheduledRebootActive_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17, 1, 3),
    _WwpLeosChassisScheduledRebootActive_Type()
)
wwpLeosChassisScheduledRebootActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootActive.setStatus("current")


class _WwpLeosChassisScheduledRebootNopost_Type(TruthValue):
    """Custom type wwpLeosChassisScheduledRebootNopost based on TruthValue"""


_WwpLeosChassisScheduledRebootNopost_Object = MibTableColumn
wwpLeosChassisScheduledRebootNopost = _WwpLeosChassisScheduledRebootNopost_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17, 1, 4),
    _WwpLeosChassisScheduledRebootNopost_Type()
)
wwpLeosChassisScheduledRebootNopost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootNopost.setStatus("current")


class _WwpLeosChassisScheduledRebootDelay_Type(Integer32):
    """Custom type wwpLeosChassisScheduledRebootDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_WwpLeosChassisScheduledRebootDelay_Type.__name__ = "Integer32"
_WwpLeosChassisScheduledRebootDelay_Object = MibTableColumn
wwpLeosChassisScheduledRebootDelay = _WwpLeosChassisScheduledRebootDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 17, 1, 5),
    _WwpLeosChassisScheduledRebootDelay_Type()
)
wwpLeosChassisScheduledRebootDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisScheduledRebootDelay.setStatus("current")
_WwpLeosChassisWelcomeBanner_Type = FileName
_WwpLeosChassisWelcomeBanner_Object = MibScalar
wwpLeosChassisWelcomeBanner = _WwpLeosChassisWelcomeBanner_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 18),
    _WwpLeosChassisWelcomeBanner_Type()
)
wwpLeosChassisWelcomeBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisWelcomeBanner.setStatus("current")
_WwpLeosChassisResetWelcomeBanner_Type = TruthValue
_WwpLeosChassisResetWelcomeBanner_Object = MibScalar
wwpLeosChassisResetWelcomeBanner = _WwpLeosChassisResetWelcomeBanner_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 19),
    _WwpLeosChassisResetWelcomeBanner_Type()
)
wwpLeosChassisResetWelcomeBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisResetWelcomeBanner.setStatus("current")
_WwpLeosChassisLoginBanner_Type = FileName
_WwpLeosChassisLoginBanner_Object = MibScalar
wwpLeosChassisLoginBanner = _WwpLeosChassisLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 20),
    _WwpLeosChassisLoginBanner_Type()
)
wwpLeosChassisLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisLoginBanner.setStatus("current")
_WwpLeosChassisResetLoginBanner_Type = TruthValue
_WwpLeosChassisResetLoginBanner_Object = MibScalar
wwpLeosChassisResetLoginBanner = _WwpLeosChassisResetLoginBanner_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 21),
    _WwpLeosChassisResetLoginBanner_Type()
)
wwpLeosChassisResetLoginBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisResetLoginBanner.setStatus("current")
_WwpLeosChassisMacAddress_Type = MacAddress
_WwpLeosChassisMacAddress_Object = MibScalar
wwpLeosChassisMacAddress = _WwpLeosChassisMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 50),
    _WwpLeosChassisMacAddress_Type()
)
wwpLeosChassisMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisMacAddress.setStatus("current")
_WwpLeosChassisDeviceId_Type = DisplayString
_WwpLeosChassisDeviceId_Object = MibScalar
wwpLeosChassisDeviceId = _WwpLeosChassisDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 51),
    _WwpLeosChassisDeviceId_Type()
)
wwpLeosChassisDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisDeviceId.setStatus("current")
_WwpLeosChassisSerialNumber_Type = DisplayString
_WwpLeosChassisSerialNumber_Object = MibScalar
wwpLeosChassisSerialNumber = _WwpLeosChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 52),
    _WwpLeosChassisSerialNumber_Type()
)
wwpLeosChassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisSerialNumber.setStatus("current")
_WwpLeosChassisMfgDate_Type = DateAndTime
_WwpLeosChassisMfgDate_Object = MibScalar
wwpLeosChassisMfgDate = _WwpLeosChassisMfgDate_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 53),
    _WwpLeosChassisMfgDate_Type()
)
wwpLeosChassisMfgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisMfgDate.setStatus("current")
_WwpLeosChassisParamVersion_Type = DisplayString
_WwpLeosChassisParamVersion_Object = MibScalar
wwpLeosChassisParamVersion = _WwpLeosChassisParamVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 54),
    _WwpLeosChassisParamVersion_Type()
)
wwpLeosChassisParamVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisParamVersion.setStatus("current")
_WwpLeosChassisHardwareVersion_Type = DisplayString
_WwpLeosChassisHardwareVersion_Object = MibScalar
wwpLeosChassisHardwareVersion = _WwpLeosChassisHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 55),
    _WwpLeosChassisHardwareVersion_Type()
)
wwpLeosChassisHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisHardwareVersion.setStatus("current")


class _WwpLeosChassisInnerDoorStatus_Type(Integer32):
    """Custom type wwpLeosChassisInnerDoorStatus based on Integer32"""
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
        *(("closed", 2),
          ("none", 0),
          ("open", 1),
          ("override", 3))
    )


_WwpLeosChassisInnerDoorStatus_Type.__name__ = "Integer32"
_WwpLeosChassisInnerDoorStatus_Object = MibScalar
wwpLeosChassisInnerDoorStatus = _WwpLeosChassisInnerDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 56),
    _WwpLeosChassisInnerDoorStatus_Type()
)
wwpLeosChassisInnerDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisInnerDoorStatus.setStatus("current")


class _WwpLeosChassisOuterDoorStatus_Type(Integer32):
    """Custom type wwpLeosChassisOuterDoorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("none", 0),
          ("open", 1))
    )


_WwpLeosChassisOuterDoorStatus_Type.__name__ = "Integer32"
_WwpLeosChassisOuterDoorStatus_Object = MibScalar
wwpLeosChassisOuterDoorStatus = _WwpLeosChassisOuterDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 57),
    _WwpLeosChassisOuterDoorStatus_Type()
)
wwpLeosChassisOuterDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisOuterDoorStatus.setStatus("current")


class _WwpLeosChassisPostState_Type(Integer32):
    """Custom type wwpLeosChassisPostState based on Integer32"""
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


_WwpLeosChassisPostState_Type.__name__ = "Integer32"
_WwpLeosChassisPostState_Object = MibScalar
wwpLeosChassisPostState = _WwpLeosChassisPostState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 60),
    _WwpLeosChassisPostState_Type()
)
wwpLeosChassisPostState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisPostState.setStatus("current")
_WwpLeosChassisPostResultTable_Object = MibTable
wwpLeosChassisPostResultTable = _WwpLeosChassisPostResultTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 61)
)
if mibBuilder.loadTexts:
    wwpLeosChassisPostResultTable.setStatus("current")
_WwpLeosChassisPostResultEntry_Object = MibTableRow
wwpLeosChassisPostResultEntry = _WwpLeosChassisPostResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 61, 1)
)
wwpLeosChassisPostResultEntry.setIndexNames(
    (0, "WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPostResultIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosChassisPostResultEntry.setStatus("current")


class _WwpLeosChassisPostResultIndex_Type(Integer32):
    """Custom type wwpLeosChassisPostResultIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_WwpLeosChassisPostResultIndex_Type.__name__ = "Integer32"
_WwpLeosChassisPostResultIndex_Object = MibTableColumn
wwpLeosChassisPostResultIndex = _WwpLeosChassisPostResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 61, 1, 1),
    _WwpLeosChassisPostResultIndex_Type()
)
wwpLeosChassisPostResultIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosChassisPostResultIndex.setStatus("current")
_WwpLeosChassisPostResultCode_Type = Unsigned32
_WwpLeosChassisPostResultCode_Object = MibTableColumn
wwpLeosChassisPostResultCode = _WwpLeosChassisPostResultCode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 61, 1, 2),
    _WwpLeosChassisPostResultCode_Type()
)
wwpLeosChassisPostResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPostResultCode.setStatus("current")
_WwpLeosChassisPostResultMessage_Type = DisplayString
_WwpLeosChassisPostResultMessage_Object = MibTableColumn
wwpLeosChassisPostResultMessage = _WwpLeosChassisPostResultMessage_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 61, 1, 3),
    _WwpLeosChassisPostResultMessage_Type()
)
wwpLeosChassisPostResultMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPostResultMessage.setStatus("current")


class _WwpLeosChassisExternalAlarmStatus_Type(Integer32):
    """Custom type wwpLeosChassisExternalAlarmStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 2),
          ("raised", 1))
    )


_WwpLeosChassisExternalAlarmStatus_Type.__name__ = "Integer32"
_WwpLeosChassisExternalAlarmStatus_Object = MibScalar
wwpLeosChassisExternalAlarmStatus = _WwpLeosChassisExternalAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 62),
    _WwpLeosChassisExternalAlarmStatus_Type()
)
wwpLeosChassisExternalAlarmStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisExternalAlarmStatus.setStatus("current")


class _WwpLeosChassisExternalAlarm_Type(Integer32):
    """Custom type wwpLeosChassisExternalAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosChassisExternalAlarm_Type.__name__ = "Integer32"
_WwpLeosChassisExternalAlarm_Object = MibScalar
wwpLeosChassisExternalAlarm = _WwpLeosChassisExternalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 63),
    _WwpLeosChassisExternalAlarm_Type()
)
wwpLeosChassisExternalAlarm.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisExternalAlarm.setStatus("current")
_WwpLeosChassisDoorAlarmTable_Object = MibTable
wwpLeosChassisDoorAlarmTable = _WwpLeosChassisDoorAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64)
)
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmTable.setStatus("current")
_WwpLeosChassisDoorAlarmEntry_Object = MibTableRow
wwpLeosChassisDoorAlarmEntry = _WwpLeosChassisDoorAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1)
)
wwpLeosChassisDoorAlarmEntry.setIndexNames(
    (0, "WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDoorAlarmIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmEntry.setStatus("current")


class _WwpLeosChassisDoorAlarmIndex_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inner", 0),
          ("outer", 1))
    )


_WwpLeosChassisDoorAlarmIndex_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmIndex_Object = MibTableColumn
wwpLeosChassisDoorAlarmIndex = _WwpLeosChassisDoorAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 1),
    _WwpLeosChassisDoorAlarmIndex_Type()
)
wwpLeosChassisDoorAlarmIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmIndex.setStatus("current")


class _WwpLeosChassisDoorAlarmStatus_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmStatus based on Integer32"""
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


_WwpLeosChassisDoorAlarmStatus_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmStatus_Object = MibTableColumn
wwpLeosChassisDoorAlarmStatus = _WwpLeosChassisDoorAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 2),
    _WwpLeosChassisDoorAlarmStatus_Type()
)
wwpLeosChassisDoorAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmStatus.setStatus("current")


class _WwpLeosChassisDoorAlarmAdminStatus_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmAdminStatus based on Integer32"""
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


_WwpLeosChassisDoorAlarmAdminStatus_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmAdminStatus_Object = MibTableColumn
wwpLeosChassisDoorAlarmAdminStatus = _WwpLeosChassisDoorAlarmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 3),
    _WwpLeosChassisDoorAlarmAdminStatus_Type()
)
wwpLeosChassisDoorAlarmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmAdminStatus.setStatus("current")


class _WwpLeosChassisDoorAlarmFlapDetect_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmFlapDetect based on Integer32"""
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


_WwpLeosChassisDoorAlarmFlapDetect_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmFlapDetect_Object = MibTableColumn
wwpLeosChassisDoorAlarmFlapDetect = _WwpLeosChassisDoorAlarmFlapDetect_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 4),
    _WwpLeosChassisDoorAlarmFlapDetect_Type()
)
wwpLeosChassisDoorAlarmFlapDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmFlapDetect.setStatus("current")


class _WwpLeosChassisDoorAlarmFlapCount_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmFlapCount based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_WwpLeosChassisDoorAlarmFlapCount_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmFlapCount_Object = MibTableColumn
wwpLeosChassisDoorAlarmFlapCount = _WwpLeosChassisDoorAlarmFlapCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 5),
    _WwpLeosChassisDoorAlarmFlapCount_Type()
)
wwpLeosChassisDoorAlarmFlapCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmFlapCount.setStatus("current")


class _WwpLeosChassisDoorAlarmFlapDetectTime_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmFlapDetectTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_WwpLeosChassisDoorAlarmFlapDetectTime_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmFlapDetectTime_Object = MibTableColumn
wwpLeosChassisDoorAlarmFlapDetectTime = _WwpLeosChassisDoorAlarmFlapDetectTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 6),
    _WwpLeosChassisDoorAlarmFlapDetectTime_Type()
)
wwpLeosChassisDoorAlarmFlapDetectTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmFlapDetectTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmFlapDetectTime.setUnits("seconds")


class _WwpLeosChassisDoorAlarmFlapHoldTime_Type(Integer32):
    """Custom type wwpLeosChassisDoorAlarmFlapHoldTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 3600),
    )


_WwpLeosChassisDoorAlarmFlapHoldTime_Type.__name__ = "Integer32"
_WwpLeosChassisDoorAlarmFlapHoldTime_Object = MibTableColumn
wwpLeosChassisDoorAlarmFlapHoldTime = _WwpLeosChassisDoorAlarmFlapHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 64, 1, 7),
    _WwpLeosChassisDoorAlarmFlapHoldTime_Type()
)
wwpLeosChassisDoorAlarmFlapHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmFlapHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmFlapHoldTime.setUnits("seconds")
_WwpLeosSystemPartNumber_Type = DisplayString
_WwpLeosSystemPartNumber_Object = MibScalar
wwpLeosSystemPartNumber = _WwpLeosSystemPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 66),
    _WwpLeosSystemPartNumber_Type()
)
wwpLeosSystemPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemPartNumber.setStatus("current")
_WwpLeosSystemSerialNumber_Type = DisplayString
_WwpLeosSystemSerialNumber_Object = MibScalar
wwpLeosSystemSerialNumber = _WwpLeosSystemSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 1, 67),
    _WwpLeosSystemSerialNumber_Type()
)
wwpLeosSystemSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosSystemSerialNumber.setStatus("current")
_WwpLeosChassisBatteryModule_ObjectIdentity = ObjectIdentity
wwpLeosChassisBatteryModule = _WwpLeosChassisBatteryModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2)
)


class _WwpLeosChassisBatteryStatus_Type(Integer32):
    """Custom type wwpLeosChassisBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("missing", 2),
          ("online", 0),
          ("present", 1))
    )


_WwpLeosChassisBatteryStatus_Type.__name__ = "Integer32"
_WwpLeosChassisBatteryStatus_Object = MibScalar
wwpLeosChassisBatteryStatus = _WwpLeosChassisBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 1),
    _WwpLeosChassisBatteryStatus_Type()
)
wwpLeosChassisBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryStatus.setStatus("current")


class _WwpLeosChassisBatteryVoltageLevel_Type(Integer32):
    """Custom type wwpLeosChassisBatteryVoltageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 2),
          ("normal", 1),
          ("unknown", 0))
    )


_WwpLeosChassisBatteryVoltageLevel_Type.__name__ = "Integer32"
_WwpLeosChassisBatteryVoltageLevel_Object = MibScalar
wwpLeosChassisBatteryVoltageLevel = _WwpLeosChassisBatteryVoltageLevel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 2),
    _WwpLeosChassisBatteryVoltageLevel_Type()
)
wwpLeosChassisBatteryVoltageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryVoltageLevel.setStatus("current")


class _WwpLeosChassisBatteryCondition_Type(Integer32):
    """Custom type wwpLeosChassisBatteryCondition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("good", 1),
          ("unknown", 0))
    )


_WwpLeosChassisBatteryCondition_Type.__name__ = "Integer32"
_WwpLeosChassisBatteryCondition_Object = MibScalar
wwpLeosChassisBatteryCondition = _WwpLeosChassisBatteryCondition_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 3),
    _WwpLeosChassisBatteryCondition_Type()
)
wwpLeosChassisBatteryCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryCondition.setStatus("current")


class _WwpLeosChassisPowerSource_Type(Integer32):
    """Custom type wwpLeosChassisPowerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("battery", 2),
          ("primaryPower", 1))
    )


_WwpLeosChassisPowerSource_Type.__name__ = "Integer32"
_WwpLeosChassisPowerSource_Object = MibScalar
wwpLeosChassisPowerSource = _WwpLeosChassisPowerSource_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 4),
    _WwpLeosChassisPowerSource_Type()
)
wwpLeosChassisPowerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSource.setStatus("current")


class _WwpLeosChassisBatteryNormalStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryNormalStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryNormalStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryNormalStateName_Object = MibScalar
wwpLeosChassisBatteryNormalStateName = _WwpLeosChassisBatteryNormalStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 5),
    _WwpLeosChassisBatteryNormalStateName_Type()
)
wwpLeosChassisBatteryNormalStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryNormalStateName.setStatus("current")


class _WwpLeosChassisBatteryLowStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryLowStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryLowStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryLowStateName_Object = MibScalar
wwpLeosChassisBatteryLowStateName = _WwpLeosChassisBatteryLowStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 6),
    _WwpLeosChassisBatteryLowStateName_Type()
)
wwpLeosChassisBatteryLowStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryLowStateName.setStatus("current")


class _WwpLeosChassisBatteryGoodStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryGoodStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryGoodStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryGoodStateName_Object = MibScalar
wwpLeosChassisBatteryGoodStateName = _WwpLeosChassisBatteryGoodStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 7),
    _WwpLeosChassisBatteryGoodStateName_Type()
)
wwpLeosChassisBatteryGoodStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryGoodStateName.setStatus("current")


class _WwpLeosChassisBatteryBadStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryBadStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryBadStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryBadStateName_Object = MibScalar
wwpLeosChassisBatteryBadStateName = _WwpLeosChassisBatteryBadStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 8),
    _WwpLeosChassisBatteryBadStateName_Type()
)
wwpLeosChassisBatteryBadStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryBadStateName.setStatus("current")


class _WwpLeosChassisBatteryPresentStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryPresentStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryPresentStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryPresentStateName_Object = MibScalar
wwpLeosChassisBatteryPresentStateName = _WwpLeosChassisBatteryPresentStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 9),
    _WwpLeosChassisBatteryPresentStateName_Type()
)
wwpLeosChassisBatteryPresentStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryPresentStateName.setStatus("current")


class _WwpLeosChassisBatteryMissingStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryMissingStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryMissingStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryMissingStateName_Object = MibScalar
wwpLeosChassisBatteryMissingStateName = _WwpLeosChassisBatteryMissingStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 10),
    _WwpLeosChassisBatteryMissingStateName_Type()
)
wwpLeosChassisBatteryMissingStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryMissingStateName.setStatus("current")


class _WwpLeosChassisBatteryPowerPrimaryStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryPowerPrimaryStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryPowerPrimaryStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryPowerPrimaryStateName_Object = MibScalar
wwpLeosChassisBatteryPowerPrimaryStateName = _WwpLeosChassisBatteryPowerPrimaryStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 11),
    _WwpLeosChassisBatteryPowerPrimaryStateName_Type()
)
wwpLeosChassisBatteryPowerPrimaryStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryPowerPrimaryStateName.setStatus("current")


class _WwpLeosChassisBatteryPowerBatteryStateName_Type(OctetString):
    """Custom type wwpLeosChassisBatteryPowerBatteryStateName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_WwpLeosChassisBatteryPowerBatteryStateName_Type.__name__ = "OctetString"
_WwpLeosChassisBatteryPowerBatteryStateName_Object = MibScalar
wwpLeosChassisBatteryPowerBatteryStateName = _WwpLeosChassisBatteryPowerBatteryStateName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 12),
    _WwpLeosChassisBatteryPowerBatteryStateName_Type()
)
wwpLeosChassisBatteryPowerBatteryStateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryPowerBatteryStateName.setStatus("current")


class _WwpLeosChassisBatteryLowStateNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisBatteryLowStateNotifEnabled based on TruthValue"""


_WwpLeosChassisBatteryLowStateNotifEnabled_Object = MibScalar
wwpLeosChassisBatteryLowStateNotifEnabled = _WwpLeosChassisBatteryLowStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 13),
    _WwpLeosChassisBatteryLowStateNotifEnabled_Type()
)
wwpLeosChassisBatteryLowStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryLowStateNotifEnabled.setStatus("current")


class _WwpLeosChassisBatteryBadStateNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisBatteryBadStateNotifEnabled based on TruthValue"""


_WwpLeosChassisBatteryBadStateNotifEnabled_Object = MibScalar
wwpLeosChassisBatteryBadStateNotifEnabled = _WwpLeosChassisBatteryBadStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 14),
    _WwpLeosChassisBatteryBadStateNotifEnabled_Type()
)
wwpLeosChassisBatteryBadStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryBadStateNotifEnabled.setStatus("current")


class _WwpLeosChassisBatteryMissingStateNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisBatteryMissingStateNotifEnabled based on TruthValue"""


_WwpLeosChassisBatteryMissingStateNotifEnabled_Object = MibScalar
wwpLeosChassisBatteryMissingStateNotifEnabled = _WwpLeosChassisBatteryMissingStateNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 15),
    _WwpLeosChassisBatteryMissingStateNotifEnabled_Type()
)
wwpLeosChassisBatteryMissingStateNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryMissingStateNotifEnabled.setStatus("current")


class _WwpLeosChassisBatteryPowerNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisBatteryPowerNotifEnabled based on TruthValue"""


_WwpLeosChassisBatteryPowerNotifEnabled_Object = MibScalar
wwpLeosChassisBatteryPowerNotifEnabled = _WwpLeosChassisBatteryPowerNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 2, 16),
    _WwpLeosChassisBatteryPowerNotifEnabled_Type()
)
wwpLeosChassisBatteryPowerNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryPowerNotifEnabled.setStatus("current")
_WwpLeosChassisPowerSupplyModule_ObjectIdentity = ObjectIdentity
wwpLeosChassisPowerSupplyModule = _WwpLeosChassisPowerSupplyModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3)
)
_WwpLeosChassisPowerTable_Object = MibTable
wwpLeosChassisPowerTable = _WwpLeosChassisPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosChassisPowerTable.setStatus("current")
_WwpLeosChassisPowerEntry_Object = MibTableRow
wwpLeosChassisPowerEntry = _WwpLeosChassisPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 1, 1)
)
wwpLeosChassisPowerEntry.setIndexNames(
    (0, "WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPowerSupplyNum"),
)
if mibBuilder.loadTexts:
    wwpLeosChassisPowerEntry.setStatus("current")


class _WwpLeosChassisPowerSupplyNum_Type(Integer32):
    """Custom type wwpLeosChassisPowerSupplyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosChassisPowerSupplyNum_Type.__name__ = "Integer32"
_WwpLeosChassisPowerSupplyNum_Object = MibTableColumn
wwpLeosChassisPowerSupplyNum = _WwpLeosChassisPowerSupplyNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 1, 1, 1),
    _WwpLeosChassisPowerSupplyNum_Type()
)
wwpLeosChassisPowerSupplyNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSupplyNum.setStatus("current")


class _WwpLeosChassisPowerSupplyState_Type(Integer32):
    """Custom type wwpLeosChassisPowerSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("faulted", 3),
          ("offline", 2),
          ("online", 1))
    )


_WwpLeosChassisPowerSupplyState_Type.__name__ = "Integer32"
_WwpLeosChassisPowerSupplyState_Object = MibTableColumn
wwpLeosChassisPowerSupplyState = _WwpLeosChassisPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 1, 1, 2),
    _WwpLeosChassisPowerSupplyState_Type()
)
wwpLeosChassisPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSupplyState.setStatus("current")


class _WwpLeosChassisPowerSupplyType_Type(Integer32):
    """Custom type wwpLeosChassisPowerSupplyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ac", 1),
          ("dc", 2),
          ("unequipped", 3))
    )


_WwpLeosChassisPowerSupplyType_Type.__name__ = "Integer32"
_WwpLeosChassisPowerSupplyType_Object = MibTableColumn
wwpLeosChassisPowerSupplyType = _WwpLeosChassisPowerSupplyType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 1, 1, 3),
    _WwpLeosChassisPowerSupplyType_Type()
)
wwpLeosChassisPowerSupplyType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSupplyType.setStatus("current")


class _WwpLeosChassisPowerSupplyRedundantState_Type(Integer32):
    """Custom type wwpLeosChassisPowerSupplyRedundantState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("protected", 1),
          ("unprotected", 2))
    )


_WwpLeosChassisPowerSupplyRedundantState_Type.__name__ = "Integer32"
_WwpLeosChassisPowerSupplyRedundantState_Object = MibTableColumn
wwpLeosChassisPowerSupplyRedundantState = _WwpLeosChassisPowerSupplyRedundantState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 1, 1, 4),
    _WwpLeosChassisPowerSupplyRedundantState_Type()
)
wwpLeosChassisPowerSupplyRedundantState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSupplyRedundantState.setStatus("current")


class _WwpLeosChassisRedPowerSupplyNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisRedPowerSupplyNotifEnabled based on TruthValue"""


_WwpLeosChassisRedPowerSupplyNotifEnabled_Object = MibScalar
wwpLeosChassisRedPowerSupplyNotifEnabled = _WwpLeosChassisRedPowerSupplyNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 3, 2),
    _WwpLeosChassisRedPowerSupplyNotifEnabled_Type()
)
wwpLeosChassisRedPowerSupplyNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisRedPowerSupplyNotifEnabled.setStatus("current")
_WwpLeosChassisFanModule_ObjectIdentity = ObjectIdentity
wwpLeosChassisFanModule = _WwpLeosChassisFanModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4)
)
_WwpLeosChassisFanModuleTable_Object = MibTable
wwpLeosChassisFanModuleTable = _WwpLeosChassisFanModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleTable.setStatus("current")
_WwpLeosChassisFanModuleEntry_Object = MibTableRow
wwpLeosChassisFanModuleEntry = _WwpLeosChassisFanModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1)
)
wwpLeosChassisFanModuleEntry.setIndexNames(
    (0, "WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisFanModuleNum"),
)
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleEntry.setStatus("current")


class _WwpLeosChassisFanModuleNum_Type(Integer32):
    """Custom type wwpLeosChassisFanModuleNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosChassisFanModuleNum_Type.__name__ = "Integer32"
_WwpLeosChassisFanModuleNum_Object = MibTableColumn
wwpLeosChassisFanModuleNum = _WwpLeosChassisFanModuleNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1, 1),
    _WwpLeosChassisFanModuleNum_Type()
)
wwpLeosChassisFanModuleNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleNum.setStatus("current")


class _WwpLeosChassisFanModuleType_Type(Integer32):
    """Custom type wwpLeosChassisFanModuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("hotSwappable", 2),
          ("unequipped", 3))
    )


_WwpLeosChassisFanModuleType_Type.__name__ = "Integer32"
_WwpLeosChassisFanModuleType_Object = MibTableColumn
wwpLeosChassisFanModuleType = _WwpLeosChassisFanModuleType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1, 2),
    _WwpLeosChassisFanModuleType_Type()
)
wwpLeosChassisFanModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleType.setStatus("current")


class _WwpLeosChassisFanModuleStatus_Type(Integer32):
    """Custom type wwpLeosChassisFanModuleStatus based on Integer32"""
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
          ("ok", 1),
          ("pending", 2))
    )


_WwpLeosChassisFanModuleStatus_Type.__name__ = "Integer32"
_WwpLeosChassisFanModuleStatus_Object = MibTableColumn
wwpLeosChassisFanModuleStatus = _WwpLeosChassisFanModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1, 3),
    _WwpLeosChassisFanModuleStatus_Type()
)
wwpLeosChassisFanModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleStatus.setStatus("current")


class _WwpLeosChassisFanAvgSpeed_Type(Integer32):
    """Custom type wwpLeosChassisFanAvgSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosChassisFanAvgSpeed_Type.__name__ = "Integer32"
_WwpLeosChassisFanAvgSpeed_Object = MibTableColumn
wwpLeosChassisFanAvgSpeed = _WwpLeosChassisFanAvgSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1, 4),
    _WwpLeosChassisFanAvgSpeed_Type()
)
wwpLeosChassisFanAvgSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisFanAvgSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisFanAvgSpeed.setUnits("rpm")


class _WwpLeosChassisFanCurrentSpeed_Type(Integer32):
    """Custom type wwpLeosChassisFanCurrentSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosChassisFanCurrentSpeed_Type.__name__ = "Integer32"
_WwpLeosChassisFanCurrentSpeed_Object = MibTableColumn
wwpLeosChassisFanCurrentSpeed = _WwpLeosChassisFanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1, 5),
    _WwpLeosChassisFanCurrentSpeed_Type()
)
wwpLeosChassisFanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisFanCurrentSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisFanCurrentSpeed.setUnits("rpm")


class _WwpLeosChassisFanMinSpeed_Type(Integer32):
    """Custom type wwpLeosChassisFanMinSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WwpLeosChassisFanMinSpeed_Type.__name__ = "Integer32"
_WwpLeosChassisFanMinSpeed_Object = MibTableColumn
wwpLeosChassisFanMinSpeed = _WwpLeosChassisFanMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 1, 1, 6),
    _WwpLeosChassisFanMinSpeed_Type()
)
wwpLeosChassisFanMinSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisFanMinSpeed.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisFanMinSpeed.setUnits("rpm")


class _WwpLeosChassisFanModuleNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisFanModuleNotifEnabled based on TruthValue"""


_WwpLeosChassisFanModuleNotifEnabled_Object = MibScalar
wwpLeosChassisFanModuleNotifEnabled = _WwpLeosChassisFanModuleNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 4, 2),
    _WwpLeosChassisFanModuleNotifEnabled_Type()
)
wwpLeosChassisFanModuleNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleNotifEnabled.setStatus("current")
_WwpLeosChassisTempSensor_ObjectIdentity = ObjectIdentity
wwpLeosChassisTempSensor = _WwpLeosChassisTempSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5)
)
_WwpLeosChassisTempSensorTable_Object = MibTable
wwpLeosChassisTempSensorTable = _WwpLeosChassisTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorTable.setStatus("current")
_WwpLeosChassisTempSensorEntry_Object = MibTableRow
wwpLeosChassisTempSensorEntry = _WwpLeosChassisTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1, 1)
)
wwpLeosChassisTempSensorEntry.setIndexNames(
    (0, "WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisTempSensorNum"),
)
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorEntry.setStatus("current")


class _WwpLeosChassisTempSensorNum_Type(Integer32):
    """Custom type wwpLeosChassisTempSensorNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_WwpLeosChassisTempSensorNum_Type.__name__ = "Integer32"
_WwpLeosChassisTempSensorNum_Object = MibTableColumn
wwpLeosChassisTempSensorNum = _WwpLeosChassisTempSensorNum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1, 1, 1),
    _WwpLeosChassisTempSensorNum_Type()
)
wwpLeosChassisTempSensorNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorNum.setStatus("current")
_WwpLeosChassisTempSensorValue_Type = Integer32
_WwpLeosChassisTempSensorValue_Object = MibTableColumn
wwpLeosChassisTempSensorValue = _WwpLeosChassisTempSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1, 1, 2),
    _WwpLeosChassisTempSensorValue_Type()
)
wwpLeosChassisTempSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorValue.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorValue.setUnits("degrees Celsius")
_WwpLeosChassisTempSensorHighThreshold_Type = Integer32
_WwpLeosChassisTempSensorHighThreshold_Object = MibTableColumn
wwpLeosChassisTempSensorHighThreshold = _WwpLeosChassisTempSensorHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1, 1, 3),
    _WwpLeosChassisTempSensorHighThreshold_Type()
)
wwpLeosChassisTempSensorHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorHighThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorHighThreshold.setUnits("degrees Celsius")
_WwpLeosChassisTempSensorLowThreshold_Type = Integer32
_WwpLeosChassisTempSensorLowThreshold_Object = MibTableColumn
wwpLeosChassisTempSensorLowThreshold = _WwpLeosChassisTempSensorLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1, 1, 4),
    _WwpLeosChassisTempSensorLowThreshold_Type()
)
wwpLeosChassisTempSensorLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorLowThreshold.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorLowThreshold.setUnits("degrees Celsius")


class _WwpLeosChassisTempSensorState_Type(Integer32):
    """Custom type wwpLeosChassisTempSensorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("higherThanThreshold", 0),
          ("lowerThanThreshold", 2),
          ("normal", 1))
    )


_WwpLeosChassisTempSensorState_Type.__name__ = "Integer32"
_WwpLeosChassisTempSensorState_Object = MibTableColumn
wwpLeosChassisTempSensorState = _WwpLeosChassisTempSensorState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 1, 1, 5),
    _WwpLeosChassisTempSensorState_Type()
)
wwpLeosChassisTempSensorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisTempSensorState.setStatus("current")


class _WwpLeosChassisTempNotifEnabled_Type(TruthValue):
    """Custom type wwpLeosChassisTempNotifEnabled based on TruthValue"""


_WwpLeosChassisTempNotifEnabled_Object = MibScalar
wwpLeosChassisTempNotifEnabled = _WwpLeosChassisTempNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 2),
    _WwpLeosChassisTempNotifEnabled_Type()
)
wwpLeosChassisTempNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisTempNotifEnabled.setStatus("current")
_WwpLeosChassisTempHighThreshold_Type = Integer32
_WwpLeosChassisTempHighThreshold_Object = MibScalar
wwpLeosChassisTempHighThreshold = _WwpLeosChassisTempHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 3),
    _WwpLeosChassisTempHighThreshold_Type()
)
wwpLeosChassisTempHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisTempHighThreshold.setStatus("current")
_WwpLeosChassisTempLowThreshold_Type = Integer32
_WwpLeosChassisTempLowThreshold_Object = MibScalar
wwpLeosChassisTempLowThreshold = _WwpLeosChassisTempLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 5, 4),
    _WwpLeosChassisTempLowThreshold_Type()
)
wwpLeosChassisTempLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosChassisTempLowThreshold.setStatus("current")
_WwpLeosChassisNotif_ObjectIdentity = ObjectIdentity
wwpLeosChassisNotif = _WwpLeosChassisNotif_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 7)
)


class _WwpPowerSwitchingOp_Type(Integer32):
    """Custom type wwpPowerSwitchingOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("acToBattery", 1),
          ("bateryToAC", 2),
          ("none", 0))
    )


_WwpPowerSwitchingOp_Type.__name__ = "Integer32"
_WwpPowerSwitchingOp_Object = MibScalar
wwpPowerSwitchingOp = _WwpPowerSwitchingOp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 7, 1),
    _WwpPowerSwitchingOp_Type()
)
wwpPowerSwitchingOp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpPowerSwitchingOp.setStatus("current")
_WwpLeosChassisPlatformCaps_ObjectIdentity = ObjectIdentity
wwpLeosChassisPlatformCaps = _WwpLeosChassisPlatformCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8)
)


class _WwpLeosChassisPlatformCapsMaxPhysPorts_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxPhysPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_WwpLeosChassisPlatformCapsMaxPhysPorts_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxPhysPorts_Object = MibScalar
wwpLeosChassisPlatformCapsMaxPhysPorts = _WwpLeosChassisPlatformCapsMaxPhysPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 1),
    _WwpLeosChassisPlatformCapsMaxPhysPorts_Type()
)
wwpLeosChassisPlatformCapsMaxPhysPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxPhysPorts.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxAggrPorts_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxAggrPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WwpLeosChassisPlatformCapsMaxAggrPorts_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxAggrPorts_Object = MibScalar
wwpLeosChassisPlatformCapsMaxAggrPorts = _WwpLeosChassisPlatformCapsMaxAggrPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 2),
    _WwpLeosChassisPlatformCapsMaxAggrPorts_Type()
)
wwpLeosChassisPlatformCapsMaxAggrPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxAggrPorts.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxVlans_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxVlans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4064),
    )


_WwpLeosChassisPlatformCapsMaxVlans_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxVlans_Object = MibScalar
wwpLeosChassisPlatformCapsMaxVlans = _WwpLeosChassisPlatformCapsMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 3),
    _WwpLeosChassisPlatformCapsMaxVlans_Type()
)
wwpLeosChassisPlatformCapsMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxVlans.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Object = MibScalar
wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans = _WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 4),
    _WwpLeosChassisPlatformCapsMaxIgmpSnoopVlans_Type()
)
wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxMulticastgroups_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxMulticastgroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WwpLeosChassisPlatformCapsMaxMulticastgroups_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxMulticastgroups_Object = MibScalar
wwpLeosChassisPlatformCapsMaxMulticastgroups = _WwpLeosChassisPlatformCapsMaxMulticastgroups_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 5),
    _WwpLeosChassisPlatformCapsMaxMulticastgroups_Type()
)
wwpLeosChassisPlatformCapsMaxMulticastgroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxMulticastgroups.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxRstpDomains_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxRstpDomains based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WwpLeosChassisPlatformCapsMaxRstpDomains_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxRstpDomains_Object = MibScalar
wwpLeosChassisPlatformCapsMaxRstpDomains = _WwpLeosChassisPlatformCapsMaxRstpDomains_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 6),
    _WwpLeosChassisPlatformCapsMaxRstpDomains_Type()
)
wwpLeosChassisPlatformCapsMaxRstpDomains.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxRstpDomains.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxTunnels_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxTunnels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisPlatformCapsMaxTunnels_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxTunnels_Object = MibScalar
wwpLeosChassisPlatformCapsMaxTunnels = _WwpLeosChassisPlatformCapsMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 7),
    _WwpLeosChassisPlatformCapsMaxTunnels_Type()
)
wwpLeosChassisPlatformCapsMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxTunnels.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxIngressTunnels_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxIngressTunnels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisPlatformCapsMaxIngressTunnels_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxIngressTunnels_Object = MibScalar
wwpLeosChassisPlatformCapsMaxIngressTunnels = _WwpLeosChassisPlatformCapsMaxIngressTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 8),
    _WwpLeosChassisPlatformCapsMaxIngressTunnels_Type()
)
wwpLeosChassisPlatformCapsMaxIngressTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxIngressTunnels.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxEgressTunnels_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxEgressTunnels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisPlatformCapsMaxEgressTunnels_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxEgressTunnels_Object = MibScalar
wwpLeosChassisPlatformCapsMaxEgressTunnels = _WwpLeosChassisPlatformCapsMaxEgressTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 9),
    _WwpLeosChassisPlatformCapsMaxEgressTunnels_Type()
)
wwpLeosChassisPlatformCapsMaxEgressTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxEgressTunnels.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxVcs_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxVcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WwpLeosChassisPlatformCapsMaxVcs_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxVcs_Object = MibScalar
wwpLeosChassisPlatformCapsMaxVcs = _WwpLeosChassisPlatformCapsMaxVcs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 10),
    _WwpLeosChassisPlatformCapsMaxVcs_Type()
)
wwpLeosChassisPlatformCapsMaxVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxVcs.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxVss_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxVss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WwpLeosChassisPlatformCapsMaxVss_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxVss_Object = MibScalar
wwpLeosChassisPlatformCapsMaxVss = _WwpLeosChassisPlatformCapsMaxVss_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 11),
    _WwpLeosChassisPlatformCapsMaxVss_Type()
)
wwpLeosChassisPlatformCapsMaxVss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxVss.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxVsMembers_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxVsMembers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5334),
    )


_WwpLeosChassisPlatformCapsMaxVsMembers_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxVsMembers_Object = MibScalar
wwpLeosChassisPlatformCapsMaxVsMembers = _WwpLeosChassisPlatformCapsMaxVsMembers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 12),
    _WwpLeosChassisPlatformCapsMaxVsMembers_Type()
)
wwpLeosChassisPlatformCapsMaxVsMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxVsMembers.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxLearnedMacs_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxLearnedMacs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_WwpLeosChassisPlatformCapsMaxLearnedMacs_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxLearnedMacs_Object = MibScalar
wwpLeosChassisPlatformCapsMaxLearnedMacs = _WwpLeosChassisPlatformCapsMaxLearnedMacs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 13),
    _WwpLeosChassisPlatformCapsMaxLearnedMacs_Type()
)
wwpLeosChassisPlatformCapsMaxLearnedMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxLearnedMacs.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxFsmtEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxFsmtEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 140),
    )


_WwpLeosChassisPlatformCapsMaxFsmtEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxFsmtEntries_Object = MibScalar
wwpLeosChassisPlatformCapsMaxFsmtEntries = _WwpLeosChassisPlatformCapsMaxFsmtEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 14),
    _WwpLeosChassisPlatformCapsMaxFsmtEntries_Type()
)
wwpLeosChassisPlatformCapsMaxFsmtEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxFsmtEntries.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxFsmtCosEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Object = MibScalar
wwpLeosChassisPlatformCapsMaxFsmtCosEntries = _WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 15),
    _WwpLeosChassisPlatformCapsMaxFsmtCosEntries_Type()
)
wwpLeosChassisPlatformCapsMaxFsmtCosEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxFsmtCosEntries.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxL4ProtEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxL4ProtEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_WwpLeosChassisPlatformCapsMaxL4ProtEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxL4ProtEntries_Object = MibScalar
wwpLeosChassisPlatformCapsMaxL4ProtEntries = _WwpLeosChassisPlatformCapsMaxL4ProtEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 16),
    _WwpLeosChassisPlatformCapsMaxL4ProtEntries_Type()
)
wwpLeosChassisPlatformCapsMaxL4ProtEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxL4ProtEntries.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxSltEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxSltEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WwpLeosChassisPlatformCapsMaxSltEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxSltEntries_Object = MibScalar
wwpLeosChassisPlatformCapsMaxSltEntries = _WwpLeosChassisPlatformCapsMaxSltEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 17),
    _WwpLeosChassisPlatformCapsMaxSltEntries_Type()
)
wwpLeosChassisPlatformCapsMaxSltEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxSltEntries.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxSactEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxSactEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2074),
    )


_WwpLeosChassisPlatformCapsMaxSactEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxSactEntries_Object = MibScalar
wwpLeosChassisPlatformCapsMaxSactEntries = _WwpLeosChassisPlatformCapsMaxSactEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 18),
    _WwpLeosChassisPlatformCapsMaxSactEntries_Type()
)
wwpLeosChassisPlatformCapsMaxSactEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxSactEntries.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxSmtEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxSmtEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WwpLeosChassisPlatformCapsMaxSmtEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxSmtEntries_Object = MibScalar
wwpLeosChassisPlatformCapsMaxSmtEntries = _WwpLeosChassisPlatformCapsMaxSmtEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 19),
    _WwpLeosChassisPlatformCapsMaxSmtEntries_Type()
)
wwpLeosChassisPlatformCapsMaxSmtEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxSmtEntries.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxEprSnids_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxEprSnids based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WwpLeosChassisPlatformCapsMaxEprSnids_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxEprSnids_Object = MibScalar
wwpLeosChassisPlatformCapsMaxEprSnids = _WwpLeosChassisPlatformCapsMaxEprSnids_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 20),
    _WwpLeosChassisPlatformCapsMaxEprSnids_Type()
)
wwpLeosChassisPlatformCapsMaxEprSnids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxEprSnids.setStatus("current")


class _WwpLeosChassisPlatformCapsMaxSltWildcards_Type(Unsigned32):
    """Custom type wwpLeosChassisPlatformCapsMaxSltWildcards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosChassisPlatformCapsMaxSltWildcards_Type.__name__ = "Unsigned32"
_WwpLeosChassisPlatformCapsMaxSltWildcards_Object = MibScalar
wwpLeosChassisPlatformCapsMaxSltWildcards = _WwpLeosChassisPlatformCapsMaxSltWildcards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 21),
    _WwpLeosChassisPlatformCapsMaxSltWildcards_Type()
)
wwpLeosChassisPlatformCapsMaxSltWildcards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMaxSltWildcards.setStatus("current")
_WwpLeosChassisPlatformCapsVlanTranslation_Type = TruthValue
_WwpLeosChassisPlatformCapsVlanTranslation_Object = MibScalar
wwpLeosChassisPlatformCapsVlanTranslation = _WwpLeosChassisPlatformCapsVlanTranslation_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 22),
    _WwpLeosChassisPlatformCapsVlanTranslation_Type()
)
wwpLeosChassisPlatformCapsVlanTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsVlanTranslation.setStatus("current")
_WwpLeosChassisPlatformCapsProtocolFilters_Type = TruthValue
_WwpLeosChassisPlatformCapsProtocolFilters_Object = MibScalar
wwpLeosChassisPlatformCapsProtocolFilters = _WwpLeosChassisPlatformCapsProtocolFilters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 23),
    _WwpLeosChassisPlatformCapsProtocolFilters_Type()
)
wwpLeosChassisPlatformCapsProtocolFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsProtocolFilters.setStatus("current")
_WwpLeosChassisPlatformCapsMultiSubsPerPort_Type = TruthValue
_WwpLeosChassisPlatformCapsMultiSubsPerPort_Object = MibScalar
wwpLeosChassisPlatformCapsMultiSubsPerPort = _WwpLeosChassisPlatformCapsMultiSubsPerPort_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 24),
    _WwpLeosChassisPlatformCapsMultiSubsPerPort_Type()
)
wwpLeosChassisPlatformCapsMultiSubsPerPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsMultiSubsPerPort.setStatus("current")
_WwpLeosChassisPlatformCapsVplsFpga_Type = TruthValue
_WwpLeosChassisPlatformCapsVplsFpga_Object = MibScalar
wwpLeosChassisPlatformCapsVplsFpga = _WwpLeosChassisPlatformCapsVplsFpga_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 25),
    _WwpLeosChassisPlatformCapsVplsFpga_Type()
)
wwpLeosChassisPlatformCapsVplsFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsVplsFpga.setStatus("current")
_WwpLeosChassisPlatformCapsPbtFpga_Type = TruthValue
_WwpLeosChassisPlatformCapsPbtFpga_Object = MibScalar
wwpLeosChassisPlatformCapsPbtFpga = _WwpLeosChassisPlatformCapsPbtFpga_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 26),
    _WwpLeosChassisPlatformCapsPbtFpga_Type()
)
wwpLeosChassisPlatformCapsPbtFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsPbtFpga.setStatus("current")
_WwpLeosChassisPlatformCapsAoamFpga_Type = TruthValue
_WwpLeosChassisPlatformCapsAoamFpga_Object = MibScalar
wwpLeosChassisPlatformCapsAoamFpga = _WwpLeosChassisPlatformCapsAoamFpga_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 27),
    _WwpLeosChassisPlatformCapsAoamFpga_Type()
)
wwpLeosChassisPlatformCapsAoamFpga.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsAoamFpga.setStatus("current")
_WwpLeosChassisPlatformCapsDcPower_Type = TruthValue
_WwpLeosChassisPlatformCapsDcPower_Object = MibScalar
wwpLeosChassisPlatformCapsDcPower = _WwpLeosChassisPlatformCapsDcPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 29),
    _WwpLeosChassisPlatformCapsDcPower_Type()
)
wwpLeosChassisPlatformCapsDcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsDcPower.setStatus("current")
_WwpLeosChassisPlatformCapsAcPower_Type = TruthValue
_WwpLeosChassisPlatformCapsAcPower_Object = MibScalar
wwpLeosChassisPlatformCapsAcPower = _WwpLeosChassisPlatformCapsAcPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 30),
    _WwpLeosChassisPlatformCapsAcPower_Type()
)
wwpLeosChassisPlatformCapsAcPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsAcPower.setStatus("current")
_WwpLeosChassisPlatformCapsRedunPower_Type = TruthValue
_WwpLeosChassisPlatformCapsRedunPower_Object = MibScalar
wwpLeosChassisPlatformCapsRedunPower = _WwpLeosChassisPlatformCapsRedunPower_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 8, 31),
    _WwpLeosChassisPlatformCapsRedunPower_Type()
)
wwpLeosChassisPlatformCapsRedunPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisPlatformCapsRedunPower.setStatus("current")
_WwpLeosChassisResourceCounts_ObjectIdentity = ObjectIdentity
wwpLeosChassisResourceCounts = _WwpLeosChassisResourceCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9)
)


class _WwpLeosChassisResourcesMaxPorts_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_WwpLeosChassisResourcesMaxPorts_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxPorts_Object = MibScalar
wwpLeosChassisResourcesMaxPorts = _WwpLeosChassisResourcesMaxPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 1),
    _WwpLeosChassisResourcesMaxPorts_Type()
)
wwpLeosChassisResourcesMaxPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxPorts.setStatus("current")


class _WwpLeosChassisResourcesFreePorts_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreePorts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 28),
    )


_WwpLeosChassisResourcesFreePorts_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreePorts_Object = MibScalar
wwpLeosChassisResourcesFreePorts = _WwpLeosChassisResourcesFreePorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 2),
    _WwpLeosChassisResourcesFreePorts_Type()
)
wwpLeosChassisResourcesFreePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreePorts.setStatus("current")


class _WwpLeosChassisResourcesMaxAggrPorts_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxAggrPorts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WwpLeosChassisResourcesMaxAggrPorts_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxAggrPorts_Object = MibScalar
wwpLeosChassisResourcesMaxAggrPorts = _WwpLeosChassisResourcesMaxAggrPorts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 3),
    _WwpLeosChassisResourcesMaxAggrPorts_Type()
)
wwpLeosChassisResourcesMaxAggrPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxAggrPorts.setStatus("current")


class _WwpLeosChassisResourcesFreeAggrs_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeAggrs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14),
    )


_WwpLeosChassisResourcesFreeAggrs_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeAggrs_Object = MibScalar
wwpLeosChassisResourcesFreeAggrs = _WwpLeosChassisResourcesFreeAggrs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 4),
    _WwpLeosChassisResourcesFreeAggrs_Type()
)
wwpLeosChassisResourcesFreeAggrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeAggrs.setStatus("current")


class _WwpLeosChassisResourcesMaxPortStateGrps_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxPortStateGrps based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_WwpLeosChassisResourcesMaxPortStateGrps_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxPortStateGrps_Object = MibScalar
wwpLeosChassisResourcesMaxPortStateGrps = _WwpLeosChassisResourcesMaxPortStateGrps_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 5),
    _WwpLeosChassisResourcesMaxPortStateGrps_Type()
)
wwpLeosChassisResourcesMaxPortStateGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxPortStateGrps.setStatus("current")


class _WwpLeosChassisResourcesFreePortStateGrps_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreePortStateGrps based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 21),
    )


_WwpLeosChassisResourcesFreePortStateGrps_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreePortStateGrps_Object = MibScalar
wwpLeosChassisResourcesFreePortStateGrps = _WwpLeosChassisResourcesFreePortStateGrps_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 6),
    _WwpLeosChassisResourcesFreePortStateGrps_Type()
)
wwpLeosChassisResourcesFreePortStateGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreePortStateGrps.setStatus("current")


class _WwpLeosChassisResourcesMaxVlans_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxVlans based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4064),
    )


_WwpLeosChassisResourcesMaxVlans_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxVlans_Object = MibScalar
wwpLeosChassisResourcesMaxVlans = _WwpLeosChassisResourcesMaxVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 7),
    _WwpLeosChassisResourcesMaxVlans_Type()
)
wwpLeosChassisResourcesMaxVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxVlans.setStatus("current")


class _WwpLeosChassisResourcesFreeVlans_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeVlans based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4064),
    )


_WwpLeosChassisResourcesFreeVlans_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeVlans_Object = MibScalar
wwpLeosChassisResourcesFreeVlans = _WwpLeosChassisResourcesFreeVlans_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 8),
    _WwpLeosChassisResourcesFreeVlans_Type()
)
wwpLeosChassisResourcesFreeVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeVlans.setStatus("current")


class _WwpLeosChassisResourcesMaxVlanMembers_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxVlanMembers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 170688),
    )


_WwpLeosChassisResourcesMaxVlanMembers_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxVlanMembers_Object = MibScalar
wwpLeosChassisResourcesMaxVlanMembers = _WwpLeosChassisResourcesMaxVlanMembers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 9),
    _WwpLeosChassisResourcesMaxVlanMembers_Type()
)
wwpLeosChassisResourcesMaxVlanMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxVlanMembers.setStatus("current")


class _WwpLeosChassisResourcesFreeVlanMembers_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeVlanMembers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 170688),
    )


_WwpLeosChassisResourcesFreeVlanMembers_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeVlanMembers_Object = MibScalar
wwpLeosChassisResourcesFreeVlanMembers = _WwpLeosChassisResourcesFreeVlanMembers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 10),
    _WwpLeosChassisResourcesFreeVlanMembers_Type()
)
wwpLeosChassisResourcesFreeVlanMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeVlanMembers.setStatus("current")


class _WwpLeosChassisResourcesMaxEprSnets_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxEprSnets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WwpLeosChassisResourcesMaxEprSnets_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxEprSnets_Object = MibScalar
wwpLeosChassisResourcesMaxEprSnets = _WwpLeosChassisResourcesMaxEprSnets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 11),
    _WwpLeosChassisResourcesMaxEprSnets_Type()
)
wwpLeosChassisResourcesMaxEprSnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxEprSnets.setStatus("current")


class _WwpLeosChassisResourcesFreeEprSnets_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeEprSnets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_WwpLeosChassisResourcesFreeEprSnets_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeEprSnets_Object = MibScalar
wwpLeosChassisResourcesFreeEprSnets = _WwpLeosChassisResourcesFreeEprSnets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 12),
    _WwpLeosChassisResourcesFreeEprSnets_Type()
)
wwpLeosChassisResourcesFreeEprSnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeEprSnets.setStatus("current")


class _WwpLeosChassisResourcesMaxMcastSnets_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxMcastSnets based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesMaxMcastSnets_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxMcastSnets_Object = MibScalar
wwpLeosChassisResourcesMaxMcastSnets = _WwpLeosChassisResourcesMaxMcastSnets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 13),
    _WwpLeosChassisResourcesMaxMcastSnets_Type()
)
wwpLeosChassisResourcesMaxMcastSnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxMcastSnets.setStatus("current")


class _WwpLeosChassisResourcesFreeMcastSnets_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeMcastSnets based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesFreeMcastSnets_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeMcastSnets_Object = MibScalar
wwpLeosChassisResourcesFreeMcastSnets = _WwpLeosChassisResourcesFreeMcastSnets_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 14),
    _WwpLeosChassisResourcesFreeMcastSnets_Type()
)
wwpLeosChassisResourcesFreeMcastSnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeMcastSnets.setStatus("current")


class _WwpLeosChassisResourcesMaxMcastGroups_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxMcastGroups based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WwpLeosChassisResourcesMaxMcastGroups_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxMcastGroups_Object = MibScalar
wwpLeosChassisResourcesMaxMcastGroups = _WwpLeosChassisResourcesMaxMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 15),
    _WwpLeosChassisResourcesMaxMcastGroups_Type()
)
wwpLeosChassisResourcesMaxMcastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxMcastGroups.setStatus("current")


class _WwpLeosChassisResourcesFreeMcastGroups_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeMcastGroups based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WwpLeosChassisResourcesFreeMcastGroups_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeMcastGroups_Object = MibScalar
wwpLeosChassisResourcesFreeMcastGroups = _WwpLeosChassisResourcesFreeMcastGroups_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 16),
    _WwpLeosChassisResourcesFreeMcastGroups_Type()
)
wwpLeosChassisResourcesFreeMcastGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeMcastGroups.setStatus("current")


class _WwpLeosChassisResourcesMaxDhcpRelayAgnts_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxDhcpRelayAgnts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WwpLeosChassisResourcesMaxDhcpRelayAgnts_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxDhcpRelayAgnts_Object = MibScalar
wwpLeosChassisResourcesMaxDhcpRelayAgnts = _WwpLeosChassisResourcesMaxDhcpRelayAgnts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 17),
    _WwpLeosChassisResourcesMaxDhcpRelayAgnts_Type()
)
wwpLeosChassisResourcesMaxDhcpRelayAgnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxDhcpRelayAgnts.setStatus("current")


class _WwpLeosChassisResourcesFreeDhcpRelayAgnts_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeDhcpRelayAgnts based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WwpLeosChassisResourcesFreeDhcpRelayAgnts_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeDhcpRelayAgnts_Object = MibScalar
wwpLeosChassisResourcesFreeDhcpRelayAgnts = _WwpLeosChassisResourcesFreeDhcpRelayAgnts_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 18),
    _WwpLeosChassisResourcesFreeDhcpRelayAgnts_Type()
)
wwpLeosChassisResourcesFreeDhcpRelayAgnts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeDhcpRelayAgnts.setStatus("current")


class _WwpLeosChassisResourcesMaxTunnels_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxTunnels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisResourcesMaxTunnels_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxTunnels_Object = MibScalar
wwpLeosChassisResourcesMaxTunnels = _WwpLeosChassisResourcesMaxTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 19),
    _WwpLeosChassisResourcesMaxTunnels_Type()
)
wwpLeosChassisResourcesMaxTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxTunnels.setStatus("current")


class _WwpLeosChassisResourcesFreeTunnels_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeTunnels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisResourcesFreeTunnels_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeTunnels_Object = MibScalar
wwpLeosChassisResourcesFreeTunnels = _WwpLeosChassisResourcesFreeTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 20),
    _WwpLeosChassisResourcesFreeTunnels_Type()
)
wwpLeosChassisResourcesFreeTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeTunnels.setStatus("current")


class _WwpLeosChassisResourcesMaxIngressTunnels_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxIngressTunnels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesMaxIngressTunnels_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxIngressTunnels_Object = MibScalar
wwpLeosChassisResourcesMaxIngressTunnels = _WwpLeosChassisResourcesMaxIngressTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 21),
    _WwpLeosChassisResourcesMaxIngressTunnels_Type()
)
wwpLeosChassisResourcesMaxIngressTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxIngressTunnels.setStatus("current")


class _WwpLeosChassisResourcesFreeIngressTunnels_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeIngressTunnels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesFreeIngressTunnels_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeIngressTunnels_Object = MibScalar
wwpLeosChassisResourcesFreeIngressTunnels = _WwpLeosChassisResourcesFreeIngressTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 22),
    _WwpLeosChassisResourcesFreeIngressTunnels_Type()
)
wwpLeosChassisResourcesFreeIngressTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeIngressTunnels.setStatus("current")


class _WwpLeosChassisResourcesMaxEgressTunnels_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxEgressTunnels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesMaxEgressTunnels_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxEgressTunnels_Object = MibScalar
wwpLeosChassisResourcesMaxEgressTunnels = _WwpLeosChassisResourcesMaxEgressTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 23),
    _WwpLeosChassisResourcesMaxEgressTunnels_Type()
)
wwpLeosChassisResourcesMaxEgressTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxEgressTunnels.setStatus("current")


class _WwpLeosChassisResourcesFreeEgressTunnels_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeEgressTunnels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesFreeEgressTunnels_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeEgressTunnels_Object = MibScalar
wwpLeosChassisResourcesFreeEgressTunnels = _WwpLeosChassisResourcesFreeEgressTunnels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 24),
    _WwpLeosChassisResourcesFreeEgressTunnels_Type()
)
wwpLeosChassisResourcesFreeEgressTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeEgressTunnels.setStatus("current")


class _WwpLeosChassisResourcesMaxVcs_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxVcs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WwpLeosChassisResourcesMaxVcs_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxVcs_Object = MibScalar
wwpLeosChassisResourcesMaxVcs = _WwpLeosChassisResourcesMaxVcs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 25),
    _WwpLeosChassisResourcesMaxVcs_Type()
)
wwpLeosChassisResourcesMaxVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxVcs.setStatus("current")


class _WwpLeosChassisResourcesFreeVcs_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeVcs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WwpLeosChassisResourcesFreeVcs_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeVcs_Object = MibScalar
wwpLeosChassisResourcesFreeVcs = _WwpLeosChassisResourcesFreeVcs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 26),
    _WwpLeosChassisResourcesFreeVcs_Type()
)
wwpLeosChassisResourcesFreeVcs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeVcs.setStatus("current")


class _WwpLeosChassisResourcesMaxVss_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxVss based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WwpLeosChassisResourcesMaxVss_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxVss_Object = MibScalar
wwpLeosChassisResourcesMaxVss = _WwpLeosChassisResourcesMaxVss_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 27),
    _WwpLeosChassisResourcesMaxVss_Type()
)
wwpLeosChassisResourcesMaxVss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxVss.setStatus("current")


class _WwpLeosChassisResourcesFreeVss_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeVss based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_WwpLeosChassisResourcesFreeVss_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeVss_Object = MibScalar
wwpLeosChassisResourcesFreeVss = _WwpLeosChassisResourcesFreeVss_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 28),
    _WwpLeosChassisResourcesFreeVss_Type()
)
wwpLeosChassisResourcesFreeVss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeVss.setStatus("current")


class _WwpLeosChassisResourcesMaxVsMembers_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxVsMembers based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5334),
    )


_WwpLeosChassisResourcesMaxVsMembers_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxVsMembers_Object = MibScalar
wwpLeosChassisResourcesMaxVsMembers = _WwpLeosChassisResourcesMaxVsMembers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 29),
    _WwpLeosChassisResourcesMaxVsMembers_Type()
)
wwpLeosChassisResourcesMaxVsMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxVsMembers.setStatus("current")


class _WwpLeosChassisResourcesFreeVsMembers_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeVsMembers based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5334),
    )


_WwpLeosChassisResourcesFreeVsMembers_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeVsMembers_Object = MibScalar
wwpLeosChassisResourcesFreeVsMembers = _WwpLeosChassisResourcesFreeVsMembers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 30),
    _WwpLeosChassisResourcesFreeVsMembers_Type()
)
wwpLeosChassisResourcesFreeVsMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeVsMembers.setStatus("current")


class _WwpLeosChassisResourcesMaxSlevelWcards_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSlevelWcards based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosChassisResourcesMaxSlevelWcards_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSlevelWcards_Object = MibScalar
wwpLeosChassisResourcesMaxSlevelWcards = _WwpLeosChassisResourcesMaxSlevelWcards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 31),
    _WwpLeosChassisResourcesMaxSlevelWcards_Type()
)
wwpLeosChassisResourcesMaxSlevelWcards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSlevelWcards.setStatus("current")


class _WwpLeosChassisResourcesFreeSlevelWcards_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSlevelWcards based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosChassisResourcesFreeSlevelWcards_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSlevelWcards_Object = MibScalar
wwpLeosChassisResourcesFreeSlevelWcards = _WwpLeosChassisResourcesFreeSlevelWcards_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 32),
    _WwpLeosChassisResourcesFreeSlevelWcards_Type()
)
wwpLeosChassisResourcesFreeSlevelWcards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSlevelWcards.setStatus("current")


class _WwpLeosChassisResourcesMaxSlevels_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSlevels based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102),
    )


_WwpLeosChassisResourcesMaxSlevels_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSlevels_Object = MibScalar
wwpLeosChassisResourcesMaxSlevels = _WwpLeosChassisResourcesMaxSlevels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 33),
    _WwpLeosChassisResourcesMaxSlevels_Type()
)
wwpLeosChassisResourcesMaxSlevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSlevels.setStatus("current")


class _WwpLeosChassisResourcesFreeSlevels_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSlevels based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 102),
    )


_WwpLeosChassisResourcesFreeSlevels_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSlevels_Object = MibScalar
wwpLeosChassisResourcesFreeSlevels = _WwpLeosChassisResourcesFreeSlevels_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 34),
    _WwpLeosChassisResourcesFreeSlevels_Type()
)
wwpLeosChassisResourcesFreeSlevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSlevels.setStatus("current")


class _WwpLeosChassisResourcesMaxSmappings_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSmappings based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 140),
    )


_WwpLeosChassisResourcesMaxSmappings_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSmappings_Object = MibScalar
wwpLeosChassisResourcesMaxSmappings = _WwpLeosChassisResourcesMaxSmappings_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 35),
    _WwpLeosChassisResourcesMaxSmappings_Type()
)
wwpLeosChassisResourcesMaxSmappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSmappings.setStatus("current")


class _WwpLeosChassisResourcesFreeSmappings_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSmappings based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 140),
    )


_WwpLeosChassisResourcesFreeSmappings_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSmappings_Object = MibScalar
wwpLeosChassisResourcesFreeSmappings = _WwpLeosChassisResourcesFreeSmappings_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 36),
    _WwpLeosChassisResourcesFreeSmappings_Type()
)
wwpLeosChassisResourcesFreeSmappings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSmappings.setStatus("current")


class _WwpLeosChassisResourcesMaxSmappingCosResources_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSmappingCosResources based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_WwpLeosChassisResourcesMaxSmappingCosResources_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSmappingCosResources_Object = MibScalar
wwpLeosChassisResourcesMaxSmappingCosResources = _WwpLeosChassisResourcesMaxSmappingCosResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 37),
    _WwpLeosChassisResourcesMaxSmappingCosResources_Type()
)
wwpLeosChassisResourcesMaxSmappingCosResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSmappingCosResources.setStatus("current")


class _WwpLeosChassisResourcesFreeSmappingCosResources_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSmappingCosResources based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 34),
    )


_WwpLeosChassisResourcesFreeSmappingCosResources_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSmappingCosResources_Object = MibScalar
wwpLeosChassisResourcesFreeSmappingCosResources = _WwpLeosChassisResourcesFreeSmappingCosResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 38),
    _WwpLeosChassisResourcesFreeSmappingCosResources_Type()
)
wwpLeosChassisResourcesFreeSmappingCosResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSmappingCosResources.setStatus("current")


class _WwpLeosChassisResourcesMaxSmappingPrtclResources_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSmappingPrtclResources based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_WwpLeosChassisResourcesMaxSmappingPrtclResources_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSmappingPrtclResources_Object = MibScalar
wwpLeosChassisResourcesMaxSmappingPrtclResources = _WwpLeosChassisResourcesMaxSmappingPrtclResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 39),
    _WwpLeosChassisResourcesMaxSmappingPrtclResources_Type()
)
wwpLeosChassisResourcesMaxSmappingPrtclResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSmappingPrtclResources.setStatus("current")


class _WwpLeosChassisResourcesFreeSmappingPrtclResources_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSmappingPrtclResources based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62),
    )


_WwpLeosChassisResourcesFreeSmappingPrtclResources_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSmappingPrtclResources_Object = MibScalar
wwpLeosChassisResourcesFreeSmappingPrtclResources = _WwpLeosChassisResourcesFreeSmappingPrtclResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 40),
    _WwpLeosChassisResourcesFreeSmappingPrtclResources_Type()
)
wwpLeosChassisResourcesFreeSmappingPrtclResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSmappingPrtclResources.setStatus("current")


class _WwpLeosChassisResourcesMaxQosResEgs_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxQosResEgs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WwpLeosChassisResourcesMaxQosResEgs_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxQosResEgs_Object = MibScalar
wwpLeosChassisResourcesMaxQosResEgs = _WwpLeosChassisResourcesMaxQosResEgs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 41),
    _WwpLeosChassisResourcesMaxQosResEgs_Type()
)
wwpLeosChassisResourcesMaxQosResEgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxQosResEgs.setStatus("current")


class _WwpLeosChassisResourcesFreeQosResEgs_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeQosResEgs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WwpLeosChassisResourcesFreeQosResEgs_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeQosResEgs_Object = MibScalar
wwpLeosChassisResourcesFreeQosResEgs = _WwpLeosChassisResourcesFreeQosResEgs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 42),
    _WwpLeosChassisResourcesFreeQosResEgs_Type()
)
wwpLeosChassisResourcesFreeQosResEgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeQosResEgs.setStatus("current")


class _WwpLeosChassisResourcesMaxTprofGblCscdEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxTprofGblCscdEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosChassisResourcesMaxTprofGblCscdEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxTprofGblCscdEntries_Object = MibScalar
wwpLeosChassisResourcesMaxTprofGblCscdEntries = _WwpLeosChassisResourcesMaxTprofGblCscdEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 43),
    _WwpLeosChassisResourcesMaxTprofGblCscdEntries_Type()
)
wwpLeosChassisResourcesMaxTprofGblCscdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxTprofGblCscdEntries.setStatus("current")


class _WwpLeosChassisResourcesFreeTprofGblCscdEntries_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeTprofGblCscdEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_WwpLeosChassisResourcesFreeTprofGblCscdEntries_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeTprofGblCscdEntries_Object = MibScalar
wwpLeosChassisResourcesFreeTprofGblCscdEntries = _WwpLeosChassisResourcesFreeTprofGblCscdEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 44),
    _WwpLeosChassisResourcesFreeTprofGblCscdEntries_Type()
)
wwpLeosChassisResourcesFreeTprofGblCscdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeTprofGblCscdEntries.setStatus("current")


class _WwpLeosChassisResourcesMaxTprofCscdEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxTprofCscdEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WwpLeosChassisResourcesMaxTprofCscdEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxTprofCscdEntries_Object = MibScalar
wwpLeosChassisResourcesMaxTprofCscdEntries = _WwpLeosChassisResourcesMaxTprofCscdEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 45),
    _WwpLeosChassisResourcesMaxTprofCscdEntries_Type()
)
wwpLeosChassisResourcesMaxTprofCscdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxTprofCscdEntries.setStatus("current")


class _WwpLeosChassisResourcesFreeTprofCscdEntries_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeTprofCscdEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 126),
    )


_WwpLeosChassisResourcesFreeTprofCscdEntries_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeTprofCscdEntries_Object = MibScalar
wwpLeosChassisResourcesFreeTprofCscdEntries = _WwpLeosChassisResourcesFreeTprofCscdEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 46),
    _WwpLeosChassisResourcesFreeTprofCscdEntries_Type()
)
wwpLeosChassisResourcesFreeTprofCscdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeTprofCscdEntries.setStatus("current")


class _WwpLeosChassisResourcesMaxTprofStdEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxTprofStdEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 336),
    )


_WwpLeosChassisResourcesMaxTprofStdEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxTprofStdEntries_Object = MibScalar
wwpLeosChassisResourcesMaxTprofStdEntries = _WwpLeosChassisResourcesMaxTprofStdEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 47),
    _WwpLeosChassisResourcesMaxTprofStdEntries_Type()
)
wwpLeosChassisResourcesMaxTprofStdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxTprofStdEntries.setStatus("current")


class _WwpLeosChassisResourcesFreeTprofStdEntries_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeTprofStdEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 336),
    )


_WwpLeosChassisResourcesFreeTprofStdEntries_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeTprofStdEntries_Object = MibScalar
wwpLeosChassisResourcesFreeTprofStdEntries = _WwpLeosChassisResourcesFreeTprofStdEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 48),
    _WwpLeosChassisResourcesFreeTprofStdEntries_Type()
)
wwpLeosChassisResourcesFreeTprofStdEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeTprofStdEntries.setStatus("current")


class _WwpLeosChassisResourcesMaxSaccessEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSaccessEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2074),
    )


_WwpLeosChassisResourcesMaxSaccessEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSaccessEntries_Object = MibScalar
wwpLeosChassisResourcesMaxSaccessEntries = _WwpLeosChassisResourcesMaxSaccessEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 49),
    _WwpLeosChassisResourcesMaxSaccessEntries_Type()
)
wwpLeosChassisResourcesMaxSaccessEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSaccessEntries.setStatus("current")


class _WwpLeosChassisResourcesFreeSaccessEntries_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSaccessEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2074),
    )


_WwpLeosChassisResourcesFreeSaccessEntries_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSaccessEntries_Object = MibScalar
wwpLeosChassisResourcesFreeSaccessEntries = _WwpLeosChassisResourcesFreeSaccessEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 50),
    _WwpLeosChassisResourcesFreeSaccessEntries_Type()
)
wwpLeosChassisResourcesFreeSaccessEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSaccessEntries.setStatus("current")


class _WwpLeosChassisResourcesMaxSmacEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxSmacEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WwpLeosChassisResourcesMaxSmacEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxSmacEntries_Object = MibScalar
wwpLeosChassisResourcesMaxSmacEntries = _WwpLeosChassisResourcesMaxSmacEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 51),
    _WwpLeosChassisResourcesMaxSmacEntries_Type()
)
wwpLeosChassisResourcesMaxSmacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxSmacEntries.setStatus("current")


class _WwpLeosChassisResourcesFreeSmacEntries_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeSmacEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_WwpLeosChassisResourcesFreeSmacEntries_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeSmacEntries_Object = MibScalar
wwpLeosChassisResourcesFreeSmacEntries = _WwpLeosChassisResourcesFreeSmacEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 52),
    _WwpLeosChassisResourcesFreeSmacEntries_Type()
)
wwpLeosChassisResourcesFreeSmacEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeSmacEntries.setStatus("current")


class _WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxDrvNoLrnSacResources based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Object = MibScalar
wwpLeosChassisResourcesMaxDrvNoLrnSacResources = _WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 53),
    _WwpLeosChassisResourcesMaxDrvNoLrnSacResources_Type()
)
wwpLeosChassisResourcesMaxDrvNoLrnSacResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxDrvNoLrnSacResources.setStatus("current")


class _WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeDrvNoLrnSacResources based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
    )


_WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Object = MibScalar
wwpLeosChassisResourcesFreeDrvNoLrnSacResources = _WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 54),
    _WwpLeosChassisResourcesFreeDrvNoLrnSacResources_Type()
)
wwpLeosChassisResourcesFreeDrvNoLrnSacResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeDrvNoLrnSacResources.setStatus("current")


class _WwpLeosChassisResourcesMaxLearnEntries_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxLearnEntries based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_WwpLeosChassisResourcesMaxLearnEntries_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxLearnEntries_Object = MibScalar
wwpLeosChassisResourcesMaxLearnEntries = _WwpLeosChassisResourcesMaxLearnEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 55),
    _WwpLeosChassisResourcesMaxLearnEntries_Type()
)
wwpLeosChassisResourcesMaxLearnEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxLearnEntries.setStatus("current")


class _WwpLeosChassisResourcesFreeLearnEntries_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeLearnEntries based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 20000),
    )


_WwpLeosChassisResourcesFreeLearnEntries_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeLearnEntries_Object = MibScalar
wwpLeosChassisResourcesFreeLearnEntries = _WwpLeosChassisResourcesFreeLearnEntries_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 56),
    _WwpLeosChassisResourcesFreeLearnEntries_Type()
)
wwpLeosChassisResourcesFreeLearnEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeLearnEntries.setStatus("current")


class _WwpLeosChassisResourcesMaxCustomPrtcls_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxCustomPrtcls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WwpLeosChassisResourcesMaxCustomPrtcls_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxCustomPrtcls_Object = MibScalar
wwpLeosChassisResourcesMaxCustomPrtcls = _WwpLeosChassisResourcesMaxCustomPrtcls_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 57),
    _WwpLeosChassisResourcesMaxCustomPrtcls_Type()
)
wwpLeosChassisResourcesMaxCustomPrtcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxCustomPrtcls.setStatus("current")


class _WwpLeosChassisResourcesFreeCustomPrtcls_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeCustomPrtcls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_WwpLeosChassisResourcesFreeCustomPrtcls_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeCustomPrtcls_Object = MibScalar
wwpLeosChassisResourcesFreeCustomPrtcls = _WwpLeosChassisResourcesFreeCustomPrtcls_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 58),
    _WwpLeosChassisResourcesFreeCustomPrtcls_Type()
)
wwpLeosChassisResourcesFreeCustomPrtcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeCustomPrtcls.setStatus("current")


class _WwpLeosChassisResourcesMaxPrtcls_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxPrtcls based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesMaxPrtcls_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxPrtcls_Object = MibScalar
wwpLeosChassisResourcesMaxPrtcls = _WwpLeosChassisResourcesMaxPrtcls_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 59),
    _WwpLeosChassisResourcesMaxPrtcls_Type()
)
wwpLeosChassisResourcesMaxPrtcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxPrtcls.setStatus("current")


class _WwpLeosChassisResourcesFreePrtcls_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreePrtcls based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_WwpLeosChassisResourcesFreePrtcls_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreePrtcls_Object = MibScalar
wwpLeosChassisResourcesFreePrtcls = _WwpLeosChassisResourcesFreePrtcls_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 60),
    _WwpLeosChassisResourcesFreePrtcls_Type()
)
wwpLeosChassisResourcesFreePrtcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreePrtcls.setStatus("current")


class _WwpLeosChassisResourcesMaxPrtclFilters_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxPrtclFilters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisResourcesMaxPrtclFilters_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxPrtclFilters_Object = MibScalar
wwpLeosChassisResourcesMaxPrtclFilters = _WwpLeosChassisResourcesMaxPrtclFilters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 61),
    _WwpLeosChassisResourcesMaxPrtclFilters_Type()
)
wwpLeosChassisResourcesMaxPrtclFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxPrtclFilters.setStatus("current")


class _WwpLeosChassisResourcesFreePrtclFilters_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreePrtclFilters based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisResourcesFreePrtclFilters_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreePrtclFilters_Object = MibScalar
wwpLeosChassisResourcesFreePrtclFilters = _WwpLeosChassisResourcesFreePrtclFilters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 62),
    _WwpLeosChassisResourcesFreePrtclFilters_Type()
)
wwpLeosChassisResourcesFreePrtclFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreePrtclFilters.setStatus("current")


class _WwpLeosChassisResourcesMaxPrtclFilterMembs_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxPrtclFilterMembs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_WwpLeosChassisResourcesMaxPrtclFilterMembs_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxPrtclFilterMembs_Object = MibScalar
wwpLeosChassisResourcesMaxPrtclFilterMembs = _WwpLeosChassisResourcesMaxPrtclFilterMembs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 63),
    _WwpLeosChassisResourcesMaxPrtclFilterMembs_Type()
)
wwpLeosChassisResourcesMaxPrtclFilterMembs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxPrtclFilterMembs.setStatus("current")


class _WwpLeosChassisResourcesFreePrtclFilterMembs_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreePrtclFilterMembs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512),
    )


_WwpLeosChassisResourcesFreePrtclFilterMembs_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreePrtclFilterMembs_Object = MibScalar
wwpLeosChassisResourcesFreePrtclFilterMembs = _WwpLeosChassisResourcesFreePrtclFilterMembs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 64),
    _WwpLeosChassisResourcesFreePrtclFilterMembs_Type()
)
wwpLeosChassisResourcesFreePrtclFilterMembs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreePrtclFilterMembs.setStatus("current")


class _WwpLeosChassisResourcesMaxBcastFilters_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxBcastFilters based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisResourcesMaxBcastFilters_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxBcastFilters_Object = MibScalar
wwpLeosChassisResourcesMaxBcastFilters = _WwpLeosChassisResourcesMaxBcastFilters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 65),
    _WwpLeosChassisResourcesMaxBcastFilters_Type()
)
wwpLeosChassisResourcesMaxBcastFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxBcastFilters.setStatus("current")


class _WwpLeosChassisResourcesFreeBcastFilters_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeBcastFilters based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_WwpLeosChassisResourcesFreeBcastFilters_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeBcastFilters_Object = MibScalar
wwpLeosChassisResourcesFreeBcastFilters = _WwpLeosChassisResourcesFreeBcastFilters_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 66),
    _WwpLeosChassisResourcesFreeBcastFilters_Type()
)
wwpLeosChassisResourcesFreeBcastFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeBcastFilters.setStatus("current")


class _WwpLeosChassisResourcesMaxBcastFilterMembs_Type(Unsigned32):
    """Custom type wwpLeosChassisResourcesMaxBcastFilterMembs based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4064),
    )


_WwpLeosChassisResourcesMaxBcastFilterMembs_Type.__name__ = "Unsigned32"
_WwpLeosChassisResourcesMaxBcastFilterMembs_Object = MibScalar
wwpLeosChassisResourcesMaxBcastFilterMembs = _WwpLeosChassisResourcesMaxBcastFilterMembs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 67),
    _WwpLeosChassisResourcesMaxBcastFilterMembs_Type()
)
wwpLeosChassisResourcesMaxBcastFilterMembs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesMaxBcastFilterMembs.setStatus("current")


class _WwpLeosChassisResourcesFreeBcastFilterMembs_Type(Gauge32):
    """Custom type wwpLeosChassisResourcesFreeBcastFilterMembs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4064),
    )


_WwpLeosChassisResourcesFreeBcastFilterMembs_Type.__name__ = "Gauge32"
_WwpLeosChassisResourcesFreeBcastFilterMembs_Object = MibScalar
wwpLeosChassisResourcesFreeBcastFilterMembs = _WwpLeosChassisResourcesFreeBcastFilterMembs_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 1, 9, 68),
    _WwpLeosChassisResourcesFreeBcastFilterMembs_Type()
)
wwpLeosChassisResourcesFreeBcastFilterMembs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosChassisResourcesFreeBcastFilterMembs.setStatus("current")
_WwpLeosChassisNotifAttrs_ObjectIdentity = ObjectIdentity
wwpLeosChassisNotifAttrs = _WwpLeosChassisNotifAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2)
)


class _WwpLeosChassisPostErrorCategory_Type(Integer32):
    """Custom type wwpLeosChassisPostErrorCategory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blade", 2),
          ("chassis", 1),
          ("port", 3))
    )


_WwpLeosChassisPostErrorCategory_Type.__name__ = "Integer32"
_WwpLeosChassisPostErrorCategory_Object = MibScalar
wwpLeosChassisPostErrorCategory = _WwpLeosChassisPostErrorCategory_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2, 1),
    _WwpLeosChassisPostErrorCategory_Type()
)
wwpLeosChassisPostErrorCategory.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisPostErrorCategory.setStatus("current")


class _WwpLeosChassisPostErrorValue_Type(Integer32):
    """Custom type wwpLeosChassisPostErrorValue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosChassisPostErrorValue_Type.__name__ = "Integer32"
_WwpLeosChassisPostErrorValue_Object = MibScalar
wwpLeosChassisPostErrorValue = _WwpLeosChassisPostErrorValue_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2, 2),
    _WwpLeosChassisPostErrorValue_Type()
)
wwpLeosChassisPostErrorValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisPostErrorValue.setStatus("current")
_WwpLeosChassisPostErrorCode_Type = Unsigned32
_WwpLeosChassisPostErrorCode_Object = MibScalar
wwpLeosChassisPostErrorCode = _WwpLeosChassisPostErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2, 3),
    _WwpLeosChassisPostErrorCode_Type()
)
wwpLeosChassisPostErrorCode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisPostErrorCode.setStatus("current")
_WwpLeosChassisPostErrorMsg_Type = DisplayString
_WwpLeosChassisPostErrorMsg_Object = MibScalar
wwpLeosChassisPostErrorMsg = _WwpLeosChassisPostErrorMsg_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2, 4),
    _WwpLeosChassisPostErrorMsg_Type()
)
wwpLeosChassisPostErrorMsg.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisPostErrorMsg.setStatus("current")


class _WwpLeosChassisRebootReasonErrorType_Type(Integer32):
    """Custom type wwpLeosChassisRebootReasonErrorType based on Integer32"""
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
        *(("appload", 4),
          ("cli", 8),
          ("errorHandler", 5),
          ("guardianReboot", 11),
          ("guardianSaosRestart", 12),
          ("powerFailure", 3),
          ("resetButton", 9),
          ("serviceModeChange", 10),
          ("snmp", 2),
          ("unknown", 1),
          ("upgrade", 7),
          ("watchDog", 6))
    )


_WwpLeosChassisRebootReasonErrorType_Type.__name__ = "Integer32"
_WwpLeosChassisRebootReasonErrorType_Object = MibScalar
wwpLeosChassisRebootReasonErrorType = _WwpLeosChassisRebootReasonErrorType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2, 5),
    _WwpLeosChassisRebootReasonErrorType_Type()
)
wwpLeosChassisRebootReasonErrorType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisRebootReasonErrorType.setStatus("current")


class _WwpLeosChassisSnmpState_Type(Integer32):
    """Custom type wwpLeosChassisSnmpState based on Integer32"""
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


_WwpLeosChassisSnmpState_Type.__name__ = "Integer32"
_WwpLeosChassisSnmpState_Object = MibScalar
wwpLeosChassisSnmpState = _WwpLeosChassisSnmpState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 1, 2, 6),
    _WwpLeosChassisSnmpState_Type()
)
wwpLeosChassisSnmpState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    wwpLeosChassisSnmpState.setStatus("current")
_WwpLeosChassisMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosChassisMIBNotificationPrefix = _WwpLeosChassisMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2)
)
_WwpLeosChassisMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosChassisMIBNotifications = _WwpLeosChassisMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0)
)
_WwpLeosChassisMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosChassisMIBConformance = _WwpLeosChassisMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 3)
)
_WwpLeosChassisMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosChassisMIBCompliances = _WwpLeosChassisMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 3, 1)
)
_WwpLeosChassisMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosChassisMIBGroups = _WwpLeosChassisMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosChassisPowerSupplyStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 1)
)
wwpLeosChassisPowerSupplyStatusNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPowerSupplyNum"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPowerSupplyState"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPowerSupplyType"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSupplyStatusNotification.setStatus(
        "current"
    )

wwpLeosChassisFanModuleNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 2)
)
wwpLeosChassisFanModuleNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisFanModuleNum"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisFanModuleStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisFanModuleNotification.setStatus(
        "current"
    )

wwpLeosChassisTempNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 3)
)
wwpLeosChassisTempNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisTempSensorState"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisTempSensorValue"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisTempSensorHighThreshold"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisTempSensorLowThreshold"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisTempNotification.setStatus(
        "current"
    )

wwpLeosChassisPowerSwitchNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 4)
)
wwpLeosChassisPowerSwitchNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpPowerSwitchingOp")
)
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSwitchNotification.setStatus(
        "current"
    )

wwpLeosChassisBatteryStatusNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 5)
)
wwpLeosChassisBatteryStatusNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisBatteryStatus")
)
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryStatusNotification.setStatus(
        "current"
    )

wwpLeosChassisBatteryVoltageLevelNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 6)
)
wwpLeosChassisBatteryVoltageLevelNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisBatteryVoltageLevel")
)
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryVoltageLevelNotification.setStatus(
        "current"
    )

wwpLeosChassisBatteryConditionNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 7)
)
wwpLeosChassisBatteryConditionNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisBatteryCondition")
)
if mibBuilder.loadTexts:
    wwpLeosChassisBatteryConditionNotification.setStatus(
        "current"
    )

wwpLeosChassisPowerSourceNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 8)
)
wwpLeosChassisPowerSourceNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPowerSource")
)
if mibBuilder.loadTexts:
    wwpLeosChassisPowerSourceNotification.setStatus(
        "current"
    )

wwpLeosChassisPostErrorNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 9)
)
wwpLeosChassisPostErrorNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPostErrorCategory"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPostErrorValue"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPostErrorCode"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisPostErrorMsg"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisPostErrorNotification.setStatus(
        "current"
    )

wwpLeosChassisRebootNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 10)
)
wwpLeosChassisRebootNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisRebootReasonErrorType")
)
if mibBuilder.loadTexts:
    wwpLeosChassisRebootNotification.setStatus(
        "current"
    )

wwpLeosChassisSnmpStateNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 11)
)
wwpLeosChassisSnmpStateNotification.setObjects(
    ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisSnmpState")
)
if mibBuilder.loadTexts:
    wwpLeosChassisSnmpStateNotification.setStatus(
        "current"
    )

wwpLeosChassisDyingGaspNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 12)
)
wwpLeosChassisDyingGaspNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDeviceId"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisHardwareVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisSerialNumber"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMacAddress"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMfgDate"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisParamVersion"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisDyingGaspNotification.setStatus(
        "current"
    )

wwpLeosChassisDoorStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 13)
)
wwpLeosChassisDoorStatusChangeNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDeviceId"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisHardwareVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisSerialNumber"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMacAddress"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMfgDate"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisParamVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisInnerDoorStatus"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisOuterDoorStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisDoorStatusChangeNotification.setStatus(
        "deprecated"
    )

wwpLeosChassisInnerDoorStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 14)
)
wwpLeosChassisInnerDoorStatusChangeNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDeviceId"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisHardwareVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisSerialNumber"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMacAddress"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMfgDate"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisParamVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisInnerDoorStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisInnerDoorStatusChangeNotification.setStatus(
        "current"
    )

wwpLeosChassisOuterDoorStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 15)
)
wwpLeosChassisOuterDoorStatusChangeNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDeviceId"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisHardwareVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisSerialNumber"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMacAddress"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMfgDate"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisParamVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisOuterDoorStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisOuterDoorStatusChangeNotification.setStatus(
        "current"
    )

wwpLeosChassisExternalAlarmStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 16)
)
wwpLeosChassisExternalAlarmStatusChangeNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDeviceId"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisHardwareVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisSerialNumber"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMacAddress"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisMfgDate"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisParamVersion"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisOuterDoorStatus"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisExternalAlarm"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisExternalAlarmStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisExternalAlarmStatusChangeNotification.setStatus(
        "current"
    )

wwpLeosChassisDoorAlarmStatusChangeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 11, 2, 0, 17)
)
wwpLeosChassisDoorAlarmStatusChangeNotification.setObjects(
      *(("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDoorAlarmIndex"),
        ("WWP-LEOS-CHASSIS-MIB", "wwpLeosChassisDoorAlarmStatus"))
)
if mibBuilder.loadTexts:
    wwpLeosChassisDoorAlarmStatusChangeNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-CHASSIS-MIB",
    **{"PortList": PortList,
       "FileName": FileName,
       "wwpLeosChassisMIB": wwpLeosChassisMIB,
       "wwpLeosChassisMIBObjects": wwpLeosChassisMIBObjects,
       "wwpLeosChassis": wwpLeosChassis,
       "wwpLeosChassisModule": wwpLeosChassisModule,
       "wwpLeosChassisRebootState": wwpLeosChassisRebootState,
       "wwpLeosChassisSystemTimeOffsetScope": wwpLeosChassisSystemTimeOffsetScope,
       "wwpLeosChassisSystemTimeOffset": wwpLeosChassisSystemTimeOffset,
       "wwpLeosChassisSerialConsoleState": wwpLeosChassisSerialConsoleState,
       "wwpLeosChassisShellInactivityTimerState": wwpLeosChassisShellInactivityTimerState,
       "wwpLeosChassisShellInactivityTimeout": wwpLeosChassisShellInactivityTimeout,
       "wwpLeosChassisSerialConsoleDataBits": wwpLeosChassisSerialConsoleDataBits,
       "wwpLeosChassisSerialConsoleParity": wwpLeosChassisSerialConsoleParity,
       "wwpLeosChassisSerialConsoleStopBits": wwpLeosChassisSerialConsoleStopBits,
       "wwpLeosChassisRebootNow": wwpLeosChassisRebootNow,
       "wwpLeosChassisShellLoginTimerState": wwpLeosChassisShellLoginTimerState,
       "wwpLeosChassisShellLoginTimeout": wwpLeosChassisShellLoginTimeout,
       "wwpLeosChassisScheduledRebootTable": wwpLeosChassisScheduledRebootTable,
       "wwpLeosChassisScheduledRebootEntry": wwpLeosChassisScheduledRebootEntry,
       "wwpLeosChassisScheduledRebootIndex": wwpLeosChassisScheduledRebootIndex,
       "wwpLeosChassisScheduledRebootTimestamp": wwpLeosChassisScheduledRebootTimestamp,
       "wwpLeosChassisScheduledRebootActive": wwpLeosChassisScheduledRebootActive,
       "wwpLeosChassisScheduledRebootNopost": wwpLeosChassisScheduledRebootNopost,
       "wwpLeosChassisScheduledRebootDelay": wwpLeosChassisScheduledRebootDelay,
       "wwpLeosChassisWelcomeBanner": wwpLeosChassisWelcomeBanner,
       "wwpLeosChassisResetWelcomeBanner": wwpLeosChassisResetWelcomeBanner,
       "wwpLeosChassisLoginBanner": wwpLeosChassisLoginBanner,
       "wwpLeosChassisResetLoginBanner": wwpLeosChassisResetLoginBanner,
       "wwpLeosChassisMacAddress": wwpLeosChassisMacAddress,
       "wwpLeosChassisDeviceId": wwpLeosChassisDeviceId,
       "wwpLeosChassisSerialNumber": wwpLeosChassisSerialNumber,
       "wwpLeosChassisMfgDate": wwpLeosChassisMfgDate,
       "wwpLeosChassisParamVersion": wwpLeosChassisParamVersion,
       "wwpLeosChassisHardwareVersion": wwpLeosChassisHardwareVersion,
       "wwpLeosChassisInnerDoorStatus": wwpLeosChassisInnerDoorStatus,
       "wwpLeosChassisOuterDoorStatus": wwpLeosChassisOuterDoorStatus,
       "wwpLeosChassisPostState": wwpLeosChassisPostState,
       "wwpLeosChassisPostResultTable": wwpLeosChassisPostResultTable,
       "wwpLeosChassisPostResultEntry": wwpLeosChassisPostResultEntry,
       "wwpLeosChassisPostResultIndex": wwpLeosChassisPostResultIndex,
       "wwpLeosChassisPostResultCode": wwpLeosChassisPostResultCode,
       "wwpLeosChassisPostResultMessage": wwpLeosChassisPostResultMessage,
       "wwpLeosChassisExternalAlarmStatus": wwpLeosChassisExternalAlarmStatus,
       "wwpLeosChassisExternalAlarm": wwpLeosChassisExternalAlarm,
       "wwpLeosChassisDoorAlarmTable": wwpLeosChassisDoorAlarmTable,
       "wwpLeosChassisDoorAlarmEntry": wwpLeosChassisDoorAlarmEntry,
       "wwpLeosChassisDoorAlarmIndex": wwpLeosChassisDoorAlarmIndex,
       "wwpLeosChassisDoorAlarmStatus": wwpLeosChassisDoorAlarmStatus,
       "wwpLeosChassisDoorAlarmAdminStatus": wwpLeosChassisDoorAlarmAdminStatus,
       "wwpLeosChassisDoorAlarmFlapDetect": wwpLeosChassisDoorAlarmFlapDetect,
       "wwpLeosChassisDoorAlarmFlapCount": wwpLeosChassisDoorAlarmFlapCount,
       "wwpLeosChassisDoorAlarmFlapDetectTime": wwpLeosChassisDoorAlarmFlapDetectTime,
       "wwpLeosChassisDoorAlarmFlapHoldTime": wwpLeosChassisDoorAlarmFlapHoldTime,
       "wwpLeosSystemPartNumber": wwpLeosSystemPartNumber,
       "wwpLeosSystemSerialNumber": wwpLeosSystemSerialNumber,
       "wwpLeosChassisBatteryModule": wwpLeosChassisBatteryModule,
       "wwpLeosChassisBatteryStatus": wwpLeosChassisBatteryStatus,
       "wwpLeosChassisBatteryVoltageLevel": wwpLeosChassisBatteryVoltageLevel,
       "wwpLeosChassisBatteryCondition": wwpLeosChassisBatteryCondition,
       "wwpLeosChassisPowerSource": wwpLeosChassisPowerSource,
       "wwpLeosChassisBatteryNormalStateName": wwpLeosChassisBatteryNormalStateName,
       "wwpLeosChassisBatteryLowStateName": wwpLeosChassisBatteryLowStateName,
       "wwpLeosChassisBatteryGoodStateName": wwpLeosChassisBatteryGoodStateName,
       "wwpLeosChassisBatteryBadStateName": wwpLeosChassisBatteryBadStateName,
       "wwpLeosChassisBatteryPresentStateName": wwpLeosChassisBatteryPresentStateName,
       "wwpLeosChassisBatteryMissingStateName": wwpLeosChassisBatteryMissingStateName,
       "wwpLeosChassisBatteryPowerPrimaryStateName": wwpLeosChassisBatteryPowerPrimaryStateName,
       "wwpLeosChassisBatteryPowerBatteryStateName": wwpLeosChassisBatteryPowerBatteryStateName,
       "wwpLeosChassisBatteryLowStateNotifEnabled": wwpLeosChassisBatteryLowStateNotifEnabled,
       "wwpLeosChassisBatteryBadStateNotifEnabled": wwpLeosChassisBatteryBadStateNotifEnabled,
       "wwpLeosChassisBatteryMissingStateNotifEnabled": wwpLeosChassisBatteryMissingStateNotifEnabled,
       "wwpLeosChassisBatteryPowerNotifEnabled": wwpLeosChassisBatteryPowerNotifEnabled,
       "wwpLeosChassisPowerSupplyModule": wwpLeosChassisPowerSupplyModule,
       "wwpLeosChassisPowerTable": wwpLeosChassisPowerTable,
       "wwpLeosChassisPowerEntry": wwpLeosChassisPowerEntry,
       "wwpLeosChassisPowerSupplyNum": wwpLeosChassisPowerSupplyNum,
       "wwpLeosChassisPowerSupplyState": wwpLeosChassisPowerSupplyState,
       "wwpLeosChassisPowerSupplyType": wwpLeosChassisPowerSupplyType,
       "wwpLeosChassisPowerSupplyRedundantState": wwpLeosChassisPowerSupplyRedundantState,
       "wwpLeosChassisRedPowerSupplyNotifEnabled": wwpLeosChassisRedPowerSupplyNotifEnabled,
       "wwpLeosChassisFanModule": wwpLeosChassisFanModule,
       "wwpLeosChassisFanModuleTable": wwpLeosChassisFanModuleTable,
       "wwpLeosChassisFanModuleEntry": wwpLeosChassisFanModuleEntry,
       "wwpLeosChassisFanModuleNum": wwpLeosChassisFanModuleNum,
       "wwpLeosChassisFanModuleType": wwpLeosChassisFanModuleType,
       "wwpLeosChassisFanModuleStatus": wwpLeosChassisFanModuleStatus,
       "wwpLeosChassisFanAvgSpeed": wwpLeosChassisFanAvgSpeed,
       "wwpLeosChassisFanCurrentSpeed": wwpLeosChassisFanCurrentSpeed,
       "wwpLeosChassisFanMinSpeed": wwpLeosChassisFanMinSpeed,
       "wwpLeosChassisFanModuleNotifEnabled": wwpLeosChassisFanModuleNotifEnabled,
       "wwpLeosChassisTempSensor": wwpLeosChassisTempSensor,
       "wwpLeosChassisTempSensorTable": wwpLeosChassisTempSensorTable,
       "wwpLeosChassisTempSensorEntry": wwpLeosChassisTempSensorEntry,
       "wwpLeosChassisTempSensorNum": wwpLeosChassisTempSensorNum,
       "wwpLeosChassisTempSensorValue": wwpLeosChassisTempSensorValue,
       "wwpLeosChassisTempSensorHighThreshold": wwpLeosChassisTempSensorHighThreshold,
       "wwpLeosChassisTempSensorLowThreshold": wwpLeosChassisTempSensorLowThreshold,
       "wwpLeosChassisTempSensorState": wwpLeosChassisTempSensorState,
       "wwpLeosChassisTempNotifEnabled": wwpLeosChassisTempNotifEnabled,
       "wwpLeosChassisTempHighThreshold": wwpLeosChassisTempHighThreshold,
       "wwpLeosChassisTempLowThreshold": wwpLeosChassisTempLowThreshold,
       "wwpLeosChassisNotif": wwpLeosChassisNotif,
       "wwpPowerSwitchingOp": wwpPowerSwitchingOp,
       "wwpLeosChassisPlatformCaps": wwpLeosChassisPlatformCaps,
       "wwpLeosChassisPlatformCapsMaxPhysPorts": wwpLeosChassisPlatformCapsMaxPhysPorts,
       "wwpLeosChassisPlatformCapsMaxAggrPorts": wwpLeosChassisPlatformCapsMaxAggrPorts,
       "wwpLeosChassisPlatformCapsMaxVlans": wwpLeosChassisPlatformCapsMaxVlans,
       "wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans": wwpLeosChassisPlatformCapsMaxIgmpSnoopVlans,
       "wwpLeosChassisPlatformCapsMaxMulticastgroups": wwpLeosChassisPlatformCapsMaxMulticastgroups,
       "wwpLeosChassisPlatformCapsMaxRstpDomains": wwpLeosChassisPlatformCapsMaxRstpDomains,
       "wwpLeosChassisPlatformCapsMaxTunnels": wwpLeosChassisPlatformCapsMaxTunnels,
       "wwpLeosChassisPlatformCapsMaxIngressTunnels": wwpLeosChassisPlatformCapsMaxIngressTunnels,
       "wwpLeosChassisPlatformCapsMaxEgressTunnels": wwpLeosChassisPlatformCapsMaxEgressTunnels,
       "wwpLeosChassisPlatformCapsMaxVcs": wwpLeosChassisPlatformCapsMaxVcs,
       "wwpLeosChassisPlatformCapsMaxVss": wwpLeosChassisPlatformCapsMaxVss,
       "wwpLeosChassisPlatformCapsMaxVsMembers": wwpLeosChassisPlatformCapsMaxVsMembers,
       "wwpLeosChassisPlatformCapsMaxLearnedMacs": wwpLeosChassisPlatformCapsMaxLearnedMacs,
       "wwpLeosChassisPlatformCapsMaxFsmtEntries": wwpLeosChassisPlatformCapsMaxFsmtEntries,
       "wwpLeosChassisPlatformCapsMaxFsmtCosEntries": wwpLeosChassisPlatformCapsMaxFsmtCosEntries,
       "wwpLeosChassisPlatformCapsMaxL4ProtEntries": wwpLeosChassisPlatformCapsMaxL4ProtEntries,
       "wwpLeosChassisPlatformCapsMaxSltEntries": wwpLeosChassisPlatformCapsMaxSltEntries,
       "wwpLeosChassisPlatformCapsMaxSactEntries": wwpLeosChassisPlatformCapsMaxSactEntries,
       "wwpLeosChassisPlatformCapsMaxSmtEntries": wwpLeosChassisPlatformCapsMaxSmtEntries,
       "wwpLeosChassisPlatformCapsMaxEprSnids": wwpLeosChassisPlatformCapsMaxEprSnids,
       "wwpLeosChassisPlatformCapsMaxSltWildcards": wwpLeosChassisPlatformCapsMaxSltWildcards,
       "wwpLeosChassisPlatformCapsVlanTranslation": wwpLeosChassisPlatformCapsVlanTranslation,
       "wwpLeosChassisPlatformCapsProtocolFilters": wwpLeosChassisPlatformCapsProtocolFilters,
       "wwpLeosChassisPlatformCapsMultiSubsPerPort": wwpLeosChassisPlatformCapsMultiSubsPerPort,
       "wwpLeosChassisPlatformCapsVplsFpga": wwpLeosChassisPlatformCapsVplsFpga,
       "wwpLeosChassisPlatformCapsPbtFpga": wwpLeosChassisPlatformCapsPbtFpga,
       "wwpLeosChassisPlatformCapsAoamFpga": wwpLeosChassisPlatformCapsAoamFpga,
       "wwpLeosChassisPlatformCapsDcPower": wwpLeosChassisPlatformCapsDcPower,
       "wwpLeosChassisPlatformCapsAcPower": wwpLeosChassisPlatformCapsAcPower,
       "wwpLeosChassisPlatformCapsRedunPower": wwpLeosChassisPlatformCapsRedunPower,
       "wwpLeosChassisResourceCounts": wwpLeosChassisResourceCounts,
       "wwpLeosChassisResourcesMaxPorts": wwpLeosChassisResourcesMaxPorts,
       "wwpLeosChassisResourcesFreePorts": wwpLeosChassisResourcesFreePorts,
       "wwpLeosChassisResourcesMaxAggrPorts": wwpLeosChassisResourcesMaxAggrPorts,
       "wwpLeosChassisResourcesFreeAggrs": wwpLeosChassisResourcesFreeAggrs,
       "wwpLeosChassisResourcesMaxPortStateGrps": wwpLeosChassisResourcesMaxPortStateGrps,
       "wwpLeosChassisResourcesFreePortStateGrps": wwpLeosChassisResourcesFreePortStateGrps,
       "wwpLeosChassisResourcesMaxVlans": wwpLeosChassisResourcesMaxVlans,
       "wwpLeosChassisResourcesFreeVlans": wwpLeosChassisResourcesFreeVlans,
       "wwpLeosChassisResourcesMaxVlanMembers": wwpLeosChassisResourcesMaxVlanMembers,
       "wwpLeosChassisResourcesFreeVlanMembers": wwpLeosChassisResourcesFreeVlanMembers,
       "wwpLeosChassisResourcesMaxEprSnets": wwpLeosChassisResourcesMaxEprSnets,
       "wwpLeosChassisResourcesFreeEprSnets": wwpLeosChassisResourcesFreeEprSnets,
       "wwpLeosChassisResourcesMaxMcastSnets": wwpLeosChassisResourcesMaxMcastSnets,
       "wwpLeosChassisResourcesFreeMcastSnets": wwpLeosChassisResourcesFreeMcastSnets,
       "wwpLeosChassisResourcesMaxMcastGroups": wwpLeosChassisResourcesMaxMcastGroups,
       "wwpLeosChassisResourcesFreeMcastGroups": wwpLeosChassisResourcesFreeMcastGroups,
       "wwpLeosChassisResourcesMaxDhcpRelayAgnts": wwpLeosChassisResourcesMaxDhcpRelayAgnts,
       "wwpLeosChassisResourcesFreeDhcpRelayAgnts": wwpLeosChassisResourcesFreeDhcpRelayAgnts,
       "wwpLeosChassisResourcesMaxTunnels": wwpLeosChassisResourcesMaxTunnels,
       "wwpLeosChassisResourcesFreeTunnels": wwpLeosChassisResourcesFreeTunnels,
       "wwpLeosChassisResourcesMaxIngressTunnels": wwpLeosChassisResourcesMaxIngressTunnels,
       "wwpLeosChassisResourcesFreeIngressTunnels": wwpLeosChassisResourcesFreeIngressTunnels,
       "wwpLeosChassisResourcesMaxEgressTunnels": wwpLeosChassisResourcesMaxEgressTunnels,
       "wwpLeosChassisResourcesFreeEgressTunnels": wwpLeosChassisResourcesFreeEgressTunnels,
       "wwpLeosChassisResourcesMaxVcs": wwpLeosChassisResourcesMaxVcs,
       "wwpLeosChassisResourcesFreeVcs": wwpLeosChassisResourcesFreeVcs,
       "wwpLeosChassisResourcesMaxVss": wwpLeosChassisResourcesMaxVss,
       "wwpLeosChassisResourcesFreeVss": wwpLeosChassisResourcesFreeVss,
       "wwpLeosChassisResourcesMaxVsMembers": wwpLeosChassisResourcesMaxVsMembers,
       "wwpLeosChassisResourcesFreeVsMembers": wwpLeosChassisResourcesFreeVsMembers,
       "wwpLeosChassisResourcesMaxSlevelWcards": wwpLeosChassisResourcesMaxSlevelWcards,
       "wwpLeosChassisResourcesFreeSlevelWcards": wwpLeosChassisResourcesFreeSlevelWcards,
       "wwpLeosChassisResourcesMaxSlevels": wwpLeosChassisResourcesMaxSlevels,
       "wwpLeosChassisResourcesFreeSlevels": wwpLeosChassisResourcesFreeSlevels,
       "wwpLeosChassisResourcesMaxSmappings": wwpLeosChassisResourcesMaxSmappings,
       "wwpLeosChassisResourcesFreeSmappings": wwpLeosChassisResourcesFreeSmappings,
       "wwpLeosChassisResourcesMaxSmappingCosResources": wwpLeosChassisResourcesMaxSmappingCosResources,
       "wwpLeosChassisResourcesFreeSmappingCosResources": wwpLeosChassisResourcesFreeSmappingCosResources,
       "wwpLeosChassisResourcesMaxSmappingPrtclResources": wwpLeosChassisResourcesMaxSmappingPrtclResources,
       "wwpLeosChassisResourcesFreeSmappingPrtclResources": wwpLeosChassisResourcesFreeSmappingPrtclResources,
       "wwpLeosChassisResourcesMaxQosResEgs": wwpLeosChassisResourcesMaxQosResEgs,
       "wwpLeosChassisResourcesFreeQosResEgs": wwpLeosChassisResourcesFreeQosResEgs,
       "wwpLeosChassisResourcesMaxTprofGblCscdEntries": wwpLeosChassisResourcesMaxTprofGblCscdEntries,
       "wwpLeosChassisResourcesFreeTprofGblCscdEntries": wwpLeosChassisResourcesFreeTprofGblCscdEntries,
       "wwpLeosChassisResourcesMaxTprofCscdEntries": wwpLeosChassisResourcesMaxTprofCscdEntries,
       "wwpLeosChassisResourcesFreeTprofCscdEntries": wwpLeosChassisResourcesFreeTprofCscdEntries,
       "wwpLeosChassisResourcesMaxTprofStdEntries": wwpLeosChassisResourcesMaxTprofStdEntries,
       "wwpLeosChassisResourcesFreeTprofStdEntries": wwpLeosChassisResourcesFreeTprofStdEntries,
       "wwpLeosChassisResourcesMaxSaccessEntries": wwpLeosChassisResourcesMaxSaccessEntries,
       "wwpLeosChassisResourcesFreeSaccessEntries": wwpLeosChassisResourcesFreeSaccessEntries,
       "wwpLeosChassisResourcesMaxSmacEntries": wwpLeosChassisResourcesMaxSmacEntries,
       "wwpLeosChassisResourcesFreeSmacEntries": wwpLeosChassisResourcesFreeSmacEntries,
       "wwpLeosChassisResourcesMaxDrvNoLrnSacResources": wwpLeosChassisResourcesMaxDrvNoLrnSacResources,
       "wwpLeosChassisResourcesFreeDrvNoLrnSacResources": wwpLeosChassisResourcesFreeDrvNoLrnSacResources,
       "wwpLeosChassisResourcesMaxLearnEntries": wwpLeosChassisResourcesMaxLearnEntries,
       "wwpLeosChassisResourcesFreeLearnEntries": wwpLeosChassisResourcesFreeLearnEntries,
       "wwpLeosChassisResourcesMaxCustomPrtcls": wwpLeosChassisResourcesMaxCustomPrtcls,
       "wwpLeosChassisResourcesFreeCustomPrtcls": wwpLeosChassisResourcesFreeCustomPrtcls,
       "wwpLeosChassisResourcesMaxPrtcls": wwpLeosChassisResourcesMaxPrtcls,
       "wwpLeosChassisResourcesFreePrtcls": wwpLeosChassisResourcesFreePrtcls,
       "wwpLeosChassisResourcesMaxPrtclFilters": wwpLeosChassisResourcesMaxPrtclFilters,
       "wwpLeosChassisResourcesFreePrtclFilters": wwpLeosChassisResourcesFreePrtclFilters,
       "wwpLeosChassisResourcesMaxPrtclFilterMembs": wwpLeosChassisResourcesMaxPrtclFilterMembs,
       "wwpLeosChassisResourcesFreePrtclFilterMembs": wwpLeosChassisResourcesFreePrtclFilterMembs,
       "wwpLeosChassisResourcesMaxBcastFilters": wwpLeosChassisResourcesMaxBcastFilters,
       "wwpLeosChassisResourcesFreeBcastFilters": wwpLeosChassisResourcesFreeBcastFilters,
       "wwpLeosChassisResourcesMaxBcastFilterMembs": wwpLeosChassisResourcesMaxBcastFilterMembs,
       "wwpLeosChassisResourcesFreeBcastFilterMembs": wwpLeosChassisResourcesFreeBcastFilterMembs,
       "wwpLeosChassisNotifAttrs": wwpLeosChassisNotifAttrs,
       "wwpLeosChassisPostErrorCategory": wwpLeosChassisPostErrorCategory,
       "wwpLeosChassisPostErrorValue": wwpLeosChassisPostErrorValue,
       "wwpLeosChassisPostErrorCode": wwpLeosChassisPostErrorCode,
       "wwpLeosChassisPostErrorMsg": wwpLeosChassisPostErrorMsg,
       "wwpLeosChassisRebootReasonErrorType": wwpLeosChassisRebootReasonErrorType,
       "wwpLeosChassisSnmpState": wwpLeosChassisSnmpState,
       "wwpLeosChassisMIBNotificationPrefix": wwpLeosChassisMIBNotificationPrefix,
       "wwpLeosChassisMIBNotifications": wwpLeosChassisMIBNotifications,
       "wwpLeosChassisPowerSupplyStatusNotification": wwpLeosChassisPowerSupplyStatusNotification,
       "wwpLeosChassisFanModuleNotification": wwpLeosChassisFanModuleNotification,
       "wwpLeosChassisTempNotification": wwpLeosChassisTempNotification,
       "wwpLeosChassisPowerSwitchNotification": wwpLeosChassisPowerSwitchNotification,
       "wwpLeosChassisBatteryStatusNotification": wwpLeosChassisBatteryStatusNotification,
       "wwpLeosChassisBatteryVoltageLevelNotification": wwpLeosChassisBatteryVoltageLevelNotification,
       "wwpLeosChassisBatteryConditionNotification": wwpLeosChassisBatteryConditionNotification,
       "wwpLeosChassisPowerSourceNotification": wwpLeosChassisPowerSourceNotification,
       "wwpLeosChassisPostErrorNotification": wwpLeosChassisPostErrorNotification,
       "wwpLeosChassisRebootNotification": wwpLeosChassisRebootNotification,
       "wwpLeosChassisSnmpStateNotification": wwpLeosChassisSnmpStateNotification,
       "wwpLeosChassisDyingGaspNotification": wwpLeosChassisDyingGaspNotification,
       "wwpLeosChassisDoorStatusChangeNotification": wwpLeosChassisDoorStatusChangeNotification,
       "wwpLeosChassisInnerDoorStatusChangeNotification": wwpLeosChassisInnerDoorStatusChangeNotification,
       "wwpLeosChassisOuterDoorStatusChangeNotification": wwpLeosChassisOuterDoorStatusChangeNotification,
       "wwpLeosChassisExternalAlarmStatusChangeNotification": wwpLeosChassisExternalAlarmStatusChangeNotification,
       "wwpLeosChassisDoorAlarmStatusChangeNotification": wwpLeosChassisDoorAlarmStatusChangeNotification,
       "wwpLeosChassisMIBConformance": wwpLeosChassisMIBConformance,
       "wwpLeosChassisMIBCompliances": wwpLeosChassisMIBCompliances,
       "wwpLeosChassisMIBGroups": wwpLeosChassisMIBGroups}
)
