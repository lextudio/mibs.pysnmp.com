# SNMP MIB module (DNOS-OUTBOUNDTELNET-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DNOS-OUTBOUNDTELNET-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:09 2024
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

(dnOS,) = mibBuilder.importSymbols(
    "DELL-REF-MIB",
    "dnOS")

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

fastPathOutboundTelnetPrivate = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19)
)
fastPathOutboundTelnetPrivate.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentOutboundTelnetGroup_ObjectIdentity = ObjectIdentity
agentOutboundTelnetGroup = _AgentOutboundTelnetGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1)
)


class _AgentOutboundTelnetAdminMode_Type(Integer32):
    """Custom type agentOutboundTelnetAdminMode based on Integer32"""
    defaultValue = 1

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


_AgentOutboundTelnetAdminMode_Type.__name__ = "Integer32"
_AgentOutboundTelnetAdminMode_Object = MibScalar
agentOutboundTelnetAdminMode = _AgentOutboundTelnetAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 1),
    _AgentOutboundTelnetAdminMode_Type()
)
agentOutboundTelnetAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundTelnetAdminMode.setStatus("current")


class _AgentOutboundTelnetMaxNoOfSessions_Type(Integer32):
    """Custom type agentOutboundTelnetMaxNoOfSessions based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AgentOutboundTelnetMaxNoOfSessions_Type.__name__ = "Integer32"
_AgentOutboundTelnetMaxNoOfSessions_Object = MibScalar
agentOutboundTelnetMaxNoOfSessions = _AgentOutboundTelnetMaxNoOfSessions_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 2),
    _AgentOutboundTelnetMaxNoOfSessions_Type()
)
agentOutboundTelnetMaxNoOfSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundTelnetMaxNoOfSessions.setStatus("current")


class _AgentOutboundTelnetTimeout_Type(Integer32):
    """Custom type agentOutboundTelnetTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentOutboundTelnetTimeout_Type.__name__ = "Integer32"
_AgentOutboundTelnetTimeout_Object = MibScalar
agentOutboundTelnetTimeout = _AgentOutboundTelnetTimeout_Object(
    (1, 3, 6, 1, 4, 1, 674, 10895, 5000, 2, 6132, 1, 1, 19, 1, 3),
    _AgentOutboundTelnetTimeout_Type()
)
agentOutboundTelnetTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentOutboundTelnetTimeout.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DNOS-OUTBOUNDTELNET-PRIVATE-MIB",
    **{"fastPathOutboundTelnetPrivate": fastPathOutboundTelnetPrivate,
       "agentOutboundTelnetGroup": agentOutboundTelnetGroup,
       "agentOutboundTelnetAdminMode": agentOutboundTelnetAdminMode,
       "agentOutboundTelnetMaxNoOfSessions": agentOutboundTelnetMaxNoOfSessions,
       "agentOutboundTelnetTimeout": agentOutboundTelnetTimeout}
)
