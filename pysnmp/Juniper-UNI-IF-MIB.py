# SNMP MIB module (Juniper-UNI-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-UNI-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:37 2024
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

(ifEntry,
 ifStackHigherLayer,
 ifStackLowerLayer) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry",
    "ifStackHigherLayer",
    "ifStackLowerLayer")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

juniIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3)
)
juniIfMIB.setRevisions(
        ("2005-10-11 20:40",
         "2003-07-16 21:40",
         "2003-02-06 15:57",
         "2002-01-22 16:52",
         "2001-03-28 15:12",
         "2000-11-22 23:41",
         "2000-09-29 18:35",
         "2000-07-27 15:45",
         "2000-05-05 15:08",
         "1999-12-21 15:18",
         "1999-09-03 14:16",
         "1998-11-13 20:19")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniIfType(Integer32, TextualConvention):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              145,
              256,
              257)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 10),
          ("atm", 9),
          ("atmActiveSubInterface", 257),
          ("atmSubInterface", 11),
          ("atmVirtualCircuit", 145),
          ("bridgeInterface", 48),
          ("bridgedEthernet", 19),
          ("cbfInterface", 36),
          ("ds0", 2),
          ("ds1", 3),
          ("ds3", 4),
          ("ethernet", 6),
          ("ethernetSubInterface", 28),
          ("frSubInterface", 16),
          ("frameRelay", 5),
          ("ft1", 12),
          ("gtpInterface", 37),
          ("hdlc", 13),
          ("ip", 0),
          ("ipLoopback", 14),
          ("ipTunnelInterface", 30),
          ("ipTunnelMdt", 55),
          ("ipVirtual", 15),
          ("ipsecInterface", 43),
          ("ipsecTransportInterface", 49),
          ("ipv6Interface", 50),
          ("ipv6Loopback", 52),
          ("ipv6TunnelInterface", 51),
          ("l2fDestinationInterface", 42),
          ("l2fSessionInterface", 41),
          ("l2fTunnelInterface", 40),
          ("l2tpDestinationInterface", 24),
          ("l2tpSessionInterface", 21),
          ("l2tpTunnelInterface", 20),
          ("lacGenInterface", 47),
          ("lag", 54),
          ("mlPppLinkInterface", 22),
          ("mlPppNetworkInterface", 27),
          ("mplsL2ShimInterface", 45),
          ("mplsMajorInterface", 25),
          ("mplsMinorInterface", 26),
          ("multilinkFrameRelayInterface", 29),
          ("osi", 53),
          ("ppp", 1),
          ("pppLink", 256),
          ("pppoe", 17),
          ("pppoeSubInterface", 18),
          ("serverPortInterface", 31),
          ("sgInterface", 44),
          ("slepInterface", 23),
          ("smdsInterface", 32),
          ("smdsMajorInterface", 38),
          ("smdsSubInterface", 39),
          ("sonet", 7),
          ("sonetPath", 8),
          ("sonetVTInterface", 33),
          ("vlanMajorInterface", 34),
          ("vlanSubInterface", 35))
    )



# MIB Managed Objects in the order of their OIDs

_JuniInterfaces_ObjectIdentity = ObjectIdentity
juniInterfaces = _JuniInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1)
)
_JuniIf_ObjectIdentity = ObjectIdentity
juniIf = _JuniIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1)
)
_JuniIfObjects_ObjectIdentity = ObjectIdentity
juniIfObjects = _JuniIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1)
)
_JuniIfTable_Object = MibTable
juniIfTable = _JuniIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIfTable.setStatus("current")
_JuniIfEntry_Object = MibTableRow
juniIfEntry = _JuniIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniIfEntry.setStatus("current")
_JuniIfType_Type = JuniIfType
_JuniIfType_Object = MibTableColumn
juniIfType = _JuniIfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1),
    _JuniIfType_Type()
)
juniIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIfType.setStatus("current")
_JuniIfInvStackTable_Object = MibTable
juniIfInvStackTable = _JuniIfInvStackTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniIfInvStackTable.setStatus("current")
_JuniIfInvStackEntry_Object = MibTableRow
juniIfInvStackEntry = _JuniIfInvStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1)
)
juniIfInvStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackLowerLayer"),
    (0, "IF-MIB", "ifStackHigherLayer"),
)
if mibBuilder.loadTexts:
    juniIfInvStackEntry.setStatus("current")
_JuniIfInvStackStatus_Type = RowStatus
_JuniIfInvStackStatus_Object = MibTableColumn
juniIfInvStackStatus = _JuniIfInvStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1),
    _JuniIfInvStackStatus_Type()
)
juniIfInvStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIfInvStackStatus.setStatus("current")
_JuniIfCountTable_Object = MibTable
juniIfCountTable = _JuniIfCountTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    juniIfCountTable.setStatus("current")
_JuniIfCountEntry_Object = MibTableRow
juniIfCountEntry = _JuniIfCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1)
)
juniIfCountEntry.setIndexNames(
    (0, "Juniper-UNI-IF-MIB", "juniIfCountIfType"),
)
if mibBuilder.loadTexts:
    juniIfCountEntry.setStatus("current")
_JuniIfCountIfType_Type = JuniIfType
_JuniIfCountIfType_Object = MibTableColumn
juniIfCountIfType = _JuniIfCountIfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 1),
    _JuniIfCountIfType_Type()
)
juniIfCountIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniIfCountIfType.setStatus("current")
_JuniIfCountNumberOfInterfaces_Type = Unsigned32
_JuniIfCountNumberOfInterfaces_Object = MibTableColumn
juniIfCountNumberOfInterfaces = _JuniIfCountNumberOfInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 3, 1, 2),
    _JuniIfCountNumberOfInterfaces_Type()
)
juniIfCountNumberOfInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniIfCountNumberOfInterfaces.setStatus("current")
_JuniIfConformance_ObjectIdentity = ObjectIdentity
juniIfConformance = _JuniIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4)
)
_JuniIfCompliances_ObjectIdentity = ObjectIdentity
juniIfCompliances = _JuniIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1)
)
_JuniIfGroups_ObjectIdentity = ObjectIdentity
juniIfGroups = _JuniIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2)
)
ifEntry.registerAugmentions(
    ("Juniper-UNI-IF-MIB",
     "juniIfEntry")
)
juniIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

juniIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)
)
juniIfGroup.setObjects(
    ("Juniper-UNI-IF-MIB", "juniIfType")
)
if mibBuilder.loadTexts:
    juniIfGroup.setStatus("current")

juniIfInvStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)
)
juniIfInvStackGroup.setObjects(
    ("Juniper-UNI-IF-MIB", "juniIfInvStackStatus")
)
if mibBuilder.loadTexts:
    juniIfInvStackGroup.setStatus("current")

juniIfCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 3)
)
juniIfCountGroup.setObjects(
    ("Juniper-UNI-IF-MIB", "juniIfCountNumberOfInterfaces")
)
if mibBuilder.loadTexts:
    juniIfCountGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniIfCompliance.setStatus(
        "current"
    )

juniIfCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniIfCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-UNI-IF-MIB",
    **{"JuniIfType": JuniIfType,
       "juniIfMIB": juniIfMIB,
       "juniInterfaces": juniInterfaces,
       "juniIf": juniIf,
       "juniIfObjects": juniIfObjects,
       "juniIfTable": juniIfTable,
       "juniIfEntry": juniIfEntry,
       "juniIfType": juniIfType,
       "juniIfInvStackTable": juniIfInvStackTable,
       "juniIfInvStackEntry": juniIfInvStackEntry,
       "juniIfInvStackStatus": juniIfInvStackStatus,
       "juniIfCountTable": juniIfCountTable,
       "juniIfCountEntry": juniIfCountEntry,
       "juniIfCountIfType": juniIfCountIfType,
       "juniIfCountNumberOfInterfaces": juniIfCountNumberOfInterfaces,
       "juniIfConformance": juniIfConformance,
       "juniIfCompliances": juniIfCompliances,
       "juniIfCompliance": juniIfCompliance,
       "juniIfCompliance1": juniIfCompliance1,
       "juniIfGroups": juniIfGroups,
       "juniIfGroup": juniIfGroup,
       "juniIfInvStackGroup": juniIfInvStackGroup,
       "juniIfCountGroup": juniIfCountGroup}
)
