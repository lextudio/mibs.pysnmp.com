# SNMP MIB module (TRUNK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRUNK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:50 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Marconi_ObjectIdentity = ObjectIdentity
marconi = _Marconi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326)
)
_Systems_ObjectIdentity = ObjectIdentity
systems = _Systems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2)
)
_External_ObjectIdentity = ObjectIdentity
external = _External_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20)
)
_Dlink_ObjectIdentity = ObjectIdentity
dlink = _Dlink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1)
)
_Dlinkcommon_ObjectIdentity = ObjectIdentity
dlinkcommon = _Dlinkcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 1)
)
_Golf_ObjectIdentity = ObjectIdentity
golf = _Golf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2)
)
_Golfproducts_ObjectIdentity = ObjectIdentity
golfproducts = _Golfproducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es1000Series_ObjectIdentity = ObjectIdentity
es1000Series = _Es1000Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24)
)
_SwPortTrunkPackage_ObjectIdentity = ObjectIdentity
swPortTrunkPackage = _SwPortTrunkPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6)
)
_SwPortTrunkTable_Object = MibTable
swPortTrunkTable = _SwPortTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1)
)
if mibBuilder.loadTexts:
    swPortTrunkTable.setStatus("mandatory")
_SwPortTrunkEntry_Object = MibTableRow
swPortTrunkEntry = _SwPortTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1)
)
swPortTrunkEntry.setIndexNames(
    (0, "TRUNK-MIB", "swPortTrunkIndex"),
)
if mibBuilder.loadTexts:
    swPortTrunkEntry.setStatus("mandatory")
_SwPortTrunkIndex_Type = Integer32
_SwPortTrunkIndex_Object = MibTableColumn
swPortTrunkIndex = _SwPortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1, 1),
    _SwPortTrunkIndex_Type()
)
swPortTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkIndex.setStatus("mandatory")


class _SwPortTrunkName_Type(DisplayString):
    """Custom type swPortTrunkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SwPortTrunkName_Type.__name__ = "DisplayString"
_SwPortTrunkName_Object = MibTableColumn
swPortTrunkName = _SwPortTrunkName_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1, 2),
    _SwPortTrunkName_Type()
)
swPortTrunkName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkName.setStatus("mandatory")
_SwPortTrunkModule_Type = Integer32
_SwPortTrunkModule_Object = MibTableColumn
swPortTrunkModule = _SwPortTrunkModule_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1, 3),
    _SwPortTrunkModule_Type()
)
swPortTrunkModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkModule.setStatus("mandatory")
_SwPortTrunkMasterPort_Type = Integer32
_SwPortTrunkMasterPort_Object = MibTableColumn
swPortTrunkMasterPort = _SwPortTrunkMasterPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1, 4),
    _SwPortTrunkMasterPort_Type()
)
swPortTrunkMasterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortTrunkMasterPort.setStatus("mandatory")
_SwPortTrunkMemberNum_Type = Integer32
_SwPortTrunkMemberNum_Object = MibTableColumn
swPortTrunkMemberNum = _SwPortTrunkMemberNum_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1, 5),
    _SwPortTrunkMemberNum_Type()
)
swPortTrunkMemberNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkMemberNum.setStatus("mandatory")


class _SwPortTrunkState_Type(Integer32):
    """Custom type swPortTrunkState based on Integer32"""
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
          ("other", 1))
    )


_SwPortTrunkState_Type.__name__ = "Integer32"
_SwPortTrunkState_Object = MibTableColumn
swPortTrunkState = _SwPortTrunkState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 6, 1, 1, 6),
    _SwPortTrunkState_Type()
)
swPortTrunkState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swPortTrunkState.setStatus("mandatory")
_SwSnoopPackage_ObjectIdentity = ObjectIdentity
swSnoopPackage = _SwSnoopPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7)
)
_SwSnoopCtrlTable_Object = MibTable
swSnoopCtrlTable = _SwSnoopCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7, 1)
)
if mibBuilder.loadTexts:
    swSnoopCtrlTable.setStatus("mandatory")
_SwSnoopCtrlEntry_Object = MibTableRow
swSnoopCtrlEntry = _SwSnoopCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7, 1, 1)
)
swSnoopCtrlEntry.setIndexNames(
    (0, "TRUNK-MIB", "swSnoopIndex"),
)
if mibBuilder.loadTexts:
    swSnoopCtrlEntry.setStatus("mandatory")
_SwSnoopIndex_Type = Integer32
_SwSnoopIndex_Object = MibTableColumn
swSnoopIndex = _SwSnoopIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7, 1, 1, 1),
    _SwSnoopIndex_Type()
)
swSnoopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSnoopIndex.setStatus("mandatory")
_SwSnoopLogicSourcePort_Type = Integer32
_SwSnoopLogicSourcePort_Object = MibTableColumn
swSnoopLogicSourcePort = _SwSnoopLogicSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7, 1, 1, 2),
    _SwSnoopLogicSourcePort_Type()
)
swSnoopLogicSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSnoopLogicSourcePort.setStatus("mandatory")
_SwSnoopLogicTargetPort_Type = Integer32
_SwSnoopLogicTargetPort_Object = MibTableColumn
swSnoopLogicTargetPort = _SwSnoopLogicTargetPort_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7, 1, 1, 3),
    _SwSnoopLogicTargetPort_Type()
)
swSnoopLogicTargetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSnoopLogicTargetPort.setStatus("mandatory")


class _SwSnoopState_Type(Integer32):
    """Custom type swSnoopState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwSnoopState_Type.__name__ = "Integer32"
_SwSnoopState_Object = MibTableColumn
swSnoopState = _SwSnoopState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 7, 1, 1, 4),
    _SwSnoopState_Type()
)
swSnoopState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSnoopState.setStatus("mandatory")
_SwIGMPPackage_ObjectIdentity = ObjectIdentity
swIGMPPackage = _SwIGMPPackage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8)
)
_SwIGMPCtrlTable_Object = MibTable
swIGMPCtrlTable = _SwIGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 1)
)
if mibBuilder.loadTexts:
    swIGMPCtrlTable.setStatus("mandatory")
_SwIGMPCtrlEntry_Object = MibTableRow
swIGMPCtrlEntry = _SwIGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 1, 1)
)
swIGMPCtrlEntry.setIndexNames(
    (0, "TRUNK-MIB", "swIGMPCtrlIndex"),
)
if mibBuilder.loadTexts:
    swIGMPCtrlEntry.setStatus("mandatory")


class _SwIGMPCtrlIndex_Type(Integer32):
    """Custom type swIGMPCtrlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwIGMPCtrlIndex_Type.__name__ = "Integer32"
_SwIGMPCtrlIndex_Object = MibTableColumn
swIGMPCtrlIndex = _SwIGMPCtrlIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 1, 1, 1),
    _SwIGMPCtrlIndex_Type()
)
swIGMPCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPCtrlIndex.setStatus("mandatory")
_SwIGMPCtrlVid_Type = Integer32
_SwIGMPCtrlVid_Object = MibTableColumn
swIGMPCtrlVid = _SwIGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 1, 1, 2),
    _SwIGMPCtrlVid_Type()
)
swIGMPCtrlVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlVid.setStatus("mandatory")


class _SwIGMPCtrlTimer_Type(Integer32):
    """Custom type swIGMPCtrlTimer based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 9999),
    )


_SwIGMPCtrlTimer_Type.__name__ = "Integer32"
_SwIGMPCtrlTimer_Object = MibTableColumn
swIGMPCtrlTimer = _SwIGMPCtrlTimer_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 1, 1, 3),
    _SwIGMPCtrlTimer_Type()
)
swIGMPCtrlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlTimer.setStatus("mandatory")


class _SwIGMPCtrlState_Type(Integer32):
    """Custom type swIGMPCtrlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 3),
          ("other", 1))
    )


_SwIGMPCtrlState_Type.__name__ = "Integer32"
_SwIGMPCtrlState_Object = MibTableColumn
swIGMPCtrlState = _SwIGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 1, 1, 4),
    _SwIGMPCtrlState_Type()
)
swIGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlState.setStatus("mandatory")
_SwIGMPInfoTable_Object = MibTable
swIGMPInfoTable = _SwIGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 2)
)
if mibBuilder.loadTexts:
    swIGMPInfoTable.setStatus("mandatory")
_SwIGMPInfoEntry_Object = MibTableRow
swIGMPInfoEntry = _SwIGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 2, 1)
)
swIGMPInfoEntry.setIndexNames(
    (0, "TRUNK-MIB", "swIGMPInfoIndex"),
)
if mibBuilder.loadTexts:
    swIGMPInfoEntry.setStatus("mandatory")


class _SwIGMPInfoIndex_Type(Integer32):
    """Custom type swIGMPInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SwIGMPInfoIndex_Type.__name__ = "Integer32"
_SwIGMPInfoIndex_Object = MibTableColumn
swIGMPInfoIndex = _SwIGMPInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 2, 1, 1),
    _SwIGMPInfoIndex_Type()
)
swIGMPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoIndex.setStatus("mandatory")
_SwIGMPInfoVid_Type = Integer32
_SwIGMPInfoVid_Object = MibTableColumn
swIGMPInfoVid = _SwIGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 2, 1, 2),
    _SwIGMPInfoVid_Type()
)
swIGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoVid.setStatus("mandatory")
_SwIGMPInfoQueryCount_Type = Integer32
_SwIGMPInfoQueryCount_Object = MibTableColumn
swIGMPInfoQueryCount = _SwIGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 2, 1, 3),
    _SwIGMPInfoQueryCount_Type()
)
swIGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoQueryCount.setStatus("mandatory")
_SwIGMPInfoTxQueryCount_Type = Integer32
_SwIGMPInfoTxQueryCount_Object = MibTableColumn
swIGMPInfoTxQueryCount = _SwIGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 2, 1, 4),
    _SwIGMPInfoTxQueryCount_Type()
)
swIGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoTxQueryCount.setStatus("mandatory")
_SwIGMPTable_Object = MibTable
swIGMPTable = _SwIGMPTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3)
)
if mibBuilder.loadTexts:
    swIGMPTable.setStatus("mandatory")
_SwIGMPEntry_Object = MibTableRow
swIGMPEntry = _SwIGMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3, 1)
)
swIGMPEntry.setIndexNames(
    (0, "TRUNK-MIB", "swIGMPVid"),
    (0, "TRUNK-MIB", "swIGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPEntry.setStatus("mandatory")
_SwIGMPVid_Type = Integer32
_SwIGMPVid_Object = MibTableColumn
swIGMPVid = _SwIGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3, 1, 1),
    _SwIGMPVid_Type()
)
swIGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPVid.setStatus("mandatory")
_SwIGMPGroupIpAddr_Type = IpAddress
_SwIGMPGroupIpAddr_Object = MibTableColumn
swIGMPGroupIpAddr = _SwIGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3, 1, 2),
    _SwIGMPGroupIpAddr_Type()
)
swIGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPGroupIpAddr.setStatus("mandatory")
_SwIGMPMacAddr_Type = MacAddress
_SwIGMPMacAddr_Object = MibTableColumn
swIGMPMacAddr = _SwIGMPMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3, 1, 3),
    _SwIGMPMacAddr_Type()
)
swIGMPMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPMacAddr.setStatus("mandatory")
_SwIGMPPortMap_Type = PortList
_SwIGMPPortMap_Object = MibTableColumn
swIGMPPortMap = _SwIGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3, 1, 4),
    _SwIGMPPortMap_Type()
)
swIGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPPortMap.setStatus("mandatory")
_SwIGMPIpGroupReportCount_Type = Integer32
_SwIGMPIpGroupReportCount_Object = MibTableColumn
swIGMPIpGroupReportCount = _SwIGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 8, 3, 1, 5),
    _SwIGMPIpGroupReportCount_Type()
)
swIGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPIpGroupReportCount.setStatus("mandatory")
_EndOfMIB_Type = Integer32
_EndOfMIB_Object = MibScalar
endOfMIB = _EndOfMIB_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 24, 9999),
    _EndOfMIB_Type()
)
endOfMIB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfMIB.setStatus("optional")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRUNK-MIB",
    **{"PortList": PortList,
       "marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "golfcommon": golfcommon,
       "marconi-mgmt": marconi_mgmt,
       "es1000Series": es1000Series,
       "swPortTrunkPackage": swPortTrunkPackage,
       "swPortTrunkTable": swPortTrunkTable,
       "swPortTrunkEntry": swPortTrunkEntry,
       "swPortTrunkIndex": swPortTrunkIndex,
       "swPortTrunkName": swPortTrunkName,
       "swPortTrunkModule": swPortTrunkModule,
       "swPortTrunkMasterPort": swPortTrunkMasterPort,
       "swPortTrunkMemberNum": swPortTrunkMemberNum,
       "swPortTrunkState": swPortTrunkState,
       "swSnoopPackage": swSnoopPackage,
       "swSnoopCtrlTable": swSnoopCtrlTable,
       "swSnoopCtrlEntry": swSnoopCtrlEntry,
       "swSnoopIndex": swSnoopIndex,
       "swSnoopLogicSourcePort": swSnoopLogicSourcePort,
       "swSnoopLogicTargetPort": swSnoopLogicTargetPort,
       "swSnoopState": swSnoopState,
       "swIGMPPackage": swIGMPPackage,
       "swIGMPCtrlTable": swIGMPCtrlTable,
       "swIGMPCtrlEntry": swIGMPCtrlEntry,
       "swIGMPCtrlIndex": swIGMPCtrlIndex,
       "swIGMPCtrlVid": swIGMPCtrlVid,
       "swIGMPCtrlTimer": swIGMPCtrlTimer,
       "swIGMPCtrlState": swIGMPCtrlState,
       "swIGMPInfoTable": swIGMPInfoTable,
       "swIGMPInfoEntry": swIGMPInfoEntry,
       "swIGMPInfoIndex": swIGMPInfoIndex,
       "swIGMPInfoVid": swIGMPInfoVid,
       "swIGMPInfoQueryCount": swIGMPInfoQueryCount,
       "swIGMPInfoTxQueryCount": swIGMPInfoTxQueryCount,
       "swIGMPTable": swIGMPTable,
       "swIGMPEntry": swIGMPEntry,
       "swIGMPVid": swIGMPVid,
       "swIGMPGroupIpAddr": swIGMPGroupIpAddr,
       "swIGMPMacAddr": swIGMPMacAddr,
       "swIGMPPortMap": swIGMPPortMap,
       "swIGMPIpGroupReportCount": swIGMPIpGroupReportCount,
       "endOfMIB": endOfMIB}
)
