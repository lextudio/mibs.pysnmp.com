# SNMP MIB module (FSM7326-MGMT-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FSM7326-MGMT-SECURITY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:31 2024
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

(fsm7326,) = mibBuilder.importSymbols(
    "FSM7326-REF-MIB",
    "fsm7326")

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


# MODULE-IDENTITY

fsm7326MgmtSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11)
)
fsm7326MgmtSecurity.setRevisions(
        ("2003-11-21 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentSSLConfigGroup_ObjectIdentity = ObjectIdentity
agentSSLConfigGroup = _AgentSSLConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1)
)


class _AgentSSLAdminMode_Type(Integer32):
    """Custom type agentSSLAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSSLAdminMode_Type.__name__ = "Integer32"
_AgentSSLAdminMode_Object = MibScalar
agentSSLAdminMode = _AgentSSLAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1, 1),
    _AgentSSLAdminMode_Type()
)
agentSSLAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLAdminMode.setStatus("current")


class _AgentSSLSecurePort_Type(Integer32):
    """Custom type agentSSLSecurePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentSSLSecurePort_Type.__name__ = "Integer32"
_AgentSSLSecurePort_Object = MibScalar
agentSSLSecurePort = _AgentSSLSecurePort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1, 2),
    _AgentSSLSecurePort_Type()
)
agentSSLSecurePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLSecurePort.setStatus("current")


class _AgentSSLProtocolLevel_Type(Integer32):
    """Custom type agentSSLProtocolLevel based on Integer32"""
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
          ("ssl30", 1),
          ("tls10", 2))
    )


_AgentSSLProtocolLevel_Type.__name__ = "Integer32"
_AgentSSLProtocolLevel_Object = MibScalar
agentSSLProtocolLevel = _AgentSSLProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 1, 3),
    _AgentSSLProtocolLevel_Type()
)
agentSSLProtocolLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSLProtocolLevel.setStatus("current")
_AgentSSHConfigGroup_ObjectIdentity = ObjectIdentity
agentSSHConfigGroup = _AgentSSHConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2)
)


class _AgentSSHAdminMode_Type(Integer32):
    """Custom type agentSSHAdminMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_AgentSSHAdminMode_Type.__name__ = "Integer32"
_AgentSSHAdminMode_Object = MibScalar
agentSSHAdminMode = _AgentSSHAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2, 1),
    _AgentSSHAdminMode_Type()
)
agentSSHAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHAdminMode.setStatus("current")


class _AgentSSHProtocolLevel_Type(Integer32):
    """Custom type agentSSHProtocolLevel based on Integer32"""
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
          ("ssh10", 1),
          ("ssh20", 2))
    )


_AgentSSHProtocolLevel_Type.__name__ = "Integer32"
_AgentSSHProtocolLevel_Object = MibScalar
agentSSHProtocolLevel = _AgentSSHProtocolLevel_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2, 2),
    _AgentSSHProtocolLevel_Type()
)
agentSSHProtocolLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentSSHProtocolLevel.setStatus("current")
_AgentSSHSessionsCount_Type = Integer32
_AgentSSHSessionsCount_Object = MibScalar
agentSSHSessionsCount = _AgentSSHSessionsCount_Object(
    (1, 3, 6, 1, 4, 1, 4526, 1, 9, 11, 2, 3),
    _AgentSSHSessionsCount_Type()
)
agentSSHSessionsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentSSHSessionsCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSM7326-MGMT-SECURITY-MIB",
    **{"fsm7326MgmtSecurity": fsm7326MgmtSecurity,
       "agentSSLConfigGroup": agentSSLConfigGroup,
       "agentSSLAdminMode": agentSSLAdminMode,
       "agentSSLSecurePort": agentSSLSecurePort,
       "agentSSLProtocolLevel": agentSSLProtocolLevel,
       "agentSSHConfigGroup": agentSSHConfigGroup,
       "agentSSHAdminMode": agentSSHAdminMode,
       "agentSSHProtocolLevel": agentSSHProtocolLevel,
       "agentSSHSessionsCount": agentSSHSessionsCount}
)
