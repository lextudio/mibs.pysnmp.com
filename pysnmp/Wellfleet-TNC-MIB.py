# SNMP MIB module (Wellfleet-TNC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-TNC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:20 2024
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

_WfTelnetClient_ObjectIdentity = ObjectIdentity
wfTelnetClient = _WfTelnetClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2)
)


class _WfTelnetClientDelete_Type(Integer32):
    """Custom type wfTelnetClientDelete based on Integer32"""
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


_WfTelnetClientDelete_Type.__name__ = "Integer32"
_WfTelnetClientDelete_Object = MibScalar
wfTelnetClientDelete = _WfTelnetClientDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 1),
    _WfTelnetClientDelete_Type()
)
wfTelnetClientDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetClientDelete.setStatus("mandatory")


class _WfTelnetClientDisable_Type(Integer32):
    """Custom type wfTelnetClientDisable based on Integer32"""
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


_WfTelnetClientDisable_Type.__name__ = "Integer32"
_WfTelnetClientDisable_Object = MibScalar
wfTelnetClientDisable = _WfTelnetClientDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 2),
    _WfTelnetClientDisable_Type()
)
wfTelnetClientDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetClientDisable.setStatus("mandatory")


class _WfTelnetClientDebug_Type(Integer32):
    """Custom type wfTelnetClientDebug based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_WfTelnetClientDebug_Type.__name__ = "Integer32"
_WfTelnetClientDebug_Object = MibScalar
wfTelnetClientDebug = _WfTelnetClientDebug_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 3),
    _WfTelnetClientDebug_Type()
)
wfTelnetClientDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetClientDebug.setStatus("mandatory")


class _WfTelnetClientRemotePort_Type(Integer32):
    """Custom type wfTelnetClientRemotePort based on Integer32"""
    defaultValue = 23


_WfTelnetClientRemotePort_Object = MibScalar
wfTelnetClientRemotePort = _WfTelnetClientRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 4),
    _WfTelnetClientRemotePort_Type()
)
wfTelnetClientRemotePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetClientRemotePort.setStatus("mandatory")
_WfTelnetClientPrompt_Type = DisplayString
_WfTelnetClientPrompt_Object = MibScalar
wfTelnetClientPrompt = _WfTelnetClientPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 5),
    _WfTelnetClientPrompt_Type()
)
wfTelnetClientPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfTelnetClientPrompt.setStatus("mandatory")
_WfTelnetClientActiveSessions_Type = Gauge32
_WfTelnetClientActiveSessions_Object = MibScalar
wfTelnetClientActiveSessions = _WfTelnetClientActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 6),
    _WfTelnetClientActiveSessions_Type()
)
wfTelnetClientActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetClientActiveSessions.setStatus("mandatory")
_WfTelnetClientTotalSessions_Type = Counter32
_WfTelnetClientTotalSessions_Object = MibScalar
wfTelnetClientTotalSessions = _WfTelnetClientTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 5, 3, 7, 2, 7),
    _WfTelnetClientTotalSessions_Type()
)
wfTelnetClientTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTelnetClientTotalSessions.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-TNC-MIB",
    **{"wfTelnetClient": wfTelnetClient,
       "wfTelnetClientDelete": wfTelnetClientDelete,
       "wfTelnetClientDisable": wfTelnetClientDisable,
       "wfTelnetClientDebug": wfTelnetClientDebug,
       "wfTelnetClientRemotePort": wfTelnetClientRemotePort,
       "wfTelnetClientPrompt": wfTelnetClientPrompt,
       "wfTelnetClientActiveSessions": wfTelnetClientActiveSessions,
       "wfTelnetClientTotalSessions": wfTelnetClientTotalSessions}
)
