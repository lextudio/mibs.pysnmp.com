# SNMP MIB module (HPN-ICF-FCOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-FCOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:22 2024
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

(fcmInstanceIndex,) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "fcmInstanceIndex")

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

hpnicfFCoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120)
)
hpnicfFCoE.setRevisions(
        ("2012-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HpnicfFCoEVfcBindType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceIndex", 1),
          ("macAddress", 2))
    )



# MIB Managed Objects in the order of their OIDs

_HpnicfFCoEObjects_ObjectIdentity = ObjectIdentity
hpnicfFCoEObjects = _HpnicfFCoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1)
)
_HpnicfFCoEConfig_ObjectIdentity = ObjectIdentity
hpnicfFCoEConfig = _HpnicfFCoEConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1)
)
_HpnicfFCoECfgTable_Object = MibTable
hpnicfFCoECfgTable = _HpnicfFCoECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpnicfFCoECfgTable.setStatus("current")
_HpnicfFCoECfgEntry_Object = MibTableRow
hpnicfFCoECfgEntry = _HpnicfFCoECfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1)
)
hpnicfFCoECfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFCoECfgEntry.setStatus("current")


class _HpnicfFCoECfgFcmap_Type(OctetString):
    """Custom type hpnicfFCoECfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfFCoECfgFcmap_Type.__name__ = "OctetString"
_HpnicfFCoECfgFcmap_Object = MibTableColumn
hpnicfFCoECfgFcmap = _HpnicfFCoECfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 1),
    _HpnicfFCoECfgFcmap_Type()
)
hpnicfFCoECfgFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoECfgFcmap.setStatus("current")


class _HpnicfFCoECfgDynamicVfcCreation_Type(TruthValue):
    """Custom type hpnicfFCoECfgDynamicVfcCreation based on TruthValue"""


_HpnicfFCoECfgDynamicVfcCreation_Object = MibTableColumn
hpnicfFCoECfgDynamicVfcCreation = _HpnicfFCoECfgDynamicVfcCreation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 2),
    _HpnicfFCoECfgDynamicVfcCreation_Type()
)
hpnicfFCoECfgDynamicVfcCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoECfgDynamicVfcCreation.setStatus("current")


class _HpnicfFCoECfgDefaultFCFPriority_Type(Unsigned32):
    """Custom type hpnicfFCoECfgDefaultFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfFCoECfgDefaultFCFPriority_Type.__name__ = "Unsigned32"
_HpnicfFCoECfgDefaultFCFPriority_Object = MibTableColumn
hpnicfFCoECfgDefaultFCFPriority = _HpnicfFCoECfgDefaultFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 3),
    _HpnicfFCoECfgDefaultFCFPriority_Type()
)
hpnicfFCoECfgDefaultFCFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoECfgDefaultFCFPriority.setStatus("current")


class _HpnicfFCoECfgDATov_Type(Unsigned32):
    """Custom type hpnicfFCoECfgDATov based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_HpnicfFCoECfgDATov_Type.__name__ = "Unsigned32"
_HpnicfFCoECfgDATov_Object = MibTableColumn
hpnicfFCoECfgDATov = _HpnicfFCoECfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 4),
    _HpnicfFCoECfgDATov_Type()
)
hpnicfFCoECfgDATov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoECfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    hpnicfFCoECfgDATov.setUnits("seconds")


class _HpnicfFCoECfgAddressingMode_Type(Integer32):
    """Custom type hpnicfFCoECfgAddressingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpma", 1),
          ("fpmaAndSpma", 3),
          ("spma", 2))
    )


_HpnicfFCoECfgAddressingMode_Type.__name__ = "Integer32"
_HpnicfFCoECfgAddressingMode_Object = MibTableColumn
hpnicfFCoECfgAddressingMode = _HpnicfFCoECfgAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 1, 1, 5),
    _HpnicfFCoECfgAddressingMode_Type()
)
hpnicfFCoECfgAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoECfgAddressingMode.setStatus("current")
_HpnicfFCoEVLANTable_Object = MibTable
hpnicfFCoEVLANTable = _HpnicfFCoEVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfFCoEVLANTable.setStatus("current")
_HpnicfFCoEVLANEntry_Object = MibTableRow
hpnicfFCoEVLANEntry = _HpnicfFCoEVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1)
)
hpnicfFCoEVLANEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEVLANIndex"),
    (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEFabricIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFCoEVLANEntry.setStatus("current")
_HpnicfFCoEVLANIndex_Type = VlanIndex
_HpnicfFCoEVLANIndex_Object = MibTableColumn
hpnicfFCoEVLANIndex = _HpnicfFCoEVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 1),
    _HpnicfFCoEVLANIndex_Type()
)
hpnicfFCoEVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFCoEVLANIndex.setStatus("current")
_HpnicfFCoEFabricIndex_Type = T11FabricIndex
_HpnicfFCoEFabricIndex_Object = MibTableColumn
hpnicfFCoEFabricIndex = _HpnicfFCoEFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 2),
    _HpnicfFCoEFabricIndex_Type()
)
hpnicfFCoEFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFCoEFabricIndex.setStatus("current")


class _HpnicfFCoEVLANOperState_Type(Integer32):
    """Custom type hpnicfFCoEVLANOperState based on Integer32"""
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


_HpnicfFCoEVLANOperState_Type.__name__ = "Integer32"
_HpnicfFCoEVLANOperState_Object = MibTableColumn
hpnicfFCoEVLANOperState = _HpnicfFCoEVLANOperState_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 3),
    _HpnicfFCoEVLANOperState_Type()
)
hpnicfFCoEVLANOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFCoEVLANOperState.setStatus("current")
_HpnicfFCoEVLANRowStatus_Type = RowStatus
_HpnicfFCoEVLANRowStatus_Object = MibTableColumn
hpnicfFCoEVLANRowStatus = _HpnicfFCoEVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 2, 1, 4),
    _HpnicfFCoEVLANRowStatus_Type()
)
hpnicfFCoEVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFCoEVLANRowStatus.setStatus("current")
_HpnicfFCoEStaticVfcTable_Object = MibTable
hpnicfFCoEStaticVfcTable = _HpnicfFCoEStaticVfcTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcTable.setStatus("current")
_HpnicfFCoEStaticVfcEntry_Object = MibTableRow
hpnicfFCoEStaticVfcEntry = _HpnicfFCoEStaticVfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1)
)
hpnicfFCoEStaticVfcEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEStaticVfcIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcEntry.setStatus("current")


class _HpnicfFCoEStaticVfcIndex_Type(Unsigned32):
    """Custom type hpnicfFCoEStaticVfcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfFCoEStaticVfcIndex_Type.__name__ = "Unsigned32"
_HpnicfFCoEStaticVfcIndex_Object = MibTableColumn
hpnicfFCoEStaticVfcIndex = _HpnicfFCoEStaticVfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 1),
    _HpnicfFCoEStaticVfcIndex_Type()
)
hpnicfFCoEStaticVfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcIndex.setStatus("current")


class _HpnicfFCoEStaticVfcFCFPriority_Type(Unsigned32):
    """Custom type hpnicfFCoEStaticVfcFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpnicfFCoEStaticVfcFCFPriority_Type.__name__ = "Unsigned32"
_HpnicfFCoEStaticVfcFCFPriority_Object = MibTableColumn
hpnicfFCoEStaticVfcFCFPriority = _HpnicfFCoEStaticVfcFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 2),
    _HpnicfFCoEStaticVfcFCFPriority_Type()
)
hpnicfFCoEStaticVfcFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcFCFPriority.setStatus("current")
_HpnicfFCoEStaticVfcBindType_Type = HpnicfFCoEVfcBindType
_HpnicfFCoEStaticVfcBindType_Object = MibTableColumn
hpnicfFCoEStaticVfcBindType = _HpnicfFCoEStaticVfcBindType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 3),
    _HpnicfFCoEStaticVfcBindType_Type()
)
hpnicfFCoEStaticVfcBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcBindType.setStatus("current")
_HpnicfFCoEStaticVfcBindIfIndex_Type = InterfaceIndexOrZero
_HpnicfFCoEStaticVfcBindIfIndex_Object = MibTableColumn
hpnicfFCoEStaticVfcBindIfIndex = _HpnicfFCoEStaticVfcBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 4),
    _HpnicfFCoEStaticVfcBindIfIndex_Type()
)
hpnicfFCoEStaticVfcBindIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcBindIfIndex.setStatus("current")
_HpnicfFCoEStaticVfcBindMACAddress_Type = MacAddress
_HpnicfFCoEStaticVfcBindMACAddress_Object = MibTableColumn
hpnicfFCoEStaticVfcBindMACAddress = _HpnicfFCoEStaticVfcBindMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 5),
    _HpnicfFCoEStaticVfcBindMACAddress_Type()
)
hpnicfFCoEStaticVfcBindMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcBindMACAddress.setStatus("current")
_HpnicfFCoEStaticVfcIfIndex_Type = InterfaceIndex
_HpnicfFCoEStaticVfcIfIndex_Object = MibTableColumn
hpnicfFCoEStaticVfcIfIndex = _HpnicfFCoEStaticVfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 6),
    _HpnicfFCoEStaticVfcIfIndex_Type()
)
hpnicfFCoEStaticVfcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcIfIndex.setStatus("current")
_HpnicfFCoEStaticVfcCreationTime_Type = TimeStamp
_HpnicfFCoEStaticVfcCreationTime_Object = MibTableColumn
hpnicfFCoEStaticVfcCreationTime = _HpnicfFCoEStaticVfcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 7),
    _HpnicfFCoEStaticVfcCreationTime_Type()
)
hpnicfFCoEStaticVfcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcCreationTime.setStatus("current")
_HpnicfFCoEStaticVfcFailureCause_Type = SnmpAdminString
_HpnicfFCoEStaticVfcFailureCause_Object = MibTableColumn
hpnicfFCoEStaticVfcFailureCause = _HpnicfFCoEStaticVfcFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 8),
    _HpnicfFCoEStaticVfcFailureCause_Type()
)
hpnicfFCoEStaticVfcFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcFailureCause.setStatus("current")
_HpnicfFCoEStaticVfcRowStatus_Type = RowStatus
_HpnicfFCoEStaticVfcRowStatus_Object = MibTableColumn
hpnicfFCoEStaticVfcRowStatus = _HpnicfFCoEStaticVfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 3, 1, 9),
    _HpnicfFCoEStaticVfcRowStatus_Type()
)
hpnicfFCoEStaticVfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfFCoEStaticVfcRowStatus.setStatus("current")
_HpnicfFCoEFIPSnoopingTable_Object = MibTable
hpnicfFCoEFIPSnoopingTable = _HpnicfFCoEFIPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpnicfFCoEFIPSnoopingTable.setStatus("current")
_HpnicfFCoEFIPSnoopingEntry_Object = MibTableRow
hpnicfFCoEFIPSnoopingEntry = _HpnicfFCoEFIPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1)
)
hpnicfFCoEFIPSnoopingEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HPN-ICF-FCOE-MIB", "hpnicfFCoEFIPSnoopingVLANIndex"),
)
if mibBuilder.loadTexts:
    hpnicfFCoEFIPSnoopingEntry.setStatus("current")
_HpnicfFCoEFIPSnoopingVLANIndex_Type = VlanIndex
_HpnicfFCoEFIPSnoopingVLANIndex_Object = MibTableColumn
hpnicfFCoEFIPSnoopingVLANIndex = _HpnicfFCoEFIPSnoopingVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 1),
    _HpnicfFCoEFIPSnoopingVLANIndex_Type()
)
hpnicfFCoEFIPSnoopingVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfFCoEFIPSnoopingVLANIndex.setStatus("current")


class _HpnicfFCoEFIPSnoopingEnable_Type(TruthValue):
    """Custom type hpnicfFCoEFIPSnoopingEnable based on TruthValue"""


_HpnicfFCoEFIPSnoopingEnable_Object = MibTableColumn
hpnicfFCoEFIPSnoopingEnable = _HpnicfFCoEFIPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 2),
    _HpnicfFCoEFIPSnoopingEnable_Type()
)
hpnicfFCoEFIPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoEFIPSnoopingEnable.setStatus("current")


class _HpnicfFCoEFIPSnoopingFcmap_Type(OctetString):
    """Custom type hpnicfFCoEFIPSnoopingFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_HpnicfFCoEFIPSnoopingFcmap_Type.__name__ = "OctetString"
_HpnicfFCoEFIPSnoopingFcmap_Object = MibTableColumn
hpnicfFCoEFIPSnoopingFcmap = _HpnicfFCoEFIPSnoopingFcmap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 120, 1, 1, 4, 1, 3),
    _HpnicfFCoEFIPSnoopingFcmap_Type()
)
hpnicfFCoEFIPSnoopingFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfFCoEFIPSnoopingFcmap.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FCOE-MIB",
    **{"HpnicfFCoEVfcBindType": HpnicfFCoEVfcBindType,
       "hpnicfFCoE": hpnicfFCoE,
       "hpnicfFCoEObjects": hpnicfFCoEObjects,
       "hpnicfFCoEConfig": hpnicfFCoEConfig,
       "hpnicfFCoECfgTable": hpnicfFCoECfgTable,
       "hpnicfFCoECfgEntry": hpnicfFCoECfgEntry,
       "hpnicfFCoECfgFcmap": hpnicfFCoECfgFcmap,
       "hpnicfFCoECfgDynamicVfcCreation": hpnicfFCoECfgDynamicVfcCreation,
       "hpnicfFCoECfgDefaultFCFPriority": hpnicfFCoECfgDefaultFCFPriority,
       "hpnicfFCoECfgDATov": hpnicfFCoECfgDATov,
       "hpnicfFCoECfgAddressingMode": hpnicfFCoECfgAddressingMode,
       "hpnicfFCoEVLANTable": hpnicfFCoEVLANTable,
       "hpnicfFCoEVLANEntry": hpnicfFCoEVLANEntry,
       "hpnicfFCoEVLANIndex": hpnicfFCoEVLANIndex,
       "hpnicfFCoEFabricIndex": hpnicfFCoEFabricIndex,
       "hpnicfFCoEVLANOperState": hpnicfFCoEVLANOperState,
       "hpnicfFCoEVLANRowStatus": hpnicfFCoEVLANRowStatus,
       "hpnicfFCoEStaticVfcTable": hpnicfFCoEStaticVfcTable,
       "hpnicfFCoEStaticVfcEntry": hpnicfFCoEStaticVfcEntry,
       "hpnicfFCoEStaticVfcIndex": hpnicfFCoEStaticVfcIndex,
       "hpnicfFCoEStaticVfcFCFPriority": hpnicfFCoEStaticVfcFCFPriority,
       "hpnicfFCoEStaticVfcBindType": hpnicfFCoEStaticVfcBindType,
       "hpnicfFCoEStaticVfcBindIfIndex": hpnicfFCoEStaticVfcBindIfIndex,
       "hpnicfFCoEStaticVfcBindMACAddress": hpnicfFCoEStaticVfcBindMACAddress,
       "hpnicfFCoEStaticVfcIfIndex": hpnicfFCoEStaticVfcIfIndex,
       "hpnicfFCoEStaticVfcCreationTime": hpnicfFCoEStaticVfcCreationTime,
       "hpnicfFCoEStaticVfcFailureCause": hpnicfFCoEStaticVfcFailureCause,
       "hpnicfFCoEStaticVfcRowStatus": hpnicfFCoEStaticVfcRowStatus,
       "hpnicfFCoEFIPSnoopingTable": hpnicfFCoEFIPSnoopingTable,
       "hpnicfFCoEFIPSnoopingEntry": hpnicfFCoEFIPSnoopingEntry,
       "hpnicfFCoEFIPSnoopingVLANIndex": hpnicfFCoEFIPSnoopingVLANIndex,
       "hpnicfFCoEFIPSnoopingEnable": hpnicfFCoEFIPSnoopingEnable,
       "hpnicfFCoEFIPSnoopingFcmap": hpnicfFCoEFIPSnoopingFcmap}
)
