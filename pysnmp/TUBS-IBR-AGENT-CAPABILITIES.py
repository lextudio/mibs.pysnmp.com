# SNMP MIB module (TUBS-IBR-AGENT-CAPABILITIES) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TUBS-IBR-AGENT-CAPABILITIES
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:53 2024
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

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

(ibr,) = mibBuilder.importSymbols(
    "TUBS-SMI",
    "ibr")


# MODULE-IDENTITY

ibrAgentCapabilities = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 6)
)
ibrAgentCapabilities.setRevisions(
        ("2000-02-09 00:00",
         "1998-08-05 16:23",
         "1997-02-14 10:23")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Linux_ObjectIdentity = ObjectIdentity
linux = _Linux_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1575, 1, 6, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

linuxAgent3dot3 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 1575, 1, 6, 2)
)
if mibBuilder.loadTexts:
    linuxAgent3dot3.setProductRelease("cmu-snmp-linux-3.3")
if mibBuilder.loadTexts:
    linuxAgent3dot3.setStatus(
        "current"
    )

wwwSubagent1dot0 = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 1575, 1, 6, 3)
)
if mibBuilder.loadTexts:
    wwwSubagent1dot0.setProductRelease("TUBS Apache WWW-MIB sub-agent version 1.0")
if mibBuilder.loadTexts:
    wwwSubagent1dot0.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TUBS-IBR-AGENT-CAPABILITIES",
    **{"ibrAgentCapabilities": ibrAgentCapabilities,
       "linux": linux,
       "linuxAgent3dot3": linuxAgent3dot3,
       "wwwSubagent1dot0": wwwSubagent1dot0}
)
