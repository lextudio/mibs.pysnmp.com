# SNMP MIB module (HPN-ICF-IP-BROADCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IP-BROADCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:36 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfIpBroadcast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33)
)
hpnicfIpBroadcast.setRevisions(
        ("2004-12-13 19:36",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfIpBdstScalarGroup_ObjectIdentity = ObjectIdentity
hpnicfIpBdstScalarGroup = _HpnicfIpBdstScalarGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1)
)


class _HpnicfIpBdstForwardBroadcast_Type(Integer32):
    """Custom type hpnicfIpBdstForwardBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forwarding", 1),
          ("notForwarding", 2))
    )


_HpnicfIpBdstForwardBroadcast_Type.__name__ = "Integer32"
_HpnicfIpBdstForwardBroadcast_Object = MibScalar
hpnicfIpBdstForwardBroadcast = _HpnicfIpBdstForwardBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 1),
    _HpnicfIpBdstForwardBroadcast_Type()
)
hpnicfIpBdstForwardBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpBdstForwardBroadcast.setStatus("current")


class _HpnicfIpReceiveBroadcast_Type(Integer32):
    """Custom type hpnicfIpReceiveBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notReceive", 2),
          ("receive", 1))
    )


_HpnicfIpReceiveBroadcast_Type.__name__ = "Integer32"
_HpnicfIpReceiveBroadcast_Object = MibScalar
hpnicfIpReceiveBroadcast = _HpnicfIpReceiveBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 1, 2),
    _HpnicfIpReceiveBroadcast_Type()
)
hpnicfIpReceiveBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpReceiveBroadcast.setStatus("current")
_HpnicfIpBdstGroup_ObjectIdentity = ObjectIdentity
hpnicfIpBdstGroup = _HpnicfIpBdstGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 2)
)
_HpnicfIpBdstTrap_ObjectIdentity = ObjectIdentity
hpnicfIpBdstTrap = _HpnicfIpBdstTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3)
)
_HpnicfIpBdstTrapPrex_ObjectIdentity = ObjectIdentity
hpnicfIpBdstTrapPrex = _HpnicfIpBdstTrapPrex_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 33, 3, 0)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IP-BROADCAST-MIB",
    **{"hpnicfIpBroadcast": hpnicfIpBroadcast,
       "hpnicfIpBdstScalarGroup": hpnicfIpBdstScalarGroup,
       "hpnicfIpBdstForwardBroadcast": hpnicfIpBdstForwardBroadcast,
       "hpnicfIpReceiveBroadcast": hpnicfIpReceiveBroadcast,
       "hpnicfIpBdstGroup": hpnicfIpBdstGroup,
       "hpnicfIpBdstTrap": hpnicfIpBdstTrap,
       "hpnicfIpBdstTrapPrex": hpnicfIpBdstTrapPrex}
)
