# SNMP MIB module (HM2-PLATFORM-SFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HM2-PLATFORM-SFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:56:25 2024
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

(hm2PlatformMibs,) = mibBuilder.importSymbols(
    "HM2-TC-MIB",
    "hm2PlatformMibs")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

hm2PlatformSflow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 59)
)
hm2PlatformSflow.setRevisions(
        ("2011-10-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2AgentFastPathSflowObjects_ObjectIdentity = ObjectIdentity
hm2AgentFastPathSflowObjects = _Hm2AgentFastPathSflowObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 12, 59, 1)
)
_Hm2AgentSflowSourceInterface_Type = InterfaceIndexOrZero
_Hm2AgentSflowSourceInterface_Object = MibScalar
hm2AgentSflowSourceInterface = _Hm2AgentSflowSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 12, 59, 1, 1),
    _Hm2AgentSflowSourceInterface_Type()
)
hm2AgentSflowSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2AgentSflowSourceInterface.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-PLATFORM-SFLOW-MIB",
    **{"hm2PlatformSflow": hm2PlatformSflow,
       "hm2AgentFastPathSflowObjects": hm2AgentFastPathSflowObjects,
       "hm2AgentSflowSourceInterface": hm2AgentSflowSourceInterface}
)
