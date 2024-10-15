# SNMP MIB module (IPMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/IPMS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:10:57 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(xylanIpmsArch,) = mibBuilder.importSymbols(
    "XYLAN-BASE-MIB",
    "xylanIpmsArch")


# MODULE-IDENTITY


# Types definitions



class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpmsMIB_ObjectIdentity = ObjectIdentity
ipmsMIB = _IpmsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1)
)
_IpmsMIBObjects_ObjectIdentity = ObjectIdentity
ipmsMIBObjects = _IpmsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1)
)
_IpmsGeneralGroup_ObjectIdentity = ObjectIdentity
ipmsGeneralGroup = _IpmsGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 1)
)
_IpmsVersion_Type = DisplayString
_IpmsVersion_Object = MibScalar
ipmsVersion = _IpmsVersion_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 1, 1),
    _IpmsVersion_Type()
)
ipmsVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsVersion.setStatus("mandatory")


class _IpmsState_Type(Integer32):
    """Custom type ipmsState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_IpmsState_Type.__name__ = "Integer32"
_IpmsState_Object = MibScalar
ipmsState = _IpmsState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 1, 2),
    _IpmsState_Type()
)
ipmsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmsState.setStatus("mandatory")
_IpmsDIPAddressPortTable_Object = MibTable
ipmsDIPAddressPortTable = _IpmsDIPAddressPortTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ipmsDIPAddressPortTable.setStatus("mandatory")
_IpmsDIPAddressPortEntry_Object = MibTableRow
ipmsDIPAddressPortEntry = _IpmsDIPAddressPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1)
)
ipmsDIPAddressPortEntry.setIndexNames(
    (0, "IPMS-MIB", "ipmsDIPAddress"),
    (0, "IPMS-MIB", "ipmsDIPDstVlan"),
    (0, "IPMS-MIB", "ipmsDIPSlotNumber"),
    (0, "IPMS-MIB", "ipmsDIPPortNumber"),
    (0, "IPMS-MIB", "ipmsDIPPortInstance"),
    (0, "IPMS-MIB", "ipmsDIPPortService"),
)
if mibBuilder.loadTexts:
    ipmsDIPAddressPortEntry.setStatus("mandatory")
_IpmsDIPAddress_Type = IpAddress
_IpmsDIPAddress_Object = MibTableColumn
ipmsDIPAddress = _IpmsDIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 1),
    _IpmsDIPAddress_Type()
)
ipmsDIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPAddress.setStatus("mandatory")
_IpmsDIPDstVlan_Type = Integer32
_IpmsDIPDstVlan_Object = MibTableColumn
ipmsDIPDstVlan = _IpmsDIPDstVlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 2),
    _IpmsDIPDstVlan_Type()
)
ipmsDIPDstVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPDstVlan.setStatus("mandatory")
_IpmsDIPDstVlanMask_Type = Integer32
_IpmsDIPDstVlanMask_Object = MibTableColumn
ipmsDIPDstVlanMask = _IpmsDIPDstVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 3),
    _IpmsDIPDstVlanMask_Type()
)
ipmsDIPDstVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPDstVlanMask.setStatus("mandatory")
_IpmsDIPSlotNumber_Type = Integer32
_IpmsDIPSlotNumber_Object = MibTableColumn
ipmsDIPSlotNumber = _IpmsDIPSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 4),
    _IpmsDIPSlotNumber_Type()
)
ipmsDIPSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPSlotNumber.setStatus("mandatory")
_IpmsDIPPortNumber_Type = Integer32
_IpmsDIPPortNumber_Object = MibTableColumn
ipmsDIPPortNumber = _IpmsDIPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 5),
    _IpmsDIPPortNumber_Type()
)
ipmsDIPPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPPortNumber.setStatus("mandatory")
_IpmsDIPPortType_Type = Integer32
_IpmsDIPPortType_Object = MibTableColumn
ipmsDIPPortType = _IpmsDIPPortType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 6),
    _IpmsDIPPortType_Type()
)
ipmsDIPPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPPortType.setStatus("mandatory")
_IpmsDIPPortInstance_Type = Integer32
_IpmsDIPPortInstance_Object = MibTableColumn
ipmsDIPPortInstance = _IpmsDIPPortInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 7),
    _IpmsDIPPortInstance_Type()
)
ipmsDIPPortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPPortInstance.setStatus("mandatory")
_IpmsDIPPortService_Type = Integer32
_IpmsDIPPortService_Object = MibTableColumn
ipmsDIPPortService = _IpmsDIPPortService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 8),
    _IpmsDIPPortService_Type()
)
ipmsDIPPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPPortService.setStatus("mandatory")
_IpmsDIPSrcIPAddr_Type = IpAddress
_IpmsDIPSrcIPAddr_Object = MibTableColumn
ipmsDIPSrcIPAddr = _IpmsDIPSrcIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 9),
    _IpmsDIPSrcIPAddr_Type()
)
ipmsDIPSrcIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPSrcIPAddr.setStatus("mandatory")
_IpmsDIPPortTimeout_Type = Integer32
_IpmsDIPPortTimeout_Object = MibTableColumn
ipmsDIPPortTimeout = _IpmsDIPPortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 2, 1, 10),
    _IpmsDIPPortTimeout_Type()
)
ipmsDIPPortTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsDIPPortTimeout.setStatus("mandatory")
_IpmsNeighborTable_Object = MibTable
ipmsNeighborTable = _IpmsNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ipmsNeighborTable.setStatus("mandatory")
_IpmsNeighborTableEntry_Object = MibTableRow
ipmsNeighborTableEntry = _IpmsNeighborTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1)
)
ipmsNeighborTableEntry.setIndexNames(
    (0, "IPMS-MIB", "ipmsNbrVlanID"),
    (0, "IPMS-MIB", "ipmsNbrSIPAddress"),
)
if mibBuilder.loadTexts:
    ipmsNeighborTableEntry.setStatus("mandatory")
_IpmsNbrVlanID_Type = Integer32
_IpmsNbrVlanID_Object = MibTableColumn
ipmsNbrVlanID = _IpmsNbrVlanID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 1),
    _IpmsNbrVlanID_Type()
)
ipmsNbrVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrVlanID.setStatus("mandatory")
_IpmsNbrVlanMask_Type = Integer32
_IpmsNbrVlanMask_Object = MibTableColumn
ipmsNbrVlanMask = _IpmsNbrVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 2),
    _IpmsNbrVlanMask_Type()
)
ipmsNbrVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrVlanMask.setStatus("mandatory")
_IpmsNbrSIPAddress_Type = IpAddress
_IpmsNbrSIPAddress_Object = MibTableColumn
ipmsNbrSIPAddress = _IpmsNbrSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 3),
    _IpmsNbrSIPAddress_Type()
)
ipmsNbrSIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrSIPAddress.setStatus("mandatory")
_IpmsNbrSlotNumber_Type = Integer32
_IpmsNbrSlotNumber_Object = MibTableColumn
ipmsNbrSlotNumber = _IpmsNbrSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 4),
    _IpmsNbrSlotNumber_Type()
)
ipmsNbrSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrSlotNumber.setStatus("mandatory")
_IpmsNbrPortNumber_Type = Integer32
_IpmsNbrPortNumber_Object = MibTableColumn
ipmsNbrPortNumber = _IpmsNbrPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 5),
    _IpmsNbrPortNumber_Type()
)
ipmsNbrPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrPortNumber.setStatus("mandatory")
_IpmsNbrPortType_Type = Integer32
_IpmsNbrPortType_Object = MibTableColumn
ipmsNbrPortType = _IpmsNbrPortType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 6),
    _IpmsNbrPortType_Type()
)
ipmsNbrPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrPortType.setStatus("mandatory")
_IpmsNbrPortInstance_Type = Integer32
_IpmsNbrPortInstance_Object = MibTableColumn
ipmsNbrPortInstance = _IpmsNbrPortInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 7),
    _IpmsNbrPortInstance_Type()
)
ipmsNbrPortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrPortInstance.setStatus("mandatory")
_IpmsNbrPortService_Type = Integer32
_IpmsNbrPortService_Object = MibTableColumn
ipmsNbrPortService = _IpmsNbrPortService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 8),
    _IpmsNbrPortService_Type()
)
ipmsNbrPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrPortService.setStatus("mandatory")
_IpmsNbrPortTimeout_Type = Integer32
_IpmsNbrPortTimeout_Object = MibTableColumn
ipmsNbrPortTimeout = _IpmsNbrPortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 3, 1, 9),
    _IpmsNbrPortTimeout_Type()
)
ipmsNbrPortTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsNbrPortTimeout.setStatus("mandatory")
_IpmsStatsTable_Object = MibTable
ipmsStatsTable = _IpmsStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipmsStatsTable.setStatus("mandatory")
_IpmsStatsEntry_Object = MibTableRow
ipmsStatsEntry = _IpmsStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1)
)
ipmsStatsEntry.setIndexNames(
    (0, "IPMS-MIB", "ipmsStatsDIPAddress"),
    (0, "IPMS-MIB", "ipmsStatsSIPAddress"),
    (0, "IPMS-MIB", "ipmsStatsVlanID"),
)
if mibBuilder.loadTexts:
    ipmsStatsEntry.setStatus("mandatory")
_IpmsStatsDIPAddress_Type = IpAddress
_IpmsStatsDIPAddress_Object = MibTableColumn
ipmsStatsDIPAddress = _IpmsStatsDIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 1),
    _IpmsStatsDIPAddress_Type()
)
ipmsStatsDIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsDIPAddress.setStatus("mandatory")
_IpmsStatsSIPAddress_Type = IpAddress
_IpmsStatsSIPAddress_Object = MibTableColumn
ipmsStatsSIPAddress = _IpmsStatsSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 2),
    _IpmsStatsSIPAddress_Type()
)
ipmsStatsSIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsSIPAddress.setStatus("mandatory")
_IpmsStatsVlanID_Type = Integer32
_IpmsStatsVlanID_Object = MibTableColumn
ipmsStatsVlanID = _IpmsStatsVlanID_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 3),
    _IpmsStatsVlanID_Type()
)
ipmsStatsVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsVlanID.setStatus("mandatory")
_IpmsStatsVlanMask_Type = Integer32
_IpmsStatsVlanMask_Object = MibTableColumn
ipmsStatsVlanMask = _IpmsStatsVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 4),
    _IpmsStatsVlanMask_Type()
)
ipmsStatsVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsVlanMask.setStatus("mandatory")
_IpmsStatsPacketsOut_Type = Integer32
_IpmsStatsPacketsOut_Object = MibTableColumn
ipmsStatsPacketsOut = _IpmsStatsPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 5),
    _IpmsStatsPacketsOut_Type()
)
ipmsStatsPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsPacketsOut.setStatus("mandatory")
_IpmsStatsSecsSinceZeroed_Type = Integer32
_IpmsStatsSecsSinceZeroed_Object = MibTableColumn
ipmsStatsSecsSinceZeroed = _IpmsStatsSecsSinceZeroed_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 6),
    _IpmsStatsSecsSinceZeroed_Type()
)
ipmsStatsSecsSinceZeroed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsSecsSinceZeroed.setStatus("mandatory")
_IpmsStatsAveragePPS_Type = Integer32
_IpmsStatsAveragePPS_Object = MibTableColumn
ipmsStatsAveragePPS = _IpmsStatsAveragePPS_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 4, 1, 7),
    _IpmsStatsAveragePPS_Type()
)
ipmsStatsAveragePPS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsStatsAveragePPS.setStatus("mandatory")
_IpmsZeroStatsGroup_ObjectIdentity = ObjectIdentity
ipmsZeroStatsGroup = _IpmsZeroStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 5)
)


class _IpmsZeroStatsFlag_Type(Integer32):
    """Custom type ipmsZeroStatsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("zeroStats", 1)
    )


_IpmsZeroStatsFlag_Type.__name__ = "Integer32"
_IpmsZeroStatsFlag_Object = MibScalar
ipmsZeroStatsFlag = _IpmsZeroStatsFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 5, 1),
    _IpmsZeroStatsFlag_Type()
)
ipmsZeroStatsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmsZeroStatsFlag.setStatus("mandatory")
_IpmsForwardingTable_Object = MibTable
ipmsForwardingTable = _IpmsForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipmsForwardingTable.setStatus("mandatory")
_IpmsFwdTableEntry_Object = MibTableRow
ipmsFwdTableEntry = _IpmsFwdTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1)
)
ipmsFwdTableEntry.setIndexNames(
    (0, "IPMS-MIB", "ipmsFwdDestIP"),
    (0, "IPMS-MIB", "ipmsFwdSourceIP"),
    (0, "IPMS-MIB", "ipmsFwdEntryType"),
    (0, "IPMS-MIB", "ipmsFwdSrcVlan"),
    (0, "IPMS-MIB", "ipmsFwdDstSlotNumber"),
    (0, "IPMS-MIB", "ipmsFwdDstPortNumber"),
    (0, "IPMS-MIB", "ipmsFwdDstPortInstance"),
    (0, "IPMS-MIB", "ipmsFwdDstPortService"),
)
if mibBuilder.loadTexts:
    ipmsFwdTableEntry.setStatus("mandatory")
_IpmsFwdDestIP_Type = IpAddress
_IpmsFwdDestIP_Object = MibTableColumn
ipmsFwdDestIP = _IpmsFwdDestIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 1),
    _IpmsFwdDestIP_Type()
)
ipmsFwdDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDestIP.setStatus("mandatory")
_IpmsFwdSourceIP_Type = IpAddress
_IpmsFwdSourceIP_Object = MibTableColumn
ipmsFwdSourceIP = _IpmsFwdSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 2),
    _IpmsFwdSourceIP_Type()
)
ipmsFwdSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSourceIP.setStatus("mandatory")


class _IpmsFwdEntryType_Type(Integer32):
    """Custom type ipmsFwdEntryType based on Integer32"""
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
        *(("routed", 4),
          ("switched", 1),
          ("switchedError", 2),
          ("switchedPrimary", 3))
    )


_IpmsFwdEntryType_Type.__name__ = "Integer32"
_IpmsFwdEntryType_Object = MibTableColumn
ipmsFwdEntryType = _IpmsFwdEntryType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 3),
    _IpmsFwdEntryType_Type()
)
ipmsFwdEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdEntryType.setStatus("mandatory")
_IpmsFwdSrcVlan_Type = Integer32
_IpmsFwdSrcVlan_Object = MibTableColumn
ipmsFwdSrcVlan = _IpmsFwdSrcVlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 4),
    _IpmsFwdSrcVlan_Type()
)
ipmsFwdSrcVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcVlan.setStatus("mandatory")
_IpmsFwdSrcVlanMask_Type = Integer32
_IpmsFwdSrcVlanMask_Object = MibTableColumn
ipmsFwdSrcVlanMask = _IpmsFwdSrcVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 5),
    _IpmsFwdSrcVlanMask_Type()
)
ipmsFwdSrcVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcVlanMask.setStatus("mandatory")
_IpmsFwdSrcSlotNumber_Type = Integer32
_IpmsFwdSrcSlotNumber_Object = MibTableColumn
ipmsFwdSrcSlotNumber = _IpmsFwdSrcSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 6),
    _IpmsFwdSrcSlotNumber_Type()
)
ipmsFwdSrcSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcSlotNumber.setStatus("mandatory")
_IpmsFwdSrcPortNumber_Type = Integer32
_IpmsFwdSrcPortNumber_Object = MibTableColumn
ipmsFwdSrcPortNumber = _IpmsFwdSrcPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 7),
    _IpmsFwdSrcPortNumber_Type()
)
ipmsFwdSrcPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcPortNumber.setStatus("mandatory")
_IpmsFwdSrcPortType_Type = Integer32
_IpmsFwdSrcPortType_Object = MibTableColumn
ipmsFwdSrcPortType = _IpmsFwdSrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 8),
    _IpmsFwdSrcPortType_Type()
)
ipmsFwdSrcPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcPortType.setStatus("mandatory")
_IpmsFwdSrcPortInstance_Type = Integer32
_IpmsFwdSrcPortInstance_Object = MibTableColumn
ipmsFwdSrcPortInstance = _IpmsFwdSrcPortInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 9),
    _IpmsFwdSrcPortInstance_Type()
)
ipmsFwdSrcPortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcPortInstance.setStatus("mandatory")
_IpmsFwdSrcPortService_Type = Integer32
_IpmsFwdSrcPortService_Object = MibTableColumn
ipmsFwdSrcPortService = _IpmsFwdSrcPortService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 10),
    _IpmsFwdSrcPortService_Type()
)
ipmsFwdSrcPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdSrcPortService.setStatus("mandatory")
_IpmsFwdDstVlan_Type = Integer32
_IpmsFwdDstVlan_Object = MibTableColumn
ipmsFwdDstVlan = _IpmsFwdDstVlan_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 11),
    _IpmsFwdDstVlan_Type()
)
ipmsFwdDstVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstVlan.setStatus("mandatory")
_IpmsFwdDstVlanMask_Type = Integer32
_IpmsFwdDstVlanMask_Object = MibTableColumn
ipmsFwdDstVlanMask = _IpmsFwdDstVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 12),
    _IpmsFwdDstVlanMask_Type()
)
ipmsFwdDstVlanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstVlanMask.setStatus("mandatory")
_IpmsFwdDstSlotNumber_Type = Integer32
_IpmsFwdDstSlotNumber_Object = MibTableColumn
ipmsFwdDstSlotNumber = _IpmsFwdDstSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 13),
    _IpmsFwdDstSlotNumber_Type()
)
ipmsFwdDstSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstSlotNumber.setStatus("mandatory")
_IpmsFwdDstPortNumber_Type = Integer32
_IpmsFwdDstPortNumber_Object = MibTableColumn
ipmsFwdDstPortNumber = _IpmsFwdDstPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 14),
    _IpmsFwdDstPortNumber_Type()
)
ipmsFwdDstPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortNumber.setStatus("mandatory")
_IpmsFwdDstPortType_Type = Integer32
_IpmsFwdDstPortType_Object = MibTableColumn
ipmsFwdDstPortType = _IpmsFwdDstPortType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 15),
    _IpmsFwdDstPortType_Type()
)
ipmsFwdDstPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortType.setStatus("mandatory")
_IpmsFwdDstPortInstance_Type = Integer32
_IpmsFwdDstPortInstance_Object = MibTableColumn
ipmsFwdDstPortInstance = _IpmsFwdDstPortInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 16),
    _IpmsFwdDstPortInstance_Type()
)
ipmsFwdDstPortInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortInstance.setStatus("mandatory")
_IpmsFwdDstPortService_Type = Integer32
_IpmsFwdDstPortService_Object = MibTableColumn
ipmsFwdDstPortService = _IpmsFwdDstPortService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 17),
    _IpmsFwdDstPortService_Type()
)
ipmsFwdDstPortService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortService.setStatus("mandatory")


class _IpmsFwdDstPortMbrFlag_Type(Integer32):
    """Custom type ipmsFwdDstPortMbrFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("membershipNotRequested", 2),
          ("membershipRequested", 1))
    )


_IpmsFwdDstPortMbrFlag_Type.__name__ = "Integer32"
_IpmsFwdDstPortMbrFlag_Object = MibTableColumn
ipmsFwdDstPortMbrFlag = _IpmsFwdDstPortMbrFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 18),
    _IpmsFwdDstPortMbrFlag_Type()
)
ipmsFwdDstPortMbrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortMbrFlag.setStatus("mandatory")


class _IpmsFwdDstPortNbrFlag_Type(Integer32):
    """Custom type ipmsFwdDstPortNbrFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portIsNeighbor", 1),
          ("portIsNotNeighbor", 2))
    )


_IpmsFwdDstPortNbrFlag_Type.__name__ = "Integer32"
_IpmsFwdDstPortNbrFlag_Object = MibTableColumn
ipmsFwdDstPortNbrFlag = _IpmsFwdDstPortNbrFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 19),
    _IpmsFwdDstPortNbrFlag_Type()
)
ipmsFwdDstPortNbrFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortNbrFlag.setStatus("mandatory")


class _IpmsFwdDstPortRteFlag_Type(Integer32):
    """Custom type ipmsFwdDstPortRteFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portIsNotRouted", 2),
          ("portIsRouted", 1))
    )


_IpmsFwdDstPortRteFlag_Type.__name__ = "Integer32"
_IpmsFwdDstPortRteFlag_Object = MibTableColumn
ipmsFwdDstPortRteFlag = _IpmsFwdDstPortRteFlag_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 6, 1, 20),
    _IpmsFwdDstPortRteFlag_Type()
)
ipmsFwdDstPortRteFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsFwdDstPortRteFlag.setStatus("mandatory")
_IpmsPolManParameters_ObjectIdentity = ObjectIdentity
ipmsPolManParameters = _IpmsPolManParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7)
)


class _IpmsPolManDefaultPolicy_Type(Integer32):
    """Custom type ipmsPolManDefaultPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denied", 2),
          ("permitted", 1))
    )


_IpmsPolManDefaultPolicy_Type.__name__ = "Integer32"
_IpmsPolManDefaultPolicy_Object = MibScalar
ipmsPolManDefaultPolicy = _IpmsPolManDefaultPolicy_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7, 1),
    _IpmsPolManDefaultPolicy_Type()
)
ipmsPolManDefaultPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmsPolManDefaultPolicy.setStatus("mandatory")
_IpmsPolManActiveTimer_Type = Integer32
_IpmsPolManActiveTimer_Object = MibScalar
ipmsPolManActiveTimer = _IpmsPolManActiveTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7, 2),
    _IpmsPolManActiveTimer_Type()
)
ipmsPolManActiveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmsPolManActiveTimer.setStatus("mandatory")
_IpmsPolManDeleteTimer_Type = Integer32
_IpmsPolManDeleteTimer_Object = MibScalar
ipmsPolManDeleteTimer = _IpmsPolManDeleteTimer_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 7, 3),
    _IpmsPolManDeleteTimer_Type()
)
ipmsPolManDeleteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipmsPolManDeleteTimer.setStatus("mandatory")
_IpmsPolManCacheTable_Object = MibTable
ipmsPolManCacheTable = _IpmsPolManCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8)
)
if mibBuilder.loadTexts:
    ipmsPolManCacheTable.setStatus("mandatory")
_IpmsPolManCacheTableEntry_Object = MibTableRow
ipmsPolManCacheTableEntry = _IpmsPolManCacheTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1)
)
ipmsPolManCacheTableEntry.setIndexNames(
    (0, "IPMS-MIB", "ipmsPolManMCGroup"),
    (0, "IPMS-MIB", "ipmsPolManSlot"),
    (0, "IPMS-MIB", "ipmsPolManPort"),
    (0, "IPMS-MIB", "ipmsPolManType"),
    (0, "IPMS-MIB", "ipmsPolManInstance"),
    (0, "IPMS-MIB", "ipmsPolManService"),
)
if mibBuilder.loadTexts:
    ipmsPolManCacheTableEntry.setStatus("mandatory")
_IpmsPolManMCGroup_Type = IpAddress
_IpmsPolManMCGroup_Object = MibTableColumn
ipmsPolManMCGroup = _IpmsPolManMCGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 1),
    _IpmsPolManMCGroup_Type()
)
ipmsPolManMCGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManMCGroup.setStatus("mandatory")
_IpmsPolManSlot_Type = Integer32
_IpmsPolManSlot_Object = MibTableColumn
ipmsPolManSlot = _IpmsPolManSlot_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 2),
    _IpmsPolManSlot_Type()
)
ipmsPolManSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManSlot.setStatus("mandatory")
_IpmsPolManPort_Type = Integer32
_IpmsPolManPort_Object = MibTableColumn
ipmsPolManPort = _IpmsPolManPort_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 3),
    _IpmsPolManPort_Type()
)
ipmsPolManPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManPort.setStatus("mandatory")
_IpmsPolManType_Type = Integer32
_IpmsPolManType_Object = MibTableColumn
ipmsPolManType = _IpmsPolManType_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 4),
    _IpmsPolManType_Type()
)
ipmsPolManType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManType.setStatus("mandatory")
_IpmsPolManInstance_Type = Integer32
_IpmsPolManInstance_Object = MibTableColumn
ipmsPolManInstance = _IpmsPolManInstance_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 5),
    _IpmsPolManInstance_Type()
)
ipmsPolManInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManInstance.setStatus("mandatory")
_IpmsPolManService_Type = Integer32
_IpmsPolManService_Object = MibTableColumn
ipmsPolManService = _IpmsPolManService_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 6),
    _IpmsPolManService_Type()
)
ipmsPolManService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManService.setStatus("mandatory")
_IpmsPolManVlanGroup_Type = Integer32
_IpmsPolManVlanGroup_Object = MibTableColumn
ipmsPolManVlanGroup = _IpmsPolManVlanGroup_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 7),
    _IpmsPolManVlanGroup_Type()
)
ipmsPolManVlanGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManVlanGroup.setStatus("mandatory")


class _IpmsPolManStatus_Type(Integer32):
    """Custom type ipmsPolManStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("denied", 2),
          ("permitted", 1))
    )


_IpmsPolManStatus_Type.__name__ = "Integer32"
_IpmsPolManStatus_Object = MibTableColumn
ipmsPolManStatus = _IpmsPolManStatus_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 8),
    _IpmsPolManStatus_Type()
)
ipmsPolManStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManStatus.setStatus("mandatory")


class _IpmsPolManState_Type(Integer32):
    """Custom type ipmsPolManState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("stale", 2))
    )


_IpmsPolManState_Type.__name__ = "Integer32"
_IpmsPolManState_Object = MibTableColumn
ipmsPolManState = _IpmsPolManState_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 9),
    _IpmsPolManState_Type()
)
ipmsPolManState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManState.setStatus("mandatory")
_IpmsPolManTimeout_Type = Integer32
_IpmsPolManTimeout_Object = MibTableColumn
ipmsPolManTimeout = _IpmsPolManTimeout_Object(
    (1, 3, 6, 1, 4, 1, 800, 2, 14, 1, 1, 8, 1, 10),
    _IpmsPolManTimeout_Type()
)
ipmsPolManTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmsPolManTimeout.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPMS-MIB",
    **{"DisplayString": DisplayString,
       "ipmsMIB": ipmsMIB,
       "ipmsMIBObjects": ipmsMIBObjects,
       "ipmsGeneralGroup": ipmsGeneralGroup,
       "ipmsVersion": ipmsVersion,
       "ipmsState": ipmsState,
       "ipmsDIPAddressPortTable": ipmsDIPAddressPortTable,
       "ipmsDIPAddressPortEntry": ipmsDIPAddressPortEntry,
       "ipmsDIPAddress": ipmsDIPAddress,
       "ipmsDIPDstVlan": ipmsDIPDstVlan,
       "ipmsDIPDstVlanMask": ipmsDIPDstVlanMask,
       "ipmsDIPSlotNumber": ipmsDIPSlotNumber,
       "ipmsDIPPortNumber": ipmsDIPPortNumber,
       "ipmsDIPPortType": ipmsDIPPortType,
       "ipmsDIPPortInstance": ipmsDIPPortInstance,
       "ipmsDIPPortService": ipmsDIPPortService,
       "ipmsDIPSrcIPAddr": ipmsDIPSrcIPAddr,
       "ipmsDIPPortTimeout": ipmsDIPPortTimeout,
       "ipmsNeighborTable": ipmsNeighborTable,
       "ipmsNeighborTableEntry": ipmsNeighborTableEntry,
       "ipmsNbrVlanID": ipmsNbrVlanID,
       "ipmsNbrVlanMask": ipmsNbrVlanMask,
       "ipmsNbrSIPAddress": ipmsNbrSIPAddress,
       "ipmsNbrSlotNumber": ipmsNbrSlotNumber,
       "ipmsNbrPortNumber": ipmsNbrPortNumber,
       "ipmsNbrPortType": ipmsNbrPortType,
       "ipmsNbrPortInstance": ipmsNbrPortInstance,
       "ipmsNbrPortService": ipmsNbrPortService,
       "ipmsNbrPortTimeout": ipmsNbrPortTimeout,
       "ipmsStatsTable": ipmsStatsTable,
       "ipmsStatsEntry": ipmsStatsEntry,
       "ipmsStatsDIPAddress": ipmsStatsDIPAddress,
       "ipmsStatsSIPAddress": ipmsStatsSIPAddress,
       "ipmsStatsVlanID": ipmsStatsVlanID,
       "ipmsStatsVlanMask": ipmsStatsVlanMask,
       "ipmsStatsPacketsOut": ipmsStatsPacketsOut,
       "ipmsStatsSecsSinceZeroed": ipmsStatsSecsSinceZeroed,
       "ipmsStatsAveragePPS": ipmsStatsAveragePPS,
       "ipmsZeroStatsGroup": ipmsZeroStatsGroup,
       "ipmsZeroStatsFlag": ipmsZeroStatsFlag,
       "ipmsForwardingTable": ipmsForwardingTable,
       "ipmsFwdTableEntry": ipmsFwdTableEntry,
       "ipmsFwdDestIP": ipmsFwdDestIP,
       "ipmsFwdSourceIP": ipmsFwdSourceIP,
       "ipmsFwdEntryType": ipmsFwdEntryType,
       "ipmsFwdSrcVlan": ipmsFwdSrcVlan,
       "ipmsFwdSrcVlanMask": ipmsFwdSrcVlanMask,
       "ipmsFwdSrcSlotNumber": ipmsFwdSrcSlotNumber,
       "ipmsFwdSrcPortNumber": ipmsFwdSrcPortNumber,
       "ipmsFwdSrcPortType": ipmsFwdSrcPortType,
       "ipmsFwdSrcPortInstance": ipmsFwdSrcPortInstance,
       "ipmsFwdSrcPortService": ipmsFwdSrcPortService,
       "ipmsFwdDstVlan": ipmsFwdDstVlan,
       "ipmsFwdDstVlanMask": ipmsFwdDstVlanMask,
       "ipmsFwdDstSlotNumber": ipmsFwdDstSlotNumber,
       "ipmsFwdDstPortNumber": ipmsFwdDstPortNumber,
       "ipmsFwdDstPortType": ipmsFwdDstPortType,
       "ipmsFwdDstPortInstance": ipmsFwdDstPortInstance,
       "ipmsFwdDstPortService": ipmsFwdDstPortService,
       "ipmsFwdDstPortMbrFlag": ipmsFwdDstPortMbrFlag,
       "ipmsFwdDstPortNbrFlag": ipmsFwdDstPortNbrFlag,
       "ipmsFwdDstPortRteFlag": ipmsFwdDstPortRteFlag,
       "ipmsPolManParameters": ipmsPolManParameters,
       "ipmsPolManDefaultPolicy": ipmsPolManDefaultPolicy,
       "ipmsPolManActiveTimer": ipmsPolManActiveTimer,
       "ipmsPolManDeleteTimer": ipmsPolManDeleteTimer,
       "ipmsPolManCacheTable": ipmsPolManCacheTable,
       "ipmsPolManCacheTableEntry": ipmsPolManCacheTableEntry,
       "ipmsPolManMCGroup": ipmsPolManMCGroup,
       "ipmsPolManSlot": ipmsPolManSlot,
       "ipmsPolManPort": ipmsPolManPort,
       "ipmsPolManType": ipmsPolManType,
       "ipmsPolManInstance": ipmsPolManInstance,
       "ipmsPolManService": ipmsPolManService,
       "ipmsPolManVlanGroup": ipmsPolManVlanGroup,
       "ipmsPolManStatus": ipmsPolManStatus,
       "ipmsPolManState": ipmsPolManState,
       "ipmsPolManTimeout": ipmsPolManTimeout}
)
