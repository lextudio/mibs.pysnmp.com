# SNMP MIB module (HPN-ICF-EVB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-EVB-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:12 2024
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

hpnicfEvb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134)
)
hpnicfEvb.setRevisions(
        ("2012-12-21 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfEvbSysObjects_ObjectIdentity = ObjectIdentity
hpnicfEvbSysObjects = _HpnicfEvbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1)
)


class _HpnicfEvbSetResult_Type(Integer32):
    """Custom type hpnicfEvbSetResult based on Integer32"""
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


_HpnicfEvbSetResult_Type.__name__ = "Integer32"
_HpnicfEvbSetResult_Object = MibScalar
hpnicfEvbSetResult = _HpnicfEvbSetResult_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 1),
    _HpnicfEvbSetResult_Type()
)
hpnicfEvbSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvbSetResult.setStatus("current")
_HpnicfEvbDefaultManagerTable_Object = MibTable
hpnicfEvbDefaultManagerTable = _HpnicfEvbDefaultManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfEvbDefaultManagerTable.setStatus("current")
_HpnicfEvbDefaultManagerEntry_Object = MibTableRow
hpnicfEvbDefaultManagerEntry = _HpnicfEvbDefaultManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1)
)
hpnicfEvbDefaultManagerEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbManagerIndex"),
)
if mibBuilder.loadTexts:
    hpnicfEvbDefaultManagerEntry.setStatus("current")
_HpnicfEvbManagerIndex_Type = Unsigned32
_HpnicfEvbManagerIndex_Object = MibTableColumn
hpnicfEvbManagerIndex = _HpnicfEvbManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 1),
    _HpnicfEvbManagerIndex_Type()
)
hpnicfEvbManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbManagerIndex.setStatus("current")


class _HpnicfEvbManagerType_Type(Integer32):
    """Custom type hpnicfEvbManagerType based on Integer32"""
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


_HpnicfEvbManagerType_Type.__name__ = "Integer32"
_HpnicfEvbManagerType_Object = MibTableColumn
hpnicfEvbManagerType = _HpnicfEvbManagerType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 2),
    _HpnicfEvbManagerType_Type()
)
hpnicfEvbManagerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbManagerType.setStatus("current")


class _HpnicfEvbManagerID_Type(OctetString):
    """Custom type hpnicfEvbManagerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_HpnicfEvbManagerID_Type.__name__ = "OctetString"
_HpnicfEvbManagerID_Object = MibTableColumn
hpnicfEvbManagerID = _HpnicfEvbManagerID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 3),
    _HpnicfEvbManagerID_Type()
)
hpnicfEvbManagerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbManagerID.setStatus("current")


class _HpnicfEvbManagerPort_Type(Unsigned32):
    """Custom type hpnicfEvbManagerPort based on Unsigned32"""
    defaultValue = 8080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfEvbManagerPort_Type.__name__ = "Unsigned32"
_HpnicfEvbManagerPort_Object = MibTableColumn
hpnicfEvbManagerPort = _HpnicfEvbManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 4),
    _HpnicfEvbManagerPort_Type()
)
hpnicfEvbManagerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbManagerPort.setStatus("current")
_HpnicfEvbManagerRowStatus_Type = RowStatus
_HpnicfEvbManagerRowStatus_Object = MibTableColumn
hpnicfEvbManagerRowStatus = _HpnicfEvbManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 1, 2, 1, 5),
    _HpnicfEvbManagerRowStatus_Type()
)
hpnicfEvbManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbManagerRowStatus.setStatus("current")
_HpnicfEvbPortObjects_ObjectIdentity = ObjectIdentity
hpnicfEvbPortObjects = _HpnicfEvbPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2)
)
_HpnicfEvbPortConfigTable_Object = MibTable
hpnicfEvbPortConfigTable = _HpnicfEvbPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfEvbPortConfigTable.setStatus("current")
_HpnicfEvbPortConfigEntry_Object = MibTableRow
hpnicfEvbPortConfigEntry = _HpnicfEvbPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1)
)
hpnicfEvbPortConfigEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbPortNumber"),
)
if mibBuilder.loadTexts:
    hpnicfEvbPortConfigEntry.setStatus("current")
_HpnicfEvbPortNumber_Type = IEEE8021BridgePortNumber
_HpnicfEvbPortNumber_Object = MibTableColumn
hpnicfEvbPortNumber = _HpnicfEvbPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 1),
    _HpnicfEvbPortNumber_Type()
)
hpnicfEvbPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbPortNumber.setStatus("current")


class _HpnicfEvbRWD_Type(Unsigned32):
    """Custom type hpnicfEvbRWD based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 31),
    )


_HpnicfEvbRWD_Type.__name__ = "Unsigned32"
_HpnicfEvbRWD_Object = MibTableColumn
hpnicfEvbRWD = _HpnicfEvbRWD_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 2),
    _HpnicfEvbRWD_Type()
)
hpnicfEvbRWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvbRWD.setStatus("current")


class _HpnicfEvbRKA_Type(Unsigned32):
    """Custom type hpnicfEvbRKA based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 31),
    )


_HpnicfEvbRKA_Type.__name__ = "Unsigned32"
_HpnicfEvbRKA_Object = MibTableColumn
hpnicfEvbRKA = _HpnicfEvbRKA_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 1, 1, 3),
    _HpnicfEvbRKA_Type()
)
hpnicfEvbRKA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvbRKA.setStatus("current")
_HpnicfEvbSchannelConfigTable_Object = MibTable
hpnicfEvbSchannelConfigTable = _HpnicfEvbSchannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2)
)
if mibBuilder.loadTexts:
    hpnicfEvbSchannelConfigTable.setStatus("current")
_HpnicfEvbSchannelConfigEntry_Object = MibTableRow
hpnicfEvbSchannelConfigEntry = _HpnicfEvbSchannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1)
)
hpnicfEvbSchannelConfigEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbPortNumber"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"),
)
if mibBuilder.loadTexts:
    hpnicfEvbSchannelConfigEntry.setStatus("current")
_HpnicfEvbSchannelID_Type = Unsigned32
_HpnicfEvbSchannelID_Object = MibTableColumn
hpnicfEvbSchannelID = _HpnicfEvbSchannelID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 1),
    _HpnicfEvbSchannelID_Type()
)
hpnicfEvbSchannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbSchannelID.setStatus("current")


class _HpnicfEvbSchannelSVLAN_Type(Unsigned32):
    """Custom type hpnicfEvbSchannelSVLAN based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_HpnicfEvbSchannelSVLAN_Type.__name__ = "Unsigned32"
_HpnicfEvbSchannelSVLAN_Object = MibTableColumn
hpnicfEvbSchannelSVLAN = _HpnicfEvbSchannelSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 2),
    _HpnicfEvbSchannelSVLAN_Type()
)
hpnicfEvbSchannelSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbSchannelSVLAN.setStatus("current")


class _HpnicfEvbMacLearningStatus_Type(TruthValue):
    """Custom type hpnicfEvbMacLearningStatus based on TruthValue"""


_HpnicfEvbMacLearningStatus_Object = MibTableColumn
hpnicfEvbMacLearningStatus = _HpnicfEvbMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 3),
    _HpnicfEvbMacLearningStatus_Type()
)
hpnicfEvbMacLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvbMacLearningStatus.setStatus("current")


class _HpnicfEvbRRStatus_Type(TruthValue):
    """Custom type hpnicfEvbRRStatus based on TruthValue"""


_HpnicfEvbRRStatus_Object = MibTableColumn
hpnicfEvbRRStatus = _HpnicfEvbRRStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 4),
    _HpnicfEvbRRStatus_Type()
)
hpnicfEvbRRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvbRRStatus.setStatus("current")
_HpnicfEvbSchannelRowStatus_Type = RowStatus
_HpnicfEvbSchannelRowStatus_Object = MibTableColumn
hpnicfEvbSchannelRowStatus = _HpnicfEvbSchannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 2, 1, 5),
    _HpnicfEvbSchannelRowStatus_Type()
)
hpnicfEvbSchannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbSchannelRowStatus.setStatus("current")
_HpnicfEvbVSIConfigTable_Object = MibTable
hpnicfEvbVSIConfigTable = _HpnicfEvbVSIConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3)
)
if mibBuilder.loadTexts:
    hpnicfEvbVSIConfigTable.setStatus("current")
_HpnicfEvbVSIConfigEntry_Object = MibTableRow
hpnicfEvbVSIConfigEntry = _HpnicfEvbVSIConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1)
)
hpnicfEvbVSIConfigEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSBPPortNumber"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSILocalID"),
)
if mibBuilder.loadTexts:
    hpnicfEvbVSIConfigEntry.setStatus("current")
_HpnicfEvbSBPPortNumber_Type = IEEE8021BridgePortNumber
_HpnicfEvbSBPPortNumber_Object = MibTableColumn
hpnicfEvbSBPPortNumber = _HpnicfEvbSBPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 1),
    _HpnicfEvbSBPPortNumber_Type()
)
hpnicfEvbSBPPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbSBPPortNumber.setStatus("current")
_HpnicfEvbVSILocalID_Type = Unsigned32
_HpnicfEvbVSILocalID_Object = MibTableColumn
hpnicfEvbVSILocalID = _HpnicfEvbVSILocalID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 2),
    _HpnicfEvbVSILocalID_Type()
)
hpnicfEvbVSILocalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbVSILocalID.setStatus("current")


class _HpnicfEvbVSICommand_Type(Integer32):
    """Custom type hpnicfEvbVSICommand based on Integer32"""
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


_HpnicfEvbVSICommand_Type.__name__ = "Integer32"
_HpnicfEvbVSICommand_Object = MibTableColumn
hpnicfEvbVSICommand = _HpnicfEvbVSICommand_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 3),
    _HpnicfEvbVSICommand_Type()
)
hpnicfEvbVSICommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbVSICommand.setStatus("current")
_HpnicfEvbVSIIfIndex_Type = InterfaceIndexOrZero
_HpnicfEvbVSIIfIndex_Object = MibTableColumn
hpnicfEvbVSIIfIndex = _HpnicfEvbVSIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 4),
    _HpnicfEvbVSIIfIndex_Type()
)
hpnicfEvbVSIIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfEvbVSIIfIndex.setStatus("current")


class _HpnicfEvbVSIIsActive_Type(TruthValue):
    """Custom type hpnicfEvbVSIIsActive based on TruthValue"""


_HpnicfEvbVSIIsActive_Object = MibTableColumn
hpnicfEvbVSIIsActive = _HpnicfEvbVSIIsActive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 5),
    _HpnicfEvbVSIIsActive_Type()
)
hpnicfEvbVSIIsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfEvbVSIIsActive.setStatus("current")
_HpnicfEvbVSIRowStatus_Type = RowStatus
_HpnicfEvbVSIRowStatus_Object = MibTableColumn
hpnicfEvbVSIRowStatus = _HpnicfEvbVSIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 3, 1, 6),
    _HpnicfEvbVSIRowStatus_Type()
)
hpnicfEvbVSIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbVSIRowStatus.setStatus("current")
_HpnicfEvbVSIFilterConfigTable_Object = MibTable
hpnicfEvbVSIFilterConfigTable = _HpnicfEvbVSIFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4)
)
if mibBuilder.loadTexts:
    hpnicfEvbVSIFilterConfigTable.setStatus("current")
_HpnicfEvbVSIFilterConfigEntry_Object = MibTableRow
hpnicfEvbVSIFilterConfigEntry = _HpnicfEvbVSIFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1)
)
hpnicfEvbVSIFilterConfigEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSBPPortNumber"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSILocalID"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbGroupID"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSIMac"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbVSIVlanId"),
)
if mibBuilder.loadTexts:
    hpnicfEvbVSIFilterConfigEntry.setStatus("current")
_HpnicfEvbGroupID_Type = Unsigned32
_HpnicfEvbGroupID_Object = MibTableColumn
hpnicfEvbGroupID = _HpnicfEvbGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 1),
    _HpnicfEvbGroupID_Type()
)
hpnicfEvbGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbGroupID.setStatus("current")
_HpnicfEvbVSIMac_Type = MacAddress
_HpnicfEvbVSIMac_Object = MibTableColumn
hpnicfEvbVSIMac = _HpnicfEvbVSIMac_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 2),
    _HpnicfEvbVSIMac_Type()
)
hpnicfEvbVSIMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbVSIMac.setStatus("current")
_HpnicfEvbVSIVlanId_Type = VlanIndex
_HpnicfEvbVSIVlanId_Object = MibTableColumn
hpnicfEvbVSIVlanId = _HpnicfEvbVSIVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 3),
    _HpnicfEvbVSIVlanId_Type()
)
hpnicfEvbVSIVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfEvbVSIVlanId.setStatus("current")
_HpnicfEvbVSIFilterRowStatus_Type = RowStatus
_HpnicfEvbVSIFilterRowStatus_Object = MibTableColumn
hpnicfEvbVSIFilterRowStatus = _HpnicfEvbVSIFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 2, 4, 1, 4),
    _HpnicfEvbVSIFilterRowStatus_Type()
)
hpnicfEvbVSIFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfEvbVSIFilterRowStatus.setStatus("current")
_HpnicfFlex10Objects_ObjectIdentity = ObjectIdentity
hpnicfFlex10Objects = _HpnicfFlex10Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3)
)
_HpnicfFlex10PortConfigTable_Object = MibTable
hpnicfFlex10PortConfigTable = _HpnicfFlex10PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1)
)
if mibBuilder.loadTexts:
    hpnicfFlex10PortConfigTable.setStatus("current")
_HpnicfFlex10PortConfigEntry_Object = MibTableRow
hpnicfFlex10PortConfigEntry = _HpnicfFlex10PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1)
)
hpnicfFlex10PortConfigEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"),
)
if mibBuilder.loadTexts:
    hpnicfFlex10PortConfigEntry.setStatus("current")
_HpnicfFlex10PortNumber_Type = IEEE8021BridgePortNumber
_HpnicfFlex10PortNumber_Object = MibTableColumn
hpnicfFlex10PortNumber = _HpnicfFlex10PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1, 1),
    _HpnicfFlex10PortNumber_Type()
)
hpnicfFlex10PortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFlex10PortNumber.setStatus("current")


class _HpnicfFlex10PortEnableStatus_Type(TruthValue):
    """Custom type hpnicfFlex10PortEnableStatus based on TruthValue"""


_HpnicfFlex10PortEnableStatus_Object = MibTableColumn
hpnicfFlex10PortEnableStatus = _HpnicfFlex10PortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 1, 1, 2),
    _HpnicfFlex10PortEnableStatus_Type()
)
hpnicfFlex10PortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFlex10PortEnableStatus.setStatus("current")
_HpnicfFlex10RemoteSchannelTable_Object = MibTable
hpnicfFlex10RemoteSchannelTable = _HpnicfFlex10RemoteSchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2)
)
if mibBuilder.loadTexts:
    hpnicfFlex10RemoteSchannelTable.setStatus("current")
_HpnicfFlex10RemoteSchannelEntry_Object = MibTableRow
hpnicfFlex10RemoteSchannelEntry = _HpnicfFlex10RemoteSchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1)
)
hpnicfFlex10RemoteSchannelEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"),
)
if mibBuilder.loadTexts:
    hpnicfFlex10RemoteSchannelEntry.setStatus("current")


class _HpnicfFlex10RemSchDesFormat_Type(Bits):
    """Custom type hpnicfFlex10RemSchDesFormat based on Bits"""
    namedValues = NamedValues(
        *(("format0", 0),
          ("format1", 1))
    )

_HpnicfFlex10RemSchDesFormat_Type.__name__ = "Bits"
_HpnicfFlex10RemSchDesFormat_Object = MibTableColumn
hpnicfFlex10RemSchDesFormat = _HpnicfFlex10RemSchDesFormat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 1),
    _HpnicfFlex10RemSchDesFormat_Type()
)
hpnicfFlex10RemSchDesFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchDesFormat.setStatus("current")
_HpnicfFlex10RemSchTerminationType_Type = Integer32
_HpnicfFlex10RemSchTerminationType_Object = MibTableColumn
hpnicfFlex10RemSchTerminationType = _HpnicfFlex10RemSchTerminationType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 2),
    _HpnicfFlex10RemSchTerminationType_Type()
)
hpnicfFlex10RemSchTerminationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchTerminationType.setStatus("current")


class _HpnicfFlex10RemSchTerminationCap_Type(Bits):
    """Custom type hpnicfFlex10RemSchTerminationCap based on Bits"""
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("fCOE", 1),
          ("iSCSI", 2),
          ("roCEE", 3))
    )

_HpnicfFlex10RemSchTerminationCap_Type.__name__ = "Bits"
_HpnicfFlex10RemSchTerminationCap_Object = MibTableColumn
hpnicfFlex10RemSchTerminationCap = _HpnicfFlex10RemSchTerminationCap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 3),
    _HpnicfFlex10RemSchTerminationCap_Type()
)
hpnicfFlex10RemSchTerminationCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchTerminationCap.setStatus("current")


class _HpnicfFlex10RemSchTrafficClass_Type(Bits):
    """Custom type hpnicfFlex10RemSchTrafficClass based on Bits"""
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

_HpnicfFlex10RemSchTrafficClass_Type.__name__ = "Bits"
_HpnicfFlex10RemSchTrafficClass_Object = MibTableColumn
hpnicfFlex10RemSchTrafficClass = _HpnicfFlex10RemSchTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 4),
    _HpnicfFlex10RemSchTrafficClass_Type()
)
hpnicfFlex10RemSchTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchTrafficClass.setStatus("current")
_HpnicfFlex10RemSchCir_Type = Integer32
_HpnicfFlex10RemSchCir_Object = MibTableColumn
hpnicfFlex10RemSchCir = _HpnicfFlex10RemSchCir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 5),
    _HpnicfFlex10RemSchCir_Type()
)
hpnicfFlex10RemSchCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchCir.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchCir.setUnits("mbps")
_HpnicfFlex10RemSchPir_Type = Integer32
_HpnicfFlex10RemSchPir_Object = MibTableColumn
hpnicfFlex10RemSchPir = _HpnicfFlex10RemSchPir_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 6),
    _HpnicfFlex10RemSchPir_Type()
)
hpnicfFlex10RemSchPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchPir.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchPir.setUnits("mbps")


class _HpnicfFlex10RemSchConnectionID_Type(OctetString):
    """Custom type hpnicfFlex10RemSchConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_HpnicfFlex10RemSchConnectionID_Type.__name__ = "OctetString"
_HpnicfFlex10RemSchConnectionID_Object = MibTableColumn
hpnicfFlex10RemSchConnectionID = _HpnicfFlex10RemSchConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 2, 1, 7),
    _HpnicfFlex10RemSchConnectionID_Type()
)
hpnicfFlex10RemSchConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10RemSchConnectionID.setStatus("current")
_HpnicfFlex10SchannelLinkCtlTable_Object = MibTable
hpnicfFlex10SchannelLinkCtlTable = _HpnicfFlex10SchannelLinkCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3)
)
if mibBuilder.loadTexts:
    hpnicfFlex10SchannelLinkCtlTable.setStatus("current")
_HpnicfFlex10SchannelLinkCtlEntry_Object = MibTableRow
hpnicfFlex10SchannelLinkCtlEntry = _HpnicfFlex10SchannelLinkCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1)
)
hpnicfFlex10SchannelLinkCtlEntry.setIndexNames(
    (0, "HPN-ICF-EVB-MIB", "hpnicfFlex10PortNumber"),
    (0, "HPN-ICF-EVB-MIB", "hpnicfEvbSchannelID"),
)
if mibBuilder.loadTexts:
    hpnicfFlex10SchannelLinkCtlEntry.setStatus("current")
_HpnicfFlex10SchannelSVID_Type = VlanIndex
_HpnicfFlex10SchannelSVID_Object = MibTableColumn
hpnicfFlex10SchannelSVID = _HpnicfFlex10SchannelSVID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 1),
    _HpnicfFlex10SchannelSVID_Type()
)
hpnicfFlex10SchannelSVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10SchannelSVID.setStatus("current")


class _HpnicfFlex10SchannelLocalStatus_Type(Integer32):
    """Custom type hpnicfFlex10SchannelLocalStatus based on Integer32"""
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


_HpnicfFlex10SchannelLocalStatus_Type.__name__ = "Integer32"
_HpnicfFlex10SchannelLocalStatus_Object = MibTableColumn
hpnicfFlex10SchannelLocalStatus = _HpnicfFlex10SchannelLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 2),
    _HpnicfFlex10SchannelLocalStatus_Type()
)
hpnicfFlex10SchannelLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10SchannelLocalStatus.setStatus("current")


class _HpnicfFlex10SchannelRemoteStatus_Type(Integer32):
    """Custom type hpnicfFlex10SchannelRemoteStatus based on Integer32"""
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


_HpnicfFlex10SchannelRemoteStatus_Type.__name__ = "Integer32"
_HpnicfFlex10SchannelRemoteStatus_Object = MibTableColumn
hpnicfFlex10SchannelRemoteStatus = _HpnicfFlex10SchannelRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 134, 3, 3, 1, 3),
    _HpnicfFlex10SchannelRemoteStatus_Type()
)
hpnicfFlex10SchannelRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFlex10SchannelRemoteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-EVB-MIB",
    **{"hpnicfEvb": hpnicfEvb,
       "hpnicfEvbSysObjects": hpnicfEvbSysObjects,
       "hpnicfEvbSetResult": hpnicfEvbSetResult,
       "hpnicfEvbDefaultManagerTable": hpnicfEvbDefaultManagerTable,
       "hpnicfEvbDefaultManagerEntry": hpnicfEvbDefaultManagerEntry,
       "hpnicfEvbManagerIndex": hpnicfEvbManagerIndex,
       "hpnicfEvbManagerType": hpnicfEvbManagerType,
       "hpnicfEvbManagerID": hpnicfEvbManagerID,
       "hpnicfEvbManagerPort": hpnicfEvbManagerPort,
       "hpnicfEvbManagerRowStatus": hpnicfEvbManagerRowStatus,
       "hpnicfEvbPortObjects": hpnicfEvbPortObjects,
       "hpnicfEvbPortConfigTable": hpnicfEvbPortConfigTable,
       "hpnicfEvbPortConfigEntry": hpnicfEvbPortConfigEntry,
       "hpnicfEvbPortNumber": hpnicfEvbPortNumber,
       "hpnicfEvbRWD": hpnicfEvbRWD,
       "hpnicfEvbRKA": hpnicfEvbRKA,
       "hpnicfEvbSchannelConfigTable": hpnicfEvbSchannelConfigTable,
       "hpnicfEvbSchannelConfigEntry": hpnicfEvbSchannelConfigEntry,
       "hpnicfEvbSchannelID": hpnicfEvbSchannelID,
       "hpnicfEvbSchannelSVLAN": hpnicfEvbSchannelSVLAN,
       "hpnicfEvbMacLearningStatus": hpnicfEvbMacLearningStatus,
       "hpnicfEvbRRStatus": hpnicfEvbRRStatus,
       "hpnicfEvbSchannelRowStatus": hpnicfEvbSchannelRowStatus,
       "hpnicfEvbVSIConfigTable": hpnicfEvbVSIConfigTable,
       "hpnicfEvbVSIConfigEntry": hpnicfEvbVSIConfigEntry,
       "hpnicfEvbSBPPortNumber": hpnicfEvbSBPPortNumber,
       "hpnicfEvbVSILocalID": hpnicfEvbVSILocalID,
       "hpnicfEvbVSICommand": hpnicfEvbVSICommand,
       "hpnicfEvbVSIIfIndex": hpnicfEvbVSIIfIndex,
       "hpnicfEvbVSIIsActive": hpnicfEvbVSIIsActive,
       "hpnicfEvbVSIRowStatus": hpnicfEvbVSIRowStatus,
       "hpnicfEvbVSIFilterConfigTable": hpnicfEvbVSIFilterConfigTable,
       "hpnicfEvbVSIFilterConfigEntry": hpnicfEvbVSIFilterConfigEntry,
       "hpnicfEvbGroupID": hpnicfEvbGroupID,
       "hpnicfEvbVSIMac": hpnicfEvbVSIMac,
       "hpnicfEvbVSIVlanId": hpnicfEvbVSIVlanId,
       "hpnicfEvbVSIFilterRowStatus": hpnicfEvbVSIFilterRowStatus,
       "hpnicfFlex10Objects": hpnicfFlex10Objects,
       "hpnicfFlex10PortConfigTable": hpnicfFlex10PortConfigTable,
       "hpnicfFlex10PortConfigEntry": hpnicfFlex10PortConfigEntry,
       "hpnicfFlex10PortNumber": hpnicfFlex10PortNumber,
       "hpnicfFlex10PortEnableStatus": hpnicfFlex10PortEnableStatus,
       "hpnicfFlex10RemoteSchannelTable": hpnicfFlex10RemoteSchannelTable,
       "hpnicfFlex10RemoteSchannelEntry": hpnicfFlex10RemoteSchannelEntry,
       "hpnicfFlex10RemSchDesFormat": hpnicfFlex10RemSchDesFormat,
       "hpnicfFlex10RemSchTerminationType": hpnicfFlex10RemSchTerminationType,
       "hpnicfFlex10RemSchTerminationCap": hpnicfFlex10RemSchTerminationCap,
       "hpnicfFlex10RemSchTrafficClass": hpnicfFlex10RemSchTrafficClass,
       "hpnicfFlex10RemSchCir": hpnicfFlex10RemSchCir,
       "hpnicfFlex10RemSchPir": hpnicfFlex10RemSchPir,
       "hpnicfFlex10RemSchConnectionID": hpnicfFlex10RemSchConnectionID,
       "hpnicfFlex10SchannelLinkCtlTable": hpnicfFlex10SchannelLinkCtlTable,
       "hpnicfFlex10SchannelLinkCtlEntry": hpnicfFlex10SchannelLinkCtlEntry,
       "hpnicfFlex10SchannelSVID": hpnicfFlex10SchannelSVID,
       "hpnicfFlex10SchannelLocalStatus": hpnicfFlex10SchannelLocalStatus,
       "hpnicfFlex10SchannelRemoteStatus": hpnicfFlex10SchannelRemoteStatus}
)
