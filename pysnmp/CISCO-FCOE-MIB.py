# SNMP MIB module (CISCO-FCOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FCOE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:25 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(fcmInstanceIndex,
 fcmSwitchIndex) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "fcmInstanceIndex",
    "fcmSwitchIndex")

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

ciscoFCoEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673)
)
ciscoFCoEMIB.setRevisions(
        ("2008-06-16 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VfcBindType(Integer32, TextualConvention):
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

_CiscoFCoEMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFCoEMIBObjects = _CiscoFCoEMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1)
)
_CfcoeConfig_ObjectIdentity = ObjectIdentity
cfcoeConfig = _CfcoeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1)
)
_CfcoeCfgTable_Object = MibTable
cfcoeCfgTable = _CfcoeCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfcoeCfgTable.setStatus("current")
_CfcoeCfgEntry_Object = MibTableRow
cfcoeCfgEntry = _CfcoeCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1)
)
cfcoeCfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
)
if mibBuilder.loadTexts:
    cfcoeCfgEntry.setStatus("current")


class _CfcoeCfgFcmap_Type(OctetString):
    """Custom type cfcoeCfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CfcoeCfgFcmap_Type.__name__ = "OctetString"
_CfcoeCfgFcmap_Object = MibTableColumn
cfcoeCfgFcmap = _CfcoeCfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 1),
    _CfcoeCfgFcmap_Type()
)
cfcoeCfgFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeCfgFcmap.setStatus("current")


class _CfcoeCfgDynamicVfcCreation_Type(TruthValue):
    """Custom type cfcoeCfgDynamicVfcCreation based on TruthValue"""


_CfcoeCfgDynamicVfcCreation_Object = MibTableColumn
cfcoeCfgDynamicVfcCreation = _CfcoeCfgDynamicVfcCreation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 2),
    _CfcoeCfgDynamicVfcCreation_Type()
)
cfcoeCfgDynamicVfcCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeCfgDynamicVfcCreation.setStatus("current")


class _CfcoeCfgDynamicVfcAgeTimer_Type(Unsigned32):
    """Custom type cfcoeCfgDynamicVfcAgeTimer based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_CfcoeCfgDynamicVfcAgeTimer_Type.__name__ = "Unsigned32"
_CfcoeCfgDynamicVfcAgeTimer_Object = MibTableColumn
cfcoeCfgDynamicVfcAgeTimer = _CfcoeCfgDynamicVfcAgeTimer_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 3),
    _CfcoeCfgDynamicVfcAgeTimer_Type()
)
cfcoeCfgDynamicVfcAgeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeCfgDynamicVfcAgeTimer.setStatus("current")


class _CfcoeCfgDefaultFCFPriority_Type(Unsigned32):
    """Custom type cfcoeCfgDefaultFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfcoeCfgDefaultFCFPriority_Type.__name__ = "Unsigned32"
_CfcoeCfgDefaultFCFPriority_Object = MibTableColumn
cfcoeCfgDefaultFCFPriority = _CfcoeCfgDefaultFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 4),
    _CfcoeCfgDefaultFCFPriority_Type()
)
cfcoeCfgDefaultFCFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeCfgDefaultFCFPriority.setStatus("current")


class _CfcoeCfgDATov_Type(Unsigned32):
    """Custom type cfcoeCfgDATov based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CfcoeCfgDATov_Type.__name__ = "Unsigned32"
_CfcoeCfgDATov_Object = MibTableColumn
cfcoeCfgDATov = _CfcoeCfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 5),
    _CfcoeCfgDATov_Type()
)
cfcoeCfgDATov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeCfgDATov.setStatus("current")


class _CfcoeCfgAddressingMode_Type(Integer32):
    """Custom type cfcoeCfgAddressingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("fpma", 1),
          ("spma", 2))
    )


_CfcoeCfgAddressingMode_Type.__name__ = "Integer32"
_CfcoeCfgAddressingMode_Object = MibTableColumn
cfcoeCfgAddressingMode = _CfcoeCfgAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 1, 1, 6),
    _CfcoeCfgAddressingMode_Type()
)
cfcoeCfgAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeCfgAddressingMode.setStatus("current")
_CfcoeVLANTable_Object = MibTable
cfcoeVLANTable = _CfcoeVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfcoeVLANTable.setStatus("current")
_CfcoeVLANEntry_Object = MibTableRow
cfcoeVLANEntry = _CfcoeVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1)
)
cfcoeVLANEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "CISCO-FCOE-MIB", "cfcoeVLANIndex"),
    (0, "CISCO-FCOE-MIB", "cfcoeFabricIndex"),
)
if mibBuilder.loadTexts:
    cfcoeVLANEntry.setStatus("current")
_CfcoeVLANIndex_Type = VlanIndex
_CfcoeVLANIndex_Object = MibTableColumn
cfcoeVLANIndex = _CfcoeVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 1),
    _CfcoeVLANIndex_Type()
)
cfcoeVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcoeVLANIndex.setStatus("current")
_CfcoeFabricIndex_Type = T11FabricIndex
_CfcoeFabricIndex_Object = MibTableColumn
cfcoeFabricIndex = _CfcoeFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 2),
    _CfcoeFabricIndex_Type()
)
cfcoeFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcoeFabricIndex.setStatus("current")


class _CfcoeVLANOperState_Type(Integer32):
    """Custom type cfcoeVLANOperState based on Integer32"""
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


_CfcoeVLANOperState_Type.__name__ = "Integer32"
_CfcoeVLANOperState_Object = MibTableColumn
cfcoeVLANOperState = _CfcoeVLANOperState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 3),
    _CfcoeVLANOperState_Type()
)
cfcoeVLANOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcoeVLANOperState.setStatus("current")
_CfcoeVLANRowStatus_Type = RowStatus
_CfcoeVLANRowStatus_Object = MibTableColumn
cfcoeVLANRowStatus = _CfcoeVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 2, 1, 4),
    _CfcoeVLANRowStatus_Type()
)
cfcoeVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeVLANRowStatus.setStatus("current")
_CfcoeStaticVfcTable_Object = MibTable
cfcoeStaticVfcTable = _CfcoeStaticVfcTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfcoeStaticVfcTable.setStatus("current")
_CfcoeStaticVfcEntry_Object = MibTableRow
cfcoeStaticVfcEntry = _CfcoeStaticVfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1)
)
cfcoeStaticVfcEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "FC-MGMT-MIB", "fcmSwitchIndex"),
    (0, "CISCO-FCOE-MIB", "cfcoeStaticVfcIndex"),
)
if mibBuilder.loadTexts:
    cfcoeStaticVfcEntry.setStatus("current")


class _CfcoeStaticVfcIndex_Type(Unsigned32):
    """Custom type cfcoeStaticVfcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CfcoeStaticVfcIndex_Type.__name__ = "Unsigned32"
_CfcoeStaticVfcIndex_Object = MibTableColumn
cfcoeStaticVfcIndex = _CfcoeStaticVfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 1),
    _CfcoeStaticVfcIndex_Type()
)
cfcoeStaticVfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcoeStaticVfcIndex.setStatus("current")


class _CfcoeStaticVfcFCFPriority_Type(Unsigned32):
    """Custom type cfcoeStaticVfcFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CfcoeStaticVfcFCFPriority_Type.__name__ = "Unsigned32"
_CfcoeStaticVfcFCFPriority_Object = MibTableColumn
cfcoeStaticVfcFCFPriority = _CfcoeStaticVfcFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 2),
    _CfcoeStaticVfcFCFPriority_Type()
)
cfcoeStaticVfcFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeStaticVfcFCFPriority.setStatus("current")
_CfcoeStaticVfcBindType_Type = VfcBindType
_CfcoeStaticVfcBindType_Object = MibTableColumn
cfcoeStaticVfcBindType = _CfcoeStaticVfcBindType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 3),
    _CfcoeStaticVfcBindType_Type()
)
cfcoeStaticVfcBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeStaticVfcBindType.setStatus("current")
_CfcoeStaticVfcBindIfIndex_Type = InterfaceIndexOrZero
_CfcoeStaticVfcBindIfIndex_Object = MibTableColumn
cfcoeStaticVfcBindIfIndex = _CfcoeStaticVfcBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 4),
    _CfcoeStaticVfcBindIfIndex_Type()
)
cfcoeStaticVfcBindIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeStaticVfcBindIfIndex.setStatus("current")
_CfcoeStaticVfcBindMACAddress_Type = MacAddress
_CfcoeStaticVfcBindMACAddress_Object = MibTableColumn
cfcoeStaticVfcBindMACAddress = _CfcoeStaticVfcBindMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 5),
    _CfcoeStaticVfcBindMACAddress_Type()
)
cfcoeStaticVfcBindMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeStaticVfcBindMACAddress.setStatus("current")
_CfcoeStaticVfcIfIndex_Type = InterfaceIndex
_CfcoeStaticVfcIfIndex_Object = MibTableColumn
cfcoeStaticVfcIfIndex = _CfcoeStaticVfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 6),
    _CfcoeStaticVfcIfIndex_Type()
)
cfcoeStaticVfcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcoeStaticVfcIfIndex.setStatus("current")
_CfcoeStaticVfcCreationTime_Type = TimeStamp
_CfcoeStaticVfcCreationTime_Object = MibTableColumn
cfcoeStaticVfcCreationTime = _CfcoeStaticVfcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 7),
    _CfcoeStaticVfcCreationTime_Type()
)
cfcoeStaticVfcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcoeStaticVfcCreationTime.setStatus("current")
_CfcoeStaticVfcFailureCause_Type = SnmpAdminString
_CfcoeStaticVfcFailureCause_Object = MibTableColumn
cfcoeStaticVfcFailureCause = _CfcoeStaticVfcFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 8),
    _CfcoeStaticVfcFailureCause_Type()
)
cfcoeStaticVfcFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcoeStaticVfcFailureCause.setStatus("current")
_CfcoeStaticVfcRowStatus_Type = RowStatus
_CfcoeStaticVfcRowStatus_Object = MibTableColumn
cfcoeStaticVfcRowStatus = _CfcoeStaticVfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 1, 3, 1, 9),
    _CfcoeStaticVfcRowStatus_Type()
)
cfcoeStaticVfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeStaticVfcRowStatus.setStatus("current")
_CfcoeFipSnoopingObjects_ObjectIdentity = ObjectIdentity
cfcoeFipSnoopingObjects = _CfcoeFipSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2)
)


class _CfcoeFipSnoopingEnable_Type(Integer32):
    """Custom type cfcoeFipSnoopingEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_CfcoeFipSnoopingEnable_Type.__name__ = "Integer32"
_CfcoeFipSnoopingEnable_Object = MibScalar
cfcoeFipSnoopingEnable = _CfcoeFipSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 1),
    _CfcoeFipSnoopingEnable_Type()
)
cfcoeFipSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeFipSnoopingEnable.setStatus("current")


class _CfcoeFipSnoopingFcmap_Type(OctetString):
    """Custom type cfcoeFipSnoopingFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_CfcoeFipSnoopingFcmap_Type.__name__ = "OctetString"
_CfcoeFipSnoopingFcmap_Object = MibScalar
cfcoeFipSnoopingFcmap = _CfcoeFipSnoopingFcmap_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 2),
    _CfcoeFipSnoopingFcmap_Type()
)
cfcoeFipSnoopingFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfcoeFipSnoopingFcmap.setStatus("current")
_CfcoeEnodeIntfTable_Object = MibTable
cfcoeEnodeIntfTable = _CfcoeEnodeIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfcoeEnodeIntfTable.setStatus("current")
_CfcoeEnodeIntfEntry_Object = MibTableRow
cfcoeEnodeIntfEntry = _CfcoeEnodeIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3, 1)
)
cfcoeEnodeIntfEntry.setIndexNames(
    (0, "CISCO-FCOE-MIB", "cfcoeEnodeIntfIfIndex"),
)
if mibBuilder.loadTexts:
    cfcoeEnodeIntfEntry.setStatus("current")
_CfcoeEnodeIntfIfIndex_Type = InterfaceIndex
_CfcoeEnodeIntfIfIndex_Object = MibTableColumn
cfcoeEnodeIntfIfIndex = _CfcoeEnodeIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3, 1, 1),
    _CfcoeEnodeIntfIfIndex_Type()
)
cfcoeEnodeIntfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcoeEnodeIntfIfIndex.setStatus("current")
_CfcoeEnodeIntfRowStatus_Type = RowStatus
_CfcoeEnodeIntfRowStatus_Object = MibTableColumn
cfcoeEnodeIntfRowStatus = _CfcoeEnodeIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 1, 2, 3, 1, 2),
    _CfcoeEnodeIntfRowStatus_Type()
)
cfcoeEnodeIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfcoeEnodeIntfRowStatus.setStatus("current")
_CiscoFCoEMIBConformance_ObjectIdentity = ObjectIdentity
ciscoFCoEMIBConformance = _CiscoFCoEMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2)
)
_CFCoEMIBCompliances_ObjectIdentity = ObjectIdentity
cFCoEMIBCompliances = _CFCoEMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 1)
)
_CFCoEMIBGroups_ObjectIdentity = ObjectIdentity
cFCoEMIBGroups = _CFCoEMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2)
)

# Managed Objects groups

cfcoeCfgConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 1)
)
cfcoeCfgConformanceObjects.setObjects(
      *(("CISCO-FCOE-MIB", "cfcoeCfgFcmap"),
        ("CISCO-FCOE-MIB", "cfcoeCfgDynamicVfcCreation"),
        ("CISCO-FCOE-MIB", "cfcoeCfgDynamicVfcAgeTimer"),
        ("CISCO-FCOE-MIB", "cfcoeCfgDefaultFCFPriority"),
        ("CISCO-FCOE-MIB", "cfcoeCfgDATov"),
        ("CISCO-FCOE-MIB", "cfcoeCfgAddressingMode"))
)
if mibBuilder.loadTexts:
    cfcoeCfgConformanceObjects.setStatus("current")

cfcoeVLANConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 2)
)
cfcoeVLANConformanceObjects.setObjects(
      *(("CISCO-FCOE-MIB", "cfcoeVLANOperState"),
        ("CISCO-FCOE-MIB", "cfcoeVLANRowStatus"))
)
if mibBuilder.loadTexts:
    cfcoeVLANConformanceObjects.setStatus("current")

cfcoeStaticVfcConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 3)
)
cfcoeStaticVfcConformanceObjects.setObjects(
      *(("CISCO-FCOE-MIB", "cfcoeStaticVfcFCFPriority"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcBindType"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcBindIfIndex"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcBindMACAddress"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcIfIndex"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcCreationTime"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcFailureCause"),
        ("CISCO-FCOE-MIB", "cfcoeStaticVfcRowStatus"))
)
if mibBuilder.loadTexts:
    cfcoeStaticVfcConformanceObjects.setStatus("current")

cfcoeFipSnoopingConformanceObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 4)
)
cfcoeFipSnoopingConformanceObjects.setObjects(
      *(("CISCO-FCOE-MIB", "cfcoeFipSnoopingEnable"),
        ("CISCO-FCOE-MIB", "cfcoeFipSnoopingFcmap"))
)
if mibBuilder.loadTexts:
    cfcoeFipSnoopingConformanceObjects.setStatus("current")

cfcoeEnodeIntfObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 2, 5)
)
cfcoeEnodeIntfObjects.setObjects(
    ("CISCO-FCOE-MIB", "cfcoeEnodeIntfRowStatus")
)
if mibBuilder.loadTexts:
    cfcoeEnodeIntfObjects.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cFCoEMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 673, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cFCoEMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FCOE-MIB",
    **{"VfcBindType": VfcBindType,
       "ciscoFCoEMIB": ciscoFCoEMIB,
       "ciscoFCoEMIBObjects": ciscoFCoEMIBObjects,
       "cfcoeConfig": cfcoeConfig,
       "cfcoeCfgTable": cfcoeCfgTable,
       "cfcoeCfgEntry": cfcoeCfgEntry,
       "cfcoeCfgFcmap": cfcoeCfgFcmap,
       "cfcoeCfgDynamicVfcCreation": cfcoeCfgDynamicVfcCreation,
       "cfcoeCfgDynamicVfcAgeTimer": cfcoeCfgDynamicVfcAgeTimer,
       "cfcoeCfgDefaultFCFPriority": cfcoeCfgDefaultFCFPriority,
       "cfcoeCfgDATov": cfcoeCfgDATov,
       "cfcoeCfgAddressingMode": cfcoeCfgAddressingMode,
       "cfcoeVLANTable": cfcoeVLANTable,
       "cfcoeVLANEntry": cfcoeVLANEntry,
       "cfcoeVLANIndex": cfcoeVLANIndex,
       "cfcoeFabricIndex": cfcoeFabricIndex,
       "cfcoeVLANOperState": cfcoeVLANOperState,
       "cfcoeVLANRowStatus": cfcoeVLANRowStatus,
       "cfcoeStaticVfcTable": cfcoeStaticVfcTable,
       "cfcoeStaticVfcEntry": cfcoeStaticVfcEntry,
       "cfcoeStaticVfcIndex": cfcoeStaticVfcIndex,
       "cfcoeStaticVfcFCFPriority": cfcoeStaticVfcFCFPriority,
       "cfcoeStaticVfcBindType": cfcoeStaticVfcBindType,
       "cfcoeStaticVfcBindIfIndex": cfcoeStaticVfcBindIfIndex,
       "cfcoeStaticVfcBindMACAddress": cfcoeStaticVfcBindMACAddress,
       "cfcoeStaticVfcIfIndex": cfcoeStaticVfcIfIndex,
       "cfcoeStaticVfcCreationTime": cfcoeStaticVfcCreationTime,
       "cfcoeStaticVfcFailureCause": cfcoeStaticVfcFailureCause,
       "cfcoeStaticVfcRowStatus": cfcoeStaticVfcRowStatus,
       "cfcoeFipSnoopingObjects": cfcoeFipSnoopingObjects,
       "cfcoeFipSnoopingEnable": cfcoeFipSnoopingEnable,
       "cfcoeFipSnoopingFcmap": cfcoeFipSnoopingFcmap,
       "cfcoeEnodeIntfTable": cfcoeEnodeIntfTable,
       "cfcoeEnodeIntfEntry": cfcoeEnodeIntfEntry,
       "cfcoeEnodeIntfIfIndex": cfcoeEnodeIntfIfIndex,
       "cfcoeEnodeIntfRowStatus": cfcoeEnodeIntfRowStatus,
       "ciscoFCoEMIBConformance": ciscoFCoEMIBConformance,
       "cFCoEMIBCompliances": cFCoEMIBCompliances,
       "cFCoEMIBCompliance": cFCoEMIBCompliance,
       "cFCoEMIBGroups": cFCoEMIBGroups,
       "cfcoeCfgConformanceObjects": cfcoeCfgConformanceObjects,
       "cfcoeVLANConformanceObjects": cfcoeVLANConformanceObjects,
       "cfcoeStaticVfcConformanceObjects": cfcoeStaticVfcConformanceObjects,
       "cfcoeFipSnoopingConformanceObjects": cfcoeFipSnoopingConformanceObjects,
       "cfcoeEnodeIntfObjects": cfcoeEnodeIntfObjects}
)
