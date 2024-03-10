"""SNMP MIB module (QB-ETHERNET-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/QB-ETHERNET-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:37:32 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(dot3StatsEntry,) = mibBuilder.importSymbols(
    "EtherLike-MIB",
    "dot3StatsEntry")

(QbAtmAal5EncapsType,) = mibBuilder.importSymbols(
    "QB-DWS-MIB",
    "QbAtmAal5EncapsType")

(qbMibs,) = mibBuilder.importSymbols(
    "QUANTUMBRIDGE-REG",
    "qbMibs")

(NotificationGroup,
 ModuleCompliance,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance",
    "ObjectGroup")

(ObjectIdentity,
 ModuleIdentity,
 Integer32,
 TimeTicks,
 Bits,
 Unsigned32,
 Gauge32,
 IpAddress,
 iso,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 MibIdentifier,
 NotificationType,
 Counter32,
 Counter64) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "ObjectIdentity",
    "ModuleIdentity",
    "Integer32",
    "TimeTicks",
    "Bits",
    "Unsigned32",
    "Gauge32",
    "IpAddress",
    "iso",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "MibIdentifier",
    "NotificationType",
    "Counter32",
    "Counter64")

(TextualConvention,
 DisplayString) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "TextualConvention",
    "DisplayString")


# MODULE-IDENTITY

qbEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5)
)
qbEthernetMIB.setLastUpdated("0110222155Z")
if mibBuilder.loadTexts:
    qbEthernetMIB.setOrganization("""\
Quanrtum Bridge Inc.
""")
qbEthernetMIB.setContactInfo("""\
mvaysman@quantumbridge.com
""")
if mibBuilder.loadTexts:
    qbEthernetMIB.setDescription("""\
This module defines proprietary objects that extend those in IETF's the
Ethernet-Like Interface MIB.
""")


# Types definitions


# TEXTUAL-CONVENTIONS



class QbDot3LoopbackType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("qbDot3LoopbackLineLoop", 2),
          ("qbDot3LoopbackNoLoop", 1),
          ("qbDot3LoopbackPayloadLoop", 3))
    )

    if mibBuilder.loadTexts:
        description = """\
The type of loopback available on Quantum Bridge 802.3 (ethernet) interfaces.
"""


# MIB Managed Objects in the order of their OIDs

_QbDot3Objects_ObjectIdentity = ObjectIdentity
qbDot3Objects = _QbDot3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1)
)
_QbDot3ConfigTable_Object = MibTable
qbDot3ConfigTable = _QbDot3ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2)
)
if mibBuilder.loadTexts:
    qbDot3ConfigTable.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigTable.setDescription("""\
Quantum Bridge proprietary configuration parameters for ethernet-like
interfaces.
""")
_QbDot3ConfigEntry_Object = MibTableRow
qbDot3ConfigEntry = _QbDot3ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1)
)
dot3StatsEntry.registerAugmentions(
    ("QB-ETHERNET-MIB",
     "qbDot3ConfigEntry")
)
qbDot3ConfigEntry.setIndexNames(*dot3StatsEntry.getIndexNames())
if mibBuilder.loadTexts:
    qbDot3ConfigEntry.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigEntry.setDescription("""\
Quantum Bridge proprietary configuration parameters for single ethernet-like
interface.
""")


class _QbDot3ConfigSpeed_Type(Integer32):
    """Custom type qbDot3ConfigSpeed based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("mbps10", 1),
          ("mbps100", 2))
    )


_QbDot3ConfigSpeed_Type.__name__ = "Integer32"
_QbDot3ConfigSpeed_Object = MibTableColumn
qbDot3ConfigSpeed = _QbDot3ConfigSpeed_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 1),
    _QbDot3ConfigSpeed_Type()
)
qbDot3ConfigSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigSpeed.setStatus("deprecated")
if mibBuilder.loadTexts:
    qbDot3ConfigSpeed.setDescription("""\
The configured speed of the interface. This may be set by the administrator or
may be the result of auto-negotiation.
""")


class _QbDot3ConfigDuplexMode_Type(Integer32):
    """Custom type qbDot3ConfigDuplexMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 3),
          ("full", 1),
          ("half", 2))
    )


_QbDot3ConfigDuplexMode_Type.__name__ = "Integer32"
_QbDot3ConfigDuplexMode_Object = MibTableColumn
qbDot3ConfigDuplexMode = _QbDot3ConfigDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 2),
    _QbDot3ConfigDuplexMode_Type()
)
qbDot3ConfigDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigDuplexMode.setStatus("deprecated")
if mibBuilder.loadTexts:
    qbDot3ConfigDuplexMode.setDescription("""\
The configured mode of the interface.
""")


class _QbDot3ConfigEncapsType_Type(QbAtmAal5EncapsType):
    """Custom type qbDot3ConfigEncapsType based on QbAtmAal5EncapsType"""


_QbDot3ConfigEncapsType_Object = MibTableColumn
qbDot3ConfigEncapsType = _QbDot3ConfigEncapsType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 3),
    _QbDot3ConfigEncapsType_Type()
)
qbDot3ConfigEncapsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigEncapsType.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigEncapsType.setDescription("""\
The type of data encapsulation used over the AAL5 SSCS layer. The definitions
reference RFC 1483 Multiprotocol Encapsulation over ATM AAL5 and to the ATM
Forum LAN Emulation specification.
""")
_QbDot3ConfigRouterAddress_Type = MacAddress
_QbDot3ConfigRouterAddress_Object = MibTableColumn
qbDot3ConfigRouterAddress = _QbDot3ConfigRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 4),
    _QbDot3ConfigRouterAddress_Type()
)
qbDot3ConfigRouterAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigRouterAddress.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigRouterAddress.setDescription("""\
The MAC address of the router that connects to the IOT Ethnernet port. Note
that this object is relevant for IOT ports only
""")
_QbDot3ConfigLoopback_Type = QbDot3LoopbackType
_QbDot3ConfigLoopback_Object = MibTableColumn
qbDot3ConfigLoopback = _QbDot3ConfigLoopback_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 5),
    _QbDot3ConfigLoopback_Type()
)
qbDot3ConfigLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigLoopback.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigLoopback.setDescription("""\
The loopback configuration of this interface. If used in a set it will cause
the agent to place the interface in the desired loopback mode. When read, it
will return the interface's curretn loopback configuration.
""")
_QbDot3ConfigEnetAdminMode_Type = ObjectIdentifier
_QbDot3ConfigEnetAdminMode_Object = MibTableColumn
qbDot3ConfigEnetAdminMode = _QbDot3ConfigEnetAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 6),
    _QbDot3ConfigEnetAdminMode_Type()
)
qbDot3ConfigEnetAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetAdminMode.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetAdminMode.setReference("""\
[IEEE 802.3 Std], 30.5.1.1.1, aMAUID, and 22.2.4.1.4.
""")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetAdminMode.setDescription("""\
This object identifies the default administrative baseband MAU type, to be used
in conjunction with the operational MAU type denoted by ifMauType. For a
detailed description see ifMauDefaultType in RFC2668.
""")
_QbDot3ConfigEnetType_Type = ObjectIdentifier
_QbDot3ConfigEnetType_Object = MibTableColumn
qbDot3ConfigEnetType = _QbDot3ConfigEnetType_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 7),
    _QbDot3ConfigEnetType_Type()
)
qbDot3ConfigEnetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetType.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetType.setReference("""\
[IEEE 802.3 Std], 30.5.1.1.1, a MAUID, and 22.2.4.1.4.
""")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetType.setDescription("""\
This object identifies the MAU type. For a detailed description see ifMauType
in RFC2668.
""")


class _QbDot3ConfigEnetNegMode_Type(Integer32):
    """Custom type qbDot3ConfigEnetNegMode based on Integer32"""
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


_QbDot3ConfigEnetNegMode_Type.__name__ = "Integer32"
_QbDot3ConfigEnetNegMode_Object = MibTableColumn
qbDot3ConfigEnetNegMode = _QbDot3ConfigEnetNegMode_Object(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 1, 2, 1, 8),
    _QbDot3ConfigEnetNegMode_Type()
)
qbDot3ConfigEnetNegMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetNegMode.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3ConfigEnetNegMode.setDescription("""\
This object is used to enable and disable auto-negotiation on a given port.
""")
_QbDot3Conformance_ObjectIdentity = ObjectIdentity
qbDot3Conformance = _QbDot3Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 2)
)
_QbDot3Compliances_ObjectIdentity = ObjectIdentity
qbDot3Compliances = _QbDot3Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 2, 1)
)
_QbDot3Groups_ObjectIdentity = ObjectIdentity
qbDot3Groups = _QbDot3Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 2, 2)
)

# Managed Objects groups

qbDot3Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 2, 2, 1)
)
qbDot3Group.setObjects(
      *(("QB-ETHERNET-MIB", "qbDot3ConfigSpeed"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigDuplexMode"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigEncapsType"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigRouterAddress"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigLoopback"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigEnetAdminMode"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigEnetType"),
        ("QB-ETHERNET-MIB", "qbDot3ConfigEnetNegMode"))
)
if mibBuilder.loadTexts:
    qbDot3Group.setStatus("current")
if mibBuilder.loadTexts:
    qbDot3Group.setDescription("""\
The set of all accessible objects in this MIB.
""")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qbDot3Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4323, 2, 5, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qbDot3Compliance.setStatus(
        "current"
    )
if mibBuilder.loadTexts:
    qbDot3Compliance.setDescription("""\
The compliance statement for all agents that support this MIB. A compliant
agent implements all objects defined in this MIB.
""")


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QB-ETHERNET-MIB",
    **{"QbDot3LoopbackType": QbDot3LoopbackType,
       "qbEthernetMIB": qbEthernetMIB,
       "qbDot3Objects": qbDot3Objects,
       "qbDot3ConfigTable": qbDot3ConfigTable,
       "qbDot3ConfigEntry": qbDot3ConfigEntry,
       "qbDot3ConfigSpeed": qbDot3ConfigSpeed,
       "qbDot3ConfigDuplexMode": qbDot3ConfigDuplexMode,
       "qbDot3ConfigEncapsType": qbDot3ConfigEncapsType,
       "qbDot3ConfigRouterAddress": qbDot3ConfigRouterAddress,
       "qbDot3ConfigLoopback": qbDot3ConfigLoopback,
       "qbDot3ConfigEnetAdminMode": qbDot3ConfigEnetAdminMode,
       "qbDot3ConfigEnetType": qbDot3ConfigEnetType,
       "qbDot3ConfigEnetNegMode": qbDot3ConfigEnetNegMode,
       "qbDot3Conformance": qbDot3Conformance,
       "qbDot3Compliances": qbDot3Compliances,
       "qbDot3Compliance": qbDot3Compliance,
       "qbDot3Groups": qbDot3Groups,
       "qbDot3Group": qbDot3Group}
)
