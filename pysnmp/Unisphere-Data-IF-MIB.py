# SNMP MIB module (Unisphere-Data-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:16 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3)
)
usdIfMIB.setRevisions(
        ("2001-03-28 15:12",
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



class UsdIfType(Integer32, TextualConvention):
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
              47)
        )
    )
    namedValues = NamedValues(
        *(("aal5", 10),
          ("atm", 9),
          ("atmSubInterface", 11),
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
          ("ipVirtual", 15),
          ("ipsecInterface", 43),
          ("l2fDestinationInterface", 42),
          ("l2fSessionInterface", 41),
          ("l2fTunnelInterface", 40),
          ("l2tpDestinationInterface", 24),
          ("l2tpSessionInterface", 21),
          ("l2tpTunnelInterface", 20),
          ("lacGenInterface", 47),
          ("mlPppLinkInterface", 22),
          ("mlPppNetworkInterface", 27),
          ("mplsMajorInterface", 25),
          ("mplsMinorInterface", 26),
          ("multilinkFrameRelayInterface", 29),
          ("ppp", 1),
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

_UsdInterfaces_ObjectIdentity = ObjectIdentity
usdInterfaces = _UsdInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1)
)
_UsdIf_ObjectIdentity = ObjectIdentity
usdIf = _UsdIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1)
)
_UsdIfObjects_ObjectIdentity = ObjectIdentity
usdIfObjects = _UsdIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1)
)
_UsdIfTable_Object = MibTable
usdIfTable = _UsdIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdIfTable.setStatus("current")
_UsdIfEntry_Object = MibTableRow
usdIfEntry = _UsdIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdIfEntry.setStatus("current")
_UsdIfType_Type = UsdIfType
_UsdIfType_Object = MibTableColumn
usdIfType = _UsdIfType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 1, 1, 1),
    _UsdIfType_Type()
)
usdIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIfType.setStatus("current")
_UsdIfInvStackTable_Object = MibTable
usdIfInvStackTable = _UsdIfInvStackTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdIfInvStackTable.setStatus("current")
_UsdIfInvStackEntry_Object = MibTableRow
usdIfInvStackEntry = _UsdIfInvStackEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1)
)
usdIfInvStackEntry.setIndexNames(
    (0, "IF-MIB", "ifStackLowerLayer"),
    (0, "IF-MIB", "ifStackHigherLayer"),
)
if mibBuilder.loadTexts:
    usdIfInvStackEntry.setStatus("current")
_UsdIfInvStackStatus_Type = RowStatus
_UsdIfInvStackStatus_Object = MibTableColumn
usdIfInvStackStatus = _UsdIfInvStackStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 1, 2, 1, 1),
    _UsdIfInvStackStatus_Type()
)
usdIfInvStackStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdIfInvStackStatus.setStatus("current")
_UsdIfConformance_ObjectIdentity = ObjectIdentity
usdIfConformance = _UsdIfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4)
)
_UsdIfCompliances_ObjectIdentity = ObjectIdentity
usdIfCompliances = _UsdIfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1)
)
_UsdIfGroups_ObjectIdentity = ObjectIdentity
usdIfGroups = _UsdIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2)
)
ifEntry.registerAugmentions(
    ("Unisphere-Data-IF-MIB",
     "usdIfEntry")
)
usdIfEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

usdIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 1)
)
usdIfGroup.setObjects(
    ("Unisphere-Data-IF-MIB", "usdIfType")
)
if mibBuilder.loadTexts:
    usdIfGroup.setStatus("current")

usdIfInvStackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 2, 2)
)
usdIfInvStackGroup.setObjects(
    ("Unisphere-Data-IF-MIB", "usdIfInvStackStatus")
)
if mibBuilder.loadTexts:
    usdIfInvStackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdIfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 3, 1, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdIfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-IF-MIB",
    **{"UsdIfType": UsdIfType,
       "usdIfMIB": usdIfMIB,
       "usdInterfaces": usdInterfaces,
       "usdIf": usdIf,
       "usdIfObjects": usdIfObjects,
       "usdIfTable": usdIfTable,
       "usdIfEntry": usdIfEntry,
       "usdIfType": usdIfType,
       "usdIfInvStackTable": usdIfInvStackTable,
       "usdIfInvStackEntry": usdIfInvStackEntry,
       "usdIfInvStackStatus": usdIfInvStackStatus,
       "usdIfConformance": usdIfConformance,
       "usdIfCompliances": usdIfCompliances,
       "usdIfCompliance": usdIfCompliance,
       "usdIfGroups": usdIfGroups,
       "usdIfGroup": usdIfGroup,
       "usdIfInvStackGroup": usdIfInvStackGroup}
)
