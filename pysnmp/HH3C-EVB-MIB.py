# SNMP MIB module (HH3C-EVB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-EVB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:12 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

(IEEE8021BridgePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hh3cEvb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134)
)
hh3cEvb.setRevisions(
        ("2012-12-21 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3cEvbSysObjects_ObjectIdentity = ObjectIdentity
hh3cEvbSysObjects = _Hh3cEvbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1)
)


class _Hh3cEvbSetResult_Type(Integer32):
    """Custom type hh3cEvbSetResult based on Integer32"""
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
        *(("failed", 4),
          ("processing", 2),
          ("success", 3),
          ("unknown", 1))
    )


_Hh3cEvbSetResult_Type.__name__ = "Integer32"
_Hh3cEvbSetResult_Object = MibScalar
hh3cEvbSetResult = _Hh3cEvbSetResult_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 1),
    _Hh3cEvbSetResult_Type()
)
hh3cEvbSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvbSetResult.setStatus("current")
_Hh3cEvbDefaultManagerTable_Object = MibTable
hh3cEvbDefaultManagerTable = _Hh3cEvbDefaultManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cEvbDefaultManagerTable.setStatus("current")
_Hh3cEvbDefaultManagerEntry_Object = MibTableRow
hh3cEvbDefaultManagerEntry = _Hh3cEvbDefaultManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1)
)
hh3cEvbDefaultManagerEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cEvbManagerIndex"),
)
if mibBuilder.loadTexts:
    hh3cEvbDefaultManagerEntry.setStatus("current")
_Hh3cEvbManagerIndex_Type = Unsigned32
_Hh3cEvbManagerIndex_Object = MibTableColumn
hh3cEvbManagerIndex = _Hh3cEvbManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 1),
    _Hh3cEvbManagerIndex_Type()
)
hh3cEvbManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbManagerIndex.setStatus("current")


class _Hh3cEvbManagerType_Type(Integer32):
    """Custom type hh3cEvbManagerType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("local", 4),
          ("name", 3))
    )


_Hh3cEvbManagerType_Type.__name__ = "Integer32"
_Hh3cEvbManagerType_Object = MibTableColumn
hh3cEvbManagerType = _Hh3cEvbManagerType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 2),
    _Hh3cEvbManagerType_Type()
)
hh3cEvbManagerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbManagerType.setStatus("current")


class _Hh3cEvbManagerID_Type(OctetString):
    """Custom type hh3cEvbManagerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Hh3cEvbManagerID_Type.__name__ = "OctetString"
_Hh3cEvbManagerID_Object = MibTableColumn
hh3cEvbManagerID = _Hh3cEvbManagerID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 3),
    _Hh3cEvbManagerID_Type()
)
hh3cEvbManagerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbManagerID.setStatus("current")


class _Hh3cEvbManagerPort_Type(Unsigned32):
    """Custom type hh3cEvbManagerPort based on Unsigned32"""
    defaultValue = 8080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cEvbManagerPort_Type.__name__ = "Unsigned32"
_Hh3cEvbManagerPort_Object = MibTableColumn
hh3cEvbManagerPort = _Hh3cEvbManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 4),
    _Hh3cEvbManagerPort_Type()
)
hh3cEvbManagerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbManagerPort.setStatus("current")
_Hh3cEvbManagerRowStatus_Type = RowStatus
_Hh3cEvbManagerRowStatus_Object = MibTableColumn
hh3cEvbManagerRowStatus = _Hh3cEvbManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 1, 2, 1, 5),
    _Hh3cEvbManagerRowStatus_Type()
)
hh3cEvbManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbManagerRowStatus.setStatus("current")
_Hh3cEvbPortObjects_ObjectIdentity = ObjectIdentity
hh3cEvbPortObjects = _Hh3cEvbPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2)
)
_Hh3cEvbPortConfigTable_Object = MibTable
hh3cEvbPortConfigTable = _Hh3cEvbPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cEvbPortConfigTable.setStatus("current")
_Hh3cEvbPortConfigEntry_Object = MibTableRow
hh3cEvbPortConfigEntry = _Hh3cEvbPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1)
)
hh3cEvbPortConfigEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cEvbPortNumber"),
)
if mibBuilder.loadTexts:
    hh3cEvbPortConfigEntry.setStatus("current")
_Hh3cEvbPortNumber_Type = IEEE8021BridgePortNumber
_Hh3cEvbPortNumber_Object = MibTableColumn
hh3cEvbPortNumber = _Hh3cEvbPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1, 1),
    _Hh3cEvbPortNumber_Type()
)
hh3cEvbPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbPortNumber.setStatus("current")


class _Hh3cEvbRWD_Type(Unsigned32):
    """Custom type hh3cEvbRWD based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 31),
    )


_Hh3cEvbRWD_Type.__name__ = "Unsigned32"
_Hh3cEvbRWD_Object = MibTableColumn
hh3cEvbRWD = _Hh3cEvbRWD_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1, 2),
    _Hh3cEvbRWD_Type()
)
hh3cEvbRWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvbRWD.setStatus("current")


class _Hh3cEvbRKA_Type(Unsigned32):
    """Custom type hh3cEvbRKA based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 31),
    )


_Hh3cEvbRKA_Type.__name__ = "Unsigned32"
_Hh3cEvbRKA_Object = MibTableColumn
hh3cEvbRKA = _Hh3cEvbRKA_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 1, 1, 3),
    _Hh3cEvbRKA_Type()
)
hh3cEvbRKA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvbRKA.setStatus("current")
_Hh3cEvbSchannelConfigTable_Object = MibTable
hh3cEvbSchannelConfigTable = _Hh3cEvbSchannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2)
)
if mibBuilder.loadTexts:
    hh3cEvbSchannelConfigTable.setStatus("current")
_Hh3cEvbSchannelConfigEntry_Object = MibTableRow
hh3cEvbSchannelConfigEntry = _Hh3cEvbSchannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1)
)
hh3cEvbSchannelConfigEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cEvbPortNumber"),
    (0, "HH3C-EVB-MIB", "hh3cEvbSchannelID"),
)
if mibBuilder.loadTexts:
    hh3cEvbSchannelConfigEntry.setStatus("current")
_Hh3cEvbSchannelID_Type = Unsigned32
_Hh3cEvbSchannelID_Object = MibTableColumn
hh3cEvbSchannelID = _Hh3cEvbSchannelID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 1),
    _Hh3cEvbSchannelID_Type()
)
hh3cEvbSchannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbSchannelID.setStatus("current")


class _Hh3cEvbSchannelSVLAN_Type(Unsigned32):
    """Custom type hh3cEvbSchannelSVLAN based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Hh3cEvbSchannelSVLAN_Type.__name__ = "Unsigned32"
_Hh3cEvbSchannelSVLAN_Object = MibTableColumn
hh3cEvbSchannelSVLAN = _Hh3cEvbSchannelSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 2),
    _Hh3cEvbSchannelSVLAN_Type()
)
hh3cEvbSchannelSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbSchannelSVLAN.setStatus("current")


class _Hh3cEvbMacLearningStatus_Type(TruthValue):
    """Custom type hh3cEvbMacLearningStatus based on TruthValue"""


_Hh3cEvbMacLearningStatus_Object = MibTableColumn
hh3cEvbMacLearningStatus = _Hh3cEvbMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 3),
    _Hh3cEvbMacLearningStatus_Type()
)
hh3cEvbMacLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvbMacLearningStatus.setStatus("current")


class _Hh3cEvbRRStatus_Type(TruthValue):
    """Custom type hh3cEvbRRStatus based on TruthValue"""


_Hh3cEvbRRStatus_Object = MibTableColumn
hh3cEvbRRStatus = _Hh3cEvbRRStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 4),
    _Hh3cEvbRRStatus_Type()
)
hh3cEvbRRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvbRRStatus.setStatus("current")
_Hh3cEvbSchannelRowStatus_Type = RowStatus
_Hh3cEvbSchannelRowStatus_Object = MibTableColumn
hh3cEvbSchannelRowStatus = _Hh3cEvbSchannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 2, 1, 5),
    _Hh3cEvbSchannelRowStatus_Type()
)
hh3cEvbSchannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbSchannelRowStatus.setStatus("current")
_Hh3cEvbVSIConfigTable_Object = MibTable
hh3cEvbVSIConfigTable = _Hh3cEvbVSIConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3)
)
if mibBuilder.loadTexts:
    hh3cEvbVSIConfigTable.setStatus("current")
_Hh3cEvbVSIConfigEntry_Object = MibTableRow
hh3cEvbVSIConfigEntry = _Hh3cEvbVSIConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1)
)
hh3cEvbVSIConfigEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cEvbSBPPortNumber"),
    (0, "HH3C-EVB-MIB", "hh3cEvbVSILocalID"),
)
if mibBuilder.loadTexts:
    hh3cEvbVSIConfigEntry.setStatus("current")
_Hh3cEvbSBPPortNumber_Type = IEEE8021BridgePortNumber
_Hh3cEvbSBPPortNumber_Object = MibTableColumn
hh3cEvbSBPPortNumber = _Hh3cEvbSBPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 1),
    _Hh3cEvbSBPPortNumber_Type()
)
hh3cEvbSBPPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbSBPPortNumber.setStatus("current")
_Hh3cEvbVSILocalID_Type = Unsigned32
_Hh3cEvbVSILocalID_Object = MibTableColumn
hh3cEvbVSILocalID = _Hh3cEvbVSILocalID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 2),
    _Hh3cEvbVSILocalID_Type()
)
hh3cEvbVSILocalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbVSILocalID.setStatus("current")


class _Hh3cEvbVSICommand_Type(Integer32):
    """Custom type hh3cEvbVSICommand based on Integer32"""
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
        *(("associate", 3),
          ("deAssociate", 4),
          ("preAssociate", 1),
          ("preAssociateWithRsrcReservation", 2))
    )


_Hh3cEvbVSICommand_Type.__name__ = "Integer32"
_Hh3cEvbVSICommand_Object = MibTableColumn
hh3cEvbVSICommand = _Hh3cEvbVSICommand_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 3),
    _Hh3cEvbVSICommand_Type()
)
hh3cEvbVSICommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbVSICommand.setStatus("current")
_Hh3cEvbVSIIfIndex_Type = InterfaceIndexOrZero
_Hh3cEvbVSIIfIndex_Object = MibTableColumn
hh3cEvbVSIIfIndex = _Hh3cEvbVSIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 4),
    _Hh3cEvbVSIIfIndex_Type()
)
hh3cEvbVSIIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cEvbVSIIfIndex.setStatus("current")


class _Hh3cEvbVSIIsActive_Type(TruthValue):
    """Custom type hh3cEvbVSIIsActive based on TruthValue"""


_Hh3cEvbVSIIsActive_Object = MibTableColumn
hh3cEvbVSIIsActive = _Hh3cEvbVSIIsActive_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 5),
    _Hh3cEvbVSIIsActive_Type()
)
hh3cEvbVSIIsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cEvbVSIIsActive.setStatus("current")
_Hh3cEvbVSIRowStatus_Type = RowStatus
_Hh3cEvbVSIRowStatus_Object = MibTableColumn
hh3cEvbVSIRowStatus = _Hh3cEvbVSIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 3, 1, 6),
    _Hh3cEvbVSIRowStatus_Type()
)
hh3cEvbVSIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbVSIRowStatus.setStatus("current")
_Hh3cEvbVSIFilterConfigTable_Object = MibTable
hh3cEvbVSIFilterConfigTable = _Hh3cEvbVSIFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4)
)
if mibBuilder.loadTexts:
    hh3cEvbVSIFilterConfigTable.setStatus("current")
_Hh3cEvbVSIFilterConfigEntry_Object = MibTableRow
hh3cEvbVSIFilterConfigEntry = _Hh3cEvbVSIFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1)
)
hh3cEvbVSIFilterConfigEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cEvbSBPPortNumber"),
    (0, "HH3C-EVB-MIB", "hh3cEvbVSILocalID"),
    (0, "HH3C-EVB-MIB", "hh3cEvbGroupID"),
    (0, "HH3C-EVB-MIB", "hh3cEvbVSIMac"),
    (0, "HH3C-EVB-MIB", "hh3cEvbVSIVlanId"),
)
if mibBuilder.loadTexts:
    hh3cEvbVSIFilterConfigEntry.setStatus("current")
_Hh3cEvbGroupID_Type = Unsigned32
_Hh3cEvbGroupID_Object = MibTableColumn
hh3cEvbGroupID = _Hh3cEvbGroupID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 1),
    _Hh3cEvbGroupID_Type()
)
hh3cEvbGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbGroupID.setStatus("current")
_Hh3cEvbVSIMac_Type = MacAddress
_Hh3cEvbVSIMac_Object = MibTableColumn
hh3cEvbVSIMac = _Hh3cEvbVSIMac_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 2),
    _Hh3cEvbVSIMac_Type()
)
hh3cEvbVSIMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbVSIMac.setStatus("current")
_Hh3cEvbVSIVlanId_Type = VlanIndex
_Hh3cEvbVSIVlanId_Object = MibTableColumn
hh3cEvbVSIVlanId = _Hh3cEvbVSIVlanId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 3),
    _Hh3cEvbVSIVlanId_Type()
)
hh3cEvbVSIVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cEvbVSIVlanId.setStatus("current")
_Hh3cEvbVSIFilterRowStatus_Type = RowStatus
_Hh3cEvbVSIFilterRowStatus_Object = MibTableColumn
hh3cEvbVSIFilterRowStatus = _Hh3cEvbVSIFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 2, 4, 1, 4),
    _Hh3cEvbVSIFilterRowStatus_Type()
)
hh3cEvbVSIFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cEvbVSIFilterRowStatus.setStatus("current")
_Hh3cFlex10Objects_ObjectIdentity = ObjectIdentity
hh3cFlex10Objects = _Hh3cFlex10Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3)
)
_Hh3cFlex10PortConfigTable_Object = MibTable
hh3cFlex10PortConfigTable = _Hh3cFlex10PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1)
)
if mibBuilder.loadTexts:
    hh3cFlex10PortConfigTable.setStatus("current")
_Hh3cFlex10PortConfigEntry_Object = MibTableRow
hh3cFlex10PortConfigEntry = _Hh3cFlex10PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1, 1)
)
hh3cFlex10PortConfigEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cFlex10PortNumber"),
)
if mibBuilder.loadTexts:
    hh3cFlex10PortConfigEntry.setStatus("current")
_Hh3cFlex10PortNumber_Type = IEEE8021BridgePortNumber
_Hh3cFlex10PortNumber_Object = MibTableColumn
hh3cFlex10PortNumber = _Hh3cFlex10PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1, 1, 1),
    _Hh3cFlex10PortNumber_Type()
)
hh3cFlex10PortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFlex10PortNumber.setStatus("current")


class _Hh3cFlex10PortEnableStatus_Type(TruthValue):
    """Custom type hh3cFlex10PortEnableStatus based on TruthValue"""


_Hh3cFlex10PortEnableStatus_Object = MibTableColumn
hh3cFlex10PortEnableStatus = _Hh3cFlex10PortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 1, 1, 2),
    _Hh3cFlex10PortEnableStatus_Type()
)
hh3cFlex10PortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFlex10PortEnableStatus.setStatus("current")
_Hh3cFlex10RemoteSchannelTable_Object = MibTable
hh3cFlex10RemoteSchannelTable = _Hh3cFlex10RemoteSchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2)
)
if mibBuilder.loadTexts:
    hh3cFlex10RemoteSchannelTable.setStatus("current")
_Hh3cFlex10RemoteSchannelEntry_Object = MibTableRow
hh3cFlex10RemoteSchannelEntry = _Hh3cFlex10RemoteSchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1)
)
hh3cFlex10RemoteSchannelEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cFlex10PortNumber"),
    (0, "HH3C-EVB-MIB", "hh3cEvbSchannelID"),
)
if mibBuilder.loadTexts:
    hh3cFlex10RemoteSchannelEntry.setStatus("current")


class _Hh3cFlex10RemSchDesFormat_Type(Bits):
    """Custom type hh3cFlex10RemSchDesFormat based on Bits"""
    namedValues = NamedValues(
        *(("format0", 0),
          ("format1", 1))
    )

_Hh3cFlex10RemSchDesFormat_Type.__name__ = "Bits"
_Hh3cFlex10RemSchDesFormat_Object = MibTableColumn
hh3cFlex10RemSchDesFormat = _Hh3cFlex10RemSchDesFormat_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 1),
    _Hh3cFlex10RemSchDesFormat_Type()
)
hh3cFlex10RemSchDesFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchDesFormat.setStatus("current")
_Hh3cFlex10RemSchTerminationType_Type = Integer32
_Hh3cFlex10RemSchTerminationType_Object = MibTableColumn
hh3cFlex10RemSchTerminationType = _Hh3cFlex10RemSchTerminationType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 2),
    _Hh3cFlex10RemSchTerminationType_Type()
)
hh3cFlex10RemSchTerminationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchTerminationType.setStatus("current")


class _Hh3cFlex10RemSchTerminationCap_Type(Bits):
    """Custom type hh3cFlex10RemSchTerminationCap based on Bits"""
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("fCOE", 1),
          ("iSCSI", 2),
          ("roCEE", 3))
    )

_Hh3cFlex10RemSchTerminationCap_Type.__name__ = "Bits"
_Hh3cFlex10RemSchTerminationCap_Object = MibTableColumn
hh3cFlex10RemSchTerminationCap = _Hh3cFlex10RemSchTerminationCap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 3),
    _Hh3cFlex10RemSchTerminationCap_Type()
)
hh3cFlex10RemSchTerminationCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchTerminationCap.setStatus("current")


class _Hh3cFlex10RemSchTrafficClass_Type(Bits):
    """Custom type hh3cFlex10RemSchTrafficClass based on Bits"""
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5),
          ("class6", 6),
          ("class7", 7))
    )

_Hh3cFlex10RemSchTrafficClass_Type.__name__ = "Bits"
_Hh3cFlex10RemSchTrafficClass_Object = MibTableColumn
hh3cFlex10RemSchTrafficClass = _Hh3cFlex10RemSchTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 4),
    _Hh3cFlex10RemSchTrafficClass_Type()
)
hh3cFlex10RemSchTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchTrafficClass.setStatus("current")
_Hh3cFlex10RemSchCir_Type = Integer32
_Hh3cFlex10RemSchCir_Object = MibTableColumn
hh3cFlex10RemSchCir = _Hh3cFlex10RemSchCir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 5),
    _Hh3cFlex10RemSchCir_Type()
)
hh3cFlex10RemSchCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchCir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchCir.setUnits("mbps")
_Hh3cFlex10RemSchPir_Type = Integer32
_Hh3cFlex10RemSchPir_Object = MibTableColumn
hh3cFlex10RemSchPir = _Hh3cFlex10RemSchPir_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 6),
    _Hh3cFlex10RemSchPir_Type()
)
hh3cFlex10RemSchPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchPir.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchPir.setUnits("mbps")


class _Hh3cFlex10RemSchConnectionID_Type(OctetString):
    """Custom type hh3cFlex10RemSchConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Hh3cFlex10RemSchConnectionID_Type.__name__ = "OctetString"
_Hh3cFlex10RemSchConnectionID_Object = MibTableColumn
hh3cFlex10RemSchConnectionID = _Hh3cFlex10RemSchConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 2, 1, 7),
    _Hh3cFlex10RemSchConnectionID_Type()
)
hh3cFlex10RemSchConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10RemSchConnectionID.setStatus("current")
_Hh3cFlex10SchannelLinkCtlTable_Object = MibTable
hh3cFlex10SchannelLinkCtlTable = _Hh3cFlex10SchannelLinkCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3)
)
if mibBuilder.loadTexts:
    hh3cFlex10SchannelLinkCtlTable.setStatus("current")
_Hh3cFlex10SchannelLinkCtlEntry_Object = MibTableRow
hh3cFlex10SchannelLinkCtlEntry = _Hh3cFlex10SchannelLinkCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1)
)
hh3cFlex10SchannelLinkCtlEntry.setIndexNames(
    (0, "HH3C-EVB-MIB", "hh3cFlex10PortNumber"),
    (0, "HH3C-EVB-MIB", "hh3cEvbSchannelID"),
)
if mibBuilder.loadTexts:
    hh3cFlex10SchannelLinkCtlEntry.setStatus("current")
_Hh3cFlex10SchannelSVID_Type = VlanIndex
_Hh3cFlex10SchannelSVID_Object = MibTableColumn
hh3cFlex10SchannelSVID = _Hh3cFlex10SchannelSVID_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1, 1),
    _Hh3cFlex10SchannelSVID_Type()
)
hh3cFlex10SchannelSVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10SchannelSVID.setStatus("current")


class _Hh3cFlex10SchannelLocalStatus_Type(Integer32):
    """Custom type hh3cFlex10SchannelLocalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("unknown", 1))
    )


_Hh3cFlex10SchannelLocalStatus_Type.__name__ = "Integer32"
_Hh3cFlex10SchannelLocalStatus_Object = MibTableColumn
hh3cFlex10SchannelLocalStatus = _Hh3cFlex10SchannelLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1, 2),
    _Hh3cFlex10SchannelLocalStatus_Type()
)
hh3cFlex10SchannelLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10SchannelLocalStatus.setStatus("current")


class _Hh3cFlex10SchannelRemoteStatus_Type(Integer32):
    """Custom type hh3cFlex10SchannelRemoteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 3),
          ("unknown", 1))
    )


_Hh3cFlex10SchannelRemoteStatus_Type.__name__ = "Integer32"
_Hh3cFlex10SchannelRemoteStatus_Object = MibTableColumn
hh3cFlex10SchannelRemoteStatus = _Hh3cFlex10SchannelRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 134, 3, 3, 1, 3),
    _Hh3cFlex10SchannelRemoteStatus_Type()
)
hh3cFlex10SchannelRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFlex10SchannelRemoteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-EVB-MIB",
    **{"hh3cEvb": hh3cEvb,
       "hh3cEvbSysObjects": hh3cEvbSysObjects,
       "hh3cEvbSetResult": hh3cEvbSetResult,
       "hh3cEvbDefaultManagerTable": hh3cEvbDefaultManagerTable,
       "hh3cEvbDefaultManagerEntry": hh3cEvbDefaultManagerEntry,
       "hh3cEvbManagerIndex": hh3cEvbManagerIndex,
       "hh3cEvbManagerType": hh3cEvbManagerType,
       "hh3cEvbManagerID": hh3cEvbManagerID,
       "hh3cEvbManagerPort": hh3cEvbManagerPort,
       "hh3cEvbManagerRowStatus": hh3cEvbManagerRowStatus,
       "hh3cEvbPortObjects": hh3cEvbPortObjects,
       "hh3cEvbPortConfigTable": hh3cEvbPortConfigTable,
       "hh3cEvbPortConfigEntry": hh3cEvbPortConfigEntry,
       "hh3cEvbPortNumber": hh3cEvbPortNumber,
       "hh3cEvbRWD": hh3cEvbRWD,
       "hh3cEvbRKA": hh3cEvbRKA,
       "hh3cEvbSchannelConfigTable": hh3cEvbSchannelConfigTable,
       "hh3cEvbSchannelConfigEntry": hh3cEvbSchannelConfigEntry,
       "hh3cEvbSchannelID": hh3cEvbSchannelID,
       "hh3cEvbSchannelSVLAN": hh3cEvbSchannelSVLAN,
       "hh3cEvbMacLearningStatus": hh3cEvbMacLearningStatus,
       "hh3cEvbRRStatus": hh3cEvbRRStatus,
       "hh3cEvbSchannelRowStatus": hh3cEvbSchannelRowStatus,
       "hh3cEvbVSIConfigTable": hh3cEvbVSIConfigTable,
       "hh3cEvbVSIConfigEntry": hh3cEvbVSIConfigEntry,
       "hh3cEvbSBPPortNumber": hh3cEvbSBPPortNumber,
       "hh3cEvbVSILocalID": hh3cEvbVSILocalID,
       "hh3cEvbVSICommand": hh3cEvbVSICommand,
       "hh3cEvbVSIIfIndex": hh3cEvbVSIIfIndex,
       "hh3cEvbVSIIsActive": hh3cEvbVSIIsActive,
       "hh3cEvbVSIRowStatus": hh3cEvbVSIRowStatus,
       "hh3cEvbVSIFilterConfigTable": hh3cEvbVSIFilterConfigTable,
       "hh3cEvbVSIFilterConfigEntry": hh3cEvbVSIFilterConfigEntry,
       "hh3cEvbGroupID": hh3cEvbGroupID,
       "hh3cEvbVSIMac": hh3cEvbVSIMac,
       "hh3cEvbVSIVlanId": hh3cEvbVSIVlanId,
       "hh3cEvbVSIFilterRowStatus": hh3cEvbVSIFilterRowStatus,
       "hh3cFlex10Objects": hh3cFlex10Objects,
       "hh3cFlex10PortConfigTable": hh3cFlex10PortConfigTable,
       "hh3cFlex10PortConfigEntry": hh3cFlex10PortConfigEntry,
       "hh3cFlex10PortNumber": hh3cFlex10PortNumber,
       "hh3cFlex10PortEnableStatus": hh3cFlex10PortEnableStatus,
       "hh3cFlex10RemoteSchannelTable": hh3cFlex10RemoteSchannelTable,
       "hh3cFlex10RemoteSchannelEntry": hh3cFlex10RemoteSchannelEntry,
       "hh3cFlex10RemSchDesFormat": hh3cFlex10RemSchDesFormat,
       "hh3cFlex10RemSchTerminationType": hh3cFlex10RemSchTerminationType,
       "hh3cFlex10RemSchTerminationCap": hh3cFlex10RemSchTerminationCap,
       "hh3cFlex10RemSchTrafficClass": hh3cFlex10RemSchTrafficClass,
       "hh3cFlex10RemSchCir": hh3cFlex10RemSchCir,
       "hh3cFlex10RemSchPir": hh3cFlex10RemSchPir,
       "hh3cFlex10RemSchConnectionID": hh3cFlex10RemSchConnectionID,
       "hh3cFlex10SchannelLinkCtlTable": hh3cFlex10SchannelLinkCtlTable,
       "hh3cFlex10SchannelLinkCtlEntry": hh3cFlex10SchannelLinkCtlEntry,
       "hh3cFlex10SchannelSVID": hh3cFlex10SchannelSVID,
       "hh3cFlex10SchannelLocalStatus": hh3cFlex10SchannelLocalStatus,
       "hh3cFlex10SchannelRemoteStatus": hh3cFlex10SchannelRemoteStatus}
)
