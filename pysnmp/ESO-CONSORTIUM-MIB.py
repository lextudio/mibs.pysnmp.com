# SNMP MIB module (ESO-CONSORTIUM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ESO-CONSORTIUM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:40:50 2024
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
 enterprises,
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "enterprises",
    "iso",
    "snmpModules")

(AutonomousType,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

esoConsortiumMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14832)
)
esoConsortiumMIB.setRevisions(
        ("2003-02-03 00:00",
         "2003-02-03 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EsoConsortiumMIBObjectIdentities_ObjectIdentity = ObjectIdentity
esoConsortiumMIBObjectIdentities = _EsoConsortiumMIBObjectIdentities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14832, 1)
)
_Usm3DESPrivProtocol_ObjectIdentity = ObjectIdentity
usm3DESPrivProtocol = _Usm3DESPrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14832, 1, 1)
)
if mibBuilder.loadTexts:
    usm3DESPrivProtocol.setStatus("current")
_UsmAESCfb128PrivProtocol_ObjectIdentity = ObjectIdentity
usmAESCfb128PrivProtocol = _UsmAESCfb128PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14832, 1, 2)
)
if mibBuilder.loadTexts:
    usmAESCfb128PrivProtocol.setStatus("current")
_UsmAESCfb192PrivProtocol_ObjectIdentity = ObjectIdentity
usmAESCfb192PrivProtocol = _UsmAESCfb192PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14832, 1, 3)
)
if mibBuilder.loadTexts:
    usmAESCfb192PrivProtocol.setStatus("current")
_UsmAESCfb256PrivProtocol_ObjectIdentity = ObjectIdentity
usmAESCfb256PrivProtocol = _UsmAESCfb256PrivProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 14832, 1, 4)
)
if mibBuilder.loadTexts:
    usmAESCfb256PrivProtocol.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ESO-CONSORTIUM-MIB",
    **{"esoConsortiumMIB": esoConsortiumMIB,
       "esoConsortiumMIBObjectIdentities": esoConsortiumMIBObjectIdentities,
       "usm3DESPrivProtocol": usm3DESPrivProtocol,
       "usmAESCfb128PrivProtocol": usmAESCfb128PrivProtocol,
       "usmAESCfb192PrivProtocol": usmAESCfb192PrivProtocol,
       "usmAESCfb256PrivProtocol": usmAESCfb256PrivProtocol}
)
