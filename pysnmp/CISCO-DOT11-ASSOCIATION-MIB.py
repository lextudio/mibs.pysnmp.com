# SNMP MIB module (CISCO-DOT11-ASSOCIATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DOT11-ASSOCIATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:58:45 2024
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

(CDot11IfCipherType,
 CDot11IfVlanIdOrZero,
 cd11IfAuxSsid) = mibBuilder.importSymbols(
    "CISCO-DOT11-IF-MIB",
    "CDot11IfCipherType",
    "CDot11IfVlanIdOrZero",
    "cd11IfAuxSsid")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 MacAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDot11AssociationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273)
)
ciscoDot11AssociationMIB.setRevisions(
        ("2007-01-05 00:00",
         "2006-06-12 00:00",
         "2005-03-08 00:00",
         "2004-11-28 00:00",
         "2004-10-18 00:00",
         "2004-02-19 00:00",
         "2003-07-27 00:00",
         "2003-04-11 00:00",
         "2003-01-29 00:00",
         "2002-07-15 00:00",
         "2002-04-17 00:00",
         "2002-03-06 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDot11ClientRoleClassType(Integer32, TextualConvention):
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
              6)
        )
    )
    namedValues = NamedValues(
        *(("accessPoint", 2),
          ("bridge", 4),
          ("bridgeHost", 3),
          ("bridgeRoot", 5),
          ("clientStation", 0),
          ("ethernetClient", 6),
          ("repeater", 1))
    )



class CDot11ClientDevType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              76,
              77,
              84,
              85,
              86,
              101,
              102,
              104,
              109,
              110,
              111,
              112,
              117,
              123,
              124,
              127,
              128,
              129,
              130,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140)
        )
    )
    namedValues = NamedValues(
        *(("c1100SeriesAP", 129),
          ("c1130SeriesAP", 137),
          ("c1200SeriesAP", 132),
          ("c1240SeriesAP", 140),
          ("c1310SeriesBridge", 138),
          ("c1410SeriesBridge", 130),
          ("c350SeriesAP", 134),
          ("c7920phone", 139),
          ("cb21agClient", 135),
          ("ethernetAP", 76),
          ("ethernetBridge", 77),
          ("ethernetClient", 112),
          ("ethernetUC", 86),
          ("generic80211Client", 104),
          ("mc", 111),
          ("mp2xClient", 133),
          ("pc3000Client", 84),
          ("pc3100Client", 110),
          ("pc3500Client", 101),
          ("pc4500Client", 102),
          ("pc4800Client", 109),
          ("pc4800bClient", 117),
          ("radioKodiak", 136),
          ("serialUC", 85),
          ("series350Client", 127),
          ("series370Client", 128),
          ("unknown", 1),
          ("wgb", 124),
          ("wgbNoDiversity", 123))
    )



class CDot11ClientRadioType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              12,
              13,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              46)
        )
    )
    namedValues = NamedValues(
        *(("bridge1410", 36),
          ("cb21ag", 46),
          ("ccxClient", 2),
          ("mp2xMAR", 40),
          ("mp2xSeries", 37),
          ("pc3000", 4),
          ("pc3100", 13),
          ("pc3500", 3),
          ("pc4500", 6),
          ("pc4800", 12),
          ("rm2gSeries", 39),
          ("rm2xSeries", 38),
          ("series340", 33),
          ("series350", 34),
          ("series370", 35),
          ("unknown", 1))
    )



class CDot11AuthenticationMethod(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              129)
        )
    )
    namedValues = NamedValues(
        *(("networkEap", 129),
          ("open", 1),
          ("sharedKey", 2))
    )



class CDot11AdditionalAuthenMethod(Bits, TextualConvention):
    status = "current"


class CDot11Dot1xAuthenMethod(Bits, TextualConvention):
    status = "current"


class CDot11KeyManagementMethod(Bits, TextualConvention):
    status = "deprecated"


class CDot11NewKeyManagementMethod(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_CiscoDot11AssocMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDot11AssocMIBObjects = _CiscoDot11AssocMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1)
)
_CDot11AssociationGlobal_ObjectIdentity = ObjectIdentity
cDot11AssociationGlobal = _CDot11AssociationGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1)
)
_CDot11ParentAddress_Type = MacAddress
_CDot11ParentAddress_Object = MibScalar
cDot11ParentAddress = _CDot11ParentAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 1),
    _CDot11ParentAddress_Type()
)
cDot11ParentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ParentAddress.setStatus("current")
_CDot11ActiveDevicesTable_Object = MibTable
cDot11ActiveDevicesTable = _CDot11ActiveDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cDot11ActiveDevicesTable.setStatus("current")
_CDot11ActiveDevicesEntry_Object = MibTableRow
cDot11ActiveDevicesEntry = _CDot11ActiveDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1)
)
cDot11ActiveDevicesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cDot11ActiveDevicesEntry.setStatus("current")


class _CDot11ActiveWirelessClients_Type(Gauge32):
    """Custom type cDot11ActiveWirelessClients based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_CDot11ActiveWirelessClients_Type.__name__ = "Gauge32"
_CDot11ActiveWirelessClients_Object = MibTableColumn
cDot11ActiveWirelessClients = _CDot11ActiveWirelessClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1, 1),
    _CDot11ActiveWirelessClients_Type()
)
cDot11ActiveWirelessClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ActiveWirelessClients.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ActiveWirelessClients.setUnits("Device")


class _CDot11ActiveBridges_Type(Gauge32):
    """Custom type cDot11ActiveBridges based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_CDot11ActiveBridges_Type.__name__ = "Gauge32"
_CDot11ActiveBridges_Object = MibTableColumn
cDot11ActiveBridges = _CDot11ActiveBridges_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1, 2),
    _CDot11ActiveBridges_Type()
)
cDot11ActiveBridges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ActiveBridges.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ActiveBridges.setUnits("Device")


class _CDot11ActiveRepeaters_Type(Gauge32):
    """Custom type cDot11ActiveRepeaters based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2007),
    )


_CDot11ActiveRepeaters_Type.__name__ = "Gauge32"
_CDot11ActiveRepeaters_Object = MibTableColumn
cDot11ActiveRepeaters = _CDot11ActiveRepeaters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 2, 1, 3),
    _CDot11ActiveRepeaters_Type()
)
cDot11ActiveRepeaters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ActiveRepeaters.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ActiveRepeaters.setUnits("Device")
_CDot11AssociationStatsTable_Object = MibTable
cDot11AssociationStatsTable = _CDot11AssociationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cDot11AssociationStatsTable.setStatus("current")
_CDot11AssociationStatsEntry_Object = MibTableRow
cDot11AssociationStatsEntry = _CDot11AssociationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1)
)
cDot11AssociationStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cDot11AssociationStatsEntry.setStatus("current")
_CDot11AssStatsAssociated_Type = Counter32
_CDot11AssStatsAssociated_Object = MibTableColumn
cDot11AssStatsAssociated = _CDot11AssStatsAssociated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 1),
    _CDot11AssStatsAssociated_Type()
)
cDot11AssStatsAssociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AssStatsAssociated.setStatus("current")
if mibBuilder.loadTexts:
    cDot11AssStatsAssociated.setUnits("client")
_CDot11AssStatsAuthenticated_Type = Counter32
_CDot11AssStatsAuthenticated_Object = MibTableColumn
cDot11AssStatsAuthenticated = _CDot11AssStatsAuthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 2),
    _CDot11AssStatsAuthenticated_Type()
)
cDot11AssStatsAuthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AssStatsAuthenticated.setStatus("current")
if mibBuilder.loadTexts:
    cDot11AssStatsAuthenticated.setUnits("client")
_CDot11AssStatsRoamedIn_Type = Counter32
_CDot11AssStatsRoamedIn_Object = MibTableColumn
cDot11AssStatsRoamedIn = _CDot11AssStatsRoamedIn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 3),
    _CDot11AssStatsRoamedIn_Type()
)
cDot11AssStatsRoamedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AssStatsRoamedIn.setStatus("current")
if mibBuilder.loadTexts:
    cDot11AssStatsRoamedIn.setUnits("client")
_CDot11AssStatsRoamedAway_Type = Counter32
_CDot11AssStatsRoamedAway_Object = MibTableColumn
cDot11AssStatsRoamedAway = _CDot11AssStatsRoamedAway_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 4),
    _CDot11AssStatsRoamedAway_Type()
)
cDot11AssStatsRoamedAway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AssStatsRoamedAway.setStatus("current")
if mibBuilder.loadTexts:
    cDot11AssStatsRoamedAway.setUnits("client")
_CDot11AssStatsDeauthenticated_Type = Counter32
_CDot11AssStatsDeauthenticated_Object = MibTableColumn
cDot11AssStatsDeauthenticated = _CDot11AssStatsDeauthenticated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 5),
    _CDot11AssStatsDeauthenticated_Type()
)
cDot11AssStatsDeauthenticated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AssStatsDeauthenticated.setStatus("current")
if mibBuilder.loadTexts:
    cDot11AssStatsDeauthenticated.setUnits("client")
_CDot11AssStatsDisassociated_Type = Counter32
_CDot11AssStatsDisassociated_Object = MibTableColumn
cDot11AssStatsDisassociated = _CDot11AssStatsDisassociated_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 3, 1, 6),
    _CDot11AssStatsDisassociated_Type()
)
cDot11AssStatsDisassociated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11AssStatsDisassociated.setStatus("current")
if mibBuilder.loadTexts:
    cDot11AssStatsDisassociated.setUnits("client")
_Cd11IfCipherStatsTable_Object = MibTable
cd11IfCipherStatsTable = _Cd11IfCipherStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cd11IfCipherStatsTable.setStatus("current")
_Cd11IfCipherStatsEntry_Object = MibTableRow
cd11IfCipherStatsEntry = _Cd11IfCipherStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1)
)
cd11IfCipherStatsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cd11IfCipherStatsEntry.setStatus("current")
_Cd11IfCipherMicFailClientAddress_Type = MacAddress
_Cd11IfCipherMicFailClientAddress_Object = MibTableColumn
cd11IfCipherMicFailClientAddress = _Cd11IfCipherMicFailClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 1),
    _Cd11IfCipherMicFailClientAddress_Type()
)
cd11IfCipherMicFailClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCipherMicFailClientAddress.setStatus("current")
_Cd11IfCipherTkipLocalMicFailures_Type = Counter32
_Cd11IfCipherTkipLocalMicFailures_Object = MibTableColumn
cd11IfCipherTkipLocalMicFailures = _Cd11IfCipherTkipLocalMicFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 2),
    _Cd11IfCipherTkipLocalMicFailures_Type()
)
cd11IfCipherTkipLocalMicFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCipherTkipLocalMicFailures.setStatus("current")
_Cd11IfCipherTkipRemotMicFailures_Type = Counter32
_Cd11IfCipherTkipRemotMicFailures_Object = MibTableColumn
cd11IfCipherTkipRemotMicFailures = _Cd11IfCipherTkipRemotMicFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 3),
    _Cd11IfCipherTkipRemotMicFailures_Type()
)
cd11IfCipherTkipRemotMicFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCipherTkipRemotMicFailures.setStatus("current")
_Cd11IfCipherTkipCounterMeasInvok_Type = Counter32
_Cd11IfCipherTkipCounterMeasInvok_Object = MibTableColumn
cd11IfCipherTkipCounterMeasInvok = _Cd11IfCipherTkipCounterMeasInvok_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 4),
    _Cd11IfCipherTkipCounterMeasInvok_Type()
)
cd11IfCipherTkipCounterMeasInvok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCipherTkipCounterMeasInvok.setStatus("current")
_Cd11IfCipherCcmpReplaysDiscarded_Type = Counter32
_Cd11IfCipherCcmpReplaysDiscarded_Object = MibTableColumn
cd11IfCipherCcmpReplaysDiscarded = _Cd11IfCipherCcmpReplaysDiscarded_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 5),
    _Cd11IfCipherCcmpReplaysDiscarded_Type()
)
cd11IfCipherCcmpReplaysDiscarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCipherCcmpReplaysDiscarded.setStatus("current")
_Cd11IfCipherTkipReplaysDetected_Type = Counter32
_Cd11IfCipherTkipReplaysDetected_Object = MibTableColumn
cd11IfCipherTkipReplaysDetected = _Cd11IfCipherTkipReplaysDetected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 1, 4, 1, 6),
    _Cd11IfCipherTkipReplaysDetected_Type()
)
cd11IfCipherTkipReplaysDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cd11IfCipherTkipReplaysDetected.setStatus("current")
_CDot11ClientConfiguration_ObjectIdentity = ObjectIdentity
cDot11ClientConfiguration = _CDot11ClientConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2)
)
_CDot11ClientConfigInfoTable_Object = MibTable
cDot11ClientConfigInfoTable = _CDot11ClientConfigInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cDot11ClientConfigInfoTable.setStatus("current")
_CDot11ClientConfigInfoEntry_Object = MibTableRow
cDot11ClientConfigInfoEntry = _CDot11ClientConfigInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1)
)
cDot11ClientConfigInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-DOT11-IF-MIB", "cd11IfAuxSsid"),
    (0, "CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAddress"),
)
if mibBuilder.loadTexts:
    cDot11ClientConfigInfoEntry.setStatus("current")
_CDot11ClientAddress_Type = MacAddress
_CDot11ClientAddress_Object = MibTableColumn
cDot11ClientAddress = _CDot11ClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 1),
    _CDot11ClientAddress_Type()
)
cDot11ClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cDot11ClientAddress.setStatus("current")
_CDot11ClientParentAddress_Type = MacAddress
_CDot11ClientParentAddress_Object = MibTableColumn
cDot11ClientParentAddress = _CDot11ClientParentAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 2),
    _CDot11ClientParentAddress_Type()
)
cDot11ClientParentAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientParentAddress.setStatus("current")
_CDot11ClientRoleClassType_Type = CDot11ClientRoleClassType
_CDot11ClientRoleClassType_Object = MibTableColumn
cDot11ClientRoleClassType = _CDot11ClientRoleClassType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 3),
    _CDot11ClientRoleClassType_Type()
)
cDot11ClientRoleClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientRoleClassType.setStatus("current")
_CDot11ClientDevType_Type = CDot11ClientDevType
_CDot11ClientDevType_Object = MibTableColumn
cDot11ClientDevType = _CDot11ClientDevType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 4),
    _CDot11ClientDevType_Type()
)
cDot11ClientDevType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientDevType.setStatus("current")
_CDot11ClientRadioType_Type = CDot11ClientRadioType
_CDot11ClientRadioType_Object = MibTableColumn
cDot11ClientRadioType = _CDot11ClientRadioType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 5),
    _CDot11ClientRadioType_Type()
)
cDot11ClientRadioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientRadioType.setStatus("current")


class _CDot11ClientWepEnabled_Type(TruthValue):
    """Custom type cDot11ClientWepEnabled based on TruthValue"""


_CDot11ClientWepEnabled_Object = MibTableColumn
cDot11ClientWepEnabled = _CDot11ClientWepEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 6),
    _CDot11ClientWepEnabled_Type()
)
cDot11ClientWepEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientWepEnabled.setStatus("current")


class _CDot11ClientWepKeyMixEnabled_Type(TruthValue):
    """Custom type cDot11ClientWepKeyMixEnabled based on TruthValue"""


_CDot11ClientWepKeyMixEnabled_Object = MibTableColumn
cDot11ClientWepKeyMixEnabled = _CDot11ClientWepKeyMixEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 7),
    _CDot11ClientWepKeyMixEnabled_Type()
)
cDot11ClientWepKeyMixEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientWepKeyMixEnabled.setStatus("current")


class _CDot11ClientMicEnabled_Type(TruthValue):
    """Custom type cDot11ClientMicEnabled based on TruthValue"""


_CDot11ClientMicEnabled_Object = MibTableColumn
cDot11ClientMicEnabled = _CDot11ClientMicEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 8),
    _CDot11ClientMicEnabled_Type()
)
cDot11ClientMicEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientMicEnabled.setStatus("current")


class _CDot11ClientPowerSaveMode_Type(Integer32):
    """Custom type cDot11ClientPowerSaveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("powersave", 2))
    )


_CDot11ClientPowerSaveMode_Type.__name__ = "Integer32"
_CDot11ClientPowerSaveMode_Object = MibTableColumn
cDot11ClientPowerSaveMode = _CDot11ClientPowerSaveMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 9),
    _CDot11ClientPowerSaveMode_Type()
)
cDot11ClientPowerSaveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientPowerSaveMode.setStatus("current")


class _CDot11ClientAid_Type(Unsigned32):
    """Custom type cDot11ClientAid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2008),
    )


_CDot11ClientAid_Type.__name__ = "Unsigned32"
_CDot11ClientAid_Object = MibTableColumn
cDot11ClientAid = _CDot11ClientAid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 10),
    _CDot11ClientAid_Type()
)
cDot11ClientAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientAid.setStatus("current")


class _CDot11ClientDataRateSet_Type(OctetString):
    """Custom type cDot11ClientDataRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_CDot11ClientDataRateSet_Type.__name__ = "OctetString"
_CDot11ClientDataRateSet_Object = MibTableColumn
cDot11ClientDataRateSet = _CDot11ClientDataRateSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 11),
    _CDot11ClientDataRateSet_Type()
)
cDot11ClientDataRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientDataRateSet.setStatus("current")
_CDot11ClientSoftwareVersion_Type = SnmpAdminString
_CDot11ClientSoftwareVersion_Object = MibTableColumn
cDot11ClientSoftwareVersion = _CDot11ClientSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 12),
    _CDot11ClientSoftwareVersion_Type()
)
cDot11ClientSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientSoftwareVersion.setStatus("current")
_CDot11ClientName_Type = SnmpAdminString
_CDot11ClientName_Object = MibTableColumn
cDot11ClientName = _CDot11ClientName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 13),
    _CDot11ClientName_Type()
)
cDot11ClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientName.setStatus("current")


class _CDot11ClientAssociationState_Type(Integer32):
    """Custom type cDot11ClientAssociationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("assocAndAuthenticated", 3),
          ("assocNotAnuthenticated", 4),
          ("authenNotAssociated", 2),
          ("initial", 1))
    )


_CDot11ClientAssociationState_Type.__name__ = "Integer32"
_CDot11ClientAssociationState_Object = MibTableColumn
cDot11ClientAssociationState = _CDot11ClientAssociationState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 14),
    _CDot11ClientAssociationState_Type()
)
cDot11ClientAssociationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientAssociationState.setStatus("current")
_CDot11ClientIpAddressType_Type = InetAddressType
_CDot11ClientIpAddressType_Object = MibTableColumn
cDot11ClientIpAddressType = _CDot11ClientIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 15),
    _CDot11ClientIpAddressType_Type()
)
cDot11ClientIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientIpAddressType.setStatus("current")
_CDot11ClientIpAddress_Type = InetAddress
_CDot11ClientIpAddress_Object = MibTableColumn
cDot11ClientIpAddress = _CDot11ClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 16),
    _CDot11ClientIpAddress_Type()
)
cDot11ClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientIpAddress.setStatus("current")
_CDot11ClientVlanId_Type = CDot11IfVlanIdOrZero
_CDot11ClientVlanId_Object = MibTableColumn
cDot11ClientVlanId = _CDot11ClientVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 17),
    _CDot11ClientVlanId_Type()
)
cDot11ClientVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientVlanId.setStatus("current")
_CDot11ClientSubIfIndex_Type = InterfaceIndex
_CDot11ClientSubIfIndex_Object = MibTableColumn
cDot11ClientSubIfIndex = _CDot11ClientSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 18),
    _CDot11ClientSubIfIndex_Type()
)
cDot11ClientSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientSubIfIndex.setStatus("current")
_CDot11ClientAuthenAlgorithm_Type = CDot11AuthenticationMethod
_CDot11ClientAuthenAlgorithm_Object = MibTableColumn
cDot11ClientAuthenAlgorithm = _CDot11ClientAuthenAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 19),
    _CDot11ClientAuthenAlgorithm_Type()
)
cDot11ClientAuthenAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientAuthenAlgorithm.setStatus("current")
_CDot11ClientAdditionalAuthen_Type = CDot11AdditionalAuthenMethod
_CDot11ClientAdditionalAuthen_Object = MibTableColumn
cDot11ClientAdditionalAuthen = _CDot11ClientAdditionalAuthen_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 20),
    _CDot11ClientAdditionalAuthen_Type()
)
cDot11ClientAdditionalAuthen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientAdditionalAuthen.setStatus("current")
_CDot11ClientDot1xAuthenAlgorithm_Type = CDot11Dot1xAuthenMethod
_CDot11ClientDot1xAuthenAlgorithm_Object = MibTableColumn
cDot11ClientDot1xAuthenAlgorithm = _CDot11ClientDot1xAuthenAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 21),
    _CDot11ClientDot1xAuthenAlgorithm_Type()
)
cDot11ClientDot1xAuthenAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientDot1xAuthenAlgorithm.setStatus("current")
_CDot11ClientKeyManagement_Type = CDot11KeyManagementMethod
_CDot11ClientKeyManagement_Object = MibTableColumn
cDot11ClientKeyManagement = _CDot11ClientKeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 22),
    _CDot11ClientKeyManagement_Type()
)
cDot11ClientKeyManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientKeyManagement.setStatus("deprecated")
_CDot11ClientUnicastCipher_Type = CDot11IfCipherType
_CDot11ClientUnicastCipher_Object = MibTableColumn
cDot11ClientUnicastCipher = _CDot11ClientUnicastCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 23),
    _CDot11ClientUnicastCipher_Type()
)
cDot11ClientUnicastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientUnicastCipher.setStatus("current")
_CDot11ClientMulticastCipher_Type = CDot11IfCipherType
_CDot11ClientMulticastCipher_Object = MibTableColumn
cDot11ClientMulticastCipher = _CDot11ClientMulticastCipher_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 24),
    _CDot11ClientMulticastCipher_Type()
)
cDot11ClientMulticastCipher.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientMulticastCipher.setStatus("current")
_CDot11ClientDevObjectID_Type = ObjectIdentifier
_CDot11ClientDevObjectID_Object = MibTableColumn
cDot11ClientDevObjectID = _CDot11ClientDevObjectID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 25),
    _CDot11ClientDevObjectID_Type()
)
cDot11ClientDevObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientDevObjectID.setStatus("current")
_CDot11ClientNewKeyManagement_Type = CDot11NewKeyManagementMethod
_CDot11ClientNewKeyManagement_Object = MibTableColumn
cDot11ClientNewKeyManagement = _CDot11ClientNewKeyManagement_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 2, 1, 1, 26),
    _CDot11ClientNewKeyManagement_Type()
)
cDot11ClientNewKeyManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientNewKeyManagement.setStatus("current")
_CDot11ClientStatistics_ObjectIdentity = ObjectIdentity
cDot11ClientStatistics = _CDot11ClientStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3)
)
_CDot11ClientStatisticTable_Object = MibTable
cDot11ClientStatisticTable = _CDot11ClientStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cDot11ClientStatisticTable.setStatus("current")
_CDot11ClientStatisticEntry_Object = MibTableRow
cDot11ClientStatisticEntry = _CDot11ClientStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    cDot11ClientStatisticEntry.setStatus("current")


class _CDot11ClientCurrentTxRateSet_Type(OctetString):
    """Custom type cDot11ClientCurrentTxRateSet based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 126),
    )


_CDot11ClientCurrentTxRateSet_Type.__name__ = "OctetString"
_CDot11ClientCurrentTxRateSet_Object = MibTableColumn
cDot11ClientCurrentTxRateSet = _CDot11ClientCurrentTxRateSet_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 1),
    _CDot11ClientCurrentTxRateSet_Type()
)
cDot11ClientCurrentTxRateSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientCurrentTxRateSet.setStatus("current")
_CDot11ClientUpTime_Type = Unsigned32
_CDot11ClientUpTime_Object = MibTableColumn
cDot11ClientUpTime = _CDot11ClientUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 2),
    _CDot11ClientUpTime_Type()
)
cDot11ClientUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientUpTime.setUnits("second")


class _CDot11ClientSignalStrength_Type(Integer32):
    """Custom type cDot11ClientSignalStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 0),
    )


_CDot11ClientSignalStrength_Type.__name__ = "Integer32"
_CDot11ClientSignalStrength_Object = MibTableColumn
cDot11ClientSignalStrength = _CDot11ClientSignalStrength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 3),
    _CDot11ClientSignalStrength_Type()
)
cDot11ClientSignalStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientSignalStrength.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientSignalStrength.setUnits("dBm")


class _CDot11ClientSigQuality_Type(Unsigned32):
    """Custom type cDot11ClientSigQuality based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CDot11ClientSigQuality_Type.__name__ = "Unsigned32"
_CDot11ClientSigQuality_Object = MibTableColumn
cDot11ClientSigQuality = _CDot11ClientSigQuality_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 4),
    _CDot11ClientSigQuality_Type()
)
cDot11ClientSigQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientSigQuality.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientSigQuality.setUnits("percentage")
_CDot11ClientAgingLeft_Type = Gauge32
_CDot11ClientAgingLeft_Object = MibTableColumn
cDot11ClientAgingLeft = _CDot11ClientAgingLeft_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 5),
    _CDot11ClientAgingLeft_Type()
)
cDot11ClientAgingLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientAgingLeft.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientAgingLeft.setUnits("second")
_CDot11ClientPacketsReceived_Type = Counter32
_CDot11ClientPacketsReceived_Object = MibTableColumn
cDot11ClientPacketsReceived = _CDot11ClientPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 6),
    _CDot11ClientPacketsReceived_Type()
)
cDot11ClientPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientPacketsReceived.setUnits("packet")
_CDot11ClientBytesReceived_Type = Counter32
_CDot11ClientBytesReceived_Object = MibTableColumn
cDot11ClientBytesReceived = _CDot11ClientBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 7),
    _CDot11ClientBytesReceived_Type()
)
cDot11ClientBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientBytesReceived.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientBytesReceived.setUnits("byte")
_CDot11ClientPacketsSent_Type = Counter32
_CDot11ClientPacketsSent_Object = MibTableColumn
cDot11ClientPacketsSent = _CDot11ClientPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 8),
    _CDot11ClientPacketsSent_Type()
)
cDot11ClientPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientPacketsSent.setUnits("packet")
_CDot11ClientBytesSent_Type = Counter32
_CDot11ClientBytesSent_Object = MibTableColumn
cDot11ClientBytesSent = _CDot11ClientBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 9),
    _CDot11ClientBytesSent_Type()
)
cDot11ClientBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientBytesSent.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientBytesSent.setUnits("byte")
_CDot11ClientDuplicates_Type = Counter32
_CDot11ClientDuplicates_Object = MibTableColumn
cDot11ClientDuplicates = _CDot11ClientDuplicates_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 10),
    _CDot11ClientDuplicates_Type()
)
cDot11ClientDuplicates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientDuplicates.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientDuplicates.setUnits("packet")
_CDot11ClientMsduRetries_Type = Counter32
_CDot11ClientMsduRetries_Object = MibTableColumn
cDot11ClientMsduRetries = _CDot11ClientMsduRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 11),
    _CDot11ClientMsduRetries_Type()
)
cDot11ClientMsduRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientMsduRetries.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientMsduRetries.setUnits("packet")
_CDot11ClientMsduFails_Type = Counter32
_CDot11ClientMsduFails_Object = MibTableColumn
cDot11ClientMsduFails = _CDot11ClientMsduFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 12),
    _CDot11ClientMsduFails_Type()
)
cDot11ClientMsduFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientMsduFails.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientMsduFails.setUnits("packet")
_CDot11ClientWepErrors_Type = Counter32
_CDot11ClientWepErrors_Object = MibTableColumn
cDot11ClientWepErrors = _CDot11ClientWepErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 13),
    _CDot11ClientWepErrors_Type()
)
cDot11ClientWepErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientWepErrors.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientWepErrors.setUnits("packet")
_CDot11ClientMicErrors_Type = Counter32
_CDot11ClientMicErrors_Object = MibTableColumn
cDot11ClientMicErrors = _CDot11ClientMicErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 14),
    _CDot11ClientMicErrors_Type()
)
cDot11ClientMicErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientMicErrors.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientMicErrors.setUnits("error")
_CDot11ClientMicMissingFrames_Type = Counter32
_CDot11ClientMicMissingFrames_Object = MibTableColumn
cDot11ClientMicMissingFrames = _CDot11ClientMicMissingFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 1, 3, 1, 1, 15),
    _CDot11ClientMicMissingFrames_Type()
)
cDot11ClientMicMissingFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cDot11ClientMicMissingFrames.setStatus("current")
if mibBuilder.loadTexts:
    cDot11ClientMicMissingFrames.setUnits("packet")
_CiscoDot11AssocMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDot11AssocMIBConformance = _CiscoDot11AssocMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2)
)
_CiscoDot11AssocMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDot11AssocMIBCompliances = _CiscoDot11AssocMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1)
)
_CiscoDot11AssocMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDot11AssocMIBGroups = _CiscoDot11AssocMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2)
)
cDot11ClientConfigInfoEntry.registerAugmentions(
    ("CISCO-DOT11-ASSOCIATION-MIB",
     "cDot11ClientStatisticEntry")
)
cDot11ClientStatisticEntry.setIndexNames(*cDot11ClientConfigInfoEntry.getIndexNames())

# Managed Objects groups

ciscoDot11AssocGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 1)
)
ciscoDot11AssocGlobalGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ParentAddress"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveWirelessClients"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveBridges"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveRepeaters"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAssociated"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAuthenticated"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedIn"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedAway"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDeauthenticated"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDisassociated"))
)
if mibBuilder.loadTexts:
    ciscoDot11AssocGlobalGroup.setStatus("deprecated")

ciscoDot11ClientConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 2)
)
ciscoDot11ClientConfigGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientParentAddress"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientRoleClassType"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDevType"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientRadioType"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientWepEnabled"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientWepKeyMixEnabled"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMicEnabled"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientPowerSaveMode"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAid"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDataRateSet"))
)
if mibBuilder.loadTexts:
    ciscoDot11ClientConfigGroup.setStatus("current")

ciscoDot11ClientStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 3)
)
ciscoDot11ClientStatGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientCurrentTxRateSet"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientUpTime"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSignalStrength"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSigQuality"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientPacketsReceived"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientBytesReceived"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientPacketsSent"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientBytesSent"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAgingLeft"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDuplicates"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMsduRetries"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMsduFails"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientWepErrors"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMicErrors"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMicMissingFrames"))
)
if mibBuilder.loadTexts:
    ciscoDot11ClientStatGroup.setStatus("current")

ciscoDot11ClientInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 4)
)
ciscoDot11ClientInfoGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSoftwareVersion"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientName"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAssociationState"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientIpAddressType"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientIpAddress"))
)
if mibBuilder.loadTexts:
    ciscoDot11ClientInfoGroup.setStatus("current")

ciscoDot11ApAssocGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 5)
)
ciscoDot11ApAssocGlobalGroup.setObjects(
    ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ParentAddress")
)
if mibBuilder.loadTexts:
    ciscoDot11ApAssocGlobalGroup.setStatus("current")

ciscoDot11IfAssocStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 6)
)
ciscoDot11IfAssocStatGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveWirelessClients"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveBridges"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ActiveRepeaters"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAssociated"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsAuthenticated"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedIn"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsRoamedAway"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDeauthenticated"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11AssStatsDisassociated"))
)
if mibBuilder.loadTexts:
    ciscoDot11IfAssocStatGroup.setStatus("current")

ciscoDot11IfCipherStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 7)
)
ciscoDot11IfCipherStatGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherMicFailClientAddress"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipLocalMicFailures"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipRemotMicFailures"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipCounterMeasInvok"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherCcmpReplaysDiscarded"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cd11IfCipherTkipReplaysDetected"))
)
if mibBuilder.loadTexts:
    ciscoDot11IfCipherStatGroup.setStatus("current")

ciscoDot11ClientAuthenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 8)
)
ciscoDot11ClientAuthenGroup.setObjects(
      *(("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientVlanId"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientSubIfIndex"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAuthenAlgorithm"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientAdditionalAuthen"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDot1xAuthenAlgorithm"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientKeyManagement"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientUnicastCipher"),
        ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientMulticastCipher"))
)
if mibBuilder.loadTexts:
    ciscoDot11ClientAuthenGroup.setStatus("deprecated")

ciscoDot11ClientConfigExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 9)
)
ciscoDot11ClientConfigExtGroup.setObjects(
    ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientDevObjectID")
)
if mibBuilder.loadTexts:
    ciscoDot11ClientConfigExtGroup.setStatus("current")

ciscoDot11ClientNewAuthenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 2, 10)
)
ciscoDot11ClientNewAuthenGroup.setObjects(
    ("CISCO-DOT11-ASSOCIATION-MIB", "cDot11ClientNewKeyManagement")
)
if mibBuilder.loadTexts:
    ciscoDot11ClientNewAuthenGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDot11AssocMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDot11AssocMIBCompliance.setStatus(
        "deprecated"
    )

ciscoDot11AssocMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoDot11AssocMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoDot11AssocMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoDot11AssocMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoDot11AssocMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoDot11AssocMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoDot11AssocMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoDot11AssocMIBComplianceRev4.setStatus(
        "current"
    )

ciscoDot11AssocMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 273, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoDot11AssocMIBComplianceRev5.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DOT11-ASSOCIATION-MIB",
    **{"CDot11ClientRoleClassType": CDot11ClientRoleClassType,
       "CDot11ClientDevType": CDot11ClientDevType,
       "CDot11ClientRadioType": CDot11ClientRadioType,
       "CDot11AuthenticationMethod": CDot11AuthenticationMethod,
       "CDot11AdditionalAuthenMethod": CDot11AdditionalAuthenMethod,
       "CDot11Dot1xAuthenMethod": CDot11Dot1xAuthenMethod,
       "CDot11KeyManagementMethod": CDot11KeyManagementMethod,
       "CDot11NewKeyManagementMethod": CDot11NewKeyManagementMethod,
       "ciscoDot11AssociationMIB": ciscoDot11AssociationMIB,
       "ciscoDot11AssocMIBObjects": ciscoDot11AssocMIBObjects,
       "cDot11AssociationGlobal": cDot11AssociationGlobal,
       "cDot11ParentAddress": cDot11ParentAddress,
       "cDot11ActiveDevicesTable": cDot11ActiveDevicesTable,
       "cDot11ActiveDevicesEntry": cDot11ActiveDevicesEntry,
       "cDot11ActiveWirelessClients": cDot11ActiveWirelessClients,
       "cDot11ActiveBridges": cDot11ActiveBridges,
       "cDot11ActiveRepeaters": cDot11ActiveRepeaters,
       "cDot11AssociationStatsTable": cDot11AssociationStatsTable,
       "cDot11AssociationStatsEntry": cDot11AssociationStatsEntry,
       "cDot11AssStatsAssociated": cDot11AssStatsAssociated,
       "cDot11AssStatsAuthenticated": cDot11AssStatsAuthenticated,
       "cDot11AssStatsRoamedIn": cDot11AssStatsRoamedIn,
       "cDot11AssStatsRoamedAway": cDot11AssStatsRoamedAway,
       "cDot11AssStatsDeauthenticated": cDot11AssStatsDeauthenticated,
       "cDot11AssStatsDisassociated": cDot11AssStatsDisassociated,
       "cd11IfCipherStatsTable": cd11IfCipherStatsTable,
       "cd11IfCipherStatsEntry": cd11IfCipherStatsEntry,
       "cd11IfCipherMicFailClientAddress": cd11IfCipherMicFailClientAddress,
       "cd11IfCipherTkipLocalMicFailures": cd11IfCipherTkipLocalMicFailures,
       "cd11IfCipherTkipRemotMicFailures": cd11IfCipherTkipRemotMicFailures,
       "cd11IfCipherTkipCounterMeasInvok": cd11IfCipherTkipCounterMeasInvok,
       "cd11IfCipherCcmpReplaysDiscarded": cd11IfCipherCcmpReplaysDiscarded,
       "cd11IfCipherTkipReplaysDetected": cd11IfCipherTkipReplaysDetected,
       "cDot11ClientConfiguration": cDot11ClientConfiguration,
       "cDot11ClientConfigInfoTable": cDot11ClientConfigInfoTable,
       "cDot11ClientConfigInfoEntry": cDot11ClientConfigInfoEntry,
       "cDot11ClientAddress": cDot11ClientAddress,
       "cDot11ClientParentAddress": cDot11ClientParentAddress,
       "cDot11ClientRoleClassType": cDot11ClientRoleClassType,
       "cDot11ClientDevType": cDot11ClientDevType,
       "cDot11ClientRadioType": cDot11ClientRadioType,
       "cDot11ClientWepEnabled": cDot11ClientWepEnabled,
       "cDot11ClientWepKeyMixEnabled": cDot11ClientWepKeyMixEnabled,
       "cDot11ClientMicEnabled": cDot11ClientMicEnabled,
       "cDot11ClientPowerSaveMode": cDot11ClientPowerSaveMode,
       "cDot11ClientAid": cDot11ClientAid,
       "cDot11ClientDataRateSet": cDot11ClientDataRateSet,
       "cDot11ClientSoftwareVersion": cDot11ClientSoftwareVersion,
       "cDot11ClientName": cDot11ClientName,
       "cDot11ClientAssociationState": cDot11ClientAssociationState,
       "cDot11ClientIpAddressType": cDot11ClientIpAddressType,
       "cDot11ClientIpAddress": cDot11ClientIpAddress,
       "cDot11ClientVlanId": cDot11ClientVlanId,
       "cDot11ClientSubIfIndex": cDot11ClientSubIfIndex,
       "cDot11ClientAuthenAlgorithm": cDot11ClientAuthenAlgorithm,
       "cDot11ClientAdditionalAuthen": cDot11ClientAdditionalAuthen,
       "cDot11ClientDot1xAuthenAlgorithm": cDot11ClientDot1xAuthenAlgorithm,
       "cDot11ClientKeyManagement": cDot11ClientKeyManagement,
       "cDot11ClientUnicastCipher": cDot11ClientUnicastCipher,
       "cDot11ClientMulticastCipher": cDot11ClientMulticastCipher,
       "cDot11ClientDevObjectID": cDot11ClientDevObjectID,
       "cDot11ClientNewKeyManagement": cDot11ClientNewKeyManagement,
       "cDot11ClientStatistics": cDot11ClientStatistics,
       "cDot11ClientStatisticTable": cDot11ClientStatisticTable,
       "cDot11ClientStatisticEntry": cDot11ClientStatisticEntry,
       "cDot11ClientCurrentTxRateSet": cDot11ClientCurrentTxRateSet,
       "cDot11ClientUpTime": cDot11ClientUpTime,
       "cDot11ClientSignalStrength": cDot11ClientSignalStrength,
       "cDot11ClientSigQuality": cDot11ClientSigQuality,
       "cDot11ClientAgingLeft": cDot11ClientAgingLeft,
       "cDot11ClientPacketsReceived": cDot11ClientPacketsReceived,
       "cDot11ClientBytesReceived": cDot11ClientBytesReceived,
       "cDot11ClientPacketsSent": cDot11ClientPacketsSent,
       "cDot11ClientBytesSent": cDot11ClientBytesSent,
       "cDot11ClientDuplicates": cDot11ClientDuplicates,
       "cDot11ClientMsduRetries": cDot11ClientMsduRetries,
       "cDot11ClientMsduFails": cDot11ClientMsduFails,
       "cDot11ClientWepErrors": cDot11ClientWepErrors,
       "cDot11ClientMicErrors": cDot11ClientMicErrors,
       "cDot11ClientMicMissingFrames": cDot11ClientMicMissingFrames,
       "ciscoDot11AssocMIBConformance": ciscoDot11AssocMIBConformance,
       "ciscoDot11AssocMIBCompliances": ciscoDot11AssocMIBCompliances,
       "ciscoDot11AssocMIBCompliance": ciscoDot11AssocMIBCompliance,
       "ciscoDot11AssocMIBComplianceRev1": ciscoDot11AssocMIBComplianceRev1,
       "ciscoDot11AssocMIBComplianceRev2": ciscoDot11AssocMIBComplianceRev2,
       "ciscoDot11AssocMIBComplianceRev3": ciscoDot11AssocMIBComplianceRev3,
       "ciscoDot11AssocMIBComplianceRev4": ciscoDot11AssocMIBComplianceRev4,
       "ciscoDot11AssocMIBComplianceRev5": ciscoDot11AssocMIBComplianceRev5,
       "ciscoDot11AssocMIBGroups": ciscoDot11AssocMIBGroups,
       "ciscoDot11AssocGlobalGroup": ciscoDot11AssocGlobalGroup,
       "ciscoDot11ClientConfigGroup": ciscoDot11ClientConfigGroup,
       "ciscoDot11ClientStatGroup": ciscoDot11ClientStatGroup,
       "ciscoDot11ClientInfoGroup": ciscoDot11ClientInfoGroup,
       "ciscoDot11ApAssocGlobalGroup": ciscoDot11ApAssocGlobalGroup,
       "ciscoDot11IfAssocStatGroup": ciscoDot11IfAssocStatGroup,
       "ciscoDot11IfCipherStatGroup": ciscoDot11IfCipherStatGroup,
       "ciscoDot11ClientAuthenGroup": ciscoDot11ClientAuthenGroup,
       "ciscoDot11ClientConfigExtGroup": ciscoDot11ClientConfigExtGroup,
       "ciscoDot11ClientNewAuthenGroup": ciscoDot11ClientNewAuthenGroup}
)
