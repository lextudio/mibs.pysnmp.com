# SNMP MIB module (ZHONE-CONSOLE) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-CONSOLE
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:26 2024
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
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp")

(zhoneConsole,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneConsole",
    "zhoneModules")

(ZhoneAdminString,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAdminString")


# MODULE-IDENTITY

phyConsole = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 14)
)
phyConsole.setRevisions(
        ("2000-11-06 09:30",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ConsoleHeight_Type(Integer32):
    """Custom type consoleHeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 120),
    )


_ConsoleHeight_Type.__name__ = "Integer32"
_ConsoleHeight_Object = MibScalar
consoleHeight = _ConsoleHeight_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 1),
    _ConsoleHeight_Type()
)
consoleHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleHeight.setStatus("current")
_ConsoleCurrentUser_Type = ZhoneAdminString
_ConsoleCurrentUser_Object = MibScalar
consoleCurrentUser = _ConsoleCurrentUser_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 2),
    _ConsoleCurrentUser_Type()
)
consoleCurrentUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleCurrentUser.setStatus("current")
_ConsoleLastLoginTime_Type = TimeStamp
_ConsoleLastLoginTime_Object = MibScalar
consoleLastLoginTime = _ConsoleLastLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 3),
    _ConsoleLastLoginTime_Type()
)
consoleLastLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleLastLoginTime.setStatus("current")
_ConsoleLastLogoutTime_Type = TimeStamp
_ConsoleLastLogoutTime_Object = MibScalar
consoleLastLogoutTime = _ConsoleLastLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 4),
    _ConsoleLastLogoutTime_Type()
)
consoleLastLogoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleLastLogoutTime.setStatus("current")
_ConsoleCharsOut_Type = Counter32
_ConsoleCharsOut_Object = MibScalar
consoleCharsOut = _ConsoleCharsOut_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 5),
    _ConsoleCharsOut_Type()
)
consoleCharsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleCharsOut.setStatus("current")
_ConsoleCharsIn_Type = Counter32
_ConsoleCharsIn_Object = MibScalar
consoleCharsIn = _ConsoleCharsIn_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 6),
    _ConsoleCharsIn_Type()
)
consoleCharsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleCharsIn.setStatus("current")


class _ConsoleBaudRate_Type(Integer32):
    """Custom type consoleBaudRate based on Integer32"""
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
        *(("gc19200", 3),
          ("gc38400", 4),
          ("gc57600", 5),
          ("gc9600", 2),
          ("gcAutoBaud", 1))
    )


_ConsoleBaudRate_Type.__name__ = "Integer32"
_ConsoleBaudRate_Object = MibScalar
consoleBaudRate = _ConsoleBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 7),
    _ConsoleBaudRate_Type()
)
consoleBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleBaudRate.setStatus("current")


class _ConsoleInactivityTime_Type(Integer32):
    """Custom type consoleInactivityTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_ConsoleInactivityTime_Type.__name__ = "Integer32"
_ConsoleInactivityTime_Object = MibScalar
consoleInactivityTime = _ConsoleInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 5, 8),
    _ConsoleInactivityTime_Type()
)
consoleInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleInactivityTime.setStatus("current")
if mibBuilder.loadTexts:
    consoleInactivityTime.setUnits("minutes")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-CONSOLE",
    **{"consoleHeight": consoleHeight,
       "consoleCurrentUser": consoleCurrentUser,
       "consoleLastLoginTime": consoleLastLoginTime,
       "consoleLastLogoutTime": consoleLastLogoutTime,
       "consoleCharsOut": consoleCharsOut,
       "consoleCharsIn": consoleCharsIn,
       "consoleBaudRate": consoleBaudRate,
       "consoleInactivityTime": consoleInactivityTime,
       "phyConsole": phyConsole}
)
