# SNMP MIB module (ZXR10-ETH-MGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZXR10-ETH-MGT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:52 2024
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

(zxr10interfaces,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10interfaces")


# MODULE-IDENTITY

zxr10EthMgtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2)
)
zxr10EthMgtMIB.setRevisions(
        ("2005-04-12 00:00",)
)


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



class InterfaceIndex(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class EthEncapsulationType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("encap-802dot1Q", 1)
    )



class IfSpeedType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("speed-1000mbps", 2),
          ("speed-100mbps", 3),
          ("speed-10mbps", 4),
          ("speed-auto", 0))
    )



class EthPhyFrameType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethernet-II", 1)
    )



class EthPhyWorkType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full-duplex", 1),
          ("half-duplex", 2))
    )



class EthNegotiationType(Integer32, TextualConvention):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("no-auto", 0))
    )



# MIB Managed Objects in the order of their OIDs

_Zxr10EthMgtMIBObjects_ObjectIdentity = ObjectIdentity
zxr10EthMgtMIBObjects = _Zxr10EthMgtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1)
)
_Zxr10EthQuery_ObjectIdentity = ObjectIdentity
zxr10EthQuery = _Zxr10EthQuery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1)
)
_Zxr10EthSubIfQueryTable_Object = MibTable
zxr10EthSubIfQueryTable = _Zxr10EthSubIfQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxr10EthSubIfQueryTable.setStatus("current")
_Zxr10EthSubIfQueryEntry_Object = MibTableRow
zxr10EthSubIfQueryEntry = _Zxr10EthSubIfQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1)
)
zxr10EthSubIfQueryEntry.setIndexNames(
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfParentIfIndex"),
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10EthSubIfQueryEntry.setStatus("current")
_Zxr10EthSubIfIndex_Type = InterfaceIndex
_Zxr10EthSubIfIndex_Object = MibTableColumn
zxr10EthSubIfIndex = _Zxr10EthSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 1),
    _Zxr10EthSubIfIndex_Type()
)
zxr10EthSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfIndex.setStatus("current")
_Zxr10EthSubIfParentIfIndex_Type = InterfaceIndex
_Zxr10EthSubIfParentIfIndex_Object = MibTableColumn
zxr10EthSubIfParentIfIndex = _Zxr10EthSubIfParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 2),
    _Zxr10EthSubIfParentIfIndex_Type()
)
zxr10EthSubIfParentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfParentIfIndex.setStatus("current")


class _Zxr10EthSubIfName_Type(DisplayString):
    """Custom type zxr10EthSubIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10EthSubIfName_Type.__name__ = "DisplayString"
_Zxr10EthSubIfName_Object = MibTableColumn
zxr10EthSubIfName = _Zxr10EthSubIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 3),
    _Zxr10EthSubIfName_Type()
)
zxr10EthSubIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfName.setStatus("current")


class _Zxr10EthSubIfParentIfName_Type(DisplayString):
    """Custom type zxr10EthSubIfParentIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10EthSubIfParentIfName_Type.__name__ = "DisplayString"
_Zxr10EthSubIfParentIfName_Object = MibTableColumn
zxr10EthSubIfParentIfName = _Zxr10EthSubIfParentIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 1, 1, 1, 4),
    _Zxr10EthSubIfParentIfName_Type()
)
zxr10EthSubIfParentIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfParentIfName.setStatus("current")
_Zxr10EthConfiguration_ObjectIdentity = ObjectIdentity
zxr10EthConfiguration = _Zxr10EthConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2)
)
_Zxr10EthSubIfConfigTable_Object = MibTable
zxr10EthSubIfConfigTable = _Zxr10EthSubIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigTable.setStatus("current")
_Zxr10EthSubIfConfigEntry_Object = MibTableRow
zxr10EthSubIfConfigEntry = _Zxr10EthSubIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1)
)
zxr10EthSubIfConfigEntry.setIndexNames(
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfConfigParentIfIndex"),
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthSubIfConfigSubIfName"),
)
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigEntry.setStatus("current")
_Zxr10EthSubIfConfigParentIfIndex_Type = Integer32
_Zxr10EthSubIfConfigParentIfIndex_Object = MibTableColumn
zxr10EthSubIfConfigParentIfIndex = _Zxr10EthSubIfConfigParentIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 1),
    _Zxr10EthSubIfConfigParentIfIndex_Type()
)
zxr10EthSubIfConfigParentIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigParentIfIndex.setStatus("current")


class _Zxr10EthSubIfConfigParentIfName_Type(DisplayString):
    """Custom type zxr10EthSubIfConfigParentIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10EthSubIfConfigParentIfName_Type.__name__ = "DisplayString"
_Zxr10EthSubIfConfigParentIfName_Object = MibTableColumn
zxr10EthSubIfConfigParentIfName = _Zxr10EthSubIfConfigParentIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 2),
    _Zxr10EthSubIfConfigParentIfName_Type()
)
zxr10EthSubIfConfigParentIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigParentIfName.setStatus("current")
_Zxr10EthSubIfConfigSubIfIndex_Type = Integer32
_Zxr10EthSubIfConfigSubIfIndex_Object = MibTableColumn
zxr10EthSubIfConfigSubIfIndex = _Zxr10EthSubIfConfigSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 3),
    _Zxr10EthSubIfConfigSubIfIndex_Type()
)
zxr10EthSubIfConfigSubIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigSubIfIndex.setStatus("current")


class _Zxr10EthSubIfConfigSubIfName_Type(DisplayString):
    """Custom type zxr10EthSubIfConfigSubIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10EthSubIfConfigSubIfName_Type.__name__ = "DisplayString"
_Zxr10EthSubIfConfigSubIfName_Object = MibTableColumn
zxr10EthSubIfConfigSubIfName = _Zxr10EthSubIfConfigSubIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 4),
    _Zxr10EthSubIfConfigSubIfName_Type()
)
zxr10EthSubIfConfigSubIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigSubIfName.setStatus("current")
_Zxr10EthSubIfConfigVlanID_Type = Integer32
_Zxr10EthSubIfConfigVlanID_Object = MibTableColumn
zxr10EthSubIfConfigVlanID = _Zxr10EthSubIfConfigVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 5),
    _Zxr10EthSubIfConfigVlanID_Type()
)
zxr10EthSubIfConfigVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigVlanID.setStatus("current")
_Zxr10EthSubIfConfigEncapType_Type = EthEncapsulationType
_Zxr10EthSubIfConfigEncapType_Object = MibTableColumn
zxr10EthSubIfConfigEncapType = _Zxr10EthSubIfConfigEncapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 6),
    _Zxr10EthSubIfConfigEncapType_Type()
)
zxr10EthSubIfConfigEncapType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigEncapType.setStatus("current")
_Zxr10EthSubIfConfigRowStatus_Type = RowStatus
_Zxr10EthSubIfConfigRowStatus_Object = MibTableColumn
zxr10EthSubIfConfigRowStatus = _Zxr10EthSubIfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 1, 1, 7),
    _Zxr10EthSubIfConfigRowStatus_Type()
)
zxr10EthSubIfConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthSubIfConfigRowStatus.setStatus("current")
_Zxr10EthPhyIfTable_Object = MibTable
zxr10EthPhyIfTable = _Zxr10EthPhyIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zxr10EthPhyIfTable.setStatus("current")
_Zxr10EthPhyIfEntry_Object = MibTableRow
zxr10EthPhyIfEntry = _Zxr10EthPhyIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1)
)
zxr10EthPhyIfEntry.setIndexNames(
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthPhyIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10EthPhyIfEntry.setStatus("current")
_Zxr10EthPhyIfIndex_Type = Integer32
_Zxr10EthPhyIfIndex_Object = MibTableColumn
zxr10EthPhyIfIndex = _Zxr10EthPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 1),
    _Zxr10EthPhyIfIndex_Type()
)
zxr10EthPhyIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthPhyIfIndex.setStatus("current")
_Zxr10EthPhyIfFrameType_Type = EthPhyFrameType
_Zxr10EthPhyIfFrameType_Object = MibTableColumn
zxr10EthPhyIfFrameType = _Zxr10EthPhyIfFrameType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 2),
    _Zxr10EthPhyIfFrameType_Type()
)
zxr10EthPhyIfFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthPhyIfFrameType.setStatus("current")
_Zxr10EthPhyIfNegotiation_Type = EthNegotiationType
_Zxr10EthPhyIfNegotiation_Object = MibTableColumn
zxr10EthPhyIfNegotiation = _Zxr10EthPhyIfNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 3),
    _Zxr10EthPhyIfNegotiation_Type()
)
zxr10EthPhyIfNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthPhyIfNegotiation.setStatus("current")
_Zxr10EthPhyWorkType_Type = EthPhyWorkType
_Zxr10EthPhyWorkType_Object = MibTableColumn
zxr10EthPhyWorkType = _Zxr10EthPhyWorkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 4),
    _Zxr10EthPhyWorkType_Type()
)
zxr10EthPhyWorkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthPhyWorkType.setStatus("current")
_Zxr10EthPhyIfSpeed_Type = IfSpeedType
_Zxr10EthPhyIfSpeed_Object = MibTableColumn
zxr10EthPhyIfSpeed = _Zxr10EthPhyIfSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 5),
    _Zxr10EthPhyIfSpeed_Type()
)
zxr10EthPhyIfSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthPhyIfSpeed.setStatus("current")
_Zxr10EthPhyIfMTU_Type = Integer32
_Zxr10EthPhyIfMTU_Object = MibTableColumn
zxr10EthPhyIfMTU = _Zxr10EthPhyIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 3, 1, 6),
    _Zxr10EthPhyIfMTU_Type()
)
zxr10EthPhyIfMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthPhyIfMTU.setStatus("current")
_Zxr10EthLoopBackTable_Object = MibTable
zxr10EthLoopBackTable = _Zxr10EthLoopBackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zxr10EthLoopBackTable.setStatus("current")
_Zxr10EthLoopBackEntry_Object = MibTableRow
zxr10EthLoopBackEntry = _Zxr10EthLoopBackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1)
)
zxr10EthLoopBackEntry.setIndexNames(
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthLoopBackNo"),
)
if mibBuilder.loadTexts:
    zxr10EthLoopBackEntry.setStatus("current")
_Zxr10EthLoopBackIfIndex_Type = InterfaceIndex
_Zxr10EthLoopBackIfIndex_Object = MibTableColumn
zxr10EthLoopBackIfIndex = _Zxr10EthLoopBackIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 1),
    _Zxr10EthLoopBackIfIndex_Type()
)
zxr10EthLoopBackIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthLoopBackIfIndex.setStatus("current")


class _Zxr10EthLoopBackIfName_Type(DisplayString):
    """Custom type zxr10EthLoopBackIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Zxr10EthLoopBackIfName_Type.__name__ = "DisplayString"
_Zxr10EthLoopBackIfName_Object = MibTableColumn
zxr10EthLoopBackIfName = _Zxr10EthLoopBackIfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 2),
    _Zxr10EthLoopBackIfName_Type()
)
zxr10EthLoopBackIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthLoopBackIfName.setStatus("current")


class _Zxr10EthLoopBackNo_Type(Integer32):
    """Custom type zxr10EthLoopBackNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Zxr10EthLoopBackNo_Type.__name__ = "Integer32"
_Zxr10EthLoopBackNo_Object = MibTableColumn
zxr10EthLoopBackNo = _Zxr10EthLoopBackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 3),
    _Zxr10EthLoopBackNo_Type()
)
zxr10EthLoopBackNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthLoopBackNo.setStatus("current")
_Zxr10EthLoopBackRowStatus_Type = RowStatus
_Zxr10EthLoopBackRowStatus_Object = MibTableColumn
zxr10EthLoopBackRowStatus = _Zxr10EthLoopBackRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 2, 4, 1, 4),
    _Zxr10EthLoopBackRowStatus_Type()
)
zxr10EthLoopBackRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthLoopBackRowStatus.setStatus("current")
_Zxr10EthStats_ObjectIdentity = ObjectIdentity
zxr10EthStats = _Zxr10EthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3)
)
_Zxr10EthRecvStatsTable_Object = MibTable
zxr10EthRecvStatsTable = _Zxr10EthRecvStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxr10EthRecvStatsTable.setStatus("current")
_Zxr10EthRecvStatsEntry_Object = MibTableRow
zxr10EthRecvStatsEntry = _Zxr10EthRecvStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1)
)
zxr10EthRecvStatsEntry.setIndexNames(
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthPhyIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10EthRecvStatsEntry.setStatus("current")
_Zxr10EthRecvStatsIfIndex_Type = Integer32
_Zxr10EthRecvStatsIfIndex_Object = MibTableColumn
zxr10EthRecvStatsIfIndex = _Zxr10EthRecvStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 1),
    _Zxr10EthRecvStatsIfIndex_Type()
)
zxr10EthRecvStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvStatsIfIndex.setStatus("current")
_Zxr10EthRecvPktsUnder64Octects_Type = Counter64
_Zxr10EthRecvPktsUnder64Octects_Object = MibTableColumn
zxr10EthRecvPktsUnder64Octects = _Zxr10EthRecvPktsUnder64Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 2),
    _Zxr10EthRecvPktsUnder64Octects_Type()
)
zxr10EthRecvPktsUnder64Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPktsUnder64Octects.setStatus("current")
_Zxr10EthRecvPkts64Octects_Type = Counter64
_Zxr10EthRecvPkts64Octects_Object = MibTableColumn
zxr10EthRecvPkts64Octects = _Zxr10EthRecvPkts64Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 3),
    _Zxr10EthRecvPkts64Octects_Type()
)
zxr10EthRecvPkts64Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPkts64Octects.setStatus("current")
_Zxr10EthRecvPkts65to127Octects_Type = Counter64
_Zxr10EthRecvPkts65to127Octects_Object = MibTableColumn
zxr10EthRecvPkts65to127Octects = _Zxr10EthRecvPkts65to127Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 4),
    _Zxr10EthRecvPkts65to127Octects_Type()
)
zxr10EthRecvPkts65to127Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPkts65to127Octects.setStatus("current")
_Zxr10EthRecvPkts128to255Octects_Type = Counter64
_Zxr10EthRecvPkts128to255Octects_Object = MibTableColumn
zxr10EthRecvPkts128to255Octects = _Zxr10EthRecvPkts128to255Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 5),
    _Zxr10EthRecvPkts128to255Octects_Type()
)
zxr10EthRecvPkts128to255Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPkts128to255Octects.setStatus("current")
_Zxr10EthRecvPkts255to511Octects_Type = Counter64
_Zxr10EthRecvPkts255to511Octects_Object = MibTableColumn
zxr10EthRecvPkts255to511Octects = _Zxr10EthRecvPkts255to511Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 6),
    _Zxr10EthRecvPkts255to511Octects_Type()
)
zxr10EthRecvPkts255to511Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPkts255to511Octects.setStatus("current")
_Zxr10EthRecvPkts512to1023Octects_Type = Counter64
_Zxr10EthRecvPkts512to1023Octects_Object = MibTableColumn
zxr10EthRecvPkts512to1023Octects = _Zxr10EthRecvPkts512to1023Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 7),
    _Zxr10EthRecvPkts512to1023Octects_Type()
)
zxr10EthRecvPkts512to1023Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPkts512to1023Octects.setStatus("current")
_Zxr10EthRecvPkts1024to1518Octects_Type = Counter64
_Zxr10EthRecvPkts1024to1518Octects_Object = MibTableColumn
zxr10EthRecvPkts1024to1518Octects = _Zxr10EthRecvPkts1024to1518Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 8),
    _Zxr10EthRecvPkts1024to1518Octects_Type()
)
zxr10EthRecvPkts1024to1518Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPkts1024to1518Octects.setStatus("current")
_Zxr10EthRecvPktsOverSize_Type = Counter64
_Zxr10EthRecvPktsOverSize_Object = MibTableColumn
zxr10EthRecvPktsOverSize = _Zxr10EthRecvPktsOverSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 9),
    _Zxr10EthRecvPktsOverSize_Type()
)
zxr10EthRecvPktsOverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPktsOverSize.setStatus("current")
_Zxr10EthRecvPktsCRCError_Type = Counter64
_Zxr10EthRecvPktsCRCError_Object = MibTableColumn
zxr10EthRecvPktsCRCError = _Zxr10EthRecvPktsCRCError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 10),
    _Zxr10EthRecvPktsCRCError_Type()
)
zxr10EthRecvPktsCRCError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthRecvPktsCRCError.setStatus("current")


class _Zxr10EthRecvClearCounts_Type(Integer32):
    """Custom type zxr10EthRecvClearCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Zxr10EthRecvClearCounts_Type.__name__ = "Integer32"
_Zxr10EthRecvClearCounts_Object = MibTableColumn
zxr10EthRecvClearCounts = _Zxr10EthRecvClearCounts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 1, 1, 11),
    _Zxr10EthRecvClearCounts_Type()
)
zxr10EthRecvClearCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthRecvClearCounts.setStatus("current")
_Zxr10EthSndStatsTable_Object = MibTable
zxr10EthSndStatsTable = _Zxr10EthSndStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxr10EthSndStatsTable.setStatus("current")
_Zxr10EthSndStatsEntry_Object = MibTableRow
zxr10EthSndStatsEntry = _Zxr10EthSndStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1)
)
zxr10EthSndStatsEntry.setIndexNames(
    (0, "ZXR10-ETH-MGT-MIB", "zxr10EthPhyIfIndex"),
)
if mibBuilder.loadTexts:
    zxr10EthSndStatsEntry.setStatus("current")
_Zxr10EthSndStatsIfIndex_Type = Integer32
_Zxr10EthSndStatsIfIndex_Object = MibTableColumn
zxr10EthSndStatsIfIndex = _Zxr10EthSndStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 1),
    _Zxr10EthSndStatsIfIndex_Type()
)
zxr10EthSndStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndStatsIfIndex.setStatus("current")
_Zxr10EthSndPktsUnder64Octects_Type = Counter64
_Zxr10EthSndPktsUnder64Octects_Object = MibTableColumn
zxr10EthSndPktsUnder64Octects = _Zxr10EthSndPktsUnder64Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 2),
    _Zxr10EthSndPktsUnder64Octects_Type()
)
zxr10EthSndPktsUnder64Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPktsUnder64Octects.setStatus("current")
_Zxr10EthSndPkts64Octects_Type = Counter64
_Zxr10EthSndPkts64Octects_Object = MibTableColumn
zxr10EthSndPkts64Octects = _Zxr10EthSndPkts64Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 3),
    _Zxr10EthSndPkts64Octects_Type()
)
zxr10EthSndPkts64Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPkts64Octects.setStatus("current")
_Zxr10EthSndPkts65to127Octects_Type = Counter64
_Zxr10EthSndPkts65to127Octects_Object = MibTableColumn
zxr10EthSndPkts65to127Octects = _Zxr10EthSndPkts65to127Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 4),
    _Zxr10EthSndPkts65to127Octects_Type()
)
zxr10EthSndPkts65to127Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPkts65to127Octects.setStatus("current")
_Zxr10EthSndPkts128to255Octects_Type = Counter64
_Zxr10EthSndPkts128to255Octects_Object = MibTableColumn
zxr10EthSndPkts128to255Octects = _Zxr10EthSndPkts128to255Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 5),
    _Zxr10EthSndPkts128to255Octects_Type()
)
zxr10EthSndPkts128to255Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPkts128to255Octects.setStatus("current")
_Zxr10EthSndPkts255to511Octects_Type = Counter64
_Zxr10EthSndPkts255to511Octects_Object = MibTableColumn
zxr10EthSndPkts255to511Octects = _Zxr10EthSndPkts255to511Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 6),
    _Zxr10EthSndPkts255to511Octects_Type()
)
zxr10EthSndPkts255to511Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPkts255to511Octects.setStatus("current")
_Zxr10EthSndPkts512to1023Octects_Type = Counter64
_Zxr10EthSndPkts512to1023Octects_Object = MibTableColumn
zxr10EthSndPkts512to1023Octects = _Zxr10EthSndPkts512to1023Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 7),
    _Zxr10EthSndPkts512to1023Octects_Type()
)
zxr10EthSndPkts512to1023Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPkts512to1023Octects.setStatus("current")
_Zxr10EthSndPkts1024to1518Octects_Type = Counter64
_Zxr10EthSndPkts1024to1518Octects_Object = MibTableColumn
zxr10EthSndPkts1024to1518Octects = _Zxr10EthSndPkts1024to1518Octects_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 8),
    _Zxr10EthSndPkts1024to1518Octects_Type()
)
zxr10EthSndPkts1024to1518Octects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPkts1024to1518Octects.setStatus("current")
_Zxr10EthSndPktsOverSize_Type = Counter64
_Zxr10EthSndPktsOverSize_Object = MibTableColumn
zxr10EthSndPktsOverSize = _Zxr10EthSndPktsOverSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 9),
    _Zxr10EthSndPktsOverSize_Type()
)
zxr10EthSndPktsOverSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10EthSndPktsOverSize.setStatus("current")


class _Zxr10EthSndClearCounts_Type(Integer32):
    """Custom type zxr10EthSndClearCounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_Zxr10EthSndClearCounts_Type.__name__ = "Integer32"
_Zxr10EthSndClearCounts_Object = MibTableColumn
zxr10EthSndClearCounts = _Zxr10EthSndClearCounts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 103, 2, 1, 3, 2, 1, 10),
    _Zxr10EthSndClearCounts_Type()
)
zxr10EthSndClearCounts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxr10EthSndClearCounts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXR10-ETH-MGT-MIB",
    **{"DisplayString": DisplayString,
       "InterfaceIndex": InterfaceIndex,
       "EthEncapsulationType": EthEncapsulationType,
       "IfSpeedType": IfSpeedType,
       "EthPhyFrameType": EthPhyFrameType,
       "EthPhyWorkType": EthPhyWorkType,
       "EthNegotiationType": EthNegotiationType,
       "zxr10EthMgtMIB": zxr10EthMgtMIB,
       "zxr10EthMgtMIBObjects": zxr10EthMgtMIBObjects,
       "zxr10EthQuery": zxr10EthQuery,
       "zxr10EthSubIfQueryTable": zxr10EthSubIfQueryTable,
       "zxr10EthSubIfQueryEntry": zxr10EthSubIfQueryEntry,
       "zxr10EthSubIfIndex": zxr10EthSubIfIndex,
       "zxr10EthSubIfParentIfIndex": zxr10EthSubIfParentIfIndex,
       "zxr10EthSubIfName": zxr10EthSubIfName,
       "zxr10EthSubIfParentIfName": zxr10EthSubIfParentIfName,
       "zxr10EthConfiguration": zxr10EthConfiguration,
       "zxr10EthSubIfConfigTable": zxr10EthSubIfConfigTable,
       "zxr10EthSubIfConfigEntry": zxr10EthSubIfConfigEntry,
       "zxr10EthSubIfConfigParentIfIndex": zxr10EthSubIfConfigParentIfIndex,
       "zxr10EthSubIfConfigParentIfName": zxr10EthSubIfConfigParentIfName,
       "zxr10EthSubIfConfigSubIfIndex": zxr10EthSubIfConfigSubIfIndex,
       "zxr10EthSubIfConfigSubIfName": zxr10EthSubIfConfigSubIfName,
       "zxr10EthSubIfConfigVlanID": zxr10EthSubIfConfigVlanID,
       "zxr10EthSubIfConfigEncapType": zxr10EthSubIfConfigEncapType,
       "zxr10EthSubIfConfigRowStatus": zxr10EthSubIfConfigRowStatus,
       "zxr10EthPhyIfTable": zxr10EthPhyIfTable,
       "zxr10EthPhyIfEntry": zxr10EthPhyIfEntry,
       "zxr10EthPhyIfIndex": zxr10EthPhyIfIndex,
       "zxr10EthPhyIfFrameType": zxr10EthPhyIfFrameType,
       "zxr10EthPhyIfNegotiation": zxr10EthPhyIfNegotiation,
       "zxr10EthPhyWorkType": zxr10EthPhyWorkType,
       "zxr10EthPhyIfSpeed": zxr10EthPhyIfSpeed,
       "zxr10EthPhyIfMTU": zxr10EthPhyIfMTU,
       "zxr10EthLoopBackTable": zxr10EthLoopBackTable,
       "zxr10EthLoopBackEntry": zxr10EthLoopBackEntry,
       "zxr10EthLoopBackIfIndex": zxr10EthLoopBackIfIndex,
       "zxr10EthLoopBackIfName": zxr10EthLoopBackIfName,
       "zxr10EthLoopBackNo": zxr10EthLoopBackNo,
       "zxr10EthLoopBackRowStatus": zxr10EthLoopBackRowStatus,
       "zxr10EthStats": zxr10EthStats,
       "zxr10EthRecvStatsTable": zxr10EthRecvStatsTable,
       "zxr10EthRecvStatsEntry": zxr10EthRecvStatsEntry,
       "zxr10EthRecvStatsIfIndex": zxr10EthRecvStatsIfIndex,
       "zxr10EthRecvPktsUnder64Octects": zxr10EthRecvPktsUnder64Octects,
       "zxr10EthRecvPkts64Octects": zxr10EthRecvPkts64Octects,
       "zxr10EthRecvPkts65to127Octects": zxr10EthRecvPkts65to127Octects,
       "zxr10EthRecvPkts128to255Octects": zxr10EthRecvPkts128to255Octects,
       "zxr10EthRecvPkts255to511Octects": zxr10EthRecvPkts255to511Octects,
       "zxr10EthRecvPkts512to1023Octects": zxr10EthRecvPkts512to1023Octects,
       "zxr10EthRecvPkts1024to1518Octects": zxr10EthRecvPkts1024to1518Octects,
       "zxr10EthRecvPktsOverSize": zxr10EthRecvPktsOverSize,
       "zxr10EthRecvPktsCRCError": zxr10EthRecvPktsCRCError,
       "zxr10EthRecvClearCounts": zxr10EthRecvClearCounts,
       "zxr10EthSndStatsTable": zxr10EthSndStatsTable,
       "zxr10EthSndStatsEntry": zxr10EthSndStatsEntry,
       "zxr10EthSndStatsIfIndex": zxr10EthSndStatsIfIndex,
       "zxr10EthSndPktsUnder64Octects": zxr10EthSndPktsUnder64Octects,
       "zxr10EthSndPkts64Octects": zxr10EthSndPkts64Octects,
       "zxr10EthSndPkts65to127Octects": zxr10EthSndPkts65to127Octects,
       "zxr10EthSndPkts128to255Octects": zxr10EthSndPkts128to255Octects,
       "zxr10EthSndPkts255to511Octects": zxr10EthSndPkts255to511Octects,
       "zxr10EthSndPkts512to1023Octects": zxr10EthSndPkts512to1023Octects,
       "zxr10EthSndPkts1024to1518Octects": zxr10EthSndPkts1024to1518Octects,
       "zxr10EthSndPktsOverSize": zxr10EthSndPktsOverSize,
       "zxr10EthSndClearCounts": zxr10EthSndClearCounts}
)
