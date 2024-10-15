# SNMP MIB module (CISCO-STACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-STACK-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:08:52 2024
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

(workgroup,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "workgroup")

(VlanIndex,) = mibBuilder.importSymbols(
    "CISCO-VTP-MIB",
    "VlanIndex")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

(fddimibPORTIndex,
 fddimibPORTSMTIndex) = mibBuilder.importSymbols(
    "FDDI-SMT73-MIB",
    "fddimibPORTIndex",
    "fddimibPORTSMTIndex")

(OwnerString,
 ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString",
    "ifIndex",
    "ifName")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(ringStationMacAddress,) = mibBuilder.importSymbols(
    "TOKEN-RING-RMON-MIB",
    "ringStationMacAddress")


# MODULE-IDENTITY

ciscoStackMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1)
)
ciscoStackMIB.setRevisions(
        ("2014-03-03 00:00",
         "2012-06-16 00:00",
         "2010-02-01 00:00",
         "2007-12-12 00:00",
         "2007-05-29 00:00",
         "2007-05-25 00:00",
         "2007-03-30 00:00",
         "2005-10-28 00:00",
         "2005-04-27 00:00",
         "2004-05-14 00:00",
         "2004-01-15 00:00",
         "2003-05-29 00:00",
         "2003-05-05 00:00",
         "2002-09-24 00:00",
         "2001-06-11 00:00",
         "2001-04-11 00:00",
         "2000-10-10 00:00",
         "2000-05-16 00:00",
         "2000-02-02 00:00",
         "1999-09-30 00:00",
         "1999-03-26 00:00",
         "1999-02-12 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VendorIdType(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



# MIB Managed Objects in the order of their OIDs

_CiscoStackNotificationsPrefix_ObjectIdentity = ObjectIdentity
ciscoStackNotificationsPrefix = _CiscoStackNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 0)
)
_SystemGrp_ObjectIdentity = ObjectIdentity
systemGrp = _SystemGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1)
)


class _SysMgmtType_Type(Integer32):
    """Custom type sysMgmtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("smux", 3),
          ("snmpV1", 2),
          ("snmpV2V1", 4),
          ("snmpV2cV1", 5),
          ("snmpV3V2cV1", 6))
    )


_SysMgmtType_Type.__name__ = "Integer32"
_SysMgmtType_Object = MibScalar
sysMgmtType = _SysMgmtType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 1),
    _SysMgmtType_Type()
)
sysMgmtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMgmtType.setStatus("current")
_SysIpAddr_Type = IpAddress
_SysIpAddr_Object = MibScalar
sysIpAddr = _SysIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 2),
    _SysIpAddr_Type()
)
sysIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpAddr.setStatus("deprecated")
_SysNetMask_Type = IpAddress
_SysNetMask_Object = MibScalar
sysNetMask = _SysNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 3),
    _SysNetMask_Type()
)
sysNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysNetMask.setStatus("deprecated")
_SysBroadcast_Type = IpAddress
_SysBroadcast_Object = MibScalar
sysBroadcast = _SysBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 4),
    _SysBroadcast_Type()
)
sysBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBroadcast.setStatus("deprecated")
_SysTrapReceiverTable_Object = MibTable
sysTrapReceiverTable = _SysTrapReceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 5)
)
if mibBuilder.loadTexts:
    sysTrapReceiverTable.setStatus("deprecated")
_SysTrapReceiverEntry_Object = MibTableRow
sysTrapReceiverEntry = _SysTrapReceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 5, 1)
)
sysTrapReceiverEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "sysTrapReceiverAddr"),
)
if mibBuilder.loadTexts:
    sysTrapReceiverEntry.setStatus("deprecated")


class _SysTrapReceiverType_Type(Integer32):
    """Custom type sysTrapReceiverType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SysTrapReceiverType_Type.__name__ = "Integer32"
_SysTrapReceiverType_Object = MibTableColumn
sysTrapReceiverType = _SysTrapReceiverType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 5, 1, 1),
    _SysTrapReceiverType_Type()
)
sysTrapReceiverType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapReceiverType.setStatus("deprecated")
_SysTrapReceiverAddr_Type = IpAddress
_SysTrapReceiverAddr_Object = MibTableColumn
sysTrapReceiverAddr = _SysTrapReceiverAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 5, 1, 2),
    _SysTrapReceiverAddr_Type()
)
sysTrapReceiverAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrapReceiverAddr.setStatus("deprecated")


class _SysTrapReceiverComm_Type(DisplayString):
    """Custom type sysTrapReceiverComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysTrapReceiverComm_Type.__name__ = "DisplayString"
_SysTrapReceiverComm_Object = MibTableColumn
sysTrapReceiverComm = _SysTrapReceiverComm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 5, 1, 3),
    _SysTrapReceiverComm_Type()
)
sysTrapReceiverComm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrapReceiverComm.setStatus("deprecated")
_SysCommunityTable_Object = MibTable
sysCommunityTable = _SysCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    sysCommunityTable.setStatus("deprecated")
_SysCommunityEntry_Object = MibTableRow
sysCommunityEntry = _SysCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 6, 1)
)
sysCommunityEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "sysCommunityAccess"),
)
if mibBuilder.loadTexts:
    sysCommunityEntry.setStatus("deprecated")


class _SysCommunityAccess_Type(Integer32):
    """Custom type sysCommunityAccess based on Integer32"""
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
        *(("other", 1),
          ("readOnly", 2),
          ("readWrite", 3),
          ("readWriteAll", 4))
    )


_SysCommunityAccess_Type.__name__ = "Integer32"
_SysCommunityAccess_Object = MibTableColumn
sysCommunityAccess = _SysCommunityAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 6, 1, 1),
    _SysCommunityAccess_Type()
)
sysCommunityAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCommunityAccess.setStatus("deprecated")


class _SysCommunityString_Type(DisplayString):
    """Custom type sysCommunityString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysCommunityString_Type.__name__ = "DisplayString"
_SysCommunityString_Object = MibTableColumn
sysCommunityString = _SysCommunityString_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 6, 1, 2),
    _SysCommunityString_Type()
)
sysCommunityString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCommunityString.setStatus("deprecated")


class _SysAttachType_Type(Integer32):
    """Custom type sysAttachType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("dualAttach", 2),
          ("dualPrio", 5),
          ("nullAttach", 4),
          ("other", 1),
          ("singleAttach", 3))
    )


_SysAttachType_Type.__name__ = "Integer32"
_SysAttachType_Object = MibScalar
sysAttachType = _SysAttachType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 7),
    _SysAttachType_Type()
)
sysAttachType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAttachType.setStatus("current")


class _SysTraffic_Type(Integer32):
    """Custom type sysTraffic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysTraffic_Type.__name__ = "Integer32"
_SysTraffic_Object = MibScalar
sysTraffic = _SysTraffic_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 8),
    _SysTraffic_Type()
)
sysTraffic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTraffic.setStatus("current")


class _SysReset_Type(Integer32):
    """Custom type sysReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("reset", 2),
          ("resetMinDown", 3))
    )


_SysReset_Type.__name__ = "Integer32"
_SysReset_Object = MibScalar
sysReset = _SysReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 9),
    _SysReset_Type()
)
sysReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysReset.setStatus("deprecated")


class _SysBaudRate_Type(Integer32):
    """Custom type sysBaudRate based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(600,
              1200,
              2400,
              4800,
              9600,
              19200,
              38400)
        )
    )
    namedValues = NamedValues(
        *(("b1200", 1200),
          ("b19200", 19200),
          ("b2400", 2400),
          ("b38400", 38400),
          ("b4800", 4800),
          ("b600", 600),
          ("b9600", 9600))
    )


_SysBaudRate_Type.__name__ = "Integer32"
_SysBaudRate_Object = MibScalar
sysBaudRate = _SysBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 10),
    _SysBaudRate_Type()
)
sysBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBaudRate.setStatus("current")


class _SysInsertMode_Type(Integer32):
    """Custom type sysInsertMode based on Integer32"""
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
        *(("graceful", 4),
          ("other", 1),
          ("scheduled", 3),
          ("standard", 2))
    )


_SysInsertMode_Type.__name__ = "Integer32"
_SysInsertMode_Object = MibScalar
sysInsertMode = _SysInsertMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 11),
    _SysInsertMode_Type()
)
sysInsertMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysInsertMode.setStatus("current")
_SysClearMacTime_Type = TimeTicks
_SysClearMacTime_Object = MibScalar
sysClearMacTime = _SysClearMacTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 12),
    _SysClearMacTime_Type()
)
sysClearMacTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClearMacTime.setStatus("deprecated")
_SysClearPortTime_Type = TimeTicks
_SysClearPortTime_Object = MibScalar
sysClearPortTime = _SysClearPortTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 13),
    _SysClearPortTime_Type()
)
sysClearPortTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysClearPortTime.setStatus("deprecated")
_SysFddiRingTable_Object = MibTable
sysFddiRingTable = _SysFddiRingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 14)
)
if mibBuilder.loadTexts:
    sysFddiRingTable.setStatus("current")
_SysFddiRingEntry_Object = MibTableRow
sysFddiRingEntry = _SysFddiRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 14, 1)
)
sysFddiRingEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "sysFddiRingSMTIndex"),
    (0, "CISCO-STACK-MIB", "sysFddiRingAddress"),
)
if mibBuilder.loadTexts:
    sysFddiRingEntry.setStatus("current")


class _SysFddiRingSMTIndex_Type(Integer32):
    """Custom type sysFddiRingSMTIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SysFddiRingSMTIndex_Type.__name__ = "Integer32"
_SysFddiRingSMTIndex_Object = MibTableColumn
sysFddiRingSMTIndex = _SysFddiRingSMTIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 14, 1, 1),
    _SysFddiRingSMTIndex_Type()
)
sysFddiRingSMTIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFddiRingSMTIndex.setStatus("current")
_SysFddiRingAddress_Type = MacAddress
_SysFddiRingAddress_Object = MibTableColumn
sysFddiRingAddress = _SysFddiRingAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 14, 1, 2),
    _SysFddiRingAddress_Type()
)
sysFddiRingAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFddiRingAddress.setStatus("current")
_SysFddiRingNext_Type = MacAddress
_SysFddiRingNext_Object = MibTableColumn
sysFddiRingNext = _SysFddiRingNext_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 14, 1, 3),
    _SysFddiRingNext_Type()
)
sysFddiRingNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysFddiRingNext.setStatus("current")


class _SysEnableModem_Type(Integer32):
    """Custom type sysEnableModem based on Integer32"""
    defaultValue = 2

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


_SysEnableModem_Type.__name__ = "Integer32"
_SysEnableModem_Object = MibScalar
sysEnableModem = _SysEnableModem_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 15),
    _SysEnableModem_Type()
)
sysEnableModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableModem.setStatus("current")


class _SysEnableRedirects_Type(Integer32):
    """Custom type sysEnableRedirects based on Integer32"""
    defaultValue = 1

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


_SysEnableRedirects_Type.__name__ = "Integer32"
_SysEnableRedirects_Object = MibScalar
sysEnableRedirects = _SysEnableRedirects_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 16),
    _SysEnableRedirects_Type()
)
sysEnableRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableRedirects.setStatus("current")


class _SysEnableRmon_Type(Integer32):
    """Custom type sysEnableRmon based on Integer32"""
    defaultValue = 1

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


_SysEnableRmon_Type.__name__ = "Integer32"
_SysEnableRmon_Object = MibScalar
sysEnableRmon = _SysEnableRmon_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 17),
    _SysEnableRmon_Type()
)
sysEnableRmon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableRmon.setStatus("current")


class _SysArpAgingTime_Type(Integer32):
    """Custom type sysArpAgingTime based on Integer32"""
    defaultValue = 1200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_SysArpAgingTime_Type.__name__ = "Integer32"
_SysArpAgingTime_Object = MibScalar
sysArpAgingTime = _SysArpAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 18),
    _SysArpAgingTime_Type()
)
sysArpAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysArpAgingTime.setStatus("current")


class _SysTrafficPeak_Type(Integer32):
    """Custom type sysTrafficPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysTrafficPeak_Type.__name__ = "Integer32"
_SysTrafficPeak_Object = MibScalar
sysTrafficPeak = _SysTrafficPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 19),
    _SysTrafficPeak_Type()
)
sysTrafficPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrafficPeak.setStatus("current")
_SysTrafficPeakTime_Type = TimeTicks
_SysTrafficPeakTime_Object = MibScalar
sysTrafficPeakTime = _SysTrafficPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 20),
    _SysTrafficPeakTime_Type()
)
sysTrafficPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrafficPeakTime.setStatus("current")


class _SysCommunityRwa_Type(DisplayString):
    """Custom type sysCommunityRwa based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysCommunityRwa_Type.__name__ = "DisplayString"
_SysCommunityRwa_Object = MibScalar
sysCommunityRwa = _SysCommunityRwa_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 21),
    _SysCommunityRwa_Type()
)
sysCommunityRwa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCommunityRwa.setStatus("current")


class _SysCommunityRw_Type(DisplayString):
    """Custom type sysCommunityRw based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysCommunityRw_Type.__name__ = "DisplayString"
_SysCommunityRw_Object = MibScalar
sysCommunityRw = _SysCommunityRw_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 22),
    _SysCommunityRw_Type()
)
sysCommunityRw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCommunityRw.setStatus("current")


class _SysCommunityRo_Type(DisplayString):
    """Custom type sysCommunityRo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysCommunityRo_Type.__name__ = "DisplayString"
_SysCommunityRo_Object = MibScalar
sysCommunityRo = _SysCommunityRo_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 23),
    _SysCommunityRo_Type()
)
sysCommunityRo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCommunityRo.setStatus("current")


class _SysEnableChassisTraps_Type(Integer32):
    """Custom type sysEnableChassisTraps based on Integer32"""
    defaultValue = 2

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


_SysEnableChassisTraps_Type.__name__ = "Integer32"
_SysEnableChassisTraps_Object = MibScalar
sysEnableChassisTraps = _SysEnableChassisTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 24),
    _SysEnableChassisTraps_Type()
)
sysEnableChassisTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableChassisTraps.setStatus("current")


class _SysEnableModuleTraps_Type(Integer32):
    """Custom type sysEnableModuleTraps based on Integer32"""
    defaultValue = 2

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


_SysEnableModuleTraps_Type.__name__ = "Integer32"
_SysEnableModuleTraps_Object = MibScalar
sysEnableModuleTraps = _SysEnableModuleTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 25),
    _SysEnableModuleTraps_Type()
)
sysEnableModuleTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableModuleTraps.setStatus("current")


class _SysEnableBridgeTraps_Type(Integer32):
    """Custom type sysEnableBridgeTraps based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForNewRootOnly", 3),
          ("enabledForTopoChangeOnly", 4))
    )


_SysEnableBridgeTraps_Type.__name__ = "Integer32"
_SysEnableBridgeTraps_Object = MibScalar
sysEnableBridgeTraps = _SysEnableBridgeTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 26),
    _SysEnableBridgeTraps_Type()
)
sysEnableBridgeTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableBridgeTraps.setStatus("deprecated")


class _SysIpVlan_Type(VlanIndex):
    """Custom type sysIpVlan based on VlanIndex"""
    defaultValue = 1


_SysIpVlan_Object = MibScalar
sysIpVlan = _SysIpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 27),
    _SysIpVlan_Type()
)
sysIpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysIpVlan.setStatus("current")
_SysConfigChangeTime_Type = TimeTicks
_SysConfigChangeTime_Object = MibScalar
sysConfigChangeTime = _SysConfigChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 28),
    _SysConfigChangeTime_Type()
)
sysConfigChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigChangeTime.setStatus("current")


class _SysEnableRepeaterTraps_Type(Integer32):
    """Custom type sysEnableRepeaterTraps based on Integer32"""
    defaultValue = 2

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


_SysEnableRepeaterTraps_Type.__name__ = "Integer32"
_SysEnableRepeaterTraps_Object = MibScalar
sysEnableRepeaterTraps = _SysEnableRepeaterTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 29),
    _SysEnableRepeaterTraps_Type()
)
sysEnableRepeaterTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableRepeaterTraps.setStatus("current")


class _SysBannerMotd_Type(DisplayString):
    """Custom type sysBannerMotd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysBannerMotd_Type.__name__ = "DisplayString"
_SysBannerMotd_Object = MibScalar
sysBannerMotd = _SysBannerMotd_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 30),
    _SysBannerMotd_Type()
)
sysBannerMotd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBannerMotd.setStatus("current")


class _SysEnableIpPermitTraps_Type(Integer32):
    """Custom type sysEnableIpPermitTraps based on Integer32"""
    defaultValue = 2

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


_SysEnableIpPermitTraps_Type.__name__ = "Integer32"
_SysEnableIpPermitTraps_Object = MibScalar
sysEnableIpPermitTraps = _SysEnableIpPermitTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 31),
    _SysEnableIpPermitTraps_Type()
)
sysEnableIpPermitTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableIpPermitTraps.setStatus("current")
_SysTrafficMeterTable_Object = MibTable
sysTrafficMeterTable = _SysTrafficMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 32)
)
if mibBuilder.loadTexts:
    sysTrafficMeterTable.setStatus("current")
_SysTrafficMeterEntry_Object = MibTableRow
sysTrafficMeterEntry = _SysTrafficMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 32, 1)
)
sysTrafficMeterEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "sysTrafficMeterType"),
)
if mibBuilder.loadTexts:
    sysTrafficMeterEntry.setStatus("current")


class _SysTrafficMeterType_Type(Integer32):
    """Custom type sysTrafficMeterType based on Integer32"""
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
        *(("switchingBusA", 2),
          ("switchingBusB", 3),
          ("switchingBusC", 4),
          ("systemSwitchingBus", 1))
    )


_SysTrafficMeterType_Type.__name__ = "Integer32"
_SysTrafficMeterType_Object = MibTableColumn
sysTrafficMeterType = _SysTrafficMeterType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 32, 1, 1),
    _SysTrafficMeterType_Type()
)
sysTrafficMeterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrafficMeterType.setStatus("current")


class _SysTrafficMeter_Type(Integer32):
    """Custom type sysTrafficMeter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysTrafficMeter_Type.__name__ = "Integer32"
_SysTrafficMeter_Object = MibTableColumn
sysTrafficMeter = _SysTrafficMeter_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 32, 1, 2),
    _SysTrafficMeter_Type()
)
sysTrafficMeter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrafficMeter.setStatus("current")


class _SysTrafficMeterPeak_Type(Integer32):
    """Custom type sysTrafficMeterPeak based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysTrafficMeterPeak_Type.__name__ = "Integer32"
_SysTrafficMeterPeak_Object = MibTableColumn
sysTrafficMeterPeak = _SysTrafficMeterPeak_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 32, 1, 3),
    _SysTrafficMeterPeak_Type()
)
sysTrafficMeterPeak.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrafficMeterPeak.setStatus("current")
_SysTrafficMeterPeakTime_Type = TimeTicks
_SysTrafficMeterPeakTime_Object = MibTableColumn
sysTrafficMeterPeakTime = _SysTrafficMeterPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 32, 1, 4),
    _SysTrafficMeterPeakTime_Type()
)
sysTrafficMeterPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTrafficMeterPeakTime.setStatus("current")


class _SysEnableVmpsTraps_Type(Integer32):
    """Custom type sysEnableVmpsTraps based on Integer32"""
    defaultValue = 2

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


_SysEnableVmpsTraps_Type.__name__ = "Integer32"
_SysEnableVmpsTraps_Object = MibScalar
sysEnableVmpsTraps = _SysEnableVmpsTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 33),
    _SysEnableVmpsTraps_Type()
)
sysEnableVmpsTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableVmpsTraps.setStatus("current")


class _SysConfigChangeInfo_Type(DisplayString):
    """Custom type sysConfigChangeInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysConfigChangeInfo_Type.__name__ = "DisplayString"
_SysConfigChangeInfo_Object = MibScalar
sysConfigChangeInfo = _SysConfigChangeInfo_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 34),
    _SysConfigChangeInfo_Type()
)
sysConfigChangeInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysConfigChangeInfo.setStatus("current")


class _SysEnableConfigTraps_Type(Integer32):
    """Custom type sysEnableConfigTraps based on Integer32"""
    defaultValue = 2

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


_SysEnableConfigTraps_Type.__name__ = "Integer32"
_SysEnableConfigTraps_Object = MibScalar
sysEnableConfigTraps = _SysEnableConfigTraps_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 35),
    _SysEnableConfigTraps_Type()
)
sysEnableConfigTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableConfigTraps.setStatus("current")


class _SysConfigRegister_Type(OctetString):
    """Custom type sysConfigRegister based on OctetString"""
    defaultHexValue = "010f"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SysConfigRegister_Type.__name__ = "OctetString"
_SysConfigRegister_Object = MibScalar
sysConfigRegister = _SysConfigRegister_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 36),
    _SysConfigRegister_Type()
)
sysConfigRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigRegister.setStatus("current")


class _SysBootVariable_Type(DisplayString):
    """Custom type sysBootVariable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysBootVariable_Type.__name__ = "DisplayString"
_SysBootVariable_Object = MibScalar
sysBootVariable = _SysBootVariable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 37),
    _SysBootVariable_Type()
)
sysBootVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBootVariable.setStatus("current")


class _SysBootedImage_Type(DisplayString):
    """Custom type sysBootedImage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SysBootedImage_Type.__name__ = "DisplayString"
_SysBootedImage_Object = MibScalar
sysBootedImage = _SysBootedImage_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 38),
    _SysBootedImage_Type()
)
sysBootedImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootedImage.setStatus("current")


class _SysEnableEntityTrap_Type(Integer32):
    """Custom type sysEnableEntityTrap based on Integer32"""
    defaultValue = 2

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


_SysEnableEntityTrap_Type.__name__ = "Integer32"
_SysEnableEntityTrap_Object = MibScalar
sysEnableEntityTrap = _SysEnableEntityTrap_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 39),
    _SysEnableEntityTrap_Type()
)
sysEnableEntityTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableEntityTrap.setStatus("current")


class _SysEnableStpxTrap_Type(Integer32):
    """Custom type sysEnableStpxTrap based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForInconLoopOnly", 7),
          ("enabledForInconOnly", 3),
          ("enabledForInconRootOnly", 6),
          ("enabledForLoopOnly", 5),
          ("enabledForRootLoopOnly", 8),
          ("enabledForRootOnly", 4))
    )


_SysEnableStpxTrap_Type.__name__ = "Integer32"
_SysEnableStpxTrap_Object = MibScalar
sysEnableStpxTrap = _SysEnableStpxTrap_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 40),
    _SysEnableStpxTrap_Type()
)
sysEnableStpxTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEnableStpxTrap.setStatus("deprecated")


class _SysExtendedRmonVlanModeEnable_Type(Integer32):
    """Custom type sysExtendedRmonVlanModeEnable based on Integer32"""
    defaultValue = 2

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


_SysExtendedRmonVlanModeEnable_Type.__name__ = "Integer32"
_SysExtendedRmonVlanModeEnable_Object = MibScalar
sysExtendedRmonVlanModeEnable = _SysExtendedRmonVlanModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 41),
    _SysExtendedRmonVlanModeEnable_Type()
)
sysExtendedRmonVlanModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedRmonVlanModeEnable.setStatus("current")


class _SysExtendedRmonNetflowPassword_Type(DisplayString):
    """Custom type sysExtendedRmonNetflowPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SysExtendedRmonNetflowPassword_Type.__name__ = "DisplayString"
_SysExtendedRmonNetflowPassword_Object = MibScalar
sysExtendedRmonNetflowPassword = _SysExtendedRmonNetflowPassword_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 42),
    _SysExtendedRmonNetflowPassword_Type()
)
sysExtendedRmonNetflowPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedRmonNetflowPassword.setStatus("current")


class _SysExtendedRmonNetflowEnable_Type(Integer32):
    """Custom type sysExtendedRmonNetflowEnable based on Integer32"""
    defaultValue = 2

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


_SysExtendedRmonNetflowEnable_Type.__name__ = "Integer32"
_SysExtendedRmonNetflowEnable_Object = MibScalar
sysExtendedRmonNetflowEnable = _SysExtendedRmonNetflowEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 43),
    _SysExtendedRmonNetflowEnable_Type()
)
sysExtendedRmonNetflowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedRmonNetflowEnable.setStatus("current")


class _SysExtendedRmonVlanAgentEnable_Type(Integer32):
    """Custom type sysExtendedRmonVlanAgentEnable based on Integer32"""
    defaultValue = 2

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


_SysExtendedRmonVlanAgentEnable_Type.__name__ = "Integer32"
_SysExtendedRmonVlanAgentEnable_Object = MibScalar
sysExtendedRmonVlanAgentEnable = _SysExtendedRmonVlanAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 44),
    _SysExtendedRmonVlanAgentEnable_Type()
)
sysExtendedRmonVlanAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedRmonVlanAgentEnable.setStatus("current")


class _SysExtendedRmonEnable_Type(Integer32):
    """Custom type sysExtendedRmonEnable based on Integer32"""
    defaultValue = 1

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
          ("enabled", 1),
          ("noNAMPresent", 3))
    )


_SysExtendedRmonEnable_Type.__name__ = "Integer32"
_SysExtendedRmonEnable_Object = MibScalar
sysExtendedRmonEnable = _SysExtendedRmonEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 45),
    _SysExtendedRmonEnable_Type()
)
sysExtendedRmonEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedRmonEnable.setStatus("current")


class _SysConsolePrimaryLoginAuthentication_Type(Integer32):
    """Custom type sysConsolePrimaryLoginAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("radius", 2),
          ("tacacs", 1))
    )


_SysConsolePrimaryLoginAuthentication_Type.__name__ = "Integer32"
_SysConsolePrimaryLoginAuthentication_Object = MibScalar
sysConsolePrimaryLoginAuthentication = _SysConsolePrimaryLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 46),
    _SysConsolePrimaryLoginAuthentication_Type()
)
sysConsolePrimaryLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConsolePrimaryLoginAuthentication.setStatus("deprecated")


class _SysConsolePrimaryEnableAuthentication_Type(Integer32):
    """Custom type sysConsolePrimaryEnableAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("radius", 2),
          ("tacacs", 1))
    )


_SysConsolePrimaryEnableAuthentication_Type.__name__ = "Integer32"
_SysConsolePrimaryEnableAuthentication_Object = MibScalar
sysConsolePrimaryEnableAuthentication = _SysConsolePrimaryEnableAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 47),
    _SysConsolePrimaryEnableAuthentication_Type()
)
sysConsolePrimaryEnableAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConsolePrimaryEnableAuthentication.setStatus("deprecated")


class _SysTelnetPrimaryLoginAuthentication_Type(Integer32):
    """Custom type sysTelnetPrimaryLoginAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("radius", 2),
          ("tacacs", 1))
    )


_SysTelnetPrimaryLoginAuthentication_Type.__name__ = "Integer32"
_SysTelnetPrimaryLoginAuthentication_Object = MibScalar
sysTelnetPrimaryLoginAuthentication = _SysTelnetPrimaryLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 48),
    _SysTelnetPrimaryLoginAuthentication_Type()
)
sysTelnetPrimaryLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTelnetPrimaryLoginAuthentication.setStatus("deprecated")


class _SysTelnetPrimaryEnableAuthentication_Type(Integer32):
    """Custom type sysTelnetPrimaryEnableAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("local", 3),
          ("radius", 2),
          ("tacacs", 1))
    )


_SysTelnetPrimaryEnableAuthentication_Type.__name__ = "Integer32"
_SysTelnetPrimaryEnableAuthentication_Object = MibScalar
sysTelnetPrimaryEnableAuthentication = _SysTelnetPrimaryEnableAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 49),
    _SysTelnetPrimaryEnableAuthentication_Type()
)
sysTelnetPrimaryEnableAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTelnetPrimaryEnableAuthentication.setStatus("deprecated")


class _SysStartupConfigSource_Type(Integer32):
    """Custom type sysStartupConfigSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flashFileNonRecurring", 2),
          ("flashFileRecurring", 1))
    )


_SysStartupConfigSource_Type.__name__ = "Integer32"
_SysStartupConfigSource_Object = MibScalar
sysStartupConfigSource = _SysStartupConfigSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 50),
    _SysStartupConfigSource_Type()
)
sysStartupConfigSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysStartupConfigSource.setStatus("current")
_SysStartupConfigSourceFile_Type = DisplayString
_SysStartupConfigSourceFile_Object = MibScalar
sysStartupConfigSourceFile = _SysStartupConfigSourceFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 51),
    _SysStartupConfigSourceFile_Type()
)
sysStartupConfigSourceFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysStartupConfigSourceFile.setStatus("current")


class _SysConfigSupervisorModuleNo_Type(Integer32):
    """Custom type sysConfigSupervisorModuleNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SysConfigSupervisorModuleNo_Type.__name__ = "Integer32"
_SysConfigSupervisorModuleNo_Object = MibScalar
sysConfigSupervisorModuleNo = _SysConfigSupervisorModuleNo_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 52),
    _SysConfigSupervisorModuleNo_Type()
)
sysConfigSupervisorModuleNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysConfigSupervisorModuleNo.setStatus("current")


class _SysStandbyPortEnable_Type(Integer32):
    """Custom type sysStandbyPortEnable based on Integer32"""
    defaultValue = 2

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


_SysStandbyPortEnable_Type.__name__ = "Integer32"
_SysStandbyPortEnable_Object = MibScalar
sysStandbyPortEnable = _SysStandbyPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 53),
    _SysStandbyPortEnable_Type()
)
sysStandbyPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysStandbyPortEnable.setStatus("current")


class _SysPortFastBpduGuard_Type(Integer32):
    """Custom type sysPortFastBpduGuard based on Integer32"""
    defaultValue = 2

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


_SysPortFastBpduGuard_Type.__name__ = "Integer32"
_SysPortFastBpduGuard_Object = MibScalar
sysPortFastBpduGuard = _SysPortFastBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 54),
    _SysPortFastBpduGuard_Type()
)
sysPortFastBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPortFastBpduGuard.setStatus("deprecated")


class _SysErrDisableTimeoutEnable_Type(Bits):
    """Custom type sysErrDisableTimeoutEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("arpInspectionRate", 9),
          ("bcastSuppression", 8),
          ("bpduPortGuard", 3),
          ("camMonitor", 11),
          ("channelMisconfig", 4),
          ("crossBarFallBack", 5),
          ("duplexMismatch", 2),
          ("ethernetOam", 19),
          ("gl2ptCdpThresholdExceed", 12),
          ("gl2ptEoamThresholdExceed", 20),
          ("gl2ptIngressLoop", 6),
          ("gl2ptStpThresholdExceed", 13),
          ("gl2ptThresholdExceed", 7),
          ("gl2ptVtpThresholdExceed", 14),
          ("linkInErrors", 17),
          ("linkRxCrc", 15),
          ("linkTxCrc", 16),
          ("noStaticInlinePwr", 10),
          ("other", 0),
          ("packetBufferError", 18),
          ("udld", 1))
    )

_SysErrDisableTimeoutEnable_Type.__name__ = "Bits"
_SysErrDisableTimeoutEnable_Object = MibScalar
sysErrDisableTimeoutEnable = _SysErrDisableTimeoutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 55),
    _SysErrDisableTimeoutEnable_Type()
)
sysErrDisableTimeoutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysErrDisableTimeoutEnable.setStatus("current")


class _SysErrDisableTimeoutInterval_Type(Integer32):
    """Custom type sysErrDisableTimeoutInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_SysErrDisableTimeoutInterval_Type.__name__ = "Integer32"
_SysErrDisableTimeoutInterval_Object = MibScalar
sysErrDisableTimeoutInterval = _SysErrDisableTimeoutInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 56),
    _SysErrDisableTimeoutInterval_Type()
)
sysErrDisableTimeoutInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysErrDisableTimeoutInterval.setStatus("current")
if mibBuilder.loadTexts:
    sysErrDisableTimeoutInterval.setUnits("seconds")


class _SysTrafficMonitorHighWaterMark_Type(Integer32):
    """Custom type sysTrafficMonitorHighWaterMark based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysTrafficMonitorHighWaterMark_Type.__name__ = "Integer32"
_SysTrafficMonitorHighWaterMark_Object = MibScalar
sysTrafficMonitorHighWaterMark = _SysTrafficMonitorHighWaterMark_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 57),
    _SysTrafficMonitorHighWaterMark_Type()
)
sysTrafficMonitorHighWaterMark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTrafficMonitorHighWaterMark.setStatus("current")


class _SysHighAvailabilityEnable_Type(TruthValue):
    """Custom type sysHighAvailabilityEnable based on TruthValue"""


_SysHighAvailabilityEnable_Object = MibScalar
sysHighAvailabilityEnable = _SysHighAvailabilityEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 58),
    _SysHighAvailabilityEnable_Type()
)
sysHighAvailabilityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHighAvailabilityEnable.setStatus("current")


class _SysHighAvailabilityVersioningEnable_Type(TruthValue):
    """Custom type sysHighAvailabilityVersioningEnable based on TruthValue"""


_SysHighAvailabilityVersioningEnable_Object = MibScalar
sysHighAvailabilityVersioningEnable = _SysHighAvailabilityVersioningEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 59),
    _SysHighAvailabilityVersioningEnable_Type()
)
sysHighAvailabilityVersioningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysHighAvailabilityVersioningEnable.setStatus("current")


class _SysHighAvailabilityOperStatus_Type(Integer32):
    """Custom type sysHighAvailabilityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRunning", 2),
          ("running", 1))
    )


_SysHighAvailabilityOperStatus_Type.__name__ = "Integer32"
_SysHighAvailabilityOperStatus_Object = MibScalar
sysHighAvailabilityOperStatus = _SysHighAvailabilityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 60),
    _SysHighAvailabilityOperStatus_Type()
)
sysHighAvailabilityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHighAvailabilityOperStatus.setStatus("current")
_SysHighAvailabilityNotRunningReason_Type = DisplayString
_SysHighAvailabilityNotRunningReason_Object = MibScalar
sysHighAvailabilityNotRunningReason = _SysHighAvailabilityNotRunningReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 61),
    _SysHighAvailabilityNotRunningReason_Type()
)
sysHighAvailabilityNotRunningReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysHighAvailabilityNotRunningReason.setStatus("current")


class _SysExtendedRmonNetflowModuleMask_Type(Bits):
    """Custom type sysExtendedRmonNetflowModuleMask based on Bits"""
    namedValues = NamedValues(
        *(("module1", 0),
          ("module10", 9),
          ("module11", 10),
          ("module12", 11),
          ("module13", 12),
          ("module14", 13),
          ("module15", 14),
          ("module16", 15),
          ("module2", 1),
          ("module3", 2),
          ("module4", 3),
          ("module5", 4),
          ("module6", 5),
          ("module7", 6),
          ("module8", 7),
          ("module9", 8))
    )

_SysExtendedRmonNetflowModuleMask_Type.__name__ = "Bits"
_SysExtendedRmonNetflowModuleMask_Object = MibScalar
sysExtendedRmonNetflowModuleMask = _SysExtendedRmonNetflowModuleMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 62),
    _SysExtendedRmonNetflowModuleMask_Type()
)
sysExtendedRmonNetflowModuleMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysExtendedRmonNetflowModuleMask.setStatus("current")


class _SshPublicKeySize_Type(Integer32):
    """Custom type sshPublicKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(512, 2048),
    )


_SshPublicKeySize_Type.__name__ = "Integer32"
_SshPublicKeySize_Object = MibScalar
sshPublicKeySize = _SshPublicKeySize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 63),
    _SshPublicKeySize_Type()
)
sshPublicKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshPublicKeySize.setStatus("current")


class _SysMaxRmonMemory_Type(Integer32):
    """Custom type sysMaxRmonMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_SysMaxRmonMemory_Type.__name__ = "Integer32"
_SysMaxRmonMemory_Object = MibScalar
sysMaxRmonMemory = _SysMaxRmonMemory_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 64),
    _SysMaxRmonMemory_Type()
)
sysMaxRmonMemory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMaxRmonMemory.setStatus("current")
_SysMacReductionAdminEnable_Type = TruthValue
_SysMacReductionAdminEnable_Object = MibScalar
sysMacReductionAdminEnable = _SysMacReductionAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 65),
    _SysMacReductionAdminEnable_Type()
)
sysMacReductionAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMacReductionAdminEnable.setStatus("current")
_SysMacReductionOperEnable_Type = TruthValue
_SysMacReductionOperEnable_Object = MibScalar
sysMacReductionOperEnable = _SysMacReductionOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 66),
    _SysMacReductionOperEnable_Type()
)
sysMacReductionOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysMacReductionOperEnable.setStatus("current")


class _SysStatus_Type(Integer32):
    """Custom type sysStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_SysStatus_Type.__name__ = "Integer32"
_SysStatus_Object = MibScalar
sysStatus = _SysStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 1, 67),
    _SysStatus_Type()
)
sysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysStatus.setStatus("current")
_ChassisGrp_ObjectIdentity = ObjectIdentity
chassisGrp = _ChassisGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2)
)


class _ChassisSysType_Type(Integer32):
    """Custom type chassisSysType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              40,
              41,
              42,
              43,
              45,
              48,
              51,
              52,
              54,
              55,
              56)
        )
    )
    namedValues = NamedValues(
        *(("c6807xl", 55),
          ("c6880x", 56),
          ("c6880xle", 54),
          ("cisco7603", 30),
          ("cisco7603s", 52),
          ("cisco7604", 42),
          ("cisco7606", 31),
          ("cisco7609", 32),
          ("cisco7613", 40),
          ("mec6524gs8s", 45),
          ("mec6524gt8s", 48),
          ("other", 1),
          ("wsc1000", 3),
          ("wsc1001", 4),
          ("wsc1100", 5),
          ("wsc1200", 11),
          ("wsc1400", 12),
          ("wsc2900", 7),
          ("wsc2926", 13),
          ("wsc2948g", 20),
          ("wsc2948ggetx", 41),
          ("wsc2980g", 26),
          ("wsc2980ga", 28),
          ("wsc4003", 17),
          ("wsc4006", 24),
          ("wsc4503", 36),
          ("wsc4506", 37),
          ("wsc4507", 35),
          ("wsc4912g", 19),
          ("wsc5000", 6),
          ("wsc5002", 9),
          ("wsc5500", 8),
          ("wsc5500e", 18),
          ("wsc5505", 10),
          ("wsc5509", 14),
          ("wsc6006", 15),
          ("wsc6009", 16),
          ("wsc6503", 33),
          ("wsc6504e", 43),
          ("wsc6506", 23),
          ("wsc6509", 22),
          ("wsc6509NEB", 25),
          ("wsc6509NEBA", 34),
          ("wsc6509ve", 51),
          ("wsc6513", 27),
          ("wsc65509", 38))
    )


_ChassisSysType_Type.__name__ = "Integer32"
_ChassisSysType_Object = MibScalar
chassisSysType = _ChassisSysType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 1),
    _ChassisSysType_Type()
)
chassisSysType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSysType.setStatus("current")


class _ChassisBkplType_Type(Integer32):
    """Custom type chassisBkplType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fddi", 2),
          ("fddiEthernet", 3),
          ("giga", 4),
          ("giga12", 7),
          ("giga16", 8),
          ("giga3", 5),
          ("giga3E", 6),
          ("giga40", 9),
          ("other", 1))
    )


_ChassisBkplType_Type.__name__ = "Integer32"
_ChassisBkplType_Object = MibScalar
chassisBkplType = _ChassisBkplType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 2),
    _ChassisBkplType_Type()
)
chassisBkplType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisBkplType.setStatus("current")


class _ChassisPs1Type_Type(Integer32):
    """Custom type chassisPs1Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              42,
              43,
              44,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              58,
              59,
              60,
              63,
              64,
              105,
              106,
              150,
              151,
              152)
        )
    )
    namedValues = NamedValues(
        *(("c6800xl3kwac", 152),
          ("c6880x3kwac", 150),
          ("c6880x3kwdc", 151),
          ("externalPS", 29),
          ("none", 2),
          ("other", 1),
          ("pwr1400ac", 51),
          ("pwr1500dc", 106),
          ("pwr1900ac", 37),
          ("pwr1900ac6", 39),
          ("pwr1900dc", 38),
          ("pwr2700ac", 54),
          ("pwr2700ac4", 59),
          ("pwr2700dc", 55),
          ("pwr2700dc4", 60),
          ("pwr4000dc", 34),
          ("pwr400ac", 64),
          ("pwr400dc", 63),
          ("pwr6000dc", 105),
          ("pwr950ac", 35),
          ("pwr950dc", 36),
          ("pwrc451000ac", 46),
          ("pwrc451300acv", 48),
          ("pwrc451400dcp", 49),
          ("pwrc452800acv", 47),
          ("w120", 28),
          ("w130", 7),
          ("w155", 15),
          ("w156", 52),
          ("w175", 10),
          ("w175dc", 17),
          ("w175pfc", 16),
          ("w200", 4),
          ("w50", 3),
          ("w600", 5),
          ("w80", 6),
          ("wsc5008", 8),
          ("wsc5008a", 9),
          ("wsc5008b", 18),
          ("wsc5008c", 19),
          ("wsc5068", 11),
          ("wsc5068b", 20),
          ("wsc5508", 12),
          ("wsc5508a", 14),
          ("wsc5518", 26),
          ("wsc5568", 13),
          ("wsc5598", 27),
          ("wscac1000", 21),
          ("wscac1300", 22),
          ("wscac2500w", 30),
          ("wscac3000w", 44),
          ("wscac4000w", 33),
          ("wscac6000w", 53),
          ("wscac8700we", 58),
          ("wscdc1000", 23),
          ("wscdc1360", 24),
          ("wscdc2500w", 31),
          ("wscdc3000w", 50),
          ("wsx4008", 25),
          ("wsx4008ac650w", 42),
          ("wsx4008dc", 32),
          ("wsx4008dc650w", 43))
    )


_ChassisPs1Type_Type.__name__ = "Integer32"
_ChassisPs1Type_Object = MibScalar
chassisPs1Type = _ChassisPs1Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 3),
    _ChassisPs1Type_Type()
)
chassisPs1Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1Type.setStatus("current")


class _ChassisPs1Status_Type(Integer32):
    """Custom type chassisPs1Status based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisPs1Status_Type.__name__ = "Integer32"
_ChassisPs1Status_Object = MibScalar
chassisPs1Status = _ChassisPs1Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 4),
    _ChassisPs1Status_Type()
)
chassisPs1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1Status.setStatus("current")


class _ChassisPs1TestResult_Type(Integer32):
    """Custom type chassisPs1TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisPs1TestResult_Type.__name__ = "Integer32"
_ChassisPs1TestResult_Object = MibScalar
chassisPs1TestResult = _ChassisPs1TestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 5),
    _ChassisPs1TestResult_Type()
)
chassisPs1TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs1TestResult.setStatus("current")


class _ChassisPs2Type_Type(Integer32):
    """Custom type chassisPs2Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              42,
              43,
              44,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              58,
              59,
              60,
              63,
              64,
              105,
              106,
              150,
              151,
              152)
        )
    )
    namedValues = NamedValues(
        *(("c6800xl3kwac", 152),
          ("c6880x3kwac", 150),
          ("c6880x3kwdc", 151),
          ("externalPS", 29),
          ("none", 2),
          ("other", 1),
          ("pwr1400ac", 51),
          ("pwr1500dc", 106),
          ("pwr1900ac", 37),
          ("pwr1900ac6", 39),
          ("pwr1900dc", 38),
          ("pwr2700ac", 54),
          ("pwr2700ac4", 59),
          ("pwr2700dc", 55),
          ("pwr2700dc4", 60),
          ("pwr4000dc", 34),
          ("pwr400ac", 64),
          ("pwr400dc", 63),
          ("pwr6000dc", 105),
          ("pwr950ac", 35),
          ("pwr950dc", 36),
          ("pwrc451000ac", 46),
          ("pwrc451300acv", 48),
          ("pwrc451400dcp", 49),
          ("pwrc452800acv", 47),
          ("w120", 28),
          ("w130", 7),
          ("w155", 15),
          ("w156", 52),
          ("w175", 10),
          ("w175dc", 17),
          ("w175pfc", 16),
          ("w200", 4),
          ("w50", 3),
          ("w600", 5),
          ("w80", 6),
          ("wsc5008", 8),
          ("wsc5008a", 9),
          ("wsc5008b", 18),
          ("wsc5008c", 19),
          ("wsc5068", 11),
          ("wsc5068b", 20),
          ("wsc5508", 12),
          ("wsc5508a", 14),
          ("wsc5518", 26),
          ("wsc5568", 13),
          ("wsc5598", 27),
          ("wscac1000", 21),
          ("wscac1300", 22),
          ("wscac2500w", 30),
          ("wscac3000w", 44),
          ("wscac4000w", 33),
          ("wscac6000w", 53),
          ("wscac8700we", 58),
          ("wscdc1000", 23),
          ("wscdc1360", 24),
          ("wscdc2500w", 31),
          ("wscdc3000w", 50),
          ("wsx4008", 25),
          ("wsx4008ac650w", 42),
          ("wsx4008dc", 32),
          ("wsx4008dc650w", 43))
    )


_ChassisPs2Type_Type.__name__ = "Integer32"
_ChassisPs2Type_Object = MibScalar
chassisPs2Type = _ChassisPs2Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 6),
    _ChassisPs2Type_Type()
)
chassisPs2Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2Type.setStatus("current")


class _ChassisPs2Status_Type(Integer32):
    """Custom type chassisPs2Status based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisPs2Status_Type.__name__ = "Integer32"
_ChassisPs2Status_Object = MibScalar
chassisPs2Status = _ChassisPs2Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 7),
    _ChassisPs2Status_Type()
)
chassisPs2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2Status.setStatus("current")


class _ChassisPs2TestResult_Type(Integer32):
    """Custom type chassisPs2TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisPs2TestResult_Type.__name__ = "Integer32"
_ChassisPs2TestResult_Object = MibScalar
chassisPs2TestResult = _ChassisPs2TestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 8),
    _ChassisPs2TestResult_Type()
)
chassisPs2TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs2TestResult.setStatus("current")


class _ChassisFanStatus_Type(Integer32):
    """Custom type chassisFanStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisFanStatus_Type.__name__ = "Integer32"
_ChassisFanStatus_Object = MibScalar
chassisFanStatus = _ChassisFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 9),
    _ChassisFanStatus_Type()
)
chassisFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanStatus.setStatus("current")


class _ChassisFanTestResult_Type(Integer32):
    """Custom type chassisFanTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisFanTestResult_Type.__name__ = "Integer32"
_ChassisFanTestResult_Object = MibScalar
chassisFanTestResult = _ChassisFanTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 10),
    _ChassisFanTestResult_Type()
)
chassisFanTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisFanTestResult.setStatus("current")


class _ChassisMinorAlarm_Type(Integer32):
    """Custom type chassisMinorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChassisMinorAlarm_Type.__name__ = "Integer32"
_ChassisMinorAlarm_Object = MibScalar
chassisMinorAlarm = _ChassisMinorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 11),
    _ChassisMinorAlarm_Type()
)
chassisMinorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMinorAlarm.setStatus("current")


class _ChassisMajorAlarm_Type(Integer32):
    """Custom type chassisMajorAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ChassisMajorAlarm_Type.__name__ = "Integer32"
_ChassisMajorAlarm_Object = MibScalar
chassisMajorAlarm = _ChassisMajorAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 12),
    _ChassisMajorAlarm_Type()
)
chassisMajorAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisMajorAlarm.setStatus("current")


class _ChassisTempAlarm_Type(Integer32):
    """Custom type chassisTempAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("critical", 3),
          ("off", 1),
          ("on", 2))
    )


_ChassisTempAlarm_Type.__name__ = "Integer32"
_ChassisTempAlarm_Object = MibScalar
chassisTempAlarm = _ChassisTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 13),
    _ChassisTempAlarm_Type()
)
chassisTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisTempAlarm.setStatus("current")


class _ChassisNumSlots_Type(Integer32):
    """Custom type chassisNumSlots based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ChassisNumSlots_Type.__name__ = "Integer32"
_ChassisNumSlots_Object = MibScalar
chassisNumSlots = _ChassisNumSlots_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 14),
    _ChassisNumSlots_Type()
)
chassisNumSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisNumSlots.setStatus("current")


class _ChassisSlotConfig_Type(Integer32):
    """Custom type chassisSlotConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisSlotConfig_Type.__name__ = "Integer32"
_ChassisSlotConfig_Object = MibScalar
chassisSlotConfig = _ChassisSlotConfig_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 15),
    _ChassisSlotConfig_Type()
)
chassisSlotConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSlotConfig.setStatus("current")


class _ChassisModel_Type(DisplayString):
    """Custom type chassisModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChassisModel_Type.__name__ = "DisplayString"
_ChassisModel_Object = MibScalar
chassisModel = _ChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 16),
    _ChassisModel_Type()
)
chassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisModel.setStatus("current")


class _ChassisSerialNumber_Type(Integer32):
    """Custom type chassisSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_ChassisSerialNumber_Type.__name__ = "Integer32"
_ChassisSerialNumber_Object = MibScalar
chassisSerialNumber = _ChassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 17),
    _ChassisSerialNumber_Type()
)
chassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumber.setStatus("deprecated")
_ChassisComponentTable_Object = MibTable
chassisComponentTable = _ChassisComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18)
)
if mibBuilder.loadTexts:
    chassisComponentTable.setStatus("deprecated")
_ChassisComponentEntry_Object = MibTableRow
chassisComponentEntry = _ChassisComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18, 1)
)
chassisComponentEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "chassisComponentIndex"),
)
if mibBuilder.loadTexts:
    chassisComponentEntry.setStatus("deprecated")


class _ChassisComponentIndex_Type(Integer32):
    """Custom type chassisComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ChassisComponentIndex_Type.__name__ = "Integer32"
_ChassisComponentIndex_Object = MibTableColumn
chassisComponentIndex = _ChassisComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18, 1, 1),
    _ChassisComponentIndex_Type()
)
chassisComponentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisComponentIndex.setStatus("deprecated")


class _ChassisComponentType_Type(Integer32):
    """Custom type chassisComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              10,
              11,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              25,
              26,
              27)
        )
    )
    namedValues = NamedValues(
        *(("c6800xl33vcon", 27),
          ("c6807xlFan", 26),
          ("c6880xFan", 25),
          ("clk7600", 6),
          ("fan6524", 16),
          ("fanMod3Hs", 21),
          ("fanMod4Hs", 15),
          ("fanMod6Shs", 17),
          ("fanMod9", 8),
          ("fanMod9Shs", 18),
          ("fanMod9St", 19),
          ("unknown", 1),
          ("ws9SlotFan", 7),
          ("wsc6000cl", 2),
          ("wsc6000tempSensor", 4),
          ("wsc6000vtt", 3),
          ("wsc6000vtte", 14),
          ("wsc6503eFan", 13),
          ("wsc6506eFan", 10),
          ("wsc6509eFan", 11),
          ("wsc6509veFan", 20),
          ("wsc6513Clock", 5))
    )


_ChassisComponentType_Type.__name__ = "Integer32"
_ChassisComponentType_Object = MibTableColumn
chassisComponentType = _ChassisComponentType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18, 1, 2),
    _ChassisComponentType_Type()
)
chassisComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisComponentType.setStatus("deprecated")


class _ChassisComponentSerialNumber_Type(DisplayString):
    """Custom type chassisComponentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChassisComponentSerialNumber_Type.__name__ = "DisplayString"
_ChassisComponentSerialNumber_Object = MibTableColumn
chassisComponentSerialNumber = _ChassisComponentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18, 1, 3),
    _ChassisComponentSerialNumber_Type()
)
chassisComponentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisComponentSerialNumber.setStatus("deprecated")


class _ChassisComponentHwVersion_Type(DisplayString):
    """Custom type chassisComponentHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChassisComponentHwVersion_Type.__name__ = "DisplayString"
_ChassisComponentHwVersion_Object = MibTableColumn
chassisComponentHwVersion = _ChassisComponentHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18, 1, 4),
    _ChassisComponentHwVersion_Type()
)
chassisComponentHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisComponentHwVersion.setStatus("deprecated")


class _ChassisComponentModel_Type(DisplayString):
    """Custom type chassisComponentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChassisComponentModel_Type.__name__ = "DisplayString"
_ChassisComponentModel_Object = MibTableColumn
chassisComponentModel = _ChassisComponentModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 18, 1, 5),
    _ChassisComponentModel_Type()
)
chassisComponentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisComponentModel.setStatus("deprecated")


class _ChassisSerialNumberString_Type(DisplayString):
    """Custom type chassisSerialNumberString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ChassisSerialNumberString_Type.__name__ = "DisplayString"
_ChassisSerialNumberString_Object = MibScalar
chassisSerialNumberString = _ChassisSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 19),
    _ChassisSerialNumberString_Type()
)
chassisSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisSerialNumberString.setStatus("current")


class _ChassisPs3Type_Type(Integer32):
    """Custom type chassisPs3Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              25,
              32,
              42,
              43)
        )
    )
    namedValues = NamedValues(
        *(("none", 2),
          ("other", 1),
          ("wsx4008", 25),
          ("wsx4008ac650w", 42),
          ("wsx4008dc", 32),
          ("wsx4008dc650w", 43))
    )


_ChassisPs3Type_Type.__name__ = "Integer32"
_ChassisPs3Type_Object = MibScalar
chassisPs3Type = _ChassisPs3Type_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 20),
    _ChassisPs3Type_Type()
)
chassisPs3Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs3Type.setStatus("current")


class _ChassisPs3Status_Type(Integer32):
    """Custom type chassisPs3Status based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ChassisPs3Status_Type.__name__ = "Integer32"
_ChassisPs3Status_Object = MibScalar
chassisPs3Status = _ChassisPs3Status_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 21),
    _ChassisPs3Status_Type()
)
chassisPs3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs3Status.setStatus("current")


class _ChassisPs3TestResult_Type(Integer32):
    """Custom type chassisPs3TestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ChassisPs3TestResult_Type.__name__ = "Integer32"
_ChassisPs3TestResult_Object = MibScalar
chassisPs3TestResult = _ChassisPs3TestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 22),
    _ChassisPs3TestResult_Type()
)
chassisPs3TestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPs3TestResult.setStatus("current")
_ChassisPEMInstalled_Type = TruthValue
_ChassisPEMInstalled_Object = MibScalar
chassisPEMInstalled = _ChassisPEMInstalled_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 2, 23),
    _ChassisPEMInstalled_Type()
)
chassisPEMInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chassisPEMInstalled.setStatus("current")
_ModuleGrp_ObjectIdentity = ObjectIdentity
moduleGrp = _ModuleGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleEntry_Object = MibTableRow
moduleEntry = _ModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1)
)
moduleEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleEntry.setStatus("current")


class _ModuleIndex_Type(Integer32):
    """Custom type moduleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModuleIndex_Type.__name__ = "Integer32"
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("current")


class _ModuleType_Type(Integer32):
    """Custom type moduleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              52,
              53,
              54,
              55,
              56,
              57,
              61,
              62,
              65,
              66,
              67,
              68,
              69,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              81,
              82,
              83,
              84,
              85,
              87,
              88,
              91,
              92,
              96,
              200,
              201,
              202,
              203,
              204,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              216,
              217,
              218,
              219,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              229,
              230,
              231,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241,
              242,
              243,
              244,
              245,
              246,
              247,
              248,
              249,
              250,
              251,
              252,
              253,
              254,
              255,
              258,
              259,
              260,
              261,
              265,
              266,
              267,
              268,
              269,
              270,
              271,
              272,
              273,
              274,
              275,
              276,
              277,
              278,
              279,
              280,
              281,
              282,
              284,
              285,
              286,
              289,
              290,
              291,
              292,
              293,
              294,
              295,
              296,
              297,
              300,
              301,
              302,
              303,
              304,
              305,
              306,
              307,
              309,
              310,
              311,
              312,
              313,
              317,
              318,
              319,
              320,
              321,
              322,
              323,
              324,
              325,
              326,
              330,
              331,
              332,
              334,
              337,
              339,
              340,
              341,
              342,
              343,
              345,
              346,
              502,
              503,
              506,
              507,
              509,
              510,
              511,
              512,
              515,
              516,
              597,
              598,
              599,
              600,
              601,
              602,
              603,
              604,
              605,
              606,
              607,
              608,
              609,
              610,
              611,
              612,
              613,
              614,
              615,
              616,
              617,
              618,
              620,
              625,
              626,
              627,
              629,
              633,
              634,
              903,
              910,
              911,
              912,
              913,
              914,
              915,
              919,
              920,
              921,
              923,
              924,
              925,
              926,
              927,
              928,
              929,
              930,
              936,
              940,
              946,
              947,
              949,
              950,
              951,
              1001,
              1002,
              1004,
              1007,
              1008,
              1009,
              1010,
              1016,
              1021,
              1023,
              1027,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1039,
              1040,
              1042,
              1043,
              1101,
              1102,
              1103,
              1104,
              1105,
              1106,
              1301,
              1304,
              1400,
              1401,
              1402,
              1403,
              1800,
              1801,
              1805)
        )
    )
    namedValues = NamedValues(
        *(("ace046500k9", 936),
          ("ace106500k9", 926),
          ("c6800ia48fpd", 1304),
          ("c6800ia48td", 1301),
          ("c6880x", 1401),
          ("c6880x16p10g", 1400),
          ("c6880xle", 1403),
          ("c6880xle16p10g", 1402),
          ("c7600Es2Tg3c", 629),
          ("c7600Es2Tg3cxl", 620),
          ("c7600Es4Tg3c", 627),
          ("c7600Es4Tg3cxl", 618),
          ("c7600msfc4", 1805),
          ("c7600ssc400", 1104),
          ("c7600ssc600", 1105),
          ("c76EsXt2Tg3c", 634),
          ("c76EsXt2Tg3cxl", 626),
          ("c76EsXt4Tg3c", 633),
          ("c76EsXt4Tg3cxl", 625),
          ("empty", 2),
          ("esm2x10ge", 1106),
          ("m7600Sip200", 1102),
          ("m7600Sip400", 1103),
          ("m7600Sip600", 1004),
          ("me6524msfc2a", 598),
          ("mec6524gs8s", 511),
          ("mec6524gt8s", 512),
          ("osm12ct3T1", 600),
          ("osm12t3e3", 601),
          ("osm16oc3PosMM", 246),
          ("osm16oc3PosSI", 247),
          ("osm16oc3PosSIPlus", 610),
          ("osm16oc3PosSL", 248),
          ("osm1choc12T1SI", 297),
          ("osm1choc12T3SI", 604),
          ("osm1choc48T3SI", 279),
          ("osm1choc48T3SS", 276),
          ("osm1oc48PosSI", 242),
          ("osm1oc48PosSIPlus", 612),
          ("osm1oc48PosSL", 243),
          ("osm1oc48PosSLPlus", 613),
          ("osm1oc48PosSS", 241),
          ("osm1oc48PosSSPlus", 611),
          ("osm24t3e3", 602),
          ("osm2choc12T3SI", 605),
          ("osm2choc48T3SI", 280),
          ("osm2choc48T3SS", 277),
          ("osm2oc12AtmMM", 213),
          ("osm2oc12AtmMMPlus", 606),
          ("osm2oc12AtmSI", 214),
          ("osm2oc12AtmSIPlus", 607),
          ("osm2oc12PosMM", 249),
          ("osm2oc12PosMMPlus", 608),
          ("osm2oc12PosSI", 250),
          ("osm2oc12PosSIPlus", 609),
          ("osm2oc12PosSL", 251),
          ("osm2oc48OneDptSI", 266),
          ("osm2oc48OneDptSIDual", 269),
          ("osm2oc48OneDptSL", 267),
          ("osm2oc48OneDptSLDual", 270),
          ("osm2oc48OneDptSS", 265),
          ("osm2oc48OneDptSSDual", 268),
          ("osm4GeWanGbicPlus", 603),
          ("osm4choc12T3MM", 272),
          ("osm4choc12T3SI", 273),
          ("osm4choc3DS0SI", 296),
          ("osm4geWanGbic", 240),
          ("osm4oc12PosMM", 216),
          ("osm4oc12PosSI", 217),
          ("osm4oc12PosSIPlus", 617),
          ("osm4oc12PosSL", 218),
          ("osm4oc3PosMM", 289),
          ("osm4oc3PosSI", 286),
          ("osm4oc3PosSIPlus", 614),
          ("osm8choc12T3MM", 274),
          ("osm8choc12T3SI", 275),
          ("osm8choc3DS0SI", 295),
          ("osm8oc3PosMM", 253),
          ("osm8oc3PosSI", 254),
          ("osm8oc3PosSIPlus", 616),
          ("osm8oc3PosSL", 255),
          ("osm8oc3PosSLPlus", 615),
          ("other", 1),
          ("rsp720", 1800),
          ("rsp720base", 1801),
          ("vss72010g", 1021),
          ("vssup2t10g", 1031),
          ("wsSvcAdm1k9", 929),
          ("wsSvcAgm1k9", 930),
          ("wsSvcAon1k9", 925),
          ("wsSvcAsaSm1", 947),
          ("wsSvcAsaSm1k7", 950),
          ("wsSvcCe1", 293),
          ("wsSvcCmm", 284),
          ("wsSvcCsg1", 911),
          ("wsSvcFwm1", 292),
          ("wsSvcIdsm2", 290),
          ("wsSvcIpSec1", 903),
          ("wsSvcMwam1", 910),
          ("wsSvcNam1", 914),
          ("wsSvcNam2", 291),
          ("wsSvcNam3k9", 949),
          ("wsSvcPsd1", 919),
          ("wsSvcSamiBb", 940),
          ("wsSvcSsl1", 294),
          ("wsSvcVse1k9", 951),
          ("wsSvcWebVpnk9", 927),
          ("wsSvcWism2k9", 946),
          ("wsSvcWlan1k9", 924),
          ("wsc1000", 3),
          ("wsc1001", 4),
          ("wsc1100", 5),
          ("wsc1200", 11),
          ("wsc1400", 12),
          ("wsc6500sfm", 245),
          ("wsf5541", 88),
          ("wsf6kmsfc", 207),
          ("wsf6kmsfc2", 234),
          ("wsf6kmsfc2a", 599),
          ("wssup3210ge3b", 510),
          ("wssup32ge3b", 509),
          ("wssup32p10ge", 516),
          ("wssup32pge", 515),
          ("wssup720", 1001),
          ("wssup720base", 1002),
          ("wssvcpisa32", 597),
          ("wsx1431", 19),
          ("wsx1434", 22),
          ("wsx1436", 21),
          ("wsx1441", 13),
          ("wsx1444", 14),
          ("wsx1450", 15),
          ("wsx1454", 17),
          ("wsx1455", 18),
          ("wsx1465", 20),
          ("wsx1483", 16),
          ("wsx2948", 309),
          ("wsx2948gbrj", 307),
          ("wsx2948ggetx", 345),
          ("wsx2948ggetxgbrj", 346),
          ("wsx2980", 322),
          ("wsx2980gbrj", 324),
          ("wsx2980rj", 323),
          ("wsx4012", 300),
          ("wsx4013", 318),
          ("wsx4019", 325),
          ("wsx4124fxmt", 317),
          ("wsx4148fxmt", 331),
          ("wsx4148lxmt", 337),
          ("wsx4148rj", 301),
          ("wsx4148rj21", 313),
          ("wsx4148rj45v", 326),
          ("wsx4232gbrj", 302),
          ("wsx4232l3", 319),
          ("wsx4232rjxx", 312),
          ("wsx4248rj21v", 341),
          ("wsx4248rj45v", 343),
          ("wsx4302gb", 342),
          ("wsx4306gb", 303),
          ("wsx44122Gbtx", 321),
          ("wsx44162gbtx", 305),
          ("wsx4418gb", 304),
          ("wsx4424gbrj45", 330),
          ("wsx4424sxmt", 311),
          ("wsx4448gblx", 332),
          ("wsx4448gbrj45", 334),
          ("wsx4548gbrj45", 339),
          ("wsx4548gbrj45v", 340),
          ("wsx4604gwy", 320),
          ("wsx4912", 310),
          ("wsx4912gb", 306),
          ("wsx5005", 39),
          ("wsx5006", 38),
          ("wsx5009", 23),
          ("wsx5010", 26),
          ("wsx5011", 25),
          ("wsx5012", 50),
          ("wsx5012a", 81),
          ("wsx5013", 24),
          ("wsx5014", 75),
          ("wsx5015", 76),
          ("wsx5020", 37),
          ("wsx5030", 46),
          ("wsx5031", 67),
          ("wsx5101", 28),
          ("wsx5103", 29),
          ("wsx5104", 30),
          ("wsx5111", 35),
          ("wsx5113", 27),
          ("wsx5114", 47),
          ("wsx5153", 34),
          ("wsx5154", 33),
          ("wsx5155", 32),
          ("wsx5156", 43),
          ("wsx5157", 44),
          ("wsx5158", 45),
          ("wsx5161", 61),
          ("wsx5162", 62),
          ("wsx5165", 65),
          ("wsx5166", 66),
          ("wsx5167", 82),
          ("wsx5168", 84),
          ("wsx5201", 55),
          ("wsx5201r", 73),
          ("wsx5203", 56),
          ("wsx5213", 36),
          ("wsx5213a", 53),
          ("wsx5223", 48),
          ("wsx5224", 49),
          ("wsx5225r", 74),
          ("wsx5234", 79),
          ("wsx5236", 77),
          ("wsx5237", 96),
          ("wsx5239", 83),
          ("wsx5302", 52),
          ("wsx5305", 85),
          ("wsx5380", 54),
          ("wsx5403", 69),
          ("wsx5410", 68),
          ("wsx5505", 42),
          ("wsx5506", 41),
          ("wsx5509", 40),
          ("wsx5530", 57),
          ("wsx5534", 91),
          ("wsx5536", 92),
          ("wsx5540", 78),
          ("wsx5550", 87),
          ("wsx6024flmt", 208),
          ("wsx6066SlbApc", 260),
          ("wsx6066SlbSk9", 920),
          ("wsx6101oc12mmf", 209),
          ("wsx6101oc12smf", 210),
          ("wsx6148FeSfp", 928),
          ("wsx6148agetx", 921),
          ("wsx6148arj45", 923),
          ("wsx6148ege45at", 1032),
          ("wsx6148egetx", 1036),
          ("wsx6148getx", 503),
          ("wsx6148rj21v", 913),
          ("wsx6148rj45v", 912),
          ("wsx6148x2rj45", 506),
          ("wsx61822pa", 212),
          ("wsx6196rj21", 507),
          ("wsx6224ammmt", 222),
          ("wsx6224mmmt", 202),
          ("wsx6248arj45", 224),
          ("wsx6248atel", 225),
          ("wsx6248rj45", 203),
          ("wsx6248tel", 204),
          ("wsx6302amsm", 220),
          ("wsx6302msm", 206),
          ("wsx6316getx", 233),
          ("wsx6324mmmt", 235),
          ("wsx6324sm", 238),
          ("wsx6348rj21", 281),
          ("wsx6348rj45", 236),
          ("wsx6380nam", 223),
          ("wsx6381ids", 244),
          ("wsx6408agbic", 226),
          ("wsx6408gbic", 201),
          ("wsx6416gbic", 221),
          ("wsx6416gemt", 211),
          ("wsx6500sfm2", 278),
          ("wsx650110gex4", 285),
          ("wsx650210ge", 252),
          ("wsx6516aGbic", 502),
          ("wsx6516gbic", 239),
          ("wsx6516getx", 261),
          ("wsx6524mmmt", 259),
          ("wsx6548getx", 915),
          ("wsx6548rj21", 282),
          ("wsx6548rj45", 258),
          ("wsx65822pa", 1101),
          ("wsx6608e1", 230),
          ("wsx6608t1", 229),
          ("wsx6624fxs", 231),
          ("wsx670410ge", 1008),
          ("wsx670810ge", 1016),
          ("wsx6708a10ge", 1023),
          ("wsx671610ge", 1027),
          ("wsx671610t", 1033),
          ("wsx6724sfp", 1010),
          ("wsx6748getx", 1007),
          ("wsx6748sfp", 1009),
          ("wsx681610ge", 1042),
          ("wsx681610t", 1043),
          ("wsx6816gbic", 271),
          ("wsx6824sfp", 1040),
          ("wsx6848sfp", 1039),
          ("wsx6848tx", 1037),
          ("wsx690440g", 1035),
          ("wsx690810g", 1034),
          ("wsx6ksup12ge", 200),
          ("wsx6ksup1a2ge", 219),
          ("wsx6ksup22ge", 237))
    )


_ModuleType_Type.__name__ = "Integer32"
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 2),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")


class _ModuleSerialNumber_Type(Integer32):
    """Custom type moduleSerialNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999999999),
    )


_ModuleSerialNumber_Type.__name__ = "Integer32"
_ModuleSerialNumber_Object = MibTableColumn
moduleSerialNumber = _ModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 3),
    _ModuleSerialNumber_Type()
)
moduleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSerialNumber.setStatus("deprecated")


class _ModuleHwHiVersion_Type(Integer32):
    """Custom type moduleHwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleHwHiVersion_Type.__name__ = "Integer32"
_ModuleHwHiVersion_Object = MibTableColumn
moduleHwHiVersion = _ModuleHwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 4),
    _ModuleHwHiVersion_Type()
)
moduleHwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwHiVersion.setStatus("deprecated")


class _ModuleHwLoVersion_Type(Integer32):
    """Custom type moduleHwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleHwLoVersion_Type.__name__ = "Integer32"
_ModuleHwLoVersion_Object = MibTableColumn
moduleHwLoVersion = _ModuleHwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 5),
    _ModuleHwLoVersion_Type()
)
moduleHwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwLoVersion.setStatus("deprecated")


class _ModuleFwHiVersion_Type(Integer32):
    """Custom type moduleFwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleFwHiVersion_Type.__name__ = "Integer32"
_ModuleFwHiVersion_Object = MibTableColumn
moduleFwHiVersion = _ModuleFwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 6),
    _ModuleFwHiVersion_Type()
)
moduleFwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFwHiVersion.setStatus("deprecated")


class _ModuleFwLoVersion_Type(Integer32):
    """Custom type moduleFwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleFwLoVersion_Type.__name__ = "Integer32"
_ModuleFwLoVersion_Object = MibTableColumn
moduleFwLoVersion = _ModuleFwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 7),
    _ModuleFwLoVersion_Type()
)
moduleFwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFwLoVersion.setStatus("deprecated")


class _ModuleSwHiVersion_Type(Integer32):
    """Custom type moduleSwHiVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleSwHiVersion_Type.__name__ = "Integer32"
_ModuleSwHiVersion_Object = MibTableColumn
moduleSwHiVersion = _ModuleSwHiVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 8),
    _ModuleSwHiVersion_Type()
)
moduleSwHiVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwHiVersion.setStatus("deprecated")


class _ModuleSwLoVersion_Type(Integer32):
    """Custom type moduleSwLoVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleSwLoVersion_Type.__name__ = "Integer32"
_ModuleSwLoVersion_Object = MibTableColumn
moduleSwLoVersion = _ModuleSwLoVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 9),
    _ModuleSwLoVersion_Type()
)
moduleSwLoVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwLoVersion.setStatus("deprecated")


class _ModuleStatus_Type(Integer32):
    """Custom type moduleStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_ModuleStatus_Type.__name__ = "Integer32"
_ModuleStatus_Object = MibTableColumn
moduleStatus = _ModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 10),
    _ModuleStatus_Type()
)
moduleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStatus.setStatus("current")


class _ModuleTestResult_Type(Integer32):
    """Custom type moduleTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ModuleTestResult_Type.__name__ = "Integer32"
_ModuleTestResult_Object = MibTableColumn
moduleTestResult = _ModuleTestResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 11),
    _ModuleTestResult_Type()
)
moduleTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTestResult.setStatus("current")


class _ModuleAction_Type(Integer32):
    """Custom type moduleAction based on Integer32"""
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
        *(("disable", 4),
          ("enable", 3),
          ("other", 1),
          ("reset", 2))
    )


_ModuleAction_Type.__name__ = "Integer32"
_ModuleAction_Object = MibTableColumn
moduleAction = _ModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 12),
    _ModuleAction_Type()
)
moduleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleAction.setStatus("current")


class _ModuleName_Type(DisplayString):
    """Custom type moduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModuleName_Type.__name__ = "DisplayString"
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 13),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")


class _ModuleNumPorts_Type(Integer32):
    """Custom type moduleNumPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ModuleNumPorts_Type.__name__ = "Integer32"
_ModuleNumPorts_Object = MibTableColumn
moduleNumPorts = _ModuleNumPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 14),
    _ModuleNumPorts_Type()
)
moduleNumPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleNumPorts.setStatus("current")
_ModulePortStatus_Type = OctetString
_ModulePortStatus_Object = MibTableColumn
modulePortStatus = _ModulePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 15),
    _ModulePortStatus_Type()
)
modulePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modulePortStatus.setStatus("current")


class _ModuleSubType_Type(Integer32):
    """Custom type moduleSubType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              7,
              8,
              9,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              107,
              200,
              201,
              202,
              203,
              205,
              206,
              207,
              208,
              213,
              216,
              217,
              218,
              221,
              223,
              224,
              225,
              226,
              227,
              228,
              229,
              230,
              231,
              232,
              233,
              234,
              235,
              236,
              237,
              238,
              239,
              240,
              241)
        )
    )
    namedValues = NamedValues(
        *(("c6880xdfc", 240),
          ("c6880xledfc", 241),
          ("c6880xlepfc", 239),
          ("c6880xpfc", 238),
          ("c7600Es3c", 233),
          ("c7600Es3cxl", 232),
          ("c7600esmdfc3c", 230),
          ("c7600esmdfc3cxl", 228),
          ("empty", 2),
          ("m7600pfc3c", 213),
          ("mec6524pfc3c", 224),
          ("other", 1),
          ("sip600earl", 225),
          ("vsf6kpfc3c", 227),
          ("vsf6kpfc3cxl", 226),
          ("vsf6kpfc4", 229),
          ("vsf6kpfc4xl", 235),
          ("vsp300dfc", 200),
          ("wsf5510", 3),
          ("wsf5511", 4),
          ("wsf5520", 7),
          ("wsf5521", 8),
          ("wsf5531", 9),
          ("wsf6020", 100),
          ("wsf6020a", 101),
          ("wsf6700cfc", 208),
          ("wsf6700dfc3a", 203),
          ("wsf6700dfc3b", 217),
          ("wsf6700dfc3bxl", 207),
          ("wsf6700dfc3c", 218),
          ("wsf6700dfc3cxl", 221),
          ("wsf6kdfc", 105),
          ("wsf6kdfc3a", 202),
          ("wsf6kdfc3b", 223),
          ("wsf6kdfc3bxl", 205),
          ("wsf6kdfc4a", 237),
          ("wsf6kdfc4axl", 236),
          ("wsf6kdfc4e", 234),
          ("wsf6kdfc4exl", 231),
          ("wsf6kdfca", 107),
          ("wsf6kpfc", 102),
          ("wsf6kpfc2", 103),
          ("wsf6kpfc2a", 106),
          ("wsf6kpfc3a", 201),
          ("wsf6kpfc3b", 216),
          ("wsf6kpfc3bxl", 206),
          ("wsf6kvpwr", 104),
          ("wsx5304", 6))
    )


_ModuleSubType_Type.__name__ = "Integer32"
_ModuleSubType_Object = MibTableColumn
moduleSubType = _ModuleSubType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 16),
    _ModuleSubType_Type()
)
moduleSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSubType.setStatus("current")


class _ModuleModel_Type(DisplayString):
    """Custom type moduleModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModuleModel_Type.__name__ = "DisplayString"
_ModuleModel_Object = MibTableColumn
moduleModel = _ModuleModel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 17),
    _ModuleModel_Type()
)
moduleModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleModel.setStatus("current")


class _ModuleHwVersion_Type(DisplayString):
    """Custom type moduleHwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_ModuleHwVersion_Type.__name__ = "DisplayString"
_ModuleHwVersion_Object = MibTableColumn
moduleHwVersion = _ModuleHwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 18),
    _ModuleHwVersion_Type()
)
moduleHwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleHwVersion.setStatus("current")


class _ModuleFwVersion_Type(DisplayString):
    """Custom type moduleFwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ModuleFwVersion_Type.__name__ = "DisplayString"
_ModuleFwVersion_Object = MibTableColumn
moduleFwVersion = _ModuleFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 19),
    _ModuleFwVersion_Type()
)
moduleFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleFwVersion.setStatus("current")


class _ModuleSwVersion_Type(DisplayString):
    """Custom type moduleSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ModuleSwVersion_Type.__name__ = "DisplayString"
_ModuleSwVersion_Object = MibTableColumn
moduleSwVersion = _ModuleSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 20),
    _ModuleSwVersion_Type()
)
moduleSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSwVersion.setStatus("current")


class _ModuleStandbyStatus_Type(Integer32):
    """Custom type moduleStandbyStatus based on Integer32"""
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
        *(("active", 2),
          ("error", 4),
          ("other", 1),
          ("standby", 3))
    )


_ModuleStandbyStatus_Type.__name__ = "Integer32"
_ModuleStandbyStatus_Object = MibTableColumn
moduleStandbyStatus = _ModuleStandbyStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 21),
    _ModuleStandbyStatus_Type()
)
moduleStandbyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleStandbyStatus.setStatus("current")
_ModuleIPAddress_Type = IpAddress
_ModuleIPAddress_Object = MibTableColumn
moduleIPAddress = _ModuleIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 22),
    _ModuleIPAddress_Type()
)
moduleIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIPAddress.setStatus("current")
_ModuleIPAddressVlan_Type = VlanIndex
_ModuleIPAddressVlan_Object = MibTableColumn
moduleIPAddressVlan = _ModuleIPAddressVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 23),
    _ModuleIPAddressVlan_Type()
)
moduleIPAddressVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIPAddressVlan.setStatus("current")


class _ModuleSubType2_Type(Integer32):
    """Custom type moduleSubType2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              102,
              103,
              104,
              105,
              106,
              107,
              108,
              109,
              207,
              234,
              314,
              315,
              402,
              403,
              404,
              405,
              406,
              410,
              411,
              597,
              598,
              599,
              618,
              620,
              625,
              626,
              1001,
              1005,
              1026,
              1701,
              1805)
        )
    )
    namedValues = NamedValues(
        *(("aceModExpnDc", 410),
          ("c7600Es2Tg", 620),
          ("c7600Es4Tg", 618),
          ("c7600EsItu2TgLk", 626),
          ("c7600EsItu4TgLk", 625),
          ("c7600msfc4", 1805),
          ("empty", 2),
          ("esm2x10ge", 1701),
          ("me6524msfc2a", 598),
          ("other", 1),
          ("vsf6kmsfc3", 1026),
          ("vsf6kmsfc5", 1005),
          ("wsSvcAppProc1", 411),
          ("wsf6kFe48af", 106),
          ("wsf6kFe48x2af", 109),
          ("wsf6kGe48af", 107),
          ("wsf6kVpwrGe", 108),
          ("wsf6kmsfc", 207),
          ("wsf6kmsfc2", 234),
          ("wsf6kmsfc2a", 599),
          ("wsg6483", 104),
          ("wsg6485", 105),
          ("wsg6488", 102),
          ("wsg6489", 103),
          ("wssup720", 1001),
          ("wssvccmm24fxs", 405),
          ("wssvccmm6e1", 403),
          ("wssvccmm6t1", 404),
          ("wssvccmmact", 406),
          ("wssvcidsupg", 402),
          ("wssvcpisa32", 597),
          ("wsu4502gb", 315),
          ("wsu4504fxmt", 314),
          ("wsu5531", 3),
          ("wsu5533", 5),
          ("wsu5534", 6),
          ("wsu5535", 7),
          ("wsu5536", 8),
          ("wsu5537", 9),
          ("wsu5538", 10),
          ("wsu5539", 11))
    )


_ModuleSubType2_Type.__name__ = "Integer32"
_ModuleSubType2_Object = MibTableColumn
moduleSubType2 = _ModuleSubType2_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 24),
    _ModuleSubType2_Type()
)
moduleSubType2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSubType2.setStatus("current")


class _ModuleSlotNum_Type(Integer32):
    """Custom type moduleSlotNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ModuleSlotNum_Type.__name__ = "Integer32"
_ModuleSlotNum_Object = MibTableColumn
moduleSlotNum = _ModuleSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 25),
    _ModuleSlotNum_Type()
)
moduleSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSlotNum.setStatus("current")


class _ModuleSerialNumberString_Type(DisplayString):
    """Custom type moduleSerialNumberString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModuleSerialNumberString_Type.__name__ = "DisplayString"
_ModuleSerialNumberString_Object = MibTableColumn
moduleSerialNumberString = _ModuleSerialNumberString_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 26),
    _ModuleSerialNumberString_Type()
)
moduleSerialNumberString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSerialNumberString.setStatus("current")
_ModuleEntPhysicalIndex_Type = PhysicalIndex
_ModuleEntPhysicalIndex_Object = MibTableColumn
moduleEntPhysicalIndex = _ModuleEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 27),
    _ModuleEntPhysicalIndex_Type()
)
moduleEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleEntPhysicalIndex.setStatus("current")


class _ModuleAdditionalStatus_Type(Bits):
    """Custom type moduleAdditionalStatus based on Bits"""
    namedValues = NamedValues(
        *(("faulty", 2),
          ("fruInstalled", 0),
          ("powerDenied", 1))
    )

_ModuleAdditionalStatus_Type.__name__ = "Bits"
_ModuleAdditionalStatus_Object = MibTableColumn
moduleAdditionalStatus = _ModuleAdditionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 3, 1, 1, 28),
    _ModuleAdditionalStatus_Type()
)
moduleAdditionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleAdditionalStatus.setStatus("current")
_PortGrp_ObjectIdentity = ObjectIdentity
portGrp = _PortGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1)
)
portEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portModuleIndex"),
    (0, "CISCO-STACK-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")


class _PortModuleIndex_Type(Integer32):
    """Custom type portModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortModuleIndex_Type.__name__ = "Integer32"
_PortModuleIndex_Object = MibTableColumn
portModuleIndex = _PortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 1),
    _PortModuleIndex_Type()
)
portModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portModuleIndex.setStatus("current")


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 2),
    _PortIndex_Type()
)
portIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortCrossIndex_Type(Integer32):
    """Custom type portCrossIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4080),
    )


_PortCrossIndex_Type.__name__ = "Integer32"
_PortCrossIndex_Object = MibTableColumn
portCrossIndex = _PortCrossIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 3),
    _PortCrossIndex_Type()
)
portCrossIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCrossIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 4),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100,
              101,
              102,
              103,
              104,
              105,
              106,
              109,
              110,
              111,
              113,
              1000,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008,
              1009,
              1010,
              1011,
              1012,
              1013,
              1014,
              1015,
              1016,
              1017,
              1018,
              1019,
              1020,
              1021,
              1022,
              1023,
              1024,
              1025,
              1026,
              1027,
              1028,
              1029,
              1030,
              1031,
              1032,
              1033,
              1034,
              1035,
              1036,
              1037,
              1038,
              1039,
              1040,
              1041,
              1042,
              1043,
              1044,
              1045,
              1046,
              1047,
              1048,
              1049,
              1050,
              1051,
              1052,
              1053,
              1054,
              1055,
              1056,
              1057,
              1058,
              1059,
              1060,
              1061,
              1062,
              1063,
              1064,
              1065,
              1066,
              1067,
              1068,
              1069,
              1070,
              1071,
              1072,
              1073,
              1074,
              1075,
              1076,
              1077,
              1078,
              1079,
              1080,
              1081,
              1082,
              1083,
              1084,
              1085,
              1086,
              1087,
              1088,
              1089,
              1090,
              1091,
              1092,
              1093,
              1094,
              1095,
              1096,
              1097,
              1098,
              1099,
              1100,
              1101,
              1102,
              1104,
              1105,
              1106,
              1107,
              1108,
              1109,
              1110,
              1111,
              1112,
              1113,
              1114,
              1115,
              1116,
              1117,
              1118,
              1119)
        )
    )
    namedValues = NamedValues(
        *(("aces", 106),
          ("adsm", 104),
          ("agsm", 105),
          ("aons", 101),
          ("atmDs3", 25),
          ("atmOc12mm", 43),
          ("atmOc12mmf", 23),
          ("atmOc12smf", 24),
          ("atmOc12smi", 44),
          ("atmOc12sml", 45),
          ("atmOc3mmf", 14),
          ("atmOc3smf", 15),
          ("atmOc3utp", 16),
          ("cddi", 2),
          ("chOc12mm", 67),
          ("chOc12smi", 66),
          ("chOc3smi", 87),
          ("chOc48smi", 69),
          ("chOc48ss", 68),
          ("coe", 89),
          ("conferencing", 42),
          ("contentEngine", 72),
          ("ct3", 76),
          ("depi2", 36),
          ("dptOc48mm", 62),
          ("dptOc48smi", 63),
          ("dptOc48sml", 64),
          ("e1", 38),
          ("e1000BaseBT", 85),
          ("e1000BaseBX10D", 1069),
          ("e1000BaseBX10U", 1070),
          ("e1000BaseCX", 29),
          ("e1000BaseCwdm1470", 77),
          ("e1000BaseCwdm1490", 78),
          ("e1000BaseCwdm1510", 79),
          ("e1000BaseCwdm1530", 80),
          ("e1000BaseCwdm1550", 81),
          ("e1000BaseCwdm1570", 82),
          ("e1000BaseCwdm1590", 83),
          ("e1000BaseCwdm1610", 84),
          ("e1000BaseDwdm3033", 1004),
          ("e1000BaseDwdm3112", 1005),
          ("e1000BaseDwdm3190", 1006),
          ("e1000BaseDwdm3268", 1007),
          ("e1000BaseDwdm3346", 1092),
          ("e1000BaseDwdm3425", 1008),
          ("e1000BaseDwdm3504", 1009),
          ("e1000BaseDwdm3582", 1010),
          ("e1000BaseDwdm3661", 1011),
          ("e1000BaseDwdm3739", 1093),
          ("e1000BaseDwdm3819", 1012),
          ("e1000BaseDwdm3898", 1013),
          ("e1000BaseDwdm3977", 1014),
          ("e1000BaseDwdm4056", 1015),
          ("e1000BaseDwdm4134", 1094),
          ("e1000BaseDwdm4214", 1016),
          ("e1000BaseDwdm4294", 1017),
          ("e1000BaseDwdm4373", 1018),
          ("e1000BaseDwdm4453", 1019),
          ("e1000BaseDwdm4532", 1095),
          ("e1000BaseDwdm4612", 1020),
          ("e1000BaseDwdm4692", 1021),
          ("e1000BaseDwdm4772", 1022),
          ("e1000BaseDwdm4851", 1023),
          ("e1000BaseDwdm4931", 1096),
          ("e1000BaseDwdm5012", 1024),
          ("e1000BaseDwdm5092", 1025),
          ("e1000BaseDwdm5172", 1026),
          ("e1000BaseDwdm5252", 1027),
          ("e1000BaseDwdm5332", 1097),
          ("e1000BaseDwdm5413", 1028),
          ("e1000BaseDwdm5494", 1029),
          ("e1000BaseDwdm5575", 1030),
          ("e1000BaseDwdm5655", 1031),
          ("e1000BaseDwdm5736", 1098),
          ("e1000BaseDwdm5817", 1032),
          ("e1000BaseDwdm5898", 1033),
          ("e1000BaseDwdm5979", 1034),
          ("e1000BaseDwdm6061", 1035),
          ("e1000BaseDwdm6141", 1099),
          ("e1000BaseEXSMD", 1114),
          ("e1000BaseLH", 32),
          ("e1000BaseLHSMD", 1118),
          ("e1000BaseLX", 27),
          ("e1000BaseSX", 28),
          ("e1000BaseSXMMD", 1117),
          ("e1000BaseSvc", 110),
          ("e1000BaseT", 33),
          ("e1000BaseTE", 1116),
          ("e1000BaseUnapproved", 86),
          ("e1000BaseUnknown", 1000),
          ("e1000BaseWdmRxOnly", 1003),
          ("e1000BaseZX", 35),
          ("e1000BaseZXSMD", 1115),
          ("e1000Empty", 31),
          ("e1000UnsupportedGbic", 34),
          ("e100BaseBX10D", 1074),
          ("e100BaseBX10U", 1075),
          ("e100BaseEX", 1078),
          ("e100BaseEmpty", 103),
          ("e100BaseF", 13),
          ("e100BaseFXGE", 1119),
          ("e100BaseFsm", 17),
          ("e100BaseLX", 92),
          ("e100BaseSX", 1073),
          ("e100BaseT4", 12),
          ("e100BaseTX", 11),
          ("e100BaseUnapproved", 1072),
          ("e100BaseUnknown", 1071),
          ("e100BaseZX", 1079),
          ("e10BaseF", 9),
          ("e10BaseT", 8),
          ("e10GBaseACU10M", 1113),
          ("e10GBaseACU7M", 1112),
          ("e10GBaseBad", 1076),
          ("e10GBaseCPX", 56),
          ("e10GBaseCU1M", 1082),
          ("e10GBaseCU2M", 1087),
          ("e10GBaseCU3M", 1083),
          ("e10GBaseCU4M", 1088),
          ("e10GBaseCU5M", 1084),
          ("e10GBaseCU6M", 1089),
          ("e10GBaseCU7M", 1085),
          ("e10GBaseCUdot3M", 1086),
          ("e10GBaseCX4", 94),
          ("e10GBaseDwdm3033", 1037),
          ("e10GBaseDwdm3112", 1038),
          ("e10GBaseDwdm3190", 1039),
          ("e10GBaseDwdm3268", 1040),
          ("e10GBaseDwdm3347", 1104),
          ("e10GBaseDwdm3425", 1041),
          ("e10GBaseDwdm3504", 1042),
          ("e10GBaseDwdm3582", 1043),
          ("e10GBaseDwdm3661", 1044),
          ("e10GBaseDwdm3740", 1105),
          ("e10GBaseDwdm3819", 1045),
          ("e10GBaseDwdm3898", 1046),
          ("e10GBaseDwdm3977", 1047),
          ("e10GBaseDwdm4056", 1048),
          ("e10GBaseDwdm4135", 1106),
          ("e10GBaseDwdm4214", 1049),
          ("e10GBaseDwdm4294", 1050),
          ("e10GBaseDwdm4373", 1051),
          ("e10GBaseDwdm4453", 1052),
          ("e10GBaseDwdm4532", 1107),
          ("e10GBaseDwdm4612", 1053),
          ("e10GBaseDwdm4692", 1054),
          ("e10GBaseDwdm4772", 1055),
          ("e10GBaseDwdm4851", 1056),
          ("e10GBaseDwdm4932", 1108),
          ("e10GBaseDwdm5012", 1057),
          ("e10GBaseDwdm5092", 1058),
          ("e10GBaseDwdm5172", 1059),
          ("e10GBaseDwdm5252", 1060),
          ("e10GBaseDwdm5333", 1109),
          ("e10GBaseDwdm5413", 1061),
          ("e10GBaseDwdm5494", 1062),
          ("e10GBaseDwdm5575", 1063),
          ("e10GBaseDwdm5655", 1064),
          ("e10GBaseDwdm5736", 1110),
          ("e10GBaseDwdm5817", 1065),
          ("e10GBaseDwdm5898", 1066),
          ("e10GBaseDwdm5979", 1067),
          ("e10GBaseDwdm6061", 1068),
          ("e10GBaseDwdm6141", 1111),
          ("e10GBaseER", 71),
          ("e10GBaseEW", 99),
          ("e10GBaseEX4", 59),
          ("e10GBaseEdc1310", 96),
          ("e10GBaseLR", 65),
          ("e10GBaseLRM", 1080),
          ("e10GBaseLRMSM", 1091),
          ("e10GBaseLW", 98),
          ("e10GBaseLX4", 57),
          ("e10GBaseSR", 93),
          ("e10GBaseSW", 97),
          ("e10GBaseSX4", 70),
          ("e10GBaseSvc", 111),
          ("e10GBaseTPluggable", 1081),
          ("e10GBaseUSR", 1090),
          ("e10GBaseUnapproved", 1002),
          ("e10GBaseUnknown", 1001),
          ("e10GBaseWdm1550", 95),
          ("e10GBaseWdmRxOnly", 1036),
          ("e10GBaseZR", 1077),
          ("e10GEmpty", 60),
          ("e10a100BaseTX", 18),
          ("e10a100a1000BaseT", 61),
          ("e40GBaseEmpty", 113),
          ("e40GBaseLR", 1100),
          ("e40GBaseSR", 1101),
          ("e40GBaseUnapproved", 1102),
          ("fddi", 3),
          ("firewall", 74),
          ("fxo", 40),
          ("fxs", 39),
          ("intrusionDetect", 55),
          ("intrusionProtect", 109),
          ("lwa", 100),
          ("mcr", 88),
          ("mii", 19),
          ("mlt3", 5),
          ("mwa", 90),
          ("networkAnalysis", 30),
          ("other", 1),
          ("posOc12mm", 46),
          ("posOc12smi", 47),
          ("posOc12sml", 48),
          ("posOc3mm", 52),
          ("posOc3smi", 53),
          ("posOc3sml", 54),
          ("posOc48smi", 50),
          ("posOc48sml", 51),
          ("posOc48sms", 49),
          ("psd", 91),
          ("remoteRouter", 21),
          ("scf", 10),
          ("sddi", 6),
          ("smf", 7),
          ("ssl", 73),
          ("sslVpn", 102),
          ("t1", 37),
          ("tokenring", 22),
          ("tokenringMmf", 26),
          ("tppmd", 4),
          ("transcoding", 41),
          ("vlanRouter", 20),
          ("vpnIpSec", 75))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 5),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortOperStatus_Type(Integer32):
    """Custom type portOperStatus based on Integer32"""
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
        *(("majorFault", 4),
          ("minorFault", 3),
          ("ok", 2),
          ("other", 1))
    )


_PortOperStatus_Type.__name__ = "Integer32"
_PortOperStatus_Object = MibTableColumn
portOperStatus = _PortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 6),
    _PortOperStatus_Type()
)
portOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperStatus.setStatus("current")


class _PortCrossGroupIndex_Type(Integer32):
    """Custom type portCrossGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortCrossGroupIndex_Type.__name__ = "Integer32"
_PortCrossGroupIndex_Object = MibTableColumn
portCrossGroupIndex = _PortCrossGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 7),
    _PortCrossGroupIndex_Type()
)
portCrossGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCrossGroupIndex.setStatus("current")


class _PortAdditionalStatus_Type(Integer32):
    """Custom type portAdditionalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PortAdditionalStatus_Type.__name__ = "Integer32"
_PortAdditionalStatus_Object = MibTableColumn
portAdditionalStatus = _PortAdditionalStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 8),
    _PortAdditionalStatus_Type()
)
portAdditionalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAdditionalStatus.setStatus("current")


class _PortAdminSpeed_Type(Integer32):
    """Custom type portAdminSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10,
              64000,
              1544000,
              2000000,
              2048000,
              4000000,
              10000000,
              16000000,
              45000000,
              64000000,
              100000000,
              155000000,
              400000000,
              622000000,
              1000000000)
        )
    )
    namedValues = NamedValues(
        *(("autoDetect", 1),
          ("autoDetect10100", 2),
          ("s10000000", 10000000),
          ("s100000000", 100000000),
          ("s1000000000", 1000000000),
          ("s10G", 10),
          ("s1544000", 1544000),
          ("s155000000", 155000000),
          ("s16000000", 16000000),
          ("s2000000", 2000000),
          ("s2048000", 2048000),
          ("s4000000", 4000000),
          ("s400000000", 400000000),
          ("s45000000", 45000000),
          ("s622000000", 622000000),
          ("s64000", 64000),
          ("s64000000", 64000000))
    )


_PortAdminSpeed_Type.__name__ = "Integer32"
_PortAdminSpeed_Object = MibTableColumn
portAdminSpeed = _PortAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 9),
    _PortAdminSpeed_Type()
)
portAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminSpeed.setStatus("current")


class _PortDuplex_Type(Integer32):
    """Custom type portDuplex based on Integer32"""
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
        *(("auto", 4),
          ("disagree", 3),
          ("full", 2),
          ("half", 1))
    )


_PortDuplex_Type.__name__ = "Integer32"
_PortDuplex_Object = MibTableColumn
portDuplex = _PortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 10),
    _PortDuplex_Type()
)
portDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portDuplex.setStatus("current")


class _PortIfIndex_Type(Integer32):
    """Custom type portIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortIfIndex_Type.__name__ = "Integer32"
_PortIfIndex_Object = MibTableColumn
portIfIndex = _PortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 11),
    _PortIfIndex_Type()
)
portIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portIfIndex.setStatus("current")


class _PortSpantreeFastStart_Type(Integer32):
    """Custom type portSpantreeFastStart based on Integer32"""
    defaultValue = 2

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


_PortSpantreeFastStart_Type.__name__ = "Integer32"
_PortSpantreeFastStart_Object = MibTableColumn
portSpantreeFastStart = _PortSpantreeFastStart_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 12),
    _PortSpantreeFastStart_Type()
)
portSpantreeFastStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpantreeFastStart.setStatus("deprecated")


class _PortAdminRxFlowControl_Type(Integer32):
    """Custom type portAdminRxFlowControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("desired", 3),
          ("off", 2),
          ("on", 1))
    )


_PortAdminRxFlowControl_Type.__name__ = "Integer32"
_PortAdminRxFlowControl_Object = MibTableColumn
portAdminRxFlowControl = _PortAdminRxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 13),
    _PortAdminRxFlowControl_Type()
)
portAdminRxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminRxFlowControl.setStatus("current")


class _PortOperRxFlowControl_Type(Integer32):
    """Custom type portOperRxFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disagree", 3),
          ("off", 2),
          ("on", 1))
    )


_PortOperRxFlowControl_Type.__name__ = "Integer32"
_PortOperRxFlowControl_Object = MibTableColumn
portOperRxFlowControl = _PortOperRxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 14),
    _PortOperRxFlowControl_Type()
)
portOperRxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperRxFlowControl.setStatus("current")


class _PortAdminTxFlowControl_Type(Integer32):
    """Custom type portAdminTxFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("desired", 3),
          ("off", 2),
          ("on", 1))
    )


_PortAdminTxFlowControl_Type.__name__ = "Integer32"
_PortAdminTxFlowControl_Object = MibTableColumn
portAdminTxFlowControl = _PortAdminTxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 15),
    _PortAdminTxFlowControl_Type()
)
portAdminTxFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAdminTxFlowControl.setStatus("current")


class _PortOperTxFlowControl_Type(Integer32):
    """Custom type portOperTxFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disagree", 3),
          ("off", 2),
          ("on", 1))
    )


_PortOperTxFlowControl_Type.__name__ = "Integer32"
_PortOperTxFlowControl_Object = MibTableColumn
portOperTxFlowControl = _PortOperTxFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 16),
    _PortOperTxFlowControl_Type()
)
portOperTxFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOperTxFlowControl.setStatus("current")
_PortMacControlTransmitFrames_Type = Counter32
_PortMacControlTransmitFrames_Object = MibTableColumn
portMacControlTransmitFrames = _PortMacControlTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 17),
    _PortMacControlTransmitFrames_Type()
)
portMacControlTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacControlTransmitFrames.setStatus("current")
_PortMacControlReceiveFrames_Type = Counter32
_PortMacControlReceiveFrames_Object = MibTableColumn
portMacControlReceiveFrames = _PortMacControlReceiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 18),
    _PortMacControlReceiveFrames_Type()
)
portMacControlReceiveFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacControlReceiveFrames.setStatus("current")
_PortMacControlPauseTransmitFrames_Type = Counter32
_PortMacControlPauseTransmitFrames_Object = MibTableColumn
portMacControlPauseTransmitFrames = _PortMacControlPauseTransmitFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 19),
    _PortMacControlPauseTransmitFrames_Type()
)
portMacControlPauseTransmitFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacControlPauseTransmitFrames.setStatus("current")
_PortMacControlPauseReceiveFrames_Type = Counter32
_PortMacControlPauseReceiveFrames_Object = MibTableColumn
portMacControlPauseReceiveFrames = _PortMacControlPauseReceiveFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 20),
    _PortMacControlPauseReceiveFrames_Type()
)
portMacControlPauseReceiveFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacControlPauseReceiveFrames.setStatus("current")
_PortMacControlUnknownProtocolFrames_Type = Counter32
_PortMacControlUnknownProtocolFrames_Object = MibTableColumn
portMacControlUnknownProtocolFrames = _PortMacControlUnknownProtocolFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 21),
    _PortMacControlUnknownProtocolFrames_Type()
)
portMacControlUnknownProtocolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portMacControlUnknownProtocolFrames.setStatus("current")


class _PortLinkFaultStatus_Type(Integer32):
    """Custom type portLinkFaultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("farEndConfigFail", 6),
          ("farEndDisable", 4),
          ("farEndFault", 5),
          ("nearEndConfigFail", 3),
          ("nearEndFault", 2),
          ("noFault", 1),
          ("notApplicable", 7))
    )


_PortLinkFaultStatus_Type.__name__ = "Integer32"
_PortLinkFaultStatus_Object = MibTableColumn
portLinkFaultStatus = _PortLinkFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 22),
    _PortLinkFaultStatus_Type()
)
portLinkFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portLinkFaultStatus.setStatus("current")


class _PortAdditionalOperStatus_Type(Bits):
    """Custom type portAdditionalOperStatus based on Bits"""
    namedValues = NamedValues(
        *(("connected", 1),
          ("disabled", 8),
          ("dripDis", 7),
          ("errdisable", 10),
          ("faulty", 3),
          ("inactive", 5),
          ("linkFaulty", 11),
          ("monitor", 9),
          ("notConnected", 4),
          ("offHook", 13),
          ("onHook", 12),
          ("other", 0),
          ("reflector", 14),
          ("shutdown", 6),
          ("standby", 2))
    )

_PortAdditionalOperStatus_Type.__name__ = "Bits"
_PortAdditionalOperStatus_Object = MibTableColumn
portAdditionalOperStatus = _PortAdditionalOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 23),
    _PortAdditionalOperStatus_Type()
)
portAdditionalOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portAdditionalOperStatus.setStatus("current")
_PortInlinePowerDetect_Type = TruthValue
_PortInlinePowerDetect_Object = MibTableColumn
portInlinePowerDetect = _PortInlinePowerDetect_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 24),
    _PortInlinePowerDetect_Type()
)
portInlinePowerDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInlinePowerDetect.setStatus("current")
_PortEntPhysicalIndex_Type = PhysicalIndex
_PortEntPhysicalIndex_Object = MibTableColumn
portEntPhysicalIndex = _PortEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 25),
    _PortEntPhysicalIndex_Type()
)
portEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portEntPhysicalIndex.setStatus("current")


class _PortErrDisableTimeOutEnable_Type(Integer32):
    """Custom type portErrDisableTimeOutEnable based on Integer32"""
    defaultValue = 1

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


_PortErrDisableTimeOutEnable_Type.__name__ = "Integer32"
_PortErrDisableTimeOutEnable_Object = MibTableColumn
portErrDisableTimeOutEnable = _PortErrDisableTimeOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 4, 1, 1, 26),
    _PortErrDisableTimeOutEnable_Type()
)
portErrDisableTimeOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portErrDisableTimeOutEnable.setStatus("current")
_TftpGrp_ObjectIdentity = ObjectIdentity
tftpGrp = _TftpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 5)
)


class _TftpHost_Type(DisplayString):
    """Custom type tftpHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TftpHost_Type.__name__ = "DisplayString"
_TftpHost_Object = MibScalar
tftpHost = _TftpHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 5, 1),
    _TftpHost_Type()
)
tftpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpHost.setStatus("current")


class _TftpFile_Type(DisplayString):
    """Custom type tftpFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TftpFile_Type.__name__ = "DisplayString"
_TftpFile_Object = MibScalar
tftpFile = _TftpFile_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 5, 2),
    _TftpFile_Type()
)
tftpFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpFile.setStatus("current")


class _TftpModule_Type(Integer32):
    """Custom type tftpModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_TftpModule_Type.__name__ = "Integer32"
_TftpModule_Object = MibScalar
tftpModule = _TftpModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 5, 3),
    _TftpModule_Type()
)
tftpModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpModule.setStatus("current")


class _TftpAction_Type(Integer32):
    """Custom type tftpAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("downloadConfig", 2),
          ("downloadFw", 6),
          ("downloadSw", 4),
          ("other", 1),
          ("uploadConfig", 3),
          ("uploadFw", 7),
          ("uploadSw", 5))
    )


_TftpAction_Type.__name__ = "Integer32"
_TftpAction_Object = MibScalar
tftpAction = _TftpAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 5, 4),
    _TftpAction_Type()
)
tftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tftpAction.setStatus("current")


class _TftpResult_Type(Integer32):
    """Custom type tftpResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("accessViolation", 16),
          ("badChecksum", 7),
          ("badFlash", 9),
          ("badLength", 8),
          ("fileNotFound", 13),
          ("inProgress", 1),
          ("incompatibleImage", 21),
          ("insufficientDramSize", 20),
          ("insufficientSpaceOnStorageDevice", 19),
          ("invalidStorageDevice", 18),
          ("invalidTftpHost", 14),
          ("invalidTftpModule", 15),
          ("noBuffers", 5),
          ("noProcesses", 6),
          ("noResponse", 3),
          ("serverError", 10),
          ("success", 2),
          ("tooManyRetries", 4),
          ("unknownStatus", 17),
          ("userCanceled", 11),
          ("wrongCode", 12))
    )


_TftpResult_Type.__name__ = "Integer32"
_TftpResult_Object = MibScalar
tftpResult = _TftpResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 5, 5),
    _TftpResult_Type()
)
tftpResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tftpResult.setStatus("current")
_BrouterGrp_ObjectIdentity = ObjectIdentity
brouterGrp = _BrouterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6)
)


class _BrouterEnableRip_Type(Integer32):
    """Custom type brouterEnableRip based on Integer32"""
    defaultValue = 1

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


_BrouterEnableRip_Type.__name__ = "Integer32"
_BrouterEnableRip_Object = MibScalar
brouterEnableRip = _BrouterEnableRip_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 1),
    _BrouterEnableRip_Type()
)
brouterEnableRip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableRip.setStatus("current")


class _BrouterEnableSpantree_Type(Integer32):
    """Custom type brouterEnableSpantree based on Integer32"""
    defaultValue = 2

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


_BrouterEnableSpantree_Type.__name__ = "Integer32"
_BrouterEnableSpantree_Object = MibScalar
brouterEnableSpantree = _BrouterEnableSpantree_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 2),
    _BrouterEnableSpantree_Type()
)
brouterEnableSpantree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableSpantree.setStatus("current")


class _BrouterEnableGiantCheck_Type(Integer32):
    """Custom type brouterEnableGiantCheck based on Integer32"""
    defaultValue = 2

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


_BrouterEnableGiantCheck_Type.__name__ = "Integer32"
_BrouterEnableGiantCheck_Object = MibScalar
brouterEnableGiantCheck = _BrouterEnableGiantCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 3),
    _BrouterEnableGiantCheck_Type()
)
brouterEnableGiantCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableGiantCheck.setStatus("current")


class _BrouterEnableIpFragmentation_Type(Integer32):
    """Custom type brouterEnableIpFragmentation based on Integer32"""
    defaultValue = 1

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


_BrouterEnableIpFragmentation_Type.__name__ = "Integer32"
_BrouterEnableIpFragmentation_Object = MibScalar
brouterEnableIpFragmentation = _BrouterEnableIpFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 4),
    _BrouterEnableIpFragmentation_Type()
)
brouterEnableIpFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableIpFragmentation.setStatus("current")


class _BrouterEnableUnreachables_Type(Integer32):
    """Custom type brouterEnableUnreachables based on Integer32"""
    defaultValue = 1

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


_BrouterEnableUnreachables_Type.__name__ = "Integer32"
_BrouterEnableUnreachables_Object = MibScalar
brouterEnableUnreachables = _BrouterEnableUnreachables_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 5),
    _BrouterEnableUnreachables_Type()
)
brouterEnableUnreachables.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableUnreachables.setStatus("current")


class _BrouterCamAgingTime_Type(Integer32):
    """Custom type brouterCamAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_BrouterCamAgingTime_Type.__name__ = "Integer32"
_BrouterCamAgingTime_Object = MibScalar
brouterCamAgingTime = _BrouterCamAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 6),
    _BrouterCamAgingTime_Type()
)
brouterCamAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterCamAgingTime.setStatus("deprecated")


class _BrouterCamMode_Type(Integer32):
    """Custom type brouterCamMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtering", 1),
          ("forwarding", 2))
    )


_BrouterCamMode_Type.__name__ = "Integer32"
_BrouterCamMode_Object = MibScalar
brouterCamMode = _BrouterCamMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 7),
    _BrouterCamMode_Type()
)
brouterCamMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterCamMode.setStatus("current")


class _BrouterIpxSnapToEther_Type(Integer32):
    """Custom type brouterIpxSnapToEther based on Integer32"""
    defaultValue = 4

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
        *(("ethernetII", 2),
          ("iso8023", 3),
          ("raw8023", 4),
          ("snap", 1))
    )


_BrouterIpxSnapToEther_Type.__name__ = "Integer32"
_BrouterIpxSnapToEther_Object = MibScalar
brouterIpxSnapToEther = _BrouterIpxSnapToEther_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 8),
    _BrouterIpxSnapToEther_Type()
)
brouterIpxSnapToEther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterIpxSnapToEther.setStatus("current")


class _BrouterIpx8023RawToFddi_Type(Integer32):
    """Custom type brouterIpx8023RawToFddi based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("fddiRaw", 6),
          ("iso8022", 5),
          ("snap", 1))
    )


_BrouterIpx8023RawToFddi_Type.__name__ = "Integer32"
_BrouterIpx8023RawToFddi_Object = MibScalar
brouterIpx8023RawToFddi = _BrouterIpx8023RawToFddi_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 9),
    _BrouterIpx8023RawToFddi_Type()
)
brouterIpx8023RawToFddi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterIpx8023RawToFddi.setStatus("current")


class _BrouterEthernetReceiveMax_Type(Integer32):
    """Custom type brouterEthernetReceiveMax based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BrouterEthernetReceiveMax_Type.__name__ = "Integer32"
_BrouterEthernetReceiveMax_Object = MibScalar
brouterEthernetReceiveMax = _BrouterEthernetReceiveMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 10),
    _BrouterEthernetReceiveMax_Type()
)
brouterEthernetReceiveMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEthernetReceiveMax.setStatus("current")


class _BrouterEthernetTransmitMax_Type(Integer32):
    """Custom type brouterEthernetTransmitMax based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_BrouterEthernetTransmitMax_Type.__name__ = "Integer32"
_BrouterEthernetTransmitMax_Object = MibScalar
brouterEthernetTransmitMax = _BrouterEthernetTransmitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 11),
    _BrouterEthernetTransmitMax_Type()
)
brouterEthernetTransmitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEthernetTransmitMax.setStatus("current")


class _BrouterFddiReceiveMax_Type(Integer32):
    """Custom type brouterFddiReceiveMax based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_BrouterFddiReceiveMax_Type.__name__ = "Integer32"
_BrouterFddiReceiveMax_Object = MibScalar
brouterFddiReceiveMax = _BrouterFddiReceiveMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 12),
    _BrouterFddiReceiveMax_Type()
)
brouterFddiReceiveMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterFddiReceiveMax.setStatus("current")


class _BrouterFddiTransmitMax_Type(Integer32):
    """Custom type brouterFddiTransmitMax based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_BrouterFddiTransmitMax_Type.__name__ = "Integer32"
_BrouterFddiTransmitMax_Object = MibScalar
brouterFddiTransmitMax = _BrouterFddiTransmitMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 13),
    _BrouterFddiTransmitMax_Type()
)
brouterFddiTransmitMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterFddiTransmitMax.setStatus("current")
_BrouterPortTable_Object = MibTable
brouterPortTable = _BrouterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14)
)
if mibBuilder.loadTexts:
    brouterPortTable.setStatus("current")
_BrouterPortEntry_Object = MibTableRow
brouterPortEntry = _BrouterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1)
)
brouterPortEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "brouterPortModule"),
    (0, "CISCO-STACK-MIB", "brouterPort"),
)
if mibBuilder.loadTexts:
    brouterPortEntry.setStatus("current")


class _BrouterPortModule_Type(Integer32):
    """Custom type brouterPortModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BrouterPortModule_Type.__name__ = "Integer32"
_BrouterPortModule_Object = MibTableColumn
brouterPortModule = _BrouterPortModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 1),
    _BrouterPortModule_Type()
)
brouterPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brouterPortModule.setStatus("current")


class _BrouterPort_Type(Integer32):
    """Custom type brouterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BrouterPort_Type.__name__ = "Integer32"
_BrouterPort_Object = MibTableColumn
brouterPort = _BrouterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 2),
    _BrouterPort_Type()
)
brouterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    brouterPort.setStatus("current")
_BrouterPortIpVlan_Type = VlanIndex
_BrouterPortIpVlan_Object = MibTableColumn
brouterPortIpVlan = _BrouterPortIpVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 3),
    _BrouterPortIpVlan_Type()
)
brouterPortIpVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterPortIpVlan.setStatus("current")
_BrouterPortIpAddr_Type = IpAddress
_BrouterPortIpAddr_Object = MibTableColumn
brouterPortIpAddr = _BrouterPortIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 4),
    _BrouterPortIpAddr_Type()
)
brouterPortIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterPortIpAddr.setStatus("current")
_BrouterPortNetMask_Type = IpAddress
_BrouterPortNetMask_Object = MibTableColumn
brouterPortNetMask = _BrouterPortNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 5),
    _BrouterPortNetMask_Type()
)
brouterPortNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterPortNetMask.setStatus("current")
_BrouterPortBroadcast_Type = IpAddress
_BrouterPortBroadcast_Object = MibTableColumn
brouterPortBroadcast = _BrouterPortBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 6),
    _BrouterPortBroadcast_Type()
)
brouterPortBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterPortBroadcast.setStatus("current")


class _BrouterPortBridgeVlan_Type(Integer32):
    """Custom type brouterPortBridgeVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_BrouterPortBridgeVlan_Type.__name__ = "Integer32"
_BrouterPortBridgeVlan_Object = MibTableColumn
brouterPortBridgeVlan = _BrouterPortBridgeVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 7),
    _BrouterPortBridgeVlan_Type()
)
brouterPortBridgeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterPortBridgeVlan.setStatus("current")


class _BrouterPortIpHelpers_Type(OctetString):
    """Custom type brouterPortIpHelpers based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BrouterPortIpHelpers_Type.__name__ = "OctetString"
_BrouterPortIpHelpers_Object = MibTableColumn
brouterPortIpHelpers = _BrouterPortIpHelpers_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 14, 1, 8),
    _BrouterPortIpHelpers_Type()
)
brouterPortIpHelpers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterPortIpHelpers.setStatus("current")


class _BrouterIpx8022ToEther_Type(Integer32):
    """Custom type brouterIpx8022ToEther based on Integer32"""
    defaultValue = 3

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
        *(("ethernetII", 2),
          ("iso8023", 3),
          ("raw8023", 4),
          ("snap", 1))
    )


_BrouterIpx8022ToEther_Type.__name__ = "Integer32"
_BrouterIpx8022ToEther_Object = MibScalar
brouterIpx8022ToEther = _BrouterIpx8022ToEther_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 15),
    _BrouterIpx8022ToEther_Type()
)
brouterIpx8022ToEther.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterIpx8022ToEther.setStatus("current")


class _BrouterEnableTransitEncapsulation_Type(Integer32):
    """Custom type brouterEnableTransitEncapsulation based on Integer32"""
    defaultValue = 2

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


_BrouterEnableTransitEncapsulation_Type.__name__ = "Integer32"
_BrouterEnableTransitEncapsulation_Object = MibScalar
brouterEnableTransitEncapsulation = _BrouterEnableTransitEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 16),
    _BrouterEnableTransitEncapsulation_Type()
)
brouterEnableTransitEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableTransitEncapsulation.setStatus("current")


class _BrouterEnableFddiCheck_Type(Integer32):
    """Custom type brouterEnableFddiCheck based on Integer32"""
    defaultValue = 2

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


_BrouterEnableFddiCheck_Type.__name__ = "Integer32"
_BrouterEnableFddiCheck_Object = MibScalar
brouterEnableFddiCheck = _BrouterEnableFddiCheck_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 17),
    _BrouterEnableFddiCheck_Type()
)
brouterEnableFddiCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableFddiCheck.setStatus("current")


class _BrouterEnableAPaRT_Type(Integer32):
    """Custom type brouterEnableAPaRT based on Integer32"""
    defaultValue = 1

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


_BrouterEnableAPaRT_Type.__name__ = "Integer32"
_BrouterEnableAPaRT_Object = MibScalar
brouterEnableAPaRT = _BrouterEnableAPaRT_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 6, 18),
    _BrouterEnableAPaRT_Type()
)
brouterEnableAPaRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    brouterEnableAPaRT.setStatus("current")
_FilterGrp_ObjectIdentity = ObjectIdentity
filterGrp = _FilterGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7)
)
_FilterMacTable_Object = MibTable
filterMacTable = _FilterMacTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 1)
)
if mibBuilder.loadTexts:
    filterMacTable.setStatus("current")
_FilterMacEntry_Object = MibTableRow
filterMacEntry = _FilterMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 1, 1)
)
filterMacEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "filterMacModule"),
    (0, "CISCO-STACK-MIB", "filterMacPort"),
    (0, "CISCO-STACK-MIB", "filterMacAddress"),
)
if mibBuilder.loadTexts:
    filterMacEntry.setStatus("current")


class _FilterMacModule_Type(Integer32):
    """Custom type filterMacModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FilterMacModule_Type.__name__ = "Integer32"
_FilterMacModule_Object = MibTableColumn
filterMacModule = _FilterMacModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 1, 1, 1),
    _FilterMacModule_Type()
)
filterMacModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMacModule.setStatus("current")


class _FilterMacPort_Type(Integer32):
    """Custom type filterMacPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FilterMacPort_Type.__name__ = "Integer32"
_FilterMacPort_Object = MibTableColumn
filterMacPort = _FilterMacPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 1, 1, 2),
    _FilterMacPort_Type()
)
filterMacPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMacPort.setStatus("current")
_FilterMacAddress_Type = MacAddress
_FilterMacAddress_Object = MibTableColumn
filterMacAddress = _FilterMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 1, 1, 3),
    _FilterMacAddress_Type()
)
filterMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterMacAddress.setStatus("current")


class _FilterMacType_Type(Integer32):
    """Custom type filterMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("denyDst", 7),
          ("denySrc", 6),
          ("denySrcLearn", 8),
          ("invalid", 2),
          ("permit", 3),
          ("permitDst", 5),
          ("permitSrc", 4))
    )


_FilterMacType_Type.__name__ = "Integer32"
_FilterMacType_Object = MibTableColumn
filterMacType = _FilterMacType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 1, 1, 4),
    _FilterMacType_Type()
)
filterMacType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterMacType.setStatus("current")
_FilterVendorTable_Object = MibTable
filterVendorTable = _FilterVendorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 2)
)
if mibBuilder.loadTexts:
    filterVendorTable.setStatus("current")
_FilterVendorEntry_Object = MibTableRow
filterVendorEntry = _FilterVendorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 2, 1)
)
filterVendorEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "filterVendorModule"),
    (0, "CISCO-STACK-MIB", "filterVendorPort"),
    (0, "CISCO-STACK-MIB", "filterVendorId"),
)
if mibBuilder.loadTexts:
    filterVendorEntry.setStatus("current")


class _FilterVendorModule_Type(Integer32):
    """Custom type filterVendorModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FilterVendorModule_Type.__name__ = "Integer32"
_FilterVendorModule_Object = MibTableColumn
filterVendorModule = _FilterVendorModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 2, 1, 1),
    _FilterVendorModule_Type()
)
filterVendorModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterVendorModule.setStatus("current")


class _FilterVendorPort_Type(Integer32):
    """Custom type filterVendorPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FilterVendorPort_Type.__name__ = "Integer32"
_FilterVendorPort_Object = MibTableColumn
filterVendorPort = _FilterVendorPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 2, 1, 2),
    _FilterVendorPort_Type()
)
filterVendorPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterVendorPort.setStatus("current")
_FilterVendorId_Type = VendorIdType
_FilterVendorId_Object = MibTableColumn
filterVendorId = _FilterVendorId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 2, 1, 3),
    _FilterVendorId_Type()
)
filterVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterVendorId.setStatus("current")


class _FilterVendorType_Type(Integer32):
    """Custom type filterVendorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("invalid", 2),
          ("permit", 3))
    )


_FilterVendorType_Type.__name__ = "Integer32"
_FilterVendorType_Object = MibTableColumn
filterVendorType = _FilterVendorType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 2, 1, 4),
    _FilterVendorType_Type()
)
filterVendorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterVendorType.setStatus("current")
_FilterProtocolTable_Object = MibTable
filterProtocolTable = _FilterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 3)
)
if mibBuilder.loadTexts:
    filterProtocolTable.setStatus("current")
_FilterProtocolEntry_Object = MibTableRow
filterProtocolEntry = _FilterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 3, 1)
)
filterProtocolEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "filterProtocolModule"),
    (0, "CISCO-STACK-MIB", "filterProtocolPort"),
    (0, "CISCO-STACK-MIB", "filterProtocolValue"),
)
if mibBuilder.loadTexts:
    filterProtocolEntry.setStatus("current")


class _FilterProtocolModule_Type(Integer32):
    """Custom type filterProtocolModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FilterProtocolModule_Type.__name__ = "Integer32"
_FilterProtocolModule_Object = MibTableColumn
filterProtocolModule = _FilterProtocolModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 3, 1, 1),
    _FilterProtocolModule_Type()
)
filterProtocolModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProtocolModule.setStatus("current")


class _FilterProtocolPort_Type(Integer32):
    """Custom type filterProtocolPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FilterProtocolPort_Type.__name__ = "Integer32"
_FilterProtocolPort_Object = MibTableColumn
filterProtocolPort = _FilterProtocolPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 3, 1, 2),
    _FilterProtocolPort_Type()
)
filterProtocolPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProtocolPort.setStatus("current")


class _FilterProtocolValue_Type(Integer32):
    """Custom type filterProtocolValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterProtocolValue_Type.__name__ = "Integer32"
_FilterProtocolValue_Object = MibTableColumn
filterProtocolValue = _FilterProtocolValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 3, 1, 3),
    _FilterProtocolValue_Type()
)
filterProtocolValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterProtocolValue.setStatus("current")


class _FilterProtocolType_Type(Integer32):
    """Custom type filterProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("invalid", 2),
          ("permit", 3))
    )


_FilterProtocolType_Type.__name__ = "Integer32"
_FilterProtocolType_Object = MibTableColumn
filterProtocolType = _FilterProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 3, 1, 4),
    _FilterProtocolType_Type()
)
filterProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterProtocolType.setStatus("current")
_FilterTestTable_Object = MibTable
filterTestTable = _FilterTestTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4)
)
if mibBuilder.loadTexts:
    filterTestTable.setStatus("current")
_FilterTestEntry_Object = MibTableRow
filterTestEntry = _FilterTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1)
)
filterTestEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "filterTestModule"),
    (0, "CISCO-STACK-MIB", "filterTestPort"),
    (0, "CISCO-STACK-MIB", "filterTestIndex"),
)
if mibBuilder.loadTexts:
    filterTestEntry.setStatus("current")


class _FilterTestModule_Type(Integer32):
    """Custom type filterTestModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FilterTestModule_Type.__name__ = "Integer32"
_FilterTestModule_Object = MibTableColumn
filterTestModule = _FilterTestModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 1),
    _FilterTestModule_Type()
)
filterTestModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTestModule.setStatus("current")


class _FilterTestPort_Type(Integer32):
    """Custom type filterTestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FilterTestPort_Type.__name__ = "Integer32"
_FilterTestPort_Object = MibTableColumn
filterTestPort = _FilterTestPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 2),
    _FilterTestPort_Type()
)
filterTestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTestPort.setStatus("current")


class _FilterTestIndex_Type(Integer32):
    """Custom type filterTestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FilterTestIndex_Type.__name__ = "Integer32"
_FilterTestIndex_Object = MibTableColumn
filterTestIndex = _FilterTestIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 3),
    _FilterTestIndex_Type()
)
filterTestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterTestIndex.setStatus("current")


class _FilterTestType_Type(Integer32):
    """Custom type filterTestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_FilterTestType_Type.__name__ = "Integer32"
_FilterTestType_Object = MibTableColumn
filterTestType = _FilterTestType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 4),
    _FilterTestType_Type()
)
filterTestType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterTestType.setStatus("current")


class _FilterTestOffset_Type(Integer32):
    """Custom type filterTestOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500),
    )


_FilterTestOffset_Type.__name__ = "Integer32"
_FilterTestOffset_Object = MibTableColumn
filterTestOffset = _FilterTestOffset_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 5),
    _FilterTestOffset_Type()
)
filterTestOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterTestOffset.setStatus("current")


class _FilterTestValue_Type(Integer32):
    """Custom type filterTestValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FilterTestValue_Type.__name__ = "Integer32"
_FilterTestValue_Object = MibTableColumn
filterTestValue = _FilterTestValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 6),
    _FilterTestValue_Type()
)
filterTestValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterTestValue.setStatus("current")


class _FilterTestMask_Type(Integer32):
    """Custom type filterTestMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FilterTestMask_Type.__name__ = "Integer32"
_FilterTestMask_Object = MibTableColumn
filterTestMask = _FilterTestMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 4, 1, 7),
    _FilterTestMask_Type()
)
filterTestMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    filterTestMask.setStatus("current")
_FilterPortTable_Object = MibTable
filterPortTable = _FilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5)
)
if mibBuilder.loadTexts:
    filterPortTable.setStatus("current")
_FilterPortEntry_Object = MibTableRow
filterPortEntry = _FilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1)
)
filterPortEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "filterPortModule"),
    (0, "CISCO-STACK-MIB", "filterPort"),
)
if mibBuilder.loadTexts:
    filterPortEntry.setStatus("current")


class _FilterPortModule_Type(Integer32):
    """Custom type filterPortModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FilterPortModule_Type.__name__ = "Integer32"
_FilterPortModule_Object = MibTableColumn
filterPortModule = _FilterPortModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 1),
    _FilterPortModule_Type()
)
filterPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterPortModule.setStatus("current")


class _FilterPort_Type(Integer32):
    """Custom type filterPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FilterPort_Type.__name__ = "Integer32"
_FilterPort_Object = MibTableColumn
filterPort = _FilterPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 2),
    _FilterPort_Type()
)
filterPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterPort.setStatus("current")


class _FilterPortComplex_Type(DisplayString):
    """Custom type filterPortComplex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_FilterPortComplex_Type.__name__ = "DisplayString"
_FilterPortComplex_Object = MibTableColumn
filterPortComplex = _FilterPortComplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 3),
    _FilterPortComplex_Type()
)
filterPortComplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortComplex.setStatus("current")


class _FilterPortBroadcastThrottle_Type(Integer32):
    """Custom type filterPortBroadcastThrottle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 150000),
    )


_FilterPortBroadcastThrottle_Type.__name__ = "Integer32"
_FilterPortBroadcastThrottle_Object = MibTableColumn
filterPortBroadcastThrottle = _FilterPortBroadcastThrottle_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 4),
    _FilterPortBroadcastThrottle_Type()
)
filterPortBroadcastThrottle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortBroadcastThrottle.setStatus("current")


class _FilterPortBroadcastThreshold_Type(Integer32):
    """Custom type filterPortBroadcastThreshold based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FilterPortBroadcastThreshold_Type.__name__ = "Integer32"
_FilterPortBroadcastThreshold_Object = MibTableColumn
filterPortBroadcastThreshold = _FilterPortBroadcastThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 5),
    _FilterPortBroadcastThreshold_Type()
)
filterPortBroadcastThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortBroadcastThreshold.setStatus("current")
_FilterPortBroadcastDiscards_Type = Counter32
_FilterPortBroadcastDiscards_Object = MibTableColumn
filterPortBroadcastDiscards = _FilterPortBroadcastDiscards_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 6),
    _FilterPortBroadcastDiscards_Type()
)
filterPortBroadcastDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filterPortBroadcastDiscards.setStatus("current")


class _FilterPortBroadcastThresholdFraction_Type(Integer32):
    """Custom type filterPortBroadcastThresholdFraction based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_FilterPortBroadcastThresholdFraction_Type.__name__ = "Integer32"
_FilterPortBroadcastThresholdFraction_Object = MibTableColumn
filterPortBroadcastThresholdFraction = _FilterPortBroadcastThresholdFraction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 7),
    _FilterPortBroadcastThresholdFraction_Type()
)
filterPortBroadcastThresholdFraction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortBroadcastThresholdFraction.setStatus("current")
if mibBuilder.loadTexts:
    filterPortBroadcastThresholdFraction.setUnits("one-hundredths")


class _FilterPortSuppressionOption_Type(Bits):
    """Custom type filterPortSuppressionOption based on Bits"""
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("multicast", 0),
          ("unicast", 1))
    )

_FilterPortSuppressionOption_Type.__name__ = "Bits"
_FilterPortSuppressionOption_Object = MibTableColumn
filterPortSuppressionOption = _FilterPortSuppressionOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 8),
    _FilterPortSuppressionOption_Type()
)
filterPortSuppressionOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortSuppressionOption.setStatus("current")


class _FilterPortSuppressionViolation_Type(Integer32):
    """Custom type filterPortSuppressionViolation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dropPackets", 1),
          ("errdisable", 2))
    )


_FilterPortSuppressionViolation_Type.__name__ = "Integer32"
_FilterPortSuppressionViolation_Object = MibTableColumn
filterPortSuppressionViolation = _FilterPortSuppressionViolation_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 7, 5, 1, 9),
    _FilterPortSuppressionViolation_Type()
)
filterPortSuppressionViolation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterPortSuppressionViolation.setStatus("current")
_MonitorGrp_ObjectIdentity = ObjectIdentity
monitorGrp = _MonitorGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8)
)


class _MonitorSourceModule_Type(Integer32):
    """Custom type monitorSourceModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MonitorSourceModule_Type.__name__ = "Integer32"
_MonitorSourceModule_Object = MibScalar
monitorSourceModule = _MonitorSourceModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 1),
    _MonitorSourceModule_Type()
)
monitorSourceModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorSourceModule.setStatus("deprecated")


class _MonitorSourcePort_Type(Integer32):
    """Custom type monitorSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_MonitorSourcePort_Type.__name__ = "Integer32"
_MonitorSourcePort_Object = MibScalar
monitorSourcePort = _MonitorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 2),
    _MonitorSourcePort_Type()
)
monitorSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorSourcePort.setStatus("deprecated")


class _MonitorDestinationModule_Type(Integer32):
    """Custom type monitorDestinationModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MonitorDestinationModule_Type.__name__ = "Integer32"
_MonitorDestinationModule_Object = MibScalar
monitorDestinationModule = _MonitorDestinationModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 3),
    _MonitorDestinationModule_Type()
)
monitorDestinationModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDestinationModule.setStatus("deprecated")


class _MonitorDestinationPort_Type(Integer32):
    """Custom type monitorDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_MonitorDestinationPort_Type.__name__ = "Integer32"
_MonitorDestinationPort_Object = MibScalar
monitorDestinationPort = _MonitorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 4),
    _MonitorDestinationPort_Type()
)
monitorDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDestinationPort.setStatus("deprecated")


class _MonitorDirection_Type(Integer32):
    """Custom type monitorDirection based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("receive", 2),
          ("transmit", 1),
          ("transmitAndReceive", 3))
    )


_MonitorDirection_Type.__name__ = "Integer32"
_MonitorDirection_Object = MibScalar
monitorDirection = _MonitorDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 5),
    _MonitorDirection_Type()
)
monitorDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorDirection.setStatus("deprecated")


class _MonitorEnable_Type(Integer32):
    """Custom type monitorEnable based on Integer32"""
    defaultValue = 2

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


_MonitorEnable_Type.__name__ = "Integer32"
_MonitorEnable_Object = MibScalar
monitorEnable = _MonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 6),
    _MonitorEnable_Type()
)
monitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorEnable.setStatus("deprecated")


class _MonitorAdminSourcePorts_Type(OctetString):
    """Custom type monitorAdminSourcePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MonitorAdminSourcePorts_Type.__name__ = "OctetString"
_MonitorAdminSourcePorts_Object = MibScalar
monitorAdminSourcePorts = _MonitorAdminSourcePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 7),
    _MonitorAdminSourcePorts_Type()
)
monitorAdminSourcePorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    monitorAdminSourcePorts.setStatus("deprecated")


class _MonitorOperSourcePorts_Type(OctetString):
    """Custom type monitorOperSourcePorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MonitorOperSourcePorts_Type.__name__ = "OctetString"
_MonitorOperSourcePorts_Object = MibScalar
monitorOperSourcePorts = _MonitorOperSourcePorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 8, 8),
    _MonitorOperSourcePorts_Type()
)
monitorOperSourcePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    monitorOperSourcePorts.setStatus("deprecated")
_VlanGrp_ObjectIdentity = ObjectIdentity
vlanGrp = _VlanGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 2)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("deprecated")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 2, 1)
)
vlanEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("deprecated")
_VlanIndex_Type = VlanIndex
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 2, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("deprecated")


class _VlanSpantreeEnable_Type(Integer32):
    """Custom type vlanSpantreeEnable based on Integer32"""
    defaultValue = 1

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
          ("enabled", 1),
          ("notApplicable", 3))
    )


_VlanSpantreeEnable_Type.__name__ = "Integer32"
_VlanSpantreeEnable_Object = MibTableColumn
vlanSpantreeEnable = _VlanSpantreeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 2, 1, 2),
    _VlanSpantreeEnable_Type()
)
vlanSpantreeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanSpantreeEnable.setStatus("deprecated")


class _VlanIfIndex_Type(Integer32):
    """Custom type vlanIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VlanIfIndex_Type.__name__ = "Integer32"
_VlanIfIndex_Object = MibTableColumn
vlanIfIndex = _VlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 2, 1, 3),
    _VlanIfIndex_Type()
)
vlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanIfIndex.setStatus("deprecated")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1)
)
vlanPortEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "vlanPortModule"),
    (0, "CISCO-STACK-MIB", "vlanPort"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")


class _VlanPortModule_Type(Integer32):
    """Custom type vlanPortModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VlanPortModule_Type.__name__ = "Integer32"
_VlanPortModule_Object = MibTableColumn
vlanPortModule = _VlanPortModule_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 1),
    _VlanPortModule_Type()
)
vlanPortModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortModule.setStatus("current")


class _VlanPort_Type(Integer32):
    """Custom type vlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VlanPort_Type.__name__ = "Integer32"
_VlanPort_Object = MibTableColumn
vlanPort = _VlanPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 2),
    _VlanPort_Type()
)
vlanPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPort.setStatus("current")
_VlanPortVlan_Type = VlanIndex
_VlanPortVlan_Object = MibTableColumn
vlanPortVlan = _VlanPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 3),
    _VlanPortVlan_Type()
)
vlanPortVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortVlan.setStatus("current")


class _VlanPortIslVlansAllowed_Type(OctetString):
    """Custom type vlanPortIslVlansAllowed based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanPortIslVlansAllowed_Type.__name__ = "OctetString"
_VlanPortIslVlansAllowed_Object = MibTableColumn
vlanPortIslVlansAllowed = _VlanPortIslVlansAllowed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 5),
    _VlanPortIslVlansAllowed_Type()
)
vlanPortIslVlansAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortIslVlansAllowed.setStatus("current")


class _VlanPortSwitchLevel_Type(Integer32):
    """Custom type vlanPortSwitchLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("normal", 1),
          ("notApplicable", 3))
    )


_VlanPortSwitchLevel_Type.__name__ = "Integer32"
_VlanPortSwitchLevel_Object = MibTableColumn
vlanPortSwitchLevel = _VlanPortSwitchLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 6),
    _VlanPortSwitchLevel_Type()
)
vlanPortSwitchLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortSwitchLevel.setStatus("current")


class _VlanPortIslAdminStatus_Type(Integer32):
    """Custom type vlanPortIslAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("desirable", 3),
          ("off", 2),
          ("on", 1),
          ("onNoNegotiate", 5))
    )


_VlanPortIslAdminStatus_Type.__name__ = "Integer32"
_VlanPortIslAdminStatus_Object = MibTableColumn
vlanPortIslAdminStatus = _VlanPortIslAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 7),
    _VlanPortIslAdminStatus_Type()
)
vlanPortIslAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortIslAdminStatus.setStatus("current")


class _VlanPortIslOperStatus_Type(Integer32):
    """Custom type vlanPortIslOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTrunking", 2),
          ("trunking", 1))
    )


_VlanPortIslOperStatus_Type.__name__ = "Integer32"
_VlanPortIslOperStatus_Object = MibTableColumn
vlanPortIslOperStatus = _VlanPortIslOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 8),
    _VlanPortIslOperStatus_Type()
)
vlanPortIslOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortIslOperStatus.setStatus("current")


class _VlanPortIslPriorityVlans_Type(OctetString):
    """Custom type vlanPortIslPriorityVlans based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_VlanPortIslPriorityVlans_Type.__name__ = "OctetString"
_VlanPortIslPriorityVlans_Object = MibTableColumn
vlanPortIslPriorityVlans = _VlanPortIslPriorityVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 9),
    _VlanPortIslPriorityVlans_Type()
)
vlanPortIslPriorityVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortIslPriorityVlans.setStatus("current")


class _VlanPortAdminStatus_Type(Integer32):
    """Custom type vlanPortAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_VlanPortAdminStatus_Type.__name__ = "Integer32"
_VlanPortAdminStatus_Object = MibTableColumn
vlanPortAdminStatus = _VlanPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 10),
    _VlanPortAdminStatus_Type()
)
vlanPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortAdminStatus.setStatus("current")


class _VlanPortOperStatus_Type(Integer32):
    """Custom type vlanPortOperStatus based on Integer32"""
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
        *(("active", 2),
          ("inactive", 1),
          ("shutdown", 3),
          ("vlanActiveFault", 4))
    )


_VlanPortOperStatus_Type.__name__ = "Integer32"
_VlanPortOperStatus_Object = MibTableColumn
vlanPortOperStatus = _VlanPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 11),
    _VlanPortOperStatus_Type()
)
vlanPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanPortOperStatus.setStatus("current")


class _VlanPortAuxiliaryVlan_Type(Integer32):
    """Custom type vlanPortAuxiliaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 1000),
        ValueRangeConstraint(1025, 4094),
        ValueRangeConstraint(4095, 4095),
        ValueRangeConstraint(4096, 4096),
    )


_VlanPortAuxiliaryVlan_Type.__name__ = "Integer32"
_VlanPortAuxiliaryVlan_Object = MibTableColumn
vlanPortAuxiliaryVlan = _VlanPortAuxiliaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 3, 1, 12),
    _VlanPortAuxiliaryVlan_Type()
)
vlanPortAuxiliaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortAuxiliaryVlan.setStatus("deprecated")
_VmpsTable_Object = MibTable
vmpsTable = _VmpsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 4)
)
if mibBuilder.loadTexts:
    vmpsTable.setStatus("current")
_VmpsEntry_Object = MibTableRow
vmpsEntry = _VmpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 4, 1)
)
vmpsEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "vmpsAddr"),
)
if mibBuilder.loadTexts:
    vmpsEntry.setStatus("current")
_VmpsAddr_Type = IpAddress
_VmpsAddr_Object = MibTableColumn
vmpsAddr = _VmpsAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 4, 1, 1),
    _VmpsAddr_Type()
)
vmpsAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsAddr.setStatus("current")


class _VmpsType_Type(Integer32):
    """Custom type vmpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("other", 3),
          ("primary", 2))
    )


_VmpsType_Type.__name__ = "Integer32"
_VmpsType_Object = MibTableColumn
vmpsType = _VmpsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 4, 1, 2),
    _VmpsType_Type()
)
vmpsType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vmpsType.setStatus("current")


class _VmpsAction_Type(Integer32):
    """Custom type vmpsAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 2),
          ("noDynamicPort", 6),
          ("noHostConnected", 7),
          ("noPrimaryVmps", 5),
          ("noResponse", 4),
          ("other", 1),
          ("reconfirm", 8),
          ("success", 3))
    )


_VmpsAction_Type.__name__ = "Integer32"
_VmpsAction_Object = MibScalar
vmpsAction = _VmpsAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 5),
    _VmpsAction_Type()
)
vmpsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vmpsAction.setStatus("current")
_VmpsAccessed_Type = IpAddress
_VmpsAccessed_Object = MibScalar
vmpsAccessed = _VmpsAccessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 6),
    _VmpsAccessed_Type()
)
vmpsAccessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmpsAccessed.setStatus("current")


class _VlanTrunkMappingMax_Type(Unsigned32):
    """Custom type vlanTrunkMappingMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanTrunkMappingMax_Type.__name__ = "Unsigned32"
_VlanTrunkMappingMax_Object = MibScalar
vlanTrunkMappingMax = _VlanTrunkMappingMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 7),
    _VlanTrunkMappingMax_Type()
)
vlanTrunkMappingMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkMappingMax.setStatus("current")
if mibBuilder.loadTexts:
    vlanTrunkMappingMax.setUnits("entries")
_VlanTrunkMappingTable_Object = MibTable
vlanTrunkMappingTable = _VlanTrunkMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8)
)
if mibBuilder.loadTexts:
    vlanTrunkMappingTable.setStatus("current")
_VlanTrunkMappingEntry_Object = MibTableRow
vlanTrunkMappingEntry = _VlanTrunkMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8, 1)
)
vlanTrunkMappingEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "vlanTrunkMappingFromVlan"),
)
if mibBuilder.loadTexts:
    vlanTrunkMappingEntry.setStatus("current")
_VlanTrunkMappingFromVlan_Type = VlanIndex
_VlanTrunkMappingFromVlan_Object = MibTableColumn
vlanTrunkMappingFromVlan = _VlanTrunkMappingFromVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8, 1, 1),
    _VlanTrunkMappingFromVlan_Type()
)
vlanTrunkMappingFromVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanTrunkMappingFromVlan.setStatus("current")
_VlanTrunkMappingToVlan_Type = VlanIndex
_VlanTrunkMappingToVlan_Object = MibTableColumn
vlanTrunkMappingToVlan = _VlanTrunkMappingToVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8, 1, 2),
    _VlanTrunkMappingToVlan_Type()
)
vlanTrunkMappingToVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkMappingToVlan.setStatus("current")


class _VlanTrunkMappingType_Type(Integer32):
    """Custom type vlanTrunkMappingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1qToisl", 2),
          ("reservedToNonReserved", 1))
    )


_VlanTrunkMappingType_Type.__name__ = "Integer32"
_VlanTrunkMappingType_Object = MibTableColumn
vlanTrunkMappingType = _VlanTrunkMappingType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8, 1, 3),
    _VlanTrunkMappingType_Type()
)
vlanTrunkMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkMappingType.setStatus("current")
_VlanTrunkMappingOper_Type = TruthValue
_VlanTrunkMappingOper_Object = MibTableColumn
vlanTrunkMappingOper = _VlanTrunkMappingOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8, 1, 4),
    _VlanTrunkMappingOper_Type()
)
vlanTrunkMappingOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanTrunkMappingOper.setStatus("current")
_VlanTrunkMappingStatus_Type = RowStatus
_VlanTrunkMappingStatus_Object = MibTableColumn
vlanTrunkMappingStatus = _VlanTrunkMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 9, 8, 1, 5),
    _VlanTrunkMappingStatus_Type()
)
vlanTrunkMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanTrunkMappingStatus.setStatus("current")
_SecurityGrp_ObjectIdentity = ObjectIdentity
securityGrp = _SecurityGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10)
)
_PortSecurityTable_Object = MibTable
portSecurityTable = _PortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1)
)
if mibBuilder.loadTexts:
    portSecurityTable.setStatus("current")
_PortSecurityEntry_Object = MibTableRow
portSecurityEntry = _PortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1)
)
portSecurityEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portSecurityModuleIndex"),
    (0, "CISCO-STACK-MIB", "portSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    portSecurityEntry.setStatus("current")


class _PortSecurityModuleIndex_Type(Integer32):
    """Custom type portSecurityModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortSecurityModuleIndex_Type.__name__ = "Integer32"
_PortSecurityModuleIndex_Object = MibTableColumn
portSecurityModuleIndex = _PortSecurityModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 1),
    _PortSecurityModuleIndex_Type()
)
portSecurityModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityModuleIndex.setStatus("current")


class _PortSecurityPortIndex_Type(Integer32):
    """Custom type portSecurityPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortSecurityPortIndex_Type.__name__ = "Integer32"
_PortSecurityPortIndex_Object = MibTableColumn
portSecurityPortIndex = _PortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 2),
    _PortSecurityPortIndex_Type()
)
portSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityPortIndex.setStatus("current")


class _PortSecurityAdminStatus_Type(Integer32):
    """Custom type portSecurityAdminStatus based on Integer32"""
    defaultValue = 2

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


_PortSecurityAdminStatus_Type.__name__ = "Integer32"
_PortSecurityAdminStatus_Object = MibTableColumn
portSecurityAdminStatus = _PortSecurityAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 3),
    _PortSecurityAdminStatus_Type()
)
portSecurityAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityAdminStatus.setStatus("current")


class _PortSecurityOperStatus_Type(Integer32):
    """Custom type portSecurityOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notShutdown", 1),
          ("shutdown", 2))
    )


_PortSecurityOperStatus_Type.__name__ = "Integer32"
_PortSecurityOperStatus_Object = MibTableColumn
portSecurityOperStatus = _PortSecurityOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 4),
    _PortSecurityOperStatus_Type()
)
portSecurityOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityOperStatus.setStatus("current")


class _PortSecurityLastSrcAddr_Type(OctetString):
    """Custom type portSecurityLastSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortSecurityLastSrcAddr_Type.__name__ = "OctetString"
_PortSecurityLastSrcAddr_Object = MibTableColumn
portSecurityLastSrcAddr = _PortSecurityLastSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 5),
    _PortSecurityLastSrcAddr_Type()
)
portSecurityLastSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityLastSrcAddr.setStatus("current")


class _PortSecuritySecureSrcAddr_Type(OctetString):
    """Custom type portSecuritySecureSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortSecuritySecureSrcAddr_Type.__name__ = "OctetString"
_PortSecuritySecureSrcAddr_Object = MibTableColumn
portSecuritySecureSrcAddr = _PortSecuritySecureSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 6),
    _PortSecuritySecureSrcAddr_Type()
)
portSecuritySecureSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecuritySecureSrcAddr.setStatus("current")


class _PortSecurityMaxSrcAddr_Type(Integer32):
    """Custom type portSecurityMaxSrcAddr based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1025),
    )


_PortSecurityMaxSrcAddr_Type.__name__ = "Integer32"
_PortSecurityMaxSrcAddr_Object = MibTableColumn
portSecurityMaxSrcAddr = _PortSecurityMaxSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 7),
    _PortSecurityMaxSrcAddr_Type()
)
portSecurityMaxSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityMaxSrcAddr.setStatus("current")


class _PortSecurityAgingTime_Type(Integer32):
    """Custom type portSecurityAgingTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1440),
    )


_PortSecurityAgingTime_Type.__name__ = "Integer32"
_PortSecurityAgingTime_Object = MibTableColumn
portSecurityAgingTime = _PortSecurityAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 8),
    _PortSecurityAgingTime_Type()
)
portSecurityAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    portSecurityAgingTime.setUnits("minutes")


class _PortSecurityShutdownTimeOut_Type(Integer32):
    """Custom type portSecurityShutdownTimeOut based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 1440),
    )


_PortSecurityShutdownTimeOut_Type.__name__ = "Integer32"
_PortSecurityShutdownTimeOut_Object = MibTableColumn
portSecurityShutdownTimeOut = _PortSecurityShutdownTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 9),
    _PortSecurityShutdownTimeOut_Type()
)
portSecurityShutdownTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityShutdownTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    portSecurityShutdownTimeOut.setUnits("minutes")


class _PortSecurityViolationPolicy_Type(Integer32):
    """Custom type portSecurityViolationPolicy based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restrict", 1),
          ("shutdown", 2))
    )


_PortSecurityViolationPolicy_Type.__name__ = "Integer32"
_PortSecurityViolationPolicy_Object = MibTableColumn
portSecurityViolationPolicy = _PortSecurityViolationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 1, 1, 10),
    _PortSecurityViolationPolicy_Type()
)
portSecurityViolationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecurityViolationPolicy.setStatus("current")
_PortSecurityExtTable_Object = MibTable
portSecurityExtTable = _PortSecurityExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 2)
)
if mibBuilder.loadTexts:
    portSecurityExtTable.setStatus("current")
_PortSecurityExtEntry_Object = MibTableRow
portSecurityExtEntry = _PortSecurityExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 2, 1)
)
portSecurityExtEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portSecurityExtModuleIndex"),
    (0, "CISCO-STACK-MIB", "portSecurityExtPortIndex"),
    (0, "CISCO-STACK-MIB", "portSecurityExtSecureSrcAddr"),
)
if mibBuilder.loadTexts:
    portSecurityExtEntry.setStatus("current")


class _PortSecurityExtModuleIndex_Type(Integer32):
    """Custom type portSecurityExtModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortSecurityExtModuleIndex_Type.__name__ = "Integer32"
_PortSecurityExtModuleIndex_Object = MibTableColumn
portSecurityExtModuleIndex = _PortSecurityExtModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 2, 1, 1),
    _PortSecurityExtModuleIndex_Type()
)
portSecurityExtModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityExtModuleIndex.setStatus("current")


class _PortSecurityExtPortIndex_Type(Integer32):
    """Custom type portSecurityExtPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortSecurityExtPortIndex_Type.__name__ = "Integer32"
_PortSecurityExtPortIndex_Object = MibTableColumn
portSecurityExtPortIndex = _PortSecurityExtPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 2, 1, 2),
    _PortSecurityExtPortIndex_Type()
)
portSecurityExtPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityExtPortIndex.setStatus("current")


class _PortSecurityExtSecureSrcAddr_Type(OctetString):
    """Custom type portSecurityExtSecureSrcAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortSecurityExtSecureSrcAddr_Type.__name__ = "OctetString"
_PortSecurityExtSecureSrcAddr_Object = MibTableColumn
portSecurityExtSecureSrcAddr = _PortSecurityExtSecureSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 2, 1, 3),
    _PortSecurityExtSecureSrcAddr_Type()
)
portSecurityExtSecureSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSecurityExtSecureSrcAddr.setStatus("current")


class _PortSecurityExtControlStatus_Type(Integer32):
    """Custom type portSecurityExtControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_PortSecurityExtControlStatus_Type.__name__ = "Integer32"
_PortSecurityExtControlStatus_Object = MibTableColumn
portSecurityExtControlStatus = _PortSecurityExtControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 10, 2, 1, 4),
    _PortSecurityExtControlStatus_Type()
)
portSecurityExtControlStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portSecurityExtControlStatus.setStatus("current")
_TokenRingGrp_ObjectIdentity = ObjectIdentity
tokenRingGrp = _TokenRingGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11)
)
_TokenRingPortTable_Object = MibTable
tokenRingPortTable = _TokenRingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1)
)
if mibBuilder.loadTexts:
    tokenRingPortTable.setStatus("current")
_TokenRingPortEntry_Object = MibTableRow
tokenRingPortEntry = _TokenRingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1)
)
tokenRingPortEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "tokenRingModuleIndex"),
    (0, "CISCO-STACK-MIB", "tokenRingPortIndex"),
)
if mibBuilder.loadTexts:
    tokenRingPortEntry.setStatus("current")


class _TokenRingModuleIndex_Type(Integer32):
    """Custom type tokenRingModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_TokenRingModuleIndex_Type.__name__ = "Integer32"
_TokenRingModuleIndex_Object = MibTableColumn
tokenRingModuleIndex = _TokenRingModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 1),
    _TokenRingModuleIndex_Type()
)
tokenRingModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingModuleIndex.setStatus("current")


class _TokenRingPortIndex_Type(Integer32):
    """Custom type tokenRingPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokenRingPortIndex_Type.__name__ = "Integer32"
_TokenRingPortIndex_Object = MibTableColumn
tokenRingPortIndex = _TokenRingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 2),
    _TokenRingPortIndex_Type()
)
tokenRingPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPortIndex.setStatus("current")


class _TokenRingPortSetACbits_Type(Integer32):
    """Custom type tokenRingPortSetACbits based on Integer32"""
    defaultValue = 2

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


_TokenRingPortSetACbits_Type.__name__ = "Integer32"
_TokenRingPortSetACbits_Object = MibTableColumn
tokenRingPortSetACbits = _TokenRingPortSetACbits_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 3),
    _TokenRingPortSetACbits_Type()
)
tokenRingPortSetACbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortSetACbits.setStatus("current")


class _TokenRingPortMode_Type(Integer32):
    """Custom type tokenRingPortMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("fdxCport", 2),
          ("fdxStation", 3),
          ("hdxCport", 4),
          ("hdxStation", 5),
          ("riro", 7))
    )


_TokenRingPortMode_Type.__name__ = "Integer32"
_TokenRingPortMode_Object = MibTableColumn
tokenRingPortMode = _TokenRingPortMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 4),
    _TokenRingPortMode_Type()
)
tokenRingPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortMode.setStatus("current")


class _TokenRingPortEarlyTokenRel_Type(Integer32):
    """Custom type tokenRingPortEarlyTokenRel based on Integer32"""
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


_TokenRingPortEarlyTokenRel_Type.__name__ = "Integer32"
_TokenRingPortEarlyTokenRel_Object = MibTableColumn
tokenRingPortEarlyTokenRel = _TokenRingPortEarlyTokenRel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 9),
    _TokenRingPortEarlyTokenRel_Type()
)
tokenRingPortEarlyTokenRel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortEarlyTokenRel.setStatus("current")


class _TokenRingPortPriorityThresh_Type(Integer32):
    """Custom type tokenRingPortPriorityThresh based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_TokenRingPortPriorityThresh_Type.__name__ = "Integer32"
_TokenRingPortPriorityThresh_Object = MibTableColumn
tokenRingPortPriorityThresh = _TokenRingPortPriorityThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 10),
    _TokenRingPortPriorityThresh_Type()
)
tokenRingPortPriorityThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortPriorityThresh.setStatus("current")


class _TokenRingPortPriorityMinXmit_Type(Integer32):
    """Custom type tokenRingPortPriorityMinXmit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_TokenRingPortPriorityMinXmit_Type.__name__ = "Integer32"
_TokenRingPortPriorityMinXmit_Object = MibTableColumn
tokenRingPortPriorityMinXmit = _TokenRingPortPriorityMinXmit_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 11),
    _TokenRingPortPriorityMinXmit_Type()
)
tokenRingPortPriorityMinXmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortPriorityMinXmit.setStatus("current")


class _TokenRingPortCfgLossThresh_Type(Integer32):
    """Custom type tokenRingPortCfgLossThresh based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TokenRingPortCfgLossThresh_Type.__name__ = "Integer32"
_TokenRingPortCfgLossThresh_Object = MibTableColumn
tokenRingPortCfgLossThresh = _TokenRingPortCfgLossThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 12),
    _TokenRingPortCfgLossThresh_Type()
)
tokenRingPortCfgLossThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortCfgLossThresh.setStatus("current")


class _TokenRingPortCfgLossInterval_Type(Integer32):
    """Custom type tokenRingPortCfgLossInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_TokenRingPortCfgLossInterval_Type.__name__ = "Integer32"
_TokenRingPortCfgLossInterval_Object = MibTableColumn
tokenRingPortCfgLossInterval = _TokenRingPortCfgLossInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 1, 1, 13),
    _TokenRingPortCfgLossInterval_Type()
)
tokenRingPortCfgLossInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortCfgLossInterval.setStatus("current")


class _TokenRingDripDistCrfMode_Type(Integer32):
    """Custom type tokenRingDripDistCrfMode based on Integer32"""
    defaultValue = 2

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


_TokenRingDripDistCrfMode_Type.__name__ = "Integer32"
_TokenRingDripDistCrfMode_Object = MibScalar
tokenRingDripDistCrfMode = _TokenRingDripDistCrfMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 2),
    _TokenRingDripDistCrfMode_Type()
)
tokenRingDripDistCrfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingDripDistCrfMode.setStatus("current")


class _TokenRingDripAreReductionMode_Type(Integer32):
    """Custom type tokenRingDripAreReductionMode based on Integer32"""
    defaultValue = 1

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


_TokenRingDripAreReductionMode_Type.__name__ = "Integer32"
_TokenRingDripAreReductionMode_Object = MibScalar
tokenRingDripAreReductionMode = _TokenRingDripAreReductionMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 3),
    _TokenRingDripAreReductionMode_Type()
)
tokenRingDripAreReductionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingDripAreReductionMode.setStatus("current")


class _TokenRingDripLocalNodeID_Type(OctetString):
    """Custom type tokenRingDripLocalNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TokenRingDripLocalNodeID_Type.__name__ = "OctetString"
_TokenRingDripLocalNodeID_Object = MibScalar
tokenRingDripLocalNodeID = _TokenRingDripLocalNodeID_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 4),
    _TokenRingDripLocalNodeID_Type()
)
tokenRingDripLocalNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripLocalNodeID.setStatus("current")


class _TokenRingDripLastRevision_Type(Integer32):
    """Custom type tokenRingDripLastRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_TokenRingDripLastRevision_Type.__name__ = "Integer32"
_TokenRingDripLastRevision_Object = MibScalar
tokenRingDripLastRevision = _TokenRingDripLastRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 5),
    _TokenRingDripLastRevision_Type()
)
tokenRingDripLastRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripLastRevision.setStatus("current")


class _TokenRingDripLastChangedRevision_Type(Integer32):
    """Custom type tokenRingDripLastChangedRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_TokenRingDripLastChangedRevision_Type.__name__ = "Integer32"
_TokenRingDripLastChangedRevision_Object = MibScalar
tokenRingDripLastChangedRevision = _TokenRingDripLastChangedRevision_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 6),
    _TokenRingDripLastChangedRevision_Type()
)
tokenRingDripLastChangedRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripLastChangedRevision.setStatus("current")
_TokenRingDripAdvertsReceived_Type = Counter32
_TokenRingDripAdvertsReceived_Object = MibScalar
tokenRingDripAdvertsReceived = _TokenRingDripAdvertsReceived_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 7),
    _TokenRingDripAdvertsReceived_Type()
)
tokenRingDripAdvertsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripAdvertsReceived.setStatus("current")
_TokenRingDripAdvertsTransmitted_Type = Counter32
_TokenRingDripAdvertsTransmitted_Object = MibScalar
tokenRingDripAdvertsTransmitted = _TokenRingDripAdvertsTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 8),
    _TokenRingDripAdvertsTransmitted_Type()
)
tokenRingDripAdvertsTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripAdvertsTransmitted.setStatus("current")
_TokenRingDripAdvertsProcessed_Type = Counter32
_TokenRingDripAdvertsProcessed_Object = MibScalar
tokenRingDripAdvertsProcessed = _TokenRingDripAdvertsProcessed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 9),
    _TokenRingDripAdvertsProcessed_Type()
)
tokenRingDripAdvertsProcessed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripAdvertsProcessed.setStatus("current")
_TokenRingDripInputQueueDrops_Type = Counter32
_TokenRingDripInputQueueDrops_Object = MibScalar
tokenRingDripInputQueueDrops = _TokenRingDripInputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 10),
    _TokenRingDripInputQueueDrops_Type()
)
tokenRingDripInputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripInputQueueDrops.setStatus("current")
_TokenRingDripOutputQueueDrops_Type = Counter32
_TokenRingDripOutputQueueDrops_Object = MibScalar
tokenRingDripOutputQueueDrops = _TokenRingDripOutputQueueDrops_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 11),
    _TokenRingDripOutputQueueDrops_Type()
)
tokenRingDripOutputQueueDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripOutputQueueDrops.setStatus("current")
_TokenRingDripLocalVlanStatusTable_Object = MibTable
tokenRingDripLocalVlanStatusTable = _TokenRingDripLocalVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12)
)
if mibBuilder.loadTexts:
    tokenRingDripLocalVlanStatusTable.setStatus("current")
_TokenRingDripLocalVlanStatusEntry_Object = MibTableRow
tokenRingDripLocalVlanStatusEntry = _TokenRingDripLocalVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1)
)
tokenRingDripLocalVlanStatusEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "tokenRingDripVlan"),
)
if mibBuilder.loadTexts:
    tokenRingDripLocalVlanStatusEntry.setStatus("current")
_TokenRingDripVlan_Type = VlanIndex
_TokenRingDripVlan_Object = MibTableColumn
tokenRingDripVlan = _TokenRingDripVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 1),
    _TokenRingDripVlan_Type()
)
tokenRingDripVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripVlan.setStatus("current")


class _TokenRingDripLocalPortStatus_Type(Integer32):
    """Custom type tokenRingDripLocalPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_TokenRingDripLocalPortStatus_Type.__name__ = "Integer32"
_TokenRingDripLocalPortStatus_Object = MibTableColumn
tokenRingDripLocalPortStatus = _TokenRingDripLocalPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 2),
    _TokenRingDripLocalPortStatus_Type()
)
tokenRingDripLocalPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripLocalPortStatus.setStatus("current")


class _TokenRingDripRemotePortStatus_Type(Integer32):
    """Custom type tokenRingDripRemotePortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_TokenRingDripRemotePortStatus_Type.__name__ = "Integer32"
_TokenRingDripRemotePortStatus_Object = MibTableColumn
tokenRingDripRemotePortStatus = _TokenRingDripRemotePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 3),
    _TokenRingDripRemotePortStatus_Type()
)
tokenRingDripRemotePortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripRemotePortStatus.setStatus("current")


class _TokenRingDripRemotePortConfigured_Type(Integer32):
    """Custom type tokenRingDripRemotePortConfigured based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_TokenRingDripRemotePortConfigured_Type.__name__ = "Integer32"
_TokenRingDripRemotePortConfigured_Object = MibTableColumn
tokenRingDripRemotePortConfigured = _TokenRingDripRemotePortConfigured_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 4),
    _TokenRingDripRemotePortConfigured_Type()
)
tokenRingDripRemotePortConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripRemotePortConfigured.setStatus("current")


class _TokenRingDripDistributedCrf_Type(Integer32):
    """Custom type tokenRingDripDistributedCrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_TokenRingDripDistributedCrf_Type.__name__ = "Integer32"
_TokenRingDripDistributedCrf_Object = MibTableColumn
tokenRingDripDistributedCrf = _TokenRingDripDistributedCrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 5),
    _TokenRingDripDistributedCrf_Type()
)
tokenRingDripDistributedCrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripDistributedCrf.setStatus("current")


class _TokenRingDripBackupCrf_Type(Integer32):
    """Custom type tokenRingDripBackupCrf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )


_TokenRingDripBackupCrf_Type.__name__ = "Integer32"
_TokenRingDripBackupCrf_Object = MibTableColumn
tokenRingDripBackupCrf = _TokenRingDripBackupCrf_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 6),
    _TokenRingDripBackupCrf_Type()
)
tokenRingDripBackupCrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripBackupCrf.setStatus("current")


class _TokenRingDripOwnerNodeID_Type(OctetString):
    """Custom type tokenRingDripOwnerNodeID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_TokenRingDripOwnerNodeID_Type.__name__ = "OctetString"
_TokenRingDripOwnerNodeID_Object = MibTableColumn
tokenRingDripOwnerNodeID = _TokenRingDripOwnerNodeID_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 12, 1, 7),
    _TokenRingDripOwnerNodeID_Type()
)
tokenRingDripOwnerNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingDripOwnerNodeID.setStatus("current")
_TokenRingPortSoftErrTable_Object = MibTable
tokenRingPortSoftErrTable = _TokenRingPortSoftErrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14)
)
if mibBuilder.loadTexts:
    tokenRingPortSoftErrTable.setStatus("current")
_TokenRingPortSoftErrEntry_Object = MibTableRow
tokenRingPortSoftErrEntry = _TokenRingPortSoftErrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14, 1)
)
if mibBuilder.loadTexts:
    tokenRingPortSoftErrEntry.setStatus("current")


class _TokenRingPortSoftErrThresh_Type(Integer32):
    """Custom type tokenRingPortSoftErrThresh based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TokenRingPortSoftErrThresh_Type.__name__ = "Integer32"
_TokenRingPortSoftErrThresh_Object = MibTableColumn
tokenRingPortSoftErrThresh = _TokenRingPortSoftErrThresh_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14, 1, 1),
    _TokenRingPortSoftErrThresh_Type()
)
tokenRingPortSoftErrThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortSoftErrThresh.setStatus("current")


class _TokenRingPortSoftErrReportInterval_Type(Integer32):
    """Custom type tokenRingPortSoftErrReportInterval based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TokenRingPortSoftErrReportInterval_Type.__name__ = "Integer32"
_TokenRingPortSoftErrReportInterval_Object = MibTableColumn
tokenRingPortSoftErrReportInterval = _TokenRingPortSoftErrReportInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14, 1, 2),
    _TokenRingPortSoftErrReportInterval_Type()
)
tokenRingPortSoftErrReportInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortSoftErrReportInterval.setStatus("current")


class _TokenRingPortSoftErrResetCounters_Type(Integer32):
    """Custom type tokenRingPortSoftErrResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noop", 1),
          ("reset", 2))
    )


_TokenRingPortSoftErrResetCounters_Type.__name__ = "Integer32"
_TokenRingPortSoftErrResetCounters_Object = MibTableColumn
tokenRingPortSoftErrResetCounters = _TokenRingPortSoftErrResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14, 1, 3),
    _TokenRingPortSoftErrResetCounters_Type()
)
tokenRingPortSoftErrResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortSoftErrResetCounters.setStatus("current")
_TokenRingPortSoftErrLastCounterReset_Type = TimeTicks
_TokenRingPortSoftErrLastCounterReset_Object = MibTableColumn
tokenRingPortSoftErrLastCounterReset = _TokenRingPortSoftErrLastCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14, 1, 4),
    _TokenRingPortSoftErrLastCounterReset_Type()
)
tokenRingPortSoftErrLastCounterReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tokenRingPortSoftErrLastCounterReset.setStatus("current")


class _TokenRingPortSoftErrEnable_Type(Integer32):
    """Custom type tokenRingPortSoftErrEnable based on Integer32"""
    defaultValue = 2

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


_TokenRingPortSoftErrEnable_Type.__name__ = "Integer32"
_TokenRingPortSoftErrEnable_Object = MibTableColumn
tokenRingPortSoftErrEnable = _TokenRingPortSoftErrEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 11, 14, 1, 5),
    _TokenRingPortSoftErrEnable_Type()
)
tokenRingPortSoftErrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tokenRingPortSoftErrEnable.setStatus("current")
_MulticastGrp_ObjectIdentity = ObjectIdentity
multicastGrp = _MulticastGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12)
)
_McastRouterTable_Object = MibTable
mcastRouterTable = _McastRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 1)
)
if mibBuilder.loadTexts:
    mcastRouterTable.setStatus("current")
_McastRouterEntry_Object = MibTableRow
mcastRouterEntry = _McastRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 1, 1)
)
mcastRouterEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "mcastRouterModuleIndex"),
    (0, "CISCO-STACK-MIB", "mcastRouterPortIndex"),
)
if mibBuilder.loadTexts:
    mcastRouterEntry.setStatus("current")


class _McastRouterModuleIndex_Type(Integer32):
    """Custom type mcastRouterModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_McastRouterModuleIndex_Type.__name__ = "Integer32"
_McastRouterModuleIndex_Object = MibTableColumn
mcastRouterModuleIndex = _McastRouterModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 1, 1, 1),
    _McastRouterModuleIndex_Type()
)
mcastRouterModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastRouterModuleIndex.setStatus("current")


class _McastRouterPortIndex_Type(Integer32):
    """Custom type mcastRouterPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McastRouterPortIndex_Type.__name__ = "Integer32"
_McastRouterPortIndex_Object = MibTableColumn
mcastRouterPortIndex = _McastRouterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 1, 1, 2),
    _McastRouterPortIndex_Type()
)
mcastRouterPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastRouterPortIndex.setStatus("current")


class _McastRouterAdminStatus_Type(Integer32):
    """Custom type mcastRouterAdminStatus based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 3),
          ("routerPresent", 1))
    )


_McastRouterAdminStatus_Type.__name__ = "Integer32"
_McastRouterAdminStatus_Object = MibTableColumn
mcastRouterAdminStatus = _McastRouterAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 1, 1, 3),
    _McastRouterAdminStatus_Type()
)
mcastRouterAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastRouterAdminStatus.setStatus("current")


class _McastRouterOperStatus_Type(Integer32):
    """Custom type mcastRouterOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRouter", 2),
          ("routerPresent", 1))
    )


_McastRouterOperStatus_Type.__name__ = "Integer32"
_McastRouterOperStatus_Object = MibTableColumn
mcastRouterOperStatus = _McastRouterOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 1, 1, 4),
    _McastRouterOperStatus_Type()
)
mcastRouterOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcastRouterOperStatus.setStatus("current")


class _McastEnableCgmp_Type(Integer32):
    """Custom type mcastEnableCgmp based on Integer32"""
    defaultValue = 2

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


_McastEnableCgmp_Type.__name__ = "Integer32"
_McastEnableCgmp_Object = MibScalar
mcastEnableCgmp = _McastEnableCgmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 2),
    _McastEnableCgmp_Type()
)
mcastEnableCgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastEnableCgmp.setStatus("current")


class _McastEnableIgmp_Type(Integer32):
    """Custom type mcastEnableIgmp based on Integer32"""
    defaultValue = 2

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


_McastEnableIgmp_Type.__name__ = "Integer32"
_McastEnableIgmp_Object = MibScalar
mcastEnableIgmp = _McastEnableIgmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 3),
    _McastEnableIgmp_Type()
)
mcastEnableIgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastEnableIgmp.setStatus("current")


class _McastEnableRgmp_Type(Integer32):
    """Custom type mcastEnableRgmp based on Integer32"""
    defaultValue = 2

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


_McastEnableRgmp_Type.__name__ = "Integer32"
_McastEnableRgmp_Object = MibScalar
mcastEnableRgmp = _McastEnableRgmp_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 12, 4),
    _McastEnableRgmp_Type()
)
mcastEnableRgmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastEnableRgmp.setStatus("current")
_DnsGrp_ObjectIdentity = ObjectIdentity
dnsGrp = _DnsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13)
)


class _DnsEnable_Type(Integer32):
    """Custom type dnsEnable based on Integer32"""
    defaultValue = 2

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


_DnsEnable_Type.__name__ = "Integer32"
_DnsEnable_Object = MibScalar
dnsEnable = _DnsEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13, 1),
    _DnsEnable_Type()
)
dnsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsEnable.setStatus("current")
_DnsServerTable_Object = MibTable
dnsServerTable = _DnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13, 2)
)
if mibBuilder.loadTexts:
    dnsServerTable.setStatus("current")
_DnsServerEntry_Object = MibTableRow
dnsServerEntry = _DnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13, 2, 1)
)
dnsServerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "dnsServerAddr"),
)
if mibBuilder.loadTexts:
    dnsServerEntry.setStatus("current")
_DnsServerAddr_Type = IpAddress
_DnsServerAddr_Object = MibTableColumn
dnsServerAddr = _DnsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13, 2, 1, 1),
    _DnsServerAddr_Type()
)
dnsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsServerAddr.setStatus("current")


class _DnsServerType_Type(Integer32):
    """Custom type dnsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("other", 3),
          ("primary", 2))
    )


_DnsServerType_Type.__name__ = "Integer32"
_DnsServerType_Object = MibTableColumn
dnsServerType = _DnsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13, 2, 1, 2),
    _DnsServerType_Type()
)
dnsServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsServerType.setStatus("current")


class _DnsDomainName_Type(DisplayString):
    """Custom type dnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_DnsDomainName_Type.__name__ = "DisplayString"
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 13, 3),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("current")
_SyslogGrp_ObjectIdentity = ObjectIdentity
syslogGrp = _SyslogGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14)
)
_SyslogServerTable_Object = MibTable
syslogServerTable = _SyslogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 1)
)
if mibBuilder.loadTexts:
    syslogServerTable.setStatus("current")
_SyslogServerEntry_Object = MibTableRow
syslogServerEntry = _SyslogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 1, 1)
)
syslogServerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "syslogServerAddr"),
)
if mibBuilder.loadTexts:
    syslogServerEntry.setStatus("current")
_SyslogServerAddr_Type = IpAddress
_SyslogServerAddr_Object = MibTableColumn
syslogServerAddr = _SyslogServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 1, 1, 1),
    _SyslogServerAddr_Type()
)
syslogServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogServerAddr.setStatus("current")


class _SyslogServerType_Type(Integer32):
    """Custom type syslogServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_SyslogServerType_Type.__name__ = "Integer32"
_SyslogServerType_Object = MibTableColumn
syslogServerType = _SyslogServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 1, 1, 2),
    _SyslogServerType_Type()
)
syslogServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogServerType.setStatus("current")


class _SyslogConsoleEnable_Type(Integer32):
    """Custom type syslogConsoleEnable based on Integer32"""
    defaultValue = 2

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


_SyslogConsoleEnable_Type.__name__ = "Integer32"
_SyslogConsoleEnable_Object = MibScalar
syslogConsoleEnable = _SyslogConsoleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 2),
    _SyslogConsoleEnable_Type()
)
syslogConsoleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogConsoleEnable.setStatus("current")


class _SyslogHostEnable_Type(Integer32):
    """Custom type syslogHostEnable based on Integer32"""
    defaultValue = 2

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


_SyslogHostEnable_Type.__name__ = "Integer32"
_SyslogHostEnable_Object = MibScalar
syslogHostEnable = _SyslogHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 3),
    _SyslogHostEnable_Type()
)
syslogHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogHostEnable.setStatus("current")
_SyslogMessageControlTable_Object = MibTable
syslogMessageControlTable = _SyslogMessageControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 4)
)
if mibBuilder.loadTexts:
    syslogMessageControlTable.setStatus("current")
_SyslogMessageControlEntry_Object = MibTableRow
syslogMessageControlEntry = _SyslogMessageControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 4, 1)
)
syslogMessageControlEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "syslogMessageFacility"),
)
if mibBuilder.loadTexts:
    syslogMessageControlEntry.setStatus("current")


class _SyslogMessageFacility_Type(Integer32):
    """Custom type syslogMessageFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              40,
              42,
              43,
              44,
              45,
              46,
              47)
        )
    )
    namedValues = NamedValues(
        *(("acl", 31),
          ("backup", 43),
          ("callhome", 37),
          ("cdp", 1),
          ("cops", 29),
          ("dhcpsnooping", 38),
          ("diags", 40),
          ("dom", 46),
          ("drip", 20),
          ("dtp", 3),
          ("dvlan", 4),
          ("earl", 5),
          ("eoam", 44),
          ("eou", 42),
          ("ethc", 35),
          ("fddi", 6),
          ("filesys", 19),
          ("gl2pt", 36),
          ("gvrp", 28),
          ("ip", 7),
          ("kernel", 18),
          ("ld", 33),
          ("mcast", 2),
          ("mgmt", 22),
          ("mls", 23),
          ("mvrp", 47),
          ("pagp", 21),
          ("privatevlan", 34),
          ("protfilt", 24),
          ("pruning", 8),
          ("qos", 30),
          ("radius", 26),
          ("rsvp", 32),
          ("security", 25),
          ("snmp", 9),
          ("spantree", 10),
          ("system", 11),
          ("tac", 12),
          ("tcp", 13),
          ("telnet", 14),
          ("tftp", 15),
          ("udld", 27),
          ("vmps", 17),
          ("vtp", 16),
          ("webauth", 45))
    )


_SyslogMessageFacility_Type.__name__ = "Integer32"
_SyslogMessageFacility_Object = MibTableColumn
syslogMessageFacility = _SyslogMessageFacility_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 4, 1, 1),
    _SyslogMessageFacility_Type()
)
syslogMessageFacility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    syslogMessageFacility.setStatus("current")


class _SyslogMessageSeverity_Type(Integer32):
    """Custom type syslogMessageSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("alerts", 2),
          ("critical", 3),
          ("debugging", 8),
          ("emergencies", 1),
          ("errors", 4),
          ("informational", 7),
          ("notification", 6),
          ("warnings", 5))
    )


_SyslogMessageSeverity_Type.__name__ = "Integer32"
_SyslogMessageSeverity_Object = MibTableColumn
syslogMessageSeverity = _SyslogMessageSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 4, 1, 2),
    _SyslogMessageSeverity_Type()
)
syslogMessageSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    syslogMessageSeverity.setStatus("current")


class _SyslogTimeStampOption_Type(Integer32):
    """Custom type syslogTimeStampOption based on Integer32"""
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


_SyslogTimeStampOption_Type.__name__ = "Integer32"
_SyslogTimeStampOption_Object = MibScalar
syslogTimeStampOption = _SyslogTimeStampOption_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 5),
    _SyslogTimeStampOption_Type()
)
syslogTimeStampOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogTimeStampOption.setStatus("current")


class _SyslogTelnetEnable_Type(Integer32):
    """Custom type syslogTelnetEnable based on Integer32"""
    defaultValue = 1

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


_SyslogTelnetEnable_Type.__name__ = "Integer32"
_SyslogTelnetEnable_Object = MibScalar
syslogTelnetEnable = _SyslogTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 14, 6),
    _SyslogTelnetEnable_Type()
)
syslogTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    syslogTelnetEnable.setStatus("current")
_NtpGrp_ObjectIdentity = ObjectIdentity
ntpGrp = _NtpGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15)
)


class _NtpBcastClient_Type(Integer32):
    """Custom type ntpBcastClient based on Integer32"""
    defaultValue = 2

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


_NtpBcastClient_Type.__name__ = "Integer32"
_NtpBcastClient_Object = MibScalar
ntpBcastClient = _NtpBcastClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 1),
    _NtpBcastClient_Type()
)
ntpBcastClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBcastClient.setStatus("current")


class _NtpBcastDelay_Type(Integer32):
    """Custom type ntpBcastDelay based on Integer32"""
    defaultValue = 3000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999999),
    )


_NtpBcastDelay_Type.__name__ = "Integer32"
_NtpBcastDelay_Object = MibScalar
ntpBcastDelay = _NtpBcastDelay_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 2),
    _NtpBcastDelay_Type()
)
ntpBcastDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpBcastDelay.setStatus("current")


class _NtpClient_Type(Integer32):
    """Custom type ntpClient based on Integer32"""
    defaultValue = 2

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


_NtpClient_Type.__name__ = "Integer32"
_NtpClient_Object = MibScalar
ntpClient = _NtpClient_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 3),
    _NtpClient_Type()
)
ntpClient.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpClient.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 4)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 4, 1)
)
ntpServerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "ntpServerAddress"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerAddress_Type = IpAddress
_NtpServerAddress_Object = MibTableColumn
ntpServerAddress = _NtpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 4, 1, 1),
    _NtpServerAddress_Type()
)
ntpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerAddress.setStatus("current")


class _NtpServerType_Type(Integer32):
    """Custom type ntpServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NtpServerType_Type.__name__ = "Integer32"
_NtpServerType_Object = MibTableColumn
ntpServerType = _NtpServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 4, 1, 2),
    _NtpServerType_Type()
)
ntpServerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerType.setStatus("current")
_NtpServerPublicKey_Type = Unsigned32
_NtpServerPublicKey_Object = MibTableColumn
ntpServerPublicKey = _NtpServerPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 4, 1, 3),
    _NtpServerPublicKey_Type()
)
ntpServerPublicKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerPublicKey.setStatus("current")


class _NtpSummertimeStatus_Type(Integer32):
    """Custom type ntpSummertimeStatus based on Integer32"""
    defaultValue = 2

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


_NtpSummertimeStatus_Type.__name__ = "Integer32"
_NtpSummertimeStatus_Object = MibScalar
ntpSummertimeStatus = _NtpSummertimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 5),
    _NtpSummertimeStatus_Type()
)
ntpSummertimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSummertimeStatus.setStatus("current")


class _NtpSummerTimezoneName_Type(DisplayString):
    """Custom type ntpSummerTimezoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpSummerTimezoneName_Type.__name__ = "DisplayString"
_NtpSummerTimezoneName_Object = MibScalar
ntpSummerTimezoneName = _NtpSummerTimezoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 6),
    _NtpSummerTimezoneName_Type()
)
ntpSummerTimezoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpSummerTimezoneName.setStatus("current")


class _NtpTimezoneName_Type(DisplayString):
    """Custom type ntpTimezoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_NtpTimezoneName_Type.__name__ = "DisplayString"
_NtpTimezoneName_Object = MibScalar
ntpTimezoneName = _NtpTimezoneName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 7),
    _NtpTimezoneName_Type()
)
ntpTimezoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimezoneName.setStatus("current")


class _NtpTimezoneOffsetHour_Type(Integer32):
    """Custom type ntpTimezoneOffsetHour based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-12, 12),
    )


_NtpTimezoneOffsetHour_Type.__name__ = "Integer32"
_NtpTimezoneOffsetHour_Object = MibScalar
ntpTimezoneOffsetHour = _NtpTimezoneOffsetHour_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 8),
    _NtpTimezoneOffsetHour_Type()
)
ntpTimezoneOffsetHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimezoneOffsetHour.setStatus("current")


class _NtpTimezoneOffsetMinute_Type(Integer32):
    """Custom type ntpTimezoneOffsetMinute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_NtpTimezoneOffsetMinute_Type.__name__ = "Integer32"
_NtpTimezoneOffsetMinute_Object = MibScalar
ntpTimezoneOffsetMinute = _NtpTimezoneOffsetMinute_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 9),
    _NtpTimezoneOffsetMinute_Type()
)
ntpTimezoneOffsetMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpTimezoneOffsetMinute.setStatus("current")


class _NtpAuthenticationEnable_Type(Integer32):
    """Custom type ntpAuthenticationEnable based on Integer32"""
    defaultValue = 2

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


_NtpAuthenticationEnable_Type.__name__ = "Integer32"
_NtpAuthenticationEnable_Object = MibScalar
ntpAuthenticationEnable = _NtpAuthenticationEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 10),
    _NtpAuthenticationEnable_Type()
)
ntpAuthenticationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticationEnable.setStatus("current")
_NtpAuthenticationTable_Object = MibTable
ntpAuthenticationTable = _NtpAuthenticationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 11)
)
if mibBuilder.loadTexts:
    ntpAuthenticationTable.setStatus("current")
_NtpAuthenticationEntry_Object = MibTableRow
ntpAuthenticationEntry = _NtpAuthenticationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 11, 1)
)
ntpAuthenticationEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "ntpAuthenticationPublicKey"),
)
if mibBuilder.loadTexts:
    ntpAuthenticationEntry.setStatus("current")
_NtpAuthenticationPublicKey_Type = Unsigned32
_NtpAuthenticationPublicKey_Object = MibTableColumn
ntpAuthenticationPublicKey = _NtpAuthenticationPublicKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 11, 1, 1),
    _NtpAuthenticationPublicKey_Type()
)
ntpAuthenticationPublicKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpAuthenticationPublicKey.setStatus("current")


class _NtpAuthenticationSecretKey_Type(DisplayString):
    """Custom type ntpAuthenticationSecretKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAuthenticationSecretKey_Type.__name__ = "DisplayString"
_NtpAuthenticationSecretKey_Object = MibTableColumn
ntpAuthenticationSecretKey = _NtpAuthenticationSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 11, 1, 2),
    _NtpAuthenticationSecretKey_Type()
)
ntpAuthenticationSecretKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticationSecretKey.setStatus("current")


class _NtpAuthenticationTrustedMode_Type(Integer32):
    """Custom type ntpAuthenticationTrustedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_NtpAuthenticationTrustedMode_Type.__name__ = "Integer32"
_NtpAuthenticationTrustedMode_Object = MibTableColumn
ntpAuthenticationTrustedMode = _NtpAuthenticationTrustedMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 11, 1, 3),
    _NtpAuthenticationTrustedMode_Type()
)
ntpAuthenticationTrustedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticationTrustedMode.setStatus("current")


class _NtpAuthenticationType_Type(Integer32):
    """Custom type ntpAuthenticationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_NtpAuthenticationType_Type.__name__ = "Integer32"
_NtpAuthenticationType_Object = MibTableColumn
ntpAuthenticationType = _NtpAuthenticationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 15, 11, 1, 4),
    _NtpAuthenticationType_Type()
)
ntpAuthenticationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticationType.setStatus("current")
_TacacsGrp_ObjectIdentity = ObjectIdentity
tacacsGrp = _TacacsGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16)
)


class _TacacsLoginAuthentication_Type(Integer32):
    """Custom type tacacsLoginAuthentication based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForConsoleOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_TacacsLoginAuthentication_Type.__name__ = "Integer32"
_TacacsLoginAuthentication_Object = MibScalar
tacacsLoginAuthentication = _TacacsLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 1),
    _TacacsLoginAuthentication_Type()
)
tacacsLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLoginAuthentication.setStatus("deprecated")


class _TacacsEnableAuthentication_Type(Integer32):
    """Custom type tacacsEnableAuthentication based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForConsoleOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_TacacsEnableAuthentication_Type.__name__ = "Integer32"
_TacacsEnableAuthentication_Object = MibScalar
tacacsEnableAuthentication = _TacacsEnableAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 2),
    _TacacsEnableAuthentication_Type()
)
tacacsEnableAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsEnableAuthentication.setStatus("deprecated")


class _TacacsLocalLoginAuthentication_Type(Integer32):
    """Custom type tacacsLocalLoginAuthentication based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForConsoleOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_TacacsLocalLoginAuthentication_Type.__name__ = "Integer32"
_TacacsLocalLoginAuthentication_Object = MibScalar
tacacsLocalLoginAuthentication = _TacacsLocalLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 3),
    _TacacsLocalLoginAuthentication_Type()
)
tacacsLocalLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLocalLoginAuthentication.setStatus("deprecated")


class _TacacsLocalEnableAuthentication_Type(Integer32):
    """Custom type tacacsLocalEnableAuthentication based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForConsoleOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_TacacsLocalEnableAuthentication_Type.__name__ = "Integer32"
_TacacsLocalEnableAuthentication_Object = MibScalar
tacacsLocalEnableAuthentication = _TacacsLocalEnableAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 4),
    _TacacsLocalEnableAuthentication_Type()
)
tacacsLocalEnableAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsLocalEnableAuthentication.setStatus("deprecated")


class _TacacsNumLoginAttempts_Type(Integer32):
    """Custom type tacacsNumLoginAttempts based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TacacsNumLoginAttempts_Type.__name__ = "Integer32"
_TacacsNumLoginAttempts_Object = MibScalar
tacacsNumLoginAttempts = _TacacsNumLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 5),
    _TacacsNumLoginAttempts_Type()
)
tacacsNumLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsNumLoginAttempts.setStatus("deprecated")


class _TacacsDirectedRequest_Type(Integer32):
    """Custom type tacacsDirectedRequest based on Integer32"""
    defaultValue = 2

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


_TacacsDirectedRequest_Type.__name__ = "Integer32"
_TacacsDirectedRequest_Object = MibScalar
tacacsDirectedRequest = _TacacsDirectedRequest_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 6),
    _TacacsDirectedRequest_Type()
)
tacacsDirectedRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsDirectedRequest.setStatus("current")


class _TacacsTimeout_Type(Integer32):
    """Custom type tacacsTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TacacsTimeout_Type.__name__ = "Integer32"
_TacacsTimeout_Object = MibScalar
tacacsTimeout = _TacacsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 7),
    _TacacsTimeout_Type()
)
tacacsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsTimeout.setStatus("deprecated")


class _TacacsAuthKey_Type(DisplayString):
    """Custom type tacacsAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_TacacsAuthKey_Type.__name__ = "DisplayString"
_TacacsAuthKey_Object = MibScalar
tacacsAuthKey = _TacacsAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 8),
    _TacacsAuthKey_Type()
)
tacacsAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsAuthKey.setStatus("current")
_TacacsServerTable_Object = MibTable
tacacsServerTable = _TacacsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 9)
)
if mibBuilder.loadTexts:
    tacacsServerTable.setStatus("current")
_TacacsServerEntry_Object = MibTableRow
tacacsServerEntry = _TacacsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 9, 1)
)
tacacsServerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "tacacsServerAddr"),
)
if mibBuilder.loadTexts:
    tacacsServerEntry.setStatus("current")
_TacacsServerAddr_Type = IpAddress
_TacacsServerAddr_Object = MibTableColumn
tacacsServerAddr = _TacacsServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 9, 1, 1),
    _TacacsServerAddr_Type()
)
tacacsServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacacsServerAddr.setStatus("current")


class _TacacsServerType_Type(Integer32):
    """Custom type tacacsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("other", 3),
          ("primary", 2))
    )


_TacacsServerType_Type.__name__ = "Integer32"
_TacacsServerType_Object = MibTableColumn
tacacsServerType = _TacacsServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 16, 9, 1, 2),
    _TacacsServerType_Type()
)
tacacsServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsServerType.setStatus("current")
_IpPermitListGrp_ObjectIdentity = ObjectIdentity
ipPermitListGrp = _IpPermitListGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17)
)


class _IpPermitEnable_Type(Integer32):
    """Custom type ipPermitEnable based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForSnmpOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_IpPermitEnable_Type.__name__ = "Integer32"
_IpPermitEnable_Object = MibScalar
ipPermitEnable = _IpPermitEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 1),
    _IpPermitEnable_Type()
)
ipPermitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPermitEnable.setStatus("deprecated")
_IpPermitListTable_Object = MibTable
ipPermitListTable = _IpPermitListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2)
)
if mibBuilder.loadTexts:
    ipPermitListTable.setStatus("current")
_IpPermitListEntry_Object = MibTableRow
ipPermitListEntry = _IpPermitListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1)
)
ipPermitListEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "ipPermitAddress"),
    (0, "CISCO-STACK-MIB", "ipPermitMask"),
)
if mibBuilder.loadTexts:
    ipPermitListEntry.setStatus("current")
_IpPermitAddress_Type = IpAddress
_IpPermitAddress_Object = MibTableColumn
ipPermitAddress = _IpPermitAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1, 1),
    _IpPermitAddress_Type()
)
ipPermitAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPermitAddress.setStatus("current")
_IpPermitMask_Type = IpAddress
_IpPermitMask_Object = MibTableColumn
ipPermitMask = _IpPermitMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1, 2),
    _IpPermitMask_Type()
)
ipPermitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPermitMask.setStatus("current")


class _IpPermitType_Type(Integer32):
    """Custom type ipPermitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_IpPermitType_Type.__name__ = "Integer32"
_IpPermitType_Object = MibTableColumn
ipPermitType = _IpPermitType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1, 3),
    _IpPermitType_Type()
)
ipPermitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipPermitType.setStatus("current")


class _IpPermitAccessType_Type(Bits):
    """Custom type ipPermitAccessType based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("http", 3),
          ("snmp", 1),
          ("ssh", 2),
          ("telnet", 0))
    )

_IpPermitAccessType_Type.__name__ = "Bits"
_IpPermitAccessType_Object = MibTableColumn
ipPermitAccessType = _IpPermitAccessType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1, 4),
    _IpPermitAccessType_Type()
)
ipPermitAccessType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipPermitAccessType.setStatus("current")


class _IpPermitTelnetConnectLimit_Type(Unsigned32):
    """Custom type ipPermitTelnetConnectLimit based on Unsigned32"""
    defaultValue = 0


_IpPermitTelnetConnectLimit_Object = MibTableColumn
ipPermitTelnetConnectLimit = _IpPermitTelnetConnectLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1, 5),
    _IpPermitTelnetConnectLimit_Type()
)
ipPermitTelnetConnectLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipPermitTelnetConnectLimit.setStatus("current")


class _IpPermitSshConnectLimit_Type(Unsigned32):
    """Custom type ipPermitSshConnectLimit based on Unsigned32"""
    defaultValue = 0


_IpPermitSshConnectLimit_Object = MibTableColumn
ipPermitSshConnectLimit = _IpPermitSshConnectLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 2, 1, 6),
    _IpPermitSshConnectLimit_Type()
)
ipPermitSshConnectLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipPermitSshConnectLimit.setStatus("current")
_IpPermitDeniedListTable_Object = MibTable
ipPermitDeniedListTable = _IpPermitDeniedListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 3)
)
if mibBuilder.loadTexts:
    ipPermitDeniedListTable.setStatus("current")
_IpPermitDeniedListEntry_Object = MibTableRow
ipPermitDeniedListEntry = _IpPermitDeniedListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 3, 1)
)
ipPermitDeniedListEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "ipPermitDeniedAddress"),
)
if mibBuilder.loadTexts:
    ipPermitDeniedListEntry.setStatus("current")
_IpPermitDeniedAddress_Type = IpAddress
_IpPermitDeniedAddress_Object = MibTableColumn
ipPermitDeniedAddress = _IpPermitDeniedAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 3, 1, 1),
    _IpPermitDeniedAddress_Type()
)
ipPermitDeniedAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPermitDeniedAddress.setStatus("current")


class _IpPermitDeniedAccess_Type(Integer32):
    """Custom type ipPermitDeniedAccess based on Integer32"""
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
        *(("http", 4),
          ("snmp", 2),
          ("ssh", 3),
          ("telnet", 1))
    )


_IpPermitDeniedAccess_Type.__name__ = "Integer32"
_IpPermitDeniedAccess_Object = MibTableColumn
ipPermitDeniedAccess = _IpPermitDeniedAccess_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 3, 1, 2),
    _IpPermitDeniedAccess_Type()
)
ipPermitDeniedAccess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPermitDeniedAccess.setStatus("current")
_IpPermitDeniedTime_Type = TimeTicks
_IpPermitDeniedTime_Object = MibTableColumn
ipPermitDeniedTime = _IpPermitDeniedTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 3, 1, 3),
    _IpPermitDeniedTime_Type()
)
ipPermitDeniedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipPermitDeniedTime.setStatus("current")


class _IpPermitAccessTypeEnable_Type(Bits):
    """Custom type ipPermitAccessTypeEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("http", 3),
          ("snmp", 1),
          ("ssh", 2),
          ("telnet", 0))
    )

_IpPermitAccessTypeEnable_Type.__name__ = "Bits"
_IpPermitAccessTypeEnable_Object = MibScalar
ipPermitAccessTypeEnable = _IpPermitAccessTypeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 17, 4),
    _IpPermitAccessTypeEnable_Type()
)
ipPermitAccessTypeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipPermitAccessTypeEnable.setStatus("current")
_PortChannelGrp_ObjectIdentity = ObjectIdentity
portChannelGrp = _PortChannelGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18)
)
_PortChannelTable_Object = MibTable
portChannelTable = _PortChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1)
)
if mibBuilder.loadTexts:
    portChannelTable.setStatus("deprecated")
_PortChannelEntry_Object = MibTableRow
portChannelEntry = _PortChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1)
)
portChannelEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portChannelModuleIndex"),
    (0, "CISCO-STACK-MIB", "portChannelPortIndex"),
)
if mibBuilder.loadTexts:
    portChannelEntry.setStatus("deprecated")


class _PortChannelModuleIndex_Type(Integer32):
    """Custom type portChannelModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortChannelModuleIndex_Type.__name__ = "Integer32"
_PortChannelModuleIndex_Object = MibTableColumn
portChannelModuleIndex = _PortChannelModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 1),
    _PortChannelModuleIndex_Type()
)
portChannelModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelModuleIndex.setStatus("deprecated")


class _PortChannelPortIndex_Type(Integer32):
    """Custom type portChannelPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortChannelPortIndex_Type.__name__ = "Integer32"
_PortChannelPortIndex_Object = MibTableColumn
portChannelPortIndex = _PortChannelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 2),
    _PortChannelPortIndex_Type()
)
portChannelPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelPortIndex.setStatus("deprecated")


class _PortChannelPorts_Type(OctetString):
    """Custom type portChannelPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortChannelPorts_Type.__name__ = "OctetString"
_PortChannelPorts_Object = MibTableColumn
portChannelPorts = _PortChannelPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 3),
    _PortChannelPorts_Type()
)
portChannelPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelPorts.setStatus("deprecated")


class _PortChannelAdminStatus_Type(Integer32):
    """Custom type portChannelAdminStatus based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("autoSilent", 6),
          ("desirable", 3),
          ("desirableSilent", 5),
          ("off", 2),
          ("on", 1))
    )


_PortChannelAdminStatus_Type.__name__ = "Integer32"
_PortChannelAdminStatus_Object = MibTableColumn
portChannelAdminStatus = _PortChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 4),
    _PortChannelAdminStatus_Type()
)
portChannelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portChannelAdminStatus.setStatus("deprecated")


class _PortChannelOperStatus_Type(Integer32):
    """Custom type portChannelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("channelling", 1),
          ("notChannelling", 2))
    )


_PortChannelOperStatus_Type.__name__ = "Integer32"
_PortChannelOperStatus_Object = MibTableColumn
portChannelOperStatus = _PortChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 5),
    _PortChannelOperStatus_Type()
)
portChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelOperStatus.setStatus("deprecated")


class _PortChannelNeighbourDeviceId_Type(OctetString):
    """Custom type portChannelNeighbourDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_PortChannelNeighbourDeviceId_Type.__name__ = "OctetString"
_PortChannelNeighbourDeviceId_Object = MibTableColumn
portChannelNeighbourDeviceId = _PortChannelNeighbourDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 6),
    _PortChannelNeighbourDeviceId_Type()
)
portChannelNeighbourDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelNeighbourDeviceId.setStatus("deprecated")


class _PortChannelNeighbourPortId_Type(Integer32):
    """Custom type portChannelNeighbourPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortChannelNeighbourPortId_Type.__name__ = "Integer32"
_PortChannelNeighbourPortId_Object = MibTableColumn
portChannelNeighbourPortId = _PortChannelNeighbourPortId_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 7),
    _PortChannelNeighbourPortId_Type()
)
portChannelNeighbourPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelNeighbourPortId.setStatus("deprecated")
_PortChannelProtInPackets_Type = Counter32
_PortChannelProtInPackets_Object = MibTableColumn
portChannelProtInPackets = _PortChannelProtInPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 8),
    _PortChannelProtInPackets_Type()
)
portChannelProtInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelProtInPackets.setStatus("deprecated")
_PortChannelProtOutPackets_Type = Counter32
_PortChannelProtOutPackets_Object = MibTableColumn
portChannelProtOutPackets = _PortChannelProtOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 9),
    _PortChannelProtOutPackets_Type()
)
portChannelProtOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelProtOutPackets.setStatus("deprecated")


class _PortChannelIfIndex_Type(Integer32):
    """Custom type portChannelIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortChannelIfIndex_Type.__name__ = "Integer32"
_PortChannelIfIndex_Object = MibTableColumn
portChannelIfIndex = _PortChannelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 18, 1, 1, 10),
    _PortChannelIfIndex_Type()
)
portChannelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portChannelIfIndex.setStatus("deprecated")
_PortCpbGrp_ObjectIdentity = ObjectIdentity
portCpbGrp = _PortCpbGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19)
)
_PortCpbTable_Object = MibTable
portCpbTable = _PortCpbTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1)
)
if mibBuilder.loadTexts:
    portCpbTable.setStatus("current")
_PortCpbEntry_Object = MibTableRow
portCpbEntry = _PortCpbEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1)
)
portCpbEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portCpbModuleIndex"),
    (0, "CISCO-STACK-MIB", "portCpbPortIndex"),
)
if mibBuilder.loadTexts:
    portCpbEntry.setStatus("current")


class _PortCpbModuleIndex_Type(Integer32):
    """Custom type portCpbModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortCpbModuleIndex_Type.__name__ = "Integer32"
_PortCpbModuleIndex_Object = MibTableColumn
portCpbModuleIndex = _PortCpbModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 1),
    _PortCpbModuleIndex_Type()
)
portCpbModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbModuleIndex.setStatus("current")


class _PortCpbPortIndex_Type(Integer32):
    """Custom type portCpbPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortCpbPortIndex_Type.__name__ = "Integer32"
_PortCpbPortIndex_Object = MibTableColumn
portCpbPortIndex = _PortCpbPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 2),
    _PortCpbPortIndex_Type()
)
portCpbPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbPortIndex.setStatus("current")


class _PortCpbSpeed_Type(Bits):
    """Custom type portCpbSpeed based on Bits"""
    namedValues = NamedValues(
        *(("auto", 0),
          ("kps64", 13),
          ("mbps10", 2),
          ("mbps100", 5),
          ("mbps1000", 9),
          ("mbps10000", 14),
          ("mbps155", 6),
          ("mbps16", 3),
          ("mbps1dot544", 10),
          ("mbps2", 11),
          ("mbps2dot048", 12),
          ("mbps4", 1),
          ("mbps400", 7),
          ("mbps45", 4),
          ("mbps622", 8))
    )

_PortCpbSpeed_Type.__name__ = "Bits"
_PortCpbSpeed_Object = MibTableColumn
portCpbSpeed = _PortCpbSpeed_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 3),
    _PortCpbSpeed_Type()
)
portCpbSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbSpeed.setStatus("current")


class _PortCpbDuplex_Type(Bits):
    """Custom type portCpbDuplex based on Bits"""
    namedValues = NamedValues(
        *(("auto", 2),
          ("fdx", 4),
          ("full", 1),
          ("half", 0),
          ("hdx", 3))
    )

_PortCpbDuplex_Type.__name__ = "Bits"
_PortCpbDuplex_Object = MibTableColumn
portCpbDuplex = _PortCpbDuplex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 4),
    _PortCpbDuplex_Type()
)
portCpbDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbDuplex.setStatus("current")


class _PortCpbTrunkEncapsulationType_Type(Bits):
    """Custom type portCpbTrunkEncapsulationType based on Bits"""
    namedValues = NamedValues(
        *(("dot10", 1),
          ("dot1Q", 2),
          ("isl", 3),
          ("lane", 0),
          ("negotiate", 4))
    )

_PortCpbTrunkEncapsulationType_Type.__name__ = "Bits"
_PortCpbTrunkEncapsulationType_Object = MibTableColumn
portCpbTrunkEncapsulationType = _PortCpbTrunkEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 5),
    _PortCpbTrunkEncapsulationType_Type()
)
portCpbTrunkEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbTrunkEncapsulationType.setStatus("current")


class _PortCpbTrunkMode_Type(Bits):
    """Custom type portCpbTrunkMode based on Bits"""
    namedValues = NamedValues(
        *(("auto", 3),
          ("desirable", 2),
          ("off", 1),
          ("on", 0),
          ("onNoNegotiate", 4))
    )

_PortCpbTrunkMode_Type.__name__ = "Bits"
_PortCpbTrunkMode_Object = MibTableColumn
portCpbTrunkMode = _PortCpbTrunkMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 6),
    _PortCpbTrunkMode_Type()
)
portCpbTrunkMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbTrunkMode.setStatus("current")


class _PortCpbChannel_Type(DisplayString):
    """Custom type portCpbChannel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PortCpbChannel_Type.__name__ = "DisplayString"
_PortCpbChannel_Object = MibTableColumn
portCpbChannel = _PortCpbChannel_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 7),
    _PortCpbChannel_Type()
)
portCpbChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbChannel.setStatus("current")


class _PortCpbBroadcastSuppression_Type(Bits):
    """Custom type portCpbBroadcastSuppression based on Bits"""
    namedValues = NamedValues(
        *(("percentage", 1),
          ("pps", 0))
    )

_PortCpbBroadcastSuppression_Type.__name__ = "Bits"
_PortCpbBroadcastSuppression_Object = MibTableColumn
portCpbBroadcastSuppression = _PortCpbBroadcastSuppression_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 8),
    _PortCpbBroadcastSuppression_Type()
)
portCpbBroadcastSuppression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbBroadcastSuppression.setStatus("current")


class _PortCpbFlowControl_Type(Bits):
    """Custom type portCpbFlowControl based on Bits"""
    namedValues = NamedValues(
        *(("receiveDesired", 2),
          ("receiveOff", 0),
          ("receiveOn", 1),
          ("sendDesired", 5),
          ("sendOff", 3),
          ("sendOn", 4))
    )

_PortCpbFlowControl_Type.__name__ = "Bits"
_PortCpbFlowControl_Object = MibTableColumn
portCpbFlowControl = _PortCpbFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 9),
    _PortCpbFlowControl_Type()
)
portCpbFlowControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbFlowControl.setStatus("current")


class _PortCpbSecurity_Type(Integer32):
    """Custom type portCpbSecurity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PortCpbSecurity_Type.__name__ = "Integer32"
_PortCpbSecurity_Object = MibTableColumn
portCpbSecurity = _PortCpbSecurity_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 10),
    _PortCpbSecurity_Type()
)
portCpbSecurity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbSecurity.setStatus("current")


class _PortCpbVlanMembership_Type(Bits):
    """Custom type portCpbVlanMembership based on Bits"""
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 0))
    )

_PortCpbVlanMembership_Type.__name__ = "Bits"
_PortCpbVlanMembership_Object = MibTableColumn
portCpbVlanMembership = _PortCpbVlanMembership_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 11),
    _PortCpbVlanMembership_Type()
)
portCpbVlanMembership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbVlanMembership.setStatus("current")


class _PortCpbPortfast_Type(Integer32):
    """Custom type portCpbPortfast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PortCpbPortfast_Type.__name__ = "Integer32"
_PortCpbPortfast_Object = MibTableColumn
portCpbPortfast = _PortCpbPortfast_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 12),
    _PortCpbPortfast_Type()
)
portCpbPortfast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbPortfast.setStatus("current")


class _PortCpbUdld_Type(Integer32):
    """Custom type portCpbUdld based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PortCpbUdld_Type.__name__ = "Integer32"
_PortCpbUdld_Object = MibTableColumn
portCpbUdld = _PortCpbUdld_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 13),
    _PortCpbUdld_Type()
)
portCpbUdld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbUdld.setStatus("current")


class _PortCpbInlinePower_Type(Bits):
    """Custom type portCpbInlinePower based on Bits"""
    namedValues = NamedValues(
        *(("auto", 0),
          ("off", 2),
          ("on", 1),
          ("static", 3))
    )

_PortCpbInlinePower_Type.__name__ = "Bits"
_PortCpbInlinePower_Object = MibTableColumn
portCpbInlinePower = _PortCpbInlinePower_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 14),
    _PortCpbInlinePower_Type()
)
portCpbInlinePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbInlinePower.setStatus("current")


class _PortCpbAuxiliaryVlan_Type(Bits):
    """Custom type portCpbAuxiliaryVlan based on Bits"""
    namedValues = NamedValues(
        *(("dot1p", 2),
          ("none", 3),
          ("untagged", 1),
          ("vlanNo", 0))
    )

_PortCpbAuxiliaryVlan_Type.__name__ = "Bits"
_PortCpbAuxiliaryVlan_Object = MibTableColumn
portCpbAuxiliaryVlan = _PortCpbAuxiliaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 15),
    _PortCpbAuxiliaryVlan_Type()
)
portCpbAuxiliaryVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbAuxiliaryVlan.setStatus("current")


class _PortCpbSpan_Type(Bits):
    """Custom type portCpbSpan based on Bits"""
    namedValues = NamedValues(
        *(("destination", 1),
          ("reflector", 2),
          ("source", 0))
    )

_PortCpbSpan_Type.__name__ = "Bits"
_PortCpbSpan_Object = MibTableColumn
portCpbSpan = _PortCpbSpan_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 16),
    _PortCpbSpan_Type()
)
portCpbSpan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbSpan.setStatus("current")


class _PortCpbCosRewrite_Type(Integer32):
    """Custom type portCpbCosRewrite based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PortCpbCosRewrite_Type.__name__ = "Integer32"
_PortCpbCosRewrite_Object = MibTableColumn
portCpbCosRewrite = _PortCpbCosRewrite_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 17),
    _PortCpbCosRewrite_Type()
)
portCpbCosRewrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbCosRewrite.setStatus("current")


class _PortCpbTosRewrite_Type(Bits):
    """Custom type portCpbTosRewrite based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 0),
          ("ipPrecedence", 1))
    )

_PortCpbTosRewrite_Type.__name__ = "Bits"
_PortCpbTosRewrite_Object = MibTableColumn
portCpbTosRewrite = _PortCpbTosRewrite_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 18),
    _PortCpbTosRewrite_Type()
)
portCpbTosRewrite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbTosRewrite.setStatus("current")


class _PortCpbCopsGrouping_Type(OctetString):
    """Custom type portCpbCopsGrouping based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortCpbCopsGrouping_Type.__name__ = "OctetString"
_PortCpbCopsGrouping_Object = MibTableColumn
portCpbCopsGrouping = _PortCpbCopsGrouping_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 19),
    _PortCpbCopsGrouping_Type()
)
portCpbCopsGrouping.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbCopsGrouping.setStatus("current")


class _PortCpbDot1x_Type(Integer32):
    """Custom type portCpbDot1x based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PortCpbDot1x_Type.__name__ = "Integer32"
_PortCpbDot1x_Object = MibTableColumn
portCpbDot1x = _PortCpbDot1x_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 20),
    _PortCpbDot1x_Type()
)
portCpbDot1x.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbDot1x.setStatus("current")


class _PortCpbIgmpFilter_Type(Integer32):
    """Custom type portCpbIgmpFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_PortCpbIgmpFilter_Type.__name__ = "Integer32"
_PortCpbIgmpFilter_Object = MibTableColumn
portCpbIgmpFilter = _PortCpbIgmpFilter_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 19, 1, 1, 21),
    _PortCpbIgmpFilter_Type()
)
portCpbIgmpFilter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portCpbIgmpFilter.setStatus("current")
_PortTopNGrp_ObjectIdentity = ObjectIdentity
portTopNGrp = _PortTopNGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20)
)
_PortTopNControlTable_Object = MibTable
portTopNControlTable = _PortTopNControlTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1)
)
if mibBuilder.loadTexts:
    portTopNControlTable.setStatus("current")
_PortTopNControlEntry_Object = MibTableRow
portTopNControlEntry = _PortTopNControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1)
)
portTopNControlEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portTopNControlIndex"),
)
if mibBuilder.loadTexts:
    portTopNControlEntry.setStatus("current")


class _PortTopNControlIndex_Type(Integer32):
    """Custom type portTopNControlIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_PortTopNControlIndex_Type.__name__ = "Integer32"
_PortTopNControlIndex_Object = MibTableColumn
portTopNControlIndex = _PortTopNControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 1),
    _PortTopNControlIndex_Type()
)
portTopNControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNControlIndex.setStatus("current")


class _PortTopNRateBase_Type(Integer32):
    """Custom type portTopNRateBase based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("portTopNBufferOverflow", 7),
          ("portTopNIOBroadcastPkts", 4),
          ("portTopNIOMulticastPkts", 5),
          ("portTopNIOOctets", 2),
          ("portTopNIOPkts", 3),
          ("portTopNInErrors", 6),
          ("portTopNUtilization", 1))
    )


_PortTopNRateBase_Type.__name__ = "Integer32"
_PortTopNRateBase_Object = MibTableColumn
portTopNRateBase = _PortTopNRateBase_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 2),
    _PortTopNRateBase_Type()
)
portTopNRateBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNRateBase.setStatus("current")


class _PortTopNType_Type(Integer32):
    """Custom type portTopNType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("portTopN10GigaEthernet", 8),
          ("portTopNAllEthernetPorts", 7),
          ("portTopNAllPorts", 1),
          ("portTopNEthernet", 2),
          ("portTopNFDDI", 6),
          ("portTopNFastEthernet", 3),
          ("portTopNGigaEthernet", 4),
          ("portTopNTokenRing", 5))
    )


_PortTopNType_Type.__name__ = "Integer32"
_PortTopNType_Object = MibTableColumn
portTopNType = _PortTopNType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 3),
    _PortTopNType_Type()
)
portTopNType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNType.setStatus("current")


class _PortTopNMode_Type(Integer32):
    """Custom type portTopNMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portTopNBackground", 2),
          ("portTopNForeground", 1))
    )


_PortTopNMode_Type.__name__ = "Integer32"
_PortTopNMode_Object = MibTableColumn
portTopNMode = _PortTopNMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 4),
    _PortTopNMode_Type()
)
portTopNMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNMode.setStatus("current")


class _PortTopNReportStatus_Type(Integer32):
    """Custom type portTopNReportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("progressing", 1),
          ("ready", 2))
    )


_PortTopNReportStatus_Type.__name__ = "Integer32"
_PortTopNReportStatus_Object = MibTableColumn
portTopNReportStatus = _PortTopNReportStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 5),
    _PortTopNReportStatus_Type()
)
portTopNReportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNReportStatus.setStatus("current")


class _PortTopNDuration_Type(Integer32):
    """Custom type portTopNDuration based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 999),
    )


_PortTopNDuration_Type.__name__ = "Integer32"
_PortTopNDuration_Object = MibTableColumn
portTopNDuration = _PortTopNDuration_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 6),
    _PortTopNDuration_Type()
)
portTopNDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNDuration.setStatus("current")


class _PortTopNTimeRemaining_Type(Integer32):
    """Custom type portTopNTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortTopNTimeRemaining_Type.__name__ = "Integer32"
_PortTopNTimeRemaining_Object = MibTableColumn
portTopNTimeRemaining = _PortTopNTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 7),
    _PortTopNTimeRemaining_Type()
)
portTopNTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNTimeRemaining.setStatus("current")
_PortTopNStartTime_Type = TimeTicks
_PortTopNStartTime_Object = MibTableColumn
portTopNStartTime = _PortTopNStartTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 8),
    _PortTopNStartTime_Type()
)
portTopNStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNStartTime.setStatus("current")


class _PortTopNRequestedSize_Type(Integer32):
    """Custom type portTopNRequestedSize based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortTopNRequestedSize_Type.__name__ = "Integer32"
_PortTopNRequestedSize_Object = MibTableColumn
portTopNRequestedSize = _PortTopNRequestedSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 9),
    _PortTopNRequestedSize_Type()
)
portTopNRequestedSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNRequestedSize.setStatus("current")


class _PortTopNGrantedSize_Type(Integer32):
    """Custom type portTopNGrantedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortTopNGrantedSize_Type.__name__ = "Integer32"
_PortTopNGrantedSize_Object = MibTableColumn
portTopNGrantedSize = _PortTopNGrantedSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 10),
    _PortTopNGrantedSize_Type()
)
portTopNGrantedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNGrantedSize.setStatus("current")
_PortTopNOwner_Type = OwnerString
_PortTopNOwner_Object = MibTableColumn
portTopNOwner = _PortTopNOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 11),
    _PortTopNOwner_Type()
)
portTopNOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNOwner.setStatus("current")
_PortTopNStatus_Type = RowStatus
_PortTopNStatus_Object = MibTableColumn
portTopNStatus = _PortTopNStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 1, 1, 12),
    _PortTopNStatus_Type()
)
portTopNStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    portTopNStatus.setStatus("current")
_PortTopNTable_Object = MibTable
portTopNTable = _PortTopNTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2)
)
if mibBuilder.loadTexts:
    portTopNTable.setStatus("current")
_PortTopNEntry_Object = MibTableRow
portTopNEntry = _PortTopNEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1)
)
portTopNEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portTopNControlIndex"),
    (0, "CISCO-STACK-MIB", "portTopNIndex"),
)
if mibBuilder.loadTexts:
    portTopNEntry.setStatus("current")


class _PortTopNIndex_Type(Integer32):
    """Custom type portTopNIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortTopNIndex_Type.__name__ = "Integer32"
_PortTopNIndex_Object = MibTableColumn
portTopNIndex = _PortTopNIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 1),
    _PortTopNIndex_Type()
)
portTopNIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNIndex.setStatus("current")


class _PortTopNModuleNumber_Type(Integer32):
    """Custom type portTopNModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_PortTopNModuleNumber_Type.__name__ = "Integer32"
_PortTopNModuleNumber_Object = MibTableColumn
portTopNModuleNumber = _PortTopNModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 2),
    _PortTopNModuleNumber_Type()
)
portTopNModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNModuleNumber.setStatus("current")


class _PortTopNPortNumber_Type(Integer32):
    """Custom type portTopNPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortTopNPortNumber_Type.__name__ = "Integer32"
_PortTopNPortNumber_Object = MibTableColumn
portTopNPortNumber = _PortTopNPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 3),
    _PortTopNPortNumber_Type()
)
portTopNPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNPortNumber.setStatus("current")


class _PortTopNUtilization_Type(Integer32):
    """Custom type portTopNUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PortTopNUtilization_Type.__name__ = "Integer32"
_PortTopNUtilization_Object = MibTableColumn
portTopNUtilization = _PortTopNUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 4),
    _PortTopNUtilization_Type()
)
portTopNUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNUtilization.setStatus("current")
_PortTopNIOOctets_Type = Counter64
_PortTopNIOOctets_Object = MibTableColumn
portTopNIOOctets = _PortTopNIOOctets_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 5),
    _PortTopNIOOctets_Type()
)
portTopNIOOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNIOOctets.setStatus("current")
_PortTopNIOPkts_Type = Counter64
_PortTopNIOPkts_Object = MibTableColumn
portTopNIOPkts = _PortTopNIOPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 6),
    _PortTopNIOPkts_Type()
)
portTopNIOPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNIOPkts.setStatus("current")
_PortTopNIOBroadcast_Type = Counter64
_PortTopNIOBroadcast_Object = MibTableColumn
portTopNIOBroadcast = _PortTopNIOBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 7),
    _PortTopNIOBroadcast_Type()
)
portTopNIOBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNIOBroadcast.setStatus("current")
_PortTopNIOMulticast_Type = Counter64
_PortTopNIOMulticast_Object = MibTableColumn
portTopNIOMulticast = _PortTopNIOMulticast_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 8),
    _PortTopNIOMulticast_Type()
)
portTopNIOMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNIOMulticast.setStatus("current")
_PortTopNInErrors_Type = Counter32
_PortTopNInErrors_Object = MibTableColumn
portTopNInErrors = _PortTopNInErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 9),
    _PortTopNInErrors_Type()
)
portTopNInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNInErrors.setStatus("current")
_PortTopNBufferOverFlow_Type = Counter32
_PortTopNBufferOverFlow_Object = MibTableColumn
portTopNBufferOverFlow = _PortTopNBufferOverFlow_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 20, 2, 1, 10),
    _PortTopNBufferOverFlow_Type()
)
portTopNBufferOverFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTopNBufferOverFlow.setStatus("current")
_MdgGrp_ObjectIdentity = ObjectIdentity
mdgGrp = _MdgGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 21)
)
_MdgGatewayTable_Object = MibTable
mdgGatewayTable = _MdgGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 21, 1)
)
if mibBuilder.loadTexts:
    mdgGatewayTable.setStatus("current")
_MdgGatewayEntry_Object = MibTableRow
mdgGatewayEntry = _MdgGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 21, 1, 1)
)
mdgGatewayEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "mdgGatewayAddr"),
)
if mibBuilder.loadTexts:
    mdgGatewayEntry.setStatus("current")
_MdgGatewayAddr_Type = IpAddress
_MdgGatewayAddr_Object = MibTableColumn
mdgGatewayAddr = _MdgGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 21, 1, 1, 1),
    _MdgGatewayAddr_Type()
)
mdgGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mdgGatewayAddr.setStatus("current")


class _MdgGatewayType_Type(Integer32):
    """Custom type mdgGatewayType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("other", 3),
          ("primary", 2))
    )


_MdgGatewayType_Type.__name__ = "Integer32"
_MdgGatewayType_Object = MibTableColumn
mdgGatewayType = _MdgGatewayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 21, 1, 1, 2),
    _MdgGatewayType_Type()
)
mdgGatewayType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mdgGatewayType.setStatus("current")
_RadiusGrp_ObjectIdentity = ObjectIdentity
radiusGrp = _RadiusGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22)
)


class _RadiusLoginAuthentication_Type(Integer32):
    """Custom type radiusLoginAuthentication based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForConsoleOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_RadiusLoginAuthentication_Type.__name__ = "Integer32"
_RadiusLoginAuthentication_Object = MibScalar
radiusLoginAuthentication = _RadiusLoginAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 1),
    _RadiusLoginAuthentication_Type()
)
radiusLoginAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusLoginAuthentication.setStatus("deprecated")


class _RadiusEnableAuthentication_Type(Integer32):
    """Custom type radiusEnableAuthentication based on Integer32"""
    defaultValue = 2

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
        *(("disabled", 2),
          ("enabled", 1),
          ("enabledForConsoleOnly", 4),
          ("enabledForTelnetOnly", 3))
    )


_RadiusEnableAuthentication_Type.__name__ = "Integer32"
_RadiusEnableAuthentication_Object = MibScalar
radiusEnableAuthentication = _RadiusEnableAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 2),
    _RadiusEnableAuthentication_Type()
)
radiusEnableAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusEnableAuthentication.setStatus("deprecated")


class _RadiusDeadtime_Type(Integer32):
    """Custom type radiusDeadtime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_RadiusDeadtime_Type.__name__ = "Integer32"
_RadiusDeadtime_Object = MibScalar
radiusDeadtime = _RadiusDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 3),
    _RadiusDeadtime_Type()
)
radiusDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusDeadtime.setStatus("current")


class _RadiusAuthKey_Type(DisplayString):
    """Custom type radiusAuthKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RadiusAuthKey_Type.__name__ = "DisplayString"
_RadiusAuthKey_Object = MibScalar
radiusAuthKey = _RadiusAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 4),
    _RadiusAuthKey_Type()
)
radiusAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusAuthKey.setStatus("current")


class _RadiusTimeout_Type(Integer32):
    """Custom type radiusTimeout based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RadiusTimeout_Type.__name__ = "Integer32"
_RadiusTimeout_Object = MibScalar
radiusTimeout = _RadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 5),
    _RadiusTimeout_Type()
)
radiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusTimeout.setStatus("current")


class _RadiusRetransmits_Type(Integer32):
    """Custom type radiusRetransmits based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RadiusRetransmits_Type.__name__ = "Integer32"
_RadiusRetransmits_Object = MibScalar
radiusRetransmits = _RadiusRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 6),
    _RadiusRetransmits_Type()
)
radiusRetransmits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusRetransmits.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 7)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("deprecated")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 7, 1)
)
radiusServerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "radiusServerAddr"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("deprecated")
_RadiusServerAddr_Type = IpAddress
_RadiusServerAddr_Object = MibTableColumn
radiusServerAddr = _RadiusServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 7, 1, 1),
    _RadiusServerAddr_Type()
)
radiusServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    radiusServerAddr.setStatus("deprecated")


class _RadiusServerAuthPort_Type(Integer32):
    """Custom type radiusServerAuthPort based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RadiusServerAuthPort_Type.__name__ = "Integer32"
_RadiusServerAuthPort_Object = MibTableColumn
radiusServerAuthPort = _RadiusServerAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 7, 1, 2),
    _RadiusServerAuthPort_Type()
)
radiusServerAuthPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAuthPort.setStatus("deprecated")


class _RadiusServerType_Type(Integer32):
    """Custom type radiusServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("other", 3),
          ("primary", 2))
    )


_RadiusServerType_Type.__name__ = "Integer32"
_RadiusServerType_Object = MibTableColumn
radiusServerType = _RadiusServerType_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 22, 7, 1, 3),
    _RadiusServerType_Type()
)
radiusServerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerType.setStatus("deprecated")
_TraceRouteGrp_ObjectIdentity = ObjectIdentity
traceRouteGrp = _TraceRouteGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24)
)


class _TraceRouteMaxQueries_Type(Integer32):
    """Custom type traceRouteMaxQueries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_TraceRouteMaxQueries_Type.__name__ = "Integer32"
_TraceRouteMaxQueries_Object = MibScalar
traceRouteMaxQueries = _TraceRouteMaxQueries_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 1),
    _TraceRouteMaxQueries_Type()
)
traceRouteMaxQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteMaxQueries.setStatus("current")
_TraceRouteQueryTable_Object = MibTable
traceRouteQueryTable = _TraceRouteQueryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2)
)
if mibBuilder.loadTexts:
    traceRouteQueryTable.setStatus("current")
_TraceRouteQueryEntry_Object = MibTableRow
traceRouteQueryEntry = _TraceRouteQueryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1)
)
traceRouteQueryEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "traceRouteQueryIndex"),
)
if mibBuilder.loadTexts:
    traceRouteQueryEntry.setStatus("current")


class _TraceRouteQueryIndex_Type(Integer32):
    """Custom type traceRouteQueryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteQueryIndex_Type.__name__ = "Integer32"
_TraceRouteQueryIndex_Object = MibTableColumn
traceRouteQueryIndex = _TraceRouteQueryIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 1),
    _TraceRouteQueryIndex_Type()
)
traceRouteQueryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteQueryIndex.setStatus("current")


class _TraceRouteHost_Type(DisplayString):
    """Custom type traceRouteHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TraceRouteHost_Type.__name__ = "DisplayString"
_TraceRouteHost_Object = MibTableColumn
traceRouteHost = _TraceRouteHost_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 2),
    _TraceRouteHost_Type()
)
traceRouteHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteHost.setStatus("current")


class _TraceRouteQueryDNSEnable_Type(Integer32):
    """Custom type traceRouteQueryDNSEnable based on Integer32"""
    defaultValue = 1

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


_TraceRouteQueryDNSEnable_Type.__name__ = "Integer32"
_TraceRouteQueryDNSEnable_Object = MibTableColumn
traceRouteQueryDNSEnable = _TraceRouteQueryDNSEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 3),
    _TraceRouteQueryDNSEnable_Type()
)
traceRouteQueryDNSEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryDNSEnable.setStatus("current")


class _TraceRouteQueryWaitingTime_Type(Integer32):
    """Custom type traceRouteQueryWaitingTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TraceRouteQueryWaitingTime_Type.__name__ = "Integer32"
_TraceRouteQueryWaitingTime_Object = MibTableColumn
traceRouteQueryWaitingTime = _TraceRouteQueryWaitingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 4),
    _TraceRouteQueryWaitingTime_Type()
)
traceRouteQueryWaitingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryWaitingTime.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteQueryWaitingTime.setUnits("seconds")


class _TraceRouteQueryInitTTL_Type(Integer32):
    """Custom type traceRouteQueryInitTTL based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteQueryInitTTL_Type.__name__ = "Integer32"
_TraceRouteQueryInitTTL_Object = MibTableColumn
traceRouteQueryInitTTL = _TraceRouteQueryInitTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 5),
    _TraceRouteQueryInitTTL_Type()
)
traceRouteQueryInitTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryInitTTL.setStatus("current")


class _TraceRouteQueryMaxTTL_Type(Integer32):
    """Custom type traceRouteQueryMaxTTL based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TraceRouteQueryMaxTTL_Type.__name__ = "Integer32"
_TraceRouteQueryMaxTTL_Object = MibTableColumn
traceRouteQueryMaxTTL = _TraceRouteQueryMaxTTL_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 6),
    _TraceRouteQueryMaxTTL_Type()
)
traceRouteQueryMaxTTL.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryMaxTTL.setStatus("current")


class _TraceRouteQueryUDPPort_Type(Integer32):
    """Custom type traceRouteQueryUDPPort based on Integer32"""
    defaultValue = 33434

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteQueryUDPPort_Type.__name__ = "Integer32"
_TraceRouteQueryUDPPort_Object = MibTableColumn
traceRouteQueryUDPPort = _TraceRouteQueryUDPPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 7),
    _TraceRouteQueryUDPPort_Type()
)
traceRouteQueryUDPPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryUDPPort.setStatus("current")


class _TraceRouteQueryPacketCount_Type(Integer32):
    """Custom type traceRouteQueryPacketCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_TraceRouteQueryPacketCount_Type.__name__ = "Integer32"
_TraceRouteQueryPacketCount_Object = MibTableColumn
traceRouteQueryPacketCount = _TraceRouteQueryPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 8),
    _TraceRouteQueryPacketCount_Type()
)
traceRouteQueryPacketCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryPacketCount.setStatus("current")


class _TraceRouteQueryPacketSize_Type(Integer32):
    """Custom type traceRouteQueryPacketSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1420),
    )


_TraceRouteQueryPacketSize_Type.__name__ = "Integer32"
_TraceRouteQueryPacketSize_Object = MibTableColumn
traceRouteQueryPacketSize = _TraceRouteQueryPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 9),
    _TraceRouteQueryPacketSize_Type()
)
traceRouteQueryPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryPacketSize.setStatus("current")


class _TraceRouteQueryTOS_Type(Integer32):
    """Custom type traceRouteQueryTOS based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TraceRouteQueryTOS_Type.__name__ = "Integer32"
_TraceRouteQueryTOS_Object = MibTableColumn
traceRouteQueryTOS = _TraceRouteQueryTOS_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 10),
    _TraceRouteQueryTOS_Type()
)
traceRouteQueryTOS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryTOS.setStatus("current")


class _TraceRouteQueryResult_Type(Integer32):
    """Custom type traceRouteQueryResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_TraceRouteQueryResult_Type.__name__ = "Integer32"
_TraceRouteQueryResult_Object = MibTableColumn
traceRouteQueryResult = _TraceRouteQueryResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 21),
    _TraceRouteQueryResult_Type()
)
traceRouteQueryResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteQueryResult.setStatus("current")
_TraceRouteQueryTime_Type = TimeTicks
_TraceRouteQueryTime_Object = MibTableColumn
traceRouteQueryTime = _TraceRouteQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 22),
    _TraceRouteQueryTime_Type()
)
traceRouteQueryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteQueryTime.setStatus("current")


class _TraceRouteQueryOwner_Type(DisplayString):
    """Custom type traceRouteQueryOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_TraceRouteQueryOwner_Type.__name__ = "DisplayString"
_TraceRouteQueryOwner_Object = MibTableColumn
traceRouteQueryOwner = _TraceRouteQueryOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 23),
    _TraceRouteQueryOwner_Type()
)
traceRouteQueryOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryOwner.setStatus("current")


class _TraceRouteQueryStatus_Type(Integer32):
    """Custom type traceRouteQueryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )


_TraceRouteQueryStatus_Type.__name__ = "Integer32"
_TraceRouteQueryStatus_Object = MibTableColumn
traceRouteQueryStatus = _TraceRouteQueryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 2, 1, 24),
    _TraceRouteQueryStatus_Type()
)
traceRouteQueryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    traceRouteQueryStatus.setStatus("current")
_TraceRouteDataTable_Object = MibTable
traceRouteDataTable = _TraceRouteDataTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3)
)
if mibBuilder.loadTexts:
    traceRouteDataTable.setStatus("current")
_TraceRouteDataEntry_Object = MibTableRow
traceRouteDataEntry = _TraceRouteDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1)
)
traceRouteDataEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "traceRouteQueryIndex"),
    (0, "CISCO-STACK-MIB", "traceRouteDataIndex"),
)
if mibBuilder.loadTexts:
    traceRouteDataEntry.setStatus("current")


class _TraceRouteDataIndex_Type(Integer32):
    """Custom type traceRouteDataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteDataIndex_Type.__name__ = "Integer32"
_TraceRouteDataIndex_Object = MibTableColumn
traceRouteDataIndex = _TraceRouteDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1, 1),
    _TraceRouteDataIndex_Type()
)
traceRouteDataIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteDataIndex.setStatus("current")


class _TraceRouteDataGatewayName_Type(DisplayString):
    """Custom type traceRouteDataGatewayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TraceRouteDataGatewayName_Type.__name__ = "DisplayString"
_TraceRouteDataGatewayName_Object = MibTableColumn
traceRouteDataGatewayName = _TraceRouteDataGatewayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1, 2),
    _TraceRouteDataGatewayName_Type()
)
traceRouteDataGatewayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteDataGatewayName.setStatus("current")
_TraceRouteDataGatewayIp_Type = IpAddress
_TraceRouteDataGatewayIp_Object = MibTableColumn
traceRouteDataGatewayIp = _TraceRouteDataGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1, 3),
    _TraceRouteDataGatewayIp_Type()
)
traceRouteDataGatewayIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteDataGatewayIp.setStatus("current")


class _TraceRouteDataRtt_Type(Integer32):
    """Custom type traceRouteDataRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteDataRtt_Type.__name__ = "Integer32"
_TraceRouteDataRtt_Object = MibTableColumn
traceRouteDataRtt = _TraceRouteDataRtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1, 4),
    _TraceRouteDataRtt_Type()
)
traceRouteDataRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteDataRtt.setStatus("current")
if mibBuilder.loadTexts:
    traceRouteDataRtt.setUnits("milliseconds")


class _TraceRouteDataHopCount_Type(Integer32):
    """Custom type traceRouteDataHopCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TraceRouteDataHopCount_Type.__name__ = "Integer32"
_TraceRouteDataHopCount_Object = MibTableColumn
traceRouteDataHopCount = _TraceRouteDataHopCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1, 5),
    _TraceRouteDataHopCount_Type()
)
traceRouteDataHopCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteDataHopCount.setStatus("current")


class _TraceRouteDataErrors_Type(Integer32):
    """Custom type traceRouteDataErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("icmpTTLExpired", 19),
          ("icmpTimeOut", 18),
          ("icmpUnknown", 17),
          ("icmpUnreachAdmin", 14),
          ("icmpUnreachHost", 2),
          ("icmpUnreachHostIsolated", 9),
          ("icmpUnreachHostPrec", 15),
          ("icmpUnreachHostTos", 13),
          ("icmpUnreachNeedFrag", 5),
          ("icmpUnreachNet", 1),
          ("icmpUnreachNetProhib", 10),
          ("icmpUnreachNetTos", 12),
          ("icmpUnreachNoHost", 8),
          ("icmpUnreachNoNet", 7),
          ("icmpUnreachPort", 4),
          ("icmpUnreachPrecedence", 16),
          ("icmpUnreachProhib", 11),
          ("icmpUnreachProtocol", 3),
          ("icmpUnreachSrcFail", 6))
    )


_TraceRouteDataErrors_Type.__name__ = "Integer32"
_TraceRouteDataErrors_Object = MibTableColumn
traceRouteDataErrors = _TraceRouteDataErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 24, 3, 1, 6),
    _TraceRouteDataErrors_Type()
)
traceRouteDataErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    traceRouteDataErrors.setStatus("current")
_FileCopyGrp_ObjectIdentity = ObjectIdentity
fileCopyGrp = _FileCopyGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25)
)


class _FileCopyProtocol_Type(Integer32):
    """Custom type fileCopyProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rcp", 2),
          ("tftp", 1))
    )


_FileCopyProtocol_Type.__name__ = "Integer32"
_FileCopyProtocol_Object = MibScalar
fileCopyProtocol = _FileCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 1),
    _FileCopyProtocol_Type()
)
fileCopyProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyProtocol.setStatus("current")


class _FileCopyRemoteServer_Type(DisplayString):
    """Custom type fileCopyRemoteServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FileCopyRemoteServer_Type.__name__ = "DisplayString"
_FileCopyRemoteServer_Object = MibScalar
fileCopyRemoteServer = _FileCopyRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 2),
    _FileCopyRemoteServer_Type()
)
fileCopyRemoteServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyRemoteServer.setStatus("current")


class _FileCopySrcFileName_Type(DisplayString):
    """Custom type fileCopySrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FileCopySrcFileName_Type.__name__ = "DisplayString"
_FileCopySrcFileName_Object = MibScalar
fileCopySrcFileName = _FileCopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 3),
    _FileCopySrcFileName_Type()
)
fileCopySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcFileName.setStatus("current")


class _FileCopyDstFileName_Type(DisplayString):
    """Custom type fileCopyDstFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FileCopyDstFileName_Type.__name__ = "DisplayString"
_FileCopyDstFileName_Object = MibScalar
fileCopyDstFileName = _FileCopyDstFileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 4),
    _FileCopyDstFileName_Type()
)
fileCopyDstFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDstFileName.setStatus("current")


class _FileCopyModuleNumber_Type(Integer32):
    """Custom type fileCopyModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_FileCopyModuleNumber_Type.__name__ = "Integer32"
_FileCopyModuleNumber_Object = MibScalar
fileCopyModuleNumber = _FileCopyModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 5),
    _FileCopyModuleNumber_Type()
)
fileCopyModuleNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyModuleNumber.setStatus("current")


class _FileCopyUserName_Type(DisplayString):
    """Custom type fileCopyUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_FileCopyUserName_Type.__name__ = "DisplayString"
_FileCopyUserName_Object = MibScalar
fileCopyUserName = _FileCopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 6),
    _FileCopyUserName_Type()
)
fileCopyUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyUserName.setStatus("current")


class _FileCopyAction_Type(Integer32):
    """Custom type fileCopyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("copyConfigFileFromFlashToHost", 11),
          ("copyConfigFileFromHostToFlash", 10),
          ("copyConfigFromFlashToRuntime", 8),
          ("copyConfigFromHostToRuntime", 2),
          ("copyConfigFromRuntimeToFlash", 9),
          ("copyConfigFromRuntimeToHost", 3),
          ("copyImageFromFlashToHost", 5),
          ("copyImageFromHostToFlash", 4),
          ("copyTechReportFromRuntimeToHost", 12),
          ("other", 1))
    )


_FileCopyAction_Type.__name__ = "Integer32"
_FileCopyAction_Object = MibScalar
fileCopyAction = _FileCopyAction_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 7),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")


class _FileCopyResult_Type(Integer32):
    """Custom type fileCopyResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22)
        )
    )
    namedValues = NamedValues(
        *(("accessViolation", 16),
          ("badChecksum", 7),
          ("badFlash", 9),
          ("badLength", 8),
          ("fileNotFound", 13),
          ("inProgress", 1),
          ("incompatibleImage", 21),
          ("insufficientDramSize", 20),
          ("insufficientSpaceOnStorageDevice", 19),
          ("invalidHost", 14),
          ("invalidModule", 15),
          ("invalidStorageDevice", 18),
          ("noBuffers", 5),
          ("noProcesses", 6),
          ("noResponse", 3),
          ("rcpError", 22),
          ("serverError", 10),
          ("success", 2),
          ("tooManyRetries", 4),
          ("unknownStatus", 17),
          ("userCanceled", 11),
          ("wrongCode", 12))
    )


_FileCopyResult_Type.__name__ = "Integer32"
_FileCopyResult_Object = MibScalar
fileCopyResult = _FileCopyResult_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 8),
    _FileCopyResult_Type()
)
fileCopyResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyResult.setStatus("current")


class _FileCopyResultRcpErrorMessage_Type(DisplayString):
    """Custom type fileCopyResultRcpErrorMessage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileCopyResultRcpErrorMessage_Type.__name__ = "DisplayString"
_FileCopyResultRcpErrorMessage_Object = MibScalar
fileCopyResultRcpErrorMessage = _FileCopyResultRcpErrorMessage_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 9),
    _FileCopyResultRcpErrorMessage_Type()
)
fileCopyResultRcpErrorMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyResultRcpErrorMessage.setStatus("current")


class _FileCopyRuntimeConfigPart_Type(Integer32):
    """Custom type fileCopyRuntimeConfigPart based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("nonDefault", 2))
    )


_FileCopyRuntimeConfigPart_Type.__name__ = "Integer32"
_FileCopyRuntimeConfigPart_Object = MibScalar
fileCopyRuntimeConfigPart = _FileCopyRuntimeConfigPart_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 25, 10),
    _FileCopyRuntimeConfigPart_Type()
)
fileCopyRuntimeConfigPart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyRuntimeConfigPart.setStatus("current")
_VoiceGrp_ObjectIdentity = ObjectIdentity
voiceGrp = _VoiceGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26)
)
_VoicePortIfConfigTable_Object = MibTable
voicePortIfConfigTable = _VoicePortIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1)
)
if mibBuilder.loadTexts:
    voicePortIfConfigTable.setStatus("current")
_VoicePortIfConfigEntry_Object = MibTableRow
voicePortIfConfigEntry = _VoicePortIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1)
)
voicePortIfConfigEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "voicePortIfConfigModuleIndex"),
    (0, "CISCO-STACK-MIB", "voicePortIfConfigPortIndex"),
)
if mibBuilder.loadTexts:
    voicePortIfConfigEntry.setStatus("current")


class _VoicePortIfConfigModuleIndex_Type(Integer32):
    """Custom type voicePortIfConfigModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoicePortIfConfigModuleIndex_Type.__name__ = "Integer32"
_VoicePortIfConfigModuleIndex_Object = MibTableColumn
voicePortIfConfigModuleIndex = _VoicePortIfConfigModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 1),
    _VoicePortIfConfigModuleIndex_Type()
)
voicePortIfConfigModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortIfConfigModuleIndex.setStatus("current")


class _VoicePortIfConfigPortIndex_Type(Integer32):
    """Custom type voicePortIfConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VoicePortIfConfigPortIndex_Type.__name__ = "Integer32"
_VoicePortIfConfigPortIndex_Object = MibTableColumn
voicePortIfConfigPortIndex = _VoicePortIfConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 2),
    _VoicePortIfConfigPortIndex_Type()
)
voicePortIfConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortIfConfigPortIndex.setStatus("current")


class _VoicePortIfDHCPEnabled_Type(TruthValue):
    """Custom type voicePortIfDHCPEnabled based on TruthValue"""


_VoicePortIfDHCPEnabled_Object = MibTableColumn
voicePortIfDHCPEnabled = _VoicePortIfDHCPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 3),
    _VoicePortIfDHCPEnabled_Type()
)
voicePortIfDHCPEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfDHCPEnabled.setStatus("current")
_VoicePortIfIpAddress_Type = IpAddress
_VoicePortIfIpAddress_Object = MibTableColumn
voicePortIfIpAddress = _VoicePortIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 4),
    _VoicePortIfIpAddress_Type()
)
voicePortIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfIpAddress.setStatus("current")
_VoicePortIfIpNetMask_Type = IpAddress
_VoicePortIfIpNetMask_Object = MibTableColumn
voicePortIfIpNetMask = _VoicePortIfIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 5),
    _VoicePortIfIpNetMask_Type()
)
voicePortIfIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfIpNetMask.setStatus("current")
_VoicePortIfTftpServerAddress_Type = IpAddress
_VoicePortIfTftpServerAddress_Object = MibTableColumn
voicePortIfTftpServerAddress = _VoicePortIfTftpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 6),
    _VoicePortIfTftpServerAddress_Type()
)
voicePortIfTftpServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfTftpServerAddress.setStatus("current")
_VoicePortIfGatewayAddress_Type = IpAddress
_VoicePortIfGatewayAddress_Object = MibTableColumn
voicePortIfGatewayAddress = _VoicePortIfGatewayAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 7),
    _VoicePortIfGatewayAddress_Type()
)
voicePortIfGatewayAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfGatewayAddress.setStatus("current")
_VoicePortIfDnsServerAddress_Type = IpAddress
_VoicePortIfDnsServerAddress_Object = MibTableColumn
voicePortIfDnsServerAddress = _VoicePortIfDnsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 8),
    _VoicePortIfDnsServerAddress_Type()
)
voicePortIfDnsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfDnsServerAddress.setStatus("current")


class _VoicePortIfDnsDomain_Type(DisplayString):
    """Custom type voicePortIfDnsDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoicePortIfDnsDomain_Type.__name__ = "DisplayString"
_VoicePortIfDnsDomain_Object = MibTableColumn
voicePortIfDnsDomain = _VoicePortIfDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 9),
    _VoicePortIfDnsDomain_Type()
)
voicePortIfDnsDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voicePortIfDnsDomain.setStatus("current")


class _VoicePortIfOperDnsDomain_Type(DisplayString):
    """Custom type voicePortIfOperDnsDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VoicePortIfOperDnsDomain_Type.__name__ = "DisplayString"
_VoicePortIfOperDnsDomain_Object = MibTableColumn
voicePortIfOperDnsDomain = _VoicePortIfOperDnsDomain_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 1, 1, 10),
    _VoicePortIfOperDnsDomain_Type()
)
voicePortIfOperDnsDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicePortIfOperDnsDomain.setStatus("current")
_VoicePortCallManagerTable_Object = MibTable
voicePortCallManagerTable = _VoicePortCallManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 2)
)
if mibBuilder.loadTexts:
    voicePortCallManagerTable.setStatus("current")
_VoicePortCallManagerEntry_Object = MibTableRow
voicePortCallManagerEntry = _VoicePortCallManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 2, 1)
)
voicePortCallManagerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "voicePortModuleIndex"),
    (0, "CISCO-STACK-MIB", "voicePortIndex"),
    (0, "CISCO-STACK-MIB", "voicePortCallManagerIndex"),
)
if mibBuilder.loadTexts:
    voicePortCallManagerEntry.setStatus("current")


class _VoicePortModuleIndex_Type(Integer32):
    """Custom type voicePortModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoicePortModuleIndex_Type.__name__ = "Integer32"
_VoicePortModuleIndex_Object = MibTableColumn
voicePortModuleIndex = _VoicePortModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 2, 1, 1),
    _VoicePortModuleIndex_Type()
)
voicePortModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortModuleIndex.setStatus("current")


class _VoicePortIndex_Type(Integer32):
    """Custom type voicePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VoicePortIndex_Type.__name__ = "Integer32"
_VoicePortIndex_Object = MibTableColumn
voicePortIndex = _VoicePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 2, 1, 2),
    _VoicePortIndex_Type()
)
voicePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortIndex.setStatus("current")


class _VoicePortCallManagerIndex_Type(Integer32):
    """Custom type voicePortCallManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_VoicePortCallManagerIndex_Type.__name__ = "Integer32"
_VoicePortCallManagerIndex_Object = MibTableColumn
voicePortCallManagerIndex = _VoicePortCallManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 2, 1, 3),
    _VoicePortCallManagerIndex_Type()
)
voicePortCallManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortCallManagerIndex.setStatus("current")
_VoicePortCallManagerIpAddr_Type = IpAddress
_VoicePortCallManagerIpAddr_Object = MibTableColumn
voicePortCallManagerIpAddr = _VoicePortCallManagerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 2, 1, 4),
    _VoicePortCallManagerIpAddr_Type()
)
voicePortCallManagerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicePortCallManagerIpAddr.setStatus("current")
_VoicePortOperDnsServerTable_Object = MibTable
voicePortOperDnsServerTable = _VoicePortOperDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3)
)
if mibBuilder.loadTexts:
    voicePortOperDnsServerTable.setStatus("current")
_VoicePortOperDnsServerEntry_Object = MibTableRow
voicePortOperDnsServerEntry = _VoicePortOperDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3, 1)
)
voicePortOperDnsServerEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "voicePortDnsModuleIndex"),
    (0, "CISCO-STACK-MIB", "voicePortDnsPortIndex"),
    (0, "CISCO-STACK-MIB", "voicePortOperDnsServerIndex"),
)
if mibBuilder.loadTexts:
    voicePortOperDnsServerEntry.setStatus("current")


class _VoicePortDnsModuleIndex_Type(Integer32):
    """Custom type voicePortDnsModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_VoicePortDnsModuleIndex_Type.__name__ = "Integer32"
_VoicePortDnsModuleIndex_Object = MibTableColumn
voicePortDnsModuleIndex = _VoicePortDnsModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3, 1, 1),
    _VoicePortDnsModuleIndex_Type()
)
voicePortDnsModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortDnsModuleIndex.setStatus("current")


class _VoicePortDnsPortIndex_Type(Integer32):
    """Custom type voicePortDnsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VoicePortDnsPortIndex_Type.__name__ = "Integer32"
_VoicePortDnsPortIndex_Object = MibTableColumn
voicePortDnsPortIndex = _VoicePortDnsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3, 1, 2),
    _VoicePortDnsPortIndex_Type()
)
voicePortDnsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortDnsPortIndex.setStatus("current")
_VoicePortOperDnsServerIndex_Type = Unsigned32
_VoicePortOperDnsServerIndex_Object = MibTableColumn
voicePortOperDnsServerIndex = _VoicePortOperDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3, 1, 3),
    _VoicePortOperDnsServerIndex_Type()
)
voicePortOperDnsServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voicePortOperDnsServerIndex.setStatus("current")
_VoicePortOperDnsServerIpAddr_Type = IpAddress
_VoicePortOperDnsServerIpAddr_Object = MibTableColumn
voicePortOperDnsServerIpAddr = _VoicePortOperDnsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3, 1, 4),
    _VoicePortOperDnsServerIpAddr_Type()
)
voicePortOperDnsServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicePortOperDnsServerIpAddr.setStatus("current")


class _VoicePortOperDnsServerSource_Type(Integer32):
    """Custom type voicePortOperDnsServerSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fromDhcp", 1),
          ("fromPortConfig", 2),
          ("fromSystemConfig", 3))
    )


_VoicePortOperDnsServerSource_Type.__name__ = "Integer32"
_VoicePortOperDnsServerSource_Object = MibTableColumn
voicePortOperDnsServerSource = _VoicePortOperDnsServerSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 26, 3, 1, 5),
    _VoicePortOperDnsServerSource_Type()
)
voicePortOperDnsServerSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voicePortOperDnsServerSource.setStatus("current")
_PortJumboFrameGrp_ObjectIdentity = ObjectIdentity
portJumboFrameGrp = _PortJumboFrameGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 27)
)
_PortJumboFrameTable_Object = MibTable
portJumboFrameTable = _PortJumboFrameTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 27, 1)
)
if mibBuilder.loadTexts:
    portJumboFrameTable.setStatus("current")
_PortJumboFrameEntry_Object = MibTableRow
portJumboFrameEntry = _PortJumboFrameEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 27, 1, 1)
)
portJumboFrameEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "portJumboFrameModuleIndex"),
    (0, "CISCO-STACK-MIB", "portJumboFramePortIndex"),
)
if mibBuilder.loadTexts:
    portJumboFrameEntry.setStatus("current")


class _PortJumboFrameModuleIndex_Type(Integer32):
    """Custom type portJumboFrameModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortJumboFrameModuleIndex_Type.__name__ = "Integer32"
_PortJumboFrameModuleIndex_Object = MibTableColumn
portJumboFrameModuleIndex = _PortJumboFrameModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 27, 1, 1, 1),
    _PortJumboFrameModuleIndex_Type()
)
portJumboFrameModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portJumboFrameModuleIndex.setStatus("current")


class _PortJumboFramePortIndex_Type(Integer32):
    """Custom type portJumboFramePortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PortJumboFramePortIndex_Type.__name__ = "Integer32"
_PortJumboFramePortIndex_Object = MibTableColumn
portJumboFramePortIndex = _PortJumboFramePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 27, 1, 1, 2),
    _PortJumboFramePortIndex_Type()
)
portJumboFramePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portJumboFramePortIndex.setStatus("current")


class _PortJumboFrameEnable_Type(Integer32):
    """Custom type portJumboFrameEnable based on Integer32"""
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


_PortJumboFrameEnable_Type.__name__ = "Integer32"
_PortJumboFrameEnable_Object = MibTableColumn
portJumboFrameEnable = _PortJumboFrameEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 27, 1, 1, 3),
    _PortJumboFrameEnable_Type()
)
portJumboFrameEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portJumboFrameEnable.setStatus("current")
_SwitchAccelerationGrp_ObjectIdentity = ObjectIdentity
switchAccelerationGrp = _SwitchAccelerationGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 28)
)
_SwitchAccelerationModuleTable_Object = MibTable
switchAccelerationModuleTable = _SwitchAccelerationModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 28, 1)
)
if mibBuilder.loadTexts:
    switchAccelerationModuleTable.setStatus("current")
_SwitchAccelerationModuleEntry_Object = MibTableRow
switchAccelerationModuleEntry = _SwitchAccelerationModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 28, 1, 1)
)
switchAccelerationModuleEntry.setIndexNames(
    (0, "CISCO-STACK-MIB", "switchAccelerationModuleIndex"),
)
if mibBuilder.loadTexts:
    switchAccelerationModuleEntry.setStatus("current")


class _SwitchAccelerationModuleIndex_Type(Integer32):
    """Custom type switchAccelerationModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SwitchAccelerationModuleIndex_Type.__name__ = "Integer32"
_SwitchAccelerationModuleIndex_Object = MibTableColumn
switchAccelerationModuleIndex = _SwitchAccelerationModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 28, 1, 1, 1),
    _SwitchAccelerationModuleIndex_Type()
)
switchAccelerationModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchAccelerationModuleIndex.setStatus("current")


class _SwitchAccelerationModuleEnable_Type(TruthValue):
    """Custom type switchAccelerationModuleEnable based on TruthValue"""


_SwitchAccelerationModuleEnable_Object = MibTableColumn
switchAccelerationModuleEnable = _SwitchAccelerationModuleEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 28, 1, 1, 2),
    _SwitchAccelerationModuleEnable_Type()
)
switchAccelerationModuleEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchAccelerationModuleEnable.setStatus("current")
_ConfigGrp_ObjectIdentity = ObjectIdentity
configGrp = _ConfigGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 29)
)


class _ConfigMode_Type(Integer32):
    """Custom type configMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("binary", 1),
          ("text", 2))
    )


_ConfigMode_Type.__name__ = "Integer32"
_ConfigMode_Object = MibScalar
configMode = _ConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 29, 1),
    _ConfigMode_Type()
)
configMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMode.setStatus("current")


class _ConfigTextFileLocation_Type(DisplayString):
    """Custom type configTextFileLocation based on DisplayString"""
    defaultHexValue = ""

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ConfigTextFileLocation_Type.__name__ = "DisplayString"
_ConfigTextFileLocation_Object = MibScalar
configTextFileLocation = _ConfigTextFileLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 29, 2),
    _ConfigTextFileLocation_Type()
)
configTextFileLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configTextFileLocation.setStatus("current")
_ConfigWriteMem_Type = TruthValue
_ConfigWriteMem_Object = MibScalar
configWriteMem = _ConfigWriteMem_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 29, 3),
    _ConfigWriteMem_Type()
)
configWriteMem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configWriteMem.setStatus("current")


class _ConfigWriteMemStatus_Type(Integer32):
    """Custom type configWriteMemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("badFileName", 4),
          ("inProgress", 1),
          ("resourceUnavailable", 3),
          ("someOtherError", 5),
          ("succeeded", 2))
    )


_ConfigWriteMemStatus_Type.__name__ = "Integer32"
_ConfigWriteMemStatus_Object = MibScalar
configWriteMemStatus = _ConfigWriteMemStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 29, 4),
    _ConfigWriteMemStatus_Type()
)
configWriteMemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configWriteMemStatus.setStatus("current")
_CiscoStackMIBConformance_ObjectIdentity = ObjectIdentity
ciscoStackMIBConformance = _CiscoStackMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31)
)
_CiscoStackMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoStackMIBCompliances = _CiscoStackMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1)
)
_CiscoStackMIBGroups_ObjectIdentity = ObjectIdentity
ciscoStackMIBGroups = _CiscoStackMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2)
)
_AdapterCard_ObjectIdentity = ObjectIdentity
adapterCard = _AdapterCard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 2)
)
_Wsc1000sysID_ObjectIdentity = ObjectIdentity
wsc1000sysID = _Wsc1000sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 3)
)
_Wsc1100sysID_ObjectIdentity = ObjectIdentity
wsc1100sysID = _Wsc1100sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 4)
)
_Wsc1200sysID_ObjectIdentity = ObjectIdentity
wsc1200sysID = _Wsc1200sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 5)
)
_Wsc1400sysID_ObjectIdentity = ObjectIdentity
wsc1400sysID = _Wsc1400sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 6)
)
_Wsc5000sysID_ObjectIdentity = ObjectIdentity
wsc5000sysID = _Wsc5000sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 7)
)
_Wsc1600sysID_ObjectIdentity = ObjectIdentity
wsc1600sysID = _Wsc1600sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 8)
)
_Cpw1600sysID_ObjectIdentity = ObjectIdentity
cpw1600sysID = _Cpw1600sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 9)
)
_Wsc3000sysID_ObjectIdentity = ObjectIdentity
wsc3000sysID = _Wsc3000sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 10)
)
_Wsc2900sysID_ObjectIdentity = ObjectIdentity
wsc2900sysID = _Wsc2900sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 12)
)
_Cpw2200sysID_ObjectIdentity = ObjectIdentity
cpw2200sysID = _Cpw2200sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 13)
)
_EsStack_ObjectIdentity = ObjectIdentity
esStack = _EsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 14)
)
_Wsc3200sysID_ObjectIdentity = ObjectIdentity
wsc3200sysID = _Wsc3200sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 15)
)
_Cpw1900sysID_ObjectIdentity = ObjectIdentity
cpw1900sysID = _Cpw1900sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 16)
)
_Wsc5500sysID_ObjectIdentity = ObjectIdentity
wsc5500sysID = _Wsc5500sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 17)
)
_Wsc1900sysID_ObjectIdentity = ObjectIdentity
wsc1900sysID = _Wsc1900sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 18)
)
_Cpw1220sysID_ObjectIdentity = ObjectIdentity
cpw1220sysID = _Cpw1220sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 19)
)
_Wsc2820sysID_ObjectIdentity = ObjectIdentity
wsc2820sysID = _Wsc2820sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 20)
)
_Cpw1420sysID_ObjectIdentity = ObjectIdentity
cpw1420sysID = _Cpw1420sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 21)
)
_Dcd_ObjectIdentity = ObjectIdentity
dcd = _Dcd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 22)
)
_Wsc3100sysID_ObjectIdentity = ObjectIdentity
wsc3100sysID = _Wsc3100sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 23)
)
_Cpw1800sysID_ObjectIdentity = ObjectIdentity
cpw1800sysID = _Cpw1800sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 24)
)
_Cpw1601sysID_ObjectIdentity = ObjectIdentity
cpw1601sysID = _Cpw1601sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 25)
)
_Wsc3001sysID_ObjectIdentity = ObjectIdentity
wsc3001sysID = _Wsc3001sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 26)
)
_Cpw1220csysID_ObjectIdentity = ObjectIdentity
cpw1220csysID = _Cpw1220csysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 27)
)
_Wsc1900csysID_ObjectIdentity = ObjectIdentity
wsc1900csysID = _Wsc1900csysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 28)
)
_Wsc5002sysID_ObjectIdentity = ObjectIdentity
wsc5002sysID = _Wsc5002sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 29)
)
_Cpw1220isysID_ObjectIdentity = ObjectIdentity
cpw1220isysID = _Cpw1220isysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 30)
)
_Wsc1900isysID_ObjectIdentity = ObjectIdentity
wsc1900isysID = _Wsc1900isysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 31)
)
_TsStack_ObjectIdentity = ObjectIdentity
tsStack = _TsStack_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 32)
)
_Wsc3900sysID_ObjectIdentity = ObjectIdentity
wsc3900sysID = _Wsc3900sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 33)
)
_Wsc5505sysID_ObjectIdentity = ObjectIdentity
wsc5505sysID = _Wsc5505sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 34)
)
_Wsc2926sysID_ObjectIdentity = ObjectIdentity
wsc2926sysID = _Wsc2926sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 35)
)
_Wsc5509sysID_ObjectIdentity = ObjectIdentity
wsc5509sysID = _Wsc5509sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 36)
)
_Wsc3920sysID_ObjectIdentity = ObjectIdentity
wsc3920sysID = _Wsc3920sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 37)
)
_Wsc6006sysID_ObjectIdentity = ObjectIdentity
wsc6006sysID = _Wsc6006sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 38)
)
_Wsc6009sysID_ObjectIdentity = ObjectIdentity
wsc6009sysID = _Wsc6009sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 39)
)
_Wsc4003sysID_ObjectIdentity = ObjectIdentity
wsc4003sysID = _Wsc4003sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 40)
)
_Wsc4912gsysID_ObjectIdentity = ObjectIdentity
wsc4912gsysID = _Wsc4912gsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 41)
)
_Wsc2948gsysID_ObjectIdentity = ObjectIdentity
wsc2948gsysID = _Wsc2948gsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 42)
)
_Wsc6509sysID_ObjectIdentity = ObjectIdentity
wsc6509sysID = _Wsc6509sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 44)
)
_Wsc6506sysID_ObjectIdentity = ObjectIdentity
wsc6506sysID = _Wsc6506sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 45)
)
_Wsc4006sysID_ObjectIdentity = ObjectIdentity
wsc4006sysID = _Wsc4006sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 46)
)
_Wsc6509nebsysID_ObjectIdentity = ObjectIdentity
wsc6509nebsysID = _Wsc6509nebsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 47)
)
_Wsc6knamsysID_ObjectIdentity = ObjectIdentity
wsc6knamsysID = _Wsc6knamsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 48)
)
_Wsc2980gsysID_ObjectIdentity = ObjectIdentity
wsc2980gsysID = _Wsc2980gsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 49)
)
_Wsc6513sysID_ObjectIdentity = ObjectIdentity
wsc6513sysID = _Wsc6513sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 50)
)
_Wsc2980gasysID_ObjectIdentity = ObjectIdentity
wsc2980gasysID = _Wsc2980gasysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 51)
)
_Cisco7603sysID_ObjectIdentity = ObjectIdentity
cisco7603sysID = _Cisco7603sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 53)
)
_Cisco7606sysID_ObjectIdentity = ObjectIdentity
cisco7606sysID = _Cisco7606sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 54)
)
_Cisco7609sysID_ObjectIdentity = ObjectIdentity
cisco7609sysID = _Cisco7609sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 55)
)
_Wsc6503sysID_ObjectIdentity = ObjectIdentity
wsc6503sysID = _Wsc6503sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 56)
)
_Wsc4503sysID_ObjectIdentity = ObjectIdentity
wsc4503sysID = _Wsc4503sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 58)
)
_Wsc4506sysID_ObjectIdentity = ObjectIdentity
wsc4506sysID = _Wsc4506sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 59)
)
_Cisco7613sysID_ObjectIdentity = ObjectIdentity
cisco7613sysID = _Cisco7613sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 60)
)
_Wsc6509nebasysID_ObjectIdentity = ObjectIdentity
wsc6509nebasysID = _Wsc6509nebasysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 61)
)
_Wsc2948ggetxsysID_ObjectIdentity = ObjectIdentity
wsc2948ggetxsysID = _Wsc2948ggetxsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 62)
)
_Cisco7604sysID_ObjectIdentity = ObjectIdentity
cisco7604sysID = _Cisco7604sysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 63)
)
_Wsc6504esysID_ObjectIdentity = ObjectIdentity
wsc6504esysID = _Wsc6504esysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 64)
)
_Wsc1900LiteFxsysID_ObjectIdentity = ObjectIdentity
wsc1900LiteFxsysID = _Wsc1900LiteFxsysID_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 5, 175)
)
tokenRingPortEntry.registerAugmentions(
    ("CISCO-STACK-MIB",
     "tokenRingPortSoftErrEntry")
)
tokenRingPortSoftErrEntry.setIndexNames(*tokenRingPortEntry.getIndexNames())

# Managed Objects groups

systemMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 1)
)
systemMiscGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysMgmtType"),
        ("CISCO-STACK-MIB", "sysIpAddr"),
        ("CISCO-STACK-MIB", "sysNetMask"),
        ("CISCO-STACK-MIB", "sysBroadcast"),
        ("CISCO-STACK-MIB", "sysAttachType"),
        ("CISCO-STACK-MIB", "sysReset"),
        ("CISCO-STACK-MIB", "sysBaudRate"),
        ("CISCO-STACK-MIB", "sysInsertMode"),
        ("CISCO-STACK-MIB", "sysClearMacTime"),
        ("CISCO-STACK-MIB", "sysClearPortTime"),
        ("CISCO-STACK-MIB", "sysEnableModem"),
        ("CISCO-STACK-MIB", "sysEnableRedirects"),
        ("CISCO-STACK-MIB", "sysArpAgingTime"),
        ("CISCO-STACK-MIB", "sysCommunityRwa"),
        ("CISCO-STACK-MIB", "sysCommunityRw"),
        ("CISCO-STACK-MIB", "sysCommunityRo"),
        ("CISCO-STACK-MIB", "sysIpVlan"))
)
if mibBuilder.loadTexts:
    systemMiscGroup.setStatus("deprecated")

systemTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 2)
)
systemTrapGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysTrapReceiverAddr"),
        ("CISCO-STACK-MIB", "sysTrapReceiverType"),
        ("CISCO-STACK-MIB", "sysTrapReceiverComm"),
        ("CISCO-STACK-MIB", "sysEnableChassisTraps"),
        ("CISCO-STACK-MIB", "sysEnableModuleTraps"),
        ("CISCO-STACK-MIB", "sysEnableBridgeTraps"),
        ("CISCO-STACK-MIB", "sysEnableRepeaterTraps"))
)
if mibBuilder.loadTexts:
    systemTrapGroup.setStatus("deprecated")

chassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 3)
)
chassisGroup.setObjects(
      *(("CISCO-STACK-MIB", "chassisSysType"),
        ("CISCO-STACK-MIB", "chassisBkplType"),
        ("CISCO-STACK-MIB", "chassisPs1Type"),
        ("CISCO-STACK-MIB", "chassisPs1Status"),
        ("CISCO-STACK-MIB", "chassisPs1TestResult"),
        ("CISCO-STACK-MIB", "chassisPs2Type"),
        ("CISCO-STACK-MIB", "chassisPs2Status"),
        ("CISCO-STACK-MIB", "chassisPs2TestResult"),
        ("CISCO-STACK-MIB", "chassisFanStatus"),
        ("CISCO-STACK-MIB", "chassisFanTestResult"),
        ("CISCO-STACK-MIB", "chassisMinorAlarm"),
        ("CISCO-STACK-MIB", "chassisMajorAlarm"),
        ("CISCO-STACK-MIB", "chassisTempAlarm"),
        ("CISCO-STACK-MIB", "chassisNumSlots"))
)
if mibBuilder.loadTexts:
    chassisGroup.setStatus("current")

moduleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 4)
)
moduleGroup.setObjects(
      *(("CISCO-STACK-MIB", "moduleIndex"),
        ("CISCO-STACK-MIB", "moduleType"),
        ("CISCO-STACK-MIB", "moduleStatus"),
        ("CISCO-STACK-MIB", "moduleTestResult"),
        ("CISCO-STACK-MIB", "moduleAction"),
        ("CISCO-STACK-MIB", "moduleName"),
        ("CISCO-STACK-MIB", "moduleNumPorts"),
        ("CISCO-STACK-MIB", "modulePortStatus"),
        ("CISCO-STACK-MIB", "moduleSubType"),
        ("CISCO-STACK-MIB", "moduleSerialNumberString"))
)
if mibBuilder.loadTexts:
    moduleGroup.setStatus("current")

portGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 5)
)
portGroup.setObjects(
      *(("CISCO-STACK-MIB", "portModuleIndex"),
        ("CISCO-STACK-MIB", "portIndex"),
        ("CISCO-STACK-MIB", "portCrossIndex"),
        ("CISCO-STACK-MIB", "portName"),
        ("CISCO-STACK-MIB", "portType"),
        ("CISCO-STACK-MIB", "portOperStatus"),
        ("CISCO-STACK-MIB", "portCrossGroupIndex"),
        ("CISCO-STACK-MIB", "portAdditionalStatus"),
        ("CISCO-STACK-MIB", "portAdminSpeed"),
        ("CISCO-STACK-MIB", "portDuplex"),
        ("CISCO-STACK-MIB", "portIfIndex"),
        ("CISCO-STACK-MIB", "portSpantreeFastStart"),
        ("CISCO-STACK-MIB", "portAdminRxFlowControl"),
        ("CISCO-STACK-MIB", "portOperRxFlowControl"),
        ("CISCO-STACK-MIB", "portAdminTxFlowControl"),
        ("CISCO-STACK-MIB", "portOperTxFlowControl"),
        ("CISCO-STACK-MIB", "portMacControlTransmitFrames"),
        ("CISCO-STACK-MIB", "portMacControlReceiveFrames"),
        ("CISCO-STACK-MIB", "portMacControlPauseTransmitFrames"),
        ("CISCO-STACK-MIB", "portMacControlPauseReceiveFrames"),
        ("CISCO-STACK-MIB", "portMacControlUnknownProtocolFrames"),
        ("CISCO-STACK-MIB", "portLinkFaultStatus"))
)
if mibBuilder.loadTexts:
    portGroup.setStatus("deprecated")

optionalSystemMiscGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 6)
)
optionalSystemMiscGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysConfigChangeTime"),
        ("CISCO-STACK-MIB", "sysBannerMotd"),
        ("CISCO-STACK-MIB", "sysConfigChangeInfo"),
        ("CISCO-STACK-MIB", "sysConfigRegister"),
        ("CISCO-STACK-MIB", "sysBootVariable"),
        ("CISCO-STACK-MIB", "sysBootedImage"))
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup.setStatus("current")

optionalSystemTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 7)
)
optionalSystemTrapGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysEnableIpPermitTraps"),
        ("CISCO-STACK-MIB", "sysEnableVmpsTraps"),
        ("CISCO-STACK-MIB", "sysEnableConfigTraps"),
        ("CISCO-STACK-MIB", "sysEnableEntityTrap"),
        ("CISCO-STACK-MIB", "sysEnableStpxTrap"))
)
if mibBuilder.loadTexts:
    optionalSystemTrapGroup.setStatus("deprecated")

optionalChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 8)
)
optionalChassisGroup.setObjects(
      *(("CISCO-STACK-MIB", "chassisPs1TestResult"),
        ("CISCO-STACK-MIB", "chassisPs2TestResult"),
        ("CISCO-STACK-MIB", "chassisFanTestResult"),
        ("CISCO-STACK-MIB", "chassisSlotConfig"),
        ("CISCO-STACK-MIB", "chassisModel"),
        ("CISCO-STACK-MIB", "chassisComponentIndex"),
        ("CISCO-STACK-MIB", "chassisComponentType"),
        ("CISCO-STACK-MIB", "chassisComponentSerialNumber"),
        ("CISCO-STACK-MIB", "chassisComponentHwVersion"),
        ("CISCO-STACK-MIB", "chassisComponentModel"),
        ("CISCO-STACK-MIB", "chassisSerialNumberString"))
)
if mibBuilder.loadTexts:
    optionalChassisGroup.setStatus("deprecated")

optionalModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 9)
)
optionalModuleGroup.setObjects(
      *(("CISCO-STACK-MIB", "moduleTestResult"),
        ("CISCO-STACK-MIB", "moduleModel"),
        ("CISCO-STACK-MIB", "moduleHwVersion"),
        ("CISCO-STACK-MIB", "moduleFwVersion"),
        ("CISCO-STACK-MIB", "moduleSwVersion"),
        ("CISCO-STACK-MIB", "moduleStandbyStatus"),
        ("CISCO-STACK-MIB", "moduleIPAddress"),
        ("CISCO-STACK-MIB", "moduleIPAddressVlan"),
        ("CISCO-STACK-MIB", "moduleSubType2"),
        ("CISCO-STACK-MIB", "moduleSlotNum"))
)
if mibBuilder.loadTexts:
    optionalModuleGroup.setStatus("current")

optionalPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 10)
)
optionalPortGroup.setObjects(
      *(("CISCO-STACK-MIB", "portSecurityModuleIndex"),
        ("CISCO-STACK-MIB", "portSecurityPortIndex"),
        ("CISCO-STACK-MIB", "portSecurityAdminStatus"),
        ("CISCO-STACK-MIB", "portSecurityOperStatus"),
        ("CISCO-STACK-MIB", "portSecurityLastSrcAddr"),
        ("CISCO-STACK-MIB", "portSecuritySecureSrcAddr"),
        ("CISCO-STACK-MIB", "portChannelModuleIndex"),
        ("CISCO-STACK-MIB", "portChannelPortIndex"),
        ("CISCO-STACK-MIB", "portChannelPorts"),
        ("CISCO-STACK-MIB", "portChannelAdminStatus"),
        ("CISCO-STACK-MIB", "portChannelOperStatus"),
        ("CISCO-STACK-MIB", "portChannelNeighbourDeviceId"),
        ("CISCO-STACK-MIB", "portChannelNeighbourPortId"),
        ("CISCO-STACK-MIB", "portChannelProtInPackets"),
        ("CISCO-STACK-MIB", "portChannelProtOutPackets"),
        ("CISCO-STACK-MIB", "portChannelIfIndex"),
        ("CISCO-STACK-MIB", "portCpbModuleIndex"),
        ("CISCO-STACK-MIB", "portCpbPortIndex"),
        ("CISCO-STACK-MIB", "portCpbSpeed"),
        ("CISCO-STACK-MIB", "portCpbDuplex"),
        ("CISCO-STACK-MIB", "portCpbTrunkEncapsulationType"),
        ("CISCO-STACK-MIB", "portCpbTrunkMode"),
        ("CISCO-STACK-MIB", "portCpbChannel"),
        ("CISCO-STACK-MIB", "portCpbBroadcastSuppression"),
        ("CISCO-STACK-MIB", "portCpbFlowControl"),
        ("CISCO-STACK-MIB", "portCpbSecurity"),
        ("CISCO-STACK-MIB", "portCpbVlanMembership"),
        ("CISCO-STACK-MIB", "portCpbPortfast"),
        ("CISCO-STACK-MIB", "portTopNControlIndex"),
        ("CISCO-STACK-MIB", "portTopNRateBase"),
        ("CISCO-STACK-MIB", "portTopNType"),
        ("CISCO-STACK-MIB", "portTopNMode"),
        ("CISCO-STACK-MIB", "portTopNReportStatus"),
        ("CISCO-STACK-MIB", "portTopNDuration"),
        ("CISCO-STACK-MIB", "portTopNTimeRemaining"),
        ("CISCO-STACK-MIB", "portTopNStartTime"),
        ("CISCO-STACK-MIB", "portTopNRequestedSize"),
        ("CISCO-STACK-MIB", "portTopNGrantedSize"),
        ("CISCO-STACK-MIB", "portTopNOwner"),
        ("CISCO-STACK-MIB", "portTopNStatus"),
        ("CISCO-STACK-MIB", "portTopNIndex"),
        ("CISCO-STACK-MIB", "portTopNModuleNumber"),
        ("CISCO-STACK-MIB", "portTopNPortNumber"),
        ("CISCO-STACK-MIB", "portTopNUtilization"),
        ("CISCO-STACK-MIB", "portTopNIOOctets"),
        ("CISCO-STACK-MIB", "portTopNIOPkts"),
        ("CISCO-STACK-MIB", "portTopNIOBroadcast"),
        ("CISCO-STACK-MIB", "portTopNIOMulticast"),
        ("CISCO-STACK-MIB", "portTopNInErrors"),
        ("CISCO-STACK-MIB", "portTopNBufferOverFlow"))
)
if mibBuilder.loadTexts:
    optionalPortGroup.setStatus("deprecated")

systemTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 11)
)
systemTrafficGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysTrafficMeterType"),
        ("CISCO-STACK-MIB", "sysTraffic"),
        ("CISCO-STACK-MIB", "sysTrafficPeak"),
        ("CISCO-STACK-MIB", "sysTrafficPeakTime"),
        ("CISCO-STACK-MIB", "sysTrafficMeter"),
        ("CISCO-STACK-MIB", "sysTrafficMeterPeak"),
        ("CISCO-STACK-MIB", "sysTrafficMeterPeakTime"))
)
if mibBuilder.loadTexts:
    systemTrafficGroup.setStatus("current")

systemFddiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 12)
)
systemFddiGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysFddiRingSMTIndex"),
        ("CISCO-STACK-MIB", "sysFddiRingAddress"),
        ("CISCO-STACK-MIB", "sysFddiRingNext"))
)
if mibBuilder.loadTexts:
    systemFddiGroup.setStatus("current")

systemRmonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 13)
)
systemRmonGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysEnableRmon"),
        ("CISCO-STACK-MIB", "sysExtendedRmonVlanModeEnable"),
        ("CISCO-STACK-MIB", "sysExtendedRmonNetflowPassword"),
        ("CISCO-STACK-MIB", "sysExtendedRmonNetflowEnable"),
        ("CISCO-STACK-MIB", "sysExtendedRmonVlanAgentEnable"),
        ("CISCO-STACK-MIB", "sysExtendedRmonEnable"))
)
if mibBuilder.loadTexts:
    systemRmonGroup.setStatus("current")

authenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 14)
)
authenticationGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysConsolePrimaryLoginAuthentication"),
        ("CISCO-STACK-MIB", "sysConsolePrimaryEnableAuthentication"),
        ("CISCO-STACK-MIB", "sysTelnetPrimaryLoginAuthentication"),
        ("CISCO-STACK-MIB", "sysTelnetPrimaryEnableAuthentication"),
        ("CISCO-STACK-MIB", "tacacsLoginAuthentication"),
        ("CISCO-STACK-MIB", "tacacsEnableAuthentication"),
        ("CISCO-STACK-MIB", "tacacsLocalLoginAuthentication"),
        ("CISCO-STACK-MIB", "tacacsLocalEnableAuthentication"),
        ("CISCO-STACK-MIB", "tacacsNumLoginAttempts"),
        ("CISCO-STACK-MIB", "tacacsDirectedRequest"),
        ("CISCO-STACK-MIB", "tacacsTimeout"),
        ("CISCO-STACK-MIB", "tacacsAuthKey"),
        ("CISCO-STACK-MIB", "tacacsServerAddr"),
        ("CISCO-STACK-MIB", "tacacsServerType"),
        ("CISCO-STACK-MIB", "radiusLoginAuthentication"),
        ("CISCO-STACK-MIB", "radiusEnableAuthentication"),
        ("CISCO-STACK-MIB", "radiusDeadtime"),
        ("CISCO-STACK-MIB", "radiusAuthKey"),
        ("CISCO-STACK-MIB", "radiusTimeout"),
        ("CISCO-STACK-MIB", "radiusRetransmits"),
        ("CISCO-STACK-MIB", "radiusServerAddr"),
        ("CISCO-STACK-MIB", "radiusServerAuthPort"),
        ("CISCO-STACK-MIB", "radiusServerType"))
)
if mibBuilder.loadTexts:
    authenticationGroup.setStatus("deprecated")

tftpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 15)
)
tftpGroup.setObjects(
      *(("CISCO-STACK-MIB", "tftpHost"),
        ("CISCO-STACK-MIB", "tftpFile"),
        ("CISCO-STACK-MIB", "tftpModule"),
        ("CISCO-STACK-MIB", "tftpAction"),
        ("CISCO-STACK-MIB", "tftpResult"))
)
if mibBuilder.loadTexts:
    tftpGroup.setStatus("current")

brouteEnableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 16)
)
brouteEnableGroup.setObjects(
      *(("CISCO-STACK-MIB", "brouterPortModule"),
        ("CISCO-STACK-MIB", "brouterPort"),
        ("CISCO-STACK-MIB", "brouterEnableRip"),
        ("CISCO-STACK-MIB", "brouterEnableSpantree"),
        ("CISCO-STACK-MIB", "brouterEnableGiantCheck"),
        ("CISCO-STACK-MIB", "brouterEnableIpFragmentation"),
        ("CISCO-STACK-MIB", "brouterEnableUnreachables"),
        ("CISCO-STACK-MIB", "brouterCamMode"),
        ("CISCO-STACK-MIB", "brouterIpxSnapToEther"),
        ("CISCO-STACK-MIB", "brouterIpx8023RawToFddi"),
        ("CISCO-STACK-MIB", "brouterEthernetReceiveMax"),
        ("CISCO-STACK-MIB", "brouterEthernetTransmitMax"),
        ("CISCO-STACK-MIB", "brouterFddiReceiveMax"),
        ("CISCO-STACK-MIB", "brouterFddiTransmitMax"),
        ("CISCO-STACK-MIB", "brouterPortIpVlan"),
        ("CISCO-STACK-MIB", "brouterPortIpAddr"),
        ("CISCO-STACK-MIB", "brouterPortNetMask"),
        ("CISCO-STACK-MIB", "brouterPortBroadcast"),
        ("CISCO-STACK-MIB", "brouterPortBridgeVlan"),
        ("CISCO-STACK-MIB", "brouterPortIpHelpers"),
        ("CISCO-STACK-MIB", "brouterIpx8022ToEther"),
        ("CISCO-STACK-MIB", "brouterEnableTransitEncapsulation"),
        ("CISCO-STACK-MIB", "brouterEnableFddiCheck"),
        ("CISCO-STACK-MIB", "brouterEnableAPaRT"))
)
if mibBuilder.loadTexts:
    brouteEnableGroup.setStatus("current")

filterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 17)
)
filterGroup.setObjects(
      *(("CISCO-STACK-MIB", "filterMacModule"),
        ("CISCO-STACK-MIB", "filterMacPort"),
        ("CISCO-STACK-MIB", "filterMacAddress"),
        ("CISCO-STACK-MIB", "filterMacType"),
        ("CISCO-STACK-MIB", "filterVendorModule"),
        ("CISCO-STACK-MIB", "filterVendorPort"),
        ("CISCO-STACK-MIB", "filterVendorId"),
        ("CISCO-STACK-MIB", "filterVendorType"),
        ("CISCO-STACK-MIB", "filterProtocolModule"),
        ("CISCO-STACK-MIB", "filterProtocolPort"),
        ("CISCO-STACK-MIB", "filterProtocolValue"),
        ("CISCO-STACK-MIB", "filterProtocolType"),
        ("CISCO-STACK-MIB", "filterTestModule"),
        ("CISCO-STACK-MIB", "filterTestPort"),
        ("CISCO-STACK-MIB", "filterTestIndex"),
        ("CISCO-STACK-MIB", "filterTestType"),
        ("CISCO-STACK-MIB", "filterTestOffset"),
        ("CISCO-STACK-MIB", "filterTestValue"),
        ("CISCO-STACK-MIB", "filterTestMask"),
        ("CISCO-STACK-MIB", "filterPortModule"),
        ("CISCO-STACK-MIB", "filterPort"),
        ("CISCO-STACK-MIB", "filterPortComplex"),
        ("CISCO-STACK-MIB", "filterPortBroadcastThrottle"),
        ("CISCO-STACK-MIB", "filterPortBroadcastThreshold"),
        ("CISCO-STACK-MIB", "filterPortBroadcastDiscards"))
)
if mibBuilder.loadTexts:
    filterGroup.setStatus("current")

monitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 18)
)
monitorGroup.setObjects(
      *(("CISCO-STACK-MIB", "monitorSourceModule"),
        ("CISCO-STACK-MIB", "monitorSourcePort"),
        ("CISCO-STACK-MIB", "monitorDestinationModule"),
        ("CISCO-STACK-MIB", "monitorDestinationPort"),
        ("CISCO-STACK-MIB", "monitorDirection"),
        ("CISCO-STACK-MIB", "monitorEnable"),
        ("CISCO-STACK-MIB", "monitorAdminSourcePorts"),
        ("CISCO-STACK-MIB", "monitorOperSourcePorts"))
)
if mibBuilder.loadTexts:
    monitorGroup.setStatus("deprecated")

vlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 19)
)
vlanGroup.setObjects(
      *(("CISCO-STACK-MIB", "vlanIndex"),
        ("CISCO-STACK-MIB", "vlanSpantreeEnable"),
        ("CISCO-STACK-MIB", "vlanIfIndex"),
        ("CISCO-STACK-MIB", "vlanPortModule"),
        ("CISCO-STACK-MIB", "vlanPort"),
        ("CISCO-STACK-MIB", "vlanPortVlan"),
        ("CISCO-STACK-MIB", "vlanPortIslVlansAllowed"),
        ("CISCO-STACK-MIB", "vlanPortSwitchLevel"),
        ("CISCO-STACK-MIB", "vlanPortIslAdminStatus"),
        ("CISCO-STACK-MIB", "vlanPortIslOperStatus"),
        ("CISCO-STACK-MIB", "vlanPortIslPriorityVlans"),
        ("CISCO-STACK-MIB", "vlanPortAdminStatus"),
        ("CISCO-STACK-MIB", "vlanPortOperStatus"))
)
if mibBuilder.loadTexts:
    vlanGroup.setStatus("deprecated")

vmpsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 20)
)
vmpsGroup.setObjects(
      *(("CISCO-STACK-MIB", "vmpsAddr"),
        ("CISCO-STACK-MIB", "vmpsType"),
        ("CISCO-STACK-MIB", "vmpsAction"),
        ("CISCO-STACK-MIB", "vmpsAccessed"))
)
if mibBuilder.loadTexts:
    vmpsGroup.setStatus("current")

tokenRingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 21)
)
tokenRingGroup.setObjects(
      *(("CISCO-STACK-MIB", "tokenRingModuleIndex"),
        ("CISCO-STACK-MIB", "tokenRingPortIndex"),
        ("CISCO-STACK-MIB", "tokenRingPortSetACbits"),
        ("CISCO-STACK-MIB", "tokenRingPortMode"),
        ("CISCO-STACK-MIB", "tokenRingPortEarlyTokenRel"),
        ("CISCO-STACK-MIB", "tokenRingPortPriorityThresh"),
        ("CISCO-STACK-MIB", "tokenRingPortPriorityMinXmit"),
        ("CISCO-STACK-MIB", "tokenRingPortCfgLossThresh"),
        ("CISCO-STACK-MIB", "tokenRingPortCfgLossInterval"),
        ("CISCO-STACK-MIB", "tokenRingDripDistCrfMode"),
        ("CISCO-STACK-MIB", "tokenRingDripAreReductionMode"),
        ("CISCO-STACK-MIB", "tokenRingDripLocalNodeID"),
        ("CISCO-STACK-MIB", "tokenRingDripLastRevision"),
        ("CISCO-STACK-MIB", "tokenRingDripLastChangedRevision"),
        ("CISCO-STACK-MIB", "tokenRingDripAdvertsReceived"),
        ("CISCO-STACK-MIB", "tokenRingDripAdvertsTransmitted"),
        ("CISCO-STACK-MIB", "tokenRingDripAdvertsProcessed"),
        ("CISCO-STACK-MIB", "tokenRingDripInputQueueDrops"),
        ("CISCO-STACK-MIB", "tokenRingDripOutputQueueDrops"),
        ("CISCO-STACK-MIB", "tokenRingDripVlan"),
        ("CISCO-STACK-MIB", "tokenRingDripLocalPortStatus"),
        ("CISCO-STACK-MIB", "tokenRingDripRemotePortStatus"),
        ("CISCO-STACK-MIB", "tokenRingDripRemotePortConfigured"),
        ("CISCO-STACK-MIB", "tokenRingDripDistributedCrf"),
        ("CISCO-STACK-MIB", "tokenRingDripBackupCrf"),
        ("CISCO-STACK-MIB", "tokenRingDripOwnerNodeID"))
)
if mibBuilder.loadTexts:
    tokenRingGroup.setStatus("current")

mcastGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 22)
)
mcastGroup.setObjects(
      *(("CISCO-STACK-MIB", "mcastRouterModuleIndex"),
        ("CISCO-STACK-MIB", "mcastRouterPortIndex"),
        ("CISCO-STACK-MIB", "mcastRouterAdminStatus"),
        ("CISCO-STACK-MIB", "mcastRouterOperStatus"),
        ("CISCO-STACK-MIB", "mcastEnableCgmp"),
        ("CISCO-STACK-MIB", "mcastEnableIgmp"))
)
if mibBuilder.loadTexts:
    mcastGroup.setStatus("current")

dnsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 23)
)
dnsGroup.setObjects(
      *(("CISCO-STACK-MIB", "dnsEnable"),
        ("CISCO-STACK-MIB", "dnsServerAddr"),
        ("CISCO-STACK-MIB", "dnsServerType"),
        ("CISCO-STACK-MIB", "dnsDomainName"))
)
if mibBuilder.loadTexts:
    dnsGroup.setStatus("current")

syslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 24)
)
syslogGroup.setObjects(
      *(("CISCO-STACK-MIB", "syslogServerAddr"),
        ("CISCO-STACK-MIB", "syslogServerType"),
        ("CISCO-STACK-MIB", "syslogConsoleEnable"),
        ("CISCO-STACK-MIB", "syslogHostEnable"),
        ("CISCO-STACK-MIB", "syslogMessageFacility"),
        ("CISCO-STACK-MIB", "syslogMessageSeverity"),
        ("CISCO-STACK-MIB", "syslogTimeStampOption"))
)
if mibBuilder.loadTexts:
    syslogGroup.setStatus("current")

ntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 25)
)
ntpGroup.setObjects(
      *(("CISCO-STACK-MIB", "ntpBcastClient"),
        ("CISCO-STACK-MIB", "ntpBcastDelay"),
        ("CISCO-STACK-MIB", "ntpClient"),
        ("CISCO-STACK-MIB", "ntpServerAddress"),
        ("CISCO-STACK-MIB", "ntpServerType"),
        ("CISCO-STACK-MIB", "ntpSummertimeStatus"),
        ("CISCO-STACK-MIB", "ntpSummerTimezoneName"),
        ("CISCO-STACK-MIB", "ntpTimezoneName"),
        ("CISCO-STACK-MIB", "ntpTimezoneOffsetHour"),
        ("CISCO-STACK-MIB", "ntpTimezoneOffsetMinute"))
)
if mibBuilder.loadTexts:
    ntpGroup.setStatus("current")

ipPermitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 26)
)
ipPermitGroup.setObjects(
      *(("CISCO-STACK-MIB", "ipPermitAddress"),
        ("CISCO-STACK-MIB", "ipPermitMask"),
        ("CISCO-STACK-MIB", "ipPermitEnable"),
        ("CISCO-STACK-MIB", "ipPermitType"),
        ("CISCO-STACK-MIB", "ipPermitDeniedAddress"),
        ("CISCO-STACK-MIB", "ipPermitDeniedAccess"),
        ("CISCO-STACK-MIB", "ipPermitDeniedTime"))
)
if mibBuilder.loadTexts:
    ipPermitGroup.setStatus("deprecated")

mdgGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 27)
)
mdgGatewayGroup.setObjects(
      *(("CISCO-STACK-MIB", "mdgGatewayAddr"),
        ("CISCO-STACK-MIB", "mdgGatewayType"))
)
if mibBuilder.loadTexts:
    mdgGatewayGroup.setStatus("current")

traceRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 28)
)
traceRouteGroup.setObjects(
      *(("CISCO-STACK-MIB", "traceRouteMaxQueries"),
        ("CISCO-STACK-MIB", "traceRouteQueryIndex"),
        ("CISCO-STACK-MIB", "traceRouteHost"),
        ("CISCO-STACK-MIB", "traceRouteQueryDNSEnable"),
        ("CISCO-STACK-MIB", "traceRouteQueryWaitingTime"),
        ("CISCO-STACK-MIB", "traceRouteQueryInitTTL"),
        ("CISCO-STACK-MIB", "traceRouteQueryMaxTTL"),
        ("CISCO-STACK-MIB", "traceRouteQueryUDPPort"),
        ("CISCO-STACK-MIB", "traceRouteQueryPacketCount"),
        ("CISCO-STACK-MIB", "traceRouteQueryPacketSize"),
        ("CISCO-STACK-MIB", "traceRouteQueryTOS"),
        ("CISCO-STACK-MIB", "traceRouteQueryResult"),
        ("CISCO-STACK-MIB", "traceRouteQueryTime"),
        ("CISCO-STACK-MIB", "traceRouteQueryOwner"),
        ("CISCO-STACK-MIB", "traceRouteQueryStatus"),
        ("CISCO-STACK-MIB", "traceRouteDataIndex"),
        ("CISCO-STACK-MIB", "traceRouteDataGatewayName"),
        ("CISCO-STACK-MIB", "traceRouteDataGatewayIp"),
        ("CISCO-STACK-MIB", "traceRouteDataRtt"),
        ("CISCO-STACK-MIB", "traceRouteDataHopCount"),
        ("CISCO-STACK-MIB", "traceRouteDataErrors"))
)
if mibBuilder.loadTexts:
    traceRouteGroup.setStatus("current")

deprecatedObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 29)
)
deprecatedObjectGroup.setObjects(
      *(("CISCO-STACK-MIB", "sysCommunityAccess"),
        ("CISCO-STACK-MIB", "sysCommunityString"),
        ("CISCO-STACK-MIB", "moduleHwHiVersion"),
        ("CISCO-STACK-MIB", "moduleHwLoVersion"),
        ("CISCO-STACK-MIB", "moduleFwHiVersion"),
        ("CISCO-STACK-MIB", "moduleFwLoVersion"),
        ("CISCO-STACK-MIB", "moduleSwHiVersion"),
        ("CISCO-STACK-MIB", "moduleSwLoVersion"),
        ("CISCO-STACK-MIB", "brouterCamAgingTime"),
        ("CISCO-STACK-MIB", "chassisSerialNumber"),
        ("CISCO-STACK-MIB", "moduleSerialNumber"))
)
if mibBuilder.loadTexts:
    deprecatedObjectGroup.setStatus("deprecated")

ntpAuthenticationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 30)
)
ntpAuthenticationGroup.setObjects(
      *(("CISCO-STACK-MIB", "ntpServerPublicKey"),
        ("CISCO-STACK-MIB", "ntpAuthenticationEnable"),
        ("CISCO-STACK-MIB", "ntpAuthenticationPublicKey"),
        ("CISCO-STACK-MIB", "ntpAuthenticationSecretKey"),
        ("CISCO-STACK-MIB", "ntpAuthenticationTrustedMode"),
        ("CISCO-STACK-MIB", "ntpAuthenticationType"))
)
if mibBuilder.loadTexts:
    ntpAuthenticationGroup.setStatus("current")

tokenRingSoftErrorMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 31)
)
tokenRingSoftErrorMonitorGroup.setObjects(
      *(("CISCO-STACK-MIB", "tokenRingPortSoftErrThresh"),
        ("CISCO-STACK-MIB", "tokenRingPortSoftErrReportInterval"),
        ("CISCO-STACK-MIB", "tokenRingPortSoftErrResetCounters"),
        ("CISCO-STACK-MIB", "tokenRingPortSoftErrLastCounterReset"),
        ("CISCO-STACK-MIB", "tokenRingPortSoftErrEnable"))
)
if mibBuilder.loadTexts:
    tokenRingSoftErrorMonitorGroup.setStatus("current")

portCpbGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 32)
)
portCpbGroup1.setObjects(
    ("CISCO-STACK-MIB", "portCpbUdld")
)
if mibBuilder.loadTexts:
    portCpbGroup1.setStatus("current")

portSecurityGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 33)
)
portSecurityGroup1.setObjects(
      *(("CISCO-STACK-MIB", "portSecurityMaxSrcAddr"),
        ("CISCO-STACK-MIB", "portSecurityAgingTime"),
        ("CISCO-STACK-MIB", "portSecurityShutdownTimeOut"),
        ("CISCO-STACK-MIB", "portSecurityViolationPolicy"),
        ("CISCO-STACK-MIB", "portSecurityExtModuleIndex"),
        ("CISCO-STACK-MIB", "portSecurityExtPortIndex"),
        ("CISCO-STACK-MIB", "portSecurityExtSecureSrcAddr"),
        ("CISCO-STACK-MIB", "portSecurityExtControlStatus"))
)
if mibBuilder.loadTexts:
    portSecurityGroup1.setStatus("current")

fileCopyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 34)
)
fileCopyGroup.setObjects(
      *(("CISCO-STACK-MIB", "fileCopyProtocol"),
        ("CISCO-STACK-MIB", "fileCopyRemoteServer"),
        ("CISCO-STACK-MIB", "fileCopySrcFileName"),
        ("CISCO-STACK-MIB", "fileCopyDstFileName"),
        ("CISCO-STACK-MIB", "fileCopyModuleNumber"),
        ("CISCO-STACK-MIB", "fileCopyUserName"),
        ("CISCO-STACK-MIB", "fileCopyAction"),
        ("CISCO-STACK-MIB", "fileCopyResult"),
        ("CISCO-STACK-MIB", "fileCopyResultRcpErrorMessage"))
)
if mibBuilder.loadTexts:
    fileCopyGroup.setStatus("current")

optionalSystemMiscGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 35)
)
optionalSystemMiscGroup1.setObjects(
      *(("CISCO-STACK-MIB", "sysStartupConfigSource"),
        ("CISCO-STACK-MIB", "sysStartupConfigSourceFile"),
        ("CISCO-STACK-MIB", "sysConfigSupervisorModuleNo"),
        ("CISCO-STACK-MIB", "sysStandbyPortEnable"))
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup1.setStatus("current")

ipPermitGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 36)
)
ipPermitGroup1.setObjects(
    ("CISCO-STACK-MIB", "ipPermitAccessType")
)
if mibBuilder.loadTexts:
    ipPermitGroup1.setStatus("current")

optionalSystemMiscGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 37)
)
optionalSystemMiscGroup2.setObjects(
      *(("CISCO-STACK-MIB", "sysPortFastBpduGuard"),
        ("CISCO-STACK-MIB", "sysErrDisableTimeoutEnable"),
        ("CISCO-STACK-MIB", "sysErrDisableTimeoutInterval"),
        ("CISCO-STACK-MIB", "sysTrafficMonitorHighWaterMark"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityEnable"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityVersioningEnable"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityOperStatus"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityNotRunningReason"))
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup2.setStatus("deprecated")

filterGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 38)
)
filterGroup1.setObjects(
    ("CISCO-STACK-MIB", "filterPortBroadcastThresholdFraction")
)
if mibBuilder.loadTexts:
    filterGroup1.setStatus("current")

mcastGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 39)
)
mcastGroup1.setObjects(
    ("CISCO-STACK-MIB", "mcastEnableRgmp")
)
if mibBuilder.loadTexts:
    mcastGroup1.setStatus("current")

portGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 40)
)
portGroup1.setObjects(
      *(("CISCO-STACK-MIB", "portAdditionalOperStatus"),
        ("CISCO-STACK-MIB", "portEntPhysicalIndex"))
)
if mibBuilder.loadTexts:
    portGroup1.setStatus("current")

chassisGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 41)
)
chassisGroup1.setObjects(
      *(("CISCO-STACK-MIB", "chassisPs3Type"),
        ("CISCO-STACK-MIB", "chassisPs3Status"),
        ("CISCO-STACK-MIB", "chassisPs3TestResult"),
        ("CISCO-STACK-MIB", "chassisPEMInstalled"))
)
if mibBuilder.loadTexts:
    chassisGroup1.setStatus("current")

moduleGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 42)
)
moduleGroup1.setObjects(
    ("CISCO-STACK-MIB", "moduleEntPhysicalIndex")
)
if mibBuilder.loadTexts:
    moduleGroup1.setStatus("current")

portCpbGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 43)
)
portCpbGroup2.setObjects(
    ("CISCO-STACK-MIB", "portCpbSpan")
)
if mibBuilder.loadTexts:
    portCpbGroup2.setStatus("current")

voiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 44)
)
voiceGroup.setObjects(
      *(("CISCO-STACK-MIB", "voicePortIfDHCPEnabled"),
        ("CISCO-STACK-MIB", "voicePortIfIpAddress"),
        ("CISCO-STACK-MIB", "voicePortIfIpNetMask"),
        ("CISCO-STACK-MIB", "voicePortIfTftpServerAddress"),
        ("CISCO-STACK-MIB", "voicePortIfGatewayAddress"),
        ("CISCO-STACK-MIB", "voicePortIfDnsServerAddress"),
        ("CISCO-STACK-MIB", "voicePortIfDnsDomain"),
        ("CISCO-STACK-MIB", "voicePortIfOperDnsDomain"),
        ("CISCO-STACK-MIB", "voicePortCallManagerIpAddr"),
        ("CISCO-STACK-MIB", "voicePortOperDnsServerIpAddr"),
        ("CISCO-STACK-MIB", "voicePortOperDnsServerSource"))
)
if mibBuilder.loadTexts:
    voiceGroup.setStatus("current")

portGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 45)
)
portGroup2.setObjects(
    ("CISCO-STACK-MIB", "portInlinePowerDetect")
)
if mibBuilder.loadTexts:
    portGroup2.setStatus("current")

vlanGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 46)
)
vlanGroup1.setObjects(
    ("CISCO-STACK-MIB", "vlanPortAuxiliaryVlan")
)
if mibBuilder.loadTexts:
    vlanGroup1.setStatus("deprecated")

portCpbGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 47)
)
portCpbGroup3.setObjects(
      *(("CISCO-STACK-MIB", "portCpbInlinePower"),
        ("CISCO-STACK-MIB", "portCpbAuxiliaryVlan"))
)
if mibBuilder.loadTexts:
    portCpbGroup3.setStatus("current")

moduleGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 48)
)
moduleGroup2.setObjects(
    ("CISCO-STACK-MIB", "moduleAdditionalStatus")
)
if mibBuilder.loadTexts:
    moduleGroup2.setStatus("current")

switchAccelerationModuleGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 49)
)
switchAccelerationModuleGroup.setObjects(
      *(("CISCO-STACK-MIB", "switchAccelerationModuleIndex"),
        ("CISCO-STACK-MIB", "switchAccelerationModuleEnable"))
)
if mibBuilder.loadTexts:
    switchAccelerationModuleGroup.setStatus("current")

optionalSystemMiscGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 50)
)
optionalSystemMiscGroup3.setObjects(
    ("CISCO-STACK-MIB", "sysExtendedRmonNetflowModuleMask")
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup3.setStatus("current")

optionalSystemMiscGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 51)
)
optionalSystemMiscGroup4.setObjects(
    ("CISCO-STACK-MIB", "sshPublicKeySize")
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup4.setStatus("current")

vlanTrunkMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 52)
)
vlanTrunkMappingGroup.setObjects(
      *(("CISCO-STACK-MIB", "vlanTrunkMappingMax"),
        ("CISCO-STACK-MIB", "vlanTrunkMappingToVlan"),
        ("CISCO-STACK-MIB", "vlanTrunkMappingType"),
        ("CISCO-STACK-MIB", "vlanTrunkMappingOper"),
        ("CISCO-STACK-MIB", "vlanTrunkMappingStatus"))
)
if mibBuilder.loadTexts:
    vlanTrunkMappingGroup.setStatus("current")

portJumboFrameGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 53)
)
portJumboFrameGroup.setObjects(
      *(("CISCO-STACK-MIB", "portJumboFrameModuleIndex"),
        ("CISCO-STACK-MIB", "portJumboFramePortIndex"),
        ("CISCO-STACK-MIB", "portJumboFrameEnable"))
)
if mibBuilder.loadTexts:
    portJumboFrameGroup.setStatus("current")

portCpbGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 54)
)
portCpbGroup4.setObjects(
      *(("CISCO-STACK-MIB", "portCpbCosRewrite"),
        ("CISCO-STACK-MIB", "portCpbTosRewrite"),
        ("CISCO-STACK-MIB", "portCpbCopsGrouping"))
)
if mibBuilder.loadTexts:
    portCpbGroup4.setStatus("current")

fileCopyGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 55)
)
fileCopyGroup2.setObjects(
    ("CISCO-STACK-MIB", "fileCopyRuntimeConfigPart")
)
if mibBuilder.loadTexts:
    fileCopyGroup2.setStatus("current")

systemRmonGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 56)
)
systemRmonGroup2.setObjects(
    ("CISCO-STACK-MIB", "sysMaxRmonMemory")
)
if mibBuilder.loadTexts:
    systemRmonGroup2.setStatus("current")

filterGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 57)
)
filterGroup2.setObjects(
    ("CISCO-STACK-MIB", "filterPortSuppressionOption")
)
if mibBuilder.loadTexts:
    filterGroup2.setStatus("current")

optionalSystemMiscGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 58)
)
optionalSystemMiscGroup5.setObjects(
      *(("CISCO-STACK-MIB", "sysMacReductionAdminEnable"),
        ("CISCO-STACK-MIB", "sysMacReductionOperEnable"))
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup5.setStatus("current")

syslogGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 59)
)
syslogGroup2.setObjects(
    ("CISCO-STACK-MIB", "syslogTelnetEnable")
)
if mibBuilder.loadTexts:
    syslogGroup2.setStatus("current")

systemStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 60)
)
systemStatusGroup.setObjects(
    ("CISCO-STACK-MIB", "sysStatus")
)
if mibBuilder.loadTexts:
    systemStatusGroup.setStatus("current")

configurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 61)
)
configurationGroup.setObjects(
      *(("CISCO-STACK-MIB", "configMode"),
        ("CISCO-STACK-MIB", "configTextFileLocation"),
        ("CISCO-STACK-MIB", "configWriteMem"),
        ("CISCO-STACK-MIB", "configWriteMemStatus"))
)
if mibBuilder.loadTexts:
    configurationGroup.setStatus("current")

filterGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 62)
)
filterGroup3.setObjects(
    ("CISCO-STACK-MIB", "filterPortSuppressionViolation")
)
if mibBuilder.loadTexts:
    filterGroup3.setStatus("current")

portGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 63)
)
portGroup3.setObjects(
    ("CISCO-STACK-MIB", "portErrDisableTimeOutEnable")
)
if mibBuilder.loadTexts:
    portGroup3.setStatus("current")

portCpbGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 64)
)
portCpbGroup5.setObjects(
      *(("CISCO-STACK-MIB", "portCpbDot1x"),
        ("CISCO-STACK-MIB", "portCpbIgmpFilter"))
)
if mibBuilder.loadTexts:
    portCpbGroup5.setStatus("current")

authenticationGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 65)
)
authenticationGroup1.setObjects(
      *(("CISCO-STACK-MIB", "tacacsDirectedRequest"),
        ("CISCO-STACK-MIB", "tacacsAuthKey"),
        ("CISCO-STACK-MIB", "tacacsServerAddr"),
        ("CISCO-STACK-MIB", "tacacsServerType"),
        ("CISCO-STACK-MIB", "radiusDeadtime"),
        ("CISCO-STACK-MIB", "radiusAuthKey"),
        ("CISCO-STACK-MIB", "radiusTimeout"),
        ("CISCO-STACK-MIB", "radiusRetransmits"),
        ("CISCO-STACK-MIB", "radiusServerAddr"),
        ("CISCO-STACK-MIB", "radiusServerAuthPort"),
        ("CISCO-STACK-MIB", "radiusServerType"))
)
if mibBuilder.loadTexts:
    authenticationGroup1.setStatus("deprecated")

systemMiscGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 66)
)
systemMiscGroup1.setObjects(
      *(("CISCO-STACK-MIB", "sysMgmtType"),
        ("CISCO-STACK-MIB", "sysAttachType"),
        ("CISCO-STACK-MIB", "sysBaudRate"),
        ("CISCO-STACK-MIB", "sysInsertMode"),
        ("CISCO-STACK-MIB", "sysEnableModem"),
        ("CISCO-STACK-MIB", "sysEnableRedirects"),
        ("CISCO-STACK-MIB", "sysArpAgingTime"),
        ("CISCO-STACK-MIB", "sysCommunityRwa"),
        ("CISCO-STACK-MIB", "sysCommunityRw"),
        ("CISCO-STACK-MIB", "sysCommunityRo"),
        ("CISCO-STACK-MIB", "sysIpVlan"))
)
if mibBuilder.loadTexts:
    systemMiscGroup1.setStatus("current")

systemTrapGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 67)
)
systemTrapGroup1.setObjects(
      *(("CISCO-STACK-MIB", "sysEnableChassisTraps"),
        ("CISCO-STACK-MIB", "sysEnableModuleTraps"),
        ("CISCO-STACK-MIB", "sysEnableBridgeTraps"),
        ("CISCO-STACK-MIB", "sysEnableRepeaterTraps"))
)
if mibBuilder.loadTexts:
    systemTrapGroup1.setStatus("deprecated")

optionalSystemMiscGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 68)
)
optionalSystemMiscGroup6.setObjects(
      *(("CISCO-STACK-MIB", "sysErrDisableTimeoutEnable"),
        ("CISCO-STACK-MIB", "sysErrDisableTimeoutInterval"),
        ("CISCO-STACK-MIB", "sysTrafficMonitorHighWaterMark"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityEnable"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityVersioningEnable"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityOperStatus"),
        ("CISCO-STACK-MIB", "sysHighAvailabilityNotRunningReason"))
)
if mibBuilder.loadTexts:
    optionalSystemMiscGroup6.setStatus("current")

optionalChassisGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 69)
)
optionalChassisGroup1.setObjects(
      *(("CISCO-STACK-MIB", "chassisPs1TestResult"),
        ("CISCO-STACK-MIB", "chassisPs2TestResult"),
        ("CISCO-STACK-MIB", "chassisFanTestResult"),
        ("CISCO-STACK-MIB", "chassisSlotConfig"),
        ("CISCO-STACK-MIB", "chassisModel"))
)
if mibBuilder.loadTexts:
    optionalChassisGroup1.setStatus("current")

portGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 70)
)
portGroup4.setObjects(
      *(("CISCO-STACK-MIB", "portModuleIndex"),
        ("CISCO-STACK-MIB", "portIndex"),
        ("CISCO-STACK-MIB", "portCrossIndex"),
        ("CISCO-STACK-MIB", "portName"),
        ("CISCO-STACK-MIB", "portType"),
        ("CISCO-STACK-MIB", "portOperStatus"),
        ("CISCO-STACK-MIB", "portCrossGroupIndex"),
        ("CISCO-STACK-MIB", "portAdditionalStatus"),
        ("CISCO-STACK-MIB", "portAdminSpeed"),
        ("CISCO-STACK-MIB", "portDuplex"),
        ("CISCO-STACK-MIB", "portIfIndex"),
        ("CISCO-STACK-MIB", "portAdminRxFlowControl"),
        ("CISCO-STACK-MIB", "portOperRxFlowControl"),
        ("CISCO-STACK-MIB", "portAdminTxFlowControl"),
        ("CISCO-STACK-MIB", "portOperTxFlowControl"),
        ("CISCO-STACK-MIB", "portMacControlTransmitFrames"),
        ("CISCO-STACK-MIB", "portMacControlReceiveFrames"),
        ("CISCO-STACK-MIB", "portMacControlPauseTransmitFrames"),
        ("CISCO-STACK-MIB", "portMacControlPauseReceiveFrames"),
        ("CISCO-STACK-MIB", "portMacControlUnknownProtocolFrames"),
        ("CISCO-STACK-MIB", "portLinkFaultStatus"))
)
if mibBuilder.loadTexts:
    portGroup4.setStatus("current")

vlanGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 71)
)
vlanGroup2.setObjects(
      *(("CISCO-STACK-MIB", "vlanPortModule"),
        ("CISCO-STACK-MIB", "vlanPort"),
        ("CISCO-STACK-MIB", "vlanPortVlan"),
        ("CISCO-STACK-MIB", "vlanPortIslVlansAllowed"),
        ("CISCO-STACK-MIB", "vlanPortSwitchLevel"),
        ("CISCO-STACK-MIB", "vlanPortIslAdminStatus"),
        ("CISCO-STACK-MIB", "vlanPortIslOperStatus"),
        ("CISCO-STACK-MIB", "vlanPortIslPriorityVlans"),
        ("CISCO-STACK-MIB", "vlanPortAdminStatus"),
        ("CISCO-STACK-MIB", "vlanPortOperStatus"))
)
if mibBuilder.loadTexts:
    vlanGroup2.setStatus("current")

ipPermitGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 72)
)
ipPermitGroup2.setObjects(
      *(("CISCO-STACK-MIB", "ipPermitAddress"),
        ("CISCO-STACK-MIB", "ipPermitMask"),
        ("CISCO-STACK-MIB", "ipPermitType"),
        ("CISCO-STACK-MIB", "ipPermitDeniedAddress"),
        ("CISCO-STACK-MIB", "ipPermitDeniedAccess"),
        ("CISCO-STACK-MIB", "ipPermitDeniedTime"),
        ("CISCO-STACK-MIB", "ipPermitAccessTypeEnable"))
)
if mibBuilder.loadTexts:
    ipPermitGroup2.setStatus("current")

optionalPortGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 73)
)
optionalPortGroup1.setObjects(
      *(("CISCO-STACK-MIB", "portSecurityModuleIndex"),
        ("CISCO-STACK-MIB", "portSecurityPortIndex"),
        ("CISCO-STACK-MIB", "portSecurityAdminStatus"),
        ("CISCO-STACK-MIB", "portSecurityOperStatus"),
        ("CISCO-STACK-MIB", "portSecurityLastSrcAddr"),
        ("CISCO-STACK-MIB", "portSecuritySecureSrcAddr"),
        ("CISCO-STACK-MIB", "portCpbModuleIndex"),
        ("CISCO-STACK-MIB", "portCpbPortIndex"),
        ("CISCO-STACK-MIB", "portCpbSpeed"),
        ("CISCO-STACK-MIB", "portCpbDuplex"),
        ("CISCO-STACK-MIB", "portCpbTrunkEncapsulationType"),
        ("CISCO-STACK-MIB", "portCpbTrunkMode"),
        ("CISCO-STACK-MIB", "portCpbChannel"),
        ("CISCO-STACK-MIB", "portCpbBroadcastSuppression"),
        ("CISCO-STACK-MIB", "portCpbFlowControl"),
        ("CISCO-STACK-MIB", "portCpbSecurity"),
        ("CISCO-STACK-MIB", "portCpbVlanMembership"),
        ("CISCO-STACK-MIB", "portCpbPortfast"),
        ("CISCO-STACK-MIB", "portTopNControlIndex"),
        ("CISCO-STACK-MIB", "portTopNRateBase"),
        ("CISCO-STACK-MIB", "portTopNType"),
        ("CISCO-STACK-MIB", "portTopNMode"),
        ("CISCO-STACK-MIB", "portTopNReportStatus"),
        ("CISCO-STACK-MIB", "portTopNDuration"),
        ("CISCO-STACK-MIB", "portTopNTimeRemaining"),
        ("CISCO-STACK-MIB", "portTopNStartTime"),
        ("CISCO-STACK-MIB", "portTopNRequestedSize"),
        ("CISCO-STACK-MIB", "portTopNGrantedSize"),
        ("CISCO-STACK-MIB", "portTopNOwner"),
        ("CISCO-STACK-MIB", "portTopNStatus"),
        ("CISCO-STACK-MIB", "portTopNIndex"),
        ("CISCO-STACK-MIB", "portTopNModuleNumber"),
        ("CISCO-STACK-MIB", "portTopNPortNumber"),
        ("CISCO-STACK-MIB", "portTopNUtilization"),
        ("CISCO-STACK-MIB", "portTopNIOOctets"),
        ("CISCO-STACK-MIB", "portTopNIOPkts"),
        ("CISCO-STACK-MIB", "portTopNIOBroadcast"),
        ("CISCO-STACK-MIB", "portTopNIOMulticast"),
        ("CISCO-STACK-MIB", "portTopNInErrors"),
        ("CISCO-STACK-MIB", "portTopNBufferOverFlow"))
)
if mibBuilder.loadTexts:
    optionalPortGroup1.setStatus("current")

optionalSystemTrapGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 74)
)
optionalSystemTrapGroup1.setObjects(
      *(("CISCO-STACK-MIB", "sysEnableIpPermitTraps"),
        ("CISCO-STACK-MIB", "sysEnableVmpsTraps"),
        ("CISCO-STACK-MIB", "sysEnableConfigTraps"),
        ("CISCO-STACK-MIB", "sysEnableEntityTrap"))
)
if mibBuilder.loadTexts:
    optionalSystemTrapGroup1.setStatus("current")

authenticationGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 75)
)
authenticationGroup2.setObjects(
      *(("CISCO-STACK-MIB", "tacacsDirectedRequest"),
        ("CISCO-STACK-MIB", "tacacsAuthKey"),
        ("CISCO-STACK-MIB", "tacacsServerAddr"),
        ("CISCO-STACK-MIB", "tacacsServerType"),
        ("CISCO-STACK-MIB", "radiusDeadtime"),
        ("CISCO-STACK-MIB", "radiusAuthKey"),
        ("CISCO-STACK-MIB", "radiusTimeout"),
        ("CISCO-STACK-MIB", "radiusRetransmits"))
)
if mibBuilder.loadTexts:
    authenticationGroup2.setStatus("current")

systemTrapGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 76)
)
systemTrapGroup2.setObjects(
      *(("CISCO-STACK-MIB", "sysEnableChassisTraps"),
        ("CISCO-STACK-MIB", "sysEnableModuleTraps"),
        ("CISCO-STACK-MIB", "sysEnableRepeaterTraps"))
)
if mibBuilder.loadTexts:
    systemTrapGroup2.setStatus("current")

ipPermitGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 78)
)
ipPermitGroup3.setObjects(
      *(("CISCO-STACK-MIB", "ipPermitTelnetConnectLimit"),
        ("CISCO-STACK-MIB", "ipPermitSshConnectLimit"))
)
if mibBuilder.loadTexts:
    ipPermitGroup3.setStatus("current")


# Notification objects

lerAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 1)
)
lerAlarmOn.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibPORTSMTIndex"),
        ("FDDI-SMT73-MIB", "fddimibPORTIndex"))
)
if mibBuilder.loadTexts:
    lerAlarmOn.setStatus(
        "current"
    )

lerAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 2)
)
lerAlarmOff.setObjects(
      *(("FDDI-SMT73-MIB", "fddimibPORTSMTIndex"),
        ("FDDI-SMT73-MIB", "fddimibPORTIndex"))
)
if mibBuilder.loadTexts:
    lerAlarmOff.setStatus(
        "current"
    )

moduleUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 3)
)
moduleUp.setObjects(
      *(("CISCO-STACK-MIB", "moduleIndex"),
        ("CISCO-STACK-MIB", "moduleType"))
)
if mibBuilder.loadTexts:
    moduleUp.setStatus(
        "current"
    )

moduleDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 4)
)
moduleDown.setObjects(
      *(("CISCO-STACK-MIB", "moduleIndex"),
        ("CISCO-STACK-MIB", "moduleType"))
)
if mibBuilder.loadTexts:
    moduleDown.setStatus(
        "current"
    )

chassisAlarmOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 5)
)
chassisAlarmOn.setObjects(
      *(("CISCO-STACK-MIB", "chassisTempAlarm"),
        ("CISCO-STACK-MIB", "chassisMinorAlarm"),
        ("CISCO-STACK-MIB", "chassisMajorAlarm"))
)
if mibBuilder.loadTexts:
    chassisAlarmOn.setStatus(
        "current"
    )

chassisAlarmOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 6)
)
chassisAlarmOff.setObjects(
      *(("CISCO-STACK-MIB", "chassisTempAlarm"),
        ("CISCO-STACK-MIB", "chassisMinorAlarm"),
        ("CISCO-STACK-MIB", "chassisMajorAlarm"))
)
if mibBuilder.loadTexts:
    chassisAlarmOff.setStatus(
        "current"
    )

ipPermitDeniedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 7)
)
ipPermitDeniedTrap.setObjects(
      *(("CISCO-STACK-MIB", "ipPermitDeniedAddress"),
        ("CISCO-STACK-MIB", "ipPermitDeniedAccess"))
)
if mibBuilder.loadTexts:
    ipPermitDeniedTrap.setStatus(
        "current"
    )

sysConfigChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 9)
)
sysConfigChangeTrap.setObjects(
      *(("CISCO-STACK-MIB", "sysConfigChangeTime"),
        ("CISCO-STACK-MIB", "sysConfigChangeInfo"))
)
if mibBuilder.loadTexts:
    sysConfigChangeTrap.setStatus(
        "current"
    )

tokenRingSoftErrExceededTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 5, 0, 10)
)
tokenRingSoftErrExceededTrap.setObjects(
      *(("TOKEN-RING-RMON-MIB", "ringStationMacAddress"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    tokenRingSoftErrExceededTrap.setStatus(
        "current"
    )


# Notifications groups

notificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 2, 77)
)
notificationGroup.setObjects(
      *(("CISCO-STACK-MIB", "lerAlarmOn"),
        ("CISCO-STACK-MIB", "lerAlarmOff"),
        ("CISCO-STACK-MIB", "moduleUp"),
        ("CISCO-STACK-MIB", "moduleDown"),
        ("CISCO-STACK-MIB", "chassisAlarmOn"),
        ("CISCO-STACK-MIB", "chassisAlarmOff"),
        ("CISCO-STACK-MIB", "ipPermitDeniedTrap"),
        ("CISCO-STACK-MIB", "sysConfigChangeTrap"),
        ("CISCO-STACK-MIB", "tokenRingSoftErrExceededTrap"))
)
if mibBuilder.loadTexts:
    notificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoStackgMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance2.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance3.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance4.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance5.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance6.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance7.setStatus(
        "deprecated"
    )

ciscoStackgMIBCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 5, 1, 31, 1, 8)
)
if mibBuilder.loadTexts:
    ciscoStackgMIBCompliance8.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-STACK-MIB",
    **{"VendorIdType": VendorIdType,
       "ciscoStackNotificationsPrefix": ciscoStackNotificationsPrefix,
       "lerAlarmOn": lerAlarmOn,
       "lerAlarmOff": lerAlarmOff,
       "moduleUp": moduleUp,
       "moduleDown": moduleDown,
       "chassisAlarmOn": chassisAlarmOn,
       "chassisAlarmOff": chassisAlarmOff,
       "ipPermitDeniedTrap": ipPermitDeniedTrap,
       "sysConfigChangeTrap": sysConfigChangeTrap,
       "tokenRingSoftErrExceededTrap": tokenRingSoftErrExceededTrap,
       "ciscoStackMIB": ciscoStackMIB,
       "systemGrp": systemGrp,
       "sysMgmtType": sysMgmtType,
       "sysIpAddr": sysIpAddr,
       "sysNetMask": sysNetMask,
       "sysBroadcast": sysBroadcast,
       "sysTrapReceiverTable": sysTrapReceiverTable,
       "sysTrapReceiverEntry": sysTrapReceiverEntry,
       "sysTrapReceiverType": sysTrapReceiverType,
       "sysTrapReceiverAddr": sysTrapReceiverAddr,
       "sysTrapReceiverComm": sysTrapReceiverComm,
       "sysCommunityTable": sysCommunityTable,
       "sysCommunityEntry": sysCommunityEntry,
       "sysCommunityAccess": sysCommunityAccess,
       "sysCommunityString": sysCommunityString,
       "sysAttachType": sysAttachType,
       "sysTraffic": sysTraffic,
       "sysReset": sysReset,
       "sysBaudRate": sysBaudRate,
       "sysInsertMode": sysInsertMode,
       "sysClearMacTime": sysClearMacTime,
       "sysClearPortTime": sysClearPortTime,
       "sysFddiRingTable": sysFddiRingTable,
       "sysFddiRingEntry": sysFddiRingEntry,
       "sysFddiRingSMTIndex": sysFddiRingSMTIndex,
       "sysFddiRingAddress": sysFddiRingAddress,
       "sysFddiRingNext": sysFddiRingNext,
       "sysEnableModem": sysEnableModem,
       "sysEnableRedirects": sysEnableRedirects,
       "sysEnableRmon": sysEnableRmon,
       "sysArpAgingTime": sysArpAgingTime,
       "sysTrafficPeak": sysTrafficPeak,
       "sysTrafficPeakTime": sysTrafficPeakTime,
       "sysCommunityRwa": sysCommunityRwa,
       "sysCommunityRw": sysCommunityRw,
       "sysCommunityRo": sysCommunityRo,
       "sysEnableChassisTraps": sysEnableChassisTraps,
       "sysEnableModuleTraps": sysEnableModuleTraps,
       "sysEnableBridgeTraps": sysEnableBridgeTraps,
       "sysIpVlan": sysIpVlan,
       "sysConfigChangeTime": sysConfigChangeTime,
       "sysEnableRepeaterTraps": sysEnableRepeaterTraps,
       "sysBannerMotd": sysBannerMotd,
       "sysEnableIpPermitTraps": sysEnableIpPermitTraps,
       "sysTrafficMeterTable": sysTrafficMeterTable,
       "sysTrafficMeterEntry": sysTrafficMeterEntry,
       "sysTrafficMeterType": sysTrafficMeterType,
       "sysTrafficMeter": sysTrafficMeter,
       "sysTrafficMeterPeak": sysTrafficMeterPeak,
       "sysTrafficMeterPeakTime": sysTrafficMeterPeakTime,
       "sysEnableVmpsTraps": sysEnableVmpsTraps,
       "sysConfigChangeInfo": sysConfigChangeInfo,
       "sysEnableConfigTraps": sysEnableConfigTraps,
       "sysConfigRegister": sysConfigRegister,
       "sysBootVariable": sysBootVariable,
       "sysBootedImage": sysBootedImage,
       "sysEnableEntityTrap": sysEnableEntityTrap,
       "sysEnableStpxTrap": sysEnableStpxTrap,
       "sysExtendedRmonVlanModeEnable": sysExtendedRmonVlanModeEnable,
       "sysExtendedRmonNetflowPassword": sysExtendedRmonNetflowPassword,
       "sysExtendedRmonNetflowEnable": sysExtendedRmonNetflowEnable,
       "sysExtendedRmonVlanAgentEnable": sysExtendedRmonVlanAgentEnable,
       "sysExtendedRmonEnable": sysExtendedRmonEnable,
       "sysConsolePrimaryLoginAuthentication": sysConsolePrimaryLoginAuthentication,
       "sysConsolePrimaryEnableAuthentication": sysConsolePrimaryEnableAuthentication,
       "sysTelnetPrimaryLoginAuthentication": sysTelnetPrimaryLoginAuthentication,
       "sysTelnetPrimaryEnableAuthentication": sysTelnetPrimaryEnableAuthentication,
       "sysStartupConfigSource": sysStartupConfigSource,
       "sysStartupConfigSourceFile": sysStartupConfigSourceFile,
       "sysConfigSupervisorModuleNo": sysConfigSupervisorModuleNo,
       "sysStandbyPortEnable": sysStandbyPortEnable,
       "sysPortFastBpduGuard": sysPortFastBpduGuard,
       "sysErrDisableTimeoutEnable": sysErrDisableTimeoutEnable,
       "sysErrDisableTimeoutInterval": sysErrDisableTimeoutInterval,
       "sysTrafficMonitorHighWaterMark": sysTrafficMonitorHighWaterMark,
       "sysHighAvailabilityEnable": sysHighAvailabilityEnable,
       "sysHighAvailabilityVersioningEnable": sysHighAvailabilityVersioningEnable,
       "sysHighAvailabilityOperStatus": sysHighAvailabilityOperStatus,
       "sysHighAvailabilityNotRunningReason": sysHighAvailabilityNotRunningReason,
       "sysExtendedRmonNetflowModuleMask": sysExtendedRmonNetflowModuleMask,
       "sshPublicKeySize": sshPublicKeySize,
       "sysMaxRmonMemory": sysMaxRmonMemory,
       "sysMacReductionAdminEnable": sysMacReductionAdminEnable,
       "sysMacReductionOperEnable": sysMacReductionOperEnable,
       "sysStatus": sysStatus,
       "chassisGrp": chassisGrp,
       "chassisSysType": chassisSysType,
       "chassisBkplType": chassisBkplType,
       "chassisPs1Type": chassisPs1Type,
       "chassisPs1Status": chassisPs1Status,
       "chassisPs1TestResult": chassisPs1TestResult,
       "chassisPs2Type": chassisPs2Type,
       "chassisPs2Status": chassisPs2Status,
       "chassisPs2TestResult": chassisPs2TestResult,
       "chassisFanStatus": chassisFanStatus,
       "chassisFanTestResult": chassisFanTestResult,
       "chassisMinorAlarm": chassisMinorAlarm,
       "chassisMajorAlarm": chassisMajorAlarm,
       "chassisTempAlarm": chassisTempAlarm,
       "chassisNumSlots": chassisNumSlots,
       "chassisSlotConfig": chassisSlotConfig,
       "chassisModel": chassisModel,
       "chassisSerialNumber": chassisSerialNumber,
       "chassisComponentTable": chassisComponentTable,
       "chassisComponentEntry": chassisComponentEntry,
       "chassisComponentIndex": chassisComponentIndex,
       "chassisComponentType": chassisComponentType,
       "chassisComponentSerialNumber": chassisComponentSerialNumber,
       "chassisComponentHwVersion": chassisComponentHwVersion,
       "chassisComponentModel": chassisComponentModel,
       "chassisSerialNumberString": chassisSerialNumberString,
       "chassisPs3Type": chassisPs3Type,
       "chassisPs3Status": chassisPs3Status,
       "chassisPs3TestResult": chassisPs3TestResult,
       "chassisPEMInstalled": chassisPEMInstalled,
       "moduleGrp": moduleGrp,
       "moduleTable": moduleTable,
       "moduleEntry": moduleEntry,
       "moduleIndex": moduleIndex,
       "moduleType": moduleType,
       "moduleSerialNumber": moduleSerialNumber,
       "moduleHwHiVersion": moduleHwHiVersion,
       "moduleHwLoVersion": moduleHwLoVersion,
       "moduleFwHiVersion": moduleFwHiVersion,
       "moduleFwLoVersion": moduleFwLoVersion,
       "moduleSwHiVersion": moduleSwHiVersion,
       "moduleSwLoVersion": moduleSwLoVersion,
       "moduleStatus": moduleStatus,
       "moduleTestResult": moduleTestResult,
       "moduleAction": moduleAction,
       "moduleName": moduleName,
       "moduleNumPorts": moduleNumPorts,
       "modulePortStatus": modulePortStatus,
       "moduleSubType": moduleSubType,
       "moduleModel": moduleModel,
       "moduleHwVersion": moduleHwVersion,
       "moduleFwVersion": moduleFwVersion,
       "moduleSwVersion": moduleSwVersion,
       "moduleStandbyStatus": moduleStandbyStatus,
       "moduleIPAddress": moduleIPAddress,
       "moduleIPAddressVlan": moduleIPAddressVlan,
       "moduleSubType2": moduleSubType2,
       "moduleSlotNum": moduleSlotNum,
       "moduleSerialNumberString": moduleSerialNumberString,
       "moduleEntPhysicalIndex": moduleEntPhysicalIndex,
       "moduleAdditionalStatus": moduleAdditionalStatus,
       "portGrp": portGrp,
       "portTable": portTable,
       "portEntry": portEntry,
       "portModuleIndex": portModuleIndex,
       "portIndex": portIndex,
       "portCrossIndex": portCrossIndex,
       "portName": portName,
       "portType": portType,
       "portOperStatus": portOperStatus,
       "portCrossGroupIndex": portCrossGroupIndex,
       "portAdditionalStatus": portAdditionalStatus,
       "portAdminSpeed": portAdminSpeed,
       "portDuplex": portDuplex,
       "portIfIndex": portIfIndex,
       "portSpantreeFastStart": portSpantreeFastStart,
       "portAdminRxFlowControl": portAdminRxFlowControl,
       "portOperRxFlowControl": portOperRxFlowControl,
       "portAdminTxFlowControl": portAdminTxFlowControl,
       "portOperTxFlowControl": portOperTxFlowControl,
       "portMacControlTransmitFrames": portMacControlTransmitFrames,
       "portMacControlReceiveFrames": portMacControlReceiveFrames,
       "portMacControlPauseTransmitFrames": portMacControlPauseTransmitFrames,
       "portMacControlPauseReceiveFrames": portMacControlPauseReceiveFrames,
       "portMacControlUnknownProtocolFrames": portMacControlUnknownProtocolFrames,
       "portLinkFaultStatus": portLinkFaultStatus,
       "portAdditionalOperStatus": portAdditionalOperStatus,
       "portInlinePowerDetect": portInlinePowerDetect,
       "portEntPhysicalIndex": portEntPhysicalIndex,
       "portErrDisableTimeOutEnable": portErrDisableTimeOutEnable,
       "tftpGrp": tftpGrp,
       "tftpHost": tftpHost,
       "tftpFile": tftpFile,
       "tftpModule": tftpModule,
       "tftpAction": tftpAction,
       "tftpResult": tftpResult,
       "brouterGrp": brouterGrp,
       "brouterEnableRip": brouterEnableRip,
       "brouterEnableSpantree": brouterEnableSpantree,
       "brouterEnableGiantCheck": brouterEnableGiantCheck,
       "brouterEnableIpFragmentation": brouterEnableIpFragmentation,
       "brouterEnableUnreachables": brouterEnableUnreachables,
       "brouterCamAgingTime": brouterCamAgingTime,
       "brouterCamMode": brouterCamMode,
       "brouterIpxSnapToEther": brouterIpxSnapToEther,
       "brouterIpx8023RawToFddi": brouterIpx8023RawToFddi,
       "brouterEthernetReceiveMax": brouterEthernetReceiveMax,
       "brouterEthernetTransmitMax": brouterEthernetTransmitMax,
       "brouterFddiReceiveMax": brouterFddiReceiveMax,
       "brouterFddiTransmitMax": brouterFddiTransmitMax,
       "brouterPortTable": brouterPortTable,
       "brouterPortEntry": brouterPortEntry,
       "brouterPortModule": brouterPortModule,
       "brouterPort": brouterPort,
       "brouterPortIpVlan": brouterPortIpVlan,
       "brouterPortIpAddr": brouterPortIpAddr,
       "brouterPortNetMask": brouterPortNetMask,
       "brouterPortBroadcast": brouterPortBroadcast,
       "brouterPortBridgeVlan": brouterPortBridgeVlan,
       "brouterPortIpHelpers": brouterPortIpHelpers,
       "brouterIpx8022ToEther": brouterIpx8022ToEther,
       "brouterEnableTransitEncapsulation": brouterEnableTransitEncapsulation,
       "brouterEnableFddiCheck": brouterEnableFddiCheck,
       "brouterEnableAPaRT": brouterEnableAPaRT,
       "filterGrp": filterGrp,
       "filterMacTable": filterMacTable,
       "filterMacEntry": filterMacEntry,
       "filterMacModule": filterMacModule,
       "filterMacPort": filterMacPort,
       "filterMacAddress": filterMacAddress,
       "filterMacType": filterMacType,
       "filterVendorTable": filterVendorTable,
       "filterVendorEntry": filterVendorEntry,
       "filterVendorModule": filterVendorModule,
       "filterVendorPort": filterVendorPort,
       "filterVendorId": filterVendorId,
       "filterVendorType": filterVendorType,
       "filterProtocolTable": filterProtocolTable,
       "filterProtocolEntry": filterProtocolEntry,
       "filterProtocolModule": filterProtocolModule,
       "filterProtocolPort": filterProtocolPort,
       "filterProtocolValue": filterProtocolValue,
       "filterProtocolType": filterProtocolType,
       "filterTestTable": filterTestTable,
       "filterTestEntry": filterTestEntry,
       "filterTestModule": filterTestModule,
       "filterTestPort": filterTestPort,
       "filterTestIndex": filterTestIndex,
       "filterTestType": filterTestType,
       "filterTestOffset": filterTestOffset,
       "filterTestValue": filterTestValue,
       "filterTestMask": filterTestMask,
       "filterPortTable": filterPortTable,
       "filterPortEntry": filterPortEntry,
       "filterPortModule": filterPortModule,
       "filterPort": filterPort,
       "filterPortComplex": filterPortComplex,
       "filterPortBroadcastThrottle": filterPortBroadcastThrottle,
       "filterPortBroadcastThreshold": filterPortBroadcastThreshold,
       "filterPortBroadcastDiscards": filterPortBroadcastDiscards,
       "filterPortBroadcastThresholdFraction": filterPortBroadcastThresholdFraction,
       "filterPortSuppressionOption": filterPortSuppressionOption,
       "filterPortSuppressionViolation": filterPortSuppressionViolation,
       "monitorGrp": monitorGrp,
       "monitorSourceModule": monitorSourceModule,
       "monitorSourcePort": monitorSourcePort,
       "monitorDestinationModule": monitorDestinationModule,
       "monitorDestinationPort": monitorDestinationPort,
       "monitorDirection": monitorDirection,
       "monitorEnable": monitorEnable,
       "monitorAdminSourcePorts": monitorAdminSourcePorts,
       "monitorOperSourcePorts": monitorOperSourcePorts,
       "vlanGrp": vlanGrp,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanSpantreeEnable": vlanSpantreeEnable,
       "vlanIfIndex": vlanIfIndex,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortModule": vlanPortModule,
       "vlanPort": vlanPort,
       "vlanPortVlan": vlanPortVlan,
       "vlanPortIslVlansAllowed": vlanPortIslVlansAllowed,
       "vlanPortSwitchLevel": vlanPortSwitchLevel,
       "vlanPortIslAdminStatus": vlanPortIslAdminStatus,
       "vlanPortIslOperStatus": vlanPortIslOperStatus,
       "vlanPortIslPriorityVlans": vlanPortIslPriorityVlans,
       "vlanPortAdminStatus": vlanPortAdminStatus,
       "vlanPortOperStatus": vlanPortOperStatus,
       "vlanPortAuxiliaryVlan": vlanPortAuxiliaryVlan,
       "vmpsTable": vmpsTable,
       "vmpsEntry": vmpsEntry,
       "vmpsAddr": vmpsAddr,
       "vmpsType": vmpsType,
       "vmpsAction": vmpsAction,
       "vmpsAccessed": vmpsAccessed,
       "vlanTrunkMappingMax": vlanTrunkMappingMax,
       "vlanTrunkMappingTable": vlanTrunkMappingTable,
       "vlanTrunkMappingEntry": vlanTrunkMappingEntry,
       "vlanTrunkMappingFromVlan": vlanTrunkMappingFromVlan,
       "vlanTrunkMappingToVlan": vlanTrunkMappingToVlan,
       "vlanTrunkMappingType": vlanTrunkMappingType,
       "vlanTrunkMappingOper": vlanTrunkMappingOper,
       "vlanTrunkMappingStatus": vlanTrunkMappingStatus,
       "securityGrp": securityGrp,
       "portSecurityTable": portSecurityTable,
       "portSecurityEntry": portSecurityEntry,
       "portSecurityModuleIndex": portSecurityModuleIndex,
       "portSecurityPortIndex": portSecurityPortIndex,
       "portSecurityAdminStatus": portSecurityAdminStatus,
       "portSecurityOperStatus": portSecurityOperStatus,
       "portSecurityLastSrcAddr": portSecurityLastSrcAddr,
       "portSecuritySecureSrcAddr": portSecuritySecureSrcAddr,
       "portSecurityMaxSrcAddr": portSecurityMaxSrcAddr,
       "portSecurityAgingTime": portSecurityAgingTime,
       "portSecurityShutdownTimeOut": portSecurityShutdownTimeOut,
       "portSecurityViolationPolicy": portSecurityViolationPolicy,
       "portSecurityExtTable": portSecurityExtTable,
       "portSecurityExtEntry": portSecurityExtEntry,
       "portSecurityExtModuleIndex": portSecurityExtModuleIndex,
       "portSecurityExtPortIndex": portSecurityExtPortIndex,
       "portSecurityExtSecureSrcAddr": portSecurityExtSecureSrcAddr,
       "portSecurityExtControlStatus": portSecurityExtControlStatus,
       "tokenRingGrp": tokenRingGrp,
       "tokenRingPortTable": tokenRingPortTable,
       "tokenRingPortEntry": tokenRingPortEntry,
       "tokenRingModuleIndex": tokenRingModuleIndex,
       "tokenRingPortIndex": tokenRingPortIndex,
       "tokenRingPortSetACbits": tokenRingPortSetACbits,
       "tokenRingPortMode": tokenRingPortMode,
       "tokenRingPortEarlyTokenRel": tokenRingPortEarlyTokenRel,
       "tokenRingPortPriorityThresh": tokenRingPortPriorityThresh,
       "tokenRingPortPriorityMinXmit": tokenRingPortPriorityMinXmit,
       "tokenRingPortCfgLossThresh": tokenRingPortCfgLossThresh,
       "tokenRingPortCfgLossInterval": tokenRingPortCfgLossInterval,
       "tokenRingDripDistCrfMode": tokenRingDripDistCrfMode,
       "tokenRingDripAreReductionMode": tokenRingDripAreReductionMode,
       "tokenRingDripLocalNodeID": tokenRingDripLocalNodeID,
       "tokenRingDripLastRevision": tokenRingDripLastRevision,
       "tokenRingDripLastChangedRevision": tokenRingDripLastChangedRevision,
       "tokenRingDripAdvertsReceived": tokenRingDripAdvertsReceived,
       "tokenRingDripAdvertsTransmitted": tokenRingDripAdvertsTransmitted,
       "tokenRingDripAdvertsProcessed": tokenRingDripAdvertsProcessed,
       "tokenRingDripInputQueueDrops": tokenRingDripInputQueueDrops,
       "tokenRingDripOutputQueueDrops": tokenRingDripOutputQueueDrops,
       "tokenRingDripLocalVlanStatusTable": tokenRingDripLocalVlanStatusTable,
       "tokenRingDripLocalVlanStatusEntry": tokenRingDripLocalVlanStatusEntry,
       "tokenRingDripVlan": tokenRingDripVlan,
       "tokenRingDripLocalPortStatus": tokenRingDripLocalPortStatus,
       "tokenRingDripRemotePortStatus": tokenRingDripRemotePortStatus,
       "tokenRingDripRemotePortConfigured": tokenRingDripRemotePortConfigured,
       "tokenRingDripDistributedCrf": tokenRingDripDistributedCrf,
       "tokenRingDripBackupCrf": tokenRingDripBackupCrf,
       "tokenRingDripOwnerNodeID": tokenRingDripOwnerNodeID,
       "tokenRingPortSoftErrTable": tokenRingPortSoftErrTable,
       "tokenRingPortSoftErrEntry": tokenRingPortSoftErrEntry,
       "tokenRingPortSoftErrThresh": tokenRingPortSoftErrThresh,
       "tokenRingPortSoftErrReportInterval": tokenRingPortSoftErrReportInterval,
       "tokenRingPortSoftErrResetCounters": tokenRingPortSoftErrResetCounters,
       "tokenRingPortSoftErrLastCounterReset": tokenRingPortSoftErrLastCounterReset,
       "tokenRingPortSoftErrEnable": tokenRingPortSoftErrEnable,
       "multicastGrp": multicastGrp,
       "mcastRouterTable": mcastRouterTable,
       "mcastRouterEntry": mcastRouterEntry,
       "mcastRouterModuleIndex": mcastRouterModuleIndex,
       "mcastRouterPortIndex": mcastRouterPortIndex,
       "mcastRouterAdminStatus": mcastRouterAdminStatus,
       "mcastRouterOperStatus": mcastRouterOperStatus,
       "mcastEnableCgmp": mcastEnableCgmp,
       "mcastEnableIgmp": mcastEnableIgmp,
       "mcastEnableRgmp": mcastEnableRgmp,
       "dnsGrp": dnsGrp,
       "dnsEnable": dnsEnable,
       "dnsServerTable": dnsServerTable,
       "dnsServerEntry": dnsServerEntry,
       "dnsServerAddr": dnsServerAddr,
       "dnsServerType": dnsServerType,
       "dnsDomainName": dnsDomainName,
       "syslogGrp": syslogGrp,
       "syslogServerTable": syslogServerTable,
       "syslogServerEntry": syslogServerEntry,
       "syslogServerAddr": syslogServerAddr,
       "syslogServerType": syslogServerType,
       "syslogConsoleEnable": syslogConsoleEnable,
       "syslogHostEnable": syslogHostEnable,
       "syslogMessageControlTable": syslogMessageControlTable,
       "syslogMessageControlEntry": syslogMessageControlEntry,
       "syslogMessageFacility": syslogMessageFacility,
       "syslogMessageSeverity": syslogMessageSeverity,
       "syslogTimeStampOption": syslogTimeStampOption,
       "syslogTelnetEnable": syslogTelnetEnable,
       "ntpGrp": ntpGrp,
       "ntpBcastClient": ntpBcastClient,
       "ntpBcastDelay": ntpBcastDelay,
       "ntpClient": ntpClient,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerAddress": ntpServerAddress,
       "ntpServerType": ntpServerType,
       "ntpServerPublicKey": ntpServerPublicKey,
       "ntpSummertimeStatus": ntpSummertimeStatus,
       "ntpSummerTimezoneName": ntpSummerTimezoneName,
       "ntpTimezoneName": ntpTimezoneName,
       "ntpTimezoneOffsetHour": ntpTimezoneOffsetHour,
       "ntpTimezoneOffsetMinute": ntpTimezoneOffsetMinute,
       "ntpAuthenticationEnable": ntpAuthenticationEnable,
       "ntpAuthenticationTable": ntpAuthenticationTable,
       "ntpAuthenticationEntry": ntpAuthenticationEntry,
       "ntpAuthenticationPublicKey": ntpAuthenticationPublicKey,
       "ntpAuthenticationSecretKey": ntpAuthenticationSecretKey,
       "ntpAuthenticationTrustedMode": ntpAuthenticationTrustedMode,
       "ntpAuthenticationType": ntpAuthenticationType,
       "tacacsGrp": tacacsGrp,
       "tacacsLoginAuthentication": tacacsLoginAuthentication,
       "tacacsEnableAuthentication": tacacsEnableAuthentication,
       "tacacsLocalLoginAuthentication": tacacsLocalLoginAuthentication,
       "tacacsLocalEnableAuthentication": tacacsLocalEnableAuthentication,
       "tacacsNumLoginAttempts": tacacsNumLoginAttempts,
       "tacacsDirectedRequest": tacacsDirectedRequest,
       "tacacsTimeout": tacacsTimeout,
       "tacacsAuthKey": tacacsAuthKey,
       "tacacsServerTable": tacacsServerTable,
       "tacacsServerEntry": tacacsServerEntry,
       "tacacsServerAddr": tacacsServerAddr,
       "tacacsServerType": tacacsServerType,
       "ipPermitListGrp": ipPermitListGrp,
       "ipPermitEnable": ipPermitEnable,
       "ipPermitListTable": ipPermitListTable,
       "ipPermitListEntry": ipPermitListEntry,
       "ipPermitAddress": ipPermitAddress,
       "ipPermitMask": ipPermitMask,
       "ipPermitType": ipPermitType,
       "ipPermitAccessType": ipPermitAccessType,
       "ipPermitTelnetConnectLimit": ipPermitTelnetConnectLimit,
       "ipPermitSshConnectLimit": ipPermitSshConnectLimit,
       "ipPermitDeniedListTable": ipPermitDeniedListTable,
       "ipPermitDeniedListEntry": ipPermitDeniedListEntry,
       "ipPermitDeniedAddress": ipPermitDeniedAddress,
       "ipPermitDeniedAccess": ipPermitDeniedAccess,
       "ipPermitDeniedTime": ipPermitDeniedTime,
       "ipPermitAccessTypeEnable": ipPermitAccessTypeEnable,
       "portChannelGrp": portChannelGrp,
       "portChannelTable": portChannelTable,
       "portChannelEntry": portChannelEntry,
       "portChannelModuleIndex": portChannelModuleIndex,
       "portChannelPortIndex": portChannelPortIndex,
       "portChannelPorts": portChannelPorts,
       "portChannelAdminStatus": portChannelAdminStatus,
       "portChannelOperStatus": portChannelOperStatus,
       "portChannelNeighbourDeviceId": portChannelNeighbourDeviceId,
       "portChannelNeighbourPortId": portChannelNeighbourPortId,
       "portChannelProtInPackets": portChannelProtInPackets,
       "portChannelProtOutPackets": portChannelProtOutPackets,
       "portChannelIfIndex": portChannelIfIndex,
       "portCpbGrp": portCpbGrp,
       "portCpbTable": portCpbTable,
       "portCpbEntry": portCpbEntry,
       "portCpbModuleIndex": portCpbModuleIndex,
       "portCpbPortIndex": portCpbPortIndex,
       "portCpbSpeed": portCpbSpeed,
       "portCpbDuplex": portCpbDuplex,
       "portCpbTrunkEncapsulationType": portCpbTrunkEncapsulationType,
       "portCpbTrunkMode": portCpbTrunkMode,
       "portCpbChannel": portCpbChannel,
       "portCpbBroadcastSuppression": portCpbBroadcastSuppression,
       "portCpbFlowControl": portCpbFlowControl,
       "portCpbSecurity": portCpbSecurity,
       "portCpbVlanMembership": portCpbVlanMembership,
       "portCpbPortfast": portCpbPortfast,
       "portCpbUdld": portCpbUdld,
       "portCpbInlinePower": portCpbInlinePower,
       "portCpbAuxiliaryVlan": portCpbAuxiliaryVlan,
       "portCpbSpan": portCpbSpan,
       "portCpbCosRewrite": portCpbCosRewrite,
       "portCpbTosRewrite": portCpbTosRewrite,
       "portCpbCopsGrouping": portCpbCopsGrouping,
       "portCpbDot1x": portCpbDot1x,
       "portCpbIgmpFilter": portCpbIgmpFilter,
       "portTopNGrp": portTopNGrp,
       "portTopNControlTable": portTopNControlTable,
       "portTopNControlEntry": portTopNControlEntry,
       "portTopNControlIndex": portTopNControlIndex,
       "portTopNRateBase": portTopNRateBase,
       "portTopNType": portTopNType,
       "portTopNMode": portTopNMode,
       "portTopNReportStatus": portTopNReportStatus,
       "portTopNDuration": portTopNDuration,
       "portTopNTimeRemaining": portTopNTimeRemaining,
       "portTopNStartTime": portTopNStartTime,
       "portTopNRequestedSize": portTopNRequestedSize,
       "portTopNGrantedSize": portTopNGrantedSize,
       "portTopNOwner": portTopNOwner,
       "portTopNStatus": portTopNStatus,
       "portTopNTable": portTopNTable,
       "portTopNEntry": portTopNEntry,
       "portTopNIndex": portTopNIndex,
       "portTopNModuleNumber": portTopNModuleNumber,
       "portTopNPortNumber": portTopNPortNumber,
       "portTopNUtilization": portTopNUtilization,
       "portTopNIOOctets": portTopNIOOctets,
       "portTopNIOPkts": portTopNIOPkts,
       "portTopNIOBroadcast": portTopNIOBroadcast,
       "portTopNIOMulticast": portTopNIOMulticast,
       "portTopNInErrors": portTopNInErrors,
       "portTopNBufferOverFlow": portTopNBufferOverFlow,
       "mdgGrp": mdgGrp,
       "mdgGatewayTable": mdgGatewayTable,
       "mdgGatewayEntry": mdgGatewayEntry,
       "mdgGatewayAddr": mdgGatewayAddr,
       "mdgGatewayType": mdgGatewayType,
       "radiusGrp": radiusGrp,
       "radiusLoginAuthentication": radiusLoginAuthentication,
       "radiusEnableAuthentication": radiusEnableAuthentication,
       "radiusDeadtime": radiusDeadtime,
       "radiusAuthKey": radiusAuthKey,
       "radiusTimeout": radiusTimeout,
       "radiusRetransmits": radiusRetransmits,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerAddr": radiusServerAddr,
       "radiusServerAuthPort": radiusServerAuthPort,
       "radiusServerType": radiusServerType,
       "traceRouteGrp": traceRouteGrp,
       "traceRouteMaxQueries": traceRouteMaxQueries,
       "traceRouteQueryTable": traceRouteQueryTable,
       "traceRouteQueryEntry": traceRouteQueryEntry,
       "traceRouteQueryIndex": traceRouteQueryIndex,
       "traceRouteHost": traceRouteHost,
       "traceRouteQueryDNSEnable": traceRouteQueryDNSEnable,
       "traceRouteQueryWaitingTime": traceRouteQueryWaitingTime,
       "traceRouteQueryInitTTL": traceRouteQueryInitTTL,
       "traceRouteQueryMaxTTL": traceRouteQueryMaxTTL,
       "traceRouteQueryUDPPort": traceRouteQueryUDPPort,
       "traceRouteQueryPacketCount": traceRouteQueryPacketCount,
       "traceRouteQueryPacketSize": traceRouteQueryPacketSize,
       "traceRouteQueryTOS": traceRouteQueryTOS,
       "traceRouteQueryResult": traceRouteQueryResult,
       "traceRouteQueryTime": traceRouteQueryTime,
       "traceRouteQueryOwner": traceRouteQueryOwner,
       "traceRouteQueryStatus": traceRouteQueryStatus,
       "traceRouteDataTable": traceRouteDataTable,
       "traceRouteDataEntry": traceRouteDataEntry,
       "traceRouteDataIndex": traceRouteDataIndex,
       "traceRouteDataGatewayName": traceRouteDataGatewayName,
       "traceRouteDataGatewayIp": traceRouteDataGatewayIp,
       "traceRouteDataRtt": traceRouteDataRtt,
       "traceRouteDataHopCount": traceRouteDataHopCount,
       "traceRouteDataErrors": traceRouteDataErrors,
       "fileCopyGrp": fileCopyGrp,
       "fileCopyProtocol": fileCopyProtocol,
       "fileCopyRemoteServer": fileCopyRemoteServer,
       "fileCopySrcFileName": fileCopySrcFileName,
       "fileCopyDstFileName": fileCopyDstFileName,
       "fileCopyModuleNumber": fileCopyModuleNumber,
       "fileCopyUserName": fileCopyUserName,
       "fileCopyAction": fileCopyAction,
       "fileCopyResult": fileCopyResult,
       "fileCopyResultRcpErrorMessage": fileCopyResultRcpErrorMessage,
       "fileCopyRuntimeConfigPart": fileCopyRuntimeConfigPart,
       "voiceGrp": voiceGrp,
       "voicePortIfConfigTable": voicePortIfConfigTable,
       "voicePortIfConfigEntry": voicePortIfConfigEntry,
       "voicePortIfConfigModuleIndex": voicePortIfConfigModuleIndex,
       "voicePortIfConfigPortIndex": voicePortIfConfigPortIndex,
       "voicePortIfDHCPEnabled": voicePortIfDHCPEnabled,
       "voicePortIfIpAddress": voicePortIfIpAddress,
       "voicePortIfIpNetMask": voicePortIfIpNetMask,
       "voicePortIfTftpServerAddress": voicePortIfTftpServerAddress,
       "voicePortIfGatewayAddress": voicePortIfGatewayAddress,
       "voicePortIfDnsServerAddress": voicePortIfDnsServerAddress,
       "voicePortIfDnsDomain": voicePortIfDnsDomain,
       "voicePortIfOperDnsDomain": voicePortIfOperDnsDomain,
       "voicePortCallManagerTable": voicePortCallManagerTable,
       "voicePortCallManagerEntry": voicePortCallManagerEntry,
       "voicePortModuleIndex": voicePortModuleIndex,
       "voicePortIndex": voicePortIndex,
       "voicePortCallManagerIndex": voicePortCallManagerIndex,
       "voicePortCallManagerIpAddr": voicePortCallManagerIpAddr,
       "voicePortOperDnsServerTable": voicePortOperDnsServerTable,
       "voicePortOperDnsServerEntry": voicePortOperDnsServerEntry,
       "voicePortDnsModuleIndex": voicePortDnsModuleIndex,
       "voicePortDnsPortIndex": voicePortDnsPortIndex,
       "voicePortOperDnsServerIndex": voicePortOperDnsServerIndex,
       "voicePortOperDnsServerIpAddr": voicePortOperDnsServerIpAddr,
       "voicePortOperDnsServerSource": voicePortOperDnsServerSource,
       "portJumboFrameGrp": portJumboFrameGrp,
       "portJumboFrameTable": portJumboFrameTable,
       "portJumboFrameEntry": portJumboFrameEntry,
       "portJumboFrameModuleIndex": portJumboFrameModuleIndex,
       "portJumboFramePortIndex": portJumboFramePortIndex,
       "portJumboFrameEnable": portJumboFrameEnable,
       "switchAccelerationGrp": switchAccelerationGrp,
       "switchAccelerationModuleTable": switchAccelerationModuleTable,
       "switchAccelerationModuleEntry": switchAccelerationModuleEntry,
       "switchAccelerationModuleIndex": switchAccelerationModuleIndex,
       "switchAccelerationModuleEnable": switchAccelerationModuleEnable,
       "configGrp": configGrp,
       "configMode": configMode,
       "configTextFileLocation": configTextFileLocation,
       "configWriteMem": configWriteMem,
       "configWriteMemStatus": configWriteMemStatus,
       "ciscoStackMIBConformance": ciscoStackMIBConformance,
       "ciscoStackMIBCompliances": ciscoStackMIBCompliances,
       "ciscoStackgMIBCompliance": ciscoStackgMIBCompliance,
       "ciscoStackgMIBCompliance2": ciscoStackgMIBCompliance2,
       "ciscoStackgMIBCompliance3": ciscoStackgMIBCompliance3,
       "ciscoStackgMIBCompliance4": ciscoStackgMIBCompliance4,
       "ciscoStackgMIBCompliance5": ciscoStackgMIBCompliance5,
       "ciscoStackgMIBCompliance6": ciscoStackgMIBCompliance6,
       "ciscoStackgMIBCompliance7": ciscoStackgMIBCompliance7,
       "ciscoStackgMIBCompliance8": ciscoStackgMIBCompliance8,
       "ciscoStackMIBGroups": ciscoStackMIBGroups,
       "systemMiscGroup": systemMiscGroup,
       "systemTrapGroup": systemTrapGroup,
       "chassisGroup": chassisGroup,
       "moduleGroup": moduleGroup,
       "portGroup": portGroup,
       "optionalSystemMiscGroup": optionalSystemMiscGroup,
       "optionalSystemTrapGroup": optionalSystemTrapGroup,
       "optionalChassisGroup": optionalChassisGroup,
       "optionalModuleGroup": optionalModuleGroup,
       "optionalPortGroup": optionalPortGroup,
       "systemTrafficGroup": systemTrafficGroup,
       "systemFddiGroup": systemFddiGroup,
       "systemRmonGroup": systemRmonGroup,
       "authenticationGroup": authenticationGroup,
       "tftpGroup": tftpGroup,
       "brouteEnableGroup": brouteEnableGroup,
       "filterGroup": filterGroup,
       "monitorGroup": monitorGroup,
       "vlanGroup": vlanGroup,
       "vmpsGroup": vmpsGroup,
       "tokenRingGroup": tokenRingGroup,
       "mcastGroup": mcastGroup,
       "dnsGroup": dnsGroup,
       "syslogGroup": syslogGroup,
       "ntpGroup": ntpGroup,
       "ipPermitGroup": ipPermitGroup,
       "mdgGatewayGroup": mdgGatewayGroup,
       "traceRouteGroup": traceRouteGroup,
       "deprecatedObjectGroup": deprecatedObjectGroup,
       "ntpAuthenticationGroup": ntpAuthenticationGroup,
       "tokenRingSoftErrorMonitorGroup": tokenRingSoftErrorMonitorGroup,
       "portCpbGroup1": portCpbGroup1,
       "portSecurityGroup1": portSecurityGroup1,
       "fileCopyGroup": fileCopyGroup,
       "optionalSystemMiscGroup1": optionalSystemMiscGroup1,
       "ipPermitGroup1": ipPermitGroup1,
       "optionalSystemMiscGroup2": optionalSystemMiscGroup2,
       "filterGroup1": filterGroup1,
       "mcastGroup1": mcastGroup1,
       "portGroup1": portGroup1,
       "chassisGroup1": chassisGroup1,
       "moduleGroup1": moduleGroup1,
       "portCpbGroup2": portCpbGroup2,
       "voiceGroup": voiceGroup,
       "portGroup2": portGroup2,
       "vlanGroup1": vlanGroup1,
       "portCpbGroup3": portCpbGroup3,
       "moduleGroup2": moduleGroup2,
       "switchAccelerationModuleGroup": switchAccelerationModuleGroup,
       "optionalSystemMiscGroup3": optionalSystemMiscGroup3,
       "optionalSystemMiscGroup4": optionalSystemMiscGroup4,
       "vlanTrunkMappingGroup": vlanTrunkMappingGroup,
       "portJumboFrameGroup": portJumboFrameGroup,
       "portCpbGroup4": portCpbGroup4,
       "fileCopyGroup2": fileCopyGroup2,
       "systemRmonGroup2": systemRmonGroup2,
       "filterGroup2": filterGroup2,
       "optionalSystemMiscGroup5": optionalSystemMiscGroup5,
       "syslogGroup2": syslogGroup2,
       "systemStatusGroup": systemStatusGroup,
       "configurationGroup": configurationGroup,
       "filterGroup3": filterGroup3,
       "portGroup3": portGroup3,
       "portCpbGroup5": portCpbGroup5,
       "authenticationGroup1": authenticationGroup1,
       "systemMiscGroup1": systemMiscGroup1,
       "systemTrapGroup1": systemTrapGroup1,
       "optionalSystemMiscGroup6": optionalSystemMiscGroup6,
       "optionalChassisGroup1": optionalChassisGroup1,
       "portGroup4": portGroup4,
       "vlanGroup2": vlanGroup2,
       "ipPermitGroup2": ipPermitGroup2,
       "optionalPortGroup1": optionalPortGroup1,
       "optionalSystemTrapGroup1": optionalSystemTrapGroup1,
       "authenticationGroup2": authenticationGroup2,
       "systemTrapGroup2": systemTrapGroup2,
       "notificationGroup": notificationGroup,
       "ipPermitGroup3": ipPermitGroup3,
       "adapterCard": adapterCard,
       "wsc1000sysID": wsc1000sysID,
       "wsc1100sysID": wsc1100sysID,
       "wsc1200sysID": wsc1200sysID,
       "wsc1400sysID": wsc1400sysID,
       "wsc5000sysID": wsc5000sysID,
       "wsc1600sysID": wsc1600sysID,
       "cpw1600sysID": cpw1600sysID,
       "wsc3000sysID": wsc3000sysID,
       "wsc2900sysID": wsc2900sysID,
       "cpw2200sysID": cpw2200sysID,
       "esStack": esStack,
       "wsc3200sysID": wsc3200sysID,
       "cpw1900sysID": cpw1900sysID,
       "wsc5500sysID": wsc5500sysID,
       "wsc1900sysID": wsc1900sysID,
       "cpw1220sysID": cpw1220sysID,
       "wsc2820sysID": wsc2820sysID,
       "cpw1420sysID": cpw1420sysID,
       "dcd": dcd,
       "wsc3100sysID": wsc3100sysID,
       "cpw1800sysID": cpw1800sysID,
       "cpw1601sysID": cpw1601sysID,
       "wsc3001sysID": wsc3001sysID,
       "cpw1220csysID": cpw1220csysID,
       "wsc1900csysID": wsc1900csysID,
       "wsc5002sysID": wsc5002sysID,
       "cpw1220isysID": cpw1220isysID,
       "wsc1900isysID": wsc1900isysID,
       "tsStack": tsStack,
       "wsc3900sysID": wsc3900sysID,
       "wsc5505sysID": wsc5505sysID,
       "wsc2926sysID": wsc2926sysID,
       "wsc5509sysID": wsc5509sysID,
       "wsc3920sysID": wsc3920sysID,
       "wsc6006sysID": wsc6006sysID,
       "wsc6009sysID": wsc6009sysID,
       "wsc4003sysID": wsc4003sysID,
       "wsc4912gsysID": wsc4912gsysID,
       "wsc2948gsysID": wsc2948gsysID,
       "wsc6509sysID": wsc6509sysID,
       "wsc6506sysID": wsc6506sysID,
       "wsc4006sysID": wsc4006sysID,
       "wsc6509nebsysID": wsc6509nebsysID,
       "wsc6knamsysID": wsc6knamsysID,
       "wsc2980gsysID": wsc2980gsysID,
       "wsc6513sysID": wsc6513sysID,
       "wsc2980gasysID": wsc2980gasysID,
       "cisco7603sysID": cisco7603sysID,
       "cisco7606sysID": cisco7606sysID,
       "cisco7609sysID": cisco7609sysID,
       "wsc6503sysID": wsc6503sysID,
       "wsc4503sysID": wsc4503sysID,
       "wsc4506sysID": wsc4506sysID,
       "cisco7613sysID": cisco7613sysID,
       "wsc6509nebasysID": wsc6509nebasysID,
       "wsc2948ggetxsysID": wsc2948ggetxsysID,
       "cisco7604sysID": cisco7604sysID,
       "wsc6504esysID": wsc6504esysID,
       "wsc1900LiteFxsysID": wsc1900LiteFxsysID}
)
