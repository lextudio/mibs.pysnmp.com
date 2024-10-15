# SNMP MIB module (STACK-TOP) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STACK-TOP
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:51 2024
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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

stacktop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301)
)
stacktop.setRevisions(
        ("2004-05-14 00:00",)
)


# Types definitions



class VendorIdType(OctetString):
    """Custom type VendorIdType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_Zxr10_ObjectIdentity = ObjectIdentity
zxr10 = _Zxr10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3)
)
_SysMasterVoteTimes_Type = Integer32
_SysMasterVoteTimes_Object = MibScalar
sysMasterVoteTimes = _SysMasterVoteTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 1),
    _SysMasterVoteTimes_Type()
)
sysMasterVoteTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMasterVoteTimes.setStatus("current")
_SysMasterLastVoteTime_Type = TimeTicks
_SysMasterLastVoteTime_Object = MibScalar
sysMasterLastVoteTime = _SysMasterLastVoteTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 2),
    _SysMasterLastVoteTime_Type()
)
sysMasterLastVoteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMasterLastVoteTime.setStatus("current")
_SysLastDetecTopEndTime_Type = TimeTicks
_SysLastDetecTopEndTime_Object = MibScalar
sysLastDetecTopEndTime = _SysLastDetecTopEndTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 3),
    _SysLastDetecTopEndTime_Type()
)
sysLastDetecTopEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastDetecTopEndTime.setStatus("current")
_SysTopChagTimes_Type = Integer32
_SysTopChagTimes_Object = MibScalar
sysTopChagTimes = _SysTopChagTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 4),
    _SysTopChagTimes_Type()
)
sysTopChagTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTopChagTimes.setStatus("current")
_SysTopDetecMsgCount_Type = Integer32
_SysTopDetecMsgCount_Object = MibScalar
sysTopDetecMsgCount = _SysTopDetecMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 5),
    _SysTopDetecMsgCount_Type()
)
sysTopDetecMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTopDetecMsgCount.setStatus("current")
_SysTopInfoTable_Object = MibTable
sysTopInfoTable = _SysTopInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6)
)
if mibBuilder.loadTexts:
    sysTopInfoTable.setStatus("current")
_SysTopInfoEntry_Object = MibTableRow
sysTopInfoEntry = _SysTopInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1)
)
sysTopInfoEntry.setIndexNames(
    (0, "STACK-TOP", "sysDeviceMacAddr"),
    (0, "STACK-TOP", "sysDeviceStkPortIndex"),
)
if mibBuilder.loadTexts:
    sysTopInfoEntry.setStatus("current")
_SysDeviceMacAddr_Type = MacAddress
_SysDeviceMacAddr_Object = MibTableColumn
sysDeviceMacAddr = _SysDeviceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 1),
    _SysDeviceMacAddr_Type()
)
sysDeviceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceMacAddr.setStatus("current")
_SysDeviceStkPortIndex_Type = Integer32
_SysDeviceStkPortIndex_Object = MibTableColumn
sysDeviceStkPortIndex = _SysDeviceStkPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 2),
    _SysDeviceStkPortIndex_Type()
)
sysDeviceStkPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkPortIndex.setStatus("current")
_SysDeviceType_Type = Integer32
_SysDeviceType_Object = MibTableColumn
sysDeviceType = _SysDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 3),
    _SysDeviceType_Type()
)
sysDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceType.setStatus("current")
_SysDeviceStkPortNum_Type = Integer32
_SysDeviceStkPortNum_Object = MibTableColumn
sysDeviceStkPortNum = _SysDeviceStkPortNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 4),
    _SysDeviceStkPortNum_Type()
)
sysDeviceStkPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkPortNum.setStatus("current")
_SysDeviceID_Type = Integer32
_SysDeviceID_Object = MibTableColumn
sysDeviceID = _SysDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 5),
    _SysDeviceID_Type()
)
sysDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceID.setStatus("current")
_SysDeviceMasterPri_Type = Integer32
_SysDeviceMasterPri_Object = MibTableColumn
sysDeviceMasterPri = _SysDeviceMasterPri_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 6),
    _SysDeviceMasterPri_Type()
)
sysDeviceMasterPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceMasterPri.setStatus("current")


class _SysDeviceStkIfStatus_Type(Integer32):
    """Custom type sysDeviceStkIfStatus based on Integer32"""
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


_SysDeviceStkIfStatus_Type.__name__ = "Integer32"
_SysDeviceStkIfStatus_Object = MibTableColumn
sysDeviceStkIfStatus = _SysDeviceStkIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 7),
    _SysDeviceStkIfStatus_Type()
)
sysDeviceStkIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkIfStatus.setStatus("current")
_SysDeviceStkIfPanel_Type = Integer32
_SysDeviceStkIfPanel_Object = MibTableColumn
sysDeviceStkIfPanel = _SysDeviceStkIfPanel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 8),
    _SysDeviceStkIfPanel_Type()
)
sysDeviceStkIfPanel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkIfPanel.setStatus("current")
_SysDeviceStkIfPortID_Type = Integer32
_SysDeviceStkIfPortID_Object = MibTableColumn
sysDeviceStkIfPortID = _SysDeviceStkIfPortID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 9),
    _SysDeviceStkIfPortID_Type()
)
sysDeviceStkIfPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkIfPortID.setStatus("current")
_SysDeviceStkPortNeibMacAddr_Type = MacAddress
_SysDeviceStkPortNeibMacAddr_Object = MibTableColumn
sysDeviceStkPortNeibMacAddr = _SysDeviceStkPortNeibMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 10),
    _SysDeviceStkPortNeibMacAddr_Type()
)
sysDeviceStkPortNeibMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkPortNeibMacAddr.setStatus("current")
_SysDeviceStkPortNeibPortIndex_Type = Integer32
_SysDeviceStkPortNeibPortIndex_Object = MibTableColumn
sysDeviceStkPortNeibPortIndex = _SysDeviceStkPortNeibPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 6, 1, 11),
    _SysDeviceStkPortNeibPortIndex_Type()
)
sysDeviceStkPortNeibPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysDeviceStkPortNeibPortIndex.setStatus("current")
_SysStkPortMsgStacTable_Object = MibTable
sysStkPortMsgStacTable = _SysStkPortMsgStacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 7)
)
if mibBuilder.loadTexts:
    sysStkPortMsgStacTable.setStatus("current")
_SysStkPortMsgStacEntry_Object = MibTableRow
sysStkPortMsgStacEntry = _SysStkPortMsgStacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 7, 1)
)
sysStkPortMsgStacEntry.setIndexNames(
    (0, "STACK-TOP", "sysStkDeviceID"),
    (0, "STACK-TOP", "sysStkDeviceStkIfIndex"),
)
if mibBuilder.loadTexts:
    sysStkPortMsgStacEntry.setStatus("current")
_SysStkDeviceID_Type = Integer32
_SysStkDeviceID_Object = MibTableColumn
sysStkDeviceID = _SysStkDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 7, 1, 1),
    _SysStkDeviceID_Type()
)
sysStkDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkDeviceID.setStatus("current")
_SysStkDeviceStkIfIndex_Type = Integer32
_SysStkDeviceStkIfIndex_Object = MibTableColumn
sysStkDeviceStkIfIndex = _SysStkDeviceStkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 7, 1, 2),
    _SysStkDeviceStkIfIndex_Type()
)
sysStkDeviceStkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkDeviceStkIfIndex.setStatus("current")
_SysStkPortRecMsgCount_Type = Integer32
_SysStkPortRecMsgCount_Object = MibTableColumn
sysStkPortRecMsgCount = _SysStkPortRecMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 7, 1, 3),
    _SysStkPortRecMsgCount_Type()
)
sysStkPortRecMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkPortRecMsgCount.setStatus("current")
_SysStkPortSendMsgCount_Type = Integer32
_SysStkPortSendMsgCount_Object = MibTableColumn
sysStkPortSendMsgCount = _SysStkPortSendMsgCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 301, 7, 1, 4),
    _SysStkPortSendMsgCount_Type()
)
sysStkPortSendMsgCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkPortSendMsgCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STACK-TOP",
    **{"VendorIdType": VendorIdType,
       "zte": zte,
       "zxr10": zxr10,
       "stacktop": stacktop,
       "sysMasterVoteTimes": sysMasterVoteTimes,
       "sysMasterLastVoteTime": sysMasterLastVoteTime,
       "sysLastDetecTopEndTime": sysLastDetecTopEndTime,
       "sysTopChagTimes": sysTopChagTimes,
       "sysTopDetecMsgCount": sysTopDetecMsgCount,
       "sysTopInfoTable": sysTopInfoTable,
       "sysTopInfoEntry": sysTopInfoEntry,
       "sysDeviceMacAddr": sysDeviceMacAddr,
       "sysDeviceStkPortIndex": sysDeviceStkPortIndex,
       "sysDeviceType": sysDeviceType,
       "sysDeviceStkPortNum": sysDeviceStkPortNum,
       "sysDeviceID": sysDeviceID,
       "sysDeviceMasterPri": sysDeviceMasterPri,
       "sysDeviceStkIfStatus": sysDeviceStkIfStatus,
       "sysDeviceStkIfPanel": sysDeviceStkIfPanel,
       "sysDeviceStkIfPortID": sysDeviceStkIfPortID,
       "sysDeviceStkPortNeibMacAddr": sysDeviceStkPortNeibMacAddr,
       "sysDeviceStkPortNeibPortIndex": sysDeviceStkPortNeibPortIndex,
       "sysStkPortMsgStacTable": sysStkPortMsgStacTable,
       "sysStkPortMsgStacEntry": sysStkPortMsgStacEntry,
       "sysStkDeviceID": sysStkDeviceID,
       "sysStkDeviceStkIfIndex": sysStkDeviceStkIfIndex,
       "sysStkPortRecMsgCount": sysStkPortRecMsgCount,
       "sysStkPortSendMsgCount": sysStkPortSendMsgCount}
)
