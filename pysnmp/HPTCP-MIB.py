# SNMP MIB module (HPTCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPTCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:34 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

hpicfTcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79)
)
hpicfTcpMib.setRevisions(
        ("2010-09-30 15:25",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpTcpObjects_ObjectIdentity = ObjectIdentity
hpTcpObjects = _HpTcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1)
)
_HpTcpOutRstsWithAck_Type = Counter32
_HpTcpOutRstsWithAck_Object = MibScalar
hpTcpOutRstsWithAck = _HpTcpOutRstsWithAck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 1, 1),
    _HpTcpOutRstsWithAck_Type()
)
hpTcpOutRstsWithAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpTcpOutRstsWithAck.setStatus("current")
_HpTcpConformance_ObjectIdentity = ObjectIdentity
hpTcpConformance = _HpTcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2)
)
_HpTcpGroups_ObjectIdentity = ObjectIdentity
hpTcpGroups = _HpTcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1)
)
_HpTcpCompliances_ObjectIdentity = ObjectIdentity
hpTcpCompliances = _HpTcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2)
)

# Managed Objects groups

hpTcpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 1, 1)
)
hpTcpBaseGroup.setObjects(
    ("HPTCP-MIB", "hpTcpOutRstsWithAck")
)
if mibBuilder.loadTexts:
    hpTcpBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpTcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 79, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpTcpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPTCP-MIB",
    **{"hpicfTcpMib": hpicfTcpMib,
       "hpTcpObjects": hpTcpObjects,
       "hpTcpOutRstsWithAck": hpTcpOutRstsWithAck,
       "hpTcpConformance": hpTcpConformance,
       "hpTcpGroups": hpTcpGroups,
       "hpTcpBaseGroup": hpTcpBaseGroup,
       "hpTcpCompliances": hpTcpCompliances,
       "hpTcpCompliance": hpTcpCompliance}
)
