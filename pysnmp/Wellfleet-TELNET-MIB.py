# SNMP MIB module (Wellfleet-TELNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-TELNET-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:18 2024
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

(wfTelnetGroup,) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfTelnetGroup")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfTelnet_ObjectIdentity = ObjectIdentity
wfTelnet = _WfTelnet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1)
)


class _WfTelnetDelete_Type(Integer32):
    """Custom type wfTelnetDelete based on Integer32"""
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


_WfTelnetDelete_Type.__name__ = "Integer32"
_WfTelnetDelete_Object = MibScalar
wfTelnetDelete = _WfTelnetDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 1),
    _WfTelnetDelete_Type()
)
wfTelnetDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDelete.setStatus("mandatory")


class _WfTelnetDisable_Type(Integer32):
    """Custom type wfTelnetDisable based on Integer32"""
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


_WfTelnetDisable_Type.__name__ = "Integer32"
_WfTelnetDisable_Object = MibScalar
wfTelnetDisable = _WfTelnetDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 2),
    _WfTelnetDisable_Type()
)
wfTelnetDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDisable.setStatus("mandatory")


class _WfTelnetLinesPerScreen_Type(Integer32):
    """Custom type wfTelnetLinesPerScreen based on Integer32"""
    defaultValue = 24


_WfTelnetLinesPerScreen_Object = MibScalar
wfTelnetLinesPerScreen = _WfTelnetLinesPerScreen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 3),
    _WfTelnetLinesPerScreen_Type()
)
wfTelnetLinesPerScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetLinesPerScreen.setStatus("mandatory")


class _WfTelnetMoreDisable_Type(Integer32):
    """Custom type wfTelnetMoreDisable based on Integer32"""
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


_WfTelnetMoreDisable_Type.__name__ = "Integer32"
_WfTelnetMoreDisable_Object = MibScalar
wfTelnetMoreDisable = _WfTelnetMoreDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 4),
    _WfTelnetMoreDisable_Type()
)
wfTelnetMoreDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetMoreDisable.setStatus("mandatory")
_WfTelnetPrompt_Type = DisplayString
_WfTelnetPrompt_Object = MibScalar
wfTelnetPrompt = _WfTelnetPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 5),
    _WfTelnetPrompt_Type()
)
wfTelnetPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetPrompt.setStatus("mandatory")


class _WfTelnetLoginTimeOut_Type(Integer32):
    """Custom type wfTelnetLoginTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfTelnetLoginTimeOut_Type.__name__ = "Integer32"
_WfTelnetLoginTimeOut_Object = MibScalar
wfTelnetLoginTimeOut = _WfTelnetLoginTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 6),
    _WfTelnetLoginTimeOut_Type()
)
wfTelnetLoginTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetLoginTimeOut.setStatus("mandatory")


class _WfTelnetPasswordTimeOut_Type(Integer32):
    """Custom type wfTelnetPasswordTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfTelnetPasswordTimeOut_Type.__name__ = "Integer32"
_WfTelnetPasswordTimeOut_Object = MibScalar
wfTelnetPasswordTimeOut = _WfTelnetPasswordTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 7),
    _WfTelnetPasswordTimeOut_Type()
)
wfTelnetPasswordTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetPasswordTimeOut.setStatus("mandatory")


class _WfTelnetCommandTimeOut_Type(Integer32):
    """Custom type wfTelnetCommandTimeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfTelnetCommandTimeOut_Type.__name__ = "Integer32"
_WfTelnetCommandTimeOut_Object = MibScalar
wfTelnetCommandTimeOut = _WfTelnetCommandTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 8),
    _WfTelnetCommandTimeOut_Type()
)
wfTelnetCommandTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetCommandTimeOut.setStatus("mandatory")


class _WfTelnetLoginRetries_Type(Integer32):
    """Custom type wfTelnetLoginRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfTelnetLoginRetries_Type.__name__ = "Integer32"
_WfTelnetLoginRetries_Object = MibScalar
wfTelnetLoginRetries = _WfTelnetLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 9),
    _WfTelnetLoginRetries_Type()
)
wfTelnetLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetLoginRetries.setStatus("mandatory")
_WfTelnetTotalLogins_Type = Counter32
_WfTelnetTotalLogins_Object = MibScalar
wfTelnetTotalLogins = _WfTelnetTotalLogins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 10),
    _WfTelnetTotalLogins_Type()
)
wfTelnetTotalLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetTotalLogins.setStatus("mandatory")
_WfTelnetUserLoginErrors_Type = Counter32
_WfTelnetUserLoginErrors_Object = MibScalar
wfTelnetUserLoginErrors = _WfTelnetUserLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 11),
    _WfTelnetUserLoginErrors_Type()
)
wfTelnetUserLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetUserLoginErrors.setStatus("mandatory")
_WfTelnetManagerLoginErrors_Type = Counter32
_WfTelnetManagerLoginErrors_Object = MibScalar
wfTelnetManagerLoginErrors = _WfTelnetManagerLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 12),
    _WfTelnetManagerLoginErrors_Type()
)
wfTelnetManagerLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetManagerLoginErrors.setStatus("mandatory")
_WfTelnetOtherLoginErrors_Type = Counter32
_WfTelnetOtherLoginErrors_Object = MibScalar
wfTelnetOtherLoginErrors = _WfTelnetOtherLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 13),
    _WfTelnetOtherLoginErrors_Type()
)
wfTelnetOtherLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetOtherLoginErrors.setStatus("mandatory")
_WfTelnetActiveSessions_Type = Gauge32
_WfTelnetActiveSessions_Object = MibScalar
wfTelnetActiveSessions = _WfTelnetActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 14),
    _WfTelnetActiveSessions_Type()
)
wfTelnetActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetActiveSessions.setStatus("mandatory")


class _WfTelnetDiagnosticReport_Type(Integer32):
    """Custom type wfTelnetDiagnosticReport based on Integer32"""
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


_WfTelnetDiagnosticReport_Type.__name__ = "Integer32"
_WfTelnetDiagnosticReport_Object = MibScalar
wfTelnetDiagnosticReport = _WfTelnetDiagnosticReport_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 15),
    _WfTelnetDiagnosticReport_Type()
)
wfTelnetDiagnosticReport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDiagnosticReport.setStatus("mandatory")


class _WfTelnetDiagnosticExercise_Type(Integer32):
    """Custom type wfTelnetDiagnosticExercise based on Integer32"""
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


_WfTelnetDiagnosticExercise_Type.__name__ = "Integer32"
_WfTelnetDiagnosticExercise_Object = MibScalar
wfTelnetDiagnosticExercise = _WfTelnetDiagnosticExercise_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 16),
    _WfTelnetDiagnosticExercise_Type()
)
wfTelnetDiagnosticExercise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDiagnosticExercise.setStatus("mandatory")


class _WfTelnetDiagnosticNetworkData_Type(Integer32):
    """Custom type wfTelnetDiagnosticNetworkData based on Integer32"""
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


_WfTelnetDiagnosticNetworkData_Type.__name__ = "Integer32"
_WfTelnetDiagnosticNetworkData_Object = MibScalar
wfTelnetDiagnosticNetworkData = _WfTelnetDiagnosticNetworkData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 17),
    _WfTelnetDiagnosticNetworkData_Type()
)
wfTelnetDiagnosticNetworkData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDiagnosticNetworkData.setStatus("mandatory")


class _WfTelnetDiagnosticPtyData_Type(Integer32):
    """Custom type wfTelnetDiagnosticPtyData based on Integer32"""
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


_WfTelnetDiagnosticPtyData_Type.__name__ = "Integer32"
_WfTelnetDiagnosticPtyData_Object = MibScalar
wfTelnetDiagnosticPtyData = _WfTelnetDiagnosticPtyData_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 18),
    _WfTelnetDiagnosticPtyData_Type()
)
wfTelnetDiagnosticPtyData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDiagnosticPtyData.setStatus("mandatory")


class _WfTelnetDiagnosticOptions_Type(Integer32):
    """Custom type wfTelnetDiagnosticOptions based on Integer32"""
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


_WfTelnetDiagnosticOptions_Type.__name__ = "Integer32"
_WfTelnetDiagnosticOptions_Object = MibScalar
wfTelnetDiagnosticOptions = _WfTelnetDiagnosticOptions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 19),
    _WfTelnetDiagnosticOptions_Type()
)
wfTelnetDiagnosticOptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetDiagnosticOptions.setStatus("mandatory")
_WfTelnetInitialSearchPath_Type = DisplayString
_WfTelnetInitialSearchPath_Object = MibScalar
wfTelnetInitialSearchPath = _WfTelnetInitialSearchPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 20),
    _WfTelnetInitialSearchPath_Type()
)
wfTelnetInitialSearchPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetInitialSearchPath.setStatus("obsolete")
_WfTelnetManagerAutoScript_Type = DisplayString
_WfTelnetManagerAutoScript_Object = MibScalar
wfTelnetManagerAutoScript = _WfTelnetManagerAutoScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 21),
    _WfTelnetManagerAutoScript_Type()
)
wfTelnetManagerAutoScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetManagerAutoScript.setStatus("mandatory")
_WfTelnetUserAutoScript_Type = DisplayString
_WfTelnetUserAutoScript_Object = MibScalar
wfTelnetUserAutoScript = _WfTelnetUserAutoScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 22),
    _WfTelnetUserAutoScript_Type()
)
wfTelnetUserAutoScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetUserAutoScript.setStatus("mandatory")


class _WfTelnetUserAbortLogoutDisable_Type(Integer32):
    """Custom type wfTelnetUserAbortLogoutDisable based on Integer32"""
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


_WfTelnetUserAbortLogoutDisable_Type.__name__ = "Integer32"
_WfTelnetUserAbortLogoutDisable_Object = MibScalar
wfTelnetUserAbortLogoutDisable = _WfTelnetUserAbortLogoutDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 23),
    _WfTelnetUserAbortLogoutDisable_Type()
)
wfTelnetUserAbortLogoutDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetUserAbortLogoutDisable.setStatus("mandatory")


class _WfTelnetHistoryDepth_Type(Integer32):
    """Custom type wfTelnetHistoryDepth based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_WfTelnetHistoryDepth_Type.__name__ = "Integer32"
_WfTelnetHistoryDepth_Object = MibScalar
wfTelnetHistoryDepth = _WfTelnetHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 24),
    _WfTelnetHistoryDepth_Type()
)
wfTelnetHistoryDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetHistoryDepth.setStatus("mandatory")


class _WfTelnetReverseEnable_Type(Integer32):
    """Custom type wfTelnetReverseEnable based on Integer32"""
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


_WfTelnetReverseEnable_Type.__name__ = "Integer32"
_WfTelnetReverseEnable_Object = MibScalar
wfTelnetReverseEnable = _WfTelnetReverseEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 25),
    _WfTelnetReverseEnable_Type()
)
wfTelnetReverseEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetReverseEnable.setStatus("mandatory")


class _WfTelnetReversePort_Type(Integer32):
    """Custom type wfTelnetReversePort based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_WfTelnetReversePort_Type.__name__ = "Integer32"
_WfTelnetReversePort_Object = MibScalar
wfTelnetReversePort = _WfTelnetReversePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 1, 26),
    _WfTelnetReversePort_Type()
)
wfTelnetReversePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetReversePort.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-TELNET-MIB",
    **{"wfTelnet": wfTelnet,
       "wfTelnetDelete": wfTelnetDelete,
       "wfTelnetDisable": wfTelnetDisable,
       "wfTelnetLinesPerScreen": wfTelnetLinesPerScreen,
       "wfTelnetMoreDisable": wfTelnetMoreDisable,
       "wfTelnetPrompt": wfTelnetPrompt,
       "wfTelnetLoginTimeOut": wfTelnetLoginTimeOut,
       "wfTelnetPasswordTimeOut": wfTelnetPasswordTimeOut,
       "wfTelnetCommandTimeOut": wfTelnetCommandTimeOut,
       "wfTelnetLoginRetries": wfTelnetLoginRetries,
       "wfTelnetTotalLogins": wfTelnetTotalLogins,
       "wfTelnetUserLoginErrors": wfTelnetUserLoginErrors,
       "wfTelnetManagerLoginErrors": wfTelnetManagerLoginErrors,
       "wfTelnetOtherLoginErrors": wfTelnetOtherLoginErrors,
       "wfTelnetActiveSessions": wfTelnetActiveSessions,
       "wfTelnetDiagnosticReport": wfTelnetDiagnosticReport,
       "wfTelnetDiagnosticExercise": wfTelnetDiagnosticExercise,
       "wfTelnetDiagnosticNetworkData": wfTelnetDiagnosticNetworkData,
       "wfTelnetDiagnosticPtyData": wfTelnetDiagnosticPtyData,
       "wfTelnetDiagnosticOptions": wfTelnetDiagnosticOptions,
       "wfTelnetInitialSearchPath": wfTelnetInitialSearchPath,
       "wfTelnetManagerAutoScript": wfTelnetManagerAutoScript,
       "wfTelnetUserAutoScript": wfTelnetUserAutoScript,
       "wfTelnetUserAbortLogoutDisable": wfTelnetUserAbortLogoutDisable,
       "wfTelnetHistoryDepth": wfTelnetHistoryDepth,
       "wfTelnetReverseEnable": wfTelnetReverseEnable,
       "wfTelnetReversePort": wfTelnetReversePort}
)
