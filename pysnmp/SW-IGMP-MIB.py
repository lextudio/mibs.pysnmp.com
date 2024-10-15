# SNMP MIB module (SW-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SW-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:58:51 2024
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



class MacAddress(OctetString):
    """Custom type MacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )





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
_Es2000_ObjectIdentity = ObjectIdentity
es2000 = _Es2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 1, 3)
)
_Golfcommon_ObjectIdentity = ObjectIdentity
golfcommon = _Golfcommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2)
)
_Marconi_mgmt_ObjectIdentity = ObjectIdentity
marconi_mgmt = _Marconi_mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2)
)
_Es2000Mgmt_ObjectIdentity = ObjectIdentity
es2000Mgmt = _Es2000Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28)
)
_SwL2Mgmt_ObjectIdentity = ObjectIdentity
swL2Mgmt = _SwL2Mgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2)
)
_SwIGMP_ObjectIdentity = ObjectIdentity
swIGMP = _SwIGMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7)
)
_SwIGMPCtrl_ObjectIdentity = ObjectIdentity
swIGMPCtrl = _SwIGMPCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 1)
)


class _SwIGMPAdminState_Type(Integer32):
    """Custom type swIGMPAdminState based on Integer32"""
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


_SwIGMPAdminState_Type.__name__ = "Integer32"
_SwIGMPAdminState_Object = MibScalar
swIGMPAdminState = _SwIGMPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 1, 1),
    _SwIGMPAdminState_Type()
)
swIGMPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPAdminState.setStatus("mandatory")


class _SwIGMPTimeout_Type(Integer32):
    """Custom type swIGMPTimeout based on Integer32"""
    defaultValue = 300


_SwIGMPTimeout_Object = MibScalar
swIGMPTimeout = _SwIGMPTimeout_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 1, 2),
    _SwIGMPTimeout_Type()
)
swIGMPTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPTimeout.setStatus("mandatory")
_SwIGMPInfoTable_Object = MibTable
swIGMPInfoTable = _SwIGMPInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 2)
)
if mibBuilder.loadTexts:
    swIGMPInfoTable.setStatus("mandatory")
_SwIGMPInfoEntry_Object = MibTableRow
swIGMPInfoEntry = _SwIGMPInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 2, 1)
)
swIGMPInfoEntry.setIndexNames(
    (0, "SW-IGMP-MIB", "swIGMPInfoIndex"),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 2, 1, 1),
    _SwIGMPInfoIndex_Type()
)
swIGMPInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoIndex.setStatus("mandatory")
_SwIGMPInfoVid_Type = Integer32
_SwIGMPInfoVid_Object = MibTableColumn
swIGMPInfoVid = _SwIGMPInfoVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 2, 1, 2),
    _SwIGMPInfoVid_Type()
)
swIGMPInfoVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoVid.setStatus("mandatory")
_SwIGMPInfoQueryCount_Type = Integer32
_SwIGMPInfoQueryCount_Object = MibTableColumn
swIGMPInfoQueryCount = _SwIGMPInfoQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 2, 1, 3),
    _SwIGMPInfoQueryCount_Type()
)
swIGMPInfoQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoQueryCount.setStatus("mandatory")
_SwIGMPInfoTxQueryCount_Type = Integer32
_SwIGMPInfoTxQueryCount_Object = MibTableColumn
swIGMPInfoTxQueryCount = _SwIGMPInfoTxQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 2, 1, 4),
    _SwIGMPInfoTxQueryCount_Type()
)
swIGMPInfoTxQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPInfoTxQueryCount.setStatus("mandatory")
_SwIGMPTable_Object = MibTable
swIGMPTable = _SwIGMPTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3)
)
if mibBuilder.loadTexts:
    swIGMPTable.setStatus("mandatory")
_SwIGMPEntry_Object = MibTableRow
swIGMPEntry = _SwIGMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3, 1)
)
swIGMPEntry.setIndexNames(
    (0, "SW-IGMP-MIB", "swIGMPVid"),
    (0, "SW-IGMP-MIB", "swIGMPGroupIpAddr"),
)
if mibBuilder.loadTexts:
    swIGMPEntry.setStatus("mandatory")
_SwIGMPVid_Type = Integer32
_SwIGMPVid_Object = MibTableColumn
swIGMPVid = _SwIGMPVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3, 1, 1),
    _SwIGMPVid_Type()
)
swIGMPVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPVid.setStatus("mandatory")
_SwIGMPGroupIpAddr_Type = IpAddress
_SwIGMPGroupIpAddr_Object = MibTableColumn
swIGMPGroupIpAddr = _SwIGMPGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3, 1, 2),
    _SwIGMPGroupIpAddr_Type()
)
swIGMPGroupIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPGroupIpAddr.setStatus("mandatory")
_SwIGMPGroupMacAddr_Type = MacAddress
_SwIGMPGroupMacAddr_Object = MibTableColumn
swIGMPGroupMacAddr = _SwIGMPGroupMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3, 1, 3),
    _SwIGMPGroupMacAddr_Type()
)
swIGMPGroupMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPGroupMacAddr.setStatus("mandatory")
_SwIGMPPortMap_Type = PortList
_SwIGMPPortMap_Object = MibTableColumn
swIGMPPortMap = _SwIGMPPortMap_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3, 1, 4),
    _SwIGMPPortMap_Type()
)
swIGMPPortMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPPortMap.setStatus("mandatory")
_SwIGMPIpGroupReportCount_Type = Integer32
_SwIGMPIpGroupReportCount_Object = MibTableColumn
swIGMPIpGroupReportCount = _SwIGMPIpGroupReportCount_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 3, 1, 5),
    _SwIGMPIpGroupReportCount_Type()
)
swIGMPIpGroupReportCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPIpGroupReportCount.setStatus("mandatory")
_SwIGMPCtrlTable_Object = MibTable
swIGMPCtrlTable = _SwIGMPCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 4)
)
if mibBuilder.loadTexts:
    swIGMPCtrlTable.setStatus("mandatory")
_SwIGMPCtrlEntry_Object = MibTableRow
swIGMPCtrlEntry = _SwIGMPCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 4, 1)
)
swIGMPCtrlEntry.setIndexNames(
    (0, "SW-IGMP-MIB", "swIGMPCtrlIndex"),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 4, 1, 1),
    _SwIGMPCtrlIndex_Type()
)
swIGMPCtrlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIGMPCtrlIndex.setStatus("mandatory")


class _SwIGMPCtrlVid_Type(Integer32):
    """Custom type swIGMPCtrlVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwIGMPCtrlVid_Type.__name__ = "Integer32"
_SwIGMPCtrlVid_Object = MibTableColumn
swIGMPCtrlVid = _SwIGMPCtrlVid_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 4, 1, 3),
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
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("deleted", 4),
          ("disabled", 2),
          ("enabled", 3),
          ("other", 1))
    )


_SwIGMPCtrlState_Type.__name__ = "Integer32"
_SwIGMPCtrlState_Object = MibTableColumn
swIGMPCtrlState = _SwIGMPCtrlState_Object(
    (1, 3, 6, 1, 4, 1, 326, 2, 20, 1, 2, 2, 2, 28, 2, 7, 4, 1, 4),
    _SwIGMPCtrlState_Type()
)
swIGMPCtrlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIGMPCtrlState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SW-IGMP-MIB",
    **{"MacAddress": MacAddress,
       "PortList": PortList,
       "marconi": marconi,
       "systems": systems,
       "external": external,
       "dlink": dlink,
       "dlinkcommon": dlinkcommon,
       "golf": golf,
       "golfproducts": golfproducts,
       "es2000": es2000,
       "golfcommon": golfcommon,
       "marconi-mgmt": marconi_mgmt,
       "es2000Mgmt": es2000Mgmt,
       "swL2Mgmt": swL2Mgmt,
       "swIGMP": swIGMP,
       "swIGMPCtrl": swIGMPCtrl,
       "swIGMPAdminState": swIGMPAdminState,
       "swIGMPTimeout": swIGMPTimeout,
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
       "swIGMPGroupMacAddr": swIGMPGroupMacAddr,
       "swIGMPPortMap": swIGMPPortMap,
       "swIGMPIpGroupReportCount": swIGMPIpGroupReportCount,
       "swIGMPCtrlTable": swIGMPCtrlTable,
       "swIGMPCtrlEntry": swIGMPCtrlEntry,
       "swIGMPCtrlIndex": swIGMPCtrlIndex,
       "swIGMPCtrlVid": swIGMPCtrlVid,
       "swIGMPCtrlTimer": swIGMPCtrlTimer,
       "swIGMPCtrlState": swIGMPCtrlState}
)
