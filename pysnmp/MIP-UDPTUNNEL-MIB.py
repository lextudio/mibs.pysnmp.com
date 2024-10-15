# SNMP MIB module (MIP-UDPTUNNEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MIP-UDPTUNNEL-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:06 2024
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

(mipMIB,) = mibBuilder.importSymbols(
    "MIP-MIB",
    "mipMIB")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mipUdpTunnelMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4)
)
mipUdpTunnelMIB.setRevisions(
        ("2007-06-12 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MipUdpTunnelMIBObjects_ObjectIdentity = ObjectIdentity
mipUdpTunnelMIBObjects = _MipUdpTunnelMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 1)
)
_MnUdpTunnel_ObjectIdentity = ObjectIdentity
mnUdpTunnel = _MnUdpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 1)
)


class _MnUdpTunnelEnable_Type(TruthValue):
    """Custom type mnUdpTunnelEnable based on TruthValue"""


_MnUdpTunnelEnable_Object = MibScalar
mnUdpTunnelEnable = _MnUdpTunnelEnable_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 1, 1),
    _MnUdpTunnelEnable_Type()
)
mnUdpTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnUdpTunnelEnable.setStatus("current")


class _MnUdpTunnelForce_Type(TruthValue):
    """Custom type mnUdpTunnelForce based on TruthValue"""


_MnUdpTunnelForce_Object = MibScalar
mnUdpTunnelForce = _MnUdpTunnelForce_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 1, 2),
    _MnUdpTunnelForce_Type()
)
mnUdpTunnelForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnUdpTunnelForce.setStatus("current")


class _MnUdpTunnelKeepaliveInterval_Type(Unsigned32):
    """Custom type mnUdpTunnelKeepaliveInterval based on Unsigned32"""
    defaultValue = 110


_MnUdpTunnelKeepaliveInterval_Object = MibScalar
mnUdpTunnelKeepaliveInterval = _MnUdpTunnelKeepaliveInterval_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 1, 3),
    _MnUdpTunnelKeepaliveInterval_Type()
)
mnUdpTunnelKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mnUdpTunnelKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    mnUdpTunnelKeepaliveInterval.setUnits("seconds")
_HaUdpTunnel_ObjectIdentity = ObjectIdentity
haUdpTunnel = _HaUdpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 2)
)


class _HaUdpTunnelEnable_Type(TruthValue):
    """Custom type haUdpTunnelEnable based on TruthValue"""


_HaUdpTunnelEnable_Object = MibScalar
haUdpTunnelEnable = _HaUdpTunnelEnable_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 1),
    _HaUdpTunnelEnable_Type()
)
haUdpTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    haUdpTunnelEnable.setStatus("current")


class _HaUdpTunnelKeepaliveInterval_Type(Unsigned32):
    """Custom type haUdpTunnelKeepaliveInterval based on Unsigned32"""
    defaultValue = 0


_HaUdpTunnelKeepaliveInterval_Object = MibScalar
haUdpTunnelKeepaliveInterval = _HaUdpTunnelKeepaliveInterval_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 2),
    _HaUdpTunnelKeepaliveInterval_Type()
)
haUdpTunnelKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    haUdpTunnelKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    haUdpTunnelKeepaliveInterval.setUnits("seconds")


class _HaUdpTunnelForce_Type(TruthValue):
    """Custom type haUdpTunnelForce based on TruthValue"""


_HaUdpTunnelForce_Object = MibScalar
haUdpTunnelForce = _HaUdpTunnelForce_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 3),
    _HaUdpTunnelForce_Type()
)
haUdpTunnelForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    haUdpTunnelForce.setStatus("current")
_HaUdpTunnelEncapUnavail_Type = Counter32
_HaUdpTunnelEncapUnavail_Object = MibScalar
haUdpTunnelEncapUnavail = _HaUdpTunnelEncapUnavail_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 2, 4),
    _HaUdpTunnelEncapUnavail_Type()
)
haUdpTunnelEncapUnavail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    haUdpTunnelEncapUnavail.setStatus("current")
_FaUdpTunnel_ObjectIdentity = ObjectIdentity
faUdpTunnel = _FaUdpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 3)
)


class _FaUdpTunnelEnable_Type(TruthValue):
    """Custom type faUdpTunnelEnable based on TruthValue"""


_FaUdpTunnelEnable_Object = MibScalar
faUdpTunnelEnable = _FaUdpTunnelEnable_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 3, 1),
    _FaUdpTunnelEnable_Type()
)
faUdpTunnelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faUdpTunnelEnable.setStatus("current")


class _FaUdpTunnelForce_Type(TruthValue):
    """Custom type faUdpTunnelForce based on TruthValue"""


_FaUdpTunnelForce_Object = MibScalar
faUdpTunnelForce = _FaUdpTunnelForce_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 3, 2),
    _FaUdpTunnelForce_Type()
)
faUdpTunnelForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faUdpTunnelForce.setStatus("current")


class _FaUdpTunnelKeepaliveInterval_Type(Unsigned32):
    """Custom type faUdpTunnelKeepaliveInterval based on Unsigned32"""
    defaultValue = 110


_FaUdpTunnelKeepaliveInterval_Object = MibScalar
faUdpTunnelKeepaliveInterval = _FaUdpTunnelKeepaliveInterval_Object(
    (1, 3, 6, 1, 2, 1, 44, 4, 1, 3, 3),
    _FaUdpTunnelKeepaliveInterval_Type()
)
faUdpTunnelKeepaliveInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    faUdpTunnelKeepaliveInterval.setStatus("current")
if mibBuilder.loadTexts:
    faUdpTunnelKeepaliveInterval.setUnits("seconds")
_MipUdpTunnelConformance_ObjectIdentity = ObjectIdentity
mipUdpTunnelConformance = _MipUdpTunnelConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 2)
)
_MipUdpTunnelGroups_ObjectIdentity = ObjectIdentity
mipUdpTunnelGroups = _MipUdpTunnelGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 2, 1)
)
_MipUdpTunnelCompliances_ObjectIdentity = ObjectIdentity
mipUdpTunnelCompliances = _MipUdpTunnelCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 44, 4, 2, 2)
)

# Managed Objects groups

mnUdpTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 4, 2, 1, 1)
)
mnUdpTunnelGroup.setObjects(
      *(("MIP-UDPTUNNEL-MIB", "mnUdpTunnelEnable"),
        ("MIP-UDPTUNNEL-MIB", "mnUdpTunnelForce"),
        ("MIP-UDPTUNNEL-MIB", "mnUdpTunnelKeepaliveInterval"))
)
if mibBuilder.loadTexts:
    mnUdpTunnelGroup.setStatus("current")

haUdpTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 4, 2, 1, 2)
)
haUdpTunnelGroup.setObjects(
      *(("MIP-UDPTUNNEL-MIB", "haUdpTunnelEnable"),
        ("MIP-UDPTUNNEL-MIB", "haUdpTunnelForce"),
        ("MIP-UDPTUNNEL-MIB", "haUdpTunnelKeepaliveInterval"),
        ("MIP-UDPTUNNEL-MIB", "haUdpTunnelEncapUnavail"))
)
if mibBuilder.loadTexts:
    haUdpTunnelGroup.setStatus("current")

faUdpTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 44, 4, 2, 1, 3)
)
faUdpTunnelGroup.setObjects(
      *(("MIP-UDPTUNNEL-MIB", "faUdpTunnelEnable"),
        ("MIP-UDPTUNNEL-MIB", "faUdpTunnelForce"),
        ("MIP-UDPTUNNEL-MIB", "faUdpTunnelKeepaliveInterval"))
)
if mibBuilder.loadTexts:
    faUdpTunnelGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mipUdpTunnelCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 44, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mipUdpTunnelCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MIP-UDPTUNNEL-MIB",
    **{"mipUdpTunnelMIB": mipUdpTunnelMIB,
       "mipUdpTunnelMIBObjects": mipUdpTunnelMIBObjects,
       "mnUdpTunnel": mnUdpTunnel,
       "mnUdpTunnelEnable": mnUdpTunnelEnable,
       "mnUdpTunnelForce": mnUdpTunnelForce,
       "mnUdpTunnelKeepaliveInterval": mnUdpTunnelKeepaliveInterval,
       "haUdpTunnel": haUdpTunnel,
       "haUdpTunnelEnable": haUdpTunnelEnable,
       "haUdpTunnelKeepaliveInterval": haUdpTunnelKeepaliveInterval,
       "haUdpTunnelForce": haUdpTunnelForce,
       "haUdpTunnelEncapUnavail": haUdpTunnelEncapUnavail,
       "faUdpTunnel": faUdpTunnel,
       "faUdpTunnelEnable": faUdpTunnelEnable,
       "faUdpTunnelForce": faUdpTunnelForce,
       "faUdpTunnelKeepaliveInterval": faUdpTunnelKeepaliveInterval,
       "mipUdpTunnelConformance": mipUdpTunnelConformance,
       "mipUdpTunnelGroups": mipUdpTunnelGroups,
       "mnUdpTunnelGroup": mnUdpTunnelGroup,
       "haUdpTunnelGroup": haUdpTunnelGroup,
       "faUdpTunnelGroup": faUdpTunnelGroup,
       "mipUdpTunnelCompliances": mipUdpTunnelCompliances,
       "mipUdpTunnelCompliance": mipUdpTunnelCompliance}
)
