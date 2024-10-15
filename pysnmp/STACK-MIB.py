# SNMP MIB module (STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:50 2024
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

stack = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300)
)
stack.setRevisions(
        ("2004-05-14 00:00",)
)


# Types definitions



class MasterSlaveDataSynStatus(Integer32):
    """Custom type MasterSlaveDataSynStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(11,
              12,
              13,
              20,
              40,
              50,
              60,
              70,
              80,
              90,
              100)
        )
    )
    namedValues = NamedValues(
        *(("backbatchsync", 70),
          ("backinit", 12),
          ("backrealsync", 90),
          ("backreg", 40),
          ("interaction", 50),
          ("masterbatchsync", 60),
          ("mastergr", 100),
          ("masteridle", 20),
          ("masterinit", 11),
          ("masterrealsync", 80),
          ("memberinit", 13))
    )





class StkDeviceStatus(Integer32):
    """Custom type StkDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 0),
          ("member", 2),
          ("slave", 1))
    )





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
_SystemGrp_ObjectIdentity = ObjectIdentity
systemGrp = _SystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1)
)
_SysNetMask_Type = IpAddress
_SysNetMask_Object = MibScalar
sysNetMask = _SysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 1),
    _SysNetMask_Type()
)
sysNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetMask.setStatus("deprecated")


class _SysManagIf_Type(DisplayString):
    """Custom type sysManagIf based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysManagIf_Type.__name__ = "DisplayString"
_SysManagIf_Object = MibScalar
sysManagIf = _SysManagIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 2),
    _SysManagIf_Type()
)
sysManagIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysManagIf.setStatus("current")
_SysMacAddr_Type = MacAddress
_SysMacAddr_Object = MibScalar
sysMacAddr = _SysMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 3),
    _SysMacAddr_Type()
)
sysMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMacAddr.setStatus("current")
_SysMacChagAgingTime_Type = Integer32
_SysMacChagAgingTime_Object = MibScalar
sysMacChagAgingTime = _SysMacChagAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 4),
    _SysMacChagAgingTime_Type()
)
sysMacChagAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMacChagAgingTime.setStatus("current")


class _SysLastchagConfigTime_Type(DisplayString):
    """Custom type sysLastchagConfigTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SysLastchagConfigTime_Type.__name__ = "DisplayString"
_SysLastchagConfigTime_Object = MibScalar
sysLastchagConfigTime = _SysLastchagConfigTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 5),
    _SysLastchagConfigTime_Type()
)
sysLastchagConfigTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysLastchagConfigTime.setStatus("current")
_SysMasterSlaveDataSynStatus_Type = MasterSlaveDataSynStatus
_SysMasterSlaveDataSynStatus_Object = MibScalar
sysMasterSlaveDataSynStatus = _SysMasterSlaveDataSynStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 6),
    _SysMasterSlaveDataSynStatus_Type()
)
sysMasterSlaveDataSynStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMasterSlaveDataSynStatus.setStatus("current")
_SysManagIpAddr_Type = IpAddress
_SysManagIpAddr_Object = MibScalar
sysManagIpAddr = _SysManagIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 1, 7),
    _SysManagIpAddr_Type()
)
sysManagIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysManagIpAddr.setStatus("current")
_SysStkDeviceInfoTable_Object = MibTable
sysStkDeviceInfoTable = _SysStkDeviceInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2)
)
if mibBuilder.loadTexts:
    sysStkDeviceInfoTable.setStatus("current")
_SysStkDeviceInfoEntry_Object = MibTableRow
sysStkDeviceInfoEntry = _SysStkDeviceInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1)
)
sysStkDeviceInfoEntry.setIndexNames(
    (0, "STACK-MIB", "sysStkDeviceID"),
)
if mibBuilder.loadTexts:
    sysStkDeviceInfoEntry.setStatus("current")
_SysStkDeviceID_Type = Integer32
_SysStkDeviceID_Object = MibTableColumn
sysStkDeviceID = _SysStkDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 1),
    _SysStkDeviceID_Type()
)
sysStkDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkDeviceID.setStatus("current")
_SysStkDeviceType_Type = Integer32
_SysStkDeviceType_Object = MibTableColumn
sysStkDeviceType = _SysStkDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 2),
    _SysStkDeviceType_Type()
)
sysStkDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkDeviceType.setStatus("current")
_SysMemDeviceMacAddr_Type = MacAddress
_SysMemDeviceMacAddr_Object = MibTableColumn
sysMemDeviceMacAddr = _SysMemDeviceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 3),
    _SysMemDeviceMacAddr_Type()
)
sysMemDeviceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemDeviceMacAddr.setStatus("current")
_SysMemUpTime_Type = TimeTicks
_SysMemUpTime_Object = MibTableColumn
sysMemUpTime = _SysMemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 4),
    _SysMemUpTime_Type()
)
sysMemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMemUpTime.setStatus("current")
_SysStkDeviceStatus_Type = StkDeviceStatus
_SysStkDeviceStatus_Object = MibTableColumn
sysStkDeviceStatus = _SysStkDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 2, 1, 5),
    _SysStkDeviceStatus_Type()
)
sysStkDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStkDeviceStatus.setStatus("current")
_Zxr10StackStatTable_Object = MibTable
zxr10StackStatTable = _Zxr10StackStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3)
)
if mibBuilder.loadTexts:
    zxr10StackStatTable.setStatus("current")
_Zxr10StackStatEntry_Object = MibTableRow
zxr10StackStatEntry = _Zxr10StackStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1)
)
zxr10StackStatEntry.setIndexNames(
    (0, "STACK-MIB", "zxr10StkDeviceID"),
)
if mibBuilder.loadTexts:
    zxr10StackStatEntry.setStatus("current")
_Zxr10StkDeviceID_Type = Integer32
_Zxr10StkDeviceID_Object = MibTableColumn
zxr10StkDeviceID = _Zxr10StkDeviceID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 1),
    _Zxr10StkDeviceID_Type()
)
zxr10StkDeviceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StkDeviceID.setStatus("current")
_Zxr10StkDeviceMacAddr_Type = MacAddress
_Zxr10StkDeviceMacAddr_Object = MibTableColumn
zxr10StkDeviceMacAddr = _Zxr10StkDeviceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 2),
    _Zxr10StkDeviceMacAddr_Type()
)
zxr10StkDeviceMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StkDeviceMacAddr.setStatus("current")
_Zxr10StkDeviceCpuUtility5s_Type = DisplayString
_Zxr10StkDeviceCpuUtility5s_Object = MibTableColumn
zxr10StkDeviceCpuUtility5s = _Zxr10StkDeviceCpuUtility5s_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 3),
    _Zxr10StkDeviceCpuUtility5s_Type()
)
zxr10StkDeviceCpuUtility5s.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StkDeviceCpuUtility5s.setStatus("current")
_Zxr10StkDeviceCpuUtility1m_Type = DisplayString
_Zxr10StkDeviceCpuUtility1m_Object = MibTableColumn
zxr10StkDeviceCpuUtility1m = _Zxr10StkDeviceCpuUtility1m_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 4),
    _Zxr10StkDeviceCpuUtility1m_Type()
)
zxr10StkDeviceCpuUtility1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StkDeviceCpuUtility1m.setStatus("current")
_Zxr10StkDeviceCpuUtility5m_Type = DisplayString
_Zxr10StkDeviceCpuUtility5m_Object = MibTableColumn
zxr10StkDeviceCpuUtility5m = _Zxr10StkDeviceCpuUtility5m_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 5),
    _Zxr10StkDeviceCpuUtility5m_Type()
)
zxr10StkDeviceCpuUtility5m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StkDeviceCpuUtility5m.setStatus("current")
_Zxr10StkDeviceMemUtility_Type = DisplayString
_Zxr10StkDeviceMemUtility_Object = MibTableColumn
zxr10StkDeviceMemUtility = _Zxr10StkDeviceMemUtility_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 300, 3, 1, 6),
    _Zxr10StkDeviceMemUtility_Type()
)
zxr10StkDeviceMemUtility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxr10StkDeviceMemUtility.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STACK-MIB",
    **{"MasterSlaveDataSynStatus": MasterSlaveDataSynStatus,
       "StkDeviceStatus": StkDeviceStatus,
       "VendorIdType": VendorIdType,
       "zte": zte,
       "zxr10": zxr10,
       "stack": stack,
       "systemGrp": systemGrp,
       "sysNetMask": sysNetMask,
       "sysManagIf": sysManagIf,
       "sysMacAddr": sysMacAddr,
       "sysMacChagAgingTime": sysMacChagAgingTime,
       "sysLastchagConfigTime": sysLastchagConfigTime,
       "sysMasterSlaveDataSynStatus": sysMasterSlaveDataSynStatus,
       "sysManagIpAddr": sysManagIpAddr,
       "sysStkDeviceInfoTable": sysStkDeviceInfoTable,
       "sysStkDeviceInfoEntry": sysStkDeviceInfoEntry,
       "sysStkDeviceID": sysStkDeviceID,
       "sysStkDeviceType": sysStkDeviceType,
       "sysMemDeviceMacAddr": sysMemDeviceMacAddr,
       "sysMemUpTime": sysMemUpTime,
       "sysStkDeviceStatus": sysStkDeviceStatus,
       "zxr10StackStatTable": zxr10StackStatTable,
       "zxr10StackStatEntry": zxr10StackStatEntry,
       "zxr10StkDeviceID": zxr10StkDeviceID,
       "zxr10StkDeviceMacAddr": zxr10StkDeviceMacAddr,
       "zxr10StkDeviceCpuUtility5s": zxr10StkDeviceCpuUtility5s,
       "zxr10StkDeviceCpuUtility1m": zxr10StkDeviceCpuUtility1m,
       "zxr10StkDeviceCpuUtility5m": zxr10StkDeviceCpuUtility5m,
       "zxr10StkDeviceMemUtility": zxr10StkDeviceMemUtility}
)
