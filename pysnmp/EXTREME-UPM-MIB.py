# SNMP MIB module (EXTREME-UPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EXTREME-UPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:42:25 2024
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

(extremeAgent,) = mibBuilder.importSymbols(
    "EXTREME-BASE-MIB",
    "extremeAgent")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

extremeUpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UpmNotificationTrap_ObjectIdentity = ObjectIdentity
upmNotificationTrap = _UpmNotificationTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 1)
)
_UpmConfig_ObjectIdentity = ObjectIdentity
upmConfig = _UpmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2)
)


class _UpmProfileName_Type(DisplayString):
    """Custom type upmProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpmProfileName_Type.__name__ = "DisplayString"
_UpmProfileName_Object = MibScalar
upmProfileName = _UpmProfileName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 1),
    _UpmProfileName_Type()
)
upmProfileName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmProfileName.setStatus("current")


class _UpmExecutionId_Type(Unsigned32):
    """Custom type upmExecutionId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967296),
    )


_UpmExecutionId_Type.__name__ = "Unsigned32"
_UpmExecutionId_Object = MibScalar
upmExecutionId = _UpmExecutionId_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 2),
    _UpmExecutionId_Type()
)
upmExecutionId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmExecutionId.setStatus("current")


class _UpmEventType_Type(Integer32):
    """Custom type upmEventType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("devicedetect", 1),
          ("deviceundetect", 2),
          ("upmTimer", 5),
          ("userauthenticated", 3),
          ("userrequest", 7),
          ("userunauthenticated", 4))
    )


_UpmEventType_Type.__name__ = "Integer32"
_UpmEventType_Object = MibScalar
upmEventType = _UpmEventType_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 3),
    _UpmEventType_Type()
)
upmEventType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmEventType.setStatus("current")


class _UpmExecutionStatus_Type(Integer32):
    """Custom type upmExecutionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_UpmExecutionStatus_Type.__name__ = "Integer32"
_UpmExecutionStatus_Object = MibScalar
upmExecutionStatus = _UpmExecutionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 4),
    _UpmExecutionStatus_Type()
)
upmExecutionStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmExecutionStatus.setStatus("current")


class _UpmPort_Type(Integer32):
    """Custom type upmPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967296),
    )


_UpmPort_Type.__name__ = "Integer32"
_UpmPort_Object = MibScalar
upmPort = _UpmPort_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 5),
    _UpmPort_Type()
)
upmPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmPort.setStatus("current")


class _UpmProfileExecVars_Type(DisplayString):
    """Custom type upmProfileExecVars based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_UpmProfileExecVars_Type.__name__ = "DisplayString"
_UpmProfileExecVars_Object = MibScalar
upmProfileExecVars = _UpmProfileExecVars_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 6),
    _UpmProfileExecVars_Type()
)
upmProfileExecVars.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmProfileExecVars.setStatus("current")


class _UpmTimerName_Type(DisplayString):
    """Custom type upmTimerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_UpmTimerName_Type.__name__ = "DisplayString"
_UpmTimerName_Object = MibScalar
upmTimerName = _UpmTimerName_Object(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 2, 7),
    _UpmTimerName_Type()
)
upmTimerName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    upmTimerName.setStatus("current")

# Managed Objects groups


# Notification objects

upmProfileEventExecution = NotificationType(
    (1, 3, 6, 1, 4, 1, 1916, 1, 35, 1, 1)
)
upmProfileEventExecution.setObjects(
      *(("EXTREME-UPM-MIB", "upmProfileName"),
        ("EXTREME-UPM-MIB", "upmExecutionId"),
        ("EXTREME-UPM-MIB", "upmEventType"),
        ("EXTREME-UPM-MIB", "upmExecutionStatus"),
        ("EXTREME-UPM-MIB", "upmPort"),
        ("EXTREME-UPM-MIB", "upmProfileExecVars"),
        ("EXTREME-UPM-MIB", "upmTimerName"))
)
if mibBuilder.loadTexts:
    upmProfileEventExecution.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-UPM-MIB",
    **{"extremeUpm": extremeUpm,
       "upmNotificationTrap": upmNotificationTrap,
       "upmProfileEventExecution": upmProfileEventExecution,
       "upmConfig": upmConfig,
       "upmProfileName": upmProfileName,
       "upmExecutionId": upmExecutionId,
       "upmEventType": upmEventType,
       "upmExecutionStatus": upmExecutionStatus,
       "upmPort": upmPort,
       "upmProfileExecVars": upmProfileExecVars,
       "upmTimerName": upmTimerName}
)
