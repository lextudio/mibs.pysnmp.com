# SNMP MIB module (L2L3-VPN-MCAST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/L2L3-VPN-MCAST-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:16:44 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(jnxL2L3VpnMcastExperiment,) = mibBuilder.importSymbols(
    "JUNIPER-EXPERIMENT-MIB",
    "jnxL2L3VpnMcastExperiment")

(jnxMibs,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxMibs")

(MplsLabel,) = mibBuilder.importSymbols(
    "MPLS-TC-STD-MIB",
    "MplsLabel")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 experimental,
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
    "experimental",
    "iso")

(DisplayString,
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

jnxL2L3VpnMcastMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1)
)
jnxL2L3VpnMcastMIB.setRevisions(
        ("2012-11-05 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxL2L3VpnMcastProviderTunnelType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ingress-replication", 6),
          ("ldp-mp2mp", 7),
          ("ldp-p2mp", 2),
          ("pim-asm", 4),
          ("pim-bidir", 5),
          ("pim-ssm", 3),
          ("rsvp-p2mp", 1),
          ("unconfigured", 0))
    )



# MIB Managed Objects in the order of their OIDs

_JnxL2L3VpnMcastObjects_ObjectIdentity = ObjectIdentity
jnxL2L3VpnMcastObjects = _JnxL2L3VpnMcastObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1)
)
_JnxL2L3VpnMcastPmsiStates_ObjectIdentity = ObjectIdentity
jnxL2L3VpnMcastPmsiStates = _JnxL2L3VpnMcastPmsiStates_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1)
)
_JnxL2L3VpnMcastPmsiTunnelAttributeTable_Object = MibTable
jnxL2L3VpnMcastPmsiTunnelAttributeTable = _JnxL2L3VpnMcastPmsiTunnelAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelAttributeTable.setStatus("current")
_JnxL2L3VpnMcastPmsiTunnelAttributeEntry_Object = MibTableRow
jnxL2L3VpnMcastPmsiTunnelAttributeEntry = _JnxL2L3VpnMcastPmsiTunnelAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1)
)
jnxL2L3VpnMcastPmsiTunnelAttributeEntry.setIndexNames(
    (0, "L2L3-VPN-MCAST-MIB", "jnxL2L3VpnMcastPmsiTunnelAttributeFlags"),
    (0, "L2L3-VPN-MCAST-MIB", "jnxL2L3VpnMcastPmsiTunnelAttributeType"),
    (0, "L2L3-VPN-MCAST-MIB", "jnxL2L3VpnMcastPmsiTunnelAttributeLabel"),
    (0, "L2L3-VPN-MCAST-MIB", "jnxL2L3VpnMcastPmsiTunnelAttributeId"),
)
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelAttributeEntry.setStatus("current")


class _JnxL2L3VpnMcastPmsiTunnelAttributeFlags_Type(OctetString):
    """Custom type jnxL2L3VpnMcastPmsiTunnelAttributeFlags based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_JnxL2L3VpnMcastPmsiTunnelAttributeFlags_Type.__name__ = "OctetString"
_JnxL2L3VpnMcastPmsiTunnelAttributeFlags_Object = MibTableColumn
jnxL2L3VpnMcastPmsiTunnelAttributeFlags = _JnxL2L3VpnMcastPmsiTunnelAttributeFlags_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1, 1),
    _JnxL2L3VpnMcastPmsiTunnelAttributeFlags_Type()
)
jnxL2L3VpnMcastPmsiTunnelAttributeFlags.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelAttributeFlags.setStatus("current")
_JnxL2L3VpnMcastPmsiTunnelAttributeType_Type = JnxL2L3VpnMcastProviderTunnelType
_JnxL2L3VpnMcastPmsiTunnelAttributeType_Object = MibTableColumn
jnxL2L3VpnMcastPmsiTunnelAttributeType = _JnxL2L3VpnMcastPmsiTunnelAttributeType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1, 2),
    _JnxL2L3VpnMcastPmsiTunnelAttributeType_Type()
)
jnxL2L3VpnMcastPmsiTunnelAttributeType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelAttributeType.setStatus("current")
_JnxL2L3VpnMcastPmsiTunnelAttributeLabel_Type = MplsLabel
_JnxL2L3VpnMcastPmsiTunnelAttributeLabel_Object = MibTableColumn
jnxL2L3VpnMcastPmsiTunnelAttributeLabel = _JnxL2L3VpnMcastPmsiTunnelAttributeLabel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1, 3),
    _JnxL2L3VpnMcastPmsiTunnelAttributeLabel_Type()
)
jnxL2L3VpnMcastPmsiTunnelAttributeLabel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelAttributeLabel.setStatus("current")


class _JnxL2L3VpnMcastPmsiTunnelAttributeId_Type(OctetString):
    """Custom type jnxL2L3VpnMcastPmsiTunnelAttributeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 37),
    )


_JnxL2L3VpnMcastPmsiTunnelAttributeId_Type.__name__ = "OctetString"
_JnxL2L3VpnMcastPmsiTunnelAttributeId_Object = MibTableColumn
jnxL2L3VpnMcastPmsiTunnelAttributeId = _JnxL2L3VpnMcastPmsiTunnelAttributeId_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1, 4),
    _JnxL2L3VpnMcastPmsiTunnelAttributeId_Type()
)
jnxL2L3VpnMcastPmsiTunnelAttributeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelAttributeId.setStatus("current")
_JnxL2L3VpnMcastPmsiTunnelPointer_Type = RowPointer
_JnxL2L3VpnMcastPmsiTunnelPointer_Object = MibTableColumn
jnxL2L3VpnMcastPmsiTunnelPointer = _JnxL2L3VpnMcastPmsiTunnelPointer_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1, 5),
    _JnxL2L3VpnMcastPmsiTunnelPointer_Type()
)
jnxL2L3VpnMcastPmsiTunnelPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelPointer.setStatus("current")
_JnxL2L3VpnMcastPmsiTunnelIf_Type = RowPointer
_JnxL2L3VpnMcastPmsiTunnelIf_Object = MibTableColumn
jnxL2L3VpnMcastPmsiTunnelIf = _JnxL2L3VpnMcastPmsiTunnelIf_Object(
    (1, 3, 6, 1, 4, 1, 2636, 5, 11, 1, 1, 1, 1, 1, 6),
    _JnxL2L3VpnMcastPmsiTunnelIf_Type()
)
jnxL2L3VpnMcastPmsiTunnelIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxL2L3VpnMcastPmsiTunnelIf.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "L2L3-VPN-MCAST-MIB",
    **{"JnxL2L3VpnMcastProviderTunnelType": JnxL2L3VpnMcastProviderTunnelType,
       "jnxL2L3VpnMcastMIB": jnxL2L3VpnMcastMIB,
       "jnxL2L3VpnMcastObjects": jnxL2L3VpnMcastObjects,
       "jnxL2L3VpnMcastPmsiStates": jnxL2L3VpnMcastPmsiStates,
       "jnxL2L3VpnMcastPmsiTunnelAttributeTable": jnxL2L3VpnMcastPmsiTunnelAttributeTable,
       "jnxL2L3VpnMcastPmsiTunnelAttributeEntry": jnxL2L3VpnMcastPmsiTunnelAttributeEntry,
       "jnxL2L3VpnMcastPmsiTunnelAttributeFlags": jnxL2L3VpnMcastPmsiTunnelAttributeFlags,
       "jnxL2L3VpnMcastPmsiTunnelAttributeType": jnxL2L3VpnMcastPmsiTunnelAttributeType,
       "jnxL2L3VpnMcastPmsiTunnelAttributeLabel": jnxL2L3VpnMcastPmsiTunnelAttributeLabel,
       "jnxL2L3VpnMcastPmsiTunnelAttributeId": jnxL2L3VpnMcastPmsiTunnelAttributeId,
       "jnxL2L3VpnMcastPmsiTunnelPointer": jnxL2L3VpnMcastPmsiTunnelPointer,
       "jnxL2L3VpnMcastPmsiTunnelIf": jnxL2L3VpnMcastPmsiTunnelIf}
)
