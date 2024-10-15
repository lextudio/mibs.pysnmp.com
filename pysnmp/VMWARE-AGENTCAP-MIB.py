# SNMP MIB module (VMWARE-AGENTCAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/VMWARE-AGENTCAP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:12:47 2024
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

(vmwareAgentCapabilities,) = mibBuilder.importSymbols(
    "VMWARE-ROOT-MIB",
    "vmwareAgentCapabilities")


# MODULE-IDENTITY

vmwAgentCapabilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1)
)
vmwAgentCapabilityMIB.setRevisions(
        ("2012-07-13 00:00",
         "2010-10-18 00:00",
         "2008-10-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VmwEsxCapability_ObjectIdentity = ObjectIdentity
vmwEsxCapability = _VmwEsxCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities

vmwESX40x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vmwESX40x.setProductRelease("4.0.x")
if mibBuilder.loadTexts:
    vmwESX40x.setStatus(
        "current"
    )

vmwESX41x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 2)
)
if mibBuilder.loadTexts:
    vmwESX41x.setProductRelease("4.1.x")
if mibBuilder.loadTexts:
    vmwESX41x.setStatus(
        "current"
    )

vmwESX50x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 3)
)
if mibBuilder.loadTexts:
    vmwESX50x.setProductRelease("5.0.x")
if mibBuilder.loadTexts:
    vmwESX50x.setStatus(
        "current"
    )

vmwESX51x = AgentCapabilities(
    (1, 3, 6, 1, 4, 1, 6876, 70, 1, 1, 4)
)
if mibBuilder.loadTexts:
    vmwESX51x.setProductRelease("5.1.x")
if mibBuilder.loadTexts:
    vmwESX51x.setStatus(
        "current"
    )


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VMWARE-AGENTCAP-MIB",
    **{"vmwAgentCapabilityMIB": vmwAgentCapabilityMIB,
       "vmwEsxCapability": vmwEsxCapability,
       "vmwESX40x": vmwESX40x,
       "vmwESX41x": vmwESX41x,
       "vmwESX50x": vmwESX50x,
       "vmwESX51x": vmwESX51x}
)
