# SNMP MIB module (HH3C-FCOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-FCOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:22 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cFCoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120)
)
hh3cFCoE.setRevisions(
        ("2012-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class Hh3cFCoEVfcBindType(Integer32, TextualConvention):
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

_Hh3cFCoEObjects_ObjectIdentity = ObjectIdentity
hh3cFCoEObjects = _Hh3cFCoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1)
)
_Hh3cFCoEConfig_ObjectIdentity = ObjectIdentity
hh3cFCoEConfig = _Hh3cFCoEConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1)
)
_Hh3cFCoECfgTable_Object = MibTable
hh3cFCoECfgTable = _Hh3cFCoECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hh3cFCoECfgTable.setStatus("current")
_Hh3cFCoECfgEntry_Object = MibTableRow
hh3cFCoECfgEntry = _Hh3cFCoECfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1)
)
hh3cFCoECfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoECfgEntry.setStatus("current")


class _Hh3cFCoECfgFcmap_Type(OctetString):
    """Custom type hh3cFCoECfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cFCoECfgFcmap_Type.__name__ = "OctetString"
_Hh3cFCoECfgFcmap_Object = MibTableColumn
hh3cFCoECfgFcmap = _Hh3cFCoECfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 1),
    _Hh3cFCoECfgFcmap_Type()
)
hh3cFCoECfgFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgFcmap.setStatus("current")


class _Hh3cFCoECfgDynamicVfcCreation_Type(TruthValue):
    """Custom type hh3cFCoECfgDynamicVfcCreation based on TruthValue"""


_Hh3cFCoECfgDynamicVfcCreation_Object = MibTableColumn
hh3cFCoECfgDynamicVfcCreation = _Hh3cFCoECfgDynamicVfcCreation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 2),
    _Hh3cFCoECfgDynamicVfcCreation_Type()
)
hh3cFCoECfgDynamicVfcCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgDynamicVfcCreation.setStatus("current")


class _Hh3cFCoECfgDefaultFCFPriority_Type(Unsigned32):
    """Custom type hh3cFCoECfgDefaultFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cFCoECfgDefaultFCFPriority_Type.__name__ = "Unsigned32"
_Hh3cFCoECfgDefaultFCFPriority_Object = MibTableColumn
hh3cFCoECfgDefaultFCFPriority = _Hh3cFCoECfgDefaultFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 3),
    _Hh3cFCoECfgDefaultFCFPriority_Type()
)
hh3cFCoECfgDefaultFCFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgDefaultFCFPriority.setStatus("current")


class _Hh3cFCoECfgDATov_Type(Unsigned32):
    """Custom type hh3cFCoECfgDATov based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_Hh3cFCoECfgDATov_Type.__name__ = "Unsigned32"
_Hh3cFCoECfgDATov_Object = MibTableColumn
hh3cFCoECfgDATov = _Hh3cFCoECfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 4),
    _Hh3cFCoECfgDATov_Type()
)
hh3cFCoECfgDATov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    hh3cFCoECfgDATov.setUnits("seconds")


class _Hh3cFCoECfgAddressingMode_Type(Integer32):
    """Custom type hh3cFCoECfgAddressingMode based on Integer32"""
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


_Hh3cFCoECfgAddressingMode_Type.__name__ = "Integer32"
_Hh3cFCoECfgAddressingMode_Object = MibTableColumn
hh3cFCoECfgAddressingMode = _Hh3cFCoECfgAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 1, 1, 5),
    _Hh3cFCoECfgAddressingMode_Type()
)
hh3cFCoECfgAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoECfgAddressingMode.setStatus("current")
_Hh3cFCoEVLANTable_Object = MibTable
hh3cFCoEVLANTable = _Hh3cFCoEVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cFCoEVLANTable.setStatus("current")
_Hh3cFCoEVLANEntry_Object = MibTableRow
hh3cFCoEVLANEntry = _Hh3cFCoEVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1)
)
hh3cFCoEVLANEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEVLANIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFabricIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEVLANEntry.setStatus("current")
_Hh3cFCoEVLANIndex_Type = VlanIndex
_Hh3cFCoEVLANIndex_Object = MibTableColumn
hh3cFCoEVLANIndex = _Hh3cFCoEVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 1),
    _Hh3cFCoEVLANIndex_Type()
)
hh3cFCoEVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEVLANIndex.setStatus("current")
_Hh3cFCoEFabricIndex_Type = T11FabricIndex
_Hh3cFCoEFabricIndex_Object = MibTableColumn
hh3cFCoEFabricIndex = _Hh3cFCoEFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 2),
    _Hh3cFCoEFabricIndex_Type()
)
hh3cFCoEFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFabricIndex.setStatus("current")


class _Hh3cFCoEVLANOperState_Type(Integer32):
    """Custom type hh3cFCoEVLANOperState based on Integer32"""
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


_Hh3cFCoEVLANOperState_Type.__name__ = "Integer32"
_Hh3cFCoEVLANOperState_Object = MibTableColumn
hh3cFCoEVLANOperState = _Hh3cFCoEVLANOperState_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 3),
    _Hh3cFCoEVLANOperState_Type()
)
hh3cFCoEVLANOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEVLANOperState.setStatus("current")
_Hh3cFCoEVLANRowStatus_Type = RowStatus
_Hh3cFCoEVLANRowStatus_Object = MibTableColumn
hh3cFCoEVLANRowStatus = _Hh3cFCoEVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 2, 1, 4),
    _Hh3cFCoEVLANRowStatus_Type()
)
hh3cFCoEVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEVLANRowStatus.setStatus("current")
_Hh3cFCoEStaticVfcTable_Object = MibTable
hh3cFCoEStaticVfcTable = _Hh3cFCoEStaticVfcTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcTable.setStatus("current")
_Hh3cFCoEStaticVfcEntry_Object = MibTableRow
hh3cFCoEStaticVfcEntry = _Hh3cFCoEStaticVfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1)
)
hh3cFCoEStaticVfcEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEStaticVfcIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcEntry.setStatus("current")


class _Hh3cFCoEStaticVfcIndex_Type(Unsigned32):
    """Custom type hh3cFCoEStaticVfcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cFCoEStaticVfcIndex_Type.__name__ = "Unsigned32"
_Hh3cFCoEStaticVfcIndex_Object = MibTableColumn
hh3cFCoEStaticVfcIndex = _Hh3cFCoEStaticVfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 1),
    _Hh3cFCoEStaticVfcIndex_Type()
)
hh3cFCoEStaticVfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcIndex.setStatus("current")


class _Hh3cFCoEStaticVfcFCFPriority_Type(Unsigned32):
    """Custom type hh3cFCoEStaticVfcFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Hh3cFCoEStaticVfcFCFPriority_Type.__name__ = "Unsigned32"
_Hh3cFCoEStaticVfcFCFPriority_Object = MibTableColumn
hh3cFCoEStaticVfcFCFPriority = _Hh3cFCoEStaticVfcFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 2),
    _Hh3cFCoEStaticVfcFCFPriority_Type()
)
hh3cFCoEStaticVfcFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcFCFPriority.setStatus("current")
_Hh3cFCoEStaticVfcBindType_Type = Hh3cFCoEVfcBindType
_Hh3cFCoEStaticVfcBindType_Object = MibTableColumn
hh3cFCoEStaticVfcBindType = _Hh3cFCoEStaticVfcBindType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 3),
    _Hh3cFCoEStaticVfcBindType_Type()
)
hh3cFCoEStaticVfcBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcBindType.setStatus("current")
_Hh3cFCoEStaticVfcBindIfIndex_Type = InterfaceIndexOrZero
_Hh3cFCoEStaticVfcBindIfIndex_Object = MibTableColumn
hh3cFCoEStaticVfcBindIfIndex = _Hh3cFCoEStaticVfcBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 4),
    _Hh3cFCoEStaticVfcBindIfIndex_Type()
)
hh3cFCoEStaticVfcBindIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcBindIfIndex.setStatus("current")
_Hh3cFCoEStaticVfcBindMACAddress_Type = MacAddress
_Hh3cFCoEStaticVfcBindMACAddress_Object = MibTableColumn
hh3cFCoEStaticVfcBindMACAddress = _Hh3cFCoEStaticVfcBindMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 5),
    _Hh3cFCoEStaticVfcBindMACAddress_Type()
)
hh3cFCoEStaticVfcBindMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcBindMACAddress.setStatus("current")
_Hh3cFCoEStaticVfcIfIndex_Type = InterfaceIndex
_Hh3cFCoEStaticVfcIfIndex_Object = MibTableColumn
hh3cFCoEStaticVfcIfIndex = _Hh3cFCoEStaticVfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 6),
    _Hh3cFCoEStaticVfcIfIndex_Type()
)
hh3cFCoEStaticVfcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcIfIndex.setStatus("current")
_Hh3cFCoEStaticVfcCreationTime_Type = TimeStamp
_Hh3cFCoEStaticVfcCreationTime_Object = MibTableColumn
hh3cFCoEStaticVfcCreationTime = _Hh3cFCoEStaticVfcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 7),
    _Hh3cFCoEStaticVfcCreationTime_Type()
)
hh3cFCoEStaticVfcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcCreationTime.setStatus("current")
_Hh3cFCoEStaticVfcFailureCause_Type = SnmpAdminString
_Hh3cFCoEStaticVfcFailureCause_Object = MibTableColumn
hh3cFCoEStaticVfcFailureCause = _Hh3cFCoEStaticVfcFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 8),
    _Hh3cFCoEStaticVfcFailureCause_Type()
)
hh3cFCoEStaticVfcFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcFailureCause.setStatus("current")
_Hh3cFCoEStaticVfcRowStatus_Type = RowStatus
_Hh3cFCoEStaticVfcRowStatus_Object = MibTableColumn
hh3cFCoEStaticVfcRowStatus = _Hh3cFCoEStaticVfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 3, 1, 9),
    _Hh3cFCoEStaticVfcRowStatus_Type()
)
hh3cFCoEStaticVfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cFCoEStaticVfcRowStatus.setStatus("current")
_Hh3cFCoEFIPSnoopingTable_Object = MibTable
hh3cFCoEFIPSnoopingTable = _Hh3cFCoEFIPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingTable.setStatus("current")
_Hh3cFCoEFIPSnoopingEntry_Object = MibTableRow
hh3cFCoEFIPSnoopingEntry = _Hh3cFCoEFIPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1)
)
hh3cFCoEFIPSnoopingEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "HH3C-FCOE-MIB", "hh3cFCoEFIPSnoopingVLANIndex"),
)
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingEntry.setStatus("current")
_Hh3cFCoEFIPSnoopingVLANIndex_Type = VlanIndex
_Hh3cFCoEFIPSnoopingVLANIndex_Object = MibTableColumn
hh3cFCoEFIPSnoopingVLANIndex = _Hh3cFCoEFIPSnoopingVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 1),
    _Hh3cFCoEFIPSnoopingVLANIndex_Type()
)
hh3cFCoEFIPSnoopingVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingVLANIndex.setStatus("current")


class _Hh3cFCoEFIPSnoopingEnable_Type(TruthValue):
    """Custom type hh3cFCoEFIPSnoopingEnable based on TruthValue"""


_Hh3cFCoEFIPSnoopingEnable_Object = MibTableColumn
hh3cFCoEFIPSnoopingEnable = _Hh3cFCoEFIPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 2),
    _Hh3cFCoEFIPSnoopingEnable_Type()
)
hh3cFCoEFIPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingEnable.setStatus("current")


class _Hh3cFCoEFIPSnoopingFcmap_Type(OctetString):
    """Custom type hh3cFCoEFIPSnoopingFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_Hh3cFCoEFIPSnoopingFcmap_Type.__name__ = "OctetString"
_Hh3cFCoEFIPSnoopingFcmap_Object = MibTableColumn
hh3cFCoEFIPSnoopingFcmap = _Hh3cFCoEFIPSnoopingFcmap_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 120, 1, 1, 4, 1, 3),
    _Hh3cFCoEFIPSnoopingFcmap_Type()
)
hh3cFCoEFIPSnoopingFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cFCoEFIPSnoopingFcmap.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-FCOE-MIB",
    **{"Hh3cFCoEVfcBindType": Hh3cFCoEVfcBindType,
       "hh3cFCoE": hh3cFCoE,
       "hh3cFCoEObjects": hh3cFCoEObjects,
       "hh3cFCoEConfig": hh3cFCoEConfig,
       "hh3cFCoECfgTable": hh3cFCoECfgTable,
       "hh3cFCoECfgEntry": hh3cFCoECfgEntry,
       "hh3cFCoECfgFcmap": hh3cFCoECfgFcmap,
       "hh3cFCoECfgDynamicVfcCreation": hh3cFCoECfgDynamicVfcCreation,
       "hh3cFCoECfgDefaultFCFPriority": hh3cFCoECfgDefaultFCFPriority,
       "hh3cFCoECfgDATov": hh3cFCoECfgDATov,
       "hh3cFCoECfgAddressingMode": hh3cFCoECfgAddressingMode,
       "hh3cFCoEVLANTable": hh3cFCoEVLANTable,
       "hh3cFCoEVLANEntry": hh3cFCoEVLANEntry,
       "hh3cFCoEVLANIndex": hh3cFCoEVLANIndex,
       "hh3cFCoEFabricIndex": hh3cFCoEFabricIndex,
       "hh3cFCoEVLANOperState": hh3cFCoEVLANOperState,
       "hh3cFCoEVLANRowStatus": hh3cFCoEVLANRowStatus,
       "hh3cFCoEStaticVfcTable": hh3cFCoEStaticVfcTable,
       "hh3cFCoEStaticVfcEntry": hh3cFCoEStaticVfcEntry,
       "hh3cFCoEStaticVfcIndex": hh3cFCoEStaticVfcIndex,
       "hh3cFCoEStaticVfcFCFPriority": hh3cFCoEStaticVfcFCFPriority,
       "hh3cFCoEStaticVfcBindType": hh3cFCoEStaticVfcBindType,
       "hh3cFCoEStaticVfcBindIfIndex": hh3cFCoEStaticVfcBindIfIndex,
       "hh3cFCoEStaticVfcBindMACAddress": hh3cFCoEStaticVfcBindMACAddress,
       "hh3cFCoEStaticVfcIfIndex": hh3cFCoEStaticVfcIfIndex,
       "hh3cFCoEStaticVfcCreationTime": hh3cFCoEStaticVfcCreationTime,
       "hh3cFCoEStaticVfcFailureCause": hh3cFCoEStaticVfcFailureCause,
       "hh3cFCoEStaticVfcRowStatus": hh3cFCoEStaticVfcRowStatus,
       "hh3cFCoEFIPSnoopingTable": hh3cFCoEFIPSnoopingTable,
       "hh3cFCoEFIPSnoopingEntry": hh3cFCoEFIPSnoopingEntry,
       "hh3cFCoEFIPSnoopingVLANIndex": hh3cFCoEFIPSnoopingVLANIndex,
       "hh3cFCoEFIPSnoopingEnable": hh3cFCoEFIPSnoopingEnable,
       "hh3cFCoEFIPSnoopingFcmap": hh3cFCoEFIPSnoopingFcmap}
)
