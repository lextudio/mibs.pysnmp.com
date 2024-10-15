# SNMP MIB module (CISCO-LWAPP-MESH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MESH-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:42 2024
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

(cLApName,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName",
    "cLApSysMacAddress")

(CLDot11Channel,) = mibBuilder.importSymbols(
    "CISCO-LWAPP-TC-MIB",
    "CLDot11Channel")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoLwappMeshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616)
)
ciscoLwappMeshMIB.setRevisions(
        ("2010-10-07 00:00",
         "2010-03-03 00:00",
         "2007-03-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMeshMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBNotifs = _CiscoLwappMeshMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0)
)
_CiscoLwappMeshMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBObjects = _CiscoLwappMeshMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1)
)
_CiscoLwappMeshConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshConfig = _CiscoLwappMeshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1)
)
_ClMeshNodeTable_Object = MibTable
clMeshNodeTable = _ClMeshNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clMeshNodeTable.setStatus("current")
_ClMeshNodeEntry_Object = MibTableRow
clMeshNodeEntry = _ClMeshNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1)
)
clMeshNodeEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNodeEntry.setStatus("current")


class _ClMeshNodeRole_Type(Integer32):
    """Custom type clMeshNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("map", 1),
          ("rap", 2))
    )


_ClMeshNodeRole_Type.__name__ = "Integer32"
_ClMeshNodeRole_Object = MibTableColumn
clMeshNodeRole = _ClMeshNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 1),
    _ClMeshNodeRole_Type()
)
clMeshNodeRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeRole.setStatus("current")


class _ClMeshNodeGroupName_Type(SnmpAdminString):
    """Custom type clMeshNodeGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ClMeshNodeGroupName_Type.__name__ = "SnmpAdminString"
_ClMeshNodeGroupName_Object = MibTableColumn
clMeshNodeGroupName = _ClMeshNodeGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 2),
    _ClMeshNodeGroupName_Type()
)
clMeshNodeGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeGroupName.setStatus("current")


class _ClMeshNodeBackhaul_Type(Integer32):
    """Custom type clMeshNodeBackhaul based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot11a", 1),
          ("dot11b", 2),
          ("dot11g", 3))
    )


_ClMeshNodeBackhaul_Type.__name__ = "Integer32"
_ClMeshNodeBackhaul_Object = MibTableColumn
clMeshNodeBackhaul = _ClMeshNodeBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 3),
    _ClMeshNodeBackhaul_Type()
)
clMeshNodeBackhaul.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBackhaul.setStatus("current")
_ClMeshNodeBackhaulDataRate_Type = Unsigned32
_ClMeshNodeBackhaulDataRate_Object = MibTableColumn
clMeshNodeBackhaulDataRate = _ClMeshNodeBackhaulDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 4),
    _ClMeshNodeBackhaulDataRate_Type()
)
clMeshNodeBackhaulDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBackhaulDataRate.setStatus("deprecated")
if mibBuilder.loadTexts:
    clMeshNodeBackhaulDataRate.setUnits("Kbps")
_ClMeshNodeEthernetBridge_Type = TruthValue
_ClMeshNodeEthernetBridge_Object = MibTableColumn
clMeshNodeEthernetBridge = _ClMeshNodeEthernetBridge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 5),
    _ClMeshNodeEthernetBridge_Type()
)
clMeshNodeEthernetBridge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeEthernetBridge.setStatus("current")


class _ClMeshNodeEthernetLinkStatus_Type(Integer32):
    """Custom type clMeshNodeEthernetLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_ClMeshNodeEthernetLinkStatus_Type.__name__ = "Integer32"
_ClMeshNodeEthernetLinkStatus_Object = MibTableColumn
clMeshNodeEthernetLinkStatus = _ClMeshNodeEthernetLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 6),
    _ClMeshNodeEthernetLinkStatus_Type()
)
clMeshNodeEthernetLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeEthernetLinkStatus.setStatus("current")
_ClMeshNodePublicSafetyBackhaul_Type = TruthValue
_ClMeshNodePublicSafetyBackhaul_Object = MibTableColumn
clMeshNodePublicSafetyBackhaul = _ClMeshNodePublicSafetyBackhaul_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 7),
    _ClMeshNodePublicSafetyBackhaul_Type()
)
clMeshNodePublicSafetyBackhaul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodePublicSafetyBackhaul.setStatus("deprecated")
_ClMeshNodeParentMacAddress_Type = MacAddress
_ClMeshNodeParentMacAddress_Object = MibTableColumn
clMeshNodeParentMacAddress = _ClMeshNodeParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 8),
    _ClMeshNodeParentMacAddress_Type()
)
clMeshNodeParentMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeParentMacAddress.setStatus("current")


class _ClMeshNodeHeaterStatus_Type(Integer32):
    """Custom type clMeshNodeHeaterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_ClMeshNodeHeaterStatus_Type.__name__ = "Integer32"
_ClMeshNodeHeaterStatus_Object = MibTableColumn
clMeshNodeHeaterStatus = _ClMeshNodeHeaterStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 9),
    _ClMeshNodeHeaterStatus_Type()
)
clMeshNodeHeaterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeHeaterStatus.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeHeaterStatus.setUnits("Percent")
_ClMeshNodeInternalTemp_Type = Integer32
_ClMeshNodeInternalTemp_Object = MibTableColumn
clMeshNodeInternalTemp = _ClMeshNodeInternalTemp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 10),
    _ClMeshNodeInternalTemp_Type()
)
clMeshNodeInternalTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeInternalTemp.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeInternalTemp.setUnits("degree Celsius")


class _ClMeshNodeType_Type(Integer32):
    """Custom type clMeshNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("indoor", 1),
          ("outdoor", 2))
    )


_ClMeshNodeType_Type.__name__ = "Integer32"
_ClMeshNodeType_Object = MibTableColumn
clMeshNodeType = _ClMeshNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 11),
    _ClMeshNodeType_Type()
)
clMeshNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeType.setStatus("current")
_ClMeshNodeHops_Type = Gauge32
_ClMeshNodeHops_Object = MibTableColumn
clMeshNodeHops = _ClMeshNodeHops_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 12),
    _ClMeshNodeHops_Type()
)
clMeshNodeHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeHops.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeHops.setUnits("hops")


class _ClMeshNodeChildCount_Type(Gauge32):
    """Custom type clMeshNodeChildCount based on Gauge32"""
    defaultValue = 0


_ClMeshNodeChildCount_Object = MibTableColumn
clMeshNodeChildCount = _ClMeshNodeChildCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 13),
    _ClMeshNodeChildCount_Type()
)
clMeshNodeChildCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeChildCount.setStatus("current")


class _ClMeshNodeBackhaulRadio_Type(Integer32):
    """Custom type clMeshNodeBackhaulRadio based on Integer32"""
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
        *(("dot11a", 3),
          ("dot11bg", 2),
          ("unknown", 1))
    )


_ClMeshNodeBackhaulRadio_Type.__name__ = "Integer32"
_ClMeshNodeBackhaulRadio_Object = MibTableColumn
clMeshNodeBackhaulRadio = _ClMeshNodeBackhaulRadio_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 14),
    _ClMeshNodeBackhaulRadio_Type()
)
clMeshNodeBackhaulRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBackhaulRadio.setStatus("current")


class _ClMeshNodeBHDataRate_Type(Integer32):
    """Custom type clMeshNodeBHDataRate based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              29)
        )
    )
    namedValues = NamedValues(
        *(("auto", 13),
          ("htMcs0", 14),
          ("htMcs1", 15),
          ("htMcs10", 24),
          ("htMcs11", 25),
          ("htMcs12", 26),
          ("htMcs13", 27),
          ("htMcs14", 28),
          ("htMcs15", 29),
          ("htMcs2", 16),
          ("htMcs3", 17),
          ("htMcs4", 18),
          ("htMcs5", 19),
          ("htMcs6", 20),
          ("htMcs7", 21),
          ("htMcs8", 22),
          ("htMcs9", 23),
          ("mbps1", 1),
          ("mbps11", 6),
          ("mbps12", 7),
          ("mbps18", 8),
          ("mbps2", 2),
          ("mbps24", 9),
          ("mbps36", 10),
          ("mbps48", 11),
          ("mbps54", 12),
          ("mbps5point5", 3),
          ("mbps6", 4),
          ("mbps9", 5))
    )


_ClMeshNodeBHDataRate_Type.__name__ = "Integer32"
_ClMeshNodeBHDataRate_Object = MibTableColumn
clMeshNodeBHDataRate = _ClMeshNodeBHDataRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 1, 1, 1, 15),
    _ClMeshNodeBHDataRate_Type()
)
clMeshNodeBHDataRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeBHDataRate.setStatus("current")
_CiscoLwappMeshGlobalConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshGlobalConfig = _CiscoLwappMeshGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2)
)


class _ClMeshNodeRange_Type(Unsigned32):
    """Custom type clMeshNodeRange based on Unsigned32"""
    defaultValue = 12000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 132000),
    )


_ClMeshNodeRange_Type.__name__ = "Unsigned32"
_ClMeshNodeRange_Object = MibScalar
clMeshNodeRange = _ClMeshNodeRange_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 1),
    _ClMeshNodeRange_Type()
)
clMeshNodeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshNodeRange.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeRange.setUnits("feet")


class _ClMeshBackhaulClientAccess_Type(TruthValue):
    """Custom type clMeshBackhaulClientAccess based on TruthValue"""


_ClMeshBackhaulClientAccess_Object = MibScalar
clMeshBackhaulClientAccess = _ClMeshBackhaulClientAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 2),
    _ClMeshBackhaulClientAccess_Type()
)
clMeshBackhaulClientAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshBackhaulClientAccess.setStatus("current")


class _ClMeshMacFilterList_Type(TruthValue):
    """Custom type clMeshMacFilterList based on TruthValue"""


_ClMeshMacFilterList_Object = MibScalar
clMeshMacFilterList = _ClMeshMacFilterList_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 3),
    _ClMeshMacFilterList_Type()
)
clMeshMacFilterList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMacFilterList.setStatus("current")


class _ClMeshMeshNodeAuthFailureThreshold_Type(Unsigned32):
    """Custom type clMeshMeshNodeAuthFailureThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ClMeshMeshNodeAuthFailureThreshold_Type.__name__ = "Unsigned32"
_ClMeshMeshNodeAuthFailureThreshold_Object = MibScalar
clMeshMeshNodeAuthFailureThreshold = _ClMeshMeshNodeAuthFailureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 4),
    _ClMeshMeshNodeAuthFailureThreshold_Type()
)
clMeshMeshNodeAuthFailureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMeshNodeAuthFailureThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clMeshMeshNodeAuthFailureThreshold.setUnits("failures")


class _ClMeshMeshChildAssociationFailuresThreshold_Type(Unsigned32):
    """Custom type clMeshMeshChildAssociationFailuresThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 30),
    )


_ClMeshMeshChildAssociationFailuresThreshold_Type.__name__ = "Unsigned32"
_ClMeshMeshChildAssociationFailuresThreshold_Object = MibScalar
clMeshMeshChildAssociationFailuresThreshold = _ClMeshMeshChildAssociationFailuresThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 5),
    _ClMeshMeshChildAssociationFailuresThreshold_Type()
)
clMeshMeshChildAssociationFailuresThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMeshChildAssociationFailuresThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clMeshMeshChildAssociationFailuresThreshold.setUnits("failures")


class _ClMeshMeshChildExcludedParentInterval_Type(TimeInterval):
    """Custom type clMeshMeshChildExcludedParentInterval based on TimeInterval"""
    defaultValue = 48000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18000, 96000),
    )


_ClMeshMeshChildExcludedParentInterval_Type.__name__ = "TimeInterval"
_ClMeshMeshChildExcludedParentInterval_Object = MibScalar
clMeshMeshChildExcludedParentInterval = _ClMeshMeshChildExcludedParentInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 6),
    _ClMeshMeshChildExcludedParentInterval_Type()
)
clMeshMeshChildExcludedParentInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshMeshChildExcludedParentInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshMeshChildExcludedParentInterval.setUnits("hundredths-seconds")


class _ClMeshSNRThresholdAbate_Type(Unsigned32):
    """Custom type clMeshSNRThresholdAbate based on Unsigned32"""
    defaultValue = 16

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_ClMeshSNRThresholdAbate_Type.__name__ = "Unsigned32"
_ClMeshSNRThresholdAbate_Object = MibScalar
clMeshSNRThresholdAbate = _ClMeshSNRThresholdAbate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 7),
    _ClMeshSNRThresholdAbate_Type()
)
clMeshSNRThresholdAbate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshSNRThresholdAbate.setStatus("current")
if mibBuilder.loadTexts:
    clMeshSNRThresholdAbate.setUnits("db")


class _ClMeshSNRThresholdOnset_Type(Unsigned32):
    """Custom type clMeshSNRThresholdOnset based on Unsigned32"""
    defaultValue = 12

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 50),
    )


_ClMeshSNRThresholdOnset_Type.__name__ = "Unsigned32"
_ClMeshSNRThresholdOnset_Object = MibScalar
clMeshSNRThresholdOnset = _ClMeshSNRThresholdOnset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 8),
    _ClMeshSNRThresholdOnset_Type()
)
clMeshSNRThresholdOnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshSNRThresholdOnset.setStatus("current")
if mibBuilder.loadTexts:
    clMeshSNRThresholdOnset.setUnits("db")


class _ClMeshSNRCheckTimeInterval_Type(TimeInterval):
    """Custom type clMeshSNRCheckTimeInterval based on TimeInterval"""
    defaultValue = 18000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(18000, 96000),
    )


_ClMeshSNRCheckTimeInterval_Type.__name__ = "TimeInterval"
_ClMeshSNRCheckTimeInterval_Object = MibScalar
clMeshSNRCheckTimeInterval = _ClMeshSNRCheckTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 9),
    _ClMeshSNRCheckTimeInterval_Type()
)
clMeshSNRCheckTimeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshSNRCheckTimeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshSNRCheckTimeInterval.setUnits("hundredths-seconds")


class _ClMeshExcessiveParentChangeThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveParentChangeThreshold based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveParentChangeThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveParentChangeThreshold_Object = MibScalar
clMeshExcessiveParentChangeThreshold = _ClMeshExcessiveParentChangeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 10),
    _ClMeshExcessiveParentChangeThreshold_Type()
)
clMeshExcessiveParentChangeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeThreshold.setUnits("occcurences")


class _ClMeshExcessiveParentChangeInterval_Type(TimeInterval):
    """Custom type clMeshExcessiveParentChangeInterval based on TimeInterval"""
    defaultValue = 360000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180000, 360000),
    )


_ClMeshExcessiveParentChangeInterval_Type.__name__ = "TimeInterval"
_ClMeshExcessiveParentChangeInterval_Object = MibScalar
clMeshExcessiveParentChangeInterval = _ClMeshExcessiveParentChangeInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 11),
    _ClMeshExcessiveParentChangeInterval_Type()
)
clMeshExcessiveParentChangeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeInterval.setStatus("current")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeInterval.setUnits("hundredths-seconds")


class _ClMeshBackgroundScan_Type(TruthValue):
    """Custom type clMeshBackgroundScan based on TruthValue"""


_ClMeshBackgroundScan_Object = MibScalar
clMeshBackgroundScan = _ClMeshBackgroundScan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 12),
    _ClMeshBackgroundScan_Type()
)
clMeshBackgroundScan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshBackgroundScan.setStatus("current")


class _ClMeshAuthenticationMode_Type(Integer32):
    """Custom type clMeshAuthenticationMode based on Integer32"""
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
        *(("eap", 2),
          ("none", 1),
          ("psk", 3))
    )


_ClMeshAuthenticationMode_Type.__name__ = "Integer32"
_ClMeshAuthenticationMode_Object = MibScalar
clMeshAuthenticationMode = _ClMeshAuthenticationMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 13),
    _ClMeshAuthenticationMode_Type()
)
clMeshAuthenticationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshAuthenticationMode.setStatus("current")


class _ClMeshExcessiveHopCountThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveHopCountThreshold based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveHopCountThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveHopCountThreshold_Object = MibScalar
clMeshExcessiveHopCountThreshold = _ClMeshExcessiveHopCountThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 14),
    _ClMeshExcessiveHopCountThreshold_Type()
)
clMeshExcessiveHopCountThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveHopCountThreshold.setStatus("current")


class _ClMeshExcessiveRapChildThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveRapChildThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveRapChildThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveRapChildThreshold_Object = MibScalar
clMeshExcessiveRapChildThreshold = _ClMeshExcessiveRapChildThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 15),
    _ClMeshExcessiveRapChildThreshold_Type()
)
clMeshExcessiveRapChildThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveRapChildThreshold.setStatus("current")


class _ClMeshExcessiveMapChildThreshold_Type(Unsigned32):
    """Custom type clMeshExcessiveMapChildThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ClMeshExcessiveMapChildThreshold_Type.__name__ = "Unsigned32"
_ClMeshExcessiveMapChildThreshold_Object = MibScalar
clMeshExcessiveMapChildThreshold = _ClMeshExcessiveMapChildThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 16),
    _ClMeshExcessiveMapChildThreshold_Type()
)
clMeshExcessiveMapChildThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveMapChildThreshold.setStatus("current")


class _ClMeshHighSNRThresholdAbate_Type(Unsigned32):
    """Custom type clMeshHighSNRThresholdAbate based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 80),
    )


_ClMeshHighSNRThresholdAbate_Type.__name__ = "Unsigned32"
_ClMeshHighSNRThresholdAbate_Object = MibScalar
clMeshHighSNRThresholdAbate = _ClMeshHighSNRThresholdAbate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 17),
    _ClMeshHighSNRThresholdAbate_Type()
)
clMeshHighSNRThresholdAbate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdAbate.setStatus("current")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdAbate.setUnits("db")


class _ClMeshHighSNRThresholdOnset_Type(Unsigned32):
    """Custom type clMeshHighSNRThresholdOnset based on Unsigned32"""
    defaultValue = 56

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 80),
    )


_ClMeshHighSNRThresholdOnset_Type.__name__ = "Unsigned32"
_ClMeshHighSNRThresholdOnset_Object = MibScalar
clMeshHighSNRThresholdOnset = _ClMeshHighSNRThresholdOnset_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 18),
    _ClMeshHighSNRThresholdOnset_Type()
)
clMeshHighSNRThresholdOnset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdOnset.setStatus("current")
if mibBuilder.loadTexts:
    clMeshHighSNRThresholdOnset.setUnits("db")


class _ClMeshPublicSafetyBackhaulGlobal_Type(TruthValue):
    """Custom type clMeshPublicSafetyBackhaulGlobal based on TruthValue"""


_ClMeshPublicSafetyBackhaulGlobal_Object = MibScalar
clMeshPublicSafetyBackhaulGlobal = _ClMeshPublicSafetyBackhaulGlobal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 19),
    _ClMeshPublicSafetyBackhaulGlobal_Type()
)
clMeshPublicSafetyBackhaulGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPublicSafetyBackhaulGlobal.setStatus("current")


class _ClMeshisAMSDUEnable_Type(TruthValue):
    """Custom type clMeshisAMSDUEnable based on TruthValue"""


_ClMeshisAMSDUEnable_Object = MibScalar
clMeshisAMSDUEnable = _ClMeshisAMSDUEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 20),
    _ClMeshisAMSDUEnable_Type()
)
clMeshisAMSDUEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshisAMSDUEnable.setStatus("current")


class _ClMeshIsIdsEnable_Type(TruthValue):
    """Custom type clMeshIsIdsEnable based on TruthValue"""


_ClMeshIsIdsEnable_Object = MibScalar
clMeshIsIdsEnable = _ClMeshIsIdsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 21),
    _ClMeshIsIdsEnable_Type()
)
clMeshIsIdsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsIdsEnable.setStatus("current")


class _ClMeshIsDCAChannelsEnable_Type(TruthValue):
    """Custom type clMeshIsDCAChannelsEnable based on TruthValue"""


_ClMeshIsDCAChannelsEnable_Object = MibScalar
clMeshIsDCAChannelsEnable = _ClMeshIsDCAChannelsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 22),
    _ClMeshIsDCAChannelsEnable_Type()
)
clMeshIsDCAChannelsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsDCAChannelsEnable.setStatus("current")


class _ClMeshIsExtendedUAEnable_Type(TruthValue):
    """Custom type clMeshIsExtendedUAEnable based on TruthValue"""


_ClMeshIsExtendedUAEnable_Object = MibScalar
clMeshIsExtendedUAEnable = _ClMeshIsExtendedUAEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 2, 23),
    _ClMeshIsExtendedUAEnable_Type()
)
clMeshIsExtendedUAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshIsExtendedUAEnable.setStatus("current")
_CiscoLwappMeshNeighborsStatus_ObjectIdentity = ObjectIdentity
ciscoLwappMeshNeighborsStatus = _CiscoLwappMeshNeighborsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3)
)
_ClMeshNeighborTable_Object = MibTable
clMeshNeighborTable = _ClMeshNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1)
)
if mibBuilder.loadTexts:
    clMeshNeighborTable.setStatus("current")
_ClMeshNeighborEntry_Object = MibTableRow
clMeshNeighborEntry = _ClMeshNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1)
)
clMeshNeighborEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
    (0, "CISCO-LWAPP-MESH-MIB", "clMeshNeighborMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNeighborEntry.setStatus("current")
_ClMeshNeighborMacAddress_Type = MacAddress
_ClMeshNeighborMacAddress_Object = MibTableColumn
clMeshNeighborMacAddress = _ClMeshNeighborMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 1),
    _ClMeshNeighborMacAddress_Type()
)
clMeshNeighborMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clMeshNeighborMacAddress.setStatus("current")


class _ClMeshNeighborType_Type(Bits):
    """Custom type clMeshNeighborType based on Bits"""
    namedValues = NamedValues(
        *(("beacon", 4),
          ("child", 3),
          ("default", 5),
          ("excluded", 2),
          ("neighbor", 1),
          ("parent", 0))
    )

_ClMeshNeighborType_Type.__name__ = "Bits"
_ClMeshNeighborType_Object = MibTableColumn
clMeshNeighborType = _ClMeshNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 2),
    _ClMeshNeighborType_Type()
)
clMeshNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborType.setStatus("current")
_ClMeshNeighborLinkSnr_Type = Integer32
_ClMeshNeighborLinkSnr_Object = MibTableColumn
clMeshNeighborLinkSnr = _ClMeshNeighborLinkSnr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 3),
    _ClMeshNeighborLinkSnr_Type()
)
clMeshNeighborLinkSnr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborLinkSnr.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNeighborLinkSnr.setUnits("dB")
_ClMeshNeighborChannel_Type = CLDot11Channel
_ClMeshNeighborChannel_Object = MibTableColumn
clMeshNeighborChannel = _ClMeshNeighborChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 4),
    _ClMeshNeighborChannel_Type()
)
clMeshNeighborChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborChannel.setStatus("current")
_ClMeshNeighborUpdate_Type = TimeStamp
_ClMeshNeighborUpdate_Object = MibTableColumn
clMeshNeighborUpdate = _ClMeshNeighborUpdate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 3, 1, 1, 5),
    _ClMeshNeighborUpdate_Type()
)
clMeshNeighborUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNeighborUpdate.setStatus("current")
_CiscoLwappMeshNotifControlConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshNotifControlConfig = _CiscoLwappMeshNotifControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4)
)


class _ClMeshAuthFailureNotifEnabled_Type(TruthValue):
    """Custom type clMeshAuthFailureNotifEnabled based on TruthValue"""


_ClMeshAuthFailureNotifEnabled_Object = MibScalar
clMeshAuthFailureNotifEnabled = _ClMeshAuthFailureNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 1),
    _ClMeshAuthFailureNotifEnabled_Type()
)
clMeshAuthFailureNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshAuthFailureNotifEnabled.setStatus("current")


class _ClMeshChildExcludedParentNotifEnabled_Type(TruthValue):
    """Custom type clMeshChildExcludedParentNotifEnabled based on TruthValue"""


_ClMeshChildExcludedParentNotifEnabled_Object = MibScalar
clMeshChildExcludedParentNotifEnabled = _ClMeshChildExcludedParentNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 2),
    _ClMeshChildExcludedParentNotifEnabled_Type()
)
clMeshChildExcludedParentNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshChildExcludedParentNotifEnabled.setStatus("current")


class _ClMeshParentChangeNotifEnabled_Type(TruthValue):
    """Custom type clMeshParentChangeNotifEnabled based on TruthValue"""


_ClMeshParentChangeNotifEnabled_Object = MibScalar
clMeshParentChangeNotifEnabled = _ClMeshParentChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 3),
    _ClMeshParentChangeNotifEnabled_Type()
)
clMeshParentChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshParentChangeNotifEnabled.setStatus("current")


class _ClMeshChildMovedNotifEnabled_Type(TruthValue):
    """Custom type clMeshChildMovedNotifEnabled based on TruthValue"""


_ClMeshChildMovedNotifEnabled_Object = MibScalar
clMeshChildMovedNotifEnabled = _ClMeshChildMovedNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 4),
    _ClMeshChildMovedNotifEnabled_Type()
)
clMeshChildMovedNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshChildMovedNotifEnabled.setStatus("current")


class _ClMeshExcessiveParentChangeNotifEnabled_Type(TruthValue):
    """Custom type clMeshExcessiveParentChangeNotifEnabled based on TruthValue"""


_ClMeshExcessiveParentChangeNotifEnabled_Object = MibScalar
clMeshExcessiveParentChangeNotifEnabled = _ClMeshExcessiveParentChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 5),
    _ClMeshExcessiveParentChangeNotifEnabled_Type()
)
clMeshExcessiveParentChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveParentChangeNotifEnabled.setStatus("current")


class _ClMeshPoorSNRNotifEnabled_Type(TruthValue):
    """Custom type clMeshPoorSNRNotifEnabled based on TruthValue"""


_ClMeshPoorSNRNotifEnabled_Object = MibScalar
clMeshPoorSNRNotifEnabled = _ClMeshPoorSNRNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 6),
    _ClMeshPoorSNRNotifEnabled_Type()
)
clMeshPoorSNRNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshPoorSNRNotifEnabled.setStatus("current")


class _ClMeshConsoleLoginNotifEnabled_Type(TruthValue):
    """Custom type clMeshConsoleLoginNotifEnabled based on TruthValue"""


_ClMeshConsoleLoginNotifEnabled_Object = MibScalar
clMeshConsoleLoginNotifEnabled = _ClMeshConsoleLoginNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 7),
    _ClMeshConsoleLoginNotifEnabled_Type()
)
clMeshConsoleLoginNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshConsoleLoginNotifEnabled.setStatus("current")


class _ClMeshDefaultBridgeGroupNameNotifEnabled_Type(TruthValue):
    """Custom type clMeshDefaultBridgeGroupNameNotifEnabled based on TruthValue"""


_ClMeshDefaultBridgeGroupNameNotifEnabled_Object = MibScalar
clMeshDefaultBridgeGroupNameNotifEnabled = _ClMeshDefaultBridgeGroupNameNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 8),
    _ClMeshDefaultBridgeGroupNameNotifEnabled_Type()
)
clMeshDefaultBridgeGroupNameNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshDefaultBridgeGroupNameNotifEnabled.setStatus("current")


class _ClMeshExcessiveHopCountNotifEnabled_Type(TruthValue):
    """Custom type clMeshExcessiveHopCountNotifEnabled based on TruthValue"""


_ClMeshExcessiveHopCountNotifEnabled_Object = MibScalar
clMeshExcessiveHopCountNotifEnabled = _ClMeshExcessiveHopCountNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 9),
    _ClMeshExcessiveHopCountNotifEnabled_Type()
)
clMeshExcessiveHopCountNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveHopCountNotifEnabled.setStatus("current")


class _ClMeshExcessiveChildrenNotifEnabled_Type(TruthValue):
    """Custom type clMeshExcessiveChildrenNotifEnabled based on TruthValue"""


_ClMeshExcessiveChildrenNotifEnabled_Object = MibScalar
clMeshExcessiveChildrenNotifEnabled = _ClMeshExcessiveChildrenNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 10),
    _ClMeshExcessiveChildrenNotifEnabled_Type()
)
clMeshExcessiveChildrenNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshExcessiveChildrenNotifEnabled.setStatus("current")


class _ClMeshHighSNRNotifEnabled_Type(TruthValue):
    """Custom type clMeshHighSNRNotifEnabled based on TruthValue"""


_ClMeshHighSNRNotifEnabled_Object = MibScalar
clMeshHighSNRNotifEnabled = _ClMeshHighSNRNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 4, 11),
    _ClMeshHighSNRNotifEnabled_Type()
)
clMeshHighSNRNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshHighSNRNotifEnabled.setStatus("current")
_CiscoLwappMeshMIBNotifObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBNotifObjects = _CiscoLwappMeshMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5)
)
_ClMeshNodeMacAddress_Type = MacAddress
_ClMeshNodeMacAddress_Object = MibScalar
clMeshNodeMacAddress = _ClMeshNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 1),
    _ClMeshNodeMacAddress_Type()
)
clMeshNodeMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshNodeMacAddress.setStatus("current")


class _ClMeshAuthFailureReason_Type(Integer32):
    """Custom type clMeshAuthFailureReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInMacFilterList", 1),
          ("securityFailure", 2))
    )


_ClMeshAuthFailureReason_Type.__name__ = "Integer32"
_ClMeshAuthFailureReason_Object = MibScalar
clMeshAuthFailureReason = _ClMeshAuthFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 2),
    _ClMeshAuthFailureReason_Type()
)
clMeshAuthFailureReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshAuthFailureReason.setStatus("current")
_ClMeshPreviousParentMacAddress_Type = MacAddress
_ClMeshPreviousParentMacAddress_Object = MibScalar
clMeshPreviousParentMacAddress = _ClMeshPreviousParentMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 3),
    _ClMeshPreviousParentMacAddress_Type()
)
clMeshPreviousParentMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshPreviousParentMacAddress.setStatus("current")


class _ClMeshConsoleLoginStatus_Type(Integer32):
    """Custom type clMeshConsoleLoginStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failure", 2),
          ("success", 1))
    )


_ClMeshConsoleLoginStatus_Type.__name__ = "Integer32"
_ClMeshConsoleLoginStatus_Object = MibScalar
clMeshConsoleLoginStatus = _ClMeshConsoleLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 1, 5, 4),
    _ClMeshConsoleLoginStatus_Type()
)
clMeshConsoleLoginStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    clMeshConsoleLoginStatus.setStatus("current")
_CiscoLwappMeshMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBConform = _CiscoLwappMeshMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2)
)
_CiscoLwappMeshMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBCompliances = _CiscoLwappMeshMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1)
)
_CiscoLwappMeshMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMeshMIBGroups = _CiscoLwappMeshMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2)
)

# Managed Objects groups

ciscoLwappMeshConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 1)
)
ciscoLwappMeshConfigGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulDataRate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodePublicSafetyBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroup.setStatus("deprecated")

ciscoLwappMeshNeighborStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 2)
)
ciscoLwappMeshNeighborStatusGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborChannel"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNeighborUpdate"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNeighborStatusGroup.setStatus("current")

ciscoLwappMeshNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 3)
)
ciscoLwappMeshNotifControlGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshChildExcludedParentNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshParentChangeNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshChildMovedNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPoorSNRNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifControlGroup.setStatus("current")

ciscoLwappMeshNotifObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 4)
)
ciscoLwappMeshNotifObjsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureReason"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifObjsGroup.setStatus("current")

ciscoLwappMeshConfigGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 6)
)
ciscoLwappMeshConfigGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulDataRate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulRadio"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveRapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveMapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPublicSafetyBackhaulGlobal"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshisAMSDUEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsIdsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsDCAChannelsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsExtendedUAEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroupSup1.setStatus("deprecated")

ciscoLwappMeshNotifControlGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 7)
)
ciscoLwappMeshNotifControlGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshDefaultBridgeGroupNameNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountNotifEnabled"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveChildrenNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifControlGroupSup1.setStatus("current")

ciscoLwappMeshConfigGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 9)
)
ciscoLwappMeshConfigGroupSup2.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaul"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBHDataRate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetBridge"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeEthernetLinkStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHeaterStatus"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeInternalTemp"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeType"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeBackhaulRadio"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRange"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackhaulClientAccess"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMacFilterList"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshNodeAuthFailureThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildAssociationFailuresThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshMeshChildExcludedParentInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdAbate"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshHighSNRThresholdOnset"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshSNRCheckTimeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveParentChangeInterval"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshBackgroundScan"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthenticationMode"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveHopCountThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveRapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshExcessiveMapChildThreshold"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPublicSafetyBackhaulGlobal"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshisAMSDUEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsIdsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsDCAChannelsEnable"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshIsExtendedUAEnable"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConfigGroupSup2.setStatus("current")


# Notification objects

ciscoLwappMeshAuthFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 1)
)
ciscoLwappMeshAuthFailure.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshAuthFailureReason"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAuthFailure.setStatus(
        "current"
    )

ciscoLwappMeshChildExcludedParent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 2)
)
ciscoLwappMeshChildExcludedParent.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshChildExcludedParent.setStatus(
        "current"
    )

ciscoLwappMeshParentChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 3)
)
ciscoLwappMeshParentChange.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshPreviousParentMacAddress"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshParentChange.setStatus(
        "current"
    )

ciscoLwappMeshChildMoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 4)
)
ciscoLwappMeshChildMoved.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshChildMoved.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveParentChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 5)
)
ciscoLwappMeshExcessiveParentChange.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborType"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveParentChange.setStatus(
        "current"
    )

ciscoLwappMeshOnsetSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 6)
)
ciscoLwappMeshOnsetSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshOnsetSNR.setStatus(
        "current"
    )

ciscoLwappMeshAbateSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 7)
)
ciscoLwappMeshAbateSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAbateSNR.setStatus(
        "current"
    )

ciscoLwappMeshConsoleLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 8)
)
ciscoLwappMeshConsoleLogin.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNodeMacAddress"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshConsoleLoginStatus"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshConsoleLogin.setStatus(
        "current"
    )

ciscoLwappMeshDefaultBridgeGroupName = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 9)
)
ciscoLwappMeshDefaultBridgeGroupName.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeParentMacAddress"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshDefaultBridgeGroupName.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveHopCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 10)
)
ciscoLwappMeshExcessiveHopCount.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeHops"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveHopCount.setStatus(
        "current"
    )

ciscoLwappMeshExcessiveChildren = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 11)
)
ciscoLwappMeshExcessiveChildren.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeRole"),
        ("CISCO-LWAPP-MESH-MIB", "clMeshNodeChildCount"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshExcessiveChildren.setStatus(
        "current"
    )

ciscoLwappMeshOnsetHighSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 12)
)
ciscoLwappMeshOnsetHighSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshOnsetHighSNR.setStatus(
        "current"
    )

ciscoLwappMeshAbateHighSNR = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 0, 13)
)
ciscoLwappMeshAbateHighSNR.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "clMeshNeighborLinkSnr"),
        ("CISCO-LWAPP-AP-MIB", "cLApName"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshAbateHighSNR.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappMeshNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 5)
)
ciscoLwappMeshNotifsGroup.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAuthFailure"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshChildExcludedParent"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshParentChange"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshChildMoved"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveParentChange"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshOnsetSNR"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAbateSNR"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshConsoleLogin"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifsGroup.setStatus(
        "current"
    )

ciscoLwappMeshNotifsGroupSup1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 2, 8)
)
ciscoLwappMeshNotifsGroupSup1.setObjects(
      *(("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshDefaultBridgeGroupName"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveHopCount"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshExcessiveChildren"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshAbateHighSNR"),
        ("CISCO-LWAPP-MESH-MIB", "ciscoLwappMeshOnsetHighSNR"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshNotifsGroupSup1.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMeshMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMeshMIBComplianceR01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBComplianceR01.setStatus(
        "deprecated"
    )

ciscoLwappMeshMIBComplianceR02 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 616, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshMIBComplianceR02.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MESH-MIB",
    **{"ciscoLwappMeshMIB": ciscoLwappMeshMIB,
       "ciscoLwappMeshMIBNotifs": ciscoLwappMeshMIBNotifs,
       "ciscoLwappMeshAuthFailure": ciscoLwappMeshAuthFailure,
       "ciscoLwappMeshChildExcludedParent": ciscoLwappMeshChildExcludedParent,
       "ciscoLwappMeshParentChange": ciscoLwappMeshParentChange,
       "ciscoLwappMeshChildMoved": ciscoLwappMeshChildMoved,
       "ciscoLwappMeshExcessiveParentChange": ciscoLwappMeshExcessiveParentChange,
       "ciscoLwappMeshOnsetSNR": ciscoLwappMeshOnsetSNR,
       "ciscoLwappMeshAbateSNR": ciscoLwappMeshAbateSNR,
       "ciscoLwappMeshConsoleLogin": ciscoLwappMeshConsoleLogin,
       "ciscoLwappMeshDefaultBridgeGroupName": ciscoLwappMeshDefaultBridgeGroupName,
       "ciscoLwappMeshExcessiveHopCount": ciscoLwappMeshExcessiveHopCount,
       "ciscoLwappMeshExcessiveChildren": ciscoLwappMeshExcessiveChildren,
       "ciscoLwappMeshOnsetHighSNR": ciscoLwappMeshOnsetHighSNR,
       "ciscoLwappMeshAbateHighSNR": ciscoLwappMeshAbateHighSNR,
       "ciscoLwappMeshMIBObjects": ciscoLwappMeshMIBObjects,
       "ciscoLwappMeshConfig": ciscoLwappMeshConfig,
       "clMeshNodeTable": clMeshNodeTable,
       "clMeshNodeEntry": clMeshNodeEntry,
       "clMeshNodeRole": clMeshNodeRole,
       "clMeshNodeGroupName": clMeshNodeGroupName,
       "clMeshNodeBackhaul": clMeshNodeBackhaul,
       "clMeshNodeBackhaulDataRate": clMeshNodeBackhaulDataRate,
       "clMeshNodeEthernetBridge": clMeshNodeEthernetBridge,
       "clMeshNodeEthernetLinkStatus": clMeshNodeEthernetLinkStatus,
       "clMeshNodePublicSafetyBackhaul": clMeshNodePublicSafetyBackhaul,
       "clMeshNodeParentMacAddress": clMeshNodeParentMacAddress,
       "clMeshNodeHeaterStatus": clMeshNodeHeaterStatus,
       "clMeshNodeInternalTemp": clMeshNodeInternalTemp,
       "clMeshNodeType": clMeshNodeType,
       "clMeshNodeHops": clMeshNodeHops,
       "clMeshNodeChildCount": clMeshNodeChildCount,
       "clMeshNodeBackhaulRadio": clMeshNodeBackhaulRadio,
       "clMeshNodeBHDataRate": clMeshNodeBHDataRate,
       "ciscoLwappMeshGlobalConfig": ciscoLwappMeshGlobalConfig,
       "clMeshNodeRange": clMeshNodeRange,
       "clMeshBackhaulClientAccess": clMeshBackhaulClientAccess,
       "clMeshMacFilterList": clMeshMacFilterList,
       "clMeshMeshNodeAuthFailureThreshold": clMeshMeshNodeAuthFailureThreshold,
       "clMeshMeshChildAssociationFailuresThreshold": clMeshMeshChildAssociationFailuresThreshold,
       "clMeshMeshChildExcludedParentInterval": clMeshMeshChildExcludedParentInterval,
       "clMeshSNRThresholdAbate": clMeshSNRThresholdAbate,
       "clMeshSNRThresholdOnset": clMeshSNRThresholdOnset,
       "clMeshSNRCheckTimeInterval": clMeshSNRCheckTimeInterval,
       "clMeshExcessiveParentChangeThreshold": clMeshExcessiveParentChangeThreshold,
       "clMeshExcessiveParentChangeInterval": clMeshExcessiveParentChangeInterval,
       "clMeshBackgroundScan": clMeshBackgroundScan,
       "clMeshAuthenticationMode": clMeshAuthenticationMode,
       "clMeshExcessiveHopCountThreshold": clMeshExcessiveHopCountThreshold,
       "clMeshExcessiveRapChildThreshold": clMeshExcessiveRapChildThreshold,
       "clMeshExcessiveMapChildThreshold": clMeshExcessiveMapChildThreshold,
       "clMeshHighSNRThresholdAbate": clMeshHighSNRThresholdAbate,
       "clMeshHighSNRThresholdOnset": clMeshHighSNRThresholdOnset,
       "clMeshPublicSafetyBackhaulGlobal": clMeshPublicSafetyBackhaulGlobal,
       "clMeshisAMSDUEnable": clMeshisAMSDUEnable,
       "clMeshIsIdsEnable": clMeshIsIdsEnable,
       "clMeshIsDCAChannelsEnable": clMeshIsDCAChannelsEnable,
       "clMeshIsExtendedUAEnable": clMeshIsExtendedUAEnable,
       "ciscoLwappMeshNeighborsStatus": ciscoLwappMeshNeighborsStatus,
       "clMeshNeighborTable": clMeshNeighborTable,
       "clMeshNeighborEntry": clMeshNeighborEntry,
       "clMeshNeighborMacAddress": clMeshNeighborMacAddress,
       "clMeshNeighborType": clMeshNeighborType,
       "clMeshNeighborLinkSnr": clMeshNeighborLinkSnr,
       "clMeshNeighborChannel": clMeshNeighborChannel,
       "clMeshNeighborUpdate": clMeshNeighborUpdate,
       "ciscoLwappMeshNotifControlConfig": ciscoLwappMeshNotifControlConfig,
       "clMeshAuthFailureNotifEnabled": clMeshAuthFailureNotifEnabled,
       "clMeshChildExcludedParentNotifEnabled": clMeshChildExcludedParentNotifEnabled,
       "clMeshParentChangeNotifEnabled": clMeshParentChangeNotifEnabled,
       "clMeshChildMovedNotifEnabled": clMeshChildMovedNotifEnabled,
       "clMeshExcessiveParentChangeNotifEnabled": clMeshExcessiveParentChangeNotifEnabled,
       "clMeshPoorSNRNotifEnabled": clMeshPoorSNRNotifEnabled,
       "clMeshConsoleLoginNotifEnabled": clMeshConsoleLoginNotifEnabled,
       "clMeshDefaultBridgeGroupNameNotifEnabled": clMeshDefaultBridgeGroupNameNotifEnabled,
       "clMeshExcessiveHopCountNotifEnabled": clMeshExcessiveHopCountNotifEnabled,
       "clMeshExcessiveChildrenNotifEnabled": clMeshExcessiveChildrenNotifEnabled,
       "clMeshHighSNRNotifEnabled": clMeshHighSNRNotifEnabled,
       "ciscoLwappMeshMIBNotifObjects": ciscoLwappMeshMIBNotifObjects,
       "clMeshNodeMacAddress": clMeshNodeMacAddress,
       "clMeshAuthFailureReason": clMeshAuthFailureReason,
       "clMeshPreviousParentMacAddress": clMeshPreviousParentMacAddress,
       "clMeshConsoleLoginStatus": clMeshConsoleLoginStatus,
       "ciscoLwappMeshMIBConform": ciscoLwappMeshMIBConform,
       "ciscoLwappMeshMIBCompliances": ciscoLwappMeshMIBCompliances,
       "ciscoLwappMeshMIBCompliance": ciscoLwappMeshMIBCompliance,
       "ciscoLwappMeshMIBComplianceR01": ciscoLwappMeshMIBComplianceR01,
       "ciscoLwappMeshMIBComplianceR02": ciscoLwappMeshMIBComplianceR02,
       "ciscoLwappMeshMIBGroups": ciscoLwappMeshMIBGroups,
       "ciscoLwappMeshConfigGroup": ciscoLwappMeshConfigGroup,
       "ciscoLwappMeshNeighborStatusGroup": ciscoLwappMeshNeighborStatusGroup,
       "ciscoLwappMeshNotifControlGroup": ciscoLwappMeshNotifControlGroup,
       "ciscoLwappMeshNotifObjsGroup": ciscoLwappMeshNotifObjsGroup,
       "ciscoLwappMeshNotifsGroup": ciscoLwappMeshNotifsGroup,
       "ciscoLwappMeshConfigGroupSup1": ciscoLwappMeshConfigGroupSup1,
       "ciscoLwappMeshNotifControlGroupSup1": ciscoLwappMeshNotifControlGroupSup1,
       "ciscoLwappMeshNotifsGroupSup1": ciscoLwappMeshNotifsGroupSup1,
       "ciscoLwappMeshConfigGroupSup2": ciscoLwappMeshConfigGroupSup2}
)
