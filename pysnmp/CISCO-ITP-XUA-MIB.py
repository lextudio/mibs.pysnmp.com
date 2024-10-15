# SNMP MIB module (CISCO-ITP-XUA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ITP-XUA-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:03:39 2024
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

(cItpSpCLLICode,) = mibBuilder.importSymbols(
    "CISCO-ITP-SP-MIB",
    "cItpSpCLLICode")

(CItpTcNetworkName,
 CItpTcPointCode,
 CItpTcQos,
 CItpTcServiceIndicator,
 CItpTcSubSystemNumber,
 CItpTcXuaName) = mibBuilder.importSymbols(
    "CISCO-ITP-TC-MIB",
    "CItpTcNetworkName",
    "CItpTcPointCode",
    "CItpTcQos",
    "CItpTcServiceIndicator",
    "CItpTcSubSystemNumber",
    "CItpTcXuaName")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoItpXuaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253)
)
ciscoItpXuaMIB.setRevisions(
        ("2008-06-09 00:00",
         "2008-05-08 00:00",
         "2008-01-04 00:00",
         "2007-09-06 00:00",
         "2004-06-14 00:00",
         "2003-08-27 00:00",
         "2003-02-19 00:00",
         "2002-04-15 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CItpXuaProtocol(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m3ua", 1),
          ("sgmp", 3),
          ("sua", 2))
    )



class CItpXuaTrafMode(Integer32, TextualConvention):
    status = "current"
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
        *(("broadcast", 4),
          ("loadBind", 2),
          ("loadRndRobin", 3),
          ("overRide", 1),
          ("undefined", 5))
    )



class CItpXuaAsState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("down", 1),
          ("inactive", 2),
          ("pending", 4),
          ("undefined", 5))
    )



class CItpXuaAspState(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("down", 1),
          ("inactive", 2),
          ("undefined", 4))
    )



class CItpXuaRouteState(Integer32, TextualConvention):
    status = "current"
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
        *(("avail", 2),
          ("deleted", 5),
          ("restr", 3),
          ("unavail", 4),
          ("unknown", 1))
    )



class CItpXuaAssocState(Integer32, TextualConvention):
    status = "current"
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
        *(("closed", 2),
          ("established", 3),
          ("failed", 4),
          ("termPend", 5),
          ("undefined", 1))
    )



class CItpXuaRemoteIpDestState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("undefined", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoItpXuaMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoItpXuaMIBNotifs = _CiscoItpXuaMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0)
)
_CiscoItpXuaMIBObjects_ObjectIdentity = ObjectIdentity
ciscoItpXuaMIBObjects = _CiscoItpXuaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1)
)
_CItpXuaScalars_ObjectIdentity = ObjectIdentity
cItpXuaScalars = _CItpXuaScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 1)
)
_CItpXuaInstConfigLastChanged_Type = TimeTicks
_CItpXuaInstConfigLastChanged_Object = MibScalar
cItpXuaInstConfigLastChanged = _CItpXuaInstConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 1, 1),
    _CItpXuaInstConfigLastChanged_Type()
)
cItpXuaInstConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaInstConfigLastChanged.setStatus("current")
_CItpXuaSgmConfigLastChanged_Type = TimeTicks
_CItpXuaSgmConfigLastChanged_Object = MibScalar
cItpXuaSgmConfigLastChanged = _CItpXuaSgmConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 1, 2),
    _CItpXuaSgmConfigLastChanged_Type()
)
cItpXuaSgmConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmConfigLastChanged.setStatus("current")
_CItpXuaAspConfigLastChanged_Type = TimeTicks
_CItpXuaAspConfigLastChanged_Object = MibScalar
cItpXuaAspConfigLastChanged = _CItpXuaAspConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 1, 3),
    _CItpXuaAspConfigLastChanged_Type()
)
cItpXuaAspConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspConfigLastChanged.setStatus("current")
_CItpXuaAsConfigLastChanged_Type = TimeTicks
_CItpXuaAsConfigLastChanged_Object = MibScalar
cItpXuaAsConfigLastChanged = _CItpXuaAsConfigLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 1, 4),
    _CItpXuaAsConfigLastChanged_Type()
)
cItpXuaAsConfigLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsConfigLastChanged.setStatus("current")


class _CItpXuaStateChangeNotifEnabled_Type(TruthValue):
    """Custom type cItpXuaStateChangeNotifEnabled based on TruthValue"""


_CItpXuaStateChangeNotifEnabled_Object = MibScalar
cItpXuaStateChangeNotifEnabled = _CItpXuaStateChangeNotifEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 1, 5),
    _CItpXuaStateChangeNotifEnabled_Type()
)
cItpXuaStateChangeNotifEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cItpXuaStateChangeNotifEnabled.setStatus("current")
_CItpXuaInst_ObjectIdentity = ObjectIdentity
cItpXuaInst = _CItpXuaInst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2)
)
_CItpXuaInstTable_Object = MibTable
cItpXuaInstTable = _CItpXuaInstTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cItpXuaInstTable.setStatus("current")
_CItpXuaInstTableEntry_Object = MibTableRow
cItpXuaInstTableEntry = _CItpXuaInstTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1)
)
cItpXuaInstTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaInstPort"),
)
if mibBuilder.loadTexts:
    cItpXuaInstTableEntry.setStatus("current")
_CItpXuaInstPort_Type = InetPortNumber
_CItpXuaInstPort_Object = MibTableColumn
cItpXuaInstPort = _CItpXuaInstPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 1),
    _CItpXuaInstPort_Type()
)
cItpXuaInstPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaInstPort.setStatus("current")
_CItpXuaInstProtocol_Type = CItpXuaProtocol
_CItpXuaInstProtocol_Object = MibTableColumn
cItpXuaInstProtocol = _CItpXuaInstProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 2),
    _CItpXuaInstProtocol_Type()
)
cItpXuaInstProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstProtocol.setStatus("current")


class _CItpXuaInstShut_Type(TruthValue):
    """Custom type cItpXuaInstShut based on TruthValue"""


_CItpXuaInstShut_Object = MibTableColumn
cItpXuaInstShut = _CItpXuaInstShut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 3),
    _CItpXuaInstShut_Type()
)
cItpXuaInstShut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstShut.setStatus("current")


class _CItpXuaInstActiveASPs_Type(Gauge32):
    """Custom type cItpXuaInstActiveASPs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpXuaInstActiveASPs_Type.__name__ = "Gauge32"
_CItpXuaInstActiveASPs_Object = MibTableColumn
cItpXuaInstActiveASPs = _CItpXuaInstActiveASPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 4),
    _CItpXuaInstActiveASPs_Type()
)
cItpXuaInstActiveASPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaInstActiveASPs.setStatus("current")
_CItpXuaInstRowStatus_Type = RowStatus
_CItpXuaInstRowStatus_Object = MibTableColumn
cItpXuaInstRowStatus = _CItpXuaInstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 5),
    _CItpXuaInstRowStatus_Type()
)
cItpXuaInstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstRowStatus.setStatus("current")


class _CItpXuaInstOffload_Type(TruthValue):
    """Custom type cItpXuaInstOffload based on TruthValue"""


_CItpXuaInstOffload_Object = MibTableColumn
cItpXuaInstOffload = _CItpXuaInstOffload_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 6),
    _CItpXuaInstOffload_Type()
)
cItpXuaInstOffload.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstOffload.setStatus("current")


class _CItpXuaInstOffloadSlot_Type(Unsigned32):
    """Custom type cItpXuaInstOffloadSlot based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_CItpXuaInstOffloadSlot_Type.__name__ = "Unsigned32"
_CItpXuaInstOffloadSlot_Object = MibTableColumn
cItpXuaInstOffloadSlot = _CItpXuaInstOffloadSlot_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 7),
    _CItpXuaInstOffloadSlot_Type()
)
cItpXuaInstOffloadSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstOffloadSlot.setStatus("current")


class _CItpXuaInstOffProcNumber_Type(Unsigned32):
    """Custom type cItpXuaInstOffProcNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CItpXuaInstOffProcNumber_Type.__name__ = "Unsigned32"
_CItpXuaInstOffProcNumber_Object = MibTableColumn
cItpXuaInstOffProcNumber = _CItpXuaInstOffProcNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 2, 1, 1, 8),
    _CItpXuaInstOffProcNumber_Type()
)
cItpXuaInstOffProcNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaInstOffProcNumber.setStatus("current")
_CItpXuaInstLocalIp_ObjectIdentity = ObjectIdentity
cItpXuaInstLocalIp = _CItpXuaInstLocalIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3)
)
_CItpXuaInstLocalIpTable_Object = MibTable
cItpXuaInstLocalIpTable = _CItpXuaInstLocalIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cItpXuaInstLocalIpTable.setStatus("current")
_CItpXuaInstLocalIpTableEntry_Object = MibTableRow
cItpXuaInstLocalIpTableEntry = _CItpXuaInstLocalIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3, 1, 1)
)
cItpXuaInstLocalIpTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaInstPort"),
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaInstAddrNum"),
)
if mibBuilder.loadTexts:
    cItpXuaInstLocalIpTableEntry.setStatus("current")


class _CItpXuaInstAddrNum_Type(Unsigned32):
    """Custom type cItpXuaInstAddrNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CItpXuaInstAddrNum_Type.__name__ = "Unsigned32"
_CItpXuaInstAddrNum_Object = MibTableColumn
cItpXuaInstAddrNum = _CItpXuaInstAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3, 1, 1, 1),
    _CItpXuaInstAddrNum_Type()
)
cItpXuaInstAddrNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaInstAddrNum.setStatus("current")
_CItpXuaInstLocalIpType_Type = InetAddressType
_CItpXuaInstLocalIpType_Object = MibTableColumn
cItpXuaInstLocalIpType = _CItpXuaInstLocalIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3, 1, 1, 2),
    _CItpXuaInstLocalIpType_Type()
)
cItpXuaInstLocalIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstLocalIpType.setStatus("current")
_CItpXuaInstLocalIpAddr_Type = InetAddress
_CItpXuaInstLocalIpAddr_Object = MibTableColumn
cItpXuaInstLocalIpAddr = _CItpXuaInstLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3, 1, 1, 3),
    _CItpXuaInstLocalIpAddr_Type()
)
cItpXuaInstLocalIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstLocalIpAddr.setStatus("current")
_CItpXuaInstLocalIpRowStatus_Type = RowStatus
_CItpXuaInstLocalIpRowStatus_Object = MibTableColumn
cItpXuaInstLocalIpRowStatus = _CItpXuaInstLocalIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 3, 1, 1, 4),
    _CItpXuaInstLocalIpRowStatus_Type()
)
cItpXuaInstLocalIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaInstLocalIpRowStatus.setStatus("current")
_CItpXuaSgm_ObjectIdentity = ObjectIdentity
cItpXuaSgm = _CItpXuaSgm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4)
)
_CItpXuaSgmTable_Object = MibTable
cItpXuaSgmTable = _CItpXuaSgmTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cItpXuaSgmTable.setStatus("current")
_CItpXuaSgmTableEntry_Object = MibTableRow
cItpXuaSgmTableEntry = _CItpXuaSgmTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1)
)
cItpXuaSgmTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaSgmName"),
)
if mibBuilder.loadTexts:
    cItpXuaSgmTableEntry.setStatus("current")
_CItpXuaSgmName_Type = CItpTcXuaName
_CItpXuaSgmName_Object = MibTableColumn
cItpXuaSgmName = _CItpXuaSgmName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 1),
    _CItpXuaSgmName_Type()
)
cItpXuaSgmName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaSgmName.setStatus("current")
_CItpXuaSgmAssocId_Type = Unsigned32
_CItpXuaSgmAssocId_Object = MibTableColumn
cItpXuaSgmAssocId = _CItpXuaSgmAssocId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 2),
    _CItpXuaSgmAssocId_Type()
)
cItpXuaSgmAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmAssocId.setStatus("current")
_CItpXuaSgmLocalPort_Type = InetPortNumber
_CItpXuaSgmLocalPort_Object = MibTableColumn
cItpXuaSgmLocalPort = _CItpXuaSgmLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 3),
    _CItpXuaSgmLocalPort_Type()
)
cItpXuaSgmLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmLocalPort.setStatus("current")
_CItpXuaSgmRemotePort_Type = InetPortNumber
_CItpXuaSgmRemotePort_Object = MibTableColumn
cItpXuaSgmRemotePort = _CItpXuaSgmRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 4),
    _CItpXuaSgmRemotePort_Type()
)
cItpXuaSgmRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmRemotePort.setStatus("current")


class _CItpXuaSgmShut_Type(TruthValue):
    """Custom type cItpXuaSgmShut based on TruthValue"""


_CItpXuaSgmShut_Object = MibTableColumn
cItpXuaSgmShut = _CItpXuaSgmShut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 6),
    _CItpXuaSgmShut_Type()
)
cItpXuaSgmShut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmShut.setStatus("current")
_CItpXuaSgmActiveTS_Type = TimeTicks
_CItpXuaSgmActiveTS_Object = MibTableColumn
cItpXuaSgmActiveTS = _CItpXuaSgmActiveTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 7),
    _CItpXuaSgmActiveTS_Type()
)
cItpXuaSgmActiveTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmActiveTS.setStatus("current")


class _CItpXuaSgmQosClass_Type(CItpTcQos):
    """Custom type cItpXuaSgmQosClass based on CItpTcQos"""
    defaultValue = 0


_CItpXuaSgmQosClass_Object = MibTableColumn
cItpXuaSgmQosClass = _CItpXuaSgmQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 8),
    _CItpXuaSgmQosClass_Type()
)
cItpXuaSgmQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmQosClass.setStatus("current")


class _CItpXuaSgmPassive_Type(TruthValue):
    """Custom type cItpXuaSgmPassive based on TruthValue"""


_CItpXuaSgmPassive_Object = MibTableColumn
cItpXuaSgmPassive = _CItpXuaSgmPassive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 10),
    _CItpXuaSgmPassive_Type()
)
cItpXuaSgmPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmPassive.setStatus("current")
_CItpXuaSgmState_Type = CItpXuaAspState
_CItpXuaSgmState_Object = MibTableColumn
cItpXuaSgmState = _CItpXuaSgmState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 11),
    _CItpXuaSgmState_Type()
)
cItpXuaSgmState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmState.setStatus("current")
_CItpXuaSgmRowStatus_Type = RowStatus
_CItpXuaSgmRowStatus_Object = MibTableColumn
cItpXuaSgmRowStatus = _CItpXuaSgmRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 12),
    _CItpXuaSgmRowStatus_Type()
)
cItpXuaSgmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmRowStatus.setStatus("current")


class _CItpXuaSgmCongLevel_Type(Unsigned32):
    """Custom type cItpXuaSgmCongLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CItpXuaSgmCongLevel_Type.__name__ = "Unsigned32"
_CItpXuaSgmCongLevel_Object = MibTableColumn
cItpXuaSgmCongLevel = _CItpXuaSgmCongLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 13),
    _CItpXuaSgmCongLevel_Type()
)
cItpXuaSgmCongLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmCongLevel.setStatus("current")
_CItpXuaSgmAssocState_Type = CItpXuaAssocState
_CItpXuaSgmAssocState_Object = MibTableColumn
cItpXuaSgmAssocState = _CItpXuaSgmAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 14),
    _CItpXuaSgmAssocState_Type()
)
cItpXuaSgmAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmAssocState.setStatus("current")


class _CItpXuaSgmAssocFailedReason_Type(SnmpAdminString):
    """Custom type cItpXuaSgmAssocFailedReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_CItpXuaSgmAssocFailedReason_Type.__name__ = "SnmpAdminString"
_CItpXuaSgmAssocFailedReason_Object = MibTableColumn
cItpXuaSgmAssocFailedReason = _CItpXuaSgmAssocFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 4, 1, 1, 15),
    _CItpXuaSgmAssocFailedReason_Type()
)
cItpXuaSgmAssocFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmAssocFailedReason.setStatus("current")
_CItpXuaAsp_ObjectIdentity = ObjectIdentity
cItpXuaAsp = _CItpXuaAsp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5)
)
_CItpXuaAspTable_Object = MibTable
cItpXuaAspTable = _CItpXuaAspTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cItpXuaAspTable.setStatus("current")
_CItpXuaAspTableEntry_Object = MibTableRow
cItpXuaAspTableEntry = _CItpXuaAspTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1)
)
cItpXuaAspTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAspName"),
)
if mibBuilder.loadTexts:
    cItpXuaAspTableEntry.setStatus("current")
_CItpXuaAspName_Type = CItpTcXuaName
_CItpXuaAspName_Object = MibTableColumn
cItpXuaAspName = _CItpXuaAspName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 1),
    _CItpXuaAspName_Type()
)
cItpXuaAspName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaAspName.setStatus("current")


class _CItpXuaAspAssocId_Type(Unsigned32):
    """Custom type cItpXuaAspAssocId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpXuaAspAssocId_Type.__name__ = "Unsigned32"
_CItpXuaAspAssocId_Object = MibTableColumn
cItpXuaAspAssocId = _CItpXuaAspAssocId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 2),
    _CItpXuaAspAssocId_Type()
)
cItpXuaAspAssocId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspAssocId.setStatus("deprecated")
_CItpXuaAspLocalPort_Type = InetPortNumber
_CItpXuaAspLocalPort_Object = MibTableColumn
cItpXuaAspLocalPort = _CItpXuaAspLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 3),
    _CItpXuaAspLocalPort_Type()
)
cItpXuaAspLocalPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspLocalPort.setStatus("current")
_CItpXuaAspRemotePort_Type = InetPortNumber
_CItpXuaAspRemotePort_Object = MibTableColumn
cItpXuaAspRemotePort = _CItpXuaAspRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 4),
    _CItpXuaAspRemotePort_Type()
)
cItpXuaAspRemotePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspRemotePort.setStatus("current")
_CItpXuaAspProtocol_Type = CItpXuaProtocol
_CItpXuaAspProtocol_Object = MibTableColumn
cItpXuaAspProtocol = _CItpXuaAspProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 5),
    _CItpXuaAspProtocol_Type()
)
cItpXuaAspProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspProtocol.setStatus("current")


class _CItpXuaAspShut_Type(TruthValue):
    """Custom type cItpXuaAspShut based on TruthValue"""


_CItpXuaAspShut_Object = MibTableColumn
cItpXuaAspShut = _CItpXuaAspShut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 6),
    _CItpXuaAspShut_Type()
)
cItpXuaAspShut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspShut.setStatus("current")


class _CItpXuaAspBlocked_Type(TruthValue):
    """Custom type cItpXuaAspBlocked based on TruthValue"""


_CItpXuaAspBlocked_Object = MibTableColumn
cItpXuaAspBlocked = _CItpXuaAspBlocked_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 7),
    _CItpXuaAspBlocked_Type()
)
cItpXuaAspBlocked.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspBlocked.setStatus("current")


class _CItpXuaAspQosClass_Type(CItpTcQos):
    """Custom type cItpXuaAspQosClass based on CItpTcQos"""
    defaultValue = 0


_CItpXuaAspQosClass_Object = MibTableColumn
cItpXuaAspQosClass = _CItpXuaAspQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 9),
    _CItpXuaAspQosClass_Type()
)
cItpXuaAspQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspQosClass.setStatus("current")


class _CItpXuaAspIdentifier_Type(Unsigned32):
    """Custom type cItpXuaAspIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CItpXuaAspIdentifier_Type.__name__ = "Unsigned32"
_CItpXuaAspIdentifier_Object = MibTableColumn
cItpXuaAspIdentifier = _CItpXuaAspIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 10),
    _CItpXuaAspIdentifier_Type()
)
cItpXuaAspIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspIdentifier.setStatus("current")
_CItpXuaAspRowStatus_Type = RowStatus
_CItpXuaAspRowStatus_Object = MibTableColumn
cItpXuaAspRowStatus = _CItpXuaAspRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 11),
    _CItpXuaAspRowStatus_Type()
)
cItpXuaAspRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspRowStatus.setStatus("current")


class _CItpXuaAspCongLevel_Type(Unsigned32):
    """Custom type cItpXuaAspCongLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CItpXuaAspCongLevel_Type.__name__ = "Unsigned32"
_CItpXuaAspCongLevel_Object = MibTableColumn
cItpXuaAspCongLevel = _CItpXuaAspCongLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 12),
    _CItpXuaAspCongLevel_Type()
)
cItpXuaAspCongLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspCongLevel.setStatus("current")
_CItpXuaAspAssocIdU32_Type = Unsigned32
_CItpXuaAspAssocIdU32_Object = MibTableColumn
cItpXuaAspAssocIdU32 = _CItpXuaAspAssocIdU32_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 13),
    _CItpXuaAspAssocIdU32_Type()
)
cItpXuaAspAssocIdU32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspAssocIdU32.setStatus("current")
_CItpXuaAspAssocState_Type = CItpXuaAssocState
_CItpXuaAspAssocState_Object = MibTableColumn
cItpXuaAspAssocState = _CItpXuaAspAssocState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 14),
    _CItpXuaAspAssocState_Type()
)
cItpXuaAspAssocState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspAssocState.setStatus("current")


class _CItpXuaAspAssocFailedReason_Type(SnmpAdminString):
    """Custom type cItpXuaAspAssocFailedReason based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_CItpXuaAspAssocFailedReason_Type.__name__ = "SnmpAdminString"
_CItpXuaAspAssocFailedReason_Object = MibTableColumn
cItpXuaAspAssocFailedReason = _CItpXuaAspAssocFailedReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 5, 1, 1, 15),
    _CItpXuaAspAssocFailedReason_Type()
)
cItpXuaAspAssocFailedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspAssocFailedReason.setStatus("current")
_CItpXuaAspRemoteIp_ObjectIdentity = ObjectIdentity
cItpXuaAspRemoteIp = _CItpXuaAspRemoteIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6)
)
_CItpXuaAspRemoteIpTable_Object = MibTable
cItpXuaAspRemoteIpTable = _CItpXuaAspRemoteIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1)
)
if mibBuilder.loadTexts:
    cItpXuaAspRemoteIpTable.setStatus("current")
_CItpXuaAspRemoteIpTableEntry_Object = MibTableRow
cItpXuaAspRemoteIpTableEntry = _CItpXuaAspRemoteIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1, 1)
)
cItpXuaAspRemoteIpTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAspName"),
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAspAddrNum"),
)
if mibBuilder.loadTexts:
    cItpXuaAspRemoteIpTableEntry.setStatus("current")


class _CItpXuaAspAddrNum_Type(Unsigned32):
    """Custom type cItpXuaAspAddrNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CItpXuaAspAddrNum_Type.__name__ = "Unsigned32"
_CItpXuaAspAddrNum_Object = MibTableColumn
cItpXuaAspAddrNum = _CItpXuaAspAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1, 1, 1),
    _CItpXuaAspAddrNum_Type()
)
cItpXuaAspAddrNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaAspAddrNum.setStatus("current")
_CItpXuaAspRemoteIpType_Type = InetAddressType
_CItpXuaAspRemoteIpType_Object = MibTableColumn
cItpXuaAspRemoteIpType = _CItpXuaAspRemoteIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1, 1, 2),
    _CItpXuaAspRemoteIpType_Type()
)
cItpXuaAspRemoteIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspRemoteIpType.setStatus("current")
_CItpXuaAspRemoteIpAddr_Type = InetAddress
_CItpXuaAspRemoteIpAddr_Object = MibTableColumn
cItpXuaAspRemoteIpAddr = _CItpXuaAspRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1, 1, 3),
    _CItpXuaAspRemoteIpAddr_Type()
)
cItpXuaAspRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspRemoteIpAddr.setStatus("current")
_CItpXuaAspRemoteIpRowStatus_Type = RowStatus
_CItpXuaAspRemoteIpRowStatus_Object = MibTableColumn
cItpXuaAspRemoteIpRowStatus = _CItpXuaAspRemoteIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1, 1, 4),
    _CItpXuaAspRemoteIpRowStatus_Type()
)
cItpXuaAspRemoteIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspRemoteIpRowStatus.setStatus("current")
_CItpXuaAspRemoteIpDestState_Type = CItpXuaRemoteIpDestState
_CItpXuaAspRemoteIpDestState_Object = MibTableColumn
cItpXuaAspRemoteIpDestState = _CItpXuaAspRemoteIpDestState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 6, 1, 1, 5),
    _CItpXuaAspRemoteIpDestState_Type()
)
cItpXuaAspRemoteIpDestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspRemoteIpDestState.setStatus("current")
_CItpXuaAspStats_ObjectIdentity = ObjectIdentity
cItpXuaAspStats = _CItpXuaAspStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7)
)
_CItpXuaAspStatsTable_Object = MibTable
cItpXuaAspStatsTable = _CItpXuaAspStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1)
)
if mibBuilder.loadTexts:
    cItpXuaAspStatsTable.setStatus("current")
_CItpXuaAspStatsTableEntry_Object = MibTableRow
cItpXuaAspStatsTableEntry = _CItpXuaAspStatsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1)
)
cItpXuaAspStatsTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAspName"),
)
if mibBuilder.loadTexts:
    cItpXuaAspStatsTableEntry.setStatus("current")
_CItpXuaAspPktsFromAsp_Type = Counter32
_CItpXuaAspPktsFromAsp_Object = MibTableColumn
cItpXuaAspPktsFromAsp = _CItpXuaAspPktsFromAsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 1),
    _CItpXuaAspPktsFromAsp_Type()
)
cItpXuaAspPktsFromAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspPktsFromAsp.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspPktsFromAsp.setUnits("MSUs")
_CItpXuaAspPktsToAsp_Type = Counter32
_CItpXuaAspPktsToAsp_Object = MibTableColumn
cItpXuaAspPktsToAsp = _CItpXuaAspPktsToAsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 2),
    _CItpXuaAspPktsToAsp_Type()
)
cItpXuaAspPktsToAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspPktsToAsp.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspPktsToAsp.setUnits("MSUs")
_CItpXuaAspPktsFromMtp3_Type = Counter32
_CItpXuaAspPktsFromMtp3_Object = MibTableColumn
cItpXuaAspPktsFromMtp3 = _CItpXuaAspPktsFromMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 3),
    _CItpXuaAspPktsFromMtp3_Type()
)
cItpXuaAspPktsFromMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspPktsFromMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspPktsFromMtp3.setUnits("MSUs")
_CItpXuaAspPktsToMtp3_Type = Counter32
_CItpXuaAspPktsToMtp3_Object = MibTableColumn
cItpXuaAspPktsToMtp3 = _CItpXuaAspPktsToMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 4),
    _CItpXuaAspPktsToMtp3_Type()
)
cItpXuaAspPktsToMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspPktsToMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspPktsToMtp3.setUnits("MSUs")
_CItpXuaAspASPUPsRcvd_Type = Counter32
_CItpXuaAspASPUPsRcvd_Object = MibTableColumn
cItpXuaAspASPUPsRcvd = _CItpXuaAspASPUPsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 5),
    _CItpXuaAspASPUPsRcvd_Type()
)
cItpXuaAspASPUPsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPUPsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPUPsRcvd.setUnits("messages")
_CItpXuaAspASPUPACKsSent_Type = Counter32
_CItpXuaAspASPUPACKsSent_Object = MibTableColumn
cItpXuaAspASPUPACKsSent = _CItpXuaAspASPUPACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 6),
    _CItpXuaAspASPUPACKsSent_Type()
)
cItpXuaAspASPUPACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPUPACKsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPUPACKsSent.setUnits("messages")
_CItpXuaAspASPDNsRcvd_Type = Counter32
_CItpXuaAspASPDNsRcvd_Object = MibTableColumn
cItpXuaAspASPDNsRcvd = _CItpXuaAspASPDNsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 7),
    _CItpXuaAspASPDNsRcvd_Type()
)
cItpXuaAspASPDNsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPDNsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPDNsRcvd.setUnits("messages")
_CItpXuaAspASPDNACKsSent_Type = Counter32
_CItpXuaAspASPDNACKsSent_Object = MibTableColumn
cItpXuaAspASPDNACKsSent = _CItpXuaAspASPDNACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 8),
    _CItpXuaAspASPDNACKsSent_Type()
)
cItpXuaAspASPDNACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPDNACKsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPDNACKsSent.setUnits("messages")
_CItpXuaAspASPACsRcvd_Type = Counter32
_CItpXuaAspASPACsRcvd_Object = MibTableColumn
cItpXuaAspASPACsRcvd = _CItpXuaAspASPACsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 9),
    _CItpXuaAspASPACsRcvd_Type()
)
cItpXuaAspASPACsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPACsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPACsRcvd.setUnits("messages")
_CItpXuaAspASPACACKsSent_Type = Counter32
_CItpXuaAspASPACACKsSent_Object = MibTableColumn
cItpXuaAspASPACACKsSent = _CItpXuaAspASPACACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 10),
    _CItpXuaAspASPACACKsSent_Type()
)
cItpXuaAspASPACACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPACACKsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPACACKsSent.setUnits("messages")
_CItpXuaAspASPIAsRcvd_Type = Counter32
_CItpXuaAspASPIAsRcvd_Object = MibTableColumn
cItpXuaAspASPIAsRcvd = _CItpXuaAspASPIAsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 11),
    _CItpXuaAspASPIAsRcvd_Type()
)
cItpXuaAspASPIAsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPIAsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPIAsRcvd.setUnits("messages")
_CItpXuaAspASPIAACKsSent_Type = Counter32
_CItpXuaAspASPIAACKsSent_Object = MibTableColumn
cItpXuaAspASPIAACKsSent = _CItpXuaAspASPIAACKsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 12),
    _CItpXuaAspASPIAACKsSent_Type()
)
cItpXuaAspASPIAACKsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspASPIAACKsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspASPIAACKsSent.setUnits("messages")
_CItpXuaAspErrorsRcvd_Type = Counter32
_CItpXuaAspErrorsRcvd_Object = MibTableColumn
cItpXuaAspErrorsRcvd = _CItpXuaAspErrorsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 13),
    _CItpXuaAspErrorsRcvd_Type()
)
cItpXuaAspErrorsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspErrorsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspErrorsRcvd.setUnits("messages")
_CItpXuaAspErrorsSent_Type = Counter32
_CItpXuaAspErrorsSent_Object = MibTableColumn
cItpXuaAspErrorsSent = _CItpXuaAspErrorsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 14),
    _CItpXuaAspErrorsSent_Type()
)
cItpXuaAspErrorsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspErrorsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspErrorsSent.setUnits("messages")
_CItpXuaAspNotifysSent_Type = Counter32
_CItpXuaAspNotifysSent_Object = MibTableColumn
cItpXuaAspNotifysSent = _CItpXuaAspNotifysSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 15),
    _CItpXuaAspNotifysSent_Type()
)
cItpXuaAspNotifysSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspNotifysSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspNotifysSent.setUnits("messages")
_CItpXuaAspDUNAsRcvd_Type = Counter32
_CItpXuaAspDUNAsRcvd_Object = MibTableColumn
cItpXuaAspDUNAsRcvd = _CItpXuaAspDUNAsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 16),
    _CItpXuaAspDUNAsRcvd_Type()
)
cItpXuaAspDUNAsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDUNAsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDUNAsRcvd.setUnits("messages")
_CItpXuaAspDUNAsSent_Type = Counter32
_CItpXuaAspDUNAsSent_Object = MibTableColumn
cItpXuaAspDUNAsSent = _CItpXuaAspDUNAsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 17),
    _CItpXuaAspDUNAsSent_Type()
)
cItpXuaAspDUNAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDUNAsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDUNAsSent.setUnits("messages")
_CItpXuaAspDAVAsRcvd_Type = Counter32
_CItpXuaAspDAVAsRcvd_Object = MibTableColumn
cItpXuaAspDAVAsRcvd = _CItpXuaAspDAVAsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 18),
    _CItpXuaAspDAVAsRcvd_Type()
)
cItpXuaAspDAVAsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDAVAsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDAVAsRcvd.setUnits("messages")
_CItpXuaAspDAVAsSent_Type = Counter32
_CItpXuaAspDAVAsSent_Object = MibTableColumn
cItpXuaAspDAVAsSent = _CItpXuaAspDAVAsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 19),
    _CItpXuaAspDAVAsSent_Type()
)
cItpXuaAspDAVAsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDAVAsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDAVAsSent.setUnits("messages")
_CItpXuaAspDUPUsRcvd_Type = Counter32
_CItpXuaAspDUPUsRcvd_Object = MibTableColumn
cItpXuaAspDUPUsRcvd = _CItpXuaAspDUPUsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 20),
    _CItpXuaAspDUPUsRcvd_Type()
)
cItpXuaAspDUPUsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDUPUsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDUPUsRcvd.setUnits("messages")
_CItpXuaAspDUPUsSent_Type = Counter32
_CItpXuaAspDUPUsSent_Object = MibTableColumn
cItpXuaAspDUPUsSent = _CItpXuaAspDUPUsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 21),
    _CItpXuaAspDUPUsSent_Type()
)
cItpXuaAspDUPUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDUPUsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDUPUsSent.setUnits("messages")
_CItpXuaAspDAUDsRcvd_Type = Counter32
_CItpXuaAspDAUDsRcvd_Object = MibTableColumn
cItpXuaAspDAUDsRcvd = _CItpXuaAspDAUDsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 22),
    _CItpXuaAspDAUDsRcvd_Type()
)
cItpXuaAspDAUDsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDAUDsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDAUDsRcvd.setUnits("messages")
_CItpXuaAspDAUDsSent_Type = Counter32
_CItpXuaAspDAUDsSent_Object = MibTableColumn
cItpXuaAspDAUDsSent = _CItpXuaAspDAUDsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 23),
    _CItpXuaAspDAUDsSent_Type()
)
cItpXuaAspDAUDsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspDAUDsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspDAUDsSent.setUnits("messages")
_CItpXuaAspSCON0sRcvd_Type = Counter32
_CItpXuaAspSCON0sRcvd_Object = MibTableColumn
cItpXuaAspSCON0sRcvd = _CItpXuaAspSCON0sRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 24),
    _CItpXuaAspSCON0sRcvd_Type()
)
cItpXuaAspSCON0sRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON0sRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON0sRcvd.setUnits("messages")
_CItpXuaAspSCON1sRcvd_Type = Counter32
_CItpXuaAspSCON1sRcvd_Object = MibTableColumn
cItpXuaAspSCON1sRcvd = _CItpXuaAspSCON1sRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 25),
    _CItpXuaAspSCON1sRcvd_Type()
)
cItpXuaAspSCON1sRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON1sRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON1sRcvd.setUnits("messages")
_CItpXuaAspSCON2sRcvd_Type = Counter32
_CItpXuaAspSCON2sRcvd_Object = MibTableColumn
cItpXuaAspSCON2sRcvd = _CItpXuaAspSCON2sRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 26),
    _CItpXuaAspSCON2sRcvd_Type()
)
cItpXuaAspSCON2sRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON2sRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON2sRcvd.setUnits("messages")
_CItpXuaAspSCON3sRcvd_Type = Counter32
_CItpXuaAspSCON3sRcvd_Object = MibTableColumn
cItpXuaAspSCON3sRcvd = _CItpXuaAspSCON3sRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 27),
    _CItpXuaAspSCON3sRcvd_Type()
)
cItpXuaAspSCON3sRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON3sRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON3sRcvd.setUnits("messages")
_CItpXuaAspSCON0sSent_Type = Counter32
_CItpXuaAspSCON0sSent_Object = MibTableColumn
cItpXuaAspSCON0sSent = _CItpXuaAspSCON0sSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 28),
    _CItpXuaAspSCON0sSent_Type()
)
cItpXuaAspSCON0sSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON0sSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON0sSent.setUnits("messages")
_CItpXuaAspSCON1sSent_Type = Counter32
_CItpXuaAspSCON1sSent_Object = MibTableColumn
cItpXuaAspSCON1sSent = _CItpXuaAspSCON1sSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 29),
    _CItpXuaAspSCON1sSent_Type()
)
cItpXuaAspSCON1sSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON1sSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON1sSent.setUnits("messages")
_CItpXuaAspSCON2sSent_Type = Counter32
_CItpXuaAspSCON2sSent_Object = MibTableColumn
cItpXuaAspSCON2sSent = _CItpXuaAspSCON2sSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 30),
    _CItpXuaAspSCON2sSent_Type()
)
cItpXuaAspSCON2sSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON2sSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON2sSent.setUnits("messages")
_CItpXuaAspSCON3sSent_Type = Counter32
_CItpXuaAspSCON3sSent_Object = MibTableColumn
cItpXuaAspSCON3sSent = _CItpXuaAspSCON3sSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 31),
    _CItpXuaAspSCON3sSent_Type()
)
cItpXuaAspSCON3sSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspSCON3sSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspSCON3sSent.setUnits("messages")
_CItpXuaAspBytesFromAsp_Type = Counter64
_CItpXuaAspBytesFromAsp_Object = MibTableColumn
cItpXuaAspBytesFromAsp = _CItpXuaAspBytesFromAsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 32),
    _CItpXuaAspBytesFromAsp_Type()
)
cItpXuaAspBytesFromAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspBytesFromAsp.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspBytesFromAsp.setUnits("Octets")
_CItpXuaAspBytesToAsp_Type = Counter64
_CItpXuaAspBytesToAsp_Object = MibTableColumn
cItpXuaAspBytesToAsp = _CItpXuaAspBytesToAsp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 33),
    _CItpXuaAspBytesToAsp_Type()
)
cItpXuaAspBytesToAsp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspBytesToAsp.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspBytesToAsp.setUnits("Octets")
_CItpXuaAspBytesFromMtp3_Type = Counter64
_CItpXuaAspBytesFromMtp3_Object = MibTableColumn
cItpXuaAspBytesFromMtp3 = _CItpXuaAspBytesFromMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 34),
    _CItpXuaAspBytesFromMtp3_Type()
)
cItpXuaAspBytesFromMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspBytesFromMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspBytesFromMtp3.setUnits("Octets")
_CItpXuaAspBytesToMtp3_Type = Counter64
_CItpXuaAspBytesToMtp3_Object = MibTableColumn
cItpXuaAspBytesToMtp3 = _CItpXuaAspBytesToMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 7, 1, 1, 35),
    _CItpXuaAspBytesToMtp3_Type()
)
cItpXuaAspBytesToMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspBytesToMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAspBytesToMtp3.setUnits("Octets")
_CItpXuaAs_ObjectIdentity = ObjectIdentity
cItpXuaAs = _CItpXuaAs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8)
)
_CItpXuaAsTable_Object = MibTable
cItpXuaAsTable = _CItpXuaAsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1)
)
if mibBuilder.loadTexts:
    cItpXuaAsTable.setStatus("current")
_CItpXuaAsTableEntry_Object = MibTableRow
cItpXuaAsTableEntry = _CItpXuaAsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1)
)
cItpXuaAsTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAsName"),
)
if mibBuilder.loadTexts:
    cItpXuaAsTableEntry.setStatus("current")
_CItpXuaAsName_Type = CItpTcXuaName
_CItpXuaAsName_Object = MibTableColumn
cItpXuaAsName = _CItpXuaAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 1),
    _CItpXuaAsName_Type()
)
cItpXuaAsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaAsName.setStatus("current")
_CItpXuaAsProtocol_Type = CItpXuaProtocol
_CItpXuaAsProtocol_Object = MibTableColumn
cItpXuaAsProtocol = _CItpXuaAsProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 2),
    _CItpXuaAsProtocol_Type()
)
cItpXuaAsProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsProtocol.setStatus("current")


class _CItpXuaAsShut_Type(TruthValue):
    """Custom type cItpXuaAsShut based on TruthValue"""


_CItpXuaAsShut_Object = MibTableColumn
cItpXuaAsShut = _CItpXuaAsShut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 3),
    _CItpXuaAsShut_Type()
)
cItpXuaAsShut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsShut.setStatus("current")
_CItpXuaAsState_Type = CItpXuaAsState
_CItpXuaAsState_Object = MibTableColumn
cItpXuaAsState = _CItpXuaAsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 4),
    _CItpXuaAsState_Type()
)
cItpXuaAsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsState.setStatus("current")
_CItpXuaAsStateOnSgMate_Type = CItpXuaAsState
_CItpXuaAsStateOnSgMate_Object = MibTableColumn
cItpXuaAsStateOnSgMate = _CItpXuaAsStateOnSgMate_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 5),
    _CItpXuaAsStateOnSgMate_Type()
)
cItpXuaAsStateOnSgMate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsStateOnSgMate.setStatus("current")
_CItpXuaAsActiveTS_Type = TimeTicks
_CItpXuaAsActiveTS_Object = MibTableColumn
cItpXuaAsActiveTS = _CItpXuaAsActiveTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 6),
    _CItpXuaAsActiveTS_Type()
)
cItpXuaAsActiveTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsActiveTS.setStatus("current")


class _CItpXuaAsQosClass_Type(CItpTcQos):
    """Custom type cItpXuaAsQosClass based on CItpTcQos"""
    defaultValue = 0


_CItpXuaAsQosClass_Object = MibTableColumn
cItpXuaAsQosClass = _CItpXuaAsQosClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 7),
    _CItpXuaAsQosClass_Type()
)
cItpXuaAsQosClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsQosClass.setStatus("current")
_CItpXuaAsTrafMode_Type = CItpXuaTrafMode
_CItpXuaAsTrafMode_Object = MibTableColumn
cItpXuaAsTrafMode = _CItpXuaAsTrafMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 8),
    _CItpXuaAsTrafMode_Type()
)
cItpXuaAsTrafMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsTrafMode.setStatus("current")
_CItpXuaAsRerouting_Type = TruthValue
_CItpXuaAsRerouting_Object = MibTableColumn
cItpXuaAsRerouting = _CItpXuaAsRerouting_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 9),
    _CItpXuaAsRerouting_Type()
)
cItpXuaAsRerouting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsRerouting.setStatus("current")


class _CItpXuaAsRoutingContext_Type(Unsigned32):
    """Custom type cItpXuaAsRoutingContext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CItpXuaAsRoutingContext_Type.__name__ = "Unsigned32"
_CItpXuaAsRoutingContext_Object = MibTableColumn
cItpXuaAsRoutingContext = _CItpXuaAsRoutingContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 10),
    _CItpXuaAsRoutingContext_Type()
)
cItpXuaAsRoutingContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsRoutingContext.setStatus("current")


class _CItpXuaAsRkParameters_Type(Bits):
    """Custom type cItpXuaAsRkParameters based on Bits"""
    namedValues = NamedValues(
        *(("cic", 6),
          ("dpc", 0),
          ("gtt", 5),
          ("opc", 1),
          ("opcMask", 2),
          ("si", 3),
          ("ssn", 4))
    )

_CItpXuaAsRkParameters_Type.__name__ = "Bits"
_CItpXuaAsRkParameters_Object = MibTableColumn
cItpXuaAsRkParameters = _CItpXuaAsRkParameters_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 11),
    _CItpXuaAsRkParameters_Type()
)
cItpXuaAsRkParameters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkParameters.setStatus("current")
_CItpXuaAsRkDpc_Type = CItpTcPointCode
_CItpXuaAsRkDpc_Object = MibTableColumn
cItpXuaAsRkDpc = _CItpXuaAsRkDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 12),
    _CItpXuaAsRkDpc_Type()
)
cItpXuaAsRkDpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkDpc.setStatus("current")
_CItpXuaAsRkOpc_Type = CItpTcPointCode
_CItpXuaAsRkOpc_Object = MibTableColumn
cItpXuaAsRkOpc = _CItpXuaAsRkOpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 13),
    _CItpXuaAsRkOpc_Type()
)
cItpXuaAsRkOpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkOpc.setStatus("current")
_CItpXuaAsRkOpcMask_Type = Unsigned32
_CItpXuaAsRkOpcMask_Object = MibTableColumn
cItpXuaAsRkOpcMask = _CItpXuaAsRkOpcMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 14),
    _CItpXuaAsRkOpcMask_Type()
)
cItpXuaAsRkOpcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkOpcMask.setStatus("current")
_CItpXuaAsRkSi_Type = CItpTcServiceIndicator
_CItpXuaAsRkSi_Object = MibTableColumn
cItpXuaAsRkSi = _CItpXuaAsRkSi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 15),
    _CItpXuaAsRkSi_Type()
)
cItpXuaAsRkSi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkSi.setStatus("current")
_CItpXuaAsRkSsn_Type = CItpTcSubSystemNumber
_CItpXuaAsRkSsn_Object = MibTableColumn
cItpXuaAsRkSsn = _CItpXuaAsRkSsn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 16),
    _CItpXuaAsRkSsn_Type()
)
cItpXuaAsRkSsn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkSsn.setStatus("current")
_CItpXuaAsRkGtt_Type = TruthValue
_CItpXuaAsRkGtt_Object = MibTableColumn
cItpXuaAsRkGtt = _CItpXuaAsRkGtt_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 17),
    _CItpXuaAsRkGtt_Type()
)
cItpXuaAsRkGtt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkGtt.setStatus("current")


class _CItpXuaAsRkCicMin_Type(Unsigned32):
    """Custom type cItpXuaAsRkCicMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpXuaAsRkCicMin_Type.__name__ = "Unsigned32"
_CItpXuaAsRkCicMin_Object = MibTableColumn
cItpXuaAsRkCicMin = _CItpXuaAsRkCicMin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 18),
    _CItpXuaAsRkCicMin_Type()
)
cItpXuaAsRkCicMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkCicMin.setStatus("current")


class _CItpXuaAsRkCicMax_Type(Unsigned32):
    """Custom type cItpXuaAsRkCicMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CItpXuaAsRkCicMax_Type.__name__ = "Unsigned32"
_CItpXuaAsRkCicMax_Object = MibTableColumn
cItpXuaAsRkCicMax = _CItpXuaAsRkCicMax_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 19),
    _CItpXuaAsRkCicMax_Type()
)
cItpXuaAsRkCicMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRkCicMax.setStatus("current")
_CItpXuaAsPktsFromMtp3_Type = Counter32
_CItpXuaAsPktsFromMtp3_Object = MibTableColumn
cItpXuaAsPktsFromMtp3 = _CItpXuaAsPktsFromMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 20),
    _CItpXuaAsPktsFromMtp3_Type()
)
cItpXuaAsPktsFromMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsPktsFromMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsPktsFromMtp3.setUnits("MSUs")
_CItpXuaAsPktsToASPsOfAs_Type = Counter32
_CItpXuaAsPktsToASPsOfAs_Object = MibTableColumn
cItpXuaAsPktsToASPsOfAs = _CItpXuaAsPktsToASPsOfAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 21),
    _CItpXuaAsPktsToASPsOfAs_Type()
)
cItpXuaAsPktsToASPsOfAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsPktsToASPsOfAs.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsPktsToASPsOfAs.setUnits("MSUs")
_CItpXuaAsRowStatus_Type = RowStatus
_CItpXuaAsRowStatus_Object = MibTableColumn
cItpXuaAsRowStatus = _CItpXuaAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 22),
    _CItpXuaAsRowStatus_Type()
)
cItpXuaAsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsRowStatus.setStatus("current")
_CItpXuaAsNetworkName_Type = CItpTcNetworkName
_CItpXuaAsNetworkName_Object = MibTableColumn
cItpXuaAsNetworkName = _CItpXuaAsNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 23),
    _CItpXuaAsNetworkName_Type()
)
cItpXuaAsNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsNetworkName.setStatus("current")
_CItpXuaAsNetworkAppear_Type = Unsigned32
_CItpXuaAsNetworkAppear_Object = MibTableColumn
cItpXuaAsNetworkAppear = _CItpXuaAsNetworkAppear_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 24),
    _CItpXuaAsNetworkAppear_Type()
)
cItpXuaAsNetworkAppear.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsNetworkAppear.setStatus("current")


class _CItpXuaAsCongLevel_Type(Unsigned32):
    """Custom type cItpXuaAsCongLevel based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CItpXuaAsCongLevel_Type.__name__ = "Unsigned32"
_CItpXuaAsCongLevel_Object = MibTableColumn
cItpXuaAsCongLevel = _CItpXuaAsCongLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 25),
    _CItpXuaAsCongLevel_Type()
)
cItpXuaAsCongLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsCongLevel.setStatus("current")
_CItpXuaAsPktsToMtp3_Type = Counter32
_CItpXuaAsPktsToMtp3_Object = MibTableColumn
cItpXuaAsPktsToMtp3 = _CItpXuaAsPktsToMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 26),
    _CItpXuaAsPktsToMtp3_Type()
)
cItpXuaAsPktsToMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsPktsToMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsPktsToMtp3.setUnits("MSUs")
_CItpXuaAsPktsFromASPsOfAs_Type = Counter32
_CItpXuaAsPktsFromASPsOfAs_Object = MibTableColumn
cItpXuaAsPktsFromASPsOfAs = _CItpXuaAsPktsFromASPsOfAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 27),
    _CItpXuaAsPktsFromASPsOfAs_Type()
)
cItpXuaAsPktsFromASPsOfAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsPktsFromASPsOfAs.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsPktsFromASPsOfAs.setUnits("MSUs")
_CItpXuaAsBytesFromMtp3_Type = Counter64
_CItpXuaAsBytesFromMtp3_Object = MibTableColumn
cItpXuaAsBytesFromMtp3 = _CItpXuaAsBytesFromMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 28),
    _CItpXuaAsBytesFromMtp3_Type()
)
cItpXuaAsBytesFromMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsBytesFromMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsBytesFromMtp3.setUnits("Octets")
_CItpXuaAsBytesToASPsOfAs_Type = Counter64
_CItpXuaAsBytesToASPsOfAs_Object = MibTableColumn
cItpXuaAsBytesToASPsOfAs = _CItpXuaAsBytesToASPsOfAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 29),
    _CItpXuaAsBytesToASPsOfAs_Type()
)
cItpXuaAsBytesToASPsOfAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsBytesToASPsOfAs.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsBytesToASPsOfAs.setUnits("Octets")
_CItpXuaAsBytesToMtp3_Type = Counter64
_CItpXuaAsBytesToMtp3_Object = MibTableColumn
cItpXuaAsBytesToMtp3 = _CItpXuaAsBytesToMtp3_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 30),
    _CItpXuaAsBytesToMtp3_Type()
)
cItpXuaAsBytesToMtp3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsBytesToMtp3.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsBytesToMtp3.setUnits("Octets")
_CItpXuaAsBytesFromASPsOfAs_Type = Counter64
_CItpXuaAsBytesFromASPsOfAs_Object = MibTableColumn
cItpXuaAsBytesFromASPsOfAs = _CItpXuaAsBytesFromASPsOfAs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 8, 1, 1, 31),
    _CItpXuaAsBytesFromASPsOfAs_Type()
)
cItpXuaAsBytesFromASPsOfAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsBytesFromASPsOfAs.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsBytesFromASPsOfAs.setUnits("Octets")
_CItpXuaAspAs_ObjectIdentity = ObjectIdentity
cItpXuaAspAs = _CItpXuaAspAs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9)
)
_CItpXuaAspAsTable_Object = MibTable
cItpXuaAspAsTable = _CItpXuaAspAsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cItpXuaAspAsTable.setStatus("current")
_CItpXuaAspAsTableEntry_Object = MibTableRow
cItpXuaAspAsTableEntry = _CItpXuaAspAsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1, 1)
)
cItpXuaAspAsTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAspName"),
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAspAsName"),
)
if mibBuilder.loadTexts:
    cItpXuaAspAsTableEntry.setStatus("current")
_CItpXuaAspAsName_Type = CItpTcXuaName
_CItpXuaAspAsName_Object = MibTableColumn
cItpXuaAspAsName = _CItpXuaAspAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1, 1, 1),
    _CItpXuaAspAsName_Type()
)
cItpXuaAspAsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaAspAsName.setStatus("current")
_CItpXuaAspAsState_Type = CItpXuaAspState
_CItpXuaAspAsState_Object = MibTableColumn
cItpXuaAspAsState = _CItpXuaAspAsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1, 1, 2),
    _CItpXuaAspAsState_Type()
)
cItpXuaAspAsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspAsState.setStatus("current")
_CItpXuaAspAsActiveTS_Type = TimeTicks
_CItpXuaAspAsActiveTS_Object = MibTableColumn
cItpXuaAspAsActiveTS = _CItpXuaAspAsActiveTS_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1, 1, 3),
    _CItpXuaAspAsActiveTS_Type()
)
cItpXuaAspAsActiveTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAspAsActiveTS.setStatus("current")
_CItpXuaAspAsRowStatus_Type = RowStatus
_CItpXuaAspAsRowStatus_Object = MibTableColumn
cItpXuaAspAsRowStatus = _CItpXuaAspAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1, 1, 4),
    _CItpXuaAspAsRowStatus_Type()
)
cItpXuaAspAsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspAsRowStatus.setStatus("current")


class _CItpXuaAspAsWeight_Type(Unsigned32):
    """Custom type cItpXuaAspAsWeight based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CItpXuaAspAsWeight_Type.__name__ = "Unsigned32"
_CItpXuaAspAsWeight_Object = MibTableColumn
cItpXuaAspAsWeight = _CItpXuaAspAsWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 9, 1, 1, 5),
    _CItpXuaAspAsWeight_Type()
)
cItpXuaAspAsWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAspAsWeight.setStatus("current")
_CItpXuaMIBNotifObjects_ObjectIdentity = ObjectIdentity
cItpXuaMIBNotifObjects = _CItpXuaMIBNotifObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 10)
)
_CItpXuaSgmDisplayName_Type = CItpTcXuaName
_CItpXuaSgmDisplayName_Object = MibScalar
cItpXuaSgmDisplayName = _CItpXuaSgmDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 10, 1),
    _CItpXuaSgmDisplayName_Type()
)
cItpXuaSgmDisplayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cItpXuaSgmDisplayName.setStatus("current")
_CItpXuaAspDisplayName_Type = CItpTcXuaName
_CItpXuaAspDisplayName_Object = MibScalar
cItpXuaAspDisplayName = _CItpXuaAspDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 10, 2),
    _CItpXuaAspDisplayName_Type()
)
cItpXuaAspDisplayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cItpXuaAspDisplayName.setStatus("current")
_CItpXuaAsDisplayName_Type = CItpTcXuaName
_CItpXuaAsDisplayName_Object = MibScalar
cItpXuaAsDisplayName = _CItpXuaAsDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 10, 3),
    _CItpXuaAsDisplayName_Type()
)
cItpXuaAsDisplayName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cItpXuaAsDisplayName.setStatus("current")
_CItpXuaSgmRemoteIp_ObjectIdentity = ObjectIdentity
cItpXuaSgmRemoteIp = _CItpXuaSgmRemoteIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11)
)
_CItpXuaSgmRemoteIpTable_Object = MibTable
cItpXuaSgmRemoteIpTable = _CItpXuaSgmRemoteIpTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1)
)
if mibBuilder.loadTexts:
    cItpXuaSgmRemoteIpTable.setStatus("current")
_CItpXuaSgmRemoteIpTableEntry_Object = MibTableRow
cItpXuaSgmRemoteIpTableEntry = _CItpXuaSgmRemoteIpTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1, 1)
)
cItpXuaSgmRemoteIpTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaSgmName"),
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaSgmAddrNum"),
)
if mibBuilder.loadTexts:
    cItpXuaSgmRemoteIpTableEntry.setStatus("current")


class _CItpXuaSgmAddrNum_Type(Unsigned32):
    """Custom type cItpXuaSgmAddrNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CItpXuaSgmAddrNum_Type.__name__ = "Unsigned32"
_CItpXuaSgmAddrNum_Object = MibTableColumn
cItpXuaSgmAddrNum = _CItpXuaSgmAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1, 1, 1),
    _CItpXuaSgmAddrNum_Type()
)
cItpXuaSgmAddrNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaSgmAddrNum.setStatus("current")
_CItpXuaSgmRemoteIpType_Type = InetAddressType
_CItpXuaSgmRemoteIpType_Object = MibTableColumn
cItpXuaSgmRemoteIpType = _CItpXuaSgmRemoteIpType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1, 1, 2),
    _CItpXuaSgmRemoteIpType_Type()
)
cItpXuaSgmRemoteIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmRemoteIpType.setStatus("current")
_CItpXuaSgmRemoteIpAddr_Type = InetAddress
_CItpXuaSgmRemoteIpAddr_Object = MibTableColumn
cItpXuaSgmRemoteIpAddr = _CItpXuaSgmRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1, 1, 3),
    _CItpXuaSgmRemoteIpAddr_Type()
)
cItpXuaSgmRemoteIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmRemoteIpAddr.setStatus("current")
_CItpXuaSgmRemoteIpRowStatus_Type = RowStatus
_CItpXuaSgmRemoteIpRowStatus_Object = MibTableColumn
cItpXuaSgmRemoteIpRowStatus = _CItpXuaSgmRemoteIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1, 1, 4),
    _CItpXuaSgmRemoteIpRowStatus_Type()
)
cItpXuaSgmRemoteIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaSgmRemoteIpRowStatus.setStatus("current")
_CItpXuaSgmRemoteIpDestState_Type = CItpXuaRemoteIpDestState
_CItpXuaSgmRemoteIpDestState_Object = MibTableColumn
cItpXuaSgmRemoteIpDestState = _CItpXuaSgmRemoteIpDestState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 11, 1, 1, 5),
    _CItpXuaSgmRemoteIpDestState_Type()
)
cItpXuaSgmRemoteIpDestState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaSgmRemoteIpDestState.setStatus("current")
_CItpXuaASRoute_ObjectIdentity = ObjectIdentity
cItpXuaASRoute = _CItpXuaASRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12)
)
_CItpXuaASRouteTable_Object = MibTable
cItpXuaASRouteTable = _CItpXuaASRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1)
)
if mibBuilder.loadTexts:
    cItpXuaASRouteTable.setStatus("current")
_CItpXuaASRouteTableEntry_Object = MibTableRow
cItpXuaASRouteTableEntry = _CItpXuaASRouteTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1)
)
cItpXuaASRouteTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAsrName"),
)
if mibBuilder.loadTexts:
    cItpXuaASRouteTableEntry.setStatus("current")
_CItpXuaAsrName_Type = CItpTcXuaName
_CItpXuaAsrName_Object = MibTableColumn
cItpXuaAsrName = _CItpXuaAsrName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 1),
    _CItpXuaAsrName_Type()
)
cItpXuaAsrName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaAsrName.setStatus("current")
_CItpXuaAsrNetwork_Type = CItpTcNetworkName
_CItpXuaAsrNetwork_Object = MibTableColumn
cItpXuaAsrNetwork = _CItpXuaAsrNetwork_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 2),
    _CItpXuaAsrNetwork_Type()
)
cItpXuaAsrNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrNetwork.setStatus("current")
_CItpXuaAsrProtocol_Type = CItpXuaProtocol
_CItpXuaAsrProtocol_Object = MibTableColumn
cItpXuaAsrProtocol = _CItpXuaAsrProtocol_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 3),
    _CItpXuaAsrProtocol_Type()
)
cItpXuaAsrProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsrProtocol.setStatus("current")


class _CItpXuaAsrRoutingContext_Type(Unsigned32):
    """Custom type cItpXuaAsrRoutingContext based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CItpXuaAsrRoutingContext_Type.__name__ = "Unsigned32"
_CItpXuaAsrRoutingContext_Object = MibTableColumn
cItpXuaAsrRoutingContext = _CItpXuaAsrRoutingContext_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 4),
    _CItpXuaAsrRoutingContext_Type()
)
cItpXuaAsrRoutingContext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrRoutingContext.setStatus("current")
_CItpXuaAsrDpc_Type = CItpTcPointCode
_CItpXuaAsrDpc_Object = MibTableColumn
cItpXuaAsrDpc = _CItpXuaAsrDpc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 5),
    _CItpXuaAsrDpc_Type()
)
cItpXuaAsrDpc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsrDpc.setStatus("current")


class _CItpXuaAsrShut_Type(TruthValue):
    """Custom type cItpXuaAsrShut based on TruthValue"""


_CItpXuaAsrShut_Object = MibTableColumn
cItpXuaAsrShut = _CItpXuaAsrShut_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 6),
    _CItpXuaAsrShut_Type()
)
cItpXuaAsrShut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsrShut.setStatus("current")
_CItpXuaAsrSgmateState_Type = CItpXuaRouteState
_CItpXuaAsrSgmateState_Object = MibTableColumn
cItpXuaAsrSgmateState = _CItpXuaAsrSgmateState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 7),
    _CItpXuaAsrSgmateState_Type()
)
cItpXuaAsrSgmateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateState.setStatus("current")


class _CItpXuaAsrSgmatePriority_Type(Unsigned32):
    """Custom type cItpXuaAsrSgmatePriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CItpXuaAsrSgmatePriority_Type.__name__ = "Unsigned32"
_CItpXuaAsrSgmatePriority_Object = MibTableColumn
cItpXuaAsrSgmatePriority = _CItpXuaAsrSgmatePriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 8),
    _CItpXuaAsrSgmatePriority_Type()
)
cItpXuaAsrSgmatePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmatePriority.setStatus("current")
_CItpXuaAsrOutbPktsRcvd_Type = Counter32
_CItpXuaAsrOutbPktsRcvd_Object = MibTableColumn
cItpXuaAsrOutbPktsRcvd = _CItpXuaAsrOutbPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 9),
    _CItpXuaAsrOutbPktsRcvd_Type()
)
cItpXuaAsrOutbPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbPktsRcvd.setUnits("MSUs")
_CItpXuaAsrOutbByteRcvd_Type = Counter64
_CItpXuaAsrOutbByteRcvd_Object = MibTableColumn
cItpXuaAsrOutbByteRcvd = _CItpXuaAsrOutbByteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 10),
    _CItpXuaAsrOutbByteRcvd_Type()
)
cItpXuaAsrOutbByteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbByteRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbByteRcvd.setUnits("Octets")
_CItpXuaAsrOutbPktsSent_Type = Counter32
_CItpXuaAsrOutbPktsSent_Object = MibTableColumn
cItpXuaAsrOutbPktsSent = _CItpXuaAsrOutbPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 11),
    _CItpXuaAsrOutbPktsSent_Type()
)
cItpXuaAsrOutbPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbPktsSent.setUnits("MSUs")
_CItpXuaAsrOutbByteSent_Type = Counter64
_CItpXuaAsrOutbByteSent_Object = MibTableColumn
cItpXuaAsrOutbByteSent = _CItpXuaAsrOutbByteSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 12),
    _CItpXuaAsrOutbByteSent_Type()
)
cItpXuaAsrOutbByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbByteSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrOutbByteSent.setUnits("Octets")
_CItpXuaAsrSgmateDunaRcvd_Type = Counter32
_CItpXuaAsrSgmateDunaRcvd_Object = MibTableColumn
cItpXuaAsrSgmateDunaRcvd = _CItpXuaAsrSgmateDunaRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 13),
    _CItpXuaAsrSgmateDunaRcvd_Type()
)
cItpXuaAsrSgmateDunaRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateDunaRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateDunaRcvd.setUnits("messages")
_CItpXuaAsrSgmateDavaRcvd_Type = Counter32
_CItpXuaAsrSgmateDavaRcvd_Object = MibTableColumn
cItpXuaAsrSgmateDavaRcvd = _CItpXuaAsrSgmateDavaRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 14),
    _CItpXuaAsrSgmateDavaRcvd_Type()
)
cItpXuaAsrSgmateDavaRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateDavaRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateDavaRcvd.setUnits("messages")
_CItpXuaAsrSgmateDrstRcvd_Type = Counter32
_CItpXuaAsrSgmateDrstRcvd_Object = MibTableColumn
cItpXuaAsrSgmateDrstRcvd = _CItpXuaAsrSgmateDrstRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 15),
    _CItpXuaAsrSgmateDrstRcvd_Type()
)
cItpXuaAsrSgmateDrstRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateDrstRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrSgmateDrstRcvd.setUnits("messages")
_CItpXuaAsrRowStatus_Type = RowStatus
_CItpXuaAsrRowStatus_Object = MibTableColumn
cItpXuaAsrRowStatus = _CItpXuaAsrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 12, 1, 1, 16),
    _CItpXuaAsrRowStatus_Type()
)
cItpXuaAsrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsrRowStatus.setStatus("current")
_CItpXuaASRouteAs_ObjectIdentity = ObjectIdentity
cItpXuaASRouteAs = _CItpXuaASRouteAs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13)
)
_CItpXuaASRouteAsTable_Object = MibTable
cItpXuaASRouteAsTable = _CItpXuaASRouteAsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1)
)
if mibBuilder.loadTexts:
    cItpXuaASRouteAsTable.setStatus("current")
_CItpXuaASRouteAsTableEntry_Object = MibTableRow
cItpXuaASRouteAsTableEntry = _CItpXuaASRouteAsTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1)
)
cItpXuaASRouteAsTableEntry.setIndexNames(
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAsrName"),
    (0, "CISCO-ITP-XUA-MIB", "cItpXuaAsrAsName"),
)
if mibBuilder.loadTexts:
    cItpXuaASRouteAsTableEntry.setStatus("current")
_CItpXuaAsrAsName_Type = CItpTcXuaName
_CItpXuaAsrAsName_Object = MibTableColumn
cItpXuaAsrAsName = _CItpXuaAsrAsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 1),
    _CItpXuaAsrAsName_Type()
)
cItpXuaAsrAsName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cItpXuaAsrAsName.setStatus("current")


class _CItpXuaAsrAsPriority_Type(Unsigned32):
    """Custom type cItpXuaAsrAsPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_CItpXuaAsrAsPriority_Type.__name__ = "Unsigned32"
_CItpXuaAsrAsPriority_Object = MibTableColumn
cItpXuaAsrAsPriority = _CItpXuaAsrAsPriority_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 2),
    _CItpXuaAsrAsPriority_Type()
)
cItpXuaAsrAsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsPriority.setStatus("current")
_CItpXuaAsrAsState_Type = CItpXuaRouteState
_CItpXuaAsrAsState_Object = MibTableColumn
cItpXuaAsrAsState = _CItpXuaAsrAsState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 3),
    _CItpXuaAsrAsState_Type()
)
cItpXuaAsrAsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsState.setStatus("current")
_CItpXuaAsrAsOutbPktsRcvd_Type = Counter32
_CItpXuaAsrAsOutbPktsRcvd_Object = MibTableColumn
cItpXuaAsrAsOutbPktsRcvd = _CItpXuaAsrAsOutbPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 4),
    _CItpXuaAsrAsOutbPktsRcvd_Type()
)
cItpXuaAsrAsOutbPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbPktsRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbPktsRcvd.setUnits("MSUs")
_CItpXuaAsrAsOutbByteRcvd_Type = Counter64
_CItpXuaAsrAsOutbByteRcvd_Object = MibTableColumn
cItpXuaAsrAsOutbByteRcvd = _CItpXuaAsrAsOutbByteRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 5),
    _CItpXuaAsrAsOutbByteRcvd_Type()
)
cItpXuaAsrAsOutbByteRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbByteRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbByteRcvd.setUnits("Octets")
_CItpXuaAsrAsOutbPktsSent_Type = Counter32
_CItpXuaAsrAsOutbPktsSent_Object = MibTableColumn
cItpXuaAsrAsOutbPktsSent = _CItpXuaAsrAsOutbPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 6),
    _CItpXuaAsrAsOutbPktsSent_Type()
)
cItpXuaAsrAsOutbPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbPktsSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbPktsSent.setUnits("MSUs")
_CItpXuaAsrAsOutbByteSent_Type = Counter64
_CItpXuaAsrAsOutbByteSent_Object = MibTableColumn
cItpXuaAsrAsOutbByteSent = _CItpXuaAsrAsOutbByteSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 7),
    _CItpXuaAsrAsOutbByteSent_Type()
)
cItpXuaAsrAsOutbByteSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbByteSent.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsOutbByteSent.setUnits("Octets")
_CItpXuaAsrAsDunaRcvd_Type = Counter32
_CItpXuaAsrAsDunaRcvd_Object = MibTableColumn
cItpXuaAsrAsDunaRcvd = _CItpXuaAsrAsDunaRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 8),
    _CItpXuaAsrAsDunaRcvd_Type()
)
cItpXuaAsrAsDunaRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsDunaRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsDunaRcvd.setUnits("messages")
_CItpXuaAsrAsDavaRcvd_Type = Counter32
_CItpXuaAsrAsDavaRcvd_Object = MibTableColumn
cItpXuaAsrAsDavaRcvd = _CItpXuaAsrAsDavaRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 9),
    _CItpXuaAsrAsDavaRcvd_Type()
)
cItpXuaAsrAsDavaRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsDavaRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsDavaRcvd.setUnits("messages")
_CItpXuaAsrAsDrstRcvd_Type = Counter32
_CItpXuaAsrAsDrstRcvd_Object = MibTableColumn
cItpXuaAsrAsDrstRcvd = _CItpXuaAsrAsDrstRcvd_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 10),
    _CItpXuaAsrAsDrstRcvd_Type()
)
cItpXuaAsrAsDrstRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cItpXuaAsrAsDrstRcvd.setStatus("current")
if mibBuilder.loadTexts:
    cItpXuaAsrAsDrstRcvd.setUnits("messages")
_CItpXuaAsrAsRowStatus_Type = RowStatus
_CItpXuaAsrAsRowStatus_Object = MibTableColumn
cItpXuaAsrAsRowStatus = _CItpXuaAsrAsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 1, 13, 1, 1, 11),
    _CItpXuaAsrAsRowStatus_Type()
)
cItpXuaAsrAsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cItpXuaAsrAsRowStatus.setStatus("current")
_CiscoItpXuaConformance_ObjectIdentity = ObjectIdentity
ciscoItpXuaConformance = _CiscoItpXuaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2)
)
_CiscoItpXuaMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoItpXuaMIBCompliances = _CiscoItpXuaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1)
)
_CiscoItpXuaMIBGroups_ObjectIdentity = ObjectIdentity
ciscoItpXuaMIBGroups = _CiscoItpXuaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2)
)
_CiscoItpXuaSup1Groups_ObjectIdentity = ObjectIdentity
ciscoItpXuaSup1Groups = _CiscoItpXuaSup1Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3)
)

# Managed Objects groups

ciscoItpXuaScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 1)
)
ciscoItpXuaScalarsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaInstConfigLastChanged"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmConfigLastChanged"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspConfigLastChanged"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsConfigLastChanged"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaStateChangeNotifEnabled"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaScalarsGroup.setStatus("current")

ciscoItpXuaInstGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 2)
)
ciscoItpXuaInstGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaInstProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstActiveASPs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaInstGroup.setStatus("deprecated")

ciscoItpXuaInstLocalIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 3)
)
ciscoItpXuaInstLocalIpGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaInstLocalIpType"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstLocalIpAddr"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstLocalIpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaInstLocalIpGroup.setStatus("current")

ciscoItpXuaSgmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 4)
)
ciscoItpXuaSgmGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocId"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmLocalPort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemotePort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmPassive"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmGroup.setStatus("deprecated")

ciscoItpXuaAspGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 5)
)
ciscoItpXuaAspGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocId"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspLocalPort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemotePort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspBlocked"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspIdentifier"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspGroup.setStatus("deprecated")

ciscoItpXuaAspRemoteIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 6)
)
ciscoItpXuaAspRemoteIpGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspRemoteIpType"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemoteIpAddr"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemoteIpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspRemoteIpGroup.setStatus("current")

ciscoItpXuaAspStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 7)
)
ciscoItpXuaAspStatsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspPktsFromAsp"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspPktsToAsp"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspPktsFromMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspPktsToMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPUPsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPUPACKsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPDNsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPDNACKsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPACsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPACACKsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPIAsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspASPIAACKsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspErrorsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspErrorsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspNotifysSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDUNAsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDUNAsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDAVAsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDAVAsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDUPUsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDUPUsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDAUDsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDAUDsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON0sRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON1sRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON2sRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON3sRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON0sSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON1sSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON2sSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspSCON3sSent"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspStatsGroup.setStatus("current")

ciscoItpXuaAsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 8)
)
ciscoItpXuaAsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAsProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsStateOnSgMate"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsTrafMode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRerouting"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRoutingContext"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkParameters"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkDpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkOpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkOpcMask"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkSi"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkSsn"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkGtt"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkCicMin"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkCicMax"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsFromMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsToASPsOfAs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsGroup.setStatus("deprecated")

ciscoItpXuaAspAsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 9)
)
ciscoItpXuaAspAsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspAsState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAsActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspAsGroup.setStatus("deprecated")

ciscoItpXuaNotifObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 10)
)
ciscoItpXuaNotifObjectsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaSgmDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsDisplayName"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaNotifObjectsGroup.setStatus("current")

ciscoItpXuaSgmGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 12)
)
ciscoItpXuaSgmGroupRev1.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocId"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmLocalPort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemotePort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmPassive"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmCongLevel"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmGroupRev1.setStatus("current")

ciscoItpXuaAspGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 13)
)
ciscoItpXuaAspGroupRev1.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocId"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspLocalPort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemotePort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspBlocked"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspIdentifier"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspCongLevel"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspGroupRev1.setStatus("deprecated")

ciscoItpXuaSgmRemoteIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 15)
)
ciscoItpXuaSgmRemoteIpGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemoteIpType"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemoteIpAddr"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemoteIpRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmRemoteIpGroup.setStatus("current")

ciscoItpXuaInstGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 16)
)
ciscoItpXuaInstGroupRev2.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaInstProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstActiveASPs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstOffload"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaInstOffloadSlot"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaInstGroupRev2.setStatus("current")

ciscoItpXuaAspGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 17)
)
ciscoItpXuaAspGroupRev2.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspLocalPort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemotePort"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspBlocked"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspIdentifier"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspCongLevel"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocIdU32"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspGroupRev2.setStatus("current")

ciscoItpXuaAsGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 18)
)
ciscoItpXuaAsGroupRev2.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAsProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsStateOnSgMate"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsTrafMode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRerouting"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRoutingContext"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkParameters"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkDpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkOpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkOpcMask"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkSi"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkSsn"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkGtt"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkCicMin"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkCicMax"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsFromMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsToASPsOfAs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsNetworkName"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsGroupRev2.setStatus("deprecated")

ciscoItpXuaAsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 19)
)
ciscoItpXuaAsGroupRev3.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAsProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsStateOnSgMate"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsQosClass"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsTrafMode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRerouting"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRoutingContext"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkParameters"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkDpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkOpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkOpcMask"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkSi"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkSsn"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkGtt"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkCicMin"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRkCicMax"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsFromMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsToASPsOfAs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsNetworkName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsNetworkAppear"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsCongLevel"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsGroupRev3.setStatus("current")

ciscoItpXuaAspAsGroupRev3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 20)
)
ciscoItpXuaAspAsGroupRev3.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspAsState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAsActiveTS"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAsRowStatus"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAsWeight"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspAsGroupRev3.setStatus("current")

ciscoItpXuaAsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 21)
)
ciscoItpXuaAsrGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAsrNetwork"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrProtocol"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrRoutingContext"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrDpc"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrShut"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrSgmateState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrSgmatePriority"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrOutbPktsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrOutbByteRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrOutbPktsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrOutbByteSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrSgmateDunaRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrSgmateDavaRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrSgmateDrstRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsrGroup.setStatus("current")

ciscoItpXuaAsrAsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 22)
)
ciscoItpXuaAsrAsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsPriority"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsOutbPktsRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsOutbByteRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsOutbPktsSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsOutbByteSent"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsDunaRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsDavaRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsDrstRcvd"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsrAsRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsrAsGroup.setStatus("current")

ciscoItpXuaSgmGroupSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 1)
)
ciscoItpXuaSgmGroupSup1Group.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocFailedReason"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmGroupSup1Group.setStatus("current")

ciscoItpXuaSgmRemoteIpSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 2)
)
ciscoItpXuaSgmRemoteIpSup1Group.setObjects(
    ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemoteIpDestState")
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmRemoteIpSup1Group.setStatus("current")

ciscoItpXuaAspSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 3)
)
ciscoItpXuaAspSup1Group.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocFailedReason"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspSup1Group.setStatus("current")

ciscoItpXuaAspRemoteIpSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 4)
)
ciscoItpXuaAspRemoteIpSup1Group.setObjects(
    ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemoteIpDestState")
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspRemoteIpSup1Group.setStatus("current")

ciscoItpXuaInstGroupSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 6)
)
ciscoItpXuaInstGroupSup1Group.setObjects(
    ("CISCO-ITP-XUA-MIB", "cItpXuaInstOffProcNumber")
)
if mibBuilder.loadTexts:
    ciscoItpXuaInstGroupSup1Group.setStatus("current")

ciscoItpXuaAsSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 7)
)
ciscoItpXuaAsSup1Group.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsToMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsPktsFromASPsOfAs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsBytesFromMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsBytesToASPsOfAs"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsBytesToMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsBytesFromASPsOfAs"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsSup1Group.setStatus("current")

ciscoItpXuaAspStatsSup1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 8)
)
ciscoItpXuaAspStatsSup1Group.setObjects(
      *(("CISCO-ITP-XUA-MIB", "cItpXuaAspBytesFromAsp"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspBytesToAsp"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspBytesFromMtp3"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspBytesToMtp3"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspStatsSup1Group.setStatus("current")


# Notification objects

ciscoItpXuaAspStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 1)
)
ciscoItpXuaAspStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAsState"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspStateChange.setStatus(
        "current"
    )

ciscoItpXuaSgmStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 2)
)
ciscoItpXuaSgmStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmState"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmStateChange.setStatus(
        "current"
    )

ciscoItpXuaAsStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 3)
)
ciscoItpXuaAsStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAsState"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAsStateChange.setStatus(
        "current"
    )

ciscoItpXuaAspCongChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 4)
)
ciscoItpXuaAspCongChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspCongLevel"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspCongChange.setStatus(
        "current"
    )

ciscoItpXuaSgmCongChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 5)
)
ciscoItpXuaSgmCongChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmCongLevel"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmCongChange.setStatus(
        "current"
    )

ciscoItpXuaSgmDestAddrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 6)
)
ciscoItpXuaSgmDestAddrStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocId"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemoteIpAddr"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmRemoteIpDestState"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmDestAddrStateChange.setStatus(
        "current"
    )

ciscoItpXuaAspDestAddrStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 7)
)
ciscoItpXuaAspDestAddrStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocIdU32"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemoteIpAddr"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspRemoteIpDestState"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspDestAddrStateChange.setStatus(
        "current"
    )

ciscoItpXuaAspAssocStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 8)
)
ciscoItpXuaAspAssocStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocIdU32"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaAspAssocFailedReason"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaAspAssocStateChange.setStatus(
        "current"
    )

ciscoItpXuaSgmAssocStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 0, 9)
)
ciscoItpXuaSgmAssocStateChange.setObjects(
      *(("CISCO-ITP-SP-MIB", "cItpSpCLLICode"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmDisplayName"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocId"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocState"),
        ("CISCO-ITP-XUA-MIB", "cItpXuaSgmAssocFailedReason"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaSgmAssocStateChange.setStatus(
        "current"
    )


# Notifications groups

ciscoItpXuaNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 11)
)
ciscoItpXuaNotificationsGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "ciscoItpXuaAspStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaSgmStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaAsStateChange"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaNotificationsGroup.setStatus(
        "deprecated"
    )

ciscoItpXuaNotifGroupRev1 = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 2, 14)
)
ciscoItpXuaNotifGroupRev1.setObjects(
      *(("CISCO-ITP-XUA-MIB", "ciscoItpXuaAspStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaSgmStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaAsStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaAspCongChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaSgmCongChange"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaNotifGroupRev1.setStatus(
        "current"
    )

ciscoItpXuaNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 3, 5)
)
ciscoItpXuaNotifGroup.setObjects(
      *(("CISCO-ITP-XUA-MIB", "ciscoItpXuaSgmDestAddrStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaAspDestAddrStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaAspAssocStateChange"),
        ("CISCO-ITP-XUA-MIB", "ciscoItpXuaSgmAssocStateChange"))
)
if mibBuilder.loadTexts:
    ciscoItpXuaNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoItpXuaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBCompliance.setStatus(
        "deprecated"
    )

ciscoItpXuaMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoItpXuaMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBComplianceRev2.setStatus(
        "deprecated"
    )

ciscoItpXuaMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBComplianceRev3.setStatus(
        "deprecated"
    )

ciscoItpXuaMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 5)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBComplianceRev4.setStatus(
        "deprecated"
    )

ciscoItpXuaMIBComplianceRev5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 6)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBComplianceRev5.setStatus(
        "deprecated"
    )

ciscoItpXuaMIBComplianceRev6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 253, 2, 1, 7)
)
if mibBuilder.loadTexts:
    ciscoItpXuaMIBComplianceRev6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ITP-XUA-MIB",
    **{"CItpXuaProtocol": CItpXuaProtocol,
       "CItpXuaTrafMode": CItpXuaTrafMode,
       "CItpXuaAsState": CItpXuaAsState,
       "CItpXuaAspState": CItpXuaAspState,
       "CItpXuaRouteState": CItpXuaRouteState,
       "CItpXuaAssocState": CItpXuaAssocState,
       "CItpXuaRemoteIpDestState": CItpXuaRemoteIpDestState,
       "ciscoItpXuaMIB": ciscoItpXuaMIB,
       "ciscoItpXuaMIBNotifs": ciscoItpXuaMIBNotifs,
       "ciscoItpXuaAspStateChange": ciscoItpXuaAspStateChange,
       "ciscoItpXuaSgmStateChange": ciscoItpXuaSgmStateChange,
       "ciscoItpXuaAsStateChange": ciscoItpXuaAsStateChange,
       "ciscoItpXuaAspCongChange": ciscoItpXuaAspCongChange,
       "ciscoItpXuaSgmCongChange": ciscoItpXuaSgmCongChange,
       "ciscoItpXuaSgmDestAddrStateChange": ciscoItpXuaSgmDestAddrStateChange,
       "ciscoItpXuaAspDestAddrStateChange": ciscoItpXuaAspDestAddrStateChange,
       "ciscoItpXuaAspAssocStateChange": ciscoItpXuaAspAssocStateChange,
       "ciscoItpXuaSgmAssocStateChange": ciscoItpXuaSgmAssocStateChange,
       "ciscoItpXuaMIBObjects": ciscoItpXuaMIBObjects,
       "cItpXuaScalars": cItpXuaScalars,
       "cItpXuaInstConfigLastChanged": cItpXuaInstConfigLastChanged,
       "cItpXuaSgmConfigLastChanged": cItpXuaSgmConfigLastChanged,
       "cItpXuaAspConfigLastChanged": cItpXuaAspConfigLastChanged,
       "cItpXuaAsConfigLastChanged": cItpXuaAsConfigLastChanged,
       "cItpXuaStateChangeNotifEnabled": cItpXuaStateChangeNotifEnabled,
       "cItpXuaInst": cItpXuaInst,
       "cItpXuaInstTable": cItpXuaInstTable,
       "cItpXuaInstTableEntry": cItpXuaInstTableEntry,
       "cItpXuaInstPort": cItpXuaInstPort,
       "cItpXuaInstProtocol": cItpXuaInstProtocol,
       "cItpXuaInstShut": cItpXuaInstShut,
       "cItpXuaInstActiveASPs": cItpXuaInstActiveASPs,
       "cItpXuaInstRowStatus": cItpXuaInstRowStatus,
       "cItpXuaInstOffload": cItpXuaInstOffload,
       "cItpXuaInstOffloadSlot": cItpXuaInstOffloadSlot,
       "cItpXuaInstOffProcNumber": cItpXuaInstOffProcNumber,
       "cItpXuaInstLocalIp": cItpXuaInstLocalIp,
       "cItpXuaInstLocalIpTable": cItpXuaInstLocalIpTable,
       "cItpXuaInstLocalIpTableEntry": cItpXuaInstLocalIpTableEntry,
       "cItpXuaInstAddrNum": cItpXuaInstAddrNum,
       "cItpXuaInstLocalIpType": cItpXuaInstLocalIpType,
       "cItpXuaInstLocalIpAddr": cItpXuaInstLocalIpAddr,
       "cItpXuaInstLocalIpRowStatus": cItpXuaInstLocalIpRowStatus,
       "cItpXuaSgm": cItpXuaSgm,
       "cItpXuaSgmTable": cItpXuaSgmTable,
       "cItpXuaSgmTableEntry": cItpXuaSgmTableEntry,
       "cItpXuaSgmName": cItpXuaSgmName,
       "cItpXuaSgmAssocId": cItpXuaSgmAssocId,
       "cItpXuaSgmLocalPort": cItpXuaSgmLocalPort,
       "cItpXuaSgmRemotePort": cItpXuaSgmRemotePort,
       "cItpXuaSgmShut": cItpXuaSgmShut,
       "cItpXuaSgmActiveTS": cItpXuaSgmActiveTS,
       "cItpXuaSgmQosClass": cItpXuaSgmQosClass,
       "cItpXuaSgmPassive": cItpXuaSgmPassive,
       "cItpXuaSgmState": cItpXuaSgmState,
       "cItpXuaSgmRowStatus": cItpXuaSgmRowStatus,
       "cItpXuaSgmCongLevel": cItpXuaSgmCongLevel,
       "cItpXuaSgmAssocState": cItpXuaSgmAssocState,
       "cItpXuaSgmAssocFailedReason": cItpXuaSgmAssocFailedReason,
       "cItpXuaAsp": cItpXuaAsp,
       "cItpXuaAspTable": cItpXuaAspTable,
       "cItpXuaAspTableEntry": cItpXuaAspTableEntry,
       "cItpXuaAspName": cItpXuaAspName,
       "cItpXuaAspAssocId": cItpXuaAspAssocId,
       "cItpXuaAspLocalPort": cItpXuaAspLocalPort,
       "cItpXuaAspRemotePort": cItpXuaAspRemotePort,
       "cItpXuaAspProtocol": cItpXuaAspProtocol,
       "cItpXuaAspShut": cItpXuaAspShut,
       "cItpXuaAspBlocked": cItpXuaAspBlocked,
       "cItpXuaAspQosClass": cItpXuaAspQosClass,
       "cItpXuaAspIdentifier": cItpXuaAspIdentifier,
       "cItpXuaAspRowStatus": cItpXuaAspRowStatus,
       "cItpXuaAspCongLevel": cItpXuaAspCongLevel,
       "cItpXuaAspAssocIdU32": cItpXuaAspAssocIdU32,
       "cItpXuaAspAssocState": cItpXuaAspAssocState,
       "cItpXuaAspAssocFailedReason": cItpXuaAspAssocFailedReason,
       "cItpXuaAspRemoteIp": cItpXuaAspRemoteIp,
       "cItpXuaAspRemoteIpTable": cItpXuaAspRemoteIpTable,
       "cItpXuaAspRemoteIpTableEntry": cItpXuaAspRemoteIpTableEntry,
       "cItpXuaAspAddrNum": cItpXuaAspAddrNum,
       "cItpXuaAspRemoteIpType": cItpXuaAspRemoteIpType,
       "cItpXuaAspRemoteIpAddr": cItpXuaAspRemoteIpAddr,
       "cItpXuaAspRemoteIpRowStatus": cItpXuaAspRemoteIpRowStatus,
       "cItpXuaAspRemoteIpDestState": cItpXuaAspRemoteIpDestState,
       "cItpXuaAspStats": cItpXuaAspStats,
       "cItpXuaAspStatsTable": cItpXuaAspStatsTable,
       "cItpXuaAspStatsTableEntry": cItpXuaAspStatsTableEntry,
       "cItpXuaAspPktsFromAsp": cItpXuaAspPktsFromAsp,
       "cItpXuaAspPktsToAsp": cItpXuaAspPktsToAsp,
       "cItpXuaAspPktsFromMtp3": cItpXuaAspPktsFromMtp3,
       "cItpXuaAspPktsToMtp3": cItpXuaAspPktsToMtp3,
       "cItpXuaAspASPUPsRcvd": cItpXuaAspASPUPsRcvd,
       "cItpXuaAspASPUPACKsSent": cItpXuaAspASPUPACKsSent,
       "cItpXuaAspASPDNsRcvd": cItpXuaAspASPDNsRcvd,
       "cItpXuaAspASPDNACKsSent": cItpXuaAspASPDNACKsSent,
       "cItpXuaAspASPACsRcvd": cItpXuaAspASPACsRcvd,
       "cItpXuaAspASPACACKsSent": cItpXuaAspASPACACKsSent,
       "cItpXuaAspASPIAsRcvd": cItpXuaAspASPIAsRcvd,
       "cItpXuaAspASPIAACKsSent": cItpXuaAspASPIAACKsSent,
       "cItpXuaAspErrorsRcvd": cItpXuaAspErrorsRcvd,
       "cItpXuaAspErrorsSent": cItpXuaAspErrorsSent,
       "cItpXuaAspNotifysSent": cItpXuaAspNotifysSent,
       "cItpXuaAspDUNAsRcvd": cItpXuaAspDUNAsRcvd,
       "cItpXuaAspDUNAsSent": cItpXuaAspDUNAsSent,
       "cItpXuaAspDAVAsRcvd": cItpXuaAspDAVAsRcvd,
       "cItpXuaAspDAVAsSent": cItpXuaAspDAVAsSent,
       "cItpXuaAspDUPUsRcvd": cItpXuaAspDUPUsRcvd,
       "cItpXuaAspDUPUsSent": cItpXuaAspDUPUsSent,
       "cItpXuaAspDAUDsRcvd": cItpXuaAspDAUDsRcvd,
       "cItpXuaAspDAUDsSent": cItpXuaAspDAUDsSent,
       "cItpXuaAspSCON0sRcvd": cItpXuaAspSCON0sRcvd,
       "cItpXuaAspSCON1sRcvd": cItpXuaAspSCON1sRcvd,
       "cItpXuaAspSCON2sRcvd": cItpXuaAspSCON2sRcvd,
       "cItpXuaAspSCON3sRcvd": cItpXuaAspSCON3sRcvd,
       "cItpXuaAspSCON0sSent": cItpXuaAspSCON0sSent,
       "cItpXuaAspSCON1sSent": cItpXuaAspSCON1sSent,
       "cItpXuaAspSCON2sSent": cItpXuaAspSCON2sSent,
       "cItpXuaAspSCON3sSent": cItpXuaAspSCON3sSent,
       "cItpXuaAspBytesFromAsp": cItpXuaAspBytesFromAsp,
       "cItpXuaAspBytesToAsp": cItpXuaAspBytesToAsp,
       "cItpXuaAspBytesFromMtp3": cItpXuaAspBytesFromMtp3,
       "cItpXuaAspBytesToMtp3": cItpXuaAspBytesToMtp3,
       "cItpXuaAs": cItpXuaAs,
       "cItpXuaAsTable": cItpXuaAsTable,
       "cItpXuaAsTableEntry": cItpXuaAsTableEntry,
       "cItpXuaAsName": cItpXuaAsName,
       "cItpXuaAsProtocol": cItpXuaAsProtocol,
       "cItpXuaAsShut": cItpXuaAsShut,
       "cItpXuaAsState": cItpXuaAsState,
       "cItpXuaAsStateOnSgMate": cItpXuaAsStateOnSgMate,
       "cItpXuaAsActiveTS": cItpXuaAsActiveTS,
       "cItpXuaAsQosClass": cItpXuaAsQosClass,
       "cItpXuaAsTrafMode": cItpXuaAsTrafMode,
       "cItpXuaAsRerouting": cItpXuaAsRerouting,
       "cItpXuaAsRoutingContext": cItpXuaAsRoutingContext,
       "cItpXuaAsRkParameters": cItpXuaAsRkParameters,
       "cItpXuaAsRkDpc": cItpXuaAsRkDpc,
       "cItpXuaAsRkOpc": cItpXuaAsRkOpc,
       "cItpXuaAsRkOpcMask": cItpXuaAsRkOpcMask,
       "cItpXuaAsRkSi": cItpXuaAsRkSi,
       "cItpXuaAsRkSsn": cItpXuaAsRkSsn,
       "cItpXuaAsRkGtt": cItpXuaAsRkGtt,
       "cItpXuaAsRkCicMin": cItpXuaAsRkCicMin,
       "cItpXuaAsRkCicMax": cItpXuaAsRkCicMax,
       "cItpXuaAsPktsFromMtp3": cItpXuaAsPktsFromMtp3,
       "cItpXuaAsPktsToASPsOfAs": cItpXuaAsPktsToASPsOfAs,
       "cItpXuaAsRowStatus": cItpXuaAsRowStatus,
       "cItpXuaAsNetworkName": cItpXuaAsNetworkName,
       "cItpXuaAsNetworkAppear": cItpXuaAsNetworkAppear,
       "cItpXuaAsCongLevel": cItpXuaAsCongLevel,
       "cItpXuaAsPktsToMtp3": cItpXuaAsPktsToMtp3,
       "cItpXuaAsPktsFromASPsOfAs": cItpXuaAsPktsFromASPsOfAs,
       "cItpXuaAsBytesFromMtp3": cItpXuaAsBytesFromMtp3,
       "cItpXuaAsBytesToASPsOfAs": cItpXuaAsBytesToASPsOfAs,
       "cItpXuaAsBytesToMtp3": cItpXuaAsBytesToMtp3,
       "cItpXuaAsBytesFromASPsOfAs": cItpXuaAsBytesFromASPsOfAs,
       "cItpXuaAspAs": cItpXuaAspAs,
       "cItpXuaAspAsTable": cItpXuaAspAsTable,
       "cItpXuaAspAsTableEntry": cItpXuaAspAsTableEntry,
       "cItpXuaAspAsName": cItpXuaAspAsName,
       "cItpXuaAspAsState": cItpXuaAspAsState,
       "cItpXuaAspAsActiveTS": cItpXuaAspAsActiveTS,
       "cItpXuaAspAsRowStatus": cItpXuaAspAsRowStatus,
       "cItpXuaAspAsWeight": cItpXuaAspAsWeight,
       "cItpXuaMIBNotifObjects": cItpXuaMIBNotifObjects,
       "cItpXuaSgmDisplayName": cItpXuaSgmDisplayName,
       "cItpXuaAspDisplayName": cItpXuaAspDisplayName,
       "cItpXuaAsDisplayName": cItpXuaAsDisplayName,
       "cItpXuaSgmRemoteIp": cItpXuaSgmRemoteIp,
       "cItpXuaSgmRemoteIpTable": cItpXuaSgmRemoteIpTable,
       "cItpXuaSgmRemoteIpTableEntry": cItpXuaSgmRemoteIpTableEntry,
       "cItpXuaSgmAddrNum": cItpXuaSgmAddrNum,
       "cItpXuaSgmRemoteIpType": cItpXuaSgmRemoteIpType,
       "cItpXuaSgmRemoteIpAddr": cItpXuaSgmRemoteIpAddr,
       "cItpXuaSgmRemoteIpRowStatus": cItpXuaSgmRemoteIpRowStatus,
       "cItpXuaSgmRemoteIpDestState": cItpXuaSgmRemoteIpDestState,
       "cItpXuaASRoute": cItpXuaASRoute,
       "cItpXuaASRouteTable": cItpXuaASRouteTable,
       "cItpXuaASRouteTableEntry": cItpXuaASRouteTableEntry,
       "cItpXuaAsrName": cItpXuaAsrName,
       "cItpXuaAsrNetwork": cItpXuaAsrNetwork,
       "cItpXuaAsrProtocol": cItpXuaAsrProtocol,
       "cItpXuaAsrRoutingContext": cItpXuaAsrRoutingContext,
       "cItpXuaAsrDpc": cItpXuaAsrDpc,
       "cItpXuaAsrShut": cItpXuaAsrShut,
       "cItpXuaAsrSgmateState": cItpXuaAsrSgmateState,
       "cItpXuaAsrSgmatePriority": cItpXuaAsrSgmatePriority,
       "cItpXuaAsrOutbPktsRcvd": cItpXuaAsrOutbPktsRcvd,
       "cItpXuaAsrOutbByteRcvd": cItpXuaAsrOutbByteRcvd,
       "cItpXuaAsrOutbPktsSent": cItpXuaAsrOutbPktsSent,
       "cItpXuaAsrOutbByteSent": cItpXuaAsrOutbByteSent,
       "cItpXuaAsrSgmateDunaRcvd": cItpXuaAsrSgmateDunaRcvd,
       "cItpXuaAsrSgmateDavaRcvd": cItpXuaAsrSgmateDavaRcvd,
       "cItpXuaAsrSgmateDrstRcvd": cItpXuaAsrSgmateDrstRcvd,
       "cItpXuaAsrRowStatus": cItpXuaAsrRowStatus,
       "cItpXuaASRouteAs": cItpXuaASRouteAs,
       "cItpXuaASRouteAsTable": cItpXuaASRouteAsTable,
       "cItpXuaASRouteAsTableEntry": cItpXuaASRouteAsTableEntry,
       "cItpXuaAsrAsName": cItpXuaAsrAsName,
       "cItpXuaAsrAsPriority": cItpXuaAsrAsPriority,
       "cItpXuaAsrAsState": cItpXuaAsrAsState,
       "cItpXuaAsrAsOutbPktsRcvd": cItpXuaAsrAsOutbPktsRcvd,
       "cItpXuaAsrAsOutbByteRcvd": cItpXuaAsrAsOutbByteRcvd,
       "cItpXuaAsrAsOutbPktsSent": cItpXuaAsrAsOutbPktsSent,
       "cItpXuaAsrAsOutbByteSent": cItpXuaAsrAsOutbByteSent,
       "cItpXuaAsrAsDunaRcvd": cItpXuaAsrAsDunaRcvd,
       "cItpXuaAsrAsDavaRcvd": cItpXuaAsrAsDavaRcvd,
       "cItpXuaAsrAsDrstRcvd": cItpXuaAsrAsDrstRcvd,
       "cItpXuaAsrAsRowStatus": cItpXuaAsrAsRowStatus,
       "ciscoItpXuaConformance": ciscoItpXuaConformance,
       "ciscoItpXuaMIBCompliances": ciscoItpXuaMIBCompliances,
       "ciscoItpXuaMIBCompliance": ciscoItpXuaMIBCompliance,
       "ciscoItpXuaMIBComplianceRev1": ciscoItpXuaMIBComplianceRev1,
       "ciscoItpXuaMIBComplianceRev2": ciscoItpXuaMIBComplianceRev2,
       "ciscoItpXuaMIBComplianceRev3": ciscoItpXuaMIBComplianceRev3,
       "ciscoItpXuaMIBComplianceRev4": ciscoItpXuaMIBComplianceRev4,
       "ciscoItpXuaMIBComplianceRev5": ciscoItpXuaMIBComplianceRev5,
       "ciscoItpXuaMIBComplianceRev6": ciscoItpXuaMIBComplianceRev6,
       "ciscoItpXuaMIBGroups": ciscoItpXuaMIBGroups,
       "ciscoItpXuaScalarsGroup": ciscoItpXuaScalarsGroup,
       "ciscoItpXuaInstGroup": ciscoItpXuaInstGroup,
       "ciscoItpXuaInstLocalIpGroup": ciscoItpXuaInstLocalIpGroup,
       "ciscoItpXuaSgmGroup": ciscoItpXuaSgmGroup,
       "ciscoItpXuaAspGroup": ciscoItpXuaAspGroup,
       "ciscoItpXuaAspRemoteIpGroup": ciscoItpXuaAspRemoteIpGroup,
       "ciscoItpXuaAspStatsGroup": ciscoItpXuaAspStatsGroup,
       "ciscoItpXuaAsGroup": ciscoItpXuaAsGroup,
       "ciscoItpXuaAspAsGroup": ciscoItpXuaAspAsGroup,
       "ciscoItpXuaNotifObjectsGroup": ciscoItpXuaNotifObjectsGroup,
       "ciscoItpXuaNotificationsGroup": ciscoItpXuaNotificationsGroup,
       "ciscoItpXuaSgmGroupRev1": ciscoItpXuaSgmGroupRev1,
       "ciscoItpXuaAspGroupRev1": ciscoItpXuaAspGroupRev1,
       "ciscoItpXuaNotifGroupRev1": ciscoItpXuaNotifGroupRev1,
       "ciscoItpXuaSgmRemoteIpGroup": ciscoItpXuaSgmRemoteIpGroup,
       "ciscoItpXuaInstGroupRev2": ciscoItpXuaInstGroupRev2,
       "ciscoItpXuaAspGroupRev2": ciscoItpXuaAspGroupRev2,
       "ciscoItpXuaAsGroupRev2": ciscoItpXuaAsGroupRev2,
       "ciscoItpXuaAsGroupRev3": ciscoItpXuaAsGroupRev3,
       "ciscoItpXuaAspAsGroupRev3": ciscoItpXuaAspAsGroupRev3,
       "ciscoItpXuaAsrGroup": ciscoItpXuaAsrGroup,
       "ciscoItpXuaAsrAsGroup": ciscoItpXuaAsrAsGroup,
       "ciscoItpXuaSup1Groups": ciscoItpXuaSup1Groups,
       "ciscoItpXuaSgmGroupSup1Group": ciscoItpXuaSgmGroupSup1Group,
       "ciscoItpXuaSgmRemoteIpSup1Group": ciscoItpXuaSgmRemoteIpSup1Group,
       "ciscoItpXuaAspSup1Group": ciscoItpXuaAspSup1Group,
       "ciscoItpXuaAspRemoteIpSup1Group": ciscoItpXuaAspRemoteIpSup1Group,
       "ciscoItpXuaNotifGroup": ciscoItpXuaNotifGroup,
       "ciscoItpXuaInstGroupSup1Group": ciscoItpXuaInstGroupSup1Group,
       "ciscoItpXuaAsSup1Group": ciscoItpXuaAsSup1Group,
       "ciscoItpXuaAspStatsSup1Group": ciscoItpXuaAspStatsSup1Group}
)
