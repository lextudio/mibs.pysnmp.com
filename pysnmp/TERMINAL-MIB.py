# SNMP MIB module (TERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TERMINAL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:01:28 2024
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

(terminalMgmt,) = mibBuilder.importSymbols(
    "APENT-MIB",
    "terminalMgmt")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

terminalMgrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _ApTermSessIdleTimeout_Type(Integer32):
    """Custom type apTermSessIdleTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ApTermSessIdleTimeout_Type.__name__ = "Integer32"
_ApTermSessIdleTimeout_Object = MibScalar
apTermSessIdleTimeout = _ApTermSessIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 2),
    _ApTermSessIdleTimeout_Type()
)
apTermSessIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessIdleTimeout.setStatus("current")


class _ApTermSessLoginFailureInfo_Type(DisplayString):
    """Custom type apTermSessLoginFailureInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_ApTermSessLoginFailureInfo_Type.__name__ = "DisplayString"
_ApTermSessLoginFailureInfo_Object = MibScalar
apTermSessLoginFailureInfo = _ApTermSessLoginFailureInfo_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 3),
    _ApTermSessLoginFailureInfo_Type()
)
apTermSessLoginFailureInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    apTermSessLoginFailureInfo.setStatus("current")


class _ApTermSessTelnetDisallowed_Type(Integer32):
    """Custom type apTermSessTelnetDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessTelnetDisallowed_Type.__name__ = "Integer32"
_ApTermSessTelnetDisallowed_Object = MibScalar
apTermSessTelnetDisallowed = _ApTermSessTelnetDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 4),
    _ApTermSessTelnetDisallowed_Type()
)
apTermSessTelnetDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessTelnetDisallowed.setStatus("current")


class _ApTermSessConsoleDisallowed_Type(Integer32):
    """Custom type apTermSessConsoleDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessConsoleDisallowed_Type.__name__ = "Integer32"
_ApTermSessConsoleDisallowed_Object = MibScalar
apTermSessConsoleDisallowed = _ApTermSessConsoleDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 5),
    _ApTermSessConsoleDisallowed_Type()
)
apTermSessConsoleDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessConsoleDisallowed.setStatus("current")


class _ApTermSessSNMPDisallowed_Type(Integer32):
    """Custom type apTermSessSNMPDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessSNMPDisallowed_Type.__name__ = "Integer32"
_ApTermSessSNMPDisallowed_Object = MibScalar
apTermSessSNMPDisallowed = _ApTermSessSNMPDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 6),
    _ApTermSessSNMPDisallowed_Type()
)
apTermSessSNMPDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessSNMPDisallowed.setStatus("current")


class _ApTermSessFTPDisallowed_Type(Integer32):
    """Custom type apTermSessFTPDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessFTPDisallowed_Type.__name__ = "Integer32"
_ApTermSessFTPDisallowed_Object = MibScalar
apTermSessFTPDisallowed = _ApTermSessFTPDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 7),
    _ApTermSessFTPDisallowed_Type()
)
apTermSessFTPDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessFTPDisallowed.setStatus("current")


class _ApTermSessEuroDateDisplay_Type(Integer32):
    """Custom type apTermSessEuroDateDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessEuroDateDisplay_Type.__name__ = "Integer32"
_ApTermSessEuroDateDisplay_Object = MibScalar
apTermSessEuroDateDisplay = _ApTermSessEuroDateDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 8),
    _ApTermSessEuroDateDisplay_Type()
)
apTermSessEuroDateDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessEuroDateDisplay.setStatus("current")


class _ApTermSessXMLDisallowed_Type(Integer32):
    """Custom type apTermSessXMLDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessXMLDisallowed_Type.__name__ = "Integer32"
_ApTermSessXMLDisallowed_Object = MibScalar
apTermSessXMLDisallowed = _ApTermSessXMLDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 9),
    _ApTermSessXMLDisallowed_Type()
)
apTermSessXMLDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessXMLDisallowed.setStatus("current")


class _ApTermSessWebMgmtDisallowed_Type(Integer32):
    """Custom type apTermSessWebMgmtDisallowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ApTermSessWebMgmtDisallowed_Type.__name__ = "Integer32"
_ApTermSessWebMgmtDisallowed_Object = MibScalar
apTermSessWebMgmtDisallowed = _ApTermSessWebMgmtDisallowed_Object(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 10),
    _ApTermSessWebMgmtDisallowed_Type()
)
apTermSessWebMgmtDisallowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    apTermSessWebMgmtDisallowed.setStatus("current")

# Managed Objects groups


# Notification objects

apTermSessLoginFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2467, 1, 11, 0, 1)
)
apTermSessLoginFailureTrap.setObjects(
    ("TERMINAL-MIB", "apTermSessLoginFailureInfo")
)
if mibBuilder.loadTexts:
    apTermSessLoginFailureTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TERMINAL-MIB",
    **{"apTermSessLoginFailureTrap": apTermSessLoginFailureTrap,
       "terminalMgrMib": terminalMgrMib,
       "apTermSessIdleTimeout": apTermSessIdleTimeout,
       "apTermSessLoginFailureInfo": apTermSessLoginFailureInfo,
       "apTermSessTelnetDisallowed": apTermSessTelnetDisallowed,
       "apTermSessConsoleDisallowed": apTermSessConsoleDisallowed,
       "apTermSessSNMPDisallowed": apTermSessSNMPDisallowed,
       "apTermSessFTPDisallowed": apTermSessFTPDisallowed,
       "apTermSessEuroDateDisplay": apTermSessEuroDateDisplay,
       "apTermSessXMLDisallowed": apTermSessXMLDisallowed,
       "apTermSessWebMgmtDisallowed": apTermSessWebMgmtDisallowed}
)
