# SNMP MIB module (H3C-FCOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/H3C-FCOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:50:32 2024
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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

h3cFCoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120)
)
h3cFCoE.setRevisions(
        ("2012-03-28 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cFCoEVfcBindType(Integer32, TextualConvention):
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

_H3cFCoEObjects_ObjectIdentity = ObjectIdentity
h3cFCoEObjects = _H3cFCoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1)
)
_H3cFCoEConfig_ObjectIdentity = ObjectIdentity
h3cFCoEConfig = _H3cFCoEConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1)
)
_H3cFCoECfgTable_Object = MibTable
h3cFCoECfgTable = _H3cFCoECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFCoECfgTable.setStatus("current")
_H3cFCoECfgEntry_Object = MibTableRow
h3cFCoECfgEntry = _H3cFCoECfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1)
)
h3cFCoECfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoECfgEntry.setStatus("current")


class _H3cFCoECfgFcmap_Type(OctetString):
    """Custom type h3cFCoECfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_H3cFCoECfgFcmap_Type.__name__ = "OctetString"
_H3cFCoECfgFcmap_Object = MibTableColumn
h3cFCoECfgFcmap = _H3cFCoECfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 1),
    _H3cFCoECfgFcmap_Type()
)
h3cFCoECfgFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgFcmap.setStatus("current")


class _H3cFCoECfgDynamicVfcCreation_Type(TruthValue):
    """Custom type h3cFCoECfgDynamicVfcCreation based on TruthValue"""


_H3cFCoECfgDynamicVfcCreation_Object = MibTableColumn
h3cFCoECfgDynamicVfcCreation = _H3cFCoECfgDynamicVfcCreation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 2),
    _H3cFCoECfgDynamicVfcCreation_Type()
)
h3cFCoECfgDynamicVfcCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgDynamicVfcCreation.setStatus("current")


class _H3cFCoECfgDefaultFCFPriority_Type(Unsigned32):
    """Custom type h3cFCoECfgDefaultFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cFCoECfgDefaultFCFPriority_Type.__name__ = "Unsigned32"
_H3cFCoECfgDefaultFCFPriority_Object = MibTableColumn
h3cFCoECfgDefaultFCFPriority = _H3cFCoECfgDefaultFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 3),
    _H3cFCoECfgDefaultFCFPriority_Type()
)
h3cFCoECfgDefaultFCFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgDefaultFCFPriority.setStatus("current")


class _H3cFCoECfgDATov_Type(Unsigned32):
    """Custom type h3cFCoECfgDATov based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_H3cFCoECfgDATov_Type.__name__ = "Unsigned32"
_H3cFCoECfgDATov_Object = MibTableColumn
h3cFCoECfgDATov = _H3cFCoECfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 4),
    _H3cFCoECfgDATov_Type()
)
h3cFCoECfgDATov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    h3cFCoECfgDATov.setUnits("seconds")


class _H3cFCoECfgAddressingMode_Type(Integer32):
    """Custom type h3cFCoECfgAddressingMode based on Integer32"""
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


_H3cFCoECfgAddressingMode_Type.__name__ = "Integer32"
_H3cFCoECfgAddressingMode_Object = MibTableColumn
h3cFCoECfgAddressingMode = _H3cFCoECfgAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 5),
    _H3cFCoECfgAddressingMode_Type()
)
h3cFCoECfgAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgAddressingMode.setStatus("current")
_H3cFCoEVLANTable_Object = MibTable
h3cFCoEVLANTable = _H3cFCoEVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cFCoEVLANTable.setStatus("current")
_H3cFCoEVLANEntry_Object = MibTableRow
h3cFCoEVLANEntry = _H3cFCoEVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1)
)
h3cFCoEVLANEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEVLANIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFabricIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEVLANEntry.setStatus("current")
_H3cFCoEVLANIndex_Type = VlanIndex
_H3cFCoEVLANIndex_Object = MibTableColumn
h3cFCoEVLANIndex = _H3cFCoEVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 1),
    _H3cFCoEVLANIndex_Type()
)
h3cFCoEVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEVLANIndex.setStatus("current")
_H3cFCoEFabricIndex_Type = T11FabricIndex
_H3cFCoEFabricIndex_Object = MibTableColumn
h3cFCoEFabricIndex = _H3cFCoEFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 2),
    _H3cFCoEFabricIndex_Type()
)
h3cFCoEFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFabricIndex.setStatus("current")


class _H3cFCoEVLANOperState_Type(Integer32):
    """Custom type h3cFCoEVLANOperState based on Integer32"""
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


_H3cFCoEVLANOperState_Type.__name__ = "Integer32"
_H3cFCoEVLANOperState_Object = MibTableColumn
h3cFCoEVLANOperState = _H3cFCoEVLANOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 3),
    _H3cFCoEVLANOperState_Type()
)
h3cFCoEVLANOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEVLANOperState.setStatus("current")
_H3cFCoEVLANRowStatus_Type = RowStatus
_H3cFCoEVLANRowStatus_Object = MibTableColumn
h3cFCoEVLANRowStatus = _H3cFCoEVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 4),
    _H3cFCoEVLANRowStatus_Type()
)
h3cFCoEVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEVLANRowStatus.setStatus("current")
_H3cFCoEStaticVfcTable_Object = MibTable
h3cFCoEStaticVfcTable = _H3cFCoEStaticVfcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcTable.setStatus("current")
_H3cFCoEStaticVfcEntry_Object = MibTableRow
h3cFCoEStaticVfcEntry = _H3cFCoEStaticVfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1)
)
h3cFCoEStaticVfcEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEStaticVfcIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcEntry.setStatus("current")


class _H3cFCoEStaticVfcIndex_Type(Unsigned32):
    """Custom type h3cFCoEStaticVfcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cFCoEStaticVfcIndex_Type.__name__ = "Unsigned32"
_H3cFCoEStaticVfcIndex_Object = MibTableColumn
h3cFCoEStaticVfcIndex = _H3cFCoEStaticVfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 1),
    _H3cFCoEStaticVfcIndex_Type()
)
h3cFCoEStaticVfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcIndex.setStatus("current")


class _H3cFCoEStaticVfcFCFPriority_Type(Unsigned32):
    """Custom type h3cFCoEStaticVfcFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cFCoEStaticVfcFCFPriority_Type.__name__ = "Unsigned32"
_H3cFCoEStaticVfcFCFPriority_Object = MibTableColumn
h3cFCoEStaticVfcFCFPriority = _H3cFCoEStaticVfcFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 2),
    _H3cFCoEStaticVfcFCFPriority_Type()
)
h3cFCoEStaticVfcFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcFCFPriority.setStatus("current")
_H3cFCoEStaticVfcBindType_Type = H3cFCoEVfcBindType
_H3cFCoEStaticVfcBindType_Object = MibTableColumn
h3cFCoEStaticVfcBindType = _H3cFCoEStaticVfcBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 3),
    _H3cFCoEStaticVfcBindType_Type()
)
h3cFCoEStaticVfcBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcBindType.setStatus("current")
_H3cFCoEStaticVfcBindIfIndex_Type = InterfaceIndexOrZero
_H3cFCoEStaticVfcBindIfIndex_Object = MibTableColumn
h3cFCoEStaticVfcBindIfIndex = _H3cFCoEStaticVfcBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 4),
    _H3cFCoEStaticVfcBindIfIndex_Type()
)
h3cFCoEStaticVfcBindIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcBindIfIndex.setStatus("current")
_H3cFCoEStaticVfcBindMACAddress_Type = MacAddress
_H3cFCoEStaticVfcBindMACAddress_Object = MibTableColumn
h3cFCoEStaticVfcBindMACAddress = _H3cFCoEStaticVfcBindMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 5),
    _H3cFCoEStaticVfcBindMACAddress_Type()
)
h3cFCoEStaticVfcBindMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcBindMACAddress.setStatus("current")
_H3cFCoEStaticVfcIfIndex_Type = InterfaceIndex
_H3cFCoEStaticVfcIfIndex_Object = MibTableColumn
h3cFCoEStaticVfcIfIndex = _H3cFCoEStaticVfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 6),
    _H3cFCoEStaticVfcIfIndex_Type()
)
h3cFCoEStaticVfcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcIfIndex.setStatus("current")
_H3cFCoEStaticVfcCreationTime_Type = TimeStamp
_H3cFCoEStaticVfcCreationTime_Object = MibTableColumn
h3cFCoEStaticVfcCreationTime = _H3cFCoEStaticVfcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 7),
    _H3cFCoEStaticVfcCreationTime_Type()
)
h3cFCoEStaticVfcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcCreationTime.setStatus("current")
_H3cFCoEStaticVfcFailureCause_Type = SnmpAdminString
_H3cFCoEStaticVfcFailureCause_Object = MibTableColumn
h3cFCoEStaticVfcFailureCause = _H3cFCoEStaticVfcFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 8),
    _H3cFCoEStaticVfcFailureCause_Type()
)
h3cFCoEStaticVfcFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcFailureCause.setStatus("current")
_H3cFCoEStaticVfcRowStatus_Type = RowStatus
_H3cFCoEStaticVfcRowStatus_Object = MibTableColumn
h3cFCoEStaticVfcRowStatus = _H3cFCoEStaticVfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 9),
    _H3cFCoEStaticVfcRowStatus_Type()
)
h3cFCoEStaticVfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcRowStatus.setStatus("current")
_H3cFCoEFIPSnoopingObjects_ObjectIdentity = ObjectIdentity
h3cFCoEFIPSnoopingObjects = _H3cFCoEFIPSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FCOE-MIB",
    **{"H3cFCoEVfcBindType": H3cFCoEVfcBindType,
       "h3cFCoE": h3cFCoE,
       "h3cFCoEObjects": h3cFCoEObjects,
       "h3cFCoEConfig": h3cFCoEConfig,
       "h3cFCoECfgTable": h3cFCoECfgTable,
       "h3cFCoECfgEntry": h3cFCoECfgEntry,
       "h3cFCoECfgFcmap": h3cFCoECfgFcmap,
       "h3cFCoECfgDynamicVfcCreation": h3cFCoECfgDynamicVfcCreation,
       "h3cFCoECfgDefaultFCFPriority": h3cFCoECfgDefaultFCFPriority,
       "h3cFCoECfgDATov": h3cFCoECfgDATov,
       "h3cFCoECfgAddressingMode": h3cFCoECfgAddressingMode,
       "h3cFCoEVLANTable": h3cFCoEVLANTable,
       "h3cFCoEVLANEntry": h3cFCoEVLANEntry,
       "h3cFCoEVLANIndex": h3cFCoEVLANIndex,
       "h3cFCoEFabricIndex": h3cFCoEFabricIndex,
       "h3cFCoEVLANOperState": h3cFCoEVLANOperState,
       "h3cFCoEVLANRowStatus": h3cFCoEVLANRowStatus,
       "h3cFCoEStaticVfcTable": h3cFCoEStaticVfcTable,
       "h3cFCoEStaticVfcEntry": h3cFCoEStaticVfcEntry,
       "h3cFCoEStaticVfcIndex": h3cFCoEStaticVfcIndex,
       "h3cFCoEStaticVfcFCFPriority": h3cFCoEStaticVfcFCFPriority,
       "h3cFCoEStaticVfcBindType": h3cFCoEStaticVfcBindType,
       "h3cFCoEStaticVfcBindIfIndex": h3cFCoEStaticVfcBindIfIndex,
       "h3cFCoEStaticVfcBindMACAddress": h3cFCoEStaticVfcBindMACAddress,
       "h3cFCoEStaticVfcIfIndex": h3cFCoEStaticVfcIfIndex,
       "h3cFCoEStaticVfcCreationTime": h3cFCoEStaticVfcCreationTime,
       "h3cFCoEStaticVfcFailureCause": h3cFCoEStaticVfcFailureCause,
       "h3cFCoEStaticVfcRowStatus": h3cFCoEStaticVfcRowStatus,
       "h3cFCoEFIPSnoopingObjects": h3cFCoEFIPSnoopingObjects}
)
